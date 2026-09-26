TASK: A-C3-001      ROLE: prover      REGIME: BLIND
PHASE: 1   MODE: -   BRANCH: -
SUBJECT: -
TIME BOX: 45 minutes
READ ONLY: run/tasks/A-C3-001/ (this brief + inbox/). Do not open anything else under run/.
WRITE ONLY: run/tasks/A-C3-001/out/
TARGET: Prove: for every integer d >= 1 and all lines l_1, ..., l_{d+1} through the origin of R^d (repetitions allowed), S(l_1, ..., l_{d+1}) = sum_{i<j} theta(l_i, l_j) <= (C(d+1, 2) - 1) * pi/2, where theta(l, l') = arccos |<x, x'>| for spanning unit vectors x, x' (the acute angle, in [0, pi/2]).
STATEMENT RULE: Work from the exact statement in TARGET. Preserve every definition, quantifier, parameter range and hand-in requirement. Never infer the question from a cell's title.
ASSUMPTIONS: gated claims you may use without proof (statements also in inbox/statement.md): (A-C1) for every N >= 0 and all lines l_1..l_N through the origin of R^2, repetitions allowed, S <= (pi/2) floor(N^2/4); (A-C2) for every m >= 2 and all unit vectors x_1..x_m in R^(m-1) with <x_i,x_j> = 0 whenever |i-j| >= 2, sum_{i=1}^{m-1} arccos|<x_i,x_{i+1}>| <= (m-2) pi/2. If you use one, check that its hypotheses hold exactly.
STOPPING CONDITION: stop when out/proof.md is complete and every ladder rung is PROVED, or when the same rung fails twice
LESSONS: role-lessons.md v0, problem-lessons.md v0
RULES: any computation must be exact or interval arithmetic, code included, runtime < 10 min; state exactly what is established; theta is the angle between the spanned lines (absolute value of the inner product), in [0, pi/2]; repetitions allowed: lines may coincide and may span a proper subspace; the claim is for every d >= 1; numerical checks are evidence only; a floating-point computation is not a proof step
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
