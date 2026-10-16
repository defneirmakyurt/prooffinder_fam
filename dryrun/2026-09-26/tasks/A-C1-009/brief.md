TASK: A-C1-009      ROLE: auditor      REGIME: RECORD
PHASE: AUDIT   MODE: -   BRANCH: -
SUBJECT: A-C1-008
TIME BOX: 20 minutes
READ ONLY: run/tasks/A-C1-009/ (this brief + inbox/). Do not open anything else under run/.
WRITE ONLY: run/tasks/A-C1-009/out/
TARGET: A-C1 "Lines in the Plane" (1 point, written proof). Verbatim: "We begin in the plane (d = 2), where the conjectured optimum splits the N lines as evenly as possible between two perpendicular directions. Let l_1, ..., l_N be lines in R^2. Prove that S(l_1, ..., l_N) <= (pi/2) floor(N^2/4)."
Exact target: for every N and all lines l_1, ..., l_N through the origin of R^2 (repetitions allowed), S(l_1, ..., l_N) = sum_{1<=i<j<=N} theta(l_i, l_j) <= (pi/2) floor(N^2/4), where theta(l, l') in [0, pi/2] is the acute (non-obtuse) angle between the lines, theta = arccos|<x, x'>| for spanning unit vectors x, x'. Definitions exactly as in inbox/statement.md.
Hand-in: a complete written proof; a step may rest on computation only with code included, running under 10 minutes, and rigorous (exact or interval arithmetic, or a bound on the numerical error). Say whether the cell is solved or partial.
STATEMENT RULE: Work from the exact statement in TARGET. Preserve every definition, quantifier, parameter range and hand-in requirement. Never infer the question from a cell's title.
ASSUMPTIONS: none beyond the statement
STOPPING CONDITION: stop when every citation in final_report.md has been checked against the artefact it names and out/audit.md gives AUDIT: PASS or AUDIT: FAIL with the failing citations listed
LESSONS: role-lessons.md v0
RULES: any computation must be exact or interval arithmetic, code included, runtime < 10 min; state exactly what is established
RETURN: only the report block from your agent instructions, at most 200 words plus RAN lines.
        Full work goes in out/.
INBOX: role-lessons.md v0, statement.md, target.md, checklist-G.md, final_report.md, record/ (tasks/<id>/brief.md + out/, cell/)
PYTHON: /Users/raducucu/bainsahackathon/.venv/bin/python3 (sympy, mpmath, networkx, python-flint, python-sat); plain python3 lacks them.
        Checkers and anything a judge reruns stay stdlib-only unless the brief says otherwise.

Phase 5 audit. Inbox holds final_report.md and inbox/record/ (the artefacts it cites).
For every citation: does the file exist, and does the cited step say what the report claims?
List every unsupported or mis-cited statement. Write out/audit.md (section 15). Verdict PASS only if none remain.
