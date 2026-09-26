# Claims: B-C2-001

| claim | status | where proved (file, step) |
|---|---|---|
| Down-closed sets are exactly partition diagrams; rows+columns initial segments criterion | PROVED | proof.md, Step 0.2 |
| Rotation rho: weight-preserving, injective, cyclic pi_d on each diagonal; rows of rho(Y) are (s, lambda_i - 1) | PROVED | proof.md, Steps 1.1-1.5 |
| If rho(Y) is down-closed then Y(B(lambda)) = rho(Y) | PROVED | proof.md, Step 1.6 |
| E(B(lambda)) <= E(lambda), equality only for pure rotation | PROVED | proof.md, Step 2.1-2.2 |
| For lambda |- T_k: E >= sum_{d<=k} d^2, equality iff lambda = delta_k; B(delta_k) = delta_k | PROVED | proof.md, Steps 3.1-3.3 |
| Pure rotation forever implies lambda = delta_k | PROVED | proof.md, Step 4.1 |
| Every partition of T_k reaches delta_k | PROVED | proof.md, Step 5.1 |
| delta_k is the unique cyclic partition of T_k; d_B = hitting time of delta_k | PROVED | proof.md, Steps 6.1-6.3 |
| d_B(lambda^(k)) = k^2 - k for every k >= 1 (lambda^(1) = (1), lambda^(k) = (k-1,k-1,k-2,...,1,1)) | PROVED | proof.md, Steps 7.0-7.9 |
| D_B(T_k) >= k^2 - k for every k >= 1 | PROVED | proof.md, Step 7.9 |
| D_B(T_k) <= k^2 - k for 1 <= k <= 11 (hence = k^2 - k) | CHECKED | proof.md, Step 8; code/check_triangular.py |
| D_B(T_k) <= k^2 - k for k >= 12 | GAP | proof.md, Step 9; stuck.md |
| D_B(T_k) = k^2 - k for every k >= 1 (target) | GAP | lower half Step 7 (all k); upper half only k <= 11 |
