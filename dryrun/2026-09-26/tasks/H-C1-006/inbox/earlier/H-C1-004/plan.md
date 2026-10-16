# Plan: H-C1-004 (searcher, BLIND, phase 1) -- U(Q_3) and U(Q_4)

Target: integers U(Q_3), U(Q_4); for each, (a) labelling attaining V (scored by inbox/checker/verify.py),
(b) evidence every labelling has >= V uphill paths.

RESULT: U(Q_3) = 14, U(Q_4) = 34.  Both halves established by exhaustive computation.

Ladder (dependencies in brackets):

- R1 CHECKED -- checker sanity: the weight-order labelling of Q_3 (000 / 001,010,100 / 011,101,110 / 111)
  is hand-computed to have 1 + 3 + 6 + 6 = 16 uphill paths; inbox/checker/verify.py on out/tmp/q3_weight.txt
  prints `VERIFIED 16`.  []
- R2 PROVED -- counting recursion N(v) = [v valley] + sum over neighbours w with f(w) < f(v) of N(w),
  total = sum_v N(v).  Full proof in out/claims.md section "R2".  Independently implemented in
  out/code/uphill.py and cross-checked against the provided checker on 300 random labellings of Q_3
  and 300 of Q_4: 0 mismatches (out/code/crosscheck.py counter).  []
- R3 CHECKED -- Q_3 exhaustive over ALL 8! = 40320 bijections V(Q_3) -> {1..8}, no symmetry reduction:
  minimum = 14, attained by 7104 labellings.  out/code/brute_q3.py, 0.25 s.  [R2]
- R4 CHECKED -- Q_4 upper bound by stochastic local search: 20 seeds x 60000 annealing iterations all
  reach 34, none below.  out/code/sa_q4.py, 13.11 s.  (Superseded as evidence by R8b, which both
  exhibits a labelling with 34 and proves 34 is optimal.)  [R2]
- R5 PROVED -- the lower-bound function LB(S) for partial labellings is a valid lower bound on the cost
  of every completion.  Full proof in out/claims.md section "R5".  [R2]
- R6 PROVED -- the state memo is sound: the achievable future costs depend only on
  (S, N restricted to the boundary of S).  Full proof in out/claims.md section "R6".
  NOT load-bearing: the headline Q_4 lower bound is reproduced with the memo switched off (R8b).  [R2]
- R7 NOT STARTED -- symmetry reduction.  DELIBERATELY UNUSED.  The search enumerates all n! bijections,
  so no symmetry soundness argument is needed.  []
- R8a CHECKED -- Q_4 exhaustive branch-and-bound over ALL 16! = 20922789888000 bijections, LB + memo:
  `bnb.py 4 34` prints `NONE BELOW 34` in 0.09 s (9425 nodes).  [R5,R6]
- R8b CHECKED -- same claim with the memo DISABLED, so it rests on R5 and the trivial prune only:
  `bnb.py 4 34 --nomemo` prints `NONE BELOW 34` in 0.85 s (135169 nodes).  This is the run the
  lower bound U(Q_4) >= 34 is claimed from.  [R5]
- R9 CHECKED -- cross-checks of the branch-and-bound against R3 on Q_3:
  `bnb.py 3 14` / `--nomemo` / `--nolb` / `--nomemo --nolb` all print `NONE BELOW 14`;
  the last uses no LB and no memo at all (59681 nodes, 0.10 s), so it is an independent
  confirmation of the R3 brute force.  `bnb.py 3 15` prints `FOUND 14`.  [R3,R8]
- R10 CHECKED -- artefacts out/Q3.txt and out/Q4.txt, both emitted by bnb.py (`--out`), scored by the
  provided checker: `VERIFIED 14` and `VERIFIED 34`.  [R3,R8]
- R11 CHECKED -- threshold sweeps confirm the transition point.  d=3: `NONE BELOW T` for T = 1..14,
  `FOUND 14` for T = 15,16.  d=4: `NONE BELOW T` for T = 30..34, `FOUND 34` for T = 35,36.
  Also `bnb.py 4 35 --nomemo --nolb` (no pruning beyond the trivial one) prints `FOUND 34`
  after 160457098 nodes / 451.59 s.  [R8]
