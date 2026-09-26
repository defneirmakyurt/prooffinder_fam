#!/usr/bin/env python3
"""Ledger bookkeeping for the Proof Pursuit head. Python stdlib only.

  pp.py open P CELL [CELL ...]                 problem + cell folders, checklist template, phases index, lessons
  pp.py task P CELL --phase PH --stop S [--role R] [--regime X] [--mode M] [--branch B [--branch-note T]]
                    [--subject TASK [--subject-file NAME ...]] [--obstacles TASK ...] [--earlier TASK ...]
                    [--record] [--checker DIR]
                    [--target T] [--timebox MIN] [--assumptions A] [--rules R] [--angle A] [--forbid F]
                    [--forbid-file F] [--inbox SRC[=NAME]] [--lib ENTRY] [--status S --cell-status C] [--extra TEXT]
      phases: 0 1 1L 2 2A 2S 2B 2B-XV 2C 3 GATE REPAIR WAVE 5 AUDIT (role, regime and mode follow from the phase)
  pp.py choose P CELL --map TASK --take "S<n>=ACTION: reason" [...]   head's decision on every card of a 2S space map
      ACTION: 2B VERIFIER WAVE DEADEND HOLD DROP → run/P/CELL/spaces.md, branches.txt (kept branches), deadends.md
  pp.py done TASK [--tokens N] [--ms N] [--tool-uses N] [--score S]   telemetry: a worker returned
  pp.py telemetry [--by KEY ...] [--tasks]      yield per role/regime/angle/lessons version/library entry
  pp.py lib add NAME SRC [SRC ...] --kind code|lemma --what T --evidence E   verified material → run/library/<P>-NAME
  pp.py lib list [--branches B ...]             library entries here and on other problem branches
  pp.py lib import BRANCH ENTRY                 copy an entry from another branch, sha256-checked
  pp.py lessons --branches B [B ...]            problem lessons across branches (candidates for role lessons)
  pp.py deadend P CELL --tag T --task ID "approach — why"
  pp.py board CELL [--pts ..] [--tier ..] [--phase ..] [--cell-status ..] [--claim-status ..] [--robustness ..]
                   [--best ..] [--lineages ..] [--next ..] [--time ..]
  pp.py board --note SECTION "text"            SECTION: partial | gate | contested | lessons | decision | obstacle
  pp.py pin P CELL FILE [FILE ...]              copy into accepted/ and record sha256
  pp.py pin --verify DIR                        re-check a MANIFEST.sha256
  pp.py crosstest CHECKER_A CHECKER_B --gen CMD [--n 200] [--log PATH]
  pp.py matrix P CELL                           agreement matrix: ROBUST / CONTESTED / UNSUPPORTED / INCOMPLETE
  pp.py gate P CELL --subject TASK [--statement-checked]   gate report: VALID / GAP / INVALID
  pp.py status P                                per-phase status table + tasks with no 'done' recorded
  pp.py blindcheck TASK                         literature markers in a task's out/
  pp.py report                                  run/<P>/report.md per problem + run/SUMMARY.md from the board
  pp.py finalize P CELL --report TASK --audit TASK   copy final_report.md after an audit PASS
  pp.py summary --branches B [B ...] [--out PATH]    merge run/SUMMARY.md rows across problem branches
"""
import argparse
import collections
import datetime as dt
import hashlib
import itertools
import json
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
TELEMETRY = os.path.join(RUN, "telemetry.jsonl")
LIBRARY = os.path.join(RUN, "library")
NON_PROBLEM_DIRS = {"tasks", "library"}
REFERENCE = os.path.join(ROOT, ".claude", "skills", "proof-pursuit-head", "references", "briefs-and-ledger.md")
LESSONS = os.path.join(ROOT, ".claude", "lessons")
VENV_PYTHON = os.path.join(ROOT, ".venv", "bin", "python3")
ROLE_LESSONS_ONLY = {"referee", "checker-builder", "auditor"}
STATEMENT_RULE = ("Work from the exact statement in TARGET. Preserve every definition, quantifier, parameter range "
                  "and hand-in requirement. Never infer the question from a cell's title.")
DEFAULT_RULES = ("any computation must be exact or interval arithmetic, code included, runtime < 10 min; "
                 "state exactly what is established")

SOLVER_REGIMES = {"BLIND", "FRESH", "CONTRARIAN", "EXPLOIT"}
ROLES = {
    "prover": SOLVER_REGIMES,
    "searcher": SOLVER_REGIMES,
    "breaker": {"BLIND", "FRESH", "CONTRARIAN"},
    "checker-builder": {"CLEAN-ROOM"},
    "referee": {"CLEAN-ROOM"},
    "literature": {"LITERATURE"},
    "triage": {"BLIND"},
    "space": {"BLIND"},
    "scribe": {"RECORD"},
    "auditor": {"RECORD"},
}
ROLE_HEADINGS = {"checker-builder": "Checker-builder"}
# phase: (roles, regime or None = from --regime, fixed mode or None, allowed modes when not fixed)
PHASES = {
    "0": ({"checker-builder"}, "CLEAN-ROOM", None, set()),
    "1": ({"prover", "searcher"}, "BLIND", None, set()),
    "1L": ({"literature"}, "LITERATURE", "SOLVE", set()),
    "2": ({"referee"}, "CLEAN-ROOM", "VERIFY", set()),
    "2A": ({"triage"}, "BLIND", None, set()),
    "2S": ({"space"}, "BLIND", None, set()),
    "2B": ({"prover", "searcher"}, "BLIND", "BRANCH", set()),
    "2B-XV": ({"referee"}, "CLEAN-ROOM", "CROSS", set()),
    "2C": ({"breaker"}, "BLIND", "ADVERSARY", set()),
    "3": ({"literature"}, "LITERATURE", "ANALYST", set()),
    "GATE": ({"referee"}, "CLEAN-ROOM", "GATE", set()),
    "REPAIR": ({"prover", "searcher"}, "EXPLOIT", None, set()),
    "WAVE": ({"prover", "searcher", "breaker"}, None, None, set()),
    "5": ({"scribe"}, "RECORD", None, {"SUBMISSION", "REPORT"}),
    "AUDIT": ({"auditor"}, "RECORD", None, set()),
}
BRANCHES = ("ALGEBRAIC", "TOPOLOGICAL", "ANALYSIS", "NUMBER-THEORY", "DISCRETE", "COMPUTATIONAL")
OBSTACLE_FILES = ("stuck.md", "verdict.md", "no_natural_route.md")
SUBJECT_ITEMS = ("proof.md", "claims.md", "code")
SUBJECT_VERSION_FILES = ("proof.md", "claims.md")
SUBJECT_ARTEFACTS = ("best.txt", "best.json", "best.csv", "best.py", "best.md")
PROCESS_FILES = ("plan.md", "runlog.md", "stuck.md")
CELL_STATUSES = ("SOLVED", "PARTIAL", "COUNTEREXAMPLE", "NOT SOLVED", "NOT ATTEMPTED")
ROBUSTNESS = ("ROBUST", "CONTESTED", "UNSUPPORTED", "INCOMPLETE", "–")
POSITIVE = {"ACCEPT", "CONFIRMED", "CONFIRMED-WITH-CAVEATS"}
NEGATIVE = {"MINOR", "MAJOR", "WRONG", "GAP", "REFUTED"}
PHASE_COLS = ["Task", "Phase", "Role", "Regime", "Mode", "Branch", "Subject", "Created"]
ADVERSARY_LABELS = ("PROOF-ROUTE-FOUND", "COUNTEREXAMPLE-CANDIDATE", "LOCALLY-OPTIMAL-EVIDENCE", "STUCK")
GROUP_KEYS = ("role", "regime", "phase", "angle", "branch", "cell", "lessons", "lib")
LIB_KINDS = ("code", "lemma")
LIB_ROLES = {"prover", "searcher", "breaker"}
CARD_FIELDS = ("SPACE", "BRANCH", "FIDELITY", "FEEDS", "CHECK", "TIGHT", "TOOLS", "COST", "PAYOFF", "LENS", "FIRST TASK")
CHOICE_ACTIONS = {
    "2B": "Phase 2B solver on the card's branch, its LENS as the branch note",
    "VERIFIER": "verifier-only branch: cross-verifies the 2B proofs",
    "WAVE": "FRESH angle for an extra wave (prover, searcher or breaker)",
    "DEADEND": "the card's obstruction goes to deadends.md, so CONTRARIAN briefs inherit it",
    "HOLD": "kept for re-admission if every chosen branch fails",
    "DROP": "not useful for this cell",
}
LIBRARY_NOTE = ("LIBRARY: inbox/library/<entry>/ holds verified material from the shared technique library; its "
                "ENTRY.md says what it is and how it was verified. Use it only if it helps. Copy any library file your "
                "code needs into out/code/ so the code runs on its own, and name the entry in claims.md for every "
                "claim that depends on it. A library lemma is an assumption: state it in full where you use it.")


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


def read(path):
    with open(path) as fh:
        return fh.read()


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


def cell_dir(p, cell):
    return os.path.join(RUN, p, cell)


def task_dir(task):
    return os.path.join(TASKS, task)


def require_cell(p, cell):
    if not os.path.isdir(cell_dir(p, cell)):
        die(f"run/{p}/{cell}/ does not exist; run 'pp.py open' first")


# ---------- reference parsing ----------

def reference_block(heading):
    m = re.search(r"\*\*" + re.escape(heading) + r"\*\*\n```\n(.*?)```", read(REFERENCE), re.S)
    return m.group(1).rstrip() if m else None


def role_heading(role):
    return ROLE_HEADINGS.get(role, role.capitalize())


def regime_addition(regime):
    m = re.search(r"- " + regime + r": `(.*?)`", read(REFERENCE))
    return m.group(1) if m else ""


def branch_lens(branch):
    text = read(REFERENCE)
    if branch == "COMPUTATIONAL":
        m = re.search(r"\*\*COMPUTATIONAL\*\* is an extra lens: (.*)", text)
    else:
        m = re.search(r"- \*\*" + re.escape(branch) + r":\*\* (.*)", text)
    if not m:
        die(f"no lens text for {branch} in {REFERENCE}")
    return m.group(1).strip()


def checklist_template():
    section = read(REFERENCE).split("## 9. Cell checklist", 1)[1]
    m = re.search(r"```\n(.*?)```", section, re.S)
    return m.group(1)


