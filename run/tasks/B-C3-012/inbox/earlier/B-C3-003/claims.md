| claim | status | where proved |
|---|---|---|
| R1: B(lambda) = phi(cells of lambda), phi bijective (cell map lemma) | PROVED | proof.md Step 1 |
| R2: cyclic partitions of T_m+r = delta_m + r cells of diagonal m (restates Cell 1) | PROVED (from Cell 1) | proof.md Step 2 |
| R3: late-phase dynamics (rotation, single drop rule), d_B = t*+1 | PROVED | proof.md Step 3 |
| R4: X_k=(k-1,k-2,k-2,k-3,...,2,1,1) is a partition of T_k-1 with d_B(X_k)=k^2-2k-1, all k>=4 | PROVED | proof.md Step 4; CHECKED k=4..25 code/check.py |
| R5: on the class L_k, max d_B = k^2-2k-1, uniquely at X_k | PROVED | proof.md Step 5; CHECKED k=4..25 code/check.py |
| R6: D_B(2)=0, D_B(5)=3 (only (1^5)); k=1 excluded | PROVED | proof.md Step 6 |
| R7 (a): d_B(lambda) <= k^2-2k-1 for all lambda of n, T_{k-1}<n<T_k, k>=4 | GAP (CHECKED exhaustively only for 4<=k<=9) | proof.md Step 7; code/check.py |
| R8 (b): D_B(T_k-1)=k^2-2k-1 for k>=4 | lower bound PROVED; upper bound GAP (CHECKED 4<=k<=9) | Steps 4, 7 |
| R9 (c): exact extremal set E_k | GAP (X_k in E_k conditional on R7; E_k != {X_k} for 5<=k<=9; counts 1,6,34,175,831,3911 for k=4..9) | Step 8; code/check.py |
