# Plan: H-C5-009 (EXPLOIT, UPPER route only; subject H-C5-005 + merged sibling H-C5-003)

Target: a labelling of Q_9 with <= 2399 uphill paths (Q9.txt, 512 lines, line i = vertex with label i).
Guide (Lemma A, gated): #uphill >= 512 + 8|S|, S = {down >= 2}, V \ S an induced forest. So <= 2399
needs a decycling set of size <= 235 (and small extra). Both lineages stop at |S| = 236.

Ladder (status kept current):

- R1 checker reproduces subject's 2400 on inbox/subject/Q9.txt. Status: CHECKED (VERIFIED 2400, 0.03 s).
- R2 re-derive the value function (exact): for an induced forest F, S = V \ F,
  (a) |S| = 224 + (c(F) + e(S))/8   [c = #components of Q_9[F], e(S) = #edges inside S];
  (b) with M = F cap E, Z = S cap O: |S| = 256 - (|M| - |Z|), and for every M the optimal Z gives
      |M| - |Z| = sum over distance-2 clusters K of M of net(K) = |K| - tau(K)  (EQUALITY, not only <=).
  Depends on: nothing. Status: see claims.md.
- R3 exact canonical form for even-word sets under (even translations x coordinate permutations);
  soundness argued in writing. Depends on R2 (defines what is invariant). Status: see claims.md.
- R4 exhaustive enumeration of all distance-2-connected even sets of size k (up to symmetry) with exact
  tau, for k = 1..kmax (as far as the 10-min cap allows); report best net per size and every net>=2 class.
  Cross-check against the lineage's sizes 2..5 (value <= 1) and H-C5-003's size <= 6. Depends on R3.
- R5 packing: for each net>=2 cluster type found, exact max number of further even words at distance >= 4
  from the cluster and from each other (i.e. singletons packed around it). Need net + code >= 21. Depends on R4.
- R6 (only if R5 gives >= 21 somewhere) build forest -> labelling -> checker; need <= 2399.
- R7 a different search class not tried by the lineages (doubled construction Q_8 x Q_1 with one half a
  perfect Q_8 forest; or SA on M with exact tau), heuristic, as time allows.