# ---------- phases index ----------

def phases_path(p, cell):
    return os.path.join(cell_dir(p, cell), "phases.md")


def phases_header():
    return ("| " + " | ".join(PHASE_COLS) + " |\n|" + "|".join("-" * (len(c) + 2) for c in PHASE_COLS) + "|\n")


def read_phases(p, cell):
    path = phases_path(p, cell)
    if not os.path.exists(path):
        return []
    rows = []
    for ln in read(path).splitlines():
        cells = [c.strip() for c in ln.strip().strip("|").split("|")]
        if ln.startswith("|") and not ln.startswith("|-") and cells[0] != "Task":
            rows.append(dict(zip(PHASE_COLS, cells)))
    return rows


def append_phase(p, cell, row):
    path = phases_path(p, cell)
    if not os.path.exists(path):
        with open(path, "w") as fh:
            fh.write(phases_header())
    with open(path, "a") as fh:
        fh.write("| " + " | ".join(row[c] for c in PHASE_COLS) + " |\n")


def phase_row(rows, task):
    return next((r for r in rows if r["Task"] == task), None)


# ---------- open ----------

def cmd_open(a):
    os.makedirs(os.path.join(RUN, a.P), exist_ok=True)
    statement = os.path.join(RUN, a.P, "statement.md")
    if not os.path.exists(statement):
        open(statement, "w").close()
    lessons = os.path.join(RUN, a.P, "lessons.md")
    if not os.path.exists(lessons):
        with open(lessons, "w") as fh:
            fh.write(f"version: 0\n# Lessons: problem {a.P}\n\n(no lessons yet)\n")
    for cell in a.cells:
        base = cell_dir(a.P, cell)
        for sub in ("checker", "lineages", "accepted", "gate"):
            os.makedirs(os.path.join(base, sub), exist_ok=True)
        for name in ("target.md", "deadends.md"):
            path = os.path.join(base, name)
            if not os.path.exists(path):
                open(path, "w").close()
        checklist = os.path.join(base, "checklist.md")
        if not os.path.exists(checklist):
            with open(checklist, "w") as fh:
                fh.write(checklist_template().replace("<P>-<cell>", f"{a.P}-{cell}"))
        if not os.path.exists(phases_path(a.P, cell)):
            with open(phases_path(a.P, cell), "w") as fh:
                fh.write(phases_header())
    print(f"opened run/{a.P}/ with cells {' '.join(a.cells)}")


# ---------- task ----------

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
        shutil.copytree(src_path, dest, ignore=shutil.ignore_patterns("tmp"))
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
    placed = {}
    for src, name in sources:
        if os.path.isfile(src):
            shutil.copy2(src, os.path.join(inbox, name))
            placed[name] = lessons_version(src)
    return placed


def split_checklist(p, cell):
    path = os.path.join(cell_dir(p, cell), "checklist.md")
    if not os.path.isfile(path):
        die(f"run/{p}/{cell}/checklist.md is missing; write the checklist first (Phase 0)")
    text = read(path)
    m = re.search(r"^## Part S\b.*$", text, re.M)
    if "## Part G" not in text or not m:
        die(f"run/{p}/{cell}/checklist.md needs '## Part G' and '## Part S' sections")
    return text[:m.start()].rstrip() + "\n", text[m.start():].rstrip() + "\n"


def checklist_items(p, cell):
    text = read(os.path.join(cell_dir(p, cell), "checklist.md"))
    return re.findall(r"^\s*-\s*\**([GS]\d+)\b", text, re.M)


def task_files(task, names):
    out = os.path.join(task_dir(task), "out")
    return [(n, os.path.join(out, n)) for n in names if os.path.exists(os.path.join(out, n))]


def copy_task_outputs(task, names, dest):
    found = task_files(task, names)
    for name, src in found:
        target = os.path.join(dest, name)
        if os.path.isdir(src):
            shutil.copytree(src, target, ignore=shutil.ignore_patterns("tmp"))
        else:
            os.makedirs(dest, exist_ok=True)
            shutil.copy2(src, target)
    return [n for n, _ in found]


def cell_tasks(p, cell):
    prefix = f"{p}-{cell}-"
    return sorted(d for d in os.listdir(TASKS) if d.startswith(prefix)) if os.path.isdir(TASKS) else []


def check_same_cell(p, cell, task, flag):
    if not task.startswith(f"{p}-{cell}-") or not os.path.isdir(task_dir(task)):
        die(f"{flag} {task}: not a task of {p}-{cell}")


def resolve_role_regime_mode(a):
    roles, regime, mode, modes = PHASES[a.phase]
    if len(roles) == 1:
        role = next(iter(roles))
        if a.role and a.role != role:
            die(f"phase {a.phase} runs {role}, not {a.role}")
    else:
        if a.role not in roles:
            die(f"phase {a.phase} needs --role, one of: {', '.join(sorted(roles))}")
        role = a.role
    if regime is None:
        allowed = ROLES[role] & SOLVER_REGIMES
        if not a.regime or a.regime.upper() not in allowed:
            die(f"phase {a.phase} needs --regime for {role}, one of: {', '.join(sorted(allowed))}")
        regime = a.regime.upper()
    elif a.regime and a.regime.upper() != regime:
        die(f"phase {a.phase} runs under {regime}, not {a.regime.upper()}")
    if regime not in ROLES[role]:
        die(f"{role} cannot run under {regime}; allowed: {', '.join(sorted(ROLES[role]))}")
    if modes:
        if a.mode not in modes:
            die(f"phase {a.phase} needs --mode, one of: {', '.join(sorted(modes))}")
        mode = a.mode
    elif a.mode and a.mode != mode:
        die(f"phase {a.phase} runs in mode {mode or '-'}, not {a.mode}")
    return role, regime, mode


def validate_task(a, role, regime, mode, rows):
    if a.branch and a.phase not in ("2B", "2B-XV"):
        die("--branch is only for phases 2B and 2B-XV")
    if a.phase in ("2B", "2B-XV") and not a.branch:
        die(f"phase {a.phase} needs --branch")
    if a.branch == "COMPUTATIONAL" and role != "searcher":
        die("the COMPUTATIONAL lens is for searchers only")
    if a.branch_note and not a.branch:
        die("--branch-note needs --branch")
    needs_subject = role in ("referee", "auditor") or regime == "EXPLOIT"
    if needs_subject and not a.subject:
        die(f"{role} under {regime} needs --subject TASK")
    if a.subject and not needs_subject:
        die(f"--subject is not allowed for {role} under {regime}")
    if a.subject:
        check_same_cell(a.P, a.cell, a.subject, "--subject")
    if a.phase == "2B-XV":
        own = (phase_row(rows, a.subject) or {}).get("Branch", "-")
        if own == a.branch:
            die(f"cross-verifier branch {a.branch} is the subject's own branch; use another branch")
        dup = [r["Task"] for r in rows if r["Phase"] == "2B-XV" and r["Subject"] == a.subject and r["Branch"] == a.branch]
        if dup:
            die(f"{a.subject} already has a {a.branch} cross-verifier ({dup[-1]}); never cross-verify twice from one branch")
        verifiers = [r["Task"] for r in rows if r["Phase"] == "2" and r["Subject"] == a.subject]
        p2 = verdict_of(verifiers[-1]) if verifiers else None
        if p2 in NEGATIVE:
            die(f"the Phase 2 verifier returned {p2} on {a.subject}; repair it first and cross-verify the repaired version")
    if a.phase == "AUDIT":
        row = phase_row(rows, a.subject) or {}
        if row.get("Role") != "scribe" or row.get("Mode") != "REPORT":
            die("the auditor's --subject must be a Scribe REPORT task")
    if a.obstacles and a.phase not in ("2A", "2S", "2C"):
        die("--obstacles is only for phases 2A (triage), 2S (space map) and 2C (adversary)")
    if a.earlier and role != "literature":
        die("--earlier is only for literature tasks (1L, 3)")
    for t in a.earlier:
        check_same_cell(a.P, a.cell, t, "--earlier")
        if a.phase == "1L" and (phase_row(rows, t) or {}).get("Phase") != "1":
            die(f"--earlier {t}: Phase 1L may read only Phase 1 results")
    for t in a.obstacles:
        check_same_cell(a.P, a.cell, t, "--obstacles")
    if a.record and not (mode == "REPORT" or a.phase == "AUDIT"):
        die("--record is only for Scribe REPORT and Auditor tasks")
    if a.checker and role not in ("searcher", "breaker", "referee", "space"):
        die("--checker is only for searchers, breakers, referees and space maps")
    if a.subject_file and role not in ("referee", "prover", "searcher", "breaker"):
        die("--subject-file goes with --subject, on referee and repair tasks")
    for name in a.subject_file:
        if name in PROCESS_FILES:
            die(f"--subject-file {name}: that file says how the work was made; a clean-room reader never sees it")
        if a.subject and not os.path.exists(os.path.join(task_dir(a.subject), "out", name)):
            die(f"--subject-file {name}: {a.subject} has no out/{name}")
    if regime == "BLIND" and a.inbox:
        die("a BLIND inbox accepts only lessons, checklist Part G, obstacles, checker/ and library code; drop --inbox")
    for name in a.lib:
        if role not in LIB_ROLES:
            die("--lib is only for provers, searchers and breakers")
        entry = os.path.join(LIBRARY, name)
        if not os.path.isfile(os.path.join(entry, "ENTRY.md")):
            die(f"run/library/{name} not found; see 'pp.py lib list' and 'pp.py lib import'")
        if regime == "BLIND":
            if verdict_field(read(os.path.join(entry, "ENTRY.md")), "KIND") != "code":
                die(f"{name} is not a code entry; BLIND inboxes take library code only")
            if marker_hits(os.path.join(entry, "files")):
                die(f"{name} has literature markers ('pp.py blindcheck'-style scan); not for a BLIND inbox")
    for src in a.inbox:
        name = os.path.basename(src.partition("=")[0].rstrip("/"))
        if role != "referee" and name.startswith("checklist"):
            die("Part S goes only to referees; pp.py places checklist-G.md itself")
    if regime == "FRESH" and role in ("prover", "searcher") and not a.angle:
        die("a FRESH prover/searcher needs --angle")
    if regime == "CONTRARIAN" and not (a.forbid or a.forbid_file):
        die("a CONTRARIAN brief needs --forbid or --forbid-file")
    if role == "scribe" and not (a.status and a.cell_status):
        die("a scribe brief needs --status and --cell-status")
    if a.cell_status == "PARTIAL" and not (a.established and a.gap):
        die("a PARTIAL scribe brief needs --established and --gap")


