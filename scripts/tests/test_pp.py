#!/usr/bin/env python3
"""Scratch-copy acceptance tests for scripts/pp.py (build step B1). Never touches the real run/."""
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

REPO = os.path.realpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
S = os.path.join(tempfile.gettempdir(), "pp_tests", "pp_sandbox")
fails = []


def setup():
    shutil.rmtree(S, ignore_errors=True)
    os.makedirs(S)
    shutil.copytree(os.path.join(REPO, "scripts"), os.path.join(S, "scripts"))
    shutil.copytree(os.path.join(REPO, ".claude"), os.path.join(S, ".claude"))
    os.makedirs(os.path.join(S, "run", "tasks"))
    with open(os.path.join(S, "run", "PROBLEM"), "w") as fh:
        fh.write("A problem-angles-lines\n")


def pp(*args, ok=True, label=None):
    res = subprocess.run([sys.executable, os.path.join(S, "scripts", "pp.py"), *args], capture_output=True, text=True)
    good = (res.returncode == 0) == ok
    name = label or " ".join(args)[:110]
    print(f"{'PASS' if good else 'FAIL'} {'ok  ' if ok else 'deny'} {name}"
          + ("" if good else f"\n     rc={res.returncode} out={res.stdout[-300:]} err={res.stderr[-300:]}"))
    if not good:
        fails.append(name)
    return res.stdout + res.stderr


def check(cond, name):
    print(f"{'PASS' if cond else 'FAIL'} check {name}")
    if not cond:
        fails.append(name)


def T(task, *parts):
    return os.path.join(S, "run", "tasks", task, *parts)


def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as fh:
        fh.write(text)


def last_task(out):
    return out.split("\n")[0].strip()


def fake_proof(task, branch_tag=""):
    write(T(task, "out", "proof.md"), f"Statement {branch_tag}\n1. step\n")
    write(T(task, "out", "claims.md"), "| c | PROVED | proof.md 1 |\n")
    write(T(task, "out", "code", "run.py"), "print(1)\n")
    write(T(task, "out", "stuck.md"), "none\n")
    write(T(task, "out", "plan.md"), "R1 PROVED\n")


ITEMS = [f"G{i}" for i in range(1, 10)] + [f"S{i}" for i in range(1, 7)]


def verdict(task, v, missing=(), fail=(), match="yes"):
    lines = [f"VERDICT: {v}", f"STATEMENT MATCH: {match}", "FIRST PROBLEM: step 3 — unjustified bound" if v != "ACCEPT"
             else "FIRST PROBLEM: none", "CHECKLIST:"]
    lines += [f"  {i} {'FAIL' if i in fail else 'PASS'} — reason" for i in ITEMS if i not in missing]
    write(T(task, "out", "verdict.md"), "\n".join(lines) + "\nStep 1 holds because ...\n")


def cross(task, v):
    write(T(task, "out", "verdict.md"), f"CROSS VERDICT: {v}\nBRANCH: x\nTRANSLATION: t\n"
          f"RED FLAGS: {'step 2 does not translate' if v in ('GAP', 'REFUTED') else 'none'}\n")


STOP = ["--stop", "stop when done"]


