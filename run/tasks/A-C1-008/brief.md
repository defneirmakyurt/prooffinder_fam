TASK: A-C1-008      ROLE: scribe      REGIME: RECORD
PHASE: 5   MODE: REPORT   BRANCH: -
SUBJECT: -
TIME BOX: 20 minutes
READ ONLY: run/tasks/A-C1-008/ (this brief + inbox/). Do not open anything else under run/.
WRITE ONLY: run/tasks/A-C1-008/out/
TARGET: A-C1 "Lines in the Plane" (1 point, written proof). Verbatim: "We begin in the plane (d = 2), where the conjectured optimum splits the N lines as evenly as possible between two perpendicular directions. Let l_1, ..., l_N be lines in R^2. Prove that S(l_1, ..., l_N) <= (pi/2) floor(N^2/4)."
Exact target: for every N and all lines l_1, ..., l_N through the origin of R^2 (repetitions allowed), S(l_1, ..., l_N) = sum_{1<=i<j<=N} theta(l_i, l_j) <= (pi/2) floor(N^2/4), where theta(l, l') in [0, pi/2] is the acute (non-obtuse) angle between the lines, theta = arccos|<x, x'>| for spanning unit vectors x, x'. Definitions exactly as in inbox/statement.md.
Hand-in: a complete written proof; a step may rest on computation only with code included, running under 10 minutes, and rigorous (exact or interval arithmetic, or a bound on the numerical error). Say whether the cell is solved or partial.
STATEMENT RULE: Work from the exact statement in TARGET. Preserve every definition, quantifier, parameter range and hand-in requirement. Never infer the question from a cell's title.
ASSUMPTIONS: none beyond the statement
STOPPING CONDITION: stop when out/final_report.md has all 8 sections with every statement cited
LESSONS: role-lessons.md v0, problem-lessons.md v0
RULES: any computation must be exact or interval arithmetic, code included, runtime < 10 min; state exactly what is established
RETURN: only the report block from your agent instructions, at most 200 words plus RAN lines.
        Full work goes in out/.
INBOX: role-lessons.md v0, problem-lessons.md v0, statement.md, target.md, checklist-G.md, record/ (tasks/<id>/brief.md + out/, cell/)
PYTHON: /Users/raducucu/bainsahackathon/.venv/bin/python3 (sympy, mpmath, networkx, python-flint, python-sat); plain python3 lacks them.
        Checkers and anything a judge reruns stay stdlib-only unless the brief says otherwise.

Reports introduce no new mathematics. Never upgrade a status given in the brief.
Fill in RAN exactly for every command you ran.

Phase 5. Inbox/record/ holds the cell's full record, paths preserved (record/tasks/<id>/out/...).
Write out/final_report.md in the section 14 format. Every statement cites its artefact by relative path and
step number (e.g. "tasks/A-C1-003/out/proof.md, step 4"); a claim with no artefact is deleted.
State in Limitations: "agent agreement is evidence, not proof".

CELL STATUS: SOLVED
CLAIM STATUS (do not upgrade): PROVED
