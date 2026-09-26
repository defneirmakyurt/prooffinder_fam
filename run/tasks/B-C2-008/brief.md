TASK: B-C2-008      ROLE: prover      REGIME: FRESH
PHASE: WAVE   MODE: -   BRANCH: -
SUBJECT: -
TIME BOX: 40 minutes
READ ONLY: run/tasks/B-C2-008/ (this brief + inbox/). Do not open anything else under run/.
WRITE ONLY: run/tasks/B-C2-008/out/
TARGET: run/B/C2/target_upper.md
STATEMENT RULE: Work from the exact statement in TARGET. Preserve every definition, quantifier, parameter range and hand-in requirement. Never infer the question from a cell's title.
ASSUMPTIONS: Gated claim B-C1 (Cell 1): delta_k is the only cyclic partition of T_k and every orbit of T_k reaches it; for n = T_{k-1}+r the cyclic partitions are (k-1+e_1,...,1+e_{k-1},e_k), e in {0,1}^k, sum e = r.
STOPPING CONDITION: Stop when the upper bound is PROVED for every k and every partition, or when the same rung fails twice; report GAP rungs honestly.
LESSONS: role-lessons.md v0, problem-lessons.md v0
RULES: any computation must be exact or interval arithmetic, code included, runtime < 10 min; state exactly what is established; Write the final proof in proof.md using LaTeX math notation ($...$), line by line; self-contained.
RETURN: only the report block from your agent instructions, at most 200 words plus LADDER / RAN lines.
        Full work goes in out/.
INBOX: role-lessons.md v0, problem-lessons.md v0, statement.md, target.md, checklist-G.md
PYTHON: /Users/radu.cucu/Developer/bainsahackathon/.venv/bin/python3 (sympy, mpmath, networkx, python-flint, python-sat); plain python3 lacks them.
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

ANGLE: potential-function. Pursue this angle; if you abandon it, say why.
