TASK: A-C4-003      ROLE: prover      REGIME: BLIND
PHASE: 1   MODE: -   BRANCH: -
SUBJECT: -
TIME BOX: 60 minutes
READ ONLY: run/tasks/A-C4-003/ (this brief + inbox/). Do not open anything else under run/.
WRITE ONLY: run/tasks/A-C4-003/out/
TARGET: Prove BOTH: (a) any 5 lines through the origin of R^3 (repetitions allowed) satisfy S <= 4*pi; (b) any 6 lines through the origin of R^4 (repetitions allowed) satisfy S <= 13*pi/2. Here S = sum over pairs i<j of theta(l_i, l_j), with theta(l, l') = arccos |<x, x'>| for spanning unit vectors (the acute angle, in [0, pi/2]). A computer-assisted step is allowed only with code included, runtime under 10 minutes on a laptop, exact or interval arithmetic (or a proved bound on the numerical error), and a written argument explaining why the computation proves the claim.
STATEMENT RULE: Work from the exact statement in TARGET. Preserve every definition, quantifier, parameter range and hand-in requirement. Never infer the question from a cell's title.
ASSUMPTIONS: none beyond the statement
STOPPING CONDITION: stop when out/proof.md proves both instances and every ladder rung is PROVED, or when the same rung fails twice
LESSONS: role-lessons.md v0, problem-lessons.md v0
RULES: any computation must be exact or interval arithmetic, code included, runtime < 10 min; state exactly what is established; theta is the angle between the spanned lines (absolute value of the inner product), in [0, pi/2]; repetitions allowed: lines may coincide and may span a proper subspace; both instances (5 lines in R^3 and 6 lines in R^4) are required; a computer-assisted step needs code, interval or exact arithmetic, runtime under 10 minutes, and a written argument that the computation proves the claim; floating-point checks are evidence only
RETURN: only the report block from your agent instructions, at most 200 words plus LADDER / RAN lines.
        Full work goes in out/.
INBOX: role-lessons.md v0, problem-lessons.md v0, statement.md, target.md, checklist-G.md
PYTHON: /Users/defneirmakyurt/bainsahackathon/.venv/bin/python3 (sympy, mpmath, networkx, python-flint, python-sat); plain python3 lacks them.
        Checkers and anything a judge reruns stay stdlib-only unless the brief says otherwise.

First write out/plan.md: TARGET as a ladder of numbered rungs (lemmas, special cases, reductions)
with dependencies. Work through it in order, marking each rung
PROVED / CHECKED / GAP / REFUTED / NOT STARTED.
Write out/proof.md. First line: the exact statement you prove, no more.
Then numbered steps; each justified by a definition, an earlier step, or a named lemma with exact reference.
"Clearly", "routine", "obviously", "similarly" and "by symmetry" may not replace an argument. Write the step out.
Mark anything you are not sure of [GAP].
Also write out/claims.md (claim | status | where proved), out/stuck.md (exact point of failure, or "none"),
and out/code/README.md (how to run any code) if you wrote code.
Check inbox/checklist-G.md item by item before you finish.
Numerics may guide you; any step resting on computation must include code in out/code/,
exact or interval arithmetic, runtime < 10 min.
If you executed code, fill in RAN exactly: what ran, parameter range, COMPLETED / TIMED OUT / PARTIAL, measured runtime.

Derive everything from first principles. Standard textbook tools are fine; results specific to this problem or its literature are not: if you recognise a known theorem about this problem, do not use it, work the argument out yourself. Cite no papers or authors.
