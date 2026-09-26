# Proof that every labelling of Q_6 has at least 204 uphill paths (computer-assisted)

Fix a labelling f of Q_6 (n = 64, |E| = 192, every vertex has degree 6). For a vertex v let
down(v) / up(v) be the numbers of neighbours with smaller / larger label (down + up = 6),
N(v) the number of uphill paths ending at v, V the number of valleys, T the total.

**L1 (recursion).** N(v) = [v valley] + sum_{w ~ v, f(w) < f(v)} N(w). Proof: the only
path with k = 1 ending at v is (v), uphill iff v is a valley. A sequence with k >= 2 ending
at v is uphill iff its last step comes from a neighbour w with f(w) < f(v) and the prefix
is an uphill path ending at w; distinct (w, prefix) give distinct sequences.

**L2.** N(v) >= 1 for all v, and N(v) >= down(v). Proof by induction on f(v): a valley
has N = 1. Otherwise down(v) >= 1 and every lower neighbour w has N(w) >= 1 by induction,
so N(v) >= down(v) >= 1.

**L3 (identity).** T = V + |E| + X, X = sum_v up(v)(N(v) - 1). Proof: sum L1 over v:
T = V + sum_v sum_{w~v, f(w)<f(v)} N(w) = V + sum_w up(w) N(w), and sum_w up(w) = |E|
(each edge counted once, at its lower endpoint).

**L4.** Each term t(v) = up(v)(N(v)-1) is 0 or >= 4. Proof: if t(v) > 0 then up(v) >= 1
and N(v) >= 2, so v is not a valley and k = down(v) is in {1,...,5}. k = 1: up = 5, t >= 5.
k >= 2: N(v) >= k by L2, t >= (6-k)(k-1), which is 4, 6, 6, 4 for k = 2, 3, 4, 5.

**Partition.** A = {v : N(v) = 1}, P = {v : up(v) = 0} (peaks), S = the rest
= {v : up(v) >= 1, N(v) >= 2}. These are disjoint and cover V(Q_6): a peak has down = 6,
so N >= 6 by L2 and it is not in A; S is defined as the complement. X = sum_{v in S} t(v)
(terms outside S are 0), so by L4, X >= 4|S|, and X = 0 iff S is empty.

**L5.** P is independent: of two adjacent vertices, the one with the smaller label has a
larger neighbour, so it is not a peak.

**L6.** Q_6[A] is a forest and its number of components c(A) equals V. Proof: if v in A is
not a valley, N(v) = 1 >= down(v) (L2) gives down(v) = 1, and its unique lower neighbour w
has N(w) = N(v) = 1 (L1 with v not a valley and a single lower neighbour), so w in A. Hence every vertex of A has at most one lower
neighbour in the whole graph. A cycle in Q_6[A] would have a vertex of maximum label on
it, with two lower neighbours on the cycle: impossible, so Q_6[A] is a forest. In a tree
component with m vertices, each non-valley has exactly one lower neighbour and it lies in
the same tree, and each edge of the tree is counted once this way (at its upper
endpoint, which is a non-valley); so m - 1 = m - (#valleys in the tree), i.e. each tree
has exactly one valley. Every valley has N = 1 so lies in A. Therefore c(A) = V.

**Reduction.** Suppose T <= 203. Then V + X <= 11 (L3). Since X >= 4|S|:
* |S| >= 3 is impossible (X >= 12);
* |S| = 0: V <= 11;  |S| = 1: V <= 11 - 4 = 7;  |S| = 2: V <= 11 - 8 = 3.
So there is a set S of at most 2 vertices and a set P of vertices of Q_6 - S with
(a) P independent (L5), (b) A = V(Q_6) - S - P induces a forest (L6), and
(c) c(A) = V <= 11, 7, 3 for |S| = 0, 1, 2 respectively.

**Computation (exhaustive, no symmetry reduction, no size restriction on P).**
`out/code/exhaust_general.c` enumerates, for every S with |S| = 0 (1 set), |S| = 1 (all 64
sets), |S| = 2 (all 2016 sets), every P with (a), (b), and counts those with c(A) <= cmax.
Its only prunings are (i) an edge inside P, (ii) a cycle already closed inside the decided
part of A, both of which persist in every completion because P and A only grow, and
(iii) a size window on |P|, which in the headline runs is [0, 64], i.e. inactive.
Results (see runlog.md):
* `exhaust_general 6 0 11 0 64` -> solutions=0 (nodes 39783)
* `exhaust_general 6 1 7 0 64`  -> solutions=0 (nodes 2889353)
* `exhaust_general 6 2 3 0 64`  -> solutions=0 (nodes 103326594)
Hence no labelling has T <= 203, i.e. **every labelling of Q_6 has T >= 204.**

Controls (the same program finds sets when they exist): `6 0 12 0 64` -> 240 solutions;
`6 1 12 0 64` -> 14400; `6 2 12 0 64` -> 597600; `3 0 2 0 8` -> 8 (Q_3 value 14 = 2 + 12
attained by out/tmp labelling, checker VERIFIED 14); `4 0 2 0 16` -> 8 (checker VERIFIED 34).

Assumption list: the soundness of the three pruning rules above (argued in the header of
exhaust_general.c) and the correctness of the C compiler/runtime. Nothing from the
literature is used.

**Upper bound.** out/Q6.txt is a labelling with 204 uphill paths (provided checker:
`VERIFIED 204`). Structure (out/tmp/analyze.py): V = 12, X = 0, 28 peaks, so it attains
L3 with equality at the extremal case S = empty, c(A) = 12.

**Conclusion.** U(Q_6) = 204.
