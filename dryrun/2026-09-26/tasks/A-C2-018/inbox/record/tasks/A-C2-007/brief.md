TASK: A-C2-007      ROLE: triage      REGIME: BLIND
PHASE: 2A   MODE: -   BRANCH: -
SUBJECT: -
TIME BOX: 15 minutes
READ ONLY: run/tasks/A-C2-007/ (this brief + inbox/). Do not open anything else under run/.
WRITE ONLY: run/tasks/A-C2-007/out/
TARGET: A-C2 "An Orthogonality Lemma" (2 points, written proof). Verbatim: "A statement about a chain of vectors, in which each vector may fail to be orthogonal only to its immediate neighbours in the list. Let m >= 2 and let x_1, ..., x_m be unit vectors in R^(m-1) with <x_i, x_j> = 0 whenever |i - j| >= 2. Prove that sum_{i=1}^{m-1} theta(x_i, x_{i+1}) <= (m - 2) pi/2, where theta(x, y) = arccos |<x, y>|."
Exact target: for every integer m >= 2 and all unit vectors x_1, ..., x_m in R^(m-1) (dimension m-1, not m) such that <x_i, x_j> = 0 for all i, j with |i - j| >= 2, the chain sum sum_{i=1}^{m-1} theta(x_i, x_{i+1}) <= (m - 2) pi/2, where theta(x, y) = arccos|<x, y>| in [0, pi/2]. Only consecutive pairs (i, i+1) are summed. Definitions exactly as in inbox/statement.md.
Hand-in: a complete written proof; a step may rest on computation only with code included, running under 10 minutes, and rigorous (exact or interval arithmetic, or a bound on the numerical error). Say whether the cell is solved or partial.
STATEMENT RULE: Work from the exact statement in TARGET. Preserve every definition, quantifier, parameter range and hand-in requirement. Never infer the question from a cell's title.
ASSUMPTIONS: none beyond the statement
STOPPING CONDITION: Stop when out/triage.md rates all five branches and out/selected_branches.txt is written.
LESSONS: role-lessons.md v0, problem-lessons.md v0
RULES: any computation must be exact or interval arithmetic, code included, runtime < 10 min; state exactly what is established
RETURN: only the report block from your agent instructions, at most 200 words plus RAN lines.
        Full work goes in out/.
INBOX: role-lessons.md v0, problem-lessons.md v0, statement.md, target.md, checklist-G.md, obstacles/A-C2-001/ (stuck.md), obstacles/A-C2-002/ (stuck.md), obstacles/A-C2-004/ (verdict.md), obstacles/A-C2-005/ (verdict.md)
PYTHON: /home/user/bainsahackathon/.venv/bin/python3 (sympy, mpmath, networkx, python-flint, python-sat); plain python3 lacks them.
        Checkers and anything a judge reruns stay stdlib-only unless the brief says otherwise.

Phase 2A. Do not solve the cell. Inbox/obstacles/ holds stuck.md and verdict.md files (not proofs).
For each branch ALGEBRAIC, TOPOLOGICAL, ANALYSIS, NUMBER-THEORY, DISCRETE write in out/triage.md:
RELEVANCE (HIGH / MEDIUM / LOW / NONE), REASON (a paragraph tied to the cell's actual structure),
ENTRY POINT (a concrete first step; none nameable => at most LOW), RISK (likely failure + early warning sign).
Rate relevance to the problem's structure, not to a guessed answer.
Selection: HIGH and MEDIUM run as solvers; NONE is dropped; keep the best LOW only to reach two solver branches;
a dropped branch may be tagged verifier-only. Log every elimination with its reason.
Write out/selected_branches.txt (section 11).

BUDGET (head): this cell is worth 2 points, and the head's rule for such cells is two branches. Keep exactly two branches in selected_branches.txt, both as solver (the two best; the best LOW only if fewer than two are HIGH/MEDIUM), and no verifier-only branch: every kept branch costs one cross-verifier call per proof and the budget has no room for a third. Rate all five branches honestly anyway; the cap applies only to selected_branches.txt, and every branch it drops goes in the re-admission list with its rating.
