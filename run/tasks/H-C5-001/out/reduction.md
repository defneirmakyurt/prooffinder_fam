# Reduction lemma (rung R2), proved from the definitions in statement.md

Fix d >= 1 and a labelling f of Q_d (a bijection V -> {1..2^d}); write u < v for f(u) < f(v).
|E| = d 2^(d-1). For a vertex v let N(v) be the number of uphill paths ending at v.

**Step 0 (recurrence).** The only path with k = 1 ending at v is (v); it is uphill iff v is a valley.
A path (v_1,...,v_k = v) with k >= 2 is uphill iff (v_1,...,v_{k-1}) is an uphill path ending at
w = v_{k-1}, w ~ v and w < v (the conditions "v_1 valley", adjacency and increase split exactly this
way). Hence N(v) = [v valley] + sum_{w ~ v, w < v} N(w), and the number of uphill paths is
total = sum_v N(v). (This is the recurrence the provided checker implements.)

**Step 1 (N >= 1).** By induction along increasing labels: a valley has N >= 1; a non-valley v has a
neighbour w < v, and N(v) >= N(w) >= 1.

**Step 2 (who has N = 1).** Let F = {v : N(v) = 1}, S = V \ F. Claim: v is in F iff v is a valley, or
v has exactly one lower neighbour and that neighbour is in F. Proof: a valley has no lower neighbour,
so N(v) = 1. A non-valley has N(v) = sum over its lower neighbours of N(w), a sum of at least one term,
each term >= 1 (Step 1); it equals 1 iff there is exactly one term and that term is 1.
In particular every valley is in F, so no vertex of S is a valley.

**Step 3 (F induces a forest).** Suppose Q_d[F] contains a cycle C; let v be the vertex of C with the
largest label. Its two neighbours on C are distinct, lie in F and have smaller labels, so v has at least
two lower neighbours; by Step 2 a vertex of F has at most one. Contradiction.

**Step 4 (one valley per tree).** Let T be a component of Q_d[F], with m vertices and m - 1 edges
(Step 3). Each edge of T has exactly one endpoint with the larger label (labels are distinct). For
u in T, the edges of T having u as larger endpoint join u to lower neighbours of u inside T. By
Step 2, a valley has 0 lower neighbours, and a non-valley u in F has exactly one lower neighbour,
which lies in F and is adjacent to u, hence lies in T. So m - 1 = m - (number of valleys in T):
T has exactly one valley. Since all valleys lie in F, #valleys = c(F), the number of trees.

**Step 5 (F-neighbours of S-vertices are lower).** Let v in S and x in F with x ~ v. If x < v we are
done. If v < x, then v is a lower neighbour of x, so x is not a valley, and by Step 2 its unique lower
neighbour (namely v) is in F, contradicting v in S. So every F-neighbour of v is lower than v.

**Step 6 (formula).** For v in S (not a valley, Step 2) Step 0 and Step 5 give
N(v) = d_F(v) + sum_{w in S, w ~ v, w < v} N(w), where d_F(v) = #neighbours of v in F. Summing,
sum_{v in S} N(v) = e(F,S) + sum_{S-edges {w,v}, w<v} N(w). With |E| = e(F) + e(F,S) + e(S) and
e(F) = |F| - c(F) (Step 3):

    total = |F| + e(F,S) + sum N(w) = |E| + c(F) + sum_{S-edges {w<v}} (N(w) - 1).        (A)

Also e(F,S) = d|S| - 2e(S), so c(F) = |F| - e(F) = 2^d - |E| + (d-1)|S| - e(S), and (A) becomes

    total = 2^d + (d-1)|S| + sum_{S-edges {w<v}} (N(w) - 2).                               (B)

Every w in S has N(w) >= 2 (N(w) >= 1 by Step 1 and N(w) != 1), so every summand in (B) is >= 0:

    **total >= 2^d + (d-1)|S|, where S = V \ F is a feedback vertex set of Q_d (Step 3).**   (C)

For d = 9: total >= 512 + 8|S|. Hence a labelling of Q_9 with at most 2399 uphill paths exists ONLY IF
Q_9 has a feedback vertex set of size <= 235 (8|S| <= 1887). (This is a necessary condition, not a
lower bound on U(Q_9): the minimum feedback vertex set size of Q_9 is not determined here.)

**Part (b) (construction).** Let S be an independent set of Q_d such that F = V \ S induces a forest
with c trees. Give labels 1..|F| to F, tree after tree, each tree in BFS order from a root, and labels
|F|+1..2^d to S in any order. For x in F: since F is an induced forest, the F-neighbours of x are
exactly its neighbours in its tree, i.e. its BFS parent (discovered earlier, smaller label; absent for
the root) and its BFS children (enqueued after x, larger labels); its S-neighbours have labels > |F|.
So a root has no lower neighbour (valley, N = 1), and a non-root has exactly one lower neighbour, its
parent, so N(x) = N(parent) = 1 by induction along BFS order. For v in S: S is independent, so all d
neighbours of v are in F and have smaller labels; v is not a valley and N(v) = d. Therefore

    total = |F| + d|S| = 2^d + (d-1)|S|  (= |E| + c, as (A) predicts).

For d = 9 this is 512 + 8|S|; |S| = 236 gives 2400, |S| <= 235 would give <= 2392.
Implemented in code/build_labelling.py (which also checks independence and acyclicity).
