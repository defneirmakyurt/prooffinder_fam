# Claims: H-C1-004

## Summary table

| claim | status | where shown |
|---|---|---|
| Counting recursion N(v) = [v valley] + sum_{w~v, f(w)<f(v)} N(w), total = sum_v N(v) | PROVED | section R2 below |
| N(x) >= 1 for every vertex x, under every labelling | PROVED | section R2b below |
| My counter (out/code/uphill.py) agrees with inbox/checker/verify.py | CHECKED | `crosscheck.py counter 3 300` and `... 4 300`, 0 mismatches |
| U(Q_3) <= 14: out/Q3.txt has exactly 14 uphill paths | CHECKED | `verify.py out/Q3.txt --d 3` -> `VERIFIED 14` |
| U(Q_3) >= 14: every one of the 8! = 40320 labellings of Q_3 has >= 14 uphill paths | CHECKED | `brute_q3.py` (full enumeration, min = 14) and `bnb.py 3 14 --nomemo --nolb` -> `NONE BELOW 14` |
| **U(Q_3) = 14** | CHECKED | the two rows above |
| U(Q_4) <= 34: out/Q4.txt has exactly 34 uphill paths | CHECKED | `verify.py out/Q4.txt --d 4` -> `VERIFIED 34` |
| LB(S) is a valid lower bound on the cost of every completion of a partial labelling | PROVED | section R5 below |
| U(Q_4) >= 34: every one of the 16! = 20922789888000 labellings of Q_4 has >= 34 uphill paths | CHECKED | `bnb.py 4 34 --nomemo` -> `NONE BELOW 34`, 0.85 s; exhaustive over all bijections, soundness from R5 |
| **U(Q_4) = 34** | CHECKED | the two rows above |
| The state memo is sound | PROVED | section R6 below (not load-bearing: R8b runs without it) |
| No symmetry reduction is used anywhere | CHECKED | `bnb.py` iterates over every unplaced vertex at every depth; see section R8 |

Nothing here is claimed for any d other than 3 and 4.  A finite search over d = 3, 4 says nothing
about U(Q_d) for d >= 5.

---

## R2. The counting recursion

Fix a labelling f of Q_d.  For a vertex v let N(v) be the number of uphill paths (v_1,...,v_k),
k >= 1, whose last vertex v_k is v.  Every uphill path has exactly one last vertex, so the number of
uphill paths of f is sum over all v of N(v).

Split the uphill paths ending at v by length.

*k = 1.*  The only length-1 sequence ending at v is (v).  By the definition, (v) is an uphill path
iff v_1 = v is a valley.  So this contributes [v is a valley] (1 or 0).

*k >= 2.*  Let A(v) = {uphill paths ending at v of length >= 2} and let
B(v) = disjoint union over {w : w ~ v and f(w) < f(v)} of {uphill paths ending at w}.
Define phi : A(v) -> B(v) by phi(v_1,...,v_{k-1},v) = (v_1,...,v_{k-1}), recorded in the copy of the
disjoint union indexed by w = v_{k-1}.

phi is well defined.  If (v_1,...,v_{k-1},v) is uphill then: v_1 is a valley; v_i ~ v_{i+1} for
i <= k-2; and f(v_1) < ... < f(v_{k-1}), these being a sub-chain of the strict chain of the whole
path.  So (v_1,...,v_{k-1}) is an uphill path ending at w = v_{k-1}.  Moreover w ~ v (consecutive
vertices of the path) and f(w) < f(v) (the last strict inequality of the chain), so the index w is
one of the allowed ones.

phi is injective: the image plus the index w determines the whole original sequence (append v).

phi is surjective: let w ~ v with f(w) < f(v) and let (v_1,...,v_{k-1}) be an uphill path ending at
w = v_{k-1}.  Then (v_1,...,v_{k-1},v) has v_1 a valley, consecutive vertices adjacent (the old ones,
plus v_{k-1} = w ~ v), and strictly increasing labels (the old chain, extended by
f(v_{k-1}) = f(w) < f(v)).  So it is an uphill path ending at v, of length >= 2, and phi sends it to
the given element.

