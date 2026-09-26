# Plan: B-C3-004 (BLIND prover)

Reading of the target: exactly as in TARGET (a), (b), (c). Notation: diagram of lambda = {(i,j): j <= lambda_i};
cell (i,j) lies on diagonal i+j-1; delta_m = diagram of all cells on diagonals <= m.
C_k := { lambda : delta_{k-1} subset lambda subset delta_{k+1} } ("near-staircase class").

| Rung | Statement | Uses | Status |
|---|---|---|---|
| R1 | For n = T_{k-1}+r, 1<=r<=k-1: lambda cyclic iff delta_{k-1} subset lambda subset delta_k; B maps cyclic to cyclic; d_B(lambda) <= t iff B^t(lambda) cyclic | Cell 1 | PROVED (Step 1) |
| R2 | Encoding: lambda in C_k <-> 0/1 vectors (A_0..A_{k-1}), (P_0..P_k) with support rule (S); row formula; size T_{k-1}+|A|+|P| | def. | PROVED (Step 2) |
| R3 | Dynamics on C_k: B = rotate A (mod k) and P (mod k+1), except when A_{k-1}=0 and P_0=1: then additionally A'_0:=1, P'_1:=0 (absorption) | R2 | PROVED (Step 3); also CHECKED k=3..10 (check_classC.py) |
| R4 | Rotating frame: hole labels H_t only shrink, one label per absorption; particle Q checks label Q-1-v at time (k+1)v-Q | R3 | PROVED (Step 4) |
| R5 | Counting lemma: with |H_0| >= p+1, particle with Q<=k-1 absorbed by check k-3, with Q in {k,k+1} by check k-2 | R4 | PROVED (Step 5) |
| R6 | (a) restricted to C_k: d_B(lambda) <= k^2-2k-1 for k>=3, lambda in C_k, n non-triangular of rank k | R1,R5 | PROVED (Step 6) |
| R7 | (b) lower bound: lambda*_k=(k-1,k-2,k-2,k-3,...,2,1,1) has d_B = k^2-2k-1 (k>=3); B^{k^2-2k-2}(lambda*_k)=nu_k=(k+1,k-1,k-2,...,3,1) | R1,R3,R4 | PROVED (Step 7) |
| R8 | (a) in full: every lambda of every non-triangular n of rank k>=4 (lambda outside C_k) | ? | GAP (no reduction to C_k); CHECKED 4<=k<=10 only |
| R9 | (b): D_B(T_k-1)=k^2-2k-1 for k>=4; D_B(2)=0 (k=2), D_B(5)=3 (k=3) | R7, R8 | lower bound PROVED; upper bound = R8 (GAP; CHECKED k<=10); small k PROVED |
| R10 | (c): {lambda : B^{k^2-2k-2}(lambda)=nu_k} is contained in the extremal set (given R9); equality | R7, R9 | "contained" PROVED (modulo R9 upper bound); equality GAP, CHECKED k=4..10; k=2,3 PROVED |

Stopping: R8 failed twice (attempted a) energy/phase monotone quantity, b) lowest-hole-diagonal argument); stopped as instructed.
