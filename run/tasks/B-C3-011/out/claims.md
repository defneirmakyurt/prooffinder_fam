# Claims: B-C3-011

| claim | status | where proved (file, step) |
|---|---|---|
| Column model: parts of row i = remaining lengths of covering columns; c_{i+1} = c_i + 1 - L_i | PROVED | proof.md §1 (1.1, 1.2, 1.3) |
| Sandwich lemma: c_i < x < c_j (i<j) => pattern (x-1,x,..,x,x+1) inside [i,j] | PROVED | proof.md §2, Lemma 2 |
| Triple lemma: (x-1,x,x+1) at p => p <= x | PROVED | proof.md §3, Lemma 3 |
| Shortening lemma (length >= 3, p > x => shorter pattern, x' <= x, p' >= p-x) | PROVED | proof.md §4, Lemma 4 |
| Descent: every pattern has p <= (q-p-1) x | PROVED | proof.md §5, Lemma 5 |
| Length lemma: q-p != x and q-p <= x+1 | PROVED | proof.md §6, Lemma 6 |
| Long-pattern lemma: q-p = x+1 = m => q <= T_{m-1}+2 | PROVED | proof.md §7, Lemma 7 |
| Cycle: B(lambda(e)) = lambda(rho e); c_{t+i} = k-1+e_{k+1-i}; c_u in {k-1,k} for u > t (uses B-C1) | PROVED | proof.md §8, 8.1-8.2 |
| End lemma: c_t in {k-2,k-1}; c_t = k-1 => unique part k+1 in row t, others <= k-1, c_{t+k-1} = k (uses B-C1) | PROVED | proof.md §9, Lemma 9 |
| c_t = k-2 => t <= k^2-2k-1 | PROVED | proof.md §10, Lemma 10 |
| c_t = k-1 => t <= k^2-2k-1 (cases A1, A2, B) | PROVED | proof.md §11, Lemma 11 |
| (a) d_B(lambda) <= k^2-2k-1 for all k>=4, all non-triangular n of rank k, all lambda | PROVED | proof.md §12, Theorem |
| (b-upper) D_B(T_k-1) <= k^2-2k-1, k >= 4 | PROVED | proof.md §12, Corollary |
| Lemmas 3,5,6,7,9 and the §10-§11 certificates on all partitions, 4<=k<=9 (n<=44 for general lemmas) | CHECKED (sanity only) | code/check_c3a.py, code/run_K9.txt |
