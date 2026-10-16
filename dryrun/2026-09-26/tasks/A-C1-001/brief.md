TASK: A-C1-001      ROLE: prover      REGIME: BLIND
PHASE: 1   MODE: -   BRANCH: -
SUBJECT: -
TIME BOX: 25 minutes
READ ONLY: run/tasks/A-C1-001/ (this brief + inbox/). Do not open anything else under run/.
WRITE ONLY: run/tasks/A-C1-001/out/
TARGET: A-C1 "Lines in the Plane" (1 point, written proof). Verbatim: "We begin in the plane (d = 2), where the conjectured optimum splits the N lines as evenly as possible between two perpendicular directions. Let l_1, ..., l_N be lines in R^2. Prove that S(l_1, ..., l_N) <= (pi/2) floor(N^2/4)."
Exact target: for every N and all lines l_1, ..., l_N through the origin of R^2 (repetitions allowed), S(l_1, ..., l_N) = sum_{1<=i<j<=N} theta(l_i, l_j) <= (pi/2) floor(N^2/4), where theta(l, l') in [0, pi/2] is the acute (non-obtuse) angle between the lines, theta = arccos|<x, x'>| for spanning unit vectors x, x'. Definitions exactly as in inbox/statement.md.
Hand-in: a complete written proof; a step may rest on computation only with code included, running under 10 minutes, and rigorous (exact or interval arithmetic, or a bound on the numerical error). Say whether the cell is solved or partial.
STATEMENT RULE: Work from the exact statement in TARGET. Preserve every definition, quantifier, parameter range and hand-in requirement. Never infer the question from a cell's title.
ASSUMPTIONS: none beyond the statement
STOPPING CONDITION: stop when out/proof.md proves the full target with no [GAP], or when the same rung fails twice
LESSONS: role-lessons.md v0, problem-lessons.md v0
RULES: any computation must be exact or interval arithmetic, code included, runtime < 10 min; state exactly what is established; citing a published result for the statement you are asked to prove does not count; lines, not vectors: theta uses |<x,y>|, so theta is in [0, pi/2]; repetitions are allowed
RETURN: only the report block from your agent instructions, at most 200 words plus LADDER / RAN lines.
        Full work goes in out/.
INBOX: role-lessons.md v0, problem-lessons.md v0, statement.md, target.md, checklist-G.md
PYTHON: /Users/raducucu/bainsahackathon/.venv/bin/python3 (sympy, mpmath, networkx, python-flint, python-sat); plain python3 lacks them.
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
