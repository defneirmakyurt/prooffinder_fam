# Plan: H-C2-001, U(Q_5)  (BLIND, phase 1)

Target: the integer U(Q_5) = min over bijections f: {0,1}^5 -> {1..32} of #uphill paths.
Needs (a) explicit labelling with V paths (checker-scored), (b) proof every labelling has >= V.

Ladder (dependencies in brackets):
- R1 checker reproduces hand-computed small case (Q_2 lex order, T=5) — CHECKED
- R2 fast C scorer (search-internal) agrees with checker on the produced labellings [R1] — CHECKED
     (internal best = checker value on every saved output, runlog.md)
- R3 simulated annealing on Q_5 gives UB 88 [R2] — CHECKED (VERIFIED 88)
- R4 UB stable across 6 independent seeds; structurally different optimum saved (Q5_alt1.txt, 5 valleys
     vs 8) [R3] — CHECKED
- R5 T = E + sum_v ([valley] + (N(v)-1) up(v)) (proof.md Lemmas 1-3) — PROVED
- R6 exact layered DP over (placed set, N on boundary), admissible matching bound (Lemma 4); soundness
     written (proof.md) [R5] — PROVED
- R7 DP sanity: U(Q_3)=14 equals brute force over 8!; U(Q_4)=34 equals annealing [R6] — CHECKED
- R8 symmetry reductions (translations; full Aut orbit merging) sound (proof.md) [R6] — PROVED
- R9 DP on Q_5: no labelling has T <= 87 (exhaustive over all labellings via R5,R6,R8) [R6,R8] — CHECKED
     (run L5-H, 3m01s; corroborated by orbit-merged run L5-S)
- R10 conclusion U(Q_5) = 88 [R3,R9] — PROVED
