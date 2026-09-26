# Claims: H-C5-009 (EXPLOIT of H-C5-005, merged with sibling H-C5-003; UPPER route only)

Headline: the UPPER target (a labelling of Q_9 with <= 2399 uphill paths) was NOT reached.
"U(Q_9) <= 2399" is SEARCH-FOUND-NOTHING. Nothing below is a lower bound on U(Q_9) or on the decycling number.

Notation. V = {0,1}^9, words as 9-bit integers (bit i = coordinate i). E / O = even / odd weight words (256 each).
For an induced forest F, S = V \ F, c(F) = number of components of Q_9[F], e(S) = number of edges inside S.
D = "distance exactly 2" graph on E. For M subset of E, a cluster of M is a connected component of D[M].
For K subset of E: N(K) = odd words with >= 1 neighbour in K; A_K = odd words with >= 2 neighbours in K;
tau(K) = min |Z'| over Z' subset of A_K with Q_9[K u (A_K \ Z')] a forest; net(K) = |K| - tau(K).

| # | claim | status | where shown |
|---|---|---|---|
| V1 | For every induced forest F of Q_9: 8|S| = 1792 + c(F) + e(S). Hence |S| <= 235 iff c(F) + e(S) <= 88 | PROVED | below |
| V2 | (value function, re-derived, EXACT) nabla(Q_9) = 256 - max over M subset of E of sum over clusters K of M of net(K) | PROVED | below |
| V3 | (cost form) for a cluster K with an optimal Z_K: 8 net(K) = |N(K)| - c_K - loss_K, where c_K = #components of Q_9[K u (N(K) \ Z_K)] and loss_K = number of edges from Z_K to E \ K; the N(K) of different clusters are disjoint | PROVED | below |
| V4 | Lemma A (gated) + V1: a labelling with <= 2399 uphill paths needs an induced forest with c + e(S) <= 88, i.e. (V2) some M with sum of net >= 21 | PROVED from the gated Lemma A | below |
| R3 | The canonical key in code/clusters.c is a complete invariant for the action of G = {x -> pi(x) xor t : pi in S_9, t in E} on even-word sets | PROVED (argument below); CHECKED against an independent canonical form for sizes 2..5 | below; runlog runs X1, X2 |
| R4 | EXHAUSTIVE over all D-connected sets K of even words of Q_9 with |K| <= KMAX (up to G): the maximum of net(K) is 1 for |K| = 1..7, and 2 for |K| = 8, attained by exactly one class: the 8 even words of a Q_4 subcube (|N(K)| = 48, tau = 6) | CHECKED (exact, exhaustive over this finite class only) | code/clusters.c, runlog run C8/C9 |
| R5 | With K = even half of a Q_4 subcube, the largest set of even words pairwise at distance >= 4 and at distance >= 4 from K has exactly 16 words (so K + singleton clusters give sum of net <= 18 < 21) | see runlog run P1 | code/maxcode.c |
| R7 | Doubled class (half x_8 = 0 forced to the perfect Q_8 forest (odd words) u RM(1,3)): SA result | heuristic; see runlog | code/fsa.c |
| T | U(Q_9) <= 2399 | SEARCH-FOUND-NOTHING | - |

## V1 (proof)
F induces a forest, so e(F) = |F| - c(F). Every edge of Q_9 lies inside F, inside S, or between them:
2304 = e(F) + e(S) + e(F,S). Summing degrees over S: 9|S| = 2 e(S) + e(F,S). Hence
e(F) = 2304 - e(S) - (9|S| - 2 e(S)) = 2304 - 9|S| + e(S). With |F| = 512 - |S|:
512 - |S| - c(F) = 2304 - 9|S| + e(S), i.e. 8|S| = 1792 + c(F) + e(S). (The parity construction of both
lineages: c = 96, e(S) = 0, |S| = 236.)

## V2 (proof: the value function, exact)
Let Phi(M) = max { |M| - |Z| : Z subset of O, Q_9[M u (O \ Z)] is a forest } for M subset of E.
(a) nabla(Q_9) = 256 - max_M Phi(M). If F is an induced forest, put M = F n E and Z = O \ F. Then
F = M u (O \ Z) and |S| = |E \ M| + |Z| = 256 - (|M| - |Z|) >= 256 - Phi(M). Conversely, for any M and any Z
feasible in the definition of Phi(M), F = M u (O \ Z) is an induced forest with |V \ F| = 256 - (|M| - |Z|).
(b) Phi(M) = sum over clusters K of M of net(K).
 (i) Two words of M in different clusters are at distance >= 4: both are even, so their distance is even; it is
     not 0 (distinct) and not 2 (else they are adjacent in D[M], hence in the same cluster).
 (ii) If an odd word o has two neighbours m, m' in M then d(m, m') <= 2, and d(m, m') = 2 (distinct, same
     parity), so m, m' are in the same cluster. Hence all M-neighbours of o lie in one cluster. In particular the
     sets A_K (K a cluster) are pairwise disjoint, and the sets N(K) are pairwise disjoint.
 (iii) Q_9[M u (O \ Z)] is bipartite with parts M and O \ Z (no edges inside E or inside O). Let C be a cycle in
     it. Every odd vertex o of C has two distinct neighbours on C, both in M; by (ii) they are in one cluster K_o,
     and o is in A_{K_o}. Walking along C, consecutive M-vertices of C have a common neighbour (the odd vertex
     between them), so they are at distance 2 and lie in the same cluster; C is connected, so all M-vertices of C
     lie in one cluster K, all odd vertices of C lie in A_K \ Z, and C is a cycle of Q_9[K u (A_K \ Z)].
     Conversely each Q_9[K u (A_K \ Z)] is an induced subgraph of Q_9[M u (O \ Z)].
     So Z is feasible iff for every cluster K, Q_9[K u (A_K \ (Z n A_K))] is a forest.
 (iv) By (ii) and (iii) the constraint splits over the pairwise disjoint sets A_K, and vertices of Z outside
     the union of the A_K play no role. So the minimum of |Z| over feasible Z is sum_K tau(K) (take an optimal
     Z_K in each A_K, and nothing else), and Phi(M) = |M| - sum_K tau(K) = sum_K (|K| - tau(K)).
 Hence nabla(Q_9) <= 235 iff some M subset of E has sum over its clusters of net(K) >= 21.
 (For |K| = 1, A_K is empty and net = 1. The lineages proved only "<="; the equality in (iv) is new here and
 is what makes the enumeration below a statement about exactly the right quantity.)

## V3 (proof: cost form)
Let K be a cluster, Z_K an optimal deletion set (|Z_K| = tau(K)), H_K = Q_9[K u (N(K) \ Z_K)]. Odd words of
N(K) \ A_K have one neighbour in K, so H_K is H'_K = Q_9[K u (A_K \ Z_K)] plus pendant leaves: a forest.
Its edges are all K-odd edges not touching Z_K: 9|K| - e(K, Z_K). Forest: 9|K| - e(K, Z_K) = |K| + |N(K)| - |Z_K| - c_K.
With loss_K = 9|Z_K| - e(K, Z_K) (edges from Z_K to even words outside K): 8(|K| - |Z_K|) = |N(K)| - c_K - loss_K.
Summing over the clusters of M (the N(K) are disjoint by V2 (ii)): 8 Phi(M) = 256 - |U| - sum_K (c_K + loss_K),
U = odd words with no neighbour in M. A singleton has cost c + loss = 1 and covers 9 odd words; the 20-word
code leaves |U| = 76 and pays 20 (total 96 = 8 x 12, Phi = 20). The target needs |U| + total cost <= 88.
The Q_4-half cluster (R4) covers 48 odd words and pays 32 for net 2: this is why it cannot help.

## V4 (link to the target)
Lemma A (gated, inbox/gated-lemmaA.md): every labelling has >= 512 + 8|S_f| uphill paths, S_f = {down >= 2},
and V \ S_f is an induced forest. 512 + 8 x 236 = 2400. So <= 2399 needs |S_f| <= 235, i.e. (V1) c + e(S) <= 88,
i.e. (V2) an M with sum of net >= 21.

## R3 (soundness of the symmetry reduction; canonical key of clusters.c)
Group. G = { g_{pi,t} : x -> pi(x) xor t }, pi a permutation of the 9 coordinates, t an even word. Each g is an
automorphism of Q_9 (coordinate permutations and translations preserve Hamming distance) and preserves weight
parity (t even). So g maps E to E, O to O, D-connected sets to D-connected sets, N(K), A_K to N(gK), A_{gK},
and Q_9[K u (A_K \ Z')] isomorphically onto Q_9[gK u (A_{gK} \ gZ')]; hence tau(gK) = tau(K), net(gK) = net(K).
Key. For K (|K| = k, 0 not assumed) and t in K, let R_t = (K xor t) \ {0}: k-1 nonzero words (rows). For an
ordering (r_1..r_{k-1}) of R_t, let col_i = (bit i of r_1, ..., bit i of r_{k-1}) for i = 0..8, sort the 9 columns
in decreasing lexicographic order, and read the resulting (k-1) x 9 matrix row by row (row j = 9-bit word).
key(K) = the lexicographically largest such row sequence over all t in K and all orderings.
(1) Equivalent sets have equal keys. If K' = pi(K xor t0), then for t' in K' with s = t0 xor pi^{-1}(t') in K:
    K' xor t' = pi(K xor s). So {R'_{t'}} = {pi(R_s)}; applying pi permutes columns, which the column sort
    removes; the maximum over orderings removes the row order. So the candidate sets coincide and so do the maxima.