def phase_tests():
    print("\n== open + every phase: briefs, inbox rules, rejections")
    pp("open", "A", "C1", "C2", "C3", "C4")
    c1 = os.path.join(S, "run", "A", "C1")
    check(os.path.isfile(os.path.join(c1, "checklist.md")) and "Checklist: A-C1" in open(os.path.join(c1, "checklist.md")).read(),
          "open writes checklist template with cell id")
    check(open(os.path.join(c1, "phases.md")).read().startswith("| Task | Phase | Role |"), "open writes phases.md header")
    check(os.path.isdir(os.path.join(c1, "gate")), "open creates gate/")
    write(os.path.join(S, "run", "A", "statement.md"), "Verbatim setting.\n")
    write(os.path.join(c1, "target.md"), "For every N, S <= pi/2 floor(N^2/4).\n")


    out = pp("task", "A", "C1", "--phase", "0", *STOP)
    t0 = last_task(out)
    inbox = os.listdir(T(t0, "inbox"))
    check("checklist-G.md" not in inbox and "checklist-S.md" not in inbox, "phase 0 checker-builder gets no checklist")
    check("problem-lessons.md" not in inbox, "checker-builder gets no problem lessons")
    check({"role-lessons.md", "statement.md", "target.md"} <= set(inbox), "phase 0 gets lessons, statement, target")
    brief = open(T(t0, "brief.md")).read()
    check("ROLE: checker-builder" in brief and "REGIME: CLEAN-ROOM" in brief and "PHASE: 0" in brief, "phase 0 header")
    check("TARGET: For every N" in brief, "TARGET defaults to target.md")

    out = pp("task", "A", "C1", "--phase", "1", "--role", "prover", *STOP)
    t1 = last_task(out)
    inbox = set(os.listdir(T(t1, "inbox")))
    brief = open(T(t1, "brief.md")).read()
    check("checklist-G.md" in inbox and "checklist-S.md" not in inbox, "blind prover: Part G only, no Part S")
    check("Part S" not in open(T(t1, "inbox", "checklist-G.md")).read(), "checklist-G.md contains no Part S text")
    check("problem-lessons.md" in inbox, "blind prover gets problem lessons")
    check("REGIME: BLIND" in brief and "MODE: -" in brief and "SUBJECT: -" in brief, "phase 1 header lines")
    check("Derive everything from first principles" in brief, "BLIND regime addition in brief")
    check("**Prover**" not in brief and "First write out/plan.md" in brief, "prover block in brief")
    check("LADDER / RAN" in brief, "RETURN line mentions LADDER / RAN")
    pp("task", "A", "C1", "--phase", "1", *STOP, ok=False, label="phase 1 without --role")
    pp("task", "A", "C1", "--phase", "1", "--role", "referee", *STOP, ok=False, label="phase 1 with referee role")
    pp("task", "A", "C1", "--phase", "1", "--role", "prover", "--inbox", os.path.join(S, "run", "A", "statement.md"),
       *STOP, ok=False, label="BLIND rejects --inbox")
    pp("task", "A", "C1", "--phase", "1", "--role", "prover", "--subject", t1, *STOP, ok=False,
       label="BLIND rejects --subject")
    pp("task", "A", "C1", "--phase", "1", "--role", "prover", "--earlier", t1, *STOP, ok=False,
       label="BLIND rejects --earlier")
    pp("task", "A", "C1", "--phase", "1", "--role", "prover", "--record", *STOP, ok=False, label="BLIND rejects --record")
    pp("task", "A", "C1", "--phase", "1", "--role", "prover", "--obstacles", t1, *STOP, ok=False,
       label="phase 1 rejects --obstacles")
    pp("task", "A", "C1", "--phase", "1", "--role", "prover", "--regime", "FRESH", *STOP, ok=False,
       label="phase 1 rejects another regime")
    pp("task", "A", "C1", "--phase", "1", "--role", "prover", "--mode", "BRANCH", *STOP, ok=False,
       label="phase 1 rejects a mode")
    pp("task", "A", "C1", "--phase", "1", "--role", "prover", "--checker", os.path.join(S, "scripts"), *STOP, ok=False,
       label="prover rejects --checker")

    chk = os.path.join(S, "chk")
    write(os.path.join(chk, "verify.py"), "print('VERIFIED 0')\n")
    out = pp("task", "A", "C1", "--phase", "1", "--role", "searcher", "--checker", chk, *STOP)
    ts = last_task(out)
    check(os.path.isfile(T(ts, "inbox", "checker", "verify.py")), "blind searcher gets checker/")

    fake_proof(t1)
    out = pp("task", "A", "C1", "--phase", "1L", "--earlier", t1, *STOP)
    tl = last_task(out)
    brief = open(T(tl, "brief.md")).read()
    check("MODE: SOLVE" in brief and "Phase 1L. Inbox/earlier/" in brief and "You have web search" in brief,
          "1L literature SOLVE brief (role + mode block)")
    check(os.path.isfile(T(tl, "inbox", "earlier", t1, "proof.md")), "1L gets Phase 1 outputs")
    pp("task", "A", "C1", "--phase", "1L", "--earlier", t0, *STOP, ok=False, label="1L rejects a non-Phase-1 task")

    out = pp("task", "A", "C1", "--phase", "2", "--subject", t1, *STOP)
    tv = last_task(out)
    inbox = set(os.listdir(T(tv, "inbox")))
    check({"checklist-G.md", "checklist-S.md", "subject"} <= inbox, "referee gets G, S and subject/")
    check("problem-lessons.md" not in inbox, "referee gets no problem lessons")
    check(sorted(os.listdir(T(tv, "inbox", "subject"))) == ["claims.md", "code", "proof.md"],
          "subject/ holds only proof.md, claims.md, code/")
    brief = open(T(tv, "brief.md")).read()
    check("MODE: VERIFY" in brief and f"SUBJECT: {t1}" in brief and "CHECKLIST / RAN" in brief, "phase 2 header")
    pp("task", "A", "C1", "--phase", "2", *STOP, ok=False, label="referee without --subject")
    pp("task", "A", "C1", "--phase", "2", "--subject", "A-C9-001", *STOP, ok=False, label="subject from another cell")

    write(T(t1, "out", "Q4.txt"), "0000\n1111\n")
    write(T(t1, "out", "runlog.md"), "how I did it\n")
    ck = os.path.join(S, "run", "A", "C1", "checker")
    write(os.path.join(ck, "verify.py"), "print('VERIFIED 0')\n")
    tcv = last_task(pp("task", "A", "C1", "--phase", "2", "--subject", t1,
                       "--subject-file", "Q4.txt", "--checker", ck, *STOP))
    check("Q4.txt" in os.listdir(T(tcv, "inbox", "subject")), "referee gets the computational subject's artefact")
    check(os.path.isfile(T(tcv, "inbox", "checker", "verify.py")), "referee may be given the checker to re-score")
    pp("task", "A", "C1", "--phase", "2", "--subject", t1, "--subject-file", "runlog.md", *STOP, ok=False,
       label="--subject-file refuses a process file (clean room)")
    pp("task", "A", "C1", "--phase", "2", "--subject", t1, "--subject-file", "nope.txt", *STOP, ok=False,
       label="--subject-file refuses a file the subject does not have")

    out = pp("task", "A", "C1", "--phase", "2A", "--obstacles", t1, tv, *STOP)
    ta = last_task(out)
    check(sorted(os.listdir(T(ta, "inbox", "obstacles", t1))) == ["stuck.md"], "triage obstacles: stuck.md only, no proof")
    check("checklist-S.md" not in os.listdir(T(ta, "inbox")), "triage gets no Part S")
    check("Phase 2A. Do not solve" in open(T(ta, "brief.md")).read(), "triage brief block")

    out = pp("task", "A", "C1", "--phase", "2B", "--role", "prover", "--branch", "ALGEBRAIC",
             "--branch-note", "Gram matrix (angle)", *STOP)
    tb = last_task(out)
    brief = open(T(tb, "brief.md")).read()
    check("BRANCH LENS: ALGEBRAIC — matrices, rank" in brief and "Problem note: Gram matrix (angle)" in brief,
          "2B lens text + branch note filled in")
    check("<branch>" not in brief and "BRANCH: ALGEBRAIC" in brief, "no lens placeholders left")
    check("Derive everything from first principles" in brief, "2B carries BLIND addition")
    out = pp("task", "A", "C1", "--phase", "2B", "--role", "searcher", "--branch", "COMPUTATIONAL", *STOP)
    check("exhaustive search, SAT/ILP" in open(T(last_task(out), "brief.md")).read(), "searcher COMPUTATIONAL lens")
    pp("task", "A", "C1", "--phase", "2B", "--role", "prover", *STOP, ok=False, label="2B without --branch")
    pp("task", "A", "C1", "--phase", "2B", "--role", "prover", "--branch", "COMPUTATIONAL", *STOP, ok=False,
       label="COMPUTATIONAL lens rejected for prover")
    pp("task", "A", "C1", "--phase", "1", "--role", "prover", "--branch", "ALGEBRAIC", *STOP, ok=False,
       label="--branch outside 2B")

    fake_proof(tb)
    pp("task", "A", "C1", "--phase", "2B-XV", "--branch", "ALGEBRAIC", "--subject", tb, *STOP, ok=False,
       label="cross-verifier from the proof's own branch")
    out = pp("task", "A", "C1", "--phase", "2B-XV", "--branch", "DISCRETE", "--subject", tb, *STOP)
    brief = open(T(last_task(out), "brief.md")).read()
    check("MODE: CROSS" in brief and "BRANCH LENS: DISCRETE — graph" in brief and "TRANSLATE the key idea" in brief,
          "2B-XV CROSS brief")

    out = pp("task", "A", "C1", "--phase", "2C", "--obstacles", t1, *STOP)
    tc = last_task(out)
    brief = open(T(tc, "brief.md")).read()
    check("MODE: ADVERSARY" in brief and "out/contrapositive.md" in brief and "REGIME: BLIND" in brief, "2C brief")

    out = pp("task", "A", "C1", "--phase", "3", "--earlier", t1, tv, tb, *STOP)
    t3 = last_task(out)
    check("MODE: ANALYST" in open(T(t3, "brief.md")).read() and os.path.isdir(T(t3, "inbox", "earlier", tv)),
          "phase 3 analyst gets everything named")

    out = pp("task", "A", "C1", "--phase", "GATE", "--subject", t1, *STOP)
    check("MODE: GATE" in open(T(last_task(out), "brief.md")).read(), "GATE referee brief")

    write(os.path.join(c1, "gate", f"{t1}.md"), "# Gate: fake\nDECISION: GAP — x\n")
    out = pp("task", "A", "C1", "--phase", "REPAIR", "--role", "prover", "--subject", t1, *STOP)
    tr = last_task(out)
    check(os.path.isfile(T(tr, "inbox", "gate_report.md")) and os.path.isdir(T(tr, "inbox", "subject")),
          "REPAIR gets subject + its gate report")
    check("Repair the listed problems first" in open(T(tr, "brief.md")).read(), "EXPLOIT addition")
    pp("task", "A", "C1", "--phase", "REPAIR", "--role", "prover", *STOP, ok=False, label="REPAIR without --subject")

    out = pp("task", "A", "C1", "--phase", "WAVE", "--role", "prover", "--regime", "FRESH", "--angle", "gram-matrix", *STOP)
    check("ANGLE: gram-matrix" in open(T(last_task(out), "brief.md")).read(), "WAVE FRESH angle")
    pp("task", "A", "C1", "--phase", "WAVE", "--role", "prover", *STOP, ok=False, label="WAVE without --regime")
    pp("task", "A", "C1", "--phase", "WAVE", "--role", "prover", "--regime", "FRESH", *STOP, ok=False,
       label="FRESH prover without --angle")
    pp("task", "A", "C1", "--phase", "WAVE", "--role", "breaker", "--regime", "EXPLOIT", "--subject", t1, *STOP,
       ok=False, label="breaker cannot EXPLOIT")
    out = pp("task", "A", "C1", "--phase", "WAVE", "--role", "prover", "--regime", "CONTRARIAN",
             "--forbid", "[gram] tried", *STOP)
    check("FORBIDDEN APPROACHES" in open(T(last_task(out), "brief.md")).read(), "WAVE CONTRARIAN forbid list")
    pp("task", "A", "C1", "--phase", "WAVE", "--role", "prover", "--regime", "FRESH", "--angle", "x",
       "--inbox", os.path.join(c1, "checklist.md"), *STOP, ok=False, label="non-referee --inbox checklist.md rejected")

    pp("task", "A", "C1", "--phase", "5", "--status", "PROVED", "--cell-status", "SOLVED", *STOP, ok=False,
       label="phase 5 without --mode")
    pp("task", "A", "C1", "--phase", "5", "--mode", "REPORT", *STOP, ok=False, label="scribe without statuses")
    out = pp("task", "A", "C1", "--phase", "5", "--mode", "REPORT", "--status", "PROVED", "--cell-status", "SOLVED", *STOP)
    tsr = last_task(out)
    rec = T(tsr, "inbox", "record")
    check(os.path.isfile(os.path.join(rec, "tasks", t1, "out", "proof.md")), "REPORT record keeps tasks/<id>/out/ paths")
    check(not os.path.exists(os.path.join(rec, "tasks", tsr)), "record excludes the scribe's own task")
    check(os.path.isfile(os.path.join(rec, "cell", "checklist.md")), "record has the cell's checklist")
    brief = open(T(tsr, "brief.md")).read()
    check("Phase 5. Inbox/record/" in brief and "CELL STATUS: SOLVED" in brief, "Scribe REPORT brief")
    out = pp("task", "A", "C1", "--phase", "5", "--mode", "SUBMISSION", "--status", "PROVED", "--cell-status", "SOLVED",
             "--inbox", f"{os.path.join(c1, 'target.md')}=handin.md", *STOP)
    check("Inbox holds accepted artefacts" in open(T(last_task(out), "brief.md")).read(), "Scribe SUBMISSION brief")
    pp("task", "A", "C1", "--phase", "5", "--mode", "SUBMISSION", "--status", "PROVED", "--cell-status", "SOLVED",
       "--record", *STOP, ok=False, label="--record rejected for SUBMISSION")

    pp("task", "A", "C1", "--phase", "AUDIT", "--subject", t1, *STOP, ok=False, label="auditor subject must be REPORT")
    write(T(tsr, "out", "final_report.md"), "1. OUTCOME: PROVED (tasks/x/out/proof.md, step 1)\n")
    out = pp("task", "A", "C1", "--phase", "AUDIT", "--subject", tsr, *STOP)
    tau = last_task(out)
    inbox = set(os.listdir(T(tau, "inbox")))
    check({"final_report.md", "record", "checklist-G.md"} <= inbox and "checklist-S.md" not in inbox
          and "problem-lessons.md" not in inbox, "auditor inbox: report + record, no Part S, no problem lessons")
    arec = T(tau, "inbox", "record")
    check(os.path.isfile(os.path.join(arec, "tasks", tsr, "out", "final_report.md")),
          "auditor record holds the subject's own brief.md + out/")
    check(open(os.path.join(arec, "cell", "phases.md")).read()
          == open(os.path.join(T(tsr, "inbox", "record"), "cell", "phases.md")).read(),
          "auditor reads the record snapshot the Scribe wrote from, not a later one")

    rows = [l for l in open(os.path.join(c1, "phases.md")).read().splitlines() if l.startswith(f"| A-C1-")]
    n_tasks = len([d for d in os.listdir(os.path.join(S, "run", "tasks")) if d.startswith("A-C1-")])
    check(len(rows) == n_tasks, f"phases.md has one row per task ({len(rows)} rows, {n_tasks} tasks)")
    check(any("| 2B-XV | referee | CLEAN-ROOM | CROSS | DISCRETE |" in r for r in rows), "phases.md row fields")

    print("\n== finalize")
    pp("finalize", "A", "C1", "--report", tsr, "--audit", tau, ok=False, label="finalize without audit.md")
    write(T(tau, "out", "audit.md"), "AUDIT: FAIL\nCITATIONS CHECKED: 3\nUNSUPPORTED: x\n")
    pp("finalize", "A", "C1", "--report", tsr, "--audit", tau, ok=False, label="finalize refuses AUDIT: FAIL")
    write(T(tau, "out", "audit.md"), "AUDIT: PASS\nCITATIONS CHECKED: 3\nUNSUPPORTED: none\n")
    pp("finalize", "A", "C1", "--report", tsr, "--audit", tau, label="finalize after AUDIT: PASS")
    check(os.path.isfile(os.path.join(c1, "final_report.md")), "final_report.md copied")
    write(T(tsr, "out", "final_report.md"), "changed after audit\n")
    pp("finalize", "A", "C1", "--report", tsr, "--audit", tau, ok=False, label="finalize refuses a report changed after audit")

    print("\n== blindcheck")
    write(T(t1, "out", "proof.md"), "1. By Cauchy-Schwarz the bound holds.\n")
    pp("blindcheck", t1, label="clean blind output → 0 hits")
    write(T(t1, "out", "notes.md"), "See arXiv:1234.5678 and Smith (1959); also Jones et al.\nthe conjecture of X\nhttps://x.org\n")
    out = pp("blindcheck", t1, ok=False, label="literature markers → hits")
    check(all(k in out for k in ("[arXiv]", "[author-year]", "[et al.]", "[conjecture of]", "[url]")), "all marker kinds found")
    return t1


