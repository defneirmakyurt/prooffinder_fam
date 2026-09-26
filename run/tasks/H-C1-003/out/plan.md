# Plan: H-C1-003 (U(Q_3), U(Q_4)), BLIND searcher

Target: the integers U(Q_3), U(Q_4); for each d an explicit attaining labelling (out/Q3.txt, out/Q4.txt)
and a lower-bound argument (computer-assisted, exact, stdlib Python, < 10 min).

| Rung | Sub-claim | Depends on | Status |
|---|---|---|---|
| R1 | Provided checker reproduces a hand-computed small case (identity order on Q_2, Q_3) | - | NOT STARTED |
| R2 | Recurrence N(v)=[valley]+sum_{lower nbrs} N(w) is exact (own fast scorer agrees with checker) | R1 | NOT STARTED |
| R3 | Automorphisms of Q_d preserve the number of uphill paths; so WLOG label 1 sits at 0...0 | - | NOT STARTED |
| R4 | Q_3: exhaustive over all 8! labellings gives min V3 and an attaining labelling | R2 | NOT STARTED |
| R5 | Q_4: heuristic search (random restarts + local swaps) gives an upper bound V4 | R2 | NOT STARTED |
| R6 | Prefix-DP soundness: state = (placed set S, N on S), future cost monotone in N; lower bound LB(S,N) on future valid | R2 | NOT STARTED |
| R7 | Q_4: exact prefix DP with pruning at V4-1 finds no complete labelling => U(Q_4) >= V4 | R3,R5,R6 | NOT STARTED |
| R8 | Cross-check: same DP on Q_3 reproduces V3 from R4 (and DP at threshold V4 finds attaining labellings for Q_4) | R4,R7 | NOT STARTED |
| R9 | Artefacts Q3.txt/Q4.txt scored with inbox/checker/verify.py | R4,R5 | NOT STARTED |
