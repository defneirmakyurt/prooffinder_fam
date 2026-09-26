TASK: B-C3-007      ROLE: literature      REGIME: LITERATURE
PHASE: 1L   MODE: SOLVE   BRANCH: -
SUBJECT: -
TIME BOX: 40 minutes
READ ONLY: run/tasks/B-C3-007/ (this brief + inbox/). Do not open anything else under run/.
WRITE ONLY: run/tasks/B-C3-007/out/
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
ASSUMPTIONS: Gated claim B-C1 (Cell 1): for n = T_{k-1}+r, 1<=r<=k, lambda is cyclic iff lambda = (k-1+e_1,...,1+e_{k-1},e_k) (final 0 dropped), e in {0,1}^k, sum e = r.
STOPPING CONDITION: Priority: a complete, self-contained, line-by-line written proof of (a) d_B <= k^2-2k-1 for every k >= 4 and every non-triangular n of rank k (e.g. reconstructing Griggs-Ho 1998 Thm 4.4 in full, every lemma re-proved), then (b) with the witness (k-1,k-2,k-2,k-3,...,2,1,1), then (c). A citation alone does not count. Stop when written, or state precisely what cannot be completed.
LESSONS: role-lessons.md v0, problem-lessons.md v0
RULES: any computation must be exact or interval arithmetic, code included, runtime < 10 min; state exactly what is established; Write the final proof in proof.md using LaTeX math notation ($...$), line by line.
RETURN: only the report block from your agent instructions, at most 200 words plus RAN lines.
        Full work goes in out/.
INBOX: role-lessons.md v0, problem-lessons.md v0, statement.md, target.md, checklist-G.md, earlier/B-C3-002/, earlier/B-C3-004/
PYTHON: /Users/radu.cucu/Developer/bainsahackathon/.venv/bin/python3 (sympy, mpmath, networkx, python-flint, python-sat); plain python3 lacks them.
        Checkers and anything a judge reruns stay stdlib-only unless the brief says otherwise.

You have web search and fetch. Tag every result PROVED / COMPUTER-VERIFIED / CONJECTURED, and say whether the
source contains the argument or only cites it. Flag computations whose code is unavailable and steps called
"routine" but not written down. Every claim carries a source link or a pointer to an artefact, plus a status tag.
Never present a citation as a proof of the cell itself. Never call anything new: write "not found in <sources searched>".
Your output never reaches blind agents.

Phase 1L. Inbox/earlier/ holds the Phase 1 blind results for this cell.
1. Find the literature for this cell and its neighbours, with links (out/sources.md: link, what was used, status).
2. Attempt the cell using known techniques (out/proof.md, out/claims.md).
3. Compare with the blind solvers: where do approaches differ or contradict? (out/divergence.md).
   Record which ideas came from the blind run, which from literature, and which are new here.
Blind and literature results are compared, never merged.