def setup_2b(cell, p2, xv, kept="ALGEBRAIC\tsolver\nDISCRETE\tsolver\nANALYSIS\tverifier-only\n"):
    c = os.path.join(S, "run", "A", cell)
    write(os.path.join(c, "target.md"), "target\n")
    ta = last_task(pp("task", "A", cell, "--phase", "2A", *STOP))
    write(T(ta, "out", "selected_branches.txt"), kept)
    tb = last_task(pp("task", "A", cell, "--phase", "2B", "--role", "prover", "--branch", "ALGEBRAIC", *STOP))
    fake_proof(tb, cell)
    tv = last_task(pp("task", "A", cell, "--phase", "2", "--subject", tb, *STOP))
    # cross-verifiers dispatched in parallel with the Phase 2 verifier, before its verdict is in
    txs = {branch: last_task(pp("task", "A", cell, "--phase", "2B-XV", "--branch", branch, "--subject", tb, *STOP))
           for branch in xv}
    verdict(tv, p2)
    for branch, v in xv.items():
        if v:
            cross(txs[branch], v)
    return tb, tv


def matrix_gate_tests():
    print("\n== matrix: ROBUST / CONTESTED / UNSUPPORTED")
    tb2, tv2 = setup_2b("C2", "ACCEPT", {"DISCRETE": "CONFIRMED", "ANALYSIS": "CONFIRMED-WITH-CAVEATS"})
    out = pp("matrix", "A", "C2")
    check("CLASS: ROBUST" in out, "3 branches, all others confirm, verifier ACCEPT → ROBUST")
    m = open(os.path.join(S, "run", "A", "C2", "matrix.md")).read()
    check("(own)" in m and "CONFIRMED-WITH-CAVEATS" in m, "matrix.md table shows own column and verdicts")

    setup_2b("C3", "ACCEPT", {"DISCRETE": "CONFIRMED", "ANALYSIS": "GAP"})
    out = pp("matrix", "A", "C3")
    check("CLASS: CONTESTED" in out, "confirm + GAP → CONTESTED")
    check("step 2 does not translate" in open(os.path.join(S, "run", "A", "C3", "matrix.md")).read(),
          "CONTESTED lists the disputed step")

    tb4, _ = setup_2b("C4", "MAJOR", {"DISCRETE": "GAP", "ANALYSIS": "REFUTED"})
    check("CLASS: UNSUPPORTED" in pp("matrix", "A", "C4"), "all negative → UNSUPPORTED")
    out = pp("task", "A", "C4", "--phase", "2B-XV", "--branch", "TOPOLOGICAL", "--subject", tb4, *STOP, ok=False,
             label="2B-XV refused after a negative Phase 2 verdict")
    check("repair it first" in out, "refusal says to repair first")

    pp("open", "A", "C5", "C6")
    setup_2b("C5", "ACCEPT", {"DISCRETE": "CONFIRMED", "ANALYSIS": "CONFIRMED", "TOPOLOGICAL": "CONFIRMED",
                              "NUMBER-THEORY": None},
             kept="ALGEBRAIC\tsolver\nDISCRETE\tsolver\nANALYSIS\tsolver\nTOPOLOGICAL\tverifier-only\n"
                  "NUMBER-THEORY\tverifier-only\n")
    check("CLASS: ROBUST" in pp("matrix", "A", "C5"), "5 branches: 3 confirmations suffice, one pending → ROBUST")
    tb6, _ = setup_2b("C6", "ACCEPT", {"DISCRETE": "CONFIRMED", "ANALYSIS": None})
    out = pp("matrix", "A", "C6")
    check("CLASS: INCOMPLETE" in out and "- A-C6-002: ANALYSIS" in open(os.path.join(S, "run", "A", "C6", "matrix.md")).read(),
          "3 branches, 1 confirm + 1 pending → INCOMPLETE (not yet UNSUPPORTED), pending listed")
    out = pp("task", "A", "C6", "--phase", "2B-XV", "--branch", "DISCRETE", "--subject", tb6, *STOP, ok=False,
             label="2B-XV refused: same proof, same branch twice")
    check("already has a DISCRETE cross-verifier" in out, "duplicate refusal names the existing task")
    pp("open", "A", "C8")
    setup_2b("C8", "ACCEPT", {"DISCRETE": "CONFIRMED", "ANALYSIS": "CONFIRMED", "TOPOLOGICAL": None, "NUMBER-THEORY": None},
             kept="ALGEBRAIC\tsolver\nDISCRETE\tsolver\nANALYSIS\tsolver\nTOPOLOGICAL\tverifier-only\n"
                  "NUMBER-THEORY\tverifier-only\n")
    check("CLASS: INCOMPLETE" in pp("matrix", "A", "C8"), "5 branches, 2 confirm + 2 pending → INCOMPLETE (not ROBUST)")

    pp("open", "A", "C9")
    tb9, _ = setup_2b("C9", "ACCEPT", {"DISCRETE": "CONFIRMED", "ANALYSIS": "CONFIRMED", "NUMBER-THEORY": None},
                      kept="ALGEBRAIC\tsolver\nDISCRETE\tsolver\nANALYSIS\tverifier-only\nNUMBER-THEORY\tverifier-only\n")
    check("CLASS: INCOMPLETE" in pp("matrix", "A", "C9"), "4 branches, 2 of 3 confirmations + 1 pending → INCOMPLETE")
    pp("task", "A", "C9", "--phase", "2B", "--role", "prover", "--branch", "TOPOLOGICAL", *STOP)  # 2B-D re-admission
    tx9 = last_task(pp("task", "A", "C9", "--phase", "2B-XV", "--branch", "TOPOLOGICAL", "--subject", tb9, *STOP))
    cross(tx9, "CONFIRMED")
    check("CLASS: ROBUST" in pp("matrix", "A", "C9"), "re-admitted branch's confirmation counts → ROBUST")
    check("TOPOLOGICAL solver (re-admitted)" in open(os.path.join(S, "run", "A", "C9", "matrix.md")).read(),
          "matrix.md lists the re-admitted branch")

    print("\n== gate: VALID / GAP / INVALID")
    tg = last_task(pp("task", "A", "C2", "--phase", "GATE", "--subject", tb2, *STOP))
    verdict(tg, "ACCEPT")
    out = pp("gate", "A", "C2", "--subject", tb2, "--statement-checked")
    check("DECISION: VALID" in out, "2 ACCEPT complete + ROBUST + statement checked → VALID")
    check(os.path.isfile(os.path.join(S, "run", "A", "C2", "gate", "gate_report.md"))
          and os.path.isfile(os.path.join(S, "run", "A", "C2", "gate", f"{tb2}.md")), "gate_report.md + per-subject copy")
    check("DECISION: GAP" in pp("gate", "A", "C2", "--subject", tb2), "without --statement-checked → GAP")
    verdict(tg, "ACCEPT", missing=("S3",))
    out = pp("gate", "A", "C2", "--subject", tb2, "--statement-checked")
    check("DECISION: GAP" in out and "S3 MISSING" in out, "checklist item missing → ACCEPT not counted → GAP")
    verdict(tg, "ACCEPT", fail=("G3",))
    check("DECISION: GAP" in pp("gate", "A", "C2", "--subject", tb2, "--statement-checked"), "FAIL item → GAP")
    verdict(tg, "ACCEPT", match="no — range d>=2 vs d>=1")
    check("DECISION: GAP" in pp("gate", "A", "C2", "--subject", tb2, "--statement-checked"), "statement mismatch → GAP")
    verdict(tg, "WRONG")
    check("DECISION: INVALID" in pp("gate", "A", "C2", "--subject", tb2, "--statement-checked"), "any WRONG → INVALID")
    verdict(tg, "ACCEPT")
    with open(T(tb2, "out", "proof.md"), "a") as fh:
        fh.write("2. edited after refereeing\n")
    out = pp("gate", "A", "C2", "--subject", tb2, "--statement-checked")
    check("DECISION: GAP" in out and "proof version: other" in out, "proof changed after refereeing → GAP")

    tb3 = next(l.split("|")[1].strip() for l in open(os.path.join(S, "run", "A", "C3", "phases.md"))
               if "| 2B |" in l)
    tg3 = last_task(pp("task", "A", "C3", "--phase", "GATE", "--subject", tb3, *STOP))
    verdict(tg3, "ACCEPT")
    out = pp("gate", "A", "C3", "--subject", tb3, "--statement-checked")
    check("DECISION: GAP" in out and "matrix is CONTESTED" in out, "2 ACCEPT but CONTESTED → GAP")

    print("\n== gate: robustness belongs to the proof, not the cell")
    pp("open", "A", "C10")
    tx10, _ = setup_2b("C10", "ACCEPT", {"DISCRETE": "CONFIRMED", "ANALYSIS": "CONFIRMED"})
    ty = last_task(pp("task", "A", "C10", "--phase", "2B", "--role", "prover", "--branch", "DISCRETE", *STOP))
    fake_proof(ty, "second")
    verdict(last_task(pp("task", "A", "C10", "--phase", "2", "--subject", ty, *STOP)), "ACCEPT")
    cross(last_task(pp("task", "A", "C10", "--phase", "2B-XV", "--branch", "ALGEBRAIC", "--subject", ty, *STOP)), "REFUTED")
    verdict(last_task(pp("task", "A", "C10", "--phase", "GATE", "--subject", ty, *STOP)), "ACCEPT")
    out = pp("gate", "A", "C10", "--subject", ty, "--statement-checked")
    check("DECISION: GAP" in out and f"{ty} is not robust" in out,
          "2 ACCEPT, cell ROBUST through another proof, this proof REFUTED cross-branch → GAP")
    verdict(last_task(pp("task", "A", "C10", "--phase", "GATE", "--subject", tx10, *STOP)), "ACCEPT")
    out = pp("gate", "A", "C10", "--subject", tx10, "--statement-checked")
    check("DECISION: VALID" in out and "this proof: robust" in out, "the robust proof itself still passes → VALID")

    print("\n== gate without 2B (matrix not run)")
    pp("open", "A", "C7")
    c7 = os.path.join(S, "run", "A", "C7")
    write(os.path.join(c7, "target.md"), "t\n")
    tp = last_task(pp("task", "A", "C7", "--phase", "1", "--role", "prover", *STOP))
    fake_proof(tp)
    ra = last_task(pp("task", "A", "C7", "--phase", "2", "--subject", tp, *STOP))
    verdict(ra, "ACCEPT")
    out = pp("gate", "A", "C7", "--subject", tp, "--statement-checked")
    check("DECISION: GAP" in out and "Next: dispatch another referee" in out,
          "a single ACCEPT → GAP asks for another referee, not a repair")
    rb = last_task(pp("task", "A", "C7", "--phase", "GATE", "--subject", tp, *STOP))
    verdict(rb, "ACCEPT")
    out = pp("gate", "A", "C7", "--subject", tp, "--statement-checked")
    check("DECISION: VALID" in out and "Matrix: not run" in out, "no 2B: 2 ACCEPT + statement → VALID")
    verdict(rb, "MINOR")
    out = pp("gate", "A", "C7", "--subject", tp, "--statement-checked")
    check("DECISION: GAP" in out and "Next: repair + Phase 2C" in out, "ACCEPT + MINOR → GAP, repair")


