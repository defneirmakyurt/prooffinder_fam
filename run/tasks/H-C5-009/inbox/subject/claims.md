# Claims: H-C5-005

Nothing here improves the cell's bounds. The UPPER route (<= 2399) was NOT reached.

| claim | status | where shown |
|---|---|---|
| out/Q9.txt (= out/best.txt) is a labelling of Q_9 with 2400 uphill paths | CHECKED (inbox/checker/verify.py -> "VERIFIED 2400") | runlog run 16; built by code/build_labelling.py from out/forest_Q9.txt (run 7, msa seed 1) |
| out/Q9_alt.txt is a second, different labelling of Q_9 with 2400 uphill paths (different 20-word even code) | CHECKED (verify.py -> "VERIFIED 2400"; cmp: differs from out/Q9.txt and inbox/subject/Q9.txt) | runlog run 16 (msa seed 4) |
| out/forest_Q9.txt, out/forest_Q9_alt.txt induce forests of Q_9 with |S| = 236, e(S) = 0, 96 components | CHECKED (code/check_forest.py, copied from the lineage) | runlog |
| A non-parity induced forest of Q_9 with |S| = 236 (234 even + 2 odd removed, e(S) = 13, 83 components) gives, via build_labelling.py, a labelling with 2406 uphill paths | CHECKED (verify.py -> "VERIFIED 2406" on out/tmp/Q9_ob_triv.txt) | runlog runs 12, 16 |
| No decycling set of Q_9 of size <= 235 was found by: forest SA over orbits of 10 groups (incl. unrestricted), SA over even parts M with greedy Z, SAT-CEGAR in the C9-invariant class (timed out), SAT-LNS with 6/7/8-dim subcube regions | SEARCH-FOUND-NOTHING (none of these searches is exhaustive; no lower bound follows) | runlog runs 4-5, 7-15, 17 |
| SAT-LNS: for 40 random 6-dim and 30 random 7-dim subcube regions R, the solver reported that the 236-solution tmp/ob_triv.txt cannot be improved by changing only vertices in R | solver output only (no DRAT proof produced; NOT a verified claim; the set of regions tried is random, not exhaustive) | runlog runs 13-14 |
| U(Q_9) <= 2399 | NOT ESTABLISHED | - |

## Structural lemma (search guide; proved here modulo the cited value A(9,4) = 20 and the exact computation)
Notation: F an induced forest of Q_9, S = V \ F. For a parity class P in {E, O} put M = F n P, Z = (other class) \ F,
so |S| = 256 - (|M| - |Z|). D = "distance 2" graph on P; clusters = components of D[M]. For a set K of
same-parity vertices, A_K = vertices of the other parity with >= 2 neighbours in K, tau(K) = min |Z'| (Z' in A_K)
with Q_9[K u (A_K \ Z')] a forest, value(K) = |K| - tau(K).

| claim | status | where shown |
|---|---|---|
| L1: |M| - |Z| <= sum over clusters K of value(K), and the number of clusters is <= A(9,4) = 20 | PROVED below (A(9,4) = 20 is a CITED classical coding-theory value, not proved here) | this file, proof of L1 |
| L2: every D-connected set of 2, 3, 4 or 5 same-parity vertices of Q_9 has value <= 1 (singletons have value 1) | CHECKED: exhaustive over all such sets containing {0, e0+e1} (1, 56, 2590, 111300 sets), exact integer/set code, symmetry reduction argued in code/cluster_value.py docstring | code/cluster_value.py 5 (70 s), tmp/cluster5.log |
| L3: any decycling set of Q_9 with |S| <= 235 has, in F n E and also in F n O, a distance-2 cluster of size >= 6 with value >= 2 | PROVED from L1 + L2 (modulo A(9,4) = 20) | below |

Proof of L1. (i) Different clusters are at distance >= 4: two vertices of the same parity are at even distance;
distance 0 means equal; distance 2 puts them in the same component of D[M]. Picking one vertex from each cluster gives
a binary code of length 9 with minimum distance >= 4, so #clusters <= A(9,4) = 20 (cited). (ii) The sets A_K for
different clusters K, K' are disjoint: an other-parity vertex x with a neighbour in K and a neighbour in K'
would put those two neighbours at distance 2, i.e. in the same cluster. (iii) For each cluster K let Z_K = Z n A_K.
Then K u (A_K \ Z_K) is a subset of F (K is in M, which is in F; A_K \ Z_K consists of other-parity vertices not in Z,
hence in F), so Q_9[K u (A_K \ Z_K)] is an induced subgraph of the forest Q_9[F], hence a forest, so |Z_K| >= tau(K).
By (ii) the Z_K are disjoint subsets of Z, so |Z| >= sum_K tau(K), and |M| = sum_K |K|. Hence
|M| - |Z| <= sum_K (|K| - tau(K)). (For |K| = 1, A_K is empty, tau = 0, value 1.)
Proof of L3. If every cluster of M = F n E had size <= 5, then by L2 every cluster has value <= 1, so by L1
|M| - |Z| <= #clusters <= 20 and |S| = 256 - (|M| - |Z|) >= 236. The same argument with the parity classes swapped
(M = F n O, Z = E \ F) applies to the same F; the computation L2 was done for even clusters, and the translation
x -> x XOR e0 is an automorphism of Q_9 mapping odd vertices to even vertices and preserving distances, so it maps odd
clusters to even clusters with the same A_K structure and the same value.
Consequence for the UPPER route (via the unrefereed identity, as a guide only): a labelling with <= 2399 uphill
paths needs such size->=6, value->=2 clusters on both parity sides. This does NOT give any lower bound on U(Q_9).