Hence |A(v)| = |B(v)| = sum over w ~ v with f(w) < f(v) of N(w), and

    N(v) = [v is a valley] + sum_{w ~ v, f(w) < f(v)} N(w),          total = sum_v N(v).

Because the right-hand side only refers to vertices with strictly smaller label, processing vertices
in increasing label order computes every N(v) with all its summands already known.

(This is the same recursion the provided checker documents.  I re-derived it above and additionally
verified my implementation against the provided checker on 600 random labellings.)

## R2b. N(x) >= 1 always

By induction on f(x).  If x is a valley then N(x) >= [x valley] = 1.  If x is not a valley then by
the definition of valley some neighbour w of x has f(w) < f(x); all terms in the recursion are
non-negative, so N(x) >= N(w), and N(w) >= 1 by the induction hypothesis since f(w) < f(x).
(The base of the induction is subsumed: the vertex with label 1 has every neighbour labelled higher,
so it is a valley.)

## R5. The lower bound LB(S)

*Setting.*  A node of the search tree is a partial labelling: a sequence of distinct vertices
v_1, ..., v_m with f(v_i) = i.  Write S = {v_1,...,v_m} (the placed vertices) and R = V \ S.
A *completion* is any ordering of R, its vertices receiving the labels m+1, ..., n in that order;
completions of this node are in bijection with the orderings of R, and every labelling of Q_d
extending this partial labelling arises exactly once this way.

*Fact 0.*  Every vertex of S has a strictly smaller label than every vertex of R, in every
completion, since S holds labels 1..m and R holds labels m+1..n.

*Fact 1 (the prefix determines the cost so far).*  For i <= m, the neighbours of v_i with label
< i are exactly the neighbours of v_i inside {v_1,...,v_{i-1}}, and v_i is a valley iff none of
v_1,...,v_{i-1} is a neighbour of v_i.  So N(v_1),...,N(v_m) and
cost(S) := sum_{v in S} N(v) depend only on the sequence v_1,...,v_m and not on the completion.
(This is exactly what `bnb.py` maintains incrementally in `N[]` and `cost`.)

*Fact 2 (expansion of the remaining cost).*  Fix a completion and let future = sum_{v in R} N(v).
Apply R2 to each v in R and split the inner sum by whether the neighbour lies in S or in R.
By Fact 0 every neighbour w of v in S has f(w) < f(v), so that part of the sum is the whole of
P(v) := sum over neighbours w of v with w in S of N(w), a quantity determined by the node alone
(Fact 1).  Therefore

    future = #{valleys in R} + sum_{v in R} P(v)
             + sum_{v in R} sum_{w in R, w ~ v, f(w) < f(v)} N(w).

In the last double sum, an ordered pair (v,w) contributes iff v,w in R, v ~ w and f(w) < f(v).
For each unordered edge {u,v} with both ends in R exactly one of the two ordered pairs qualifies
(labels are distinct, so exactly one end is the lower one), and it contributes N of the lower end.
So the last double sum equals sum over edges {u,v} of Q_d with u,v in R of N(lower end of {u,v}).

*Fact 3 (pointwise bounds).*  For x in R: by R2 and non-negativity of all terms,
N(x) >= sum over neighbours w of x with w in S of N(w) = P(x)  (Fact 0 makes all these terms count).
By R2b, N(x) >= 1.  Hence N(x) >= max(1, P(x)).

*Assembling.*  #{valleys in R} >= 0.  If S is empty then the vertex that gets label 1 lies in R and
is a valley (all its neighbours have larger labels), so #{valleys in R} >= 1 in that case.
For an edge {u,v} with u,v in R, its lower end is u or v, so by Fact 3
N(lower end) >= min( max(1,P(u)), max(1,P(v)) ).  Substituting into Fact 2,

    future  >=  LB(S) := [S is empty]
                          + sum_{v in R} P(v)
                          + sum_{edges {u,v} with u,v in R} min( max(1,P(u)), max(1,P(v)) ).

LB(S) is computed from the node only (it uses P, hence N on S), and the inequality holds for
*every* completion.  Consequently, if cost(S) + LB(S) >= T then every labelling extending this
partial labelling has total cost = cost(S) + future >= T, and the whole subtree can be cut without
losing any labelling with fewer than T uphill paths.  QED

