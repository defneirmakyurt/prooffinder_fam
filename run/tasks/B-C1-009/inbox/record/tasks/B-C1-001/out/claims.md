# Claims: B-C1-001

| claim | status | where proved (file, step) |
|---|---|---|
| R1: E(s, lambda_0-1, ..., lambda_{s-1}-1) = E(lambda) | PROVED | proof.md, Step 1.2 (Lemma 1) |
| R2: sorting weakly lowers E, strictly if not already weakly decreasing | PROVED | proof.md, Step 1.3 (Lemma 2) |
| R3: E(B(lambda)) <= E(lambda); equality => s >= lambda_0 - 1; then B(lambda) = mu minus trailing zeros | PROVED | proof.md, Step 1.4 (Lemma 3) |
| R4a: sort-free step moves cells by tau | PROVED | proof.md, Step 2.2 (Lemma 4) |
| R5: tau rotates each diagonal D_d with period d+1 | PROVED | proof.md, Step 2.3 (Lemma 5) |
| R4: along a cycle every step is sort-free and Y(B^t lambda) = tau^t Y(lambda) | PROVED | proof.md, Step 2.4 (Lemma 6) |
| R6: a cyclic partition has no hole on D_d together with a cell on D_d', d < d' | PROVED | proof.md, Step 3.1 (Prop. 7) |
| R6': cyclic => full diagonals below e, r' <= e cells on D_e, none above; n = T_e + r' | PROVED | proof.md, Step 3.2 (Cor. 8) |
| R8: lambda(eps) is a partition of T_{k-1}+r; cell set; injective; B(lambda(eps)) = lambda(rho eps) | PROVED | proof.md, Step 4.2 (Thm 9) |
| R8': every element of C(k,r) is cyclic (B^k = id on C(k,r)) | PROVED | proof.md, Step 4.3 (Cor. 10) |
| R9 = (ii)(a): cyclic partitions of T_{k-1}+r are exactly C(k,r); there are binom(k,r) | PROVED | proof.md, Step 5.1 (Thm 11), 5.2 |
| cycles partition the cyclic set; cycles <-> rotation orbits on W(k,r) | PROVED | proof.md, Steps 6.1, 6.2 |
| orbit-counting lemma | PROVED | proof.md, Step 6.3 |
| fixed-point count of rho^j on W(k,r) | PROVED | proof.md, Steps 6.4, 6.5 |
| R10 = (ii)(b): #cycles = (1/k) sum_{d | gcd(k,r)} phi(d) binom(k/d, r/d) | PROVED | proof.md, Step 6.6 (Thm 12) |
| R11 = (i): n = T_k: delta_k only cyclic partition; every orbit reaches delta_k | PROVED | proof.md, Step 7.1 (Thm 13) |
| sanity: brute force agrees with (i), (ii)(a), (ii)(b) and E-monotonicity for 1 <= n <= 45 | CHECKED (not load-bearing) | out/code/check_c1.py |