def build_inbox(a, role, regime, mode, task_id, inbox):
    placed = []
    for name in ("statement.md",):
        src = os.path.join(RUN, a.P, name)
        if os.path.isfile(src) and os.path.getsize(src):
            shutil.copy2(src, os.path.join(inbox, name))
            placed.append(name)
    target = os.path.join(cell_dir(a.P, a.cell), "target.md")
    if os.path.isfile(target) and os.path.getsize(target):
        shutil.copy2(target, os.path.join(inbox, "target.md"))
        placed.append("target.md")
    if role != "checker-builder":
        part_g, part_s = split_checklist(a.P, a.cell)
        with open(os.path.join(inbox, "checklist-G.md"), "w") as fh:
            fh.write(part_g)
        placed.append("checklist-G.md")
        if role == "referee":
            with open(os.path.join(inbox, "checklist-S.md"), "w") as fh:
                fh.write(f"# Checklist {a.P}-{a.cell}\n\n" + part_s)
            placed.append("checklist-S.md")
    if a.subject and role == "auditor":
        found = copy_task_outputs(a.subject, ["final_report.md"], inbox)
        if not found:
            die(f"{a.subject} has no out/final_report.md")
        placed.append("final_report.md")
    elif a.subject:
        wanted = (*SUBJECT_ITEMS, *SUBJECT_ARTEFACTS, *a.subject_file)
        found = copy_task_outputs(a.subject, wanted, os.path.join(inbox, "subject"))
        if not found:
            die(f"{a.subject} has none of out/{', out/'.join(SUBJECT_ITEMS)}")
        placed.append(f"subject/ ({', '.join(found)} of {a.subject})")
        if regime == "EXPLOIT":
            report = os.path.join(cell_dir(a.P, a.cell), "gate", f"{a.subject}.md")
            if os.path.isfile(report):
                shutil.copy2(report, os.path.join(inbox, "gate_report.md"))
                placed.append("gate_report.md")
    for t in a.obstacles:
        found = copy_task_outputs(t, OBSTACLE_FILES, os.path.join(inbox, "obstacles", t))
        placed.append(f"obstacles/{t}/ ({', '.join(found) or 'nothing found'})")
    if a.checker:
        placed.append(copy_into(f"{a.checker}=checker", inbox))
    for t in a.earlier:
        src = os.path.join(task_dir(t), "out")
        shutil.copytree(src, os.path.join(inbox, "earlier", t), ignore=shutil.ignore_patterns("tmp"))
        placed.append(f"earlier/{t}/")
    if a.phase == "3":
        dest = os.path.join(inbox, "earlier", "cell")
        os.makedirs(dest, exist_ok=True)
        for name in ("matrix.md", "spaces.md", "gate"):
            src = os.path.join(cell_dir(a.P, a.cell), name)
            if os.path.exists(src):
                copy_into(f"{src}={name}", dest)
                placed.append(f"earlier/cell/{name}")
    if mode == "SUBMISSION":
        accepted = os.path.join(cell_dir(a.P, a.cell), "accepted")
        if os.path.isdir(accepted) and os.listdir(accepted):
            placed.append(copy_into(f"{accepted}=accepted", inbox))
    if a.phase == "AUDIT":
        # The auditor must read the report against exactly the record the Scribe wrote it from.
        # A fresh snapshot is taken later and can contradict the report's own citations (the
        # Scribe's copy of phases.md predates its own row; a new copy contains it).
        rec = os.path.join(inbox, "record")
        subj_rec = os.path.join(task_dir(a.subject), "inbox", "record")
        if os.path.isdir(subj_rec):
            shutil.copytree(subj_rec, rec, dirs_exist_ok=True)
        dest = os.path.join(rec, "tasks", a.subject)
        os.makedirs(dest, exist_ok=True)
        for name in ("brief.md",):
            src = os.path.join(task_dir(a.subject), name)
            if os.path.isfile(src):
                shutil.copy2(src, dest)
        out = os.path.join(task_dir(a.subject), "out")
        if os.path.isdir(out):
            shutil.copytree(out, os.path.join(dest, "out"),
                            ignore=shutil.ignore_patterns("tmp"), dirs_exist_ok=True)
        placed.append(f"record/ (the snapshot {a.subject} wrote from, plus its own brief.md and out/)")
    elif a.record or mode == "REPORT":
        rec = os.path.join(inbox, "record")
        for t in cell_tasks(a.P, a.cell):
            if t == task_id:
                continue
            dest = os.path.join(rec, "tasks", t)
            os.makedirs(dest, exist_ok=True)
            if os.path.isfile(os.path.join(task_dir(t), "brief.md")):
                shutil.copy2(os.path.join(task_dir(t), "brief.md"), dest)
            if os.path.isdir(os.path.join(task_dir(t), "out")):
                shutil.copytree(os.path.join(task_dir(t), "out"), os.path.join(dest, "out"),
                                ignore=shutil.ignore_patterns("tmp"))
        cdest = os.path.join(rec, "cell")
        os.makedirs(cdest, exist_ok=True)
        for name in ("target.md", "checklist.md", "phases.md", "spaces.md", "matrix.md", "deadends.md", "gate",
                     "accepted"):
            src = os.path.join(cell_dir(a.P, a.cell), name)
            if os.path.exists(src) and not (os.path.isdir(src) and not os.listdir(src)):
                copy_into(f"{src}={name}", cdest)
        placed.append("record/ (tasks/<id>/brief.md + out/, cell/)")
    for name in a.lib:
        placed.append(copy_into(f"{os.path.join(LIBRARY, name)}=library/{name}", inbox))
    placed += [copy_into(src, inbox) for src in a.inbox]
    return placed


def fill_lens(block, branch, note):
    lens = branch_lens(branch) + (f" Problem note: {note}" if note else "")
    return re.sub(r"<branch> — <[^>]*>", lambda _: f"{branch} — {lens}", block)


def cmd_task(a):
    if a.phase not in PHASES:
        die(f"--phase must be one of {' '.join(PHASES)}")
    require_cell(a.P, a.cell)
    rows = read_phases(a.P, a.cell)
    role, regime, mode = resolve_role_regime_mode(a)
    validate_task(a, role, regime, mode, rows)
    target = a.target
    if not target:
        path = os.path.join(cell_dir(a.P, a.cell), "target.md")
        target = read(path).strip() if os.path.isfile(path) else ""
        if not target:
            die(f"no --target and run/{a.P}/{a.cell}/target.md is empty")

    task_id = next_task_id(a.P, a.cell)
    tdir = task_dir(task_id)
    inbox, out = os.path.join(tdir, "inbox"), os.path.join(tdir, "out")
    os.makedirs(inbox)
    os.makedirs(out)
    versions = copy_lessons(a.P, role, inbox)
    lessons = [f"{name} v{v}" for name, v in versions.items()]
    placed = build_inbox(a, role, regime, mode, task_id, inbox)

    extra_lines = {"prover": "LADDER / RAN", "searcher": "LADDER / RAN", "breaker": "LADDER / RAN",
                   "referee": "CHECKLIST / RAN", "space": "CARDS / RAN"}.get(role, "RAN")
    rules = "; ".join([DEFAULT_RULES] + a.rules)
    lines = [
        f"TASK: {task_id}      ROLE: {role}      REGIME: {regime}",
        f"PHASE: {a.phase}   MODE: {mode or '-'}   BRANCH: {a.branch or '-'}",
        f"SUBJECT: {a.subject or '-'}",
        f"TIME BOX: {a.timebox} minutes",
        f"READ ONLY: run/tasks/{task_id}/ (this brief + inbox/). Do not open anything else under run/.",
        f"WRITE ONLY: run/tasks/{task_id}/out/",
        f"TARGET: {target}",
        f"STATEMENT RULE: {STATEMENT_RULE}",
        f"ASSUMPTIONS: {a.assumptions}",
        f"STOPPING CONDITION: {a.stop}",
        f"LESSONS: {', '.join(lessons) if lessons else 'none'}",
        f"RULES: {rules}",
        f"RETURN: only the report block from your agent instructions, at most 200 words plus {extra_lines} lines.",
        "        Full work goes in out/.",
        f"INBOX: {', '.join(lessons + placed) if lessons or placed else '(empty)'}",
        f"PYTHON: {VENV_PYTHON} (sympy, mpmath, networkx, python-flint, python-sat); plain python3 lacks them.",
        "        Checkers and anything a judge reruns stay stdlib-only unless the brief says otherwise.",
        "",
    ]
    heading = role_heading(role)
    block = reference_block(heading) or die(f"no brief section for {heading} in {REFERENCE}")
    lines.append(block)
    if mode:
        mblock = reference_block(f"{heading}: {mode}")
        if mblock is None and role == "searcher" and mode == "BRANCH":
            mblock = reference_block("Prover: BRANCH")
        if mblock:
            lines += ["", fill_lens(mblock, a.branch, a.branch_note) if a.branch else mblock]
    if role in ("prover", "searcher", "breaker"):
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
    if a.lib:
        lines += ["", LIBRARY_NOTE]
    for extra in a.extra:
        lines += ["", extra]
    with open(os.path.join(tdir, "brief.md"), "w") as fh:
        fh.write("\n".join(lines) + "\n")
    append_phase(a.P, a.cell, {"Task": task_id, "Phase": a.phase, "Role": role, "Regime": regime,
                               "Mode": mode or "-", "Branch": a.branch or "-", "Subject": a.subject or "-",
                               "Created": now()})
    log_event("task", task=task_id, cell=f"{a.P}-{a.cell}", phase=a.phase, role=role, regime=regime,
              mode=mode or "-", branch=a.branch or "-", subject=a.subject or "-", angle=a.angle or "-",
              lessons={"role": versions.get("role-lessons.md", "-"),
                       "problem": versions.get("problem-lessons.md", "-")},
              lib=a.lib, timebox=a.timebox)
    print(task_id)
    print(f"dispatch: subagent_type={role}  prompt=\"Your task folder is {tdir}/ . "
          f"Read inbox/role-lessons.md, then inbox/problem-lessons.md if it exists, then brief.md, "
          f"and follow them.\"")


# ---------- dead ends ----------