(2) Equal keys give equivalent sets. The key's rows are exactly the words of sigma(R_t) for a column permutation
    sigma (the sort), so {0} u rows(key) = sigma(K xor t) is in the orbit of K. Two sets with the same key are both
    equivalent to the same set.
(3) The branch and bound computes this maximum exactly. After j rows have been chosen, the first j rows of the
    final matrix are determined: sorting columns decreasingly by their full bit strings orders them first by their
    j-bit prefixes, and columns with equal prefixes agree in rows 1..j, so rows 1..j of the result depend only on
    the multiset of prefixes. Hence (i) at depth j only rows attaining the largest possible row-j word can lead to
    the maximum (earlier rows being equal), and (ii) a partial ordering whose rows 1..j are lexicographically smaller
    than the best complete key found so far cannot be completed to a larger key. The code keeps every tie (all
    rows attaining the maximum) and prunes only by (ii), so it returns the exact maximum. (The code keeps column
    prefixes indexed by the original coordinate and sorts a copy only to read off the row word.)
Growth completeness. Every D-connected set K' with |K'| = k+1 >= 2 has a vertex w whose removal leaves a
D-connected set K (a leaf of a spanning tree of D[K']). K is equivalent to a stored representative K0 = g(K).
Then g(K') = K0 u {g(w)} and g(w) is a D-neighbour of g(v) in K0 for the tree-neighbour v of w. The program forms
K0 u {w'} for EVERY vertex of K0 and EVERY D-neighbour w' outside K0, so it forms g(K'), and the key dedup keeps
one set of its class. By induction from the single class of size 1 ({0}), every class of every size <= KMAX is
generated and evaluated.
tau computation (exact). Iterative deepening on the budget b = 0, 1, ..., k-1. For a budget, find a cycle of
Q_9[K u kept witnesses] (first a 4-cycle: two words of K at distance 2 whose two common neighbours are both kept;
otherwise any cycle by depth-first search; in an undirected DFS every non-tree edge joins a vertex to an ancestor,
so walking up the parent pointers gives a cycle). Any feasible deletion set must contain a witness of that cycle
(K cannot be deleted), so branching over the witnesses of the cycle is complete. Pruning: a forest on
K u W' has at most |K| + |W'| - 1 edges, i.e. sum over W' of (t_w - 1) <= |K| - 1 (t_w = #K-neighbours of w);
one deletion lowers the left side by at most max(t_w) - 1, so a branch whose excess exceeds budget x (max t_w - 1)
is infeasible. If no budget <= k-1 works, net(K) <= 0 (reported as "net<=0").