def telemetry_library_tests():
    print("\n== telemetry: task / done / gate / pin records, yield table")
    tel = os.path.join(S, "run", "telemetry.jsonl")
    recs = [json.loads(l) for l in open(tel)]
    n_tasks = len(os.listdir(os.path.join(S, "run", "tasks")))
    check(sum(r["event"] == "task" for r in recs) == n_tasks, "one task record per task created so far")
    prover = next(r for r in recs if r["event"] == "task" and r["role"] == "prover")
    check(prover["lessons"]["role"] != "-" and prover["lessons"]["problem"] != "-", "task record has lessons versions")
    check(any(r["event"] == "gate" for r in recs), "pp.py gate writes a gate record")

    pp("open", "A", "C11")
    c11 = os.path.join(S, "run", "A", "C11")
    write(os.path.join(c11, "target.md"), "t\n")
    tp = last_task(pp("task", "A", "C11", "--phase", "1", "--role", "prover", *STOP))
    fake_proof(tp)
    ra = last_task(pp("task", "A", "C11", "--phase", "2", "--subject", tp, *STOP))
    rb = last_task(pp("task", "A", "C11", "--phase", "GATE", "--subject", tp, *STOP))
    verdict(ra, "ACCEPT")
    verdict(rb, "ACCEPT")
    pp("done", tp, "--tokens", "42000", "--ms", "600000", "--tool-uses", "12")
    pp("done", ra, "--tokens", "8000")
    pp("done", "A-C11-999", ok=False, label="done on a task that does not exist")
    check("DECISION: VALID" in pp("gate", "A", "C11", "--subject", tp, "--statement-checked"), "C11 gate VALID")

    print("\n== gate on a computational subject (no proof.md)")
    ts = last_task(pp("task", "A", "C11", "--phase", "1", "--role", "searcher", *STOP))
    write(T(ts, "out", "claims.md"), "| claim | status |\n| U = 34 | CHECKED |\n")
    write(T(ts, "out", "best.txt"), "0000\n1111\n")
    for phase in ("2", "GATE"):
        tr = last_task(pp("task", "A", "C11", "--phase", phase, "--subject", ts, *STOP))
        verdict(tr, "ACCEPT")
    g = pp("gate", "A", "C11", "--subject", ts, "--statement-checked")
    check("DECISION: VALID" in g, "a computational subject can be gated (claims.md is its version)")
    check("proof version: current" in g, "the referee's copy of claims.md is version-checked")
    tbk = last_task(pp("task", "A", "C11", "--phase", "2C", "--obstacles", tp, *STOP))
    write(T(tbk, "out", "verdict.md"), "STUCK\nno route beyond step 2\n")
    pp("done", tbk)
    ts = last_task(pp("task", "A", "C11", "--phase", "1", "--role", "searcher", *STOP))
    write(T(ts, "out", "best.txt"), "1 2 3\n")
    pp("done", ts, "--score", "17")
    pp("pin", "A", "C11", T(ts, "out", "best.txt"))
    out = pp("telemetry", "--tasks")
    row = lambda t: next((l for l in out.splitlines() if l.startswith(f"| {t} |")), "")
    check("| yes |" in row(tp) and "proof.md" in row(tp) and "| 42000 | 10.0 |" in row(tp),
          "prover: out files, tokens, minutes, fed by VALID gate")
    check("ACCEPT" in row(ra) and "| yes |" in row(ra), "accepting referee of a VALID gate counts as fed")
    check("STUCK" in row(tbk) and "| no |" in row(tbk), "breaker ADVERSARY label read from verdict.md")
    check("| 17 |" in row(ts) and "| yes |" in row(ts), "searcher score recorded; pinned artefact counts as fed")
    check("not returned" in row(rb), "task without 'done' shows as not returned")
    out = pp("telemetry", "--by", "role")
    check(re.search(r"\| prover \| \d+ \| \d+ \| [1-9]\d* \| [1-9]", out) is not None, "grouped by role: prover proofs + fed")
    check("Not marked returned" in out and rb in out, "grouped view lists tasks not marked returned")
    check(re.search(r"\| prover r\d+ p\d+ \|", pp("telemetry", "--by", "lessons")) is not None,
          "grouped by lessons version (role r*, problem p*)")
    pp("telemetry", "--by", "colour", ok=False, label="unknown group key rejected")

    print("\n== technique library: admission, inbox rules, blindness")
    accepted = os.path.join(c11, "accepted")
    write(os.path.join(c11, "checker", "exact.py"), "from fractions import Fraction\n")
    write(os.path.join(c11, "checker", "notes.py"), "# idea from arXiv:1234.5678\n")
    pp("lib", "add", "raw", T(ts, "out", "best.txt"), "--kind", "code", "--what", "w", "--evidence", "e", ok=False,
       label="lib add refuses a task's raw out/ (not verified)")
    pp("lib", "add", "lem", os.path.join(c11, "checker", "exact.py"), "--kind", "lemma", "--what", "w", "--evidence", "e",
       ok=False, label="lib add refuses a lemma from checker/")
    pp("lib", "add", "Bad_Name", os.path.join(accepted, "best.txt"), "--kind", "code", "--what", "w", "--evidence", "e",
       ok=False, label="lib add refuses a non-slug name")
    pp("lib", "add", "exact", os.path.join(c11, "checker", "exact.py"), os.path.join(accepted, "best.txt"),
       "--kind", "code", "--what", "exact rational helpers", "--evidence", "crosstest 200/200")
    entry = os.path.join(S, "run", "library", "A-exact")
    check(os.path.isfile(os.path.join(entry, "files", "exact.py")) and "KIND: code" in open(os.path.join(entry, "ENTRY.md")).read()
          and len(open(os.path.join(entry, "MANIFEST.sha256")).read().splitlines()) == 2,
          "entry named <P>-NAME with files/, ENTRY.md, MANIFEST.sha256")
    pp("lib", "add", "exact", os.path.join(accepted, "best.txt"), "--kind", "code", "--what", "w", "--evidence", "e",
       ok=False, label="lib add refuses a duplicate entry")
    write(os.path.join(accepted, "lemma.md"), "Lemma. x <= y.\nProof. ...\n")
    pp("lib", "add", "lemma1", os.path.join(accepted, "lemma.md"), "--kind", "lemma", "--what", "x<=y", "--evidence", "gate VALID")
    pp("lib", "add", "litcode", os.path.join(c11, "checker", "notes.py"), "--kind", "code", "--what", "w", "--evidence", "e")

    tl = last_task(pp("task", "A", "C11", "--phase", "1", "--role", "searcher", "--lib", "A-exact", *STOP))
    check(os.path.isfile(T(tl, "inbox", "library", "A-exact", "files", "exact.py")), "BLIND searcher gets library code")
    brief = open(T(tl, "brief.md")).read()
    check("LIBRARY: inbox/library/" in brief and "library/A-exact" in brief, "brief has LIBRARY note and INBOX entry")
    pp("task", "A", "C11", "--phase", "1", "--role", "prover", "--lib", "A-lemma1", *STOP, ok=False,
       label="BLIND refuses a library lemma")
    pp("task", "A", "C11", "--phase", "1", "--role", "prover", "--lib", "A-litcode", *STOP, ok=False,
       label="BLIND refuses library code with literature markers")
    pp("task", "A", "C11", "--phase", "WAVE", "--role", "prover", "--regime", "FRESH", "--angle", "x",
       "--lib", "A-lemma1", "--lib", "A-litcode", *STOP, label="FRESH prover may take a lemma and marked code")
    pp("task", "A", "C11", "--phase", "2", "--subject", tp, "--lib", "A-exact", *STOP, ok=False,
       label="referee (clean-room) refuses --lib")
    pp("task", "A", "C11", "--phase", "0", "--lib", "A-exact", *STOP, ok=False, label="checker-builder refuses --lib")
    pp("task", "A", "C11", "--phase", "1", "--role", "prover", "--lib", "A-nothing", *STOP, ok=False,
       label="unknown library entry")
    check("A-exact" in pp("telemetry", "--by", "lib"), "telemetry groups by library entry")
    check("| A-exact | code | exact rational helpers | crosstest 200/200 | here |" in pp("lib", "list"), "lib list (local)")


