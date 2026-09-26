# Plan: H-C1-003 (U(Q_3), U(Q_4)), BLIND searcher

Target: the integers U(Q_3), U(Q_4); for each d an explicit attaining labelling
(out/Q3.txt, out/Q4.txt) and a lower-bound argument (computer-assisted, exact,
stdlib Python, < 10 min).

RESULT: U(Q_3) = 14, U(Q_4) = 34.

| Rung | Sub-claim | Depends on | Status |
|---|---|---|---|
| R1 | Provided checker reproduces hand-computed cases (Q_2 identity = 5, Q_2 cyclic = 5, Q_3 identity = 16) | - | CHECKED |
| R2 | Recurrence N(v)=[valley]+sum_{lower nbrs}N(w) is exact: own scorer + explicit DFS enumeration of all uphill paths agree with checker | R1 | CHECKED |
| R3 | Automorphism soundness: v -> v XOR u is an automorphism of Q_d, so WLOG label 1 sits at 0...0 | - | PROVED (not needed: final runs use --no-fix) |
| R4 | Q_3: exhaustive over ALL 8! = 40320 labellings gives min = 14 and an attaining labelling | R2 | CHECKED |
| R5 | Q_4: local search (3 seeds, 200 restarts each) reaches 34, never lower | R2 | CHECKED (heuristic only, upper bound) |
| R6 | Lower-bound function LB(S,N) is a valid lower bound on the future cost of every completion | R2 | PROVED (argument in out/claims.md and code/README.md) |
| R7 | Q_4: exact prefix DP at threshold T = 33 over ALL labellings (no symmetry fix) has no surviving state => U(Q_4) >= 34 | R2,R6 | CHECKED |
| R8 | Cross-checks: (a) DP on Q_3 at T=13 empty / T=14 found, matching R4; (b) independent branch-and-bound WITHOUT state merging, no symmetry fix, at d=4 T=33 empty and T=34 found | R4,R7 | CHECKED |
| R9 | Artefacts out/Q3.txt (VERIFIED 14) and out/Q4.txt (VERIFIED 34) scored by inbox/checker/verify.py | R4,R7 | CHECKED |
| R10 | Control: same DP at d=4 T=33 with LB pruning switched off entirely | R7 | GAP (TIMED OUT at 10 min; R8(b) is the substitute independent check) |
