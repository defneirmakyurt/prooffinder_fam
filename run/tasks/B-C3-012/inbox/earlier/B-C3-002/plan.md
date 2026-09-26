# Plan: B-C3-002 (prover, BLIND, phase 1)

Notation: n = T_{k-1}+r, 1<=r<=k-1 (non-triangular). Cells (i,j), i=row, j=column (0-based);
diagonal index i+j. E(lambda) = sum of diagonal indices of the cells of the Young diagram.
D_{m} = {(i,j): i+j<=m}. Phi(lambda) = E(lambda) - E_min(n).

| Rung | Statement | Uses | Status |
|---|---|---|---|
| R1 | Rotation lemma: R(i,j)=(i+1,j-1) (j>=1), R(i,0)=(0,i). R(C) is an order ideal iff lambda_1<=s+1, and then B(lambda) has diagram R(C), E preserved; if lambda_1>=s+2 then E(B lambda)<E(lambda). | defs | PROVED |
| R2 | E(S) >= E_min(n) for any n-set S, equality iff S = D_{k-2} + r cells of diagonal k-1; lambda cyclic iff Phi(lambda)=0. | R1, Cell 1 | PROVED |
| R3 | Classification of Phi=1 partitions: case A (one hole on diag k-2, r+1 cells on diag k-1, needs r<=k-3) or case B (D_{k-2} full, r-1 cells on diag k-1, one cell on diag k). For n=T_k-1 only case B. | R2 | PROVED |
| R4 | Case B dynamics: for admissible (H,c), d = 1-c+(k+1)*min_{a in H}((c-1-a) mod k). | R1,R2,R3 | PROVED (+CHECKED k<=10) |
| R5 | Max over case B is (k+1)(r-2)+2, attained only by c=k, H={0..h-1}; for r=k-1 only by lambda*_k=(k-1,k-2,k-2,k-3,...,2,1,1). | R4 | PROVED |
| R6 | Lower bound: d(lambda*_k)=k^2-2k-1 for every k>=3, so D_B(T_k-1)>=k^2-2k-1. | R5 | PROVED |
| R7 | d(mu_k)=2k+1 (k>=5), mu_k=(k,k-1,k-1,k-3,...,3,1); every lambda with B^{k^2-4k-2}(lambda)=mu_k has d=k^2-2k-1. | R4 | PROVED |
| R8 | (a) Upper bound d(lambda)<=k^2-2k-1 for all k>=4, all n in (T_{k-1},T_k), all lambda. | R1-R5 + ? | GAP (general k); CHECKED k=4..10 exhaustive |
| R9 | (b) D_B(T_k-1)=k^2-2k-1 for k>=4; D_B(2)=0 (k=2), D_B(5)=3 (k=3). | R6, R8 | lower bound PROVED all k>=3; equality CHECKED k=4..10; all k>=11 conditional on R8 (GAP); k=2,3 PROVED by hand |
| R10 | (c) Maximizers of T_k-1: k=2: {(2),(1,1)}; k=3: {(1^5)}; k=4: {(3,2,2,1,1)}; k=5: 6 listed; k>=6: exactly {lambda : B^{k^2-4k-2}(lambda)=mu_k}. | R7, R8 | k<=10 CHECKED; "contains" PROVED for all k>=6 modulo R8 (value of max); "only these" GAP for k>=11 |

Dependencies: R2 uses R1 and Cell 1; R3 uses R2; R4 uses R1-R3; R5 uses R4; R6 uses R5; R7 uses R4;
R8 would need a multi-excess-cell analysis (not done); R9 uses R6+R8; R10 uses R7+R8.