This is `lower_bound(S)` in out/code/bnb.py, line for line.

*The trivial prune.*  When the child that gives label m+1 to v is considered, its N(v) is known
exactly.  All N values are >= 1 > 0 (R2b), so the total of any labelling through this child is at
least cost(S) + N(v).  If cost(S) + N(v) >= T the child is cut.  QED

## R6. The state memo (used only in the faster runs)

Let B(S) = {s in S : s has at least one neighbour outside S} (the boundary of S).

*Claim.*  Given the node's placed set S and the values N(s) for s in B(S), the value of `future`
for any given completion is determined; it does not depend on anything else about the node.

*Proof.*  Run the recursion R2 forward along the completion.  For the j-th vertex u of the
completion, N(u) = [u is a valley] + sum over neighbours w of u with f(w) < f(u) of N(w).
The neighbours w of u with smaller label are: (i) all neighbours of u lying in S (Fact 0), and
(ii) those neighbours of u in R that appear earlier in the completion.  Every w of type (i) has the
neighbour u outside S, hence w is in B(S), so N(w) is available from the key.  Every w of type (ii)
has its N already computed earlier in this same forward pass.  And "u is a valley" holds iff u has
no neighbour in S and no neighbour earlier in the completion, which is decided by S and the
completion order.  So the whole pass, and hence future = sum_{u in R} N(u), is a function of
(S, N restricted to B(S)) and the completion order alone.  QED

Consequently minfuture(k) := min over completions of future is a function of the key
k = (S, N|_{B(S)}) only.  This is `key(S)` in out/code/bnb.py.

*Memo invariant.*  `memo[k] = c` is only ever written so that the statement
  I(k,c):  c + minfuture(k) >= T
holds.  Then a node with key k and cost' >= c can be cut, since
cost' + minfuture(k) >= c + minfuture(k) >= T.

*The invariant is maintained.*  Induct on the order in which entries are written.
 - Written right after the LB cut: we had cost + LB(S) >= T, and minfuture(k) >= LB(S) by R5
   (LB bounds `future` for every completion, hence the minimum).  So I(k, cost) holds.
   When the stored value is min(prev, cost) < cost, the smaller value is `prev`, for which the
   invariant already holds by the induction hypothesis.
 - Written after the child loop returned False: minfuture(k) = min over unplaced v of
   ( N(v) + minfuture(k_v) ), where k_v is the key of the child (the minimum over completions
   splits on which vertex takes label m+1).  Each child was disposed of in one of three ways:
   (a) trivial prune, cost + N(v) >= T, so cost + N(v) + minfuture(k_v) >= T since minfuture >= 0;
   (b) memo cut, memo[k_v] = c_v <= cost + N(v) with I(k_v,c_v) by the induction hypothesis, so
       cost + N(v) + minfuture(k_v) >= c_v + minfuture(k_v) >= T;
   (c) recursive call returned False, which by this same induction means
       (cost + N(v)) + minfuture(k_v) >= T.
   Taking the minimum over v gives cost + minfuture(k) >= T, i.e. I(k, cost).  QED

The memo is *not* relied on for the reported bounds: `bnb.py 4 34 --nomemo` reproduces
`NONE BELOW 34` in 0.85 s using only R5 and the trivial prune, and `bnb.py 3 14 --nomemo --nolb`
reproduces `NONE BELOW 14` using neither.

## R8. What "exhaustive" means here

`dfs` builds label sequences.  At a node with placed set S it loops `for v in range(n)` and recurses
on every v not in S, i.e. every unplaced vertex is tried as the holder of the next label.  There is
no symmetry reduction, no canonical-form filter and no restriction on which vertex may take label 1.
With all pruning removed, the leaves are therefore in bijection with the n! bijections
V(Q_d) -> {1,...,n}; this is confirmed empirically for d = 3, where the unpruned run visits the full
tree (59681 nodes with only the trivial prune) and reports the same answer as the independent
`brute_q3.py`, which literally iterates `itertools.permutations(range(8))`.

Every prune is proved above to cut only subtrees containing no labelling with total < T.  Therefore
`NONE BELOW T` is exactly the statement "every labelling of Q_d has at least T uphill paths",
for the specific d and T of that run:

 - d = 3, T = 14: every one of the 40320 labellings of Q_3 has >= 14 uphill paths.
 - d = 4, T = 34: every one of the 20922789888000 labellings of Q_4 has >= 34 uphill paths.