def cmd_deadend(a):
    base = cell_dir(a.P, a.cell)
    require_cell(a.P, a.cell)
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


# ---------- space map choice (Phase 2S) ----------

def parse_cards(path):
    """Cards in a space map's out/spaces.md: '### S<n> <tag>' then 'FIELD: value' lines (first one of each counts)."""
    cards, cur = {}, None
    for ln in read(path).splitlines():
        m = re.match(r"#{2,4}\s+(S\d+)\b[\s:—-]*(.*)", ln)
        if m:
            cur = cards.setdefault(m.group(1), {"tag": m.group(2).strip() or m.group(1)})
            continue
        f = re.match(r"\s*[*_]*([A-Z][A-Z ]*[A-Z])[*_]*:\s*(.*)", ln) if cur is not None else None
        if f and f.group(1) in CARD_FIELDS and f.group(1) not in cur:
            cur[f.group(1)] = f.group(2).strip()
    return cards


def card_word(card, field):
    m = re.match(r"[*_`\s]*([A-Za-z][A-Za-z/-]*)", card.get(field, ""))
    return m.group(1).upper() if m else ""


def text_markers(text):
    return [label for label, pat in BLIND_MARKERS if pat.search(text)]


def cmd_choose(a):
    require_cell(a.P, a.cell)
    row = phase_row(read_phases(a.P, a.cell), a.map)
    if not row or row["Phase"] != "2S":
        die(f"--map {a.map}: not a Phase 2S task of {a.P}-{a.cell}")
    path = os.path.join(task_dir(a.map), "out", "spaces.md")
    if not os.path.isfile(path):
        die(f"{a.map} has no out/spaces.md")
    cards = parse_cards(path)
    if not cards:
        die(f"{a.map}: no '### S<n> <tag>' cards in out/spaces.md")

    decisions = {}
    for take in a.take:
        m = re.match(r"\s*(S\d+)\s*=\s*([A-Z0-9]+)\s*:\s*(\S.*)", take)
        if not m:
            die(f"--take '{take}': use 'S<n>=ACTION: reason'; the reason is required")
        cid, action, reason = m.groups()
        if cid not in cards:
            die(f"--take {cid}: {a.map} has no card {cid}")
        if action not in CHOICE_ACTIONS:
            die(f"--take {cid}: ACTION must be one of {' '.join(CHOICE_ACTIONS)}")
        if cid in decisions:
            die(f"{cid} has two decisions")
        decisions[cid] = (action, reason.strip().replace("|", "/"))
    missing = [c for c in cards if c not in decisions]
    if missing:
        die(f"decide every card of the map; missing: {', '.join(missing)}")

    kept = {}
    for cid, (action, _) in decisions.items():
        card = cards[cid]
        branch, check, tight = card_word(card, "BRANCH"), card_word(card, "CHECK"), card_word(card, "TIGHT")
        if action in ("2B", "VERIFIER"):
            if branch not in BRANCHES or branch == "COMPUTATIONAL":
                die(f"{cid}: {action} needs BRANCH to be one of the five branches, not '{card.get('BRANCH', '')}'; "
                    "a search-only card goes to WAVE")
            if branch in kept:
                die(f"{cid}: branch {branch} is already taken by another card; one card per branch "
                    "(send the other to WAVE)")
            if check == "FAILED":
                die(f"{cid}: CHECK FAILED; a failed translation is dead (DEADEND or DROP)")
            kept[branch] = "solver" if action == "2B" else "verifier-only"
        if action == "2B":
            lacking = [f for f in CARD_FIELDS if not card.get(f)]
            if lacking:
                die(f"{cid}: the card lacks {', '.join(lacking)}")
            if check != "PASSED":
                die(f"{cid}: 2B needs CHECK PASSED (card: '{card['CHECK']}'); an unchecked card goes to WAVE at most")
            if card_word(card, "FIDELITY") == "HEURISTIC":
                die(f"{cid}: a HEURISTIC translation cannot carry a proof; send it to WAVE")
            if tight == "NO":
                die(f"{cid}: TIGHT NO; a relaxation that is not tight cannot carry an exact proof "
                    "(WAVE for a bound-only task, or DEADEND)")
        if action == "WAVE" and check == "FAILED":
            die(f"{cid}: CHECK FAILED; a failed translation is dead (DEADEND or DROP)")
        if action in ("2B", "VERIFIER", "WAVE"):
            if not card.get("LENS"):
                die(f"{cid}: no LENS line; nothing blind-safe to hand a worker")
            hits = text_markers(card["LENS"])
            if hits:
                die(f"{cid}: LENS has literature markers ({', '.join(hits)}); it would go into blind briefs")
        if action == "DEADEND" and not (tight == "NO" or check == "FAILED"):
            die(f"{cid}: DEADEND needs TIGHT NO or CHECK FAILED on the card, i.e. an obstruction to record")
    if "solver" in kept.values() and len(kept) < 2:
        die("a 2B proof needs another kept branch to cross-verify it; choose a second 2B card or a VERIFIER")

    base, stamp = cell_dir(a.P, a.cell), now()
    choice = os.path.join(base, "branches.txt")
    if kept:
        with open(choice, "w") as fh:
            fh.write(f"# head choice from {a.map}, {stamp} (pp.py choose)\n")
            fh.write("".join(f"{b}\t{k}\n" for b, k in kept.items()))
    elif os.path.isfile(choice):
        os.remove(choice)
    for cid, (action, _) in decisions.items():
        if action == "DEADEND":
            card = cards[cid]
            why = card["TIGHT"] if card_word(card, "TIGHT") == "NO" else card["CHECK"]
            with open(os.path.join(base, "deadends.md"), "a") as fh:
                fh.write(f"- [{card['tag']}] {card.get('SPACE', cid)} — {why} ({a.map} {cid})\n")

    record = os.path.join(base, "spaces.md")
    lines = [] if os.path.isfile(record) else [f"# Space choices: {a.P}-{a.cell}", ""]
    lines += [f"## {stamp}, map {a.map}", "",
              "| Card | Tag | Branch | Fidelity | Check | Tight | Cost | Payoff | Decision | Reason |",
              "|---|---|---|---|---|---|---|---|---|---|"]
    for cid, card in cards.items():
        action, reason = decisions[cid]
        vals = [card_word(card, f) or "?" for f in ("BRANCH", "FIDELITY", "CHECK", "TIGHT", "COST", "PAYOFF")]
        lines.append(f"| {cid} | {card['tag']} | " + " | ".join(vals) + f" | {action} | {reason} |")
    lines += ["", "Kept branches: " + (", ".join(f"{b} {k}" for b, k in kept.items())
                                       or "none (the matrix falls back to the latest 2A triage)"), "",
              "Lenses handed to workers (2B: --branch-note; WAVE: --angle):"]
    lines += [f"- {cid} {decisions[cid][0]} [{cards[cid]['tag']}]: {cards[cid]['LENS']}"
              for cid in cards if decisions[cid][0] in ("2B", "VERIFIER", "WAVE")] or ["- none"]
    with open(record, "a") as fh:
        fh.write("\n".join(lines) + "\n\n")
    log_event("choose", cell=f"{a.P}-{a.cell}", map=a.map, kept=kept,
              decisions={cid: d[0] for cid, d in decisions.items()})

    print(f"{a.P}-{a.cell}: " + ", ".join(f"{cid} {d[0]}" for cid, d in decisions.items()))
    print("kept branches: " + (", ".join(f"{b} {k}" for b, k in kept.items()) or "none"))
    for cid, (action, _) in decisions.items():
        card = cards[cid]
        first = card_word(card, "FIRST TASK").lower()
        if action == "2B":
            role = first if first in ("prover", "searcher") else "prover"
            print(f"next: pp.py task {a.P} {a.cell} --phase 2B --role {role} --branch {card_word(card, 'BRANCH')} "
                  f"--angle {shlex.quote(card['tag'])} --branch-note {shlex.quote(card['LENS'])} --stop ...")
        elif action == "WAVE":
            role = first if first in ("prover", "searcher", "breaker") else "prover"
            print(f"later: pp.py task {a.P} {a.cell} --phase WAVE --role {role} --regime FRESH "
                  f"--angle {shlex.quote(card['tag'] + ': ' + card['LENS'])} --stop ...")


# ---------- board ----------

BOARD_COLS = ["Cell", "Pts", "Tier", "Phase", "Cell status", "Claim status", "Robustness", "Best so far",
              "Live lineages", "Next", "Time used"]
NOTE_SECTIONS = {"partial": "## Partial cells: established / remaining gap",
                 "gate": "## Awaiting gate",
                 "contested": "## Contested cells (tell the humans)",
                 "lessons": "## Lessons (changes since last checkpoint; pending Referee/Checker-builder/Auditor lessons)",
                 "decision": "## Decisions for the team",
                 "obstacle": "## Obstacle notes (parked cells)"}
NOTE_PREFIXES = {"partial": "## Partial cells", "gate": "## Awaiting gate", "contested": "## Contested",
                 "lessons": "## Lessons", "decision": "## Decisions", "obstacle": "## Obstacle notes"}
BOARD_FLAGS = {"Pts": "pts", "Tier": "tier", "Phase": "phase", "Cell status": "cell_status",
               "Claim status": "claim_status", "Robustness": "robustness", "Best so far": "best",
               "Live lineages": "lineages", "Next": "next", "Time used": "time"}


def problem_letter():
    path = os.path.join(RUN, "PROBLEM")
    return read(path).split()[0] if os.path.isfile(path) and read(path).split() else "?"


def parse_board(text):
    rows, notes, header, current = {}, {k: [] for k in NOTE_SECTIONS}, None, None
    for ln in text.split("\n"):
        if ln.startswith("## "):
            current = next((k for k, pre in NOTE_PREFIXES.items() if ln.startswith(pre)), None)
        elif ln.startswith("|") and not ln.startswith("|-"):
            cells = [c.strip() for c in ln.strip().strip("|").split("|")]
            if cells[0] == "Cell":
                header = ["Next" if c == "Next wave" else c for c in cells]
            elif header:
                rows[cells[0]] = dict(zip(header, cells))
        elif current and ln.startswith("- "):
            notes[current].append(ln)
    return rows, notes


