#!/usr/bin/env python3
"""Ledger bookkeeping for the Proof Pursuit head. Python stdlib only.

  pp.py open P CELL [CELL ...]                       create run/P/ and cell folders
  pp.py task P CELL --role R --regime X --target T   create run/tasks/P-CELL-nnn/ with brief + inbox
  pp.py deadend P CELL --tag T --task ID "approach — why"
  pp.py board CELL [--pts ..] [--tier ..] [--status ..] [--best ..] [--lineages ..] [--next ..] [--time ..]
  pp.py board --note SECTION "text"                 SECTION: gate | decision | obstacle
  pp.py pin P CELL FILE [FILE ...]                   copy into accepted/ and record sha256
  pp.py pin --verify DIR                             re-check a MANIFEST.sha256
  pp.py crosstest CHECKER_A CHECKER_B --gen CMD [--n 200] [--log PATH]
"""
import argparse
import datetime as dt
import hashlib
import os
import re
import shlex
import shutil
import subprocess
import sys
import tempfile

ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), ".."))
RUN = os.path.join(ROOT, "run")
TASKS = os.path.join(RUN, "tasks")
REFERENCE = os.path.join(ROOT, ".claude", "skills", "proof-pursuit-head", "references", "briefs-and-ledger.md")
LESSONS = os.path.join(ROOT, ".claude", "lessons")
VENV_PYTHON = os.path.join(ROOT, ".venv", "bin", "python3")
ROLE_LESSONS_ONLY = {"referee", "checker-builder"}
STATEMENT_RULE = ("Work from the exact statement in TARGET. Preserve every definition, quantifier, parameter range "
                  "and hand-in requirement. Never infer the question from a cell's title.")

ROLES = {
    "scout": {"CLEAN-ROOM"},
    "prover": {"EXPLOIT", "FRESH", "CONTRARIAN"},
    "searcher": {"EXPLOIT", "FRESH", "CONTRARIAN"},
    "breaker": {"FRESH", "CONTRARIAN"},
    "checker-builder": {"CLEAN-ROOM"},
    "referee": {"CLEAN-ROOM"},
    "scribe": {"ACCEPTED-ONLY"},
}
ROLE_HEADINGS = {"checker-builder": "Checker-builder"}
DEFAULT_RULES = ("any computation must be exact or interval arithmetic, code included, runtime < 10 min; "
                 "state exactly what is established")


def die(msg):
    sys.exit(f"pp: {msg}")


def now():
    return dt.datetime.now().strftime("%H:%M")


