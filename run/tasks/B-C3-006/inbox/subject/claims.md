| claim | status | where proved (file, step) |
|---|---|---|
| R1: B = R (rotation) with E preserved iff lambda_1 <= s+1; else E drops by >= 1 | PROVED | proof.md 1.3-1.4 |
| R2: E >= E_min(n), equality iff D_{k-2} + r cells on diag k-1; cyclic iff Phi=0 (uses Cell 1) | PROVED | proof.md 2.4-2.5 |
| R3: Phi=1 partitions are case A (needs r<=k-3) or case B; for T_k-1 only case B | PROVED | proof.md 3.2-3.4 |
| R3': S(H,c) order ideal iff (H,c) admissible | PROVED | proof.md 3.5 |
| R4: d_B(Lambda(H,c)) = 1-c+(k+1) min_{a in H} ((c-1-a) mod k) | PROVED; also CHECKED k=3..10 | proof.md 4.2-4.5; code/check_c3.py lines (L) |
| R5: max over case B = (k+1)(r-2)+2, unique maximiser c=k, H={0..h-1}; for T_k-1: lambda*_k unique Phi=1 maximiser | PROVED | proof.md 5.1-5.4 |
| R6: d_B(lambda*_k)=k^2-2k-1 for all k>=3, so D_B(T_k-1) >= k^2-2k-1 | PROVED | proof.md 6.1 |
| R7: d_B(mu_k)=2k+1 (k>=5); every lambda with B^{k^2-4k-2}(lambda)=mu_k has d_B=k^2-2k-1 | PROVED | proof.md 7.1-7.3 |
| R8 / (a): d_B(lambda) <= k^2-2k-1 for all k>=4, T_{k-1}<n<T_k | GAP for k>=11; CHECKED 4<=k<=10 | proof.md 8.1-8.2; code/check_c3.py |
| (b): D_B(T_k-1)=k^2-2k-1 | lower bound PROVED k>=3; equality CHECKED 4<=k<=10; GAP k>=11 | proof.md 6.1, 8.2, 8.4 |
| (b) small k: D_B(2)=0, D_B(5)=3 | PROVED (by hand) and CHECKED | proof.md 8.3 |
| (c) k=2,3 maximisers {(2),(1,1)}, {(1^5)} | PROVED (by hand) | proof.md 8.3, 9.1 |
| (c) k=4: {(3,2,2,1,1)}; k=5: 6 listed partitions | CHECKED | proof.md 9.2; code/check_c3.py |
| (c) 6<=k<=10: maximisers = {lambda : B^{k^2-4k-2}(lambda) = mu_k} | CHECKED | proof.md 9.3; code/check_c3.py |
| (c) k>=11: that set is the maximiser set | GAP (inclusion M_k subset {d=k^2-2k-1} PROVED; maximality needs R8; completeness open) | proof.md 9.4 |
