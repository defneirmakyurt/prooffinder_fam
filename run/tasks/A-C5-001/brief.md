TASK: A-C5-001      ROLE: prover      REGIME: BLIND
PHASE: 1   MODE: -   BRANCH: -
SUBJECT: -
TIME BOX: 45 minutes
READ ONLY: run/tasks/A-C5-001/ (this brief + inbox/). Do not open anything else under run/.
WRITE ONLY: run/tasks/A-C5-001/out/
TARGET: # Target: A-C5 — "d+2 Lines in R^d" (8 pts)

## Exact statement (verbatim cell text)

The case N=d+2 in every dimension, with the same conjectured optimum: the d coordinate axes,
two of them repeated. Prove that for every d≥2, any d+2 lines in R^d satisfy

    S ≤ (C(d+2,2) - 2) * π/2

where C(n,2) = n(n-1)/2, S(ℓ_1,...,ℓ_{d+2}) = Σ_{i<j} θ(ℓ_i,ℓ_j), θ(ℓ,ℓ') = arccos|⟨x,x'⟩| ∈ [0,π/2]
for unit vectors x,x' spanning ℓ,ℓ', and repetitions among the ℓ_i are allowed.

## Parameter range

- d ≥ 2 (all integers), N = d+2 lines (with repetition allowed).
- No restriction on the lines beyond "N=d+2 lines through the origin of R^d".

## Deliverable

A complete, general (every d≥2) written proof, or an honest PARTIAL result (e.g. proved for a
family of d, or for A-C4's two concrete instances only) with the exact remaining gap stated.
STATEMENT RULE: Work from the exact statement in TARGET. Preserve every definition, quantifier, parameter range and hand-in requirement. Never infer the question from a cell's title.
ASSUMPTIONS: none beyond the statement
STOPPING CONDITION: stop once you have either a complete proof for every d>=2 or you are stuck on the same obstruction after two distinct approaches
LESSONS: role-lessons.md v0, problem-lessons.md v0
RULES: any computation must be exact or interval arithmetic, code included, runtime < 10 min; state exactly what is established
RETURN: only the report block from your agent instructions, at most 200 words plus LADDER / RAN lines.
        Full work goes in out/.
INBOX: role-lessons.md v0, problem-lessons.md v0, statement.md, target.md, checklist-G.md
PYTHON: /home/user/bainsahackathon/.venv/bin/python3 (sympy, mpmath, networkx, python-flint, python-sat); plain python3 lacks them.
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
