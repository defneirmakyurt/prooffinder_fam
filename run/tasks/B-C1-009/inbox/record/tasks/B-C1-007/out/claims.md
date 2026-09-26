# Claims: B-C1-007 (literature, Phase 1L)

| claim | status | where proved |
|---|---|---|
| B = sort(U); sort is a single insertion of s at position p (p-1 = #tail entries > s) | PROVED | proof.md 1.1-1.3 |
| R is a level-preserving bijection of N^2; R(C(lambda)) = C(U(lambda)), E(U) = E | PROVED | proof.md 2.1-2.2 (Lemma 1) |
| R rotates each level D_l cyclically (period l) | PROVED | proof.md 2.3 (Lemma 2) |
| E(B lambda) <= E(lambda) - (p-1); equality iff lambda_1 - 1 <= s, then C(B lambda) = R(C lambda) | PROVED | proof.md 3 (Lemma 3) |
| on a cycle: C(B^t lambda) = R^t(C(lambda)) | PROVED | proof.md 3 (Lemma 4) |
| cyclic lambda: hole on D_l => D_{l+1} empty (progression argument, no CRT) | PROVED | proof.md 4 (Lemma 5) |
| cyclic lambda of rank-k n: D_1..D_{k-1} subset C subset D_1..D_k, r cells on D_k | PROVED | proof.md 5 (Prop. 6) |
| C(lambda(eps)) = D_1..D_{k-1} + {pos i of D_k: eps_i = 1}; B(lambda(eps)) = lambda(rho eps); injective | PROVED | proof.md 6 (Lemmas 7, 8, Cor. 9) |
| (ii)(a): cyclic partitions of T_{k-1}+r are exactly lambda(eps), eps in W(k,r); binom(k,r) of them | PROVED | proof.md 7 (Thm 10) |
| (i): delta_k unique cyclic partition of T_k; every orbit reaches it | PROVED | proof.md 8 (Thm 11) |
| (ii)(b): #cycles = (1/k) sum_{d|gcd(k,r)} phi(d) binom(k/d, r/d) (Burnside proved inline) | PROVED | proof.md 9 (Thm 12) |
| same statements in the literature (Brandt 1982 Thm 5; Akin-Davis 1985 Thm 5; Griggs-Ho 1998 Thm 2.1; Hart-Khan-Khan Thm 1, Cor. 9; Drensky Thms 1-2) | cited, not used as proof; Brandt/Akin-Davis/Griggs-Ho/Etienne NOT opened | sources.md |
| brute-force agreement for 1 <= n <= 50 (incl. Lemma 3 equality criterion) | COMPUTER-VERIFIED (code public: y, out/code/check_c1_lit.py), not load-bearing | out/code/run50.log |
