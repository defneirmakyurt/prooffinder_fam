# Plan: B-C3 (BLIND, Phase 1)

Notation: k >= 4, m = k-1 >= 3, n = T_m + r with 1 <= r <= m (so T_{k-1} < n < T_k); cells (i,j), 0-indexed
row i, column j; diagonal of (i,j) is i+j; "row i of diagonal d" = cell (i, d-i).

Reading of (b)/(c): F(k) must be given for all k >= 2 with T_k - 1 >= 1 (k = 1 gives n = 0, not a partition size).

| Rung | Statement | Depends | Status |
|---|---|---|---|
| R1 | Cell map lemma: B(lambda) = image of the cells of lambda under phi: (i,0)->(0,i); (i,j),1<=j<=s ->(i+1,j-1); (i,j), j>=s+1 -> (i,j-1) (s = number of parts). phi is a bijection onto the diagram of B(lambda). | defs | PROVED (proof.md Step 1) |
| R2 | Cyclic partitions of n = T_m + r are exactly delta_m union (r cells of diagonal m). | Cell 1 | PROVED (Step 2, restating Cell 1) |
| R3 | Late-phase dynamics: if lambda contains delta_m and all other cells lie on diagonals m, m+1 with exactly one on m+1, B rotates each diagonal (row i -> i+1 mod d+1) except that the diagonal-(m+1) cell at row 0 drops to (0,m) iff (m,0) is empty. | R1 | PROVED (Step 3) |
| R4 | Lower bound: X_k = (m, m-1, m-1, m-2, ..., 2, 1, 1) is a partition of T_k - 1 and d_B(X_k) = m^2 - 2 = k^2-2k-1 for every k >= 4. | R2, R3 | PROVED (Step 4) |
| R5 | In the class L (delta_m + (m-1) cells on diag m + one cell on diag m+1, n = T_k - 1), max d_B = m^2 - 2, attained only by X_k. | R2, R3 | PROVED (Step 5) |
| R6 | Small k: k=2 (n=2): D=0; k=3 (n=5): D=3; k=1: n=0 excluded. | defs | PROVED (Step 6, hand computation) |
| R7 | (a) upper bound: every partition lambda of n, T_{k-1}<n<T_k, k>=4, has d_B(lambda) <= k^2-2k-1. | R1, R2, ... | GAP for general k; CHECKED exhaustively for 4 <= k <= 9 (code/check.py) |
| R8 | (b) D_B(T_k - 1) = k^2-2k-1 for k >= 4 | R4, R7 | lower bound PROVED all k>=4; upper bound = R7 (GAP general k, CHECKED k<=9) |
| R9 | (c) exact extremal set E_k for n = T_k - 1 | R7 + equality analysis | GAP; X_k in E_k PROVED all k>=4; E_k computed exactly for k<=9 (counts 1,6,34,175,831,...); E_k != {X_k} for k>=5 |

Stopping: R7 attempted (early/late phase coupling) and did not close within the time box; R9 depends on it.
