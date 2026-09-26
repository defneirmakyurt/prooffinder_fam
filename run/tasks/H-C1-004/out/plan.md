# Plan: H-C1-004 (searcher, BLIND, phase 1) -- U(Q_3) and U(Q_4)

Target: integers U(Q_3), U(Q_4); for each, (a) labelling attaining V (scored by inbox/checker/verify.py),
(b) evidence every labelling has >= V uphill paths.

Ladder (dependencies in brackets):
- R1 NOT STARTED -- checker sanity: checker reproduces hand-computed counts (weight-order labelling of Q_3 gives 1+3+6+6=16). []
- R2 NOT STARTED -- counting recursion N(v) = [valley] + sum_{lower nbrs} N(w) (independent re-derivation). []
- R3 NOT STARTED -- Q_3 exhaustive over all 8! = 40320 bijections: min value V3 and a minimiser. [R2]
- R4 NOT STARTED -- Q_4 upper bound: stochastic local search finds labelling with count V4'. [R2]
- R5 NOT STARTED -- lower-bound function LB for partial labellings is sound (written proof). [R2]
- R6 NOT STARTED -- state-memo pruning is sound (future cost depends only on (S, N on boundary of S)). [R2]
- R7 NOT STARTED -- translation symmetry: may fix label 1 at 0000 (written proof), if used. []
- R8 NOT STARTED -- Q_4 exhaustive branch-and-bound over all 16! bijections: none has count < V4'. [R5,R6,R7]
- R9 NOT STARTED -- cross-check B&B on Q_3 against brute force R3. [R3,R8]
- R10 NOT STARTED -- artefacts out/Q3.txt, out/Q4.txt scored by provided checker. [R3,R4]