def render_board(rows, notes):
    out = [f"# Board: problem {problem_letter()}, updated {now()}, run time {run_elapsed()} of 7:00", "",
           "| " + " | ".join(BOARD_COLS) + " |", "|" + "|".join("-" * (len(c) + 2) for c in BOARD_COLS) + "|"]
    for cell in sorted(rows):
        out.append("| " + " | ".join(rows[cell].get(c, "") for c in BOARD_COLS) + " |")
    for key, heading in NOTE_SECTIONS.items():
        out += ["", heading] + notes.get(key, [])
    return "\n".join(out) + "\n"


def board_state():
    path = os.path.join(RUN, "board.md")
    return parse_board(read(path)) if os.path.exists(path) else ({}, {k: [] for k in NOTE_SECTIONS})


def cmd_board(a):
    rows, notes = board_state()
    if a.note:
        section, note = a.note
        if section not in NOTE_SECTIONS:
            die(f"note section must be one of {', '.join(NOTE_SECTIONS)}")
        notes[section].append(f"- [{now()}] {note}")
    elif a.cell:
        row = rows.setdefault(a.cell, {"Cell": a.cell})
        for col, flag in BOARD_FLAGS.items():
            val = getattr(a, flag)
            if val is not None:
                row[col] = val.replace("|", "/")
    with open(os.path.join(RUN, "board.md"), "w") as fh:
        fh.write(render_board(rows, notes))
    print(f"board updated ({a.cell or (a.note[0] if a.note else 'regenerated')})")


# ---------- pin / crosstest ----------

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
    dest = os.path.join(cell_dir(p, cell), "accepted")
    if not os.path.isdir(dest):
        die(f"{dest} does not exist; run 'pp.py open' first")
    with open(os.path.join(dest, "MANIFEST.sha256"), "a") as man:
        for f in files:
            from_task = os.path.relpath(os.path.realpath(f.partition("=")[0]), TASKS)
            if not from_task.startswith(".."):
                log_event("pin", task=from_task.split(os.sep)[0], cell=f"{p}-{cell}")
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


# ---------- verdicts, matrix, gate ----------

def verdict_text(task):
    path = os.path.join(task_dir(task), "out", "verdict.md")
    return read(path) if os.path.isfile(path) else ""


def verdict_field(text, field):
    for ln in text.splitlines():
        m = re.match(r"^[\s>#*_-]*" + field + r"[*_]*\s*:[*_]*\s*(.*)$", ln)
        if m:
            return m.group(1).strip()
    return None


def verdict_of(task, cross=False):
    value = verdict_field(verdict_text(task), "CROSS VERDICT" if cross else "VERDICT")
    if not value:
        return None
    m = re.match(r"[*_]*([A-Z][A-Z-]*)", value)
    return m.group(1) if m else None


def selected_branches(p, cell, rows):
    """Kept branches: the head's choice from a 2S space map (branches.txt) wins; else the latest 2A triage."""
    choice = os.path.join(cell_dir(p, cell), "branches.txt")
    if os.path.isfile(choice):
        source, path = "head choice, branches.txt", choice
    else:
        triage = [r["Task"] for r in rows if r["Phase"] == "2A"]
        if not triage:
            return None, {}
        source, path = triage[-1], os.path.join(task_dir(triage[-1]), "out", "selected_branches.txt")
    kept = {}
    if os.path.isfile(path):
        for ln in read(path).splitlines():
            parts = ln.split()
            if len(parts) >= 2 and parts[0] in BRANCHES:
                kept[parts[0]] = parts[1]
    return source, kept


def compute_matrix(p, cell):
    rows = read_phases(p, cell)
    triage, kept = selected_branches(p, cell, rows)
    if not triage:
        die(f"{p}-{cell}: no kept branches: no Phase 2A task in phases.md and no branches.txt from 'pp.py choose'")
    if not kept:
        die(f"{triage}: the kept-branch file (selected_branches.txt or branches.txt) is missing or empty")
    # Phase 2B-D: a dropped branch re-admitted as a solver counts as selected from its first 2B task
    for r in rows:
        if r["Phase"] == "2B" and r["Branch"] in BRANCHES and r["Branch"] != "COMPUTATIONAL" and r["Branch"] not in kept:
            kept[r["Branch"]] = "solver (re-admitted)"
    xv = [r for r in rows if r["Phase"] == "2B-XV"]
    proofs = sorted({r["Task"] for r in rows if r["Phase"] == "2B"
                     and os.path.isfile(os.path.join(task_dir(r["Task"]), "out", "proof.md"))}
                    | {r["Subject"] for r in xv})
    report = []
    for proof in proofs:
        own = (phase_row(rows, proof) or {}).get("Branch", "-")
        verifiers = [r["Task"] for r in rows if r["Phase"] == "2" and r["Subject"] == proof]
        p2 = (verdict_of(verifiers[-1]), verifiers[-1]) if verifiers else (None, None)
        cross = {}
        for r in xv:
            if r["Subject"] == proof:
                cross[r["Branch"]] = (verdict_of(r["Task"], cross=True), r["Task"])
        others = [b for b in kept if b != own]
        confirmed = [b for b in others if cross.get(b, (None,))[0] in POSITIVE]
        present = [v for v, _ in [p2] + list(cross.values()) if v]
        negatives = [v for v in present if v in NEGATIVE]
        pending = ([] if p2[0] else ["Phase 2 verifier"]) + [b for b in others if not cross.get(b, (None,))[0]]
        need = len(others) if len(kept) < 4 else 3
        robust = p2[0] == "ACCEPT" and not negatives and others and len(confirmed) >= max(need, 1)
        disputed = []
        for label, (v, t) in [("Phase 2", p2)] + list(cross.items()):
            if v in NEGATIVE:
                text = verdict_text(t)
                detail = verdict_field(text, "FIRST PROBLEM") or verdict_field(text, "RED FLAGS") or "see verdict.md"
                disputed.append(f"- {proof} / {label} ({t}, {v}): {detail}")
        report.append({"proof": proof, "own": own, "p2": p2, "cross": cross, "confirmed": confirmed,
                       "robust": bool(robust), "disagree": bool(negatives) and len(negatives) < len(present),
                       "negative": bool(negatives), "pending": pending, "disputed": disputed})
    # a proof with no negative verdict and verdicts still pending could still become ROBUST
    still_open = [r["proof"] for r in report if not r["robust"] and not r["negative"] and r["pending"]]
    if any(r["robust"] for r in report):
        cls = "ROBUST"
        reason = "proof(s) " + ", ".join(r["proof"] for r in report if r["robust"]) + \
                 " passed the Phase 2 verifier and were confirmed by the required other branches, with no GAP or REFUTED"
    elif any(r["disagree"] for r in report):
        cls = "CONTESTED"
        reason = "verdicts disagree on " + ", ".join(r["proof"] for r in report if r["disagree"])
    elif still_open:
        cls = "INCOMPLETE"
        reason = "no disagreement so far, but verdicts are still pending on " + ", ".join(still_open)
    else:
        cls = "UNSUPPORTED"
        reason = "every verdict is in, and no proof has the confirmations ROBUST needs"
    return rows, triage, kept, report, cls, reason


def cmd_matrix(a):
    require_cell(a.P, a.cell)
    cls = write_matrix(a.P, a.cell)
    print(f"CLASS: {cls}")


def write_matrix(p, cell):
    _, triage, kept, report, cls, reason = compute_matrix(p, cell)
    cols = list(kept) + sorted({b for r in report for b in r["cross"]} - set(kept))
    out = [f"# Agreement matrix: {p}-{cell} (generated {now()})", "",
           f"Selected branches (from {triage}): " + ", ".join(f"{b} {k}" for b, k in kept.items()), "",
           "| Proof | Own branch | Phase 2 verifier | " + " | ".join(cols) + " |",
           "|---|---|---|" + "---|" * len(cols)]
    for r in report:
        v, t = r["p2"]
        cells = [f"{v or 'pending'} ({t})" if t else "pending"]
        for b in cols:
            if b == r["own"]:
                cells.append("(own)")
            else:
                cv, ct = r["cross"].get(b, (None, None))
                cells.append(f"{cv or 'pending'} ({ct})" if ct else "pending")
        out.append(f"| {r['proof']} | {r['own']} | " + " | ".join(cells) + " |")
    out += ["", f"CLASS: {cls}", f"Reason: {reason}", "", "## Disputed steps"]
    out += [d for r in report for d in r["disputed"]] or ["- none"]
    out += ["", "## Pending"]
    out += [f"- {r['proof']}: {', '.join(r['pending'])}" for r in report if r["pending"]] or ["- none"]
    with open(os.path.join(cell_dir(p, cell), "matrix.md"), "w") as fh:
        fh.write("\n".join(out) + "\n")
    return cls


def checklist_scores(text, items):
    scores = {}
    for item in items:
        m = re.search(r"\b" + item + r"\b[^A-Za-z\n]*(PASS|FAIL|N/A)\b", text)
        scores[item] = m.group(1) if m else "MISSING"
    return scores


