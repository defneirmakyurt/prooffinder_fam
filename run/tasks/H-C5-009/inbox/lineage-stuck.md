# Where the search stalls (H-C5-005)

Every search in every class stops at a decycling set of size 236, i.e. labellings with 2400 uphill paths
(parity construction, 20-word even code) or 2406 (the non-parity 236 shape: 234 even + 2 odd removed,
e(S) = 13, 83 components). A labelling with <= 2399 needs (per the subject's unrefereed identity, used as a
guide only) a decycling set of size <= 235 with small extra, and none was found.

What was tried and where it stops:
* forest SA over orbits, 10 groups (unrestricted, translations by weight 2/3/4/9 vectors, C9, (012)(345)(678),
  transposition, and two twisted maps): unrestricted -> 236 (three seeds); every nontrivial group -> >= 237.
  Symmetric classes are too restrictive here; |S| = 235 is odd, so no fixed-point-free group can reach it at all.
* SA over the even part M (odd part all in F except a greedy Z): always converges to a 20-word code (Z empty),
  |S| = 236; it never kept a nonempty Z at the best score.
* exact SAT sub-solves (LNS) around a 236 solution: every 6-dim and 7-dim subcube region tried is "locally
  optimal" (solver UNSAT, no DRAT); an 8-dim region (half the cube) is already too hard for one SAT call in
  280 s.
* full SAT-CEGAR without symmetry: fine up to d = 7 (75 s), hopeless at d = 9 in the time box; C9-invariant
  class at d = 9 timed out even for K = 236.

Structural observation (partly proved, see claims.md L1-L3): in the (M, Z) language (M = F cap E, Z = S cap O,
|S| = 256 - (|M| - |Z|)), split M into clusters = components of the "distance 2" graph on M. Distinct clusters
are at distance >= 4, so there are at most A(9,4) = 20 clusters; the target needs |M| - |Z| >= 21, so some
cluster K must have |K| - |Z_K| >= 2. Now CHECKED exhaustively (code/cluster_value.py, lemma L2 in
claims.md): every distance-2-connected set of 2..5 same-parity vertices has value <= 1, so (L3) a decycling set of
size <= 235 needs a cluster of size >= 6 with value >= 2 on BOTH parity sides. The even part of a Q_5 subcube
(16 vertices) has value 2 but blocks far too much space (by a hand count, at most ~12 in total). Next steps: port
cluster_value to C and push to sizes 6-8 (about 4-5 million sets at size 6), list the value->=2 clusters with the
smallest neighbourhood |N(K)|, and pack them with a code by exact search; if no cluster of size <= s has value >= 2,
the search for 235 can be restricted to forests with large clusters.

No lower bound follows from any of this: all searches are incomplete (SEARCH-FOUND-NOTHING).
