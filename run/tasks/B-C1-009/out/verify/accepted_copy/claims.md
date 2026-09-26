| claim | status | where proved (file, step) |
|---|---|---|
| R1: B maps P(n) to P(n); every orbit reaches a cyclic partition | PROVED | proof.md, 1.1-1.2 |
| R2: C(U(lambda)) = R(C(lambda)) (bijection), E(U(lambda)) = E(lambda) | PROVED | proof.md, 2.1-2.2 |
| R3: sorting lemma E(sort c) <= E(c), equality iff c weakly decreasing | PROVED | proof.md, Lemma 3 (3.1-3.5) |
| R4: E non-increasing under B; on a cycle no sorting, C(B^t lambda) = R^t(C(lambda)) | PROVED | proof.md, 4.1-4.2 |
| R5: R rotates each diagonal D_d cyclically (order d) | PROVED | proof.md, 5.1-5.2 |
| R6: cyclic lambda, D_d not full => D_{d+1} empty | PROVED | proof.md, Lemma 6 |
| R7: cyclic partition of T_{k-1}+r = delta_{k-1} cells + r cells of D_k, i.e. lambda(eps) | PROVED | proof.md, 7.1-7.5 |
| R8: B(lambda(eps)) = lambda(rho eps); each lambda(eps) cyclic; eps -> lambda(eps) injective | PROVED | proof.md, 8.1-8.4 |
| R9 (ii)(a): cyclic partitions of n = {lambda(eps): eps in {0,1}^k, sum eps = r}, binom(k,r) of them | PROVED | proof.md, Theorem 9 |
| R10 (ii)(b): #cycles = (1/k) sum_{d | gcd(k,r)} phi(d) binom(k/d, r/d) | PROVED | proof.md, 10.1-10.4 |
| R11 (i): delta_k unique cyclic partition of T_k; every lambda reaches it | PROVED | proof.md, 11 |
| Brute-force agreement of (i), (ii)(a), (ii)(b) for all 1 <= n <= 45 (not load-bearing) | CHECKED | code/check_c1.py |
