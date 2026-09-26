TASK: B-C3-011      ROLE: prover      REGIME: EXPLOIT
PHASE: REPAIR   MODE: -   BRANCH: -
SUBJECT: B-C3-004
TIME BOX: 40 minutes
READ ONLY: run/tasks/B-C3-011/ (this brief + inbox/). Do not open anything else under run/.
WRITE ONLY: run/tasks/B-C3-011/out/
TARGET: # Target: B-C3(a) and the UPPER half of B-C3(b)

Definitions as in run/B/statement.md (partition, shift B, cyclic, d_B, D_B, T_k, rank).
(a) For every k >= 4, every non-triangular n with T_{k-1} < n < T_k, and every partition lambda of n:
    d_B(lambda) <= k^2 - 2k - 1.
(b-upper) In particular D_B(T_k - 1) <= k^2 - 2k - 1 for every k >= 4 (n = T_k - 1 is non-triangular of rank k).
    (Lower half D_B(T_k-1) >= k^2-2k-1 is already proved; with (a) this gives D_B(T_k-1) = k^2-2k-1.)
A complete, self-contained, line-by-line written proof valid for every k >= 4; finite checks prove nothing for all k.
STATEMENT RULE: Work from the exact statement in TARGET. Preserve every definition, quantifier, parameter range and hand-in requirement. Never infer the question from a cell's title.
ASSUMPTIONS: Gated claims: B-C1 (Cell 1: for n = T_{k-1}+r the cyclic partitions are (k-1+e_1,...,1+e_{k-1},e_k), e in {0,1}^k, sum e = r). B-C2 (Cell 2, proved and verified: D_B(T_k) = k^2-k; its accepted proof is in inbox/gated_B-C2_proof.md where provided).
STOPPING CONDITION: Stop when (a) is PROVED for every k>=4 and every non-triangular n of rank k, or the same rung fails twice. Suggested route: adapt the c-sequence argument B1-B9 of the gated Cell 2 proof to non-triangular n (end-of-orbit lemma B4/B5 changes because the cyclic set is a rotation class, not a fixed point).
LESSONS: role-lessons.md v0, problem-lessons.md v0
RULES: any computation must be exact or interval arithmetic, code included, runtime < 10 min; state exactly what is established; Write the final proof in proof.md using LaTeX math notation ($...$), line by line; self-contained.
RETURN: only the report block from your agent instructions, at most 200 words plus LADDER / RAN lines.
        Full work goes in out/.
INBOX: role-lessons.md v0, problem-lessons.md v0, statement.md, target.md, checklist-G.md, subject/ (proof.md, claims.md, code of B-C3-004), gated_B-C2_proof.md
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

Inbox holds the current best proof and its gate report or critique. Repair the listed problems first. If the approach cannot be repaired, say so and why.
