TASK: A-C2-018      ROLE: scribe      REGIME: RECORD
PHASE: 5   MODE: REPORT   BRANCH: -
SUBJECT: -
TIME BOX: 25 minutes
READ ONLY: run/tasks/A-C2-018/ (this brief + inbox/). Do not open anything else under run/.
WRITE ONLY: run/tasks/A-C2-018/out/
TARGET: A-C2 "An Orthogonality Lemma" (2 points, written proof). Verbatim: "A statement about a chain of vectors, in which each vector may fail to be orthogonal only to its immediate neighbours in the list. Let m >= 2 and let x_1, ..., x_m be unit vectors in R^(m-1) with <x_i, x_j> = 0 whenever |i - j| >= 2. Prove that sum_{i=1}^{m-1} theta(x_i, x_{i+1}) <= (m - 2) pi/2, where theta(x, y) = arccos |<x, y>|."
Exact target: for every integer m >= 2 and all unit vectors x_1, ..., x_m in R^(m-1) (dimension m-1, not m) such that <x_i, x_j> = 0 for all i, j with |i - j| >= 2, the chain sum sum_{i=1}^{m-1} theta(x_i, x_{i+1}) <= (m - 2) pi/2, where theta(x, y) = arccos|<x, y>| in [0, pi/2]. Only consecutive pairs (i, i+1) are summed. Definitions exactly as in inbox/statement.md.
Hand-in: a complete written proof; a step may rest on computation only with code included, running under 10 minutes, and rigorous (exact or interval arithmetic, or a bound on the numerical error). Say whether the cell is solved or partial.
STATEMENT RULE: Work from the exact statement in TARGET. Preserve every definition, quantifier, parameter range and hand-in requirement. Never infer the question from a cell's title.
ASSUMPTIONS: none beyond the statement
STOPPING CONDITION: Stop when out/final_report.md is complete in the section 14 format, with every statement cited and a saved log for every RAN line.
LESSONS: role-lessons.md v2, problem-lessons.md v0
RULES: any computation must be exact or interval arithmetic, code included, runtime < 10 min; state exactly what is established
RETURN: only the report block from your agent instructions, at most 200 words plus RAN lines.
        Full work goes in out/.
INBOX: role-lessons.md v2, problem-lessons.md v0, statement.md, target.md, checklist-G.md, record/ (tasks/<id>/brief.md + out/, cell/)
PYTHON: /home/user/bainsahackathon/.venv/bin/python3 (sympy, mpmath, networkx, python-flint, python-sat); plain python3 lacks them.
        Checkers and anything a judge reruns stay stdlib-only unless the brief says otherwise.

Reports introduce no new mathematics. Never upgrade a status given in the brief.
Fill in RAN exactly for every command you ran.

Phase 5. Inbox/record/ holds the cell's full record, paths preserved (record/tasks/<id>/out/...).
Write out/final_report.md in the section 14 format. Every statement cites its artefact by relative path and
step number (e.g. "tasks/A-C1-003/out/proof.md, step 4"); a claim with no artefact is deleted.
State in Limitations: "agent agreement is evidence, not proof".

CELL STATUS: SOLVED
CLAIM STATUS (do not upgrade): PROVED

GATE FACTS (head): the only gated claim is A-C2-002's proof (record/cell/gate/A-C2-002.md: VALID, referees A-C2-005 VERIFY + A-C2-006 GATE, matrix ROBUST). record/cell/gate/A-C2-002.pre-2B.md is the same proof's earlier gate report, taken before any Phase 2B task existed (matrix 'not run'). The proofs of A-C2-001, A-C2-003 and A-C2-011 each have one ACCEPT and were not gated; the proofs of A-C2-010, A-C2-015 and A-C2-017 have no referee. A-C2-007 was created and never dispatched (its inbox would have shown Part S to a blind triage agent); it has no out/. Report these as they are; do not upgrade any of them.
