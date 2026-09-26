# Claims: A-C3-002

| claim | status | where proved (file, step) |
|---|---|---|
| R1: theta_ij = pi/2 - arcsin\|g_ij\|; S = C(n,2) pi/2 - T; target iff T >= pi/2 | PROVED | proof.md, Step 1 |
| R2 (Lemma L): a_j >= 0, D = sum a_j <= pi/2 => sum sin(a_j) cos(D - a_j) <= sin D | PROVED | proof.md, Step 2 |
| R3 (Key Lemma): T < pi/2, p_i = sin(D_i + pi/2 - T) => p_i > 0 and sum_{j!=i} sin(alpha_ij) p_j < p_i | PROVED | proof.md, Step 3 |
| R4 (Lemma W): unit diagonal + positive weights with strict weighted row dominance => trivial kernel | PROVED | proof.md, Step 4 |
| R5: d+1 unit vectors in R^d give c != 0 with G c = 0 | PROVED | proof.md, Step 5 |
| R6 (TARGET): for all d >= 1, any d+1 lines in R^d have S <= (C(d+1,2) - 1) pi/2 | PROVED | proof.md, Step 6 |
| R7: bound attained for every d >= 1 (remark) | PROVED | proof.md, Step 7 |
| Floating-point sampling agrees with R2, R3, R6 (evidence only, not a proof step) | evidence | code/evidence.py |