def cmd_gate(a):
    require_cell(a.P, a.cell)
    check_same_cell(a.P, a.cell, a.subject, "--subject")
    rows = read_phases(a.P, a.cell)
    items = checklist_items(a.P, a.cell)
    # The object under evaluation is proof.md for a written proof, claims.md for a computational
    # subject (a Searcher writes no proof.md). Version-checking proof.md alone silently discounted
    # every ACCEPT on a computational claim.
    subject_file = next((n for n in SUBJECT_VERSION_FILES
                         if os.path.isfile(os.path.join(task_dir(a.subject), "out", n))), None)
    current = sha256(os.path.join(task_dir(a.subject), "out", subject_file)) if subject_file else None
    refs = [r for r in rows if r["Role"] == "referee" and r["Mode"] in ("VERIFY", "GATE") and r["Subject"] == a.subject]
    lines, score_lines, accepts, wrong = [], [], [], []
    for r in refs:
        t = r["Task"]
        text = verdict_text(t)
        v = verdict_of(t) or "none"
        scores = checklist_scores(text, items)
        complete = bool(items) and all(s in ("PASS", "N/A") for s in scores.values())
        seen = os.path.join(task_dir(t), "inbox", "subject", subject_file or "proof.md")
        same = current is not None and os.path.isfile(seen) and sha256(seen) == current
        match = (verdict_field(text, "STATEMENT MATCH") or "").lower().startswith("yes")
        lines.append(f"{t} {r['Mode']} {v} (checklist complete: {'yes' if complete else 'no'}; "
                     f"proof version: {'current' if same else 'other'}; statement match: {'yes' if match else 'no'})")
        score_lines.append(f"{t}: " + ", ".join(f"{k} {s}" for k, s in scores.items()))
        if v == "WRONG":
            wrong.append(t)
        if v == "ACCEPT" and complete and same and match:
            accepts.append(t)
    ran_2b = any(r["Phase"] in ("2B", "2B-XV") for r in rows)
    if ran_2b:
        matrix = write_matrix(a.P, a.cell)
        mine = next((r for r in compute_matrix(a.P, a.cell)[3] if r["proof"] == a.subject), None)
        this_proof = "not in matrix" if mine is None else ("robust" if mine["robust"] else "not robust")
    else:
        matrix, this_proof = "not run", "n/a"
    # the proof under the gate must itself be ROBUST; another proof's robustness doesn't carry over
    robust_ok = matrix == "not run" or (matrix == "ROBUST" and this_proof == "robust")
    if wrong:
        decision, rule = "INVALID", f"referee verdict WRONG ({', '.join(wrong)})"
    elif len(accepts) >= 2 and robust_ok and a.statement_checked:
        decision, rule = "VALID", (f"two referees ACCEPT the same proof version with complete checklists "
                                   f"({', '.join(accepts)}); matrix {matrix}; statement checked by head")
    else:
        missing = []
        if len(accepts) < 2:
            missing.append(f"{len(accepts)} counted ACCEPT(s) of 2 needed")
        if matrix not in ("ROBUST", "not run"):
            missing.append(f"matrix is {matrix}, not ROBUST")
        elif not robust_ok:
            missing.append(f"matrix is ROBUST through other proof(s), but {a.subject} is {this_proof}")
        if not a.statement_checked:
            missing.append("statement not checked word for word by head")
        decision, rule = "GAP", "; ".join(missing)
    nxt = {"VALID": "PROVED on board", "GAP": "repair + Phase 2C with this report",
           "INVALID": "tell the humans; repair + Phase 2C with this report"}[decision]
    # Every referee accepted and only the count falls short: nothing to repair, the proof needs another read.
    if decision == "GAP" and accepts and len(accepts) == len(refs) and missing == [f"{len(accepts)} counted ACCEPT(s) of 2 needed"]:
        nxt = "dispatch another referee on this same version; no repair needed"
    report = [f"# Gate: {a.P}-{a.cell}, proof {a.subject}, {now()}",
              "Referees: " + (" | ".join(lines) or "none"),
              f"Matrix: {matrix}; this proof: {this_proof}",
              f"Statement checked word for word by head: {'yes' if a.statement_checked else 'no'}",
              "Checklist scores: " + (" || ".join(score_lines) or "none"),
              f"DECISION: {decision} — {rule}",
              f"Next: {nxt}"]
    gdir = os.path.join(cell_dir(a.P, a.cell), "gate")
    os.makedirs(gdir, exist_ok=True)
    for name in ("gate_report.md", f"{a.subject}.md"):
        with open(os.path.join(gdir, name), "w") as fh:
            fh.write("\n".join(report) + "\n")
    log_event("gate", task=a.subject, cell=f"{a.P}-{a.cell}", decision=decision, accepts=accepts)
    print("\n".join(report))


# ---------- status / blindcheck ----------

def cmd_status(a):
    base = os.path.join(RUN, a.P)
    if not os.path.isdir(base):
        die(f"run/{a.P}/ does not exist")
    board, _ = board_state()
    print("| Cell | Agents run (by phase) | Verdicts | Robustness | Next |")
    print("|---|---|---|---|---|")
    for cell in sorted(d for d in os.listdir(base) if os.path.isdir(os.path.join(base, d))):
        rows = read_phases(a.P, cell)
        counts = {}
        for r in rows:
            counts[r["Phase"]] = counts.get(r["Phase"], 0) + 1
        agents = " ".join(f"{ph}:{n}" for ph, n in counts.items()) or "none"
        verdicts = []
        for r in rows:
            if r["Role"] == "referee":
                v = verdict_of(r["Task"], cross=r["Mode"] == "CROSS") or "pending"
                verdicts.append(f"{r['Task'].rsplit('-', 1)[1]} {r['Mode']} {v}")
        gate = os.path.join(base, cell, "gate", "gate_report.md")
        if os.path.isfile(gate):
            d = verdict_field(read(gate), "DECISION")
            verdicts.append(f"gate {d.split()[0] if d else '?'}")
        matrix = os.path.join(base, cell, "matrix.md")
        robust = (verdict_field(read(matrix), "CLASS") if os.path.isfile(matrix) else None) or "–"
        nxt = board.get(f"{a.P}-{cell}", {}).get("Next", "")
        print(f"| {a.P}-{cell} | {agents} | {'; '.join(verdicts) or '–'} | {robust} | {nxt} |")
    open_tasks = tasks_without_done(a.P)
    if open_tasks:
        print(f"\nno 'pp.py done' recorded (still running, or telemetry lost): {', '.join(open_tasks)}")


BLIND_MARKERS = [
    ("arXiv", re.compile(r"arxiv", re.I)),
    ("doi", re.compile(r"\bdoi\b|doi\.org", re.I)),
    ("url", re.compile(r"https?://|www\.", re.I)),
    ("et al.", re.compile(r"\bet\s+al\b", re.I)),
    ("conjecture of", re.compile(r"\bconjecture\s+of\b", re.I)),
    ("author-year", re.compile(r"\b[A-Z][^\W\d_]+(?:\s+(?:and|&)\s+[A-Z][^\W\d_]+)?,?\s+\(?(?:1[6-9]|20)\d\d\)?")),
]


def marker_hits(base):
    hits = []
    for root, _, names in os.walk(base):
        for name in sorted(names):
            path = os.path.join(root, name)
            try:
                text = read(path)
            except (UnicodeDecodeError, OSError):
                continue
            for i, ln in enumerate(text.splitlines(), 1):
                for label, pat in BLIND_MARKERS:
                    if pat.search(ln):
                        hits.append(f"{os.path.relpath(path, base)}:{i}: [{label}] {ln.strip()[:160]}")
    return hits


def cmd_blindcheck(a):
    out = os.path.join(task_dir(a.task), "out")
    if not os.path.isdir(out):
        die(f"{a.task} has no out/")
    brief = os.path.join(task_dir(a.task), "brief.md")
    regime = re.search(r"REGIME:\s*(\S+)", read(brief)).group(1) if os.path.isfile(brief) else "?"
    found = marker_hits(out)
    hits = len(found)
    for ln in found:
        print(ln)
    print(f"blindcheck {a.task} (regime {regime}): {hits} hit(s)"
          + ("; read each one and tell the humans if literature was used" if hits else ""))
    sys.exit(1 if hits else 0)


# ---------- reports ----------

def points(row):
    m = re.match(r"\d+", row.get("Pts", "") or "")
    return int(m.group()) if m else 0


def attention(p, rows):
    ranked = []
    for key, row in rows.items():
        if not key.startswith(f"{p}-"):
            continue
        st, rb = row.get("Cell status", ""), row.get("Robustness", "")
        if rb == "CONTESTED" or st == "COUNTEREXAMPLE":
            ranked.append((0, -points(row), key, "CONTESTED" if rb == "CONTESTED" else "COUNTEREXAMPLE"))
        elif st == "PARTIAL":
            ranked.append((1, -points(row), key, f"PARTIAL, {points(row)} pts"))
    return [(k, why) for _, _, k, why in sorted(ranked)[:3]]


def problem_report(p, rows, notes):
    cells = sorted(set(c for c in os.listdir(os.path.join(RUN, p)) if os.path.isdir(os.path.join(RUN, p, c)))
                   | set(k.split("-", 1)[1] for k in rows if k.startswith(f"{p}-")))
    by_status = {st: [] for st in CELL_STATUSES}
    table = ["| Cell | Pts | Phase | Cell status | Claim status | Robustness | Best so far | Final report |",
             "|---|---|---|---|---|---|---|---|"]
    for cell in cells:
        row = rows.get(f"{p}-{cell}", {})
        status = row.get("Cell status") or "NOT ATTEMPTED"
        by_status.setdefault(status, []).append(cell)
        final = f"{cell}/final_report.md" if os.path.isfile(os.path.join(RUN, p, cell, "final_report.md")) else "–"
        table.append(f"| {cell} | {row.get('Pts', '')} | {row.get('Phase', '')} | {status} | "
                     f"{row.get('Claim status', '')} | {row.get('Robustness', '') or '–'} | "
                     f"{row.get('Best so far', '')} | {final} |")
    mine = lambda key: [n for n in notes.get(key, []) if re.search(rf"\b{re.escape(p)}-C", n)] or ["- none"]
    top = attention(p, rows)
    out = [f"# Problem {p}: report (generated {now()} from run/board.md; statuses as gated)", ""]
    out += [f"- **{st.capitalize()}:** {', '.join(by_status[st]) or 'none'}" for st in CELL_STATUSES]
    out += ["", *table, "", "## Top cells for human attention"]
    out += [f"- {k}: {why}" for k, why in top] or ["- none"]
    out += ["", "## Partial cells: established / remaining gap", *mine("partial"), "",
            "## Contested cells", *mine("contested"), "",
            "## Obstacles: why the remaining cells are not solved now", *mine("obstacle"), "",
            "## Accepted artefacts (sha256-pinned)"]
    for cell in cells:
        manifest = os.path.join(RUN, p, cell, "accepted", "MANIFEST.sha256")
        if os.path.exists(manifest):
            out += [f"- {cell}:"] + [f"  - `{ln.strip()}`" for ln in open(manifest) if ln.strip()]
    with open(os.path.join(RUN, p, "report.md"), "w") as fh:
        fh.write("\n".join(out) + "\n")
    return by_status, top


def cmd_report(a):
    rows, notes = board_state()
    problems = sorted(d for d in os.listdir(RUN)
                      if os.path.isdir(os.path.join(RUN, d)) and d not in NON_PROBLEM_DIRS and not d.startswith("."))
    summary = [f"# Summary (generated {now()}, run time {run_elapsed()} of 7:00)", "",
               "| Problem | Solved | Partial | Counterexample | Not solved | Not attempted | Report |",
               "|---|---|---|---|---|---|---|"]
    tops = []
    for p in problems:
        st, top = problem_report(p, rows, notes)
        summary.append(f"| {p} | " + " | ".join(', '.join(st[s]) or '–' for s in CELL_STATUSES)
                       + f" | {p}/report.md |")
        tops += [f"- {k}: {why}" for k, why in top]
    summary += ["", "## Top cells for human attention", *(tops or ["- none"]), "",
                "Every status above is copied from the gated board. Nothing here is established unless it is "
                "SOLVED or listed as ESTABLISHED in a problem report."]
    with open(os.path.join(RUN, "SUMMARY.md"), "w") as fh:
        fh.write("\n".join(summary) + "\n")
    print(f"wrote run/SUMMARY.md and report.md for {', '.join(problems) or 'no problems'}")


