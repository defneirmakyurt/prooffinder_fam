# Claims: B-C2-002

| claim | status | where proved (file, step) |
|---|---|---|
| D(B(l)) = rho(D(l)) followed by moving every column j > s up one row; rho keeps tracks, rotates rows of track d cyclically | PROVED | proof.md, Steps 1-3 |
| Energy E non-increasing under B; equality iff no compaction | PROVED | proof.md, Step 4 |
| l of T_k, l != delta_k => hole on some track <= k and cell on some track > k; cells on track e => cells on tracks 1..e | PROVED | proof.md, Steps 5-6 |
| delta_k is the only cyclic partition of T_k (every k >= 1); d_B(l) = first time B^i(l) = delta_k | PROVED | proof.md, Steps 7-9 |
| Two-track region R_k = {delta_{k-1} <= l <= delta_{k+1}} is B-closed; inside it only (row-1 hole of track k, row-2 cell of track k+1) annihilations occur | PROVED | proof.md, Steps 10-12 |
| tau(h,i) = k*x0 + 1 - h <= k^2-k for valid pairs, equality iff (h,i) = (1,k+1) | PROVED | proof.md, Step 13 |
| d_B(l) <= k^2 - k for every l in R_k, every k >= 1 | PROVED | proof.md, Step 14 |
| d_B(lambda^(k)) = k^2 - k, lambda^(k) = (k-1,k-1,k-2,...,1,1) (k>=2), (1) (k=1); so D_B(T_k) >= k^2-k for all k >= 1 | PROVED | proof.md, Step 15 |
| D_B(T_k) <= k^2 - k for k = 1, 2 | PROVED | proof.md, Step 16 |
| D_B(T_k) = k^2 - k for 1 <= k <= 11 (exhaustive over all partitions of T_k) | CHECKED | proof.md, Step 17; code/check_DB_triangular.py |
| d_B(l) <= k^2 - k for every partition l of T_k, every k (in particular k >= 12) | GAP | proof.md, Step 18; stuck.md |
| D_B(T_k) = k^2 - k for every k >= 1 (target) | GAP (lower half PROVED for all k; equality for k <= 11) | proof.md, Steps 15-18 |
| Invariant "t + max over (track-k hole, track-(k+1) cell) pairs of tau <= k^2-k along every orbit" | REFUTED | tmp/explore2.py (violations for all 3 <= k <= 8), stuck.md |
