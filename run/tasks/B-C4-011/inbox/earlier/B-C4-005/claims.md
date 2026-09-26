# Claims: B-C4-005

| claim | status | where proved |
|---|---|---|
| Conjectured formula F(k) = (k-1)(k-3) for k >= 5 | CHECKED for 5 <= k <= 11 only | out/code/check.py; proof.md Step 9.3 |
| Lemma C: lambda |- T_{k-1}+1 cyclic iff diagram contains delta_{k-1} (uses B-C1, r=1) | PROVED | proof.md Step 1 |
| Lemma R: non-sorting step rotates each diagonal | PROVED | proof.md Step 2 |
| Lemma S: near-state sorting criterion and rotation | PROVED | proof.md Step 3 |
| Lemma F: sorting step of near state (k-1,{1,q}) gives lambda(e_{q+1}), cyclic | PROVED | proof.md Step 4 |
| LOWER: d_B(lambda^(k)) = (k-1)(k-3) for every k >= 5, lambda^(k) = (k-2,k-2,k-3,...,3,2,2,1) | PROVED | proof.md Step 5 |
| Lemma M: lambda subset mu => B(lambda) subset B(mu) | PROVED | proof.md Step 6 |
| Corollary U1: d_B(lambda) <= min_c d_B(lambda\c) <= (k-1)(k-2) (uses B-C1, B-C2 at k-1) | PROVED | proof.md Step 7 |
| Theorem N: every near state has d_B <= (k-1)(k-3), k >= 5 | PROVED | proof.md Step 8 |
| UPPER: d_B(lambda) <= (k-1)(k-3) for every lambda |- T_{k-1}+1, every k >= 5 | GAP | proof.md Step 9.2; out/stuck.md |
| TARGET: D_B(T_{k-1}+1) = (k-1)(k-3) for every k >= 5 | GAP (lower half PROVED) | proof.md Steps 5, 9 |
