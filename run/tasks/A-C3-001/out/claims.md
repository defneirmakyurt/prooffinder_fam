# Claims: A-C3-001

| claim | status | where proved (file, step) |
|---|---|---|
| R1: S = C(n,2) pi/2 - F(x); TARGET for d <=> P(d): F >= pi/2 for all unit x_1..x_{d+1} in R^d | PROVED | proof.md, Step 1 |
| R2: arcsin(r cos(t - tau)) is concave on any interval where cos(t - tau) >= 0, for r in [0,1] | PROVED | proof.md, Step 2 (Lemma 2) |
| R3: along y(t) = cos t u + sin t v, f(t) = <y(t),w> has zeros in (0,pi) and (-pi,0) when <u,w> != 0; arcsin|f| concave on sign-constant intervals | PROVED | proof.md, Step 3 (Lemma 3) |
| R4: a minimiser with some i, O_i != all others and dim L_i >= 2, can be slid to a minimiser with more orthogonal pairs | PROVED | proof.md, Step 4 (Lemma 4) |
| R5: d+1 unit vectors in R^d, each non-orthogonal to at most one other => some |<x_i,x_j>| = 1 => F >= pi/2 | PROVED | proof.md, Step 5 (Lemma 5) |
| R6: P(1) | PROVED | proof.md, Step 6 |
| R7: P(d-1) => P(d), d >= 2 | PROVED | proof.md, Step 7 |
| R8: TARGET for every d >= 1 | PROVED | proof.md, Step 8 |
| h'' formula, F >= pi/2 on random / locally optimised configs (d = 1..6), concavity along great circles | evidence only (float), not a proof step | out/code/sanity.py |
