TASK: B-C4-005      ROLE: prover      REGIME: BLIND
PHASE: 1   MODE: -   BRANCH: -
SUBJECT: -
TIME BOX: 60 minutes
READ ONLY: run/tasks/B-C4-005/ (this brief + inbox/). Do not open anything else under run/.
WRITE ONLY: run/tasks/B-C4-005/out/
TARGET: # Target: B-C4 (One Above a Triangular Number, 5 points, written proof)

Definitions (verbatim, run/B/statement.md): partition, shift B (positive numbers among lambda_i - 1, plus one part s),
cyclic (B^i(lambda) = lambda for some i >= 1), d_B(lambda) = min{i >= 0: B^i(lambda) cyclic},
D_B(n) = max over partitions of n of d_B; T_k = k(k+1)/2; rank.

Cell text (verbatim): "The first family just above a triangular number: n = T_{k-1} + 1, that is, n = 11, 16, 22, 29, ...
for k = 5, 6, 7, 8, .... Determine D_B(T_{k-1} + 1) for every k >= 5, with proof of both bounds."

Exact target (exact extremal value; the halves are gated separately):
- A formula F(k) with D_B(T_{k-1} + 1) = F(k) for EVERY k >= 5.
- UPPER: d_B(lambda) <= F(k) for every partition lambda of T_{k-1} + 1, every k >= 5.
- LOWER: an explicit partition lambda^(k) of T_{k-1} + 1 (a function of k) with d_B(lambda^(k)) = F(k), every k >= 5,
  its orbit tracked symbolically in k.
Hand-in: written proof (LaTeX). Computation only if exhaustive over a finite set the argument reduced the problem to
(code included, < 10 min); tables for finitely many k prove nothing for all k.
STATEMENT RULE: Work from the exact statement in TARGET. Preserve every definition, quantifier, parameter range and hand-in requirement. Never infer the question from a cell's title.
ASSUMPTIONS: gated claims you may use without proof (statements also in inbox/statement.md): (B-C1) for every k >= 1 and 1 <= r <= k, with n = T_{k-1} + r, a partition of n is cyclic iff it equals lambda(eps) = (k-1+eps_1, k-2+eps_2, ..., 1+eps_{k-1}, eps_k) (last entry deleted when 0) for some eps in {0,1}^k with eps_1+...+eps_k = r, and B(lambda(eps)) = lambda(eps_k, eps_1, ..., eps_{k-1}); (B-C2) for every k >= 1, D_B(T_k) = k^2 - k. If you use one, check that its hypotheses hold exactly.
STOPPING CONDITION: stop when out/proof.md proves both bounds for every k >= 5 and every ladder rung is PROVED, or when the same rung fails twice
LESSONS: role-lessons.md v0, problem-lessons.md v0
RULES: any computation must be exact or interval arithmetic, code included, runtime < 10 min; state exactly what is established; d_B is the time to ENTER a cycle (d_B = 0 for cyclic partitions), not the first repeat time; the new part equals the number s of piles BEFORE removing cards, and it is sorted into the partition; the formula must hold for EVERY k >= 5, with both bounds proved for all k; a table for finitely many k proves nothing for all k; computation only if exhaustive over a finite set your argument reduced the problem to (code included, under 10 minutes)
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
