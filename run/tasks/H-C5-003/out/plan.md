# Plan: H-C5-003 (EXPLOIT of H-C5-002), UPPER route only

Target: a labelling of Q_9 with <= 2399 uphill paths (out/Q9.txt), scored by inbox/checker/verify.py.
Search guide (subject proof.md, not refereed; used only to steer the search): P(f) = 512 + 8|S_f| + extra,
S_f decycling set, so a hand-in needs an induced forest F of Q_9 with |F| >= 277 (|S| <= 235) and a
labelling of S with extra <= 1887 - 8|S|.

Rungs (dependencies in brackets):
- R1 checker reproduces subject Q9.txt = 2400. [-]  STATUS: CHECKED (VERIFIED 2400, 0.025 s)
- R2 new local search (min-vertex-multiway-cut repair move: add v, delete the minimum vertex set of the
  touched trees that separates v's F-neighbours; plateau moves possible, which the predecessor's
  neighbour-eviction move cannot make) reproduces known optima |S| = 14, 28, 56, 112 for d = 5..8. [-]
- R3 same search on d = 9 reaches |S| = 236. [R2]
- R4 same search reaches |S| <= 235 on d = 9 (induced forest >= 277). [R3]
- R5 labelling built from the forest (BFS forest order, then S ordered to minimise extra) scores <= 2399
  on the checker. [R4]
- R6 (fallback if R4 fails) structured sub-searches: parity-dominated class (M even kept, Z odd removed)
  and/or symmetric (group-invariant) forests; report as SEARCH-FOUND-NOTHING for the class searched. [R3]

Status is kept current below.

## Status
- R1 CHECKED: VERIFIED 2400 on inbox/subject/Q9.txt, 0.025 s.
- R2 CHECKED: |S| = 14, 28, 56, 112 for d = 5..8, each in < 1 s (runlog.md).
- R3 CHECKED: |S| = 236 on d = 9 in 11 s. The labelling built from it gets checker VERIFIED 2400
  (out/Q9.txt, out/Q9_alt.txt).
- R4 GAP (SEARCH-FOUND-NOTHING): 7 multiway-cut SA runs at d = 9 (2e7..4e8 moves, incl. a constant-T walk
  on the 276-level set) and 2 symmetric penalty-SA runs never go below |S| = 236. Lazy SAT is too weak
  (times out on d = 7).
- R5 NOT STARTED (needs R4).
- R6 CHECKED (partial, structural): cluster reduction (claims.md C4, PROVED given A(9,4) = 20).
  Exhaustive over clusters of <= 6 words: all have net <= 1 (C5). Q_4-even cluster: net 2, but it leaves
  room for only a 16-word code (solver verdict), giving 18 < 21 (C6, C7). SEARCH-FOUND-NOTHING in these
  classes.
