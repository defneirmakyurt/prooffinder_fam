# Where the search stalls (H-C5-003)

## Main stall: every search stops at an induced forest of 276 vertices (|S| = 236), never 277
A labelling with <= 2399 uphill paths needs a decycling set S of Q_9 with |S| <= 235 (subject proof.md
Step 8, used here only as a search guide). Every run of the new multiway-cut-repair annealer
(code/mcut_sa.c, 7 runs at d = 9 in runlog.md) reaches |S| = 236 within seconds and never goes below. This
includes a 4e8-move run with mixed moves and a constant-temperature walk on the 276-level set. A penalty
annealer restricted to forests invariant under a coordinate permutation (code/sym_pen_sa.c) gives 237 and
236. The attaining forests
are of several kinds (S = 235 odd + 1 even with e(S) = 7; S = 234 + 2 with e(S) = 13), all with
|M| - |Z| = 20 in the language below. Plain lazy SAT (code/sat_forest.py) is far too weak: it already
fails to find the 72-vertex forest of Q_7 in 120 s.

## Structural reason found here (cluster reduction, argued in claims.md C4)
Write M = F n E, Z = S n O; |S| = 256 - (|M| - |Z|). Group M into clusters (components of the
"distance 2" graph). Different clusters are at distance >= 4, a witness (odd vertex with >= 2 M-neighbours)
belongs to exactly one cluster, and G[F] is a forest iff inside every cluster the kept witnesses form a
Berge-acyclic hypergraph. So |M| - |Z| <= sum over clusters of net(K) = |K| - delta(K), and picking one word
per cluster gives a distance-4 code, so there are at most A(9,4) = 20 clusters (A(9,4) = 20 is the classical
value, cited, not re-proved). Hence |S| <= 235 NEEDS a cluster with net(K) >= 2.
* Exhaustive (up to translation + coordinate permutation) over all clusters with <= 6 words
  (code/clusters.py): every one has net <= 1. So a net-2 cluster has >= 7 words.
* Inside one Q_5 subcube (exhaustive, code/clusters_q5.py): the only net-2 clusters of <= 8 words are the
  even halves of Q_4 subcubes. Net-2 clusters of 9 and 10 words also exist there (not analysed). Clusters
  spanning more than 5 coordinates with 7 or more words were NOT enumerated.
* Known net-2 cluster: the 8 even words of a Q_4 subcube (delete 6 of its 8 odd words, keep an antipodal
  pair). But every word of another cluster must then have its outer 5 coordinates at distance >= 3 from the
  subcube's. One word per other cluster is a distance-4 code in that region, and the largest such code has
  16 words (SAT verdict, no certificate). So if the other clusters are singletons this gives
  |M| - |Z| <= 2 + 16 = 18, worse than 20. Other clusters of net >= 2 in the region were not ruled out.
* Even with |S| = 235 the labelling budget is extra <= 7 (P = 512 + 8|S| + extra). Apply the reduction to
  F = T_f = {N = 1}. A deleted witness z with >= 3 forest neighbours has N(z) >= 3 (forest neighbours of an
  S-vertex are below it), so an S-edge {z, s} costs N(z) - 2 >= 1 if z is its lower end, and N(s) - 2 >=
  deg_F(s) - 2 if s is the lower end, which is 0 only when s has >= 7 neighbours in Z. Net-2 clusters need
  such deletions: if every deleted witness of K has exactly 2 K-neighbours, each distance-2 pair of K needs
  its own deleted witness (else its two common neighbours close a 4-cycle), so |Z_K| >= |K| - 1 and
  net(K) <= 1. So a hand-in needs a net-2 cluster whose high-degree deletions have almost no costly
  S-edges. That is a much stronger requirement than nabla(Q_9) <= 235.

## What a next worker could try
* Enumerate clusters of 7 and more words spanning 6 or more coordinates (needs a faster canonical form
  than clusters.py, e.g. in C). List every net-2 type and its blocked region, then SAT the packing
  "net-2 cluster + 19-word code in the rest". Start with the 9- and 10-word net-2 sets in Q_5.
* Or turn the cluster reduction into a LOWER-bound argument (net(K) weighted by the odd neighbourhood
  |N(K)|, with sum |N(K)| <= 256). The evidence here points to nabla(Q_9) = 236. Together with the
  2400 construction that would give U(Q_9) = 2400, but nothing here proves it.