def branch_tests():
    print("\n== library + lessons across branches")
    g = lambda cmd: subprocess.run(cmd, shell=True, cwd=S, check=True)
    g("git checkout -qb hbranch")
    write(os.path.join(S, "run", "H", "C1", "accepted", "sa.py"), "def anneal(): pass\n")
    write(os.path.join(S, "run", "A", "lessons.md"), "version: 1\n# Lessons: problem A\n\n- check small cases first (A-C1-002)\n")
    pp("lib", "add", "annealer", os.path.join(S, "run", "H", "C1", "accepted", "sa.py"),
       "--kind", "code", "--what", "SA harness", "--evidence", "pinned H-C1")
    g("git add -A && git -c user.email=t@t -c user.name=t commit -qm h && git checkout -q main")
    check(not os.path.exists(os.path.join(S, "run", "library", "H-annealer")), "entry lives only on hbranch")
    out = pp("lib", "list", "--branches", "hbranch", "nolib")
    check("| H-annealer | code | SA harness | pinned H-C1 | hbranch |" in out and "No run/library on: nolib" in out,
          "lib list shows other branches' entries and branches without a library")
    pp("lib", "import", "hbranch", "H-annealer")
    check(os.path.isfile(os.path.join(S, "run", "library", "H-annealer", "files", "sa.py")), "lib import copies the entry")
    pp("lib", "import", "hbranch", "H-annealer", ok=False, label="lib import refuses an entry already here")
    pp("lib", "import", "hbranch", "H-nothing", ok=False, label="lib import of a missing entry")
    shutil.rmtree(os.path.join(S, "run", "library", "H-annealer"))
    g("git -c user.email=t@t -c user.name=t commit -qam imports && git checkout -q hbranch "
      "&& echo tampered >> run/library/H-annealer/files/sa.py "
      "&& git -c user.email=t@t -c user.name=t commit -qam t && git checkout -q main")
    pp("lib", "import", "hbranch", "H-annealer", ok=False, label="lib import refuses a manifest mismatch")
    check(not os.path.exists(os.path.join(S, "run", "library", "H-annealer")), "failed import leaves nothing behind")
    out = pp("lessons", "--branches", "main", "hbranch", "gone")
    check("## hbranch: problem A (version: 1)" in out and "check small cases first" in out
          and "## main: problem A (version: 0)" in out and "No run/ on: gone" in out,
          "lessons lists each branch's problem lessons")
    check("problem library" not in out and "problem tasks" not in out, "lessons skips tasks/ and library/")


