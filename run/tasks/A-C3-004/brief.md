TASK: A-C3-004      ROLE: triage      REGIME: BLIND
PHASE: 2A   MODE: -   BRANCH: -
SUBJECT: -
TIME BOX: 15 minutes
READ ONLY: run/tasks/A-C3-004/ (this brief + inbox/). Do not open anything else under run/.
WRITE ONLY: run/tasks/A-C3-004/out/
TARGET: Prove: for every integer d >= 1 and all lines l_1, ..., l_{d+1} through the origin of R^d (repetitions allowed), S(l_1, ..., l_{d+1}) = sum_{i<j} theta(l_i, l_j) <= (C(d+1, 2) - 1) * pi/2, where theta(l, l') = arccos |<x, x'>| for spanning unit vectors x, x' (the acute angle, in [0, pi/2]).
STATEMENT RULE: Work from the exact statement in TARGET. Preserve every definition, quantifier, parameter range and hand-in requirement. Never infer the question from a cell's title.
ASSUMPTIONS: none beyond the statement
STOPPING CONDITION: stop when triage.md and selected_branches.txt are written
LESSONS: role-lessons.md v0, problem-lessons.md v0
RULES: any computation must be exact or interval arithmetic, code included, runtime < 10 min; state exactly what is established
RETURN: only the report block from your agent instructions, at most 200 words plus RAN lines.
        Full work goes in out/.
INBOX: role-lessons.md v0, problem-lessons.md v0, statement.md, target.md, checklist-G.md
PYTHON: /Users/defneirmakyurt/bainsahackathon/.venv/bin/python3 (sympy, mpmath, networkx, python-flint, python-sat); plain python3 lacks them.
        Checkers and anything a judge reruns stay stdlib-only unless the brief says otherwise.

Phase 2A. Do not solve the cell. Inbox/obstacles/ holds stuck.md and verdict.md files (not proofs).
For each branch ALGEBRAIC, TOPOLOGICAL, ANALYSIS, NUMBER-THEORY, DISCRETE write in out/triage.md:
RELEVANCE (HIGH / MEDIUM / LOW / NONE), REASON (a paragraph tied to the cell's actual structure),
ENTRY POINT (a concrete first step; none nameable => at most LOW), RISK (likely failure + early warning sign).
Rate relevance to the problem's structure, not to a guessed answer.
Selection: HIGH and MEDIUM run as solvers; NONE is dropped; keep the best LOW only to reach two solver branches;
a dropped branch may be tagged verifier-only. Log every elimination with its reason.
Write out/selected_branches.txt (section 11).

Time-critical, easy cell (T1): keep EXACTLY two solver branches (the two best) and no verifier-only branches. There are no obstacles yet: rate from the statement alone and say so.
