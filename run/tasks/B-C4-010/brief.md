TASK: B-C4-010      ROLE: prover      REGIME: EXPLOIT
PHASE: REPAIR   MODE: -   BRANCH: -
SUBJECT: B-C4-006
TIME BOX: 60 minutes
READ ONLY: run/tasks/B-C4-010/ (this brief + inbox/). Do not open anything else under run/.
WRITE ONLY: run/tasks/B-C4-010/out/
TARGET: UPPER half of B-C4: for EVERY k >= 5 and EVERY partition lambda of n = T_{k-1} + 1, d_B(lambda) <= (k-1)(k-3). (The matching lower bound, d_B(lambda^(k)) = (k-1)(k-3) for lambda^(k) = (k-2, k-2, k-3, ..., 3, 2, 2, 1), is handled separately.) Definitions exactly as in inbox/statement.md.
STATEMENT RULE: Work from the exact statement in TARGET. Preserve every definition, quantifier, parameter range and hand-in requirement. Never infer the question from a cell's title.
ASSUMPTIONS: gated claims you may use without proof: (B-C1) for every k >= 1 and 1 <= r <= k, with n = T_{k-1} + r, a partition of n is cyclic iff it equals lambda(eps) = (k-1+eps_1, ..., 1+eps_{k-1}, eps_k) (last entry deleted when 0) for some eps in {0,1}^k with eps_1+...+eps_k = r, and B(lambda(eps)) = lambda(eps_k, eps_1, ..., eps_{k-1}); (B-C2) for every k >= 1, D_B(T_k) = k^2 - k. Rungs of the inbox proof are NOT gated: if you rely on them, keep their proofs in your write-up.
STOPPING CONDITION: stop when out/proof.md proves the UPPER half for every k >= 5 with every rung PROVED, or when the same rung fails twice
LESSONS: role-lessons.md v0, problem-lessons.md v0
RULES: any computation must be exact or interval arithmetic, code included, runtime < 10 min; state exactly what is established
RETURN: only the report block from your agent instructions, at most 200 words plus LADDER / RAN lines.
        Full work goes in out/.
INBOX: role-lessons.md v0, problem-lessons.md v0, statement.md, target.md, checklist-G.md, subject/ (proof.md, claims.md, code of B-C4-006), lineage-stuck.md
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

Inbox holds the current best proof and its gate report or critique. Repair the listed problems first. If the approach cannot be repaired, say so and why.