def cmd_finalize(a):
    require_cell(a.P, a.cell)
    rows = read_phases(a.P, a.cell)
    rep, aud = phase_row(rows, a.report) or {}, phase_row(rows, a.audit) or {}
    if rep.get("Role") != "scribe" or rep.get("Mode") != "REPORT":
        die(f"{a.report} is not a Scribe REPORT task of {a.P}-{a.cell}")
    if aud.get("Role") != "auditor" or aud.get("Subject") != a.report:
        die(f"{a.audit} is not an audit of {a.report}")
    report = os.path.join(task_dir(a.report), "out", "final_report.md")
    audited = os.path.join(task_dir(a.audit), "inbox", "final_report.md")
    audit = os.path.join(task_dir(a.audit), "out", "audit.md")
    if not os.path.isfile(report):
        die(f"{a.report} has no out/final_report.md")
    if not os.path.isfile(audit):
        die(f"{a.audit} has no out/audit.md")
    verdict = verdict_field(read(audit), "AUDIT") or ""
    if not verdict.startswith("PASS"):
        die(f"audit {a.audit} says AUDIT: {verdict or 'missing'}; final_report.md not copied")
    if not os.path.isfile(audited) or sha256(audited) != sha256(report):
        die(f"the report {a.audit} audited differs from {a.report}/out/final_report.md; re-audit")
    shutil.copy2(report, os.path.join(cell_dir(a.P, a.cell), "final_report.md"))
    print(f"finalized run/{a.P}/{a.cell}/final_report.md (audit {a.audit} PASS)")


def cmd_summary(a):
    header, rows, tops, missing = None, [], [], []
    for b in a.branches:
        res = subprocess.run(["git", "-C", ROOT, "show", f"{b}:run/SUMMARY.md"], capture_output=True, text=True)
        if res.returncode:
            missing.append(b)
            continue
        section = None
        for ln in res.stdout.splitlines():
            if ln.startswith("## "):
                section = ln
            elif ln.startswith("|") and not ln.startswith("|-"):
                if ln.startswith("| Problem"):
                    header = header or ln
                else:
                    rows.append(ln)
            elif section == "## Top cells for human attention" and ln.startswith("- ") and ln != "- none":
                tops.append(ln)
    ncols = header.count("|") - 1 if header else 7
    out = [f"# Summary across branches (generated {now()})", "", header or "| Problem | ... |",
           "|" + "---|" * ncols, *rows, "", "## Top cells for human attention", *(tops or ["- none"])]
    if missing:
        out += ["", "## Branches without run/SUMMARY.md", *[f"- {b}" for b in missing]]
    text = "\n".join(out) + "\n"
    if a.out:
        with open(a.out, "w") as fh:
            fh.write(text)
    print(text, end="")


# ---------- telemetry ----------

def log_event(event, **fields):
    rec = {"event": event, "at": dt.datetime.now().isoformat(timespec="seconds"), "run_time": run_elapsed(), **fields}
    with open(TELEMETRY, "a") as fh:
        fh.write(json.dumps(rec) + "\n")


def task_outcome(task):
    out = os.path.join(task_dir(task), "out")
    names = sorted(n for n in os.listdir(out) if n != "tmp") if os.path.isdir(out) else []
    verdict = verdict_of(task) or verdict_of(task, cross=True)
    audit = os.path.join(out, "audit.md")
    if not verdict and os.path.isfile(audit):
        m = re.match(r"[*_]*([A-Z]+)", verdict_field(read(audit), "AUDIT") or "")
        verdict = f"AUDIT {m.group(1)}" if m else None
    if not verdict and verdict_text(task):
        verdict = next((lab for lab in ADVERSARY_LABELS if lab in verdict_text(task)), None)
    return names, verdict


def tasks_without_done(p=None):
    tasks = telemetry_tasks()
    return sorted(t for t, rec in tasks.items()
                  if not rec.get("done") and (p is None or t.startswith(f"{p}-")))


def cmd_done(a):
    if not os.path.isfile(os.path.join(task_dir(a.task), "brief.md")):
        die(f"{a.task} is not a task")
    names, verdict = task_outcome(a.task)
    fields = {k: getattr(a, k) for k in ("tokens", "ms", "tool_uses", "score") if getattr(a, k) is not None}
    log_event("done", task=a.task, out=names, verdict=verdict, **fields)
    print(f"telemetry: {a.task} returned ({verdict or ', '.join(names) or 'empty out/'})")


def telemetry_tasks():
    if not os.path.isfile(TELEMETRY):
        return {}
    tasks, gates, fed = {}, {}, set()
    for ln in open(TELEMETRY):
        if not ln.strip():
            continue
        rec = json.loads(ln)
        event, task = rec.get("event"), rec.get("task")
        if event == "task":
            tasks[task] = dict(rec)
        elif event == "done" and task in tasks:
            tasks[task]["done"] = True
            tasks[task].update({k: rec[k] for k in ("out", "verdict", "tokens", "ms", "tool_uses", "score") if k in rec})
        elif event == "gate":
            gates[task] = rec
        elif event == "pin":
            fed.add(task)
    for subject, g in gates.items():
        if g["decision"] == "VALID":
            fed |= {subject, *g.get("accepts", [])}
    for task, rec in tasks.items():
        rec["fed"] = task in fed
    return tasks


def group_values(rec, key):
    if key == "lessons":
        v = rec.get("lessons", {})
        return [f"{rec['role']} r{v.get('role', '-')} p{v.get('problem', '-')}"]
    if key == "lib":
        return rec.get("lib") or ["none"]
    return [str(rec.get(key) or "-")]


def cmd_telemetry(a):
    tasks = telemetry_tasks()
    if not tasks:
        die("run/telemetry.jsonl has no task records yet")
    if a.tasks:
        print("| Task | Phase | Role | Regime | Angle | Lessons | Library | Out | Verdict | Score | Tokens | Min | Fed |")
        print("|---|---|---|---|---|---|---|---|---|---|---|---|---|")
        for t, r in sorted(tasks.items()):
            mins = f"{r['ms'] / 60000:.1f}" if r.get("ms") else "–"
            print(f"| {t} | {r['phase']} | {r['role']} | {r['regime']} | {r.get('angle', '-')} | "
                  f"{group_values(r, 'lessons')[0]} | {', '.join(r.get('lib') or []) or '–'} | "
                  f"{', '.join(r.get('out', [])) or ('–' if r.get('done') else 'not returned')} | "
                  f"{r.get('verdict') or '–'} | {r.get('score', '–')} | {r.get('tokens', '–')} | {mins} | "
                  f"{'yes' if r['fed'] else 'no'} |")
        return
    groups = collections.defaultdict(list)
    for rec in tasks.values():
        for key in itertools.product(*(group_values(rec, k) for k in a.by)):
            groups[key].append(rec)
    print(f"| {' / '.join(a.by)} | Tasks | Returned | Proof | Fed gated claim | Verdicts | Tokens | Mean min |")
    print("|---|---|---|---|---|---|---|---|")
    for key in sorted(groups):
        recs = groups[key]
        done = [r for r in recs if r.get("done")]
        verdicts = collections.Counter(r["verdict"] for r in done if r.get("verdict"))
        tokens = sum(r.get("tokens", 0) for r in done)
        mins = [r["ms"] / 60000 for r in done if r.get("ms")]
        print(f"| {' / '.join(key)} | {len(recs)} | {len(done)} | {sum('proof.md' in r.get('out', []) for r in done)} | "
              f"{sum(r['fed'] for r in recs)} | {', '.join(f'{v} {n}' for v, n in verdicts.most_common()) or '–'} | "
              f"{f'{tokens / 1000:.0f}k' if tokens else '–'} | {f'{sum(mins) / len(mins):.1f}' if mins else '–'} |")
    waiting = sorted(t for t, r in tasks.items() if not r.get("done"))
    print(f"\nNot marked returned (pp.py done): {', '.join(waiting) or 'none'}")


# ---------- technique library ----------

def git(*args, text=True):
    return subprocess.run(["git", "-C", ROOT, *args], capture_output=True, text=text)


def lib_origin(src):
    rel = os.path.relpath(os.path.realpath(src), RUN)
    parts = rel.split(os.sep)
    if rel.startswith("..") or len(parts) < 4 or parts[0] in NON_PROBLEM_DIRS or parts[2] not in ("accepted", "checker"):
        return None
    return parts[0], parts[2]


def manifest_mismatches(entry_dir):
    bad = []
    for ln in open(os.path.join(entry_dir, "MANIFEST.sha256")):
        digest, name = ln.rstrip("\n").split("  ", 1)
        path = os.path.join(entry_dir, name)
        if not os.path.isfile(path) or sha256(path) != digest:
            bad.append(name)
    return bad


def cmd_lib_add(a):
    if not re.fullmatch(r"[a-z0-9][a-z0-9-]*", a.name):
        die("NAME must be lower-case letters, digits and hyphens")
    problems = set()
    for src in a.sources:
        path = src.partition("=")[0]
        origin = lib_origin(path) if os.path.exists(path) else None
        if not origin:
            die(f"{src}: library sources must exist under run/<P>/<cell>/accepted/ or run/<P>/<cell>/checker/")
        if a.kind == "lemma" and origin[1] != "accepted":
            die(f"{src}: a lemma must come from accepted/ (it passed the gate)")
        problems.add(origin[0])
    if len(problems) != 1:
        die("all sources of one entry must come from one problem")
    entry = f"{problems.pop()}-{a.name}"
    edir = os.path.join(LIBRARY, entry)
    if os.path.exists(edir):
        die(f"run/library/{entry} already exists")
    files = os.path.join(edir, "files")
    os.makedirs(files)
    for src in a.sources:
        copy_into(src, files)
    with open(os.path.join(edir, "MANIFEST.sha256"), "w") as man:
        for root, _, names in sorted(os.walk(files)):
            for n in sorted(names):
                man.write(f"{sha256(os.path.join(root, n))}  {os.path.relpath(os.path.join(root, n), edir)}\n")
    origins = ", ".join(os.path.relpath(os.path.realpath(s.partition('=')[0]), ROOT) for s in a.sources)
    with open(os.path.join(edir, "ENTRY.md"), "w") as fh:
        fh.write(f"# Library entry: {entry}\nKIND: {a.kind}\nWHAT: {a.what}\nFROM: {origins}\n"
                 f"EVIDENCE: {a.evidence}\nADDED: {dt.datetime.now().strftime('%Y-%m-%d %H:%M')}, "
                 f"run time {run_elapsed()}\n")
    log_event("lib-add", entry=entry, kind=a.kind)
    print(f"added run/library/{entry}")