Together with the attaining labellings out/Q3.txt (VERIFIED 14) and out/Q4.txt (VERIFIED 34):

    U(Q_3) = 14        U(Q_4) = 34

All arithmetic is exact Python integers throughout; no floating point enters any bound
(the only float in the repository is the annealing temperature in sa_q4.py, which merely proposes
candidates and influences no claim).

## Degenerate and edge cases (checklist G3)

 - *Isolated vertices.*  The statement says an isolated vertex counts as a valley.  In Q_d with
   d >= 1 every vertex has exactly d >= 1 neighbours, so Q_d has no isolated vertex and the clause is
   vacuous here.  It is also correctly subsumed: "every neighbour w of v has f(w) > f(v)" is
   vacuously true for a vertex with no neighbours, which is what `all(...)` over an empty
   neighbour list returns in both the provided checker and out/code/uphill.py.
 - *k = 1 paths.*  A valley on its own is an uphill path and is counted: it is the `[v is a valley]`
   term of the recursion.  For d = 3 the labelling in out/Q3.txt has exactly one valley (000, the
   label-1 vertex), and 1 of its 14 uphill paths is the single-vertex path (000).
 - *S empty.*  LB(0) is the only place where the valley term of R is used; the special case is
   handled explicitly in R5 and in the code (`if S == 0: tot += 1`).  Dropping it would only weaken
   the bound, never invalidate it.
 - *T at the extremes.*  `bnb.py d 1` must print `NONE BELOW 1` since every labelling has at least
   the one uphill path consisting of the label-1 vertex alone; the sweep (run 20) confirms this.
 - *Recursion depth.*  `sys.setrecursionlimit(10000)` covers depth 2^d = 16 with room to spare.

## Checklist G, item by item

 - **G1** The statement settled is exactly the cell's: the two integers U(Q_3) and U(Q_4), each with
   an explicit attaining labelling in the required format.  No extra hypothesis; the parameter range
   is exactly d in {3,4} and nothing outside it is claimed.
 - **G2** Every step is written out: R2 (bijection phi, with well-definedness, injectivity and
   surjectivity each argued), R2b (induction), R5 (Facts 0-3 and the assembly), R6 (the memo
   invariant and its maintenance in all three child cases), R8 (why the enumeration is exhaustive).
   No step is replaced by "clearly", "similarly", "routine", "obviously" or "by symmetry" -- in
   particular no symmetry argument is used anywhere, because no symmetry reduction is used.
 - **G3** See the section above.
 - **G4** The one invariant claimed is the memo invariant I(k,c); R6 proves it is established at
   every write and used only where it applies.  The strictness that matters is `f(w) < f(v)` in the
   recursion, which is strict because f is a bijection into {1,...,n} so no two vertices tie.
 - **G5** The two constructions are checked by the provided checker at exactly the two claimed
   parameter values d = 3 and d = 4; there are no untested claimed values.
 - **G6** No circularity: the lower bound comes from an enumeration that never consults the upper
   bound's labelling, and the upper bound is an explicit object checked by the provided checker.
   The only external artefact used is inbox/checker/verify.py, as a scorer, not as an authority for
   any claim; its counting recursion was re-derived from the definitions in R2 and its output was
   cross-checked against an independent implementation on 600 random labellings.
 - **G7** All arithmetic is exact Python integer arithmetic.  All code is in out/code/.  The two
   decisive runs take 0.09 s and 0.92 s.  The finite check covers exactly d = 3 and d = 4 and is
   claimed for nothing else.  The reduction from "every labelling" to "the set actually searched" is
   R8: the search tree's leaves are all (2^d)! bijections, and every cut is proved to remove only
   subtrees with no labelling below T.
 - **G8** No result from any source outside this task is used or cited.  Everything is derived from
   the definitions in inbox/statement.md.
 - **G9** Established: U(Q_3) = 14 and U(Q_4) = 34, both halves, by exhaustive search.
   Not established: anything about U(Q_d) for d >= 5, and any general formula.  See out/stuck.md.
