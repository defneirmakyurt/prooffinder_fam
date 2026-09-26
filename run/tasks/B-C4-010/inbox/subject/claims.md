# Claims: B-C4-006

| claim | status | where proved (file, step) |
|---|---|---|
| Diagram criterion (C) characterises partition diagrams | PROVED | proof.md Step 1 |
| rho: diag(lambda) -> S(R(lambda)) bijection, preserves diagonal index, shifts positions on D_d by +1 mod d | PROVED | proof.md Step 3 |
| lambda_1 <= s+1 => diag B(lambda) = rho(diag lambda), E unchanged; lambda_1 >= s+2 => rho(diag lambda) not a diagram and E drops by >= 1 | PROVED | proof.md Step 4 |
| eps = [sum_{d>=k}(d-k+1)o_d - 1] + sum_{d<=k-1}(k-1-d)(d-o_d) >= 0 for n = T_{k-1}+1 | PROVED | proof.md Step 5 |
| eps(lambda) = 0 iff lambda cyclic (uses B-C1, r=1) | PROVED | proof.md Step 6 |
| eps = 1 iff D_1..D_{k-2} full, one hole on D_{k-1}, two cells on D_k, nothing higher | PROVED | proof.md Step 7 |
| Level-1 partitions <-> triples (Q; P<P') with P,P' not in {Q,Q+1} | PROVED | proof.md Step 8 |
| For eps = 1: d_B(lambda) = T = first t >= 1 at which the rotated triple violates the constraint | PROVED | proof.md Steps 9-10 |
| Lap lemma: violation of c_t depends only on the lap index a, and holds iff pi_a or pi'_a in {0,1} | PROVED | proof.md Step 11 |
| eps <= 1 => d_B <= (k-1)(k-3); on level 1 equality iff triple (0; k-2, k-1) | PROVED | proof.md Step 12 |
| LOWER: d_B(lambda^(k)) = (k-1)(k-3), lambda^(k) = (k-2,k-2,k-3,...,3,2,2,1), every k >= 5 | PROVED | proof.md Step 13 |
| B^{F-1}(lambda^(k)) = (k,k-1,k-3,...,2), B^F(lambda^(k)) = lambda(e_3) | PROVED | proof.md Step 13 |
| UPPER for all partitions of T_{k-1}+1, all k >= 5 | GAP | proof.md Step 14; stuck.md |
| D_B(T_{k-1}+1) = (k-1)(k-3) for k = 5..11 (evidence only) | CHECKED | code/check.py part (1) |
| Step 12 closed form T matches the true d_B on every level-1 partition, k = 5..25 (sanity check of the proof) | CHECKED | code/check.py part (3) |
| Lower-bound orbit end predicted in Step 13, k = 5..60 (sanity check) | CHECKED | code/check.py part (2) |