def lib_entries(branch=None):
    if branch is None:
        if not os.path.isdir(LIBRARY):
            return {}
        return {n: read(os.path.join(LIBRARY, n, "ENTRY.md")) for n in sorted(os.listdir(LIBRARY))
                if os.path.isfile(os.path.join(LIBRARY, n, "ENTRY.md"))}
    res = git("ls-tree", "--name-only", f"{branch}:run/library")
    if res.returncode:
        return None
    entries = {}
    for n in res.stdout.split():
        shown = git("show", f"{branch}:run/library/{n}/ENTRY.md")
        if not shown.returncode:
            entries[n] = shown.stdout
    return entries


def cmd_lib_list(a):
    found, missing = {}, []
    for n, text in lib_entries().items():
        found[n] = (text, ["here"])
    for b in a.branches:
        entries = lib_entries(b)
        if entries is None:
            missing.append(b)
            continue
        for n, text in entries.items():
            found.setdefault(n, (text, []))[1].append(b)
    print("| Entry | Kind | What | Evidence | Where |")
    print("|---|---|---|---|---|")
    for n, (text, where) in sorted(found.items()):
        print(f"| {n} | {verdict_field(text, 'KIND')} | {verdict_field(text, 'WHAT')} | "
              f"{verdict_field(text, 'EVIDENCE')} | {', '.join(where)} |")
    if missing:
        print(f"\nNo run/library on: {', '.join(missing)}")
    print("\n'here' entries can go into an inbox with 'pp.py task ... --lib ENTRY'; others need 'pp.py lib import'.")


def cmd_lib_import(a):
    dest = os.path.join(LIBRARY, a.entry)
    if os.path.exists(dest):
        die(f"run/library/{a.entry} already exists here")
    res = git("ls-tree", "-r", "-z", "--name-only", a.branch, f"run/library/{a.entry}/")
    paths = [p for p in res.stdout.split("\0") if p]
    if res.returncode or not paths:
        die(f"{a.branch} has no run/library/{a.entry}/")
    for path in paths:
        target = os.path.join(ROOT, path)
        os.makedirs(os.path.dirname(target), exist_ok=True)
        with open(target, "wb") as fh:
            fh.write(git("show", f"{a.branch}:{path}", text=False).stdout)
    bad = manifest_mismatches(dest)
    if bad:
        shutil.rmtree(dest)
        die(f"{a.entry} from {a.branch} does not match its MANIFEST.sha256 ({', '.join(bad)}); not imported")
    log_event("lib-import", entry=a.entry, branch=a.branch)
    print(f"imported run/library/{a.entry} from {a.branch} (sha256 checked)")


def cmd_lessons(a):
    missing = []
    for b in a.branches:
        res = git("ls-tree", "--name-only", f"{b}:run")
        if res.returncode:
            missing.append(b)
            continue
        for p in res.stdout.split():
            if p in NON_PROBLEM_DIRS:
                continue
            shown = git("show", f"{b}:run/{p}/lessons.md")
            if shown.returncode:
                continue
            first = shown.stdout.split("\n", 1)[0]
            items = [ln for ln in shown.stdout.splitlines() if ln.startswith("- ")]
            print(f"## {b}: problem {p} ({first.strip()})")
            print("\n".join(items) or "- (no lessons)")
            print()
    if missing:
        print(f"No run/ on: {', '.join(missing)}\n")
    print("A lesson that shows up for two or more problems is a candidate role lesson (head skill, Learning).")


# ---------- CLI ----------

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
    s.add_argument("--phase", required=True, choices=list(PHASES))
    s.add_argument("--role", choices=sorted(ROLES))
    s.add_argument("--regime", help="WAVE only: BLIND / FRESH / CONTRARIAN / EXPLOIT")
    s.add_argument("--mode", choices=["VERIFY", "GATE", "CROSS", "SOLVE", "ANALYST", "ADVERSARY", "BRANCH",
                                      "SUBMISSION", "REPORT"])
    s.add_argument("--branch", choices=BRANCHES)
    s.add_argument("--branch-note", help="the problem skill's branch note for this lens")
    s.add_argument("--subject", help="task whose proof.md, claims.md, code/ go to inbox/subject/")
    s.add_argument("--subject-file", action="append", default=[], metavar="NAME",
                   help="extra file or dir from the subject's out/ into inbox/subject/ "
                        "(a computational subject's artefact); repeatable")
    s.add_argument("--obstacles", nargs="+", default=[], help="tasks whose stuck/verdict/no_natural_route files go in")
    s.add_argument("--earlier", nargs="+", default=[], help="literature: earlier tasks whose out/ goes in")
    s.add_argument("--record", action="store_true", help="copy the cell's full record (Scribe REPORT, Auditor)")
    s.add_argument("--checker", help="checker directory, copied to inbox/checker/")
    s.add_argument("--target", help="default: run/P/CELL/target.md")
    s.add_argument("--timebox", type=int, default=30)
    s.add_argument("--stop", required=True, help="stopping condition for the worker")
    s.add_argument("--assumptions", default="none beyond the statement")
    s.add_argument("--rules", action="append", default=[], help="extra rule; repeatable")
    s.add_argument("--angle")
    s.add_argument("--forbid", action="append", default=[], help="forbidden-approach line; repeatable")
    s.add_argument("--forbid-file", action="append", default=[], help="deadends.md to inline; repeatable")
    s.add_argument("--inbox", action="append", default=[], help="SRC or SRC=NAME to copy into inbox/; repeatable")
    s.add_argument("--lib", action="append", default=[], help="run/library entry copied to inbox/library/; repeatable")
    s.add_argument("--status", help="scribe: the gate-approved claim status")
    s.add_argument("--cell-status", choices=CELL_STATUSES, help="scribe: the gated cell status")
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
    for f in ("pts", "tier", "phase", "claim-status", "best", "lineages", "next", "time"):
        s.add_argument("--" + f)
    s.add_argument("--cell-status", choices=CELL_STATUSES)
    s.add_argument("--robustness", choices=ROBUSTNESS)
    s.add_argument("--note", nargs=2, metavar=("SECTION", "TEXT"))
    s.add_argument("--regenerate", action="store_true", help="rewrite board.md in the current template")
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

    s = sub.add_parser("choose")
    s.add_argument("P")
    s.add_argument("cell")
    s.add_argument("--map", required=True, help="the Phase 2S task whose out/spaces.md holds the cards")
    s.add_argument("--take", action="append", default=[],
                   help="'S<n>=ACTION: reason', one per card; ACTION: " + " ".join(CHOICE_ACTIONS))
    s.set_defaults(func=cmd_choose)

    s = sub.add_parser("matrix")
    s.add_argument("P")
    s.add_argument("cell")
    s.set_defaults(func=cmd_matrix)

    s = sub.add_parser("gate")
    s.add_argument("P")
    s.add_argument("cell")
    s.add_argument("--subject", required=True)
    s.add_argument("--statement-checked", action="store_true",
                   help="the head has checked the proved statement word for word against the cell")
    s.set_defaults(func=cmd_gate)

    s = sub.add_parser("status")
    s.add_argument("P")
    s.set_defaults(func=cmd_status)

    s = sub.add_parser("blindcheck")
    s.add_argument("task")
    s.set_defaults(func=cmd_blindcheck)

    s = sub.add_parser("report")
    s.set_defaults(func=cmd_report)

    s = sub.add_parser("finalize")
    s.add_argument("P")
    s.add_argument("cell")
    s.add_argument("--report", required=True)
    s.add_argument("--audit", required=True)
    s.set_defaults(func=cmd_finalize)

    s = sub.add_parser("summary")
    s.add_argument("--branches", nargs="+", required=True)
    s.add_argument("--out")
    s.set_defaults(func=cmd_summary)

    s = sub.add_parser("done")
    s.add_argument("task")
    s.add_argument("--tokens", type=int, help="total tokens from the subagent result")
    s.add_argument("--ms", type=int, help="duration_ms from the subagent result")
    s.add_argument("--tool-uses", type=int)
    s.add_argument("--score", help="searchers: the score you re-computed with the checker")
    s.set_defaults(func=cmd_done)

    s = sub.add_parser("telemetry")
    s.add_argument("--by", nargs="+", default=["role", "regime"], choices=GROUP_KEYS)
    s.add_argument("--tasks", action="store_true", help="one row per task instead of groups")
    s.set_defaults(func=cmd_telemetry)

    s = sub.add_parser("lib")
    lib = s.add_subparsers(dest="lib_cmd", required=True)
    s = lib.add_parser("add")
    s.add_argument("name")
    s.add_argument("sources", nargs="+")
    s.add_argument("--kind", required=True, choices=LIB_KINDS)
    s.add_argument("--what", required=True, help="one line: what it does and how to call it")
    s.add_argument("--evidence", required=True, help="how it was verified (cross-test log, gate report, pinned sha)")
    s.set_defaults(func=cmd_lib_add)
    s = lib.add_parser("list")
    s.add_argument("--branches", nargs="*", default=[])
    s.set_defaults(func=cmd_lib_list)
    s = lib.add_parser("import")
    s.add_argument("branch")
    s.add_argument("entry")
    s.set_defaults(func=cmd_lib_import)

    s = sub.add_parser("lessons")
    s.add_argument("--branches", nargs="+", required=True)
    s.set_defaults(func=cmd_lessons)

    a = ap.parse_args()
    if a.cmd == "board" and not (a.cell or a.note or a.regenerate):
        die("board needs a CELL, --note or --regenerate")
    a.func(a)


if __name__ == "__main__":
    main()
