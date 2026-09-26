TASK: B-C3-001      ROLE: space      REGIME: LITERATURE
PHASE: 2S   MODE: -   BRANCH: -
SUBJECT: -
TIME BOX: 30 minutes
READ ONLY: run/tasks/B-C3-001/ (this brief + inbox/). Do not open anything else under run/.
WRITE ONLY: run/tasks/B-C3-001/out/
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
ASSUMPTIONS: none beyond the statement
STOPPING CONDITION: Stop when 4-8 space cards with checked translations, graph.md, spec.md and proposals.md are written.
LESSONS: role-lessons.md v0, problem-lessons.md v0
RULES: any computation must be exact or interval arithmetic, code included, runtime < 10 min; state exactly what is established
RETURN: only the report block from your agent instructions, at most 200 words plus CARDS / RAN lines.
        Full work goes in out/.
INBOX: role-lessons.md v0, problem-lessons.md v0, statement.md, target.md, checklist-G.md
PYTHON: /Users/radu.cucu/Developer/bainsahackathon/.venv/bin/python3 (sympy, mpmath, networkx, python-flint, python-sat); plain python3 lacks them.
        Checkers and anything a judge reruns stay stdlib-only unless the brief says otherwise.

Phase 2S. Do not solve the cell and do not choose: the head evaluates your cards and decides what runs.
You have web search and fetch: use them to discover spaces and tools, what is known in each space about this
problem and its neighbours, and what no source has used. Open every source you cite; tag it PROVED /
COMPUTER-VERIFIED / CONJECTURED and say whether it contains the argument or only cites it. Never present a
citation as a proof of the cell. Never call anything new: write "not found in <sources searched>".
Inbox/obstacles/ (if present) holds stuck.md and verdict.md files, never proofs; inbox/checker/ (if present) is an
exact checker you may use on small cases; any other inbox file is extra material the head chose to give you.
1. Pin the target: restate it, classify the goal, compute small and boundary cases by code, list extremizers
   (out/target_pin.md, out/small_cases.md).
2. Sweep the catalogue in your agent instructions and search beyond it; log every search and source in
   out/sources.md; keep 4-8 spaces where the problem can be written precisely (discards in out/discarded.md).
3. One card per kept space in out/spaces.md, in the exact field format of section 17: fidelity with its direction,
   a translation check run on the small cases, tightness on every known extremizer, the tools and what each would
   deliver here, what is KNOWN in this space, what is UNEXPLORED, cost, payoff, an ANGLE and a FIRST TASK.
4. out/graph.md: directed edges between spaces and neighbours, with sources; unanswered NEIGHBOUR QUESTION lines.
5. out/spec.md: properties any valid proof must have. 6. out/proposals.md: 3-6 ranked proposals.
Code in out/checks/. Fill in RAN exactly: what ran, parameter range, COMPLETED / TIMED OUT / PARTIAL, measured runtime.
