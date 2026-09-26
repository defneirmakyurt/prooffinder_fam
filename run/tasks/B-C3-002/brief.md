TASK: B-C3-002      ROLE: prover      REGIME: BLIND
PHASE: 1   MODE: -   BRANCH: -
SUBJECT: -
TIME BOX: 60 minutes
READ ONLY: run/tasks/B-C3-002/ (this brief + inbox/). Do not open anything else under run/.
WRITE ONLY: run/tasks/B-C3-002/out/
TARGET: # Target: B-C3 (A General Upper Bound, 3 points, written proof)

Definitions (verbatim, run/B/statement.md): a partition of n >= 1 is a weakly decreasing sequence of positive
integers with sum n (s piles). B(lambda): the positive numbers among lambda_1 - 1, ..., lambda_s - 1, together with
one extra part equal to s. lambda is cyclic if B^i(lambda) = lambda for some i >= 1.
d_B(lambda) = min{ i >= 0 : B^i(lambda) cyclic }, D_B(n) = max{ d_B(lambda) : lambda a partition of n }.
T_k = k(k+1)/2, delta_k = (k, ..., 1); rank of n = the unique k with T_{k-1} < n <= T_k.

Cell text (verbatim): "Now the numbers strictly between two consecutive triangular numbers.
(a) Prove that for every k >= 4 and every non-triangular n with T_{k-1} < n < T_k, D_B(n) <= k^2 - 2k - 1.
(b) Determine D_B(T_k - 1) exactly.
(c) Determine also, for that n, which partitions attain the maximum."

Exact targets:
(a) For every k >= 4, every n with T_{k-1} < n < T_k, and every partition lambda of n: d_B(lambda) <= k^2 - 2k - 1.
(b) A formula F(k) with D_B(T_k - 1) = F(k); state explicitly the k-range proved (the cell states none; cover as
    many k >= 1 as possible and give any small-k values separately). Both halves: upper bound over every partition
    of T_k - 1, and an explicit partition (function of k) attaining F(k), each proved for every k in the range.
(c) The exact set of partitions lambda of T_k - 1 with d_B(lambda) = D_B(T_k - 1), as explicit functions of k,
    with proof that every listed partition attains the maximum and that no other partition does.

Hand-in: a written proof (LaTeX). Computation only if exhaustive over a finite set the argument has reduced the
problem to (code included, < 10 min); small-k tables alone prove nothing for all k.
STATEMENT RULE: Work from the exact statement in TARGET. Preserve every definition, quantifier, parameter range and hand-in requirement. Never infer the question from a cell's title.
ASSUMPTIONS: Gated claim B-C1 (Cell 1, proved and verified): for n = T_{k-1}+r, 1<=r<=k, lambda is cyclic iff lambda = (k-1+e_1,...,1+e_{k-1},e_k) (final 0 dropped), e in {0,1}^k, sum e = r; B acts by B(lambda(e)) = lambda(e_k,e_1,...,e_{k-1}); delta_k is the only cyclic partition of T_k and every orbit of T_k reaches it. You may use it without proof, citing it as Cell 1.
STOPPING CONDITION: Stop when (a), (b) and (c) all have every rung PROVED, or when the same rung fails twice; report proved parts and GAP rungs honestly (partial progress counts).
LESSONS: role-lessons.md v0, problem-lessons.md v0
RULES: any computation must be exact or interval arithmetic, code included, runtime < 10 min; state exactly what is established; Write the final proof in proof.md using LaTeX math notation ($...$), line by line.
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

Derive everything from first principles. Standard textbook tools are fine; results specific to this problem or its literature are not: if you recognise a known theorem about this problem, do not use it, work the argument out yourself. Cite no papers or authors.
