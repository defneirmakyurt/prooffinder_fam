# Claims: B-C2-006

| claim | status | where proved (file, step) |
|---|---|---|
| D(B l) = rho(D l) then compaction of columns j > s; rho rotates each track | PROVED | proof.md, Steps 1-3 |
| Energy non-increasing, equality iff no compaction | PROVED | proof.md, Step 4 |
| delta_k is the only cyclic partition of T_k; d_B = first time B^i l = delta_k | PROVED | proof.md, Steps 5-9 |
| R_k (delta_{k-1} <= l <= delta_{k+1}) is B-invariant; dynamics = single-row annihilations | PROVED | proof.md, Steps 10-12 (also Step 21) |
| tau(h,i) <= k^2-k for i-h not in {0,1} | PROVED | proof.md, Step 13 |
| d_B(l) <= k^2-k for every l in R_k, every k >= 1 | PROVED | proof.md, Step 14 |
| (B l)'_j = l'_{j+1} + [j <= l'_1] | PROVED | proof.md, Step 19 (sanity: code/check_monotone_queue.py, n<=16) |
| D(l) subset D(m) => D(B l) subset D(B m), any sizes | PROVED | proof.md, Step 20 (sanity: code/check_monotone_queue.py, n<=16) |
| delta_m subset l => delta_m subset B^t l; l subset delta_m => B^t l subset delta_m | PROVED | proof.md, Step 21 |
| queue form e_j(B l) = e_{j+1}(l) + [j <= k+e_1] - [j <= k] | PROVED | proof.md, Step 22 |
| d_B(l) <= k^2-k for all l of T_k, k = 1,2 | PROVED | proof.md, Step 23a |
| d_B(l) <= k^2-k for all l of T_k, 1 <= k <= 11 | CHECKED | proof.md, Step 23b; code/check_DB_triangular.py |
| d_B(l) <= k^2-k for all l of T_k, all k >= 1 (TARGET, upper half) | GAP | proof.md, Step 24; stuck.md |