def board_report_tests():
    print("\n== board, status, report, summary")
    pp("board", "--regenerate")
    b = open(os.path.join(S, "run", "board.md")).read()
    check(b.startswith("# Board: problem A,") and "| Phase |" in b and "| Robustness |" in b
          and "## Contested cells (tell the humans)" in b, "regenerated board has new columns + contested section")
    pp("board", "A-C1", "--pts", "1", "--cell-status", "SOLVED", "--robustness", "–", "--phase", "5")
    pp("board", "A-C2", "--pts", "2", "--cell-status", "PARTIAL", "--robustness", "ROBUST")
    pp("board", "A-C3", "--pts", "3", "--cell-status", "PARTIAL", "--robustness", "CONTESTED")
    pp("board", "A-C4", "--pts", "5", "--cell-status", "PARTIAL", "--robustness", "UNSUPPORTED")
    pp("board", "A-C5", "--pts", "8", "--cell-status", "COUNTEREXAMPLE")
    pp("board", "A-C6", "--pts", "13", "--cell-status", "NOT SOLVED")
    pp("board", "A-C2", "--cell-status", "DONE", ok=False, label="invalid cell status rejected")
    pp("board", "A-C2", "--robustness", "SOLID", ok=False, label="invalid robustness rejected")
    pp("board", "--note", "contested", "A-C3: step 2 disputed")
    b = open(os.path.join(S, "run", "board.md")).read()
    check("A-C3: step 2 disputed" in b.split("## Contested cells")[1].split("##")[0], "contested note in its section")
    old = ("# Board: updated --:--, run time 0:00 of 7:00\n\n| Cell | Pts | Tier | Cell status | Claim status | "
           "Best so far | Live lineages | Next wave | Time used |\n|---|---|---|---|---|---|---|---|---|\n"
           "| A-C1 | 1 | T0 | SOLVED | PROVED | x | – | done | 0:10 |\n\n## Partial cells: established / remaining gap\n"
           "- [10:00] old note\n")
    write(os.path.join(S, "run", "board.md"), old)
    pp("board", "--regenerate", label="old-format board migrates")
    b = open(os.path.join(S, "run", "board.md")).read()
    check("| A-C1 | 1 | T0 |  | SOLVED | PROVED |  | x | – | done | 0:10 |" in b and "- [10:00] old note" in b,
          "migration keeps rows (Next wave → Next) and notes")
    write(os.path.join(S, "run", "board.md"), "")
    for args in (["A-C1", "--pts", "1", "--cell-status", "SOLVED"], ["A-C2", "--pts", "2", "--cell-status", "PARTIAL"],
                 ["A-C3", "--pts", "3", "--cell-status", "PARTIAL", "--robustness", "CONTESTED"],
                 ["A-C4", "--pts", "5", "--cell-status", "PARTIAL"], ["A-C5", "--pts", "8", "--cell-status", "COUNTEREXAMPLE"],
                 ["A-C6", "--pts", "13", "--cell-status", "NOT SOLVED"]):
        pp("board", *args)

    out = pp("status", "A")
    check("| A-C2 |" in out and "ROBUST" in out and "gate" in out and "2B-XV:2" in out, "status table per phase")

    pp("report")
    r = open(os.path.join(S, "run", "A", "report.md")).read()
    top = r.split("## Top cells for human attention")[1].split("##")[0]
    order = re.findall(r"- (A-C\d)", top)
    check(order == ["A-C5", "A-C3", "A-C4"], f"top 3: counterexample/contested first, then PARTIAL by points ({order})")
    check("| Robustness |" in r and "C1/final_report.md" in r, "report has Robustness + final report link")
    s = open(os.path.join(S, "run", "SUMMARY.md")).read()
    check("| Counterexample | Not solved |" in s and "C5" in s.split("| A |")[1].split("\n")[0], "SUMMARY has 5 statuses")
    check("| library |" not in s and not os.path.exists(os.path.join(S, "run", "library", "report.md")),
          "report treats run/library as the library, not a problem")

    subprocess.run("git init -q -b main && git add -A && git -c user.email=t@t -c user.name=t commit -qm s "
                   "&& git checkout -qb other && sed -i '' 's/| A |/| H |/' run/SUMMARY.md "
                   "&& git -c user.email=t@t -c user.name=t commit -qam h && git checkout -q main",
                   shell=True, cwd=S, check=True)
    out = pp("summary", "--branches", "main", "other", "missing_branch")
    check("| A |" in out and "| H |" in out and "- missing_branch" in out and out.count("A-C5") >= 2,
          "summary merges rows + top cells across branches, lists missing ones")


if __name__ == "__main__":
    setup()
    phase_tests()
    matrix_gate_tests()
    telemetry_library_tests()
    board_report_tests()
    branch_tests()
    print(f"\n{'ALL PASSED' if not fails else f'{len(fails)} FAILED: ' + '; '.join(fails)}")
    sys.exit(1 if fails else 0)
