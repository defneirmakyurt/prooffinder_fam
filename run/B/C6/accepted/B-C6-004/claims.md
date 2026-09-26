# Claims (B-C6-004)

| claim | status | where proved (file, step) |
|---|---|---|
| Lemma 1: if s >= lambda_1 - 1 then B(lambda) = (s, lambda_1-1, ..., lambda_s-1), zeros deleted | PROVED | proof.md §1 |
| Lemma 2: kappa(A) = delta_{k-1}+1_A satisfies B(kappa(A)) = kappa(A+1 mod k); all of S_k cyclic, S_k B-closed | PROVED | proof.md §2 |
| Lemma 3: first hitting time of S_k equals d_B | PROVED | proof.md §2 |
| Prop A: d_B(1^n) = n-k+1 for every n >= 3 (rank k) | PROVED | proof.md §3 |
| Prop B: d_B(delta_{k-1} u {r-1,1}) = r(k+1)-2k for k>=2, 2<=r<=k | PROVED | proof.md §4 |
| Prop C: d_B(delta_{k-2} u {k-2,r+1}) = (k-1)(k-2-r) for k>=4, 1<=r<=k-3 | PROVED | proof.md §5 |
| Theorem: D_B(n) >= F(n) for every n >= 1 | PROVED | proof.md §6 |
| D_B(n) = F(n) for 1 <= n <= 62 | CHECKED | code/conj_check.py; code/run_conj_1_55.txt, code/run_conj_56_62.txt |
| D_B(n) = F(n) for all n (upper half) | GAP (conjectured) | not proved |
| Sanity: Props A,B,C formulas agree with direct orbit computation for 4<=k<=29 | CHECKED (not load-bearing) | code/witness_check.py |