def run_elapsed():
    start_file = os.path.join(RUN, ".start")
    if not os.path.exists(start_file):
        with open(start_file, "w") as fh:
            fh.write(dt.datetime.now().isoformat())
    with open(start_file) as fh:
        start = dt.datetime.fromisoformat(fh.read().strip())
    mins = int((dt.datetime.now() - start).total_seconds() // 60)
    return f"{mins // 60}:{mins % 60:02d}"


def reference_block(role):
    text = open(REFERENCE).read()
    heading = ROLE_HEADINGS.get(role, role.capitalize())
    m = re.search(r"\*\*" + re.escape(heading) + r"\*\*\n```\n(.*?)```", text, re.S)
    if not m:
        die(f"no brief section for {heading} in {REFERENCE}")
    return m.group(1).rstrip()


def regime_addition(regime):
    text = open(REFERENCE).read()
    m = re.search(r"- " + regime + r": `(.*?)`", text)
    return m.group(1) if m else ""


def cmd_open(a):
    os.makedirs(os.path.join(RUN, a.P), exist_ok=True)
    for name in ("statement.md", "boundary.md"):
        path = os.path.join(RUN, a.P, name)
        if not os.path.exists(path):
            open(path, "w").close()
    for cell in a.cells:
        base = os.path.join(RUN, a.P, cell)
        for sub in ("checker", "lineages", "accepted"):
            os.makedirs(os.path.join(base, sub), exist_ok=True)
        for name in ("target.md", "deadends.md"):
            path = os.path.join(base, name)
            if not os.path.exists(path):
                open(path, "w").close()
    print(f"opened run/{a.P}/ with cells {' '.join(a.cells)}")


def next_task_id(p, cell):
    prefix = f"{p}-{cell}-"
    nums = [int(d[len(prefix):]) for d in os.listdir(TASKS)
            if d.startswith(prefix) and d[len(prefix):].isdigit()] if os.path.isdir(TASKS) else []
    return f"{prefix}{max(nums, default=0) + 1:03d}"


def copy_into(src, dest_dir):
    src_path, _, name = src.partition("=")
    src_path = os.path.realpath(src_path)
    if not os.path.exists(src_path):
        die(f"inbox source not found: {src_path}")
    dest = os.path.join(dest_dir, name or os.path.basename(src_path.rstrip("/")))
    if os.path.isdir(src_path):
        shutil.copytree(src_path, dest)
    else:
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        shutil.copy2(src_path, dest)
    return os.path.relpath(dest, dest_dir)


def lessons_version(path):
    with open(path) as fh:
        m = re.match(r"version:\s*(\S+)", fh.readline().strip())
    return m.group(1) if m else "?"


def copy_lessons(p, role, inbox):
    sources = [(os.path.join(LESSONS, f"{role}.md"), "role-lessons.md")]
    if role not in ROLE_LESSONS_ONLY:
        sources.append((os.path.join(RUN, p, "lessons.md"), "problem-lessons.md"))
    placed = []
    for src, name in sources:
        if os.path.isfile(src):
            shutil.copy2(src, os.path.join(inbox, name))
            placed.append(f"{name} v{lessons_version(src)}")
    return placed


def cmd_task(a):
    role, regime = a.role, a.regime.upper()
    if regime not in ROLES[role]:
        die(f"{role} cannot run under {regime}; allowed: {', '.join(sorted(ROLES[role]))}")
    if regime == "FRESH" and role in ("prover", "searcher") and not a.angle:
        die("a FRESH prover/searcher needs --angle")
    if role == "scribe" and not (a.status and a.cell_status):
        die("a scribe brief needs --status and --cell-status")
    if a.cell_status == "PARTIAL" and not (a.established and a.gap):
        die("a PARTIAL scribe brief needs --established and --gap")
    if regime == "CONTRARIAN" and not (a.forbid or a.forbid_file):
        die("a CONTRARIAN brief needs --forbid or --forbid-file")

    task_id = next_task_id(a.P, a.cell)
    tdir = os.path.join(TASKS, task_id)
    inbox, out = os.path.join(tdir, "inbox"), os.path.join(tdir, "out")
    os.makedirs(inbox)
    os.makedirs(out)
    placed = [copy_into(src, inbox) for src in a.inbox]
    lessons = copy_lessons(a.P, role, inbox)

    rules = "; ".join([DEFAULT_RULES] + a.rules)
    lines = [
        f"TASK: {task_id}      ROLE: {role}      REGIME: {regime}",
        f"TIME BOX: {a.timebox} minutes",
        f"READ ONLY: run/tasks/{task_id}/ (this brief + inbox/). Do not open anything else under run/.",
        f"WRITE ONLY: run/tasks/{task_id}/out/",
        f"TARGET: {a.target}",
        f"STATEMENT RULE: {STATEMENT_RULE}",
        f"ASSUMPTIONS: {a.assumptions}",
        f"STOPPING CONDITION: {a.stop}",
        f"LESSONS: {', '.join(lessons) if lessons else 'none'}",
        f"RULES: {rules}",
        "RETURN: only the report block from your agent instructions, at most 200 words"
        + (" plus a LADDER of at most 10 lines." if role in ("prover", "searcher", "breaker") else "."),
        "        Full work goes in out/.",
        f"INBOX: {', '.join(placed) if placed else '(empty)'}",
        f"PYTHON: {VENV_PYTHON} (sympy, mpmath, networkx, python-flint, python-sat); plain python3 lacks them. "
        "Checkers and anything a judge reruns stay stdlib-only unless the brief says otherwise.",
        "",
        reference_block(role),
    ]
    if regime in ("EXPLOIT", "FRESH", "CONTRARIAN") and role in ("prover", "searcher", "breaker"):
        add = regime_addition(regime)
        if regime == "FRESH":
            add = add.replace("<angle>", a.angle) if a.angle else ""
        if regime == "CONTRARIAN":
            forbidden = list(a.forbid)
            for path in a.forbid_file:
                forbidden += [ln.rstrip() for ln in open(path) if ln.strip()]
            add = "FORBIDDEN APPROACHES (already tried, do not use):\n" + "\n".join(forbidden)
        if add:
            lines += ["", add]
    if role == "scribe":
        lines += ["", f"CELL STATUS: {a.cell_status}", f"CLAIM STATUS (do not upgrade): {a.status}"]
        if a.cell_status == "PARTIAL":
            lines += ["ESTABLISHED: " + "; ".join(a.established), f"REMAINING GAP: {a.gap}"]
    for extra in a.extra:
        lines += ["", extra]
    with open(os.path.join(tdir, "brief.md"), "w") as fh:
        fh.write("\n".join(lines) + "\n")
    print(task_id)
    print(f"dispatch: subagent_type={role}  prompt=\"Your task folder is {tdir}/ . "
          f"Read inbox/role-lessons.md, then inbox/problem-lessons.md if it exists, then brief.md, "
          f"and follow them.\"")


def cmd_deadend(a):
    base = os.path.join(RUN, a.P, a.cell)
    if not os.path.isdir(base):
        die(f"run/{a.P}/{a.cell}/ does not exist; run 'pp.py open' first")
    entry = f"- [{a.tag}] {a.text} ({a.task})\n"
    targets = [os.path.join(base, "deadends.md")]
    if a.lineage:
        ldir = os.path.join(base, "lineages", a.lineage)
        os.makedirs(ldir, exist_ok=True)
        targets.append(os.path.join(ldir, "deadends.md"))
    for path in targets:
        with open(path, "a") as fh:
            fh.write(entry)
    print(entry.rstrip())


BOARD_COLS = ["Cell", "Pts", "Tier", "Cell status", "Claim status", "Best so far", "Live lineages", "Next wave",
              "Time used"]
CELL_STATUSES = ("SOLVED", "PARTIAL", "NOT ATTEMPTED")
NOTE_SECTIONS = {"partial": "## Partial cells: established / remaining gap",
                 "gate": "## Awaiting gate",
                 "lessons": "## Lessons (changes since last checkpoint; pending Referee/Checker-builder lessons)",
                 "decision": "## Decisions for the team",
                 "obstacle": "## Obstacle notes (parked cells)"}


def empty_board():
    header = "| " + " | ".join(BOARD_COLS) + " |\n|" + "|".join("-" * (len(c) + 2) for c in BOARD_COLS) + "|\n"
    return ("# Board: updated --:--, run time 0:00 of 7:00\n\n" + header + "\n"
            + "\n\n".join(NOTE_SECTIONS.values()) + "\n")


def cmd_board(a):
    path = os.path.join(RUN, "board.md")
    text = open(path).read() if os.path.exists(path) else empty_board()
    lines = text.split("\n")
    lines[0] = f"# Board: updated {now()}, run time {run_elapsed()} of 7:00"

    if a.note:
        section, note = a.note
        heading = NOTE_SECTIONS.get(section) or die(f"note section must be one of {', '.join(NOTE_SECTIONS)}")
        i = lines.index(heading) + 1
        while i < len(lines) and lines[i].startswith("- "):
            i += 1
        lines.insert(i, f"- [{now()}] {note}")
    else:
        sep = next(i for i, ln in enumerate(lines) if ln.startswith("|-"))
        end = sep + 1
        while end < len(lines) and lines[end].startswith("|"):
            end += 1
        rows = {}
        for ln in lines[sep + 1:end]:
            cells = [c.strip() for c in ln.strip().strip("|").split("|")]
            rows[cells[0]] = cells + [""] * (len(BOARD_COLS) - len(cells))
        row = rows.get(a.cell, [a.cell] + [""] * (len(BOARD_COLS) - 1))
        for col, val in zip(BOARD_COLS[1:], [a.pts, a.tier, a.cell_status, a.claim_status, a.best, a.lineages,
                                             a.next, a.time]):
            if val is not None:
                row[BOARD_COLS.index(col)] = val.replace("|", "/")
        rows[a.cell] = row
        body = ["| " + " | ".join(r) + " |" for _, r in sorted(rows.items())]
        lines[sep + 1:end] = body
    with open(path, "w") as fh:
        fh.write("\n".join(lines))
    print(f"board updated ({a.cell or a.note[0]})")


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


def cmd_pin(a):
    if a.verify:
        manifest = os.path.join(a.verify, "MANIFEST.sha256")
        bad = 0
        for ln in open(manifest):
            digest, name = ln.rstrip("\n").split("  ", 1)
            actual = sha256(os.path.join(a.verify, name)) if os.path.exists(os.path.join(a.verify, name)) else "missing"
            ok = actual == digest
            bad += not ok
            print(f"{'OK ' if ok else 'BAD'} {name}")
        sys.exit(1 if bad else 0)
    if len(a.args) < 3:
        die("usage: pp.py pin P CELL FILE [FILE ...]")
    p, cell, files = a.args[0], a.args[1], a.args[2:]
    dest = os.path.join(RUN, p, cell, "accepted")
    if not os.path.isdir(dest):
        die(f"{dest} does not exist; run 'pp.py open' first")
    with open(os.path.join(dest, "MANIFEST.sha256"), "a") as man:
        for f in files:
            full = os.path.join(dest, copy_into(f, dest))
            paths = [os.path.join(r, n) for r, _, ns in os.walk(full) for n in ns] if os.path.isdir(full) else [full]
            for path in sorted(paths):
                rel = os.path.relpath(path, dest)
                digest = sha256(path)
                man.write(f"{digest}  {rel}\n")
                print(f"{digest}  {rel}")


def run_checker(checker, artefact):
    cmd = [sys.executable, checker, artefact] if checker.endswith(".py") else shlex.split(checker) + [artefact]
    res = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
    out = (res.stdout.strip().splitlines() or [""])[-1]
    return res.returncode, out


def cmd_crosstest(a):
    log = []
    disagreements = 0
    with tempfile.TemporaryDirectory() as tmp:
        cases = list(a.files)
        for i in range(a.n):
            path = os.path.join(tmp, f"case{i:04d}.txt")
            gen = a.gen.replace("{seed}", str(i))
            with open(path, "w") as fh:
                subprocess.run(gen, shell=True, stdout=fh, check=True)
            cases.append(path)
        for path in cases:
            ra, oa = run_checker(a.checker_a, path)
            rb, ob = run_checker(a.checker_b, path)
            agree = (ra == rb) and (ra != 0 or oa.split()[:2] == ob.split()[:2])
            disagreements += not agree
            name = os.path.basename(path)
            log.append(f"{'AGREE   ' if agree else 'DISAGREE'} {name}: A[{ra}] {oa} | B[{rb}] {ob}")
            if not agree:
                keep = os.path.join(os.path.dirname(a.log) if a.log else ".", "disagree-" + name)
                shutil.copy2(path, keep)
    summary = f"crosstest: {len(cases)} cases, {disagreements} disagreements"
    if a.log:
        with open(a.log, "a") as fh:
            fh.write(f"# {dt.datetime.now().isoformat(timespec='seconds')}\nA={a.checker_a}\nB={a.checker_b}\n"
                     f"gen={a.gen}\n" + "\n".join(log) + f"\n{summary}\n\n")
    print("\n".join(ln for ln in log if ln.startswith("DISAGREE"))[:4000])
    print(summary)
    sys.exit(1 if disagreements else 0)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("open")
    s.add_argument("P")
    s.add_argument("cells", nargs="+")
    s.set_defaults(func=cmd_open)

    s = sub.add_parser("task")
    s.add_argument("P")
    s.add_argument("cell")
    s.add_argument("--role", required=True, choices=sorted(ROLES))
    s.add_argument("--regime", required=True)
    s.add_argument("--target", required=True)
    s.add_argument("--timebox", type=int, default=30)
    s.add_argument("--stop", required=True, help="stopping condition for the worker")
    s.add_argument("--assumptions", default="none beyond the statement")
    s.add_argument("--rules", action="append", default=[], help="extra rule; repeatable")
    s.add_argument("--angle")
    s.add_argument("--forbid", action="append", default=[], help="forbidden-approach line; repeatable")
    s.add_argument("--forbid-file", action="append", default=[], help="deadends.md to inline; repeatable")
    s.add_argument("--inbox", action="append", default=[], help="SRC or SRC=NAME to copy into inbox/; repeatable")
    s.add_argument("--status", help="scribe: the gate-approved claim status")
    s.add_argument("--cell-status", choices=CELL_STATUSES, help="scribe: SOLVED / PARTIAL / NOT ATTEMPTED")
    s.add_argument("--established", action="append", default=[], help="scribe, PARTIAL: established claim; repeatable")
    s.add_argument("--gap", help="scribe, PARTIAL: the exact remaining gap")
    s.add_argument("--extra", action="append", default=[], help="extra paragraph appended to the brief")
    s.set_defaults(func=cmd_task)

    s = sub.add_parser("deadend")
    s.add_argument("P")
    s.add_argument("cell")
    s.add_argument("--tag", required=True)
    s.add_argument("--task", required=True)
    s.add_argument("--lineage")
    s.add_argument("text")
    s.set_defaults(func=cmd_deadend)

    s = sub.add_parser("board")
    s.add_argument("cell", nargs="?")
    for f in ("pts", "tier", "claim-status", "best", "lineages", "next", "time"):
        s.add_argument("--" + f)
    s.add_argument("--cell-status", choices=CELL_STATUSES)
    s.add_argument("--note", nargs=2, metavar=("SECTION", "TEXT"))
    s.set_defaults(func=cmd_board)

    s = sub.add_parser("pin")
    s.add_argument("args", nargs="*")
    s.add_argument("--verify", metavar="DIR")
    s.set_defaults(func=cmd_pin)

    s = sub.add_parser("crosstest")
    s.add_argument("checker_a")
    s.add_argument("checker_b")
    s.add_argument("--gen", required=True, help="shell command printing one artefact; {seed} is substituted")
    s.add_argument("--n", type=int, default=200)
    s.add_argument("--files", nargs="*", default=[], help="extra fixed artefacts to test")
    s.add_argument("--log")
    s.set_defaults(func=cmd_crosstest)

    a = ap.parse_args()
    if a.cmd == "board" and not a.cell and not a.note:
        die("board needs a CELL or --note")
    a.func(a)


if __name__ == "__main__":
    main()
