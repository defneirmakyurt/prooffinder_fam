# Claims: A-C4-003

| claim | status | where proved (file, step) |
|---|---|---|
| (a) any 5 lines in R^3 satisfy S <= 4pi | PROVED | proof.md, Steps 0-9 (9.3) |
| (b) any 6 lines in R^4 satisfy S <= 13pi/2 | PROVED | proof.md, Steps 0-9 (9.3) |
| Reformulation: target iff D = sum_{i<j} arcsin\|<x_i,x_j>\| >= pi for N = d+2, d in {3,4} | PROVED | proof.md, Step 0 |
| R1: S attains its max; a maximizer with the most orthogonal pairs exists | PROVED | proof.md, Step 1 |
| R2 (Lemma T): arcsin(alpha cos s + beta sin s) concave where the argument is >= 0 (amplitude <= 1) | PROVED | proof.md, Step 2 |
| R3 (Lemma A): at that maximizer each x_k is orthogonal to all others, or its orthogonal partners span x_k^perp | PROVED | proof.md, Step 3 |
| R4: non-orthogonality graph G' has max degree <= N-d = 2; components are vertices, paths, cycles | PROVED | proof.md, Step 4 |
| R5a: dim U_K <= m_K - deg(k) for any non-isolated vertex k of component K | PROVED | proof.md, 5.1 |
| R5b: tridiagonal Gram with nonzero off-diagonal has rank >= m-1 | PROVED | proof.md, 5.2 |
| R5c: components are isolated vertices, coincident pairs, or cycles with dim U_K = m-2, m <= d+2 | PROVED | proof.md, 5.3 |
| R6: 3-cycle (dim 1) has D = 3pi/2; 4-cycle (dim 2) has D = pi | PROVED | proof.md, Step 6 |
| R7: 5-cycle spanning a 3-space has sum of consecutive arcsin\|.\| >= pi | PROVED | proof.md, Step 7 |
| R8: 6-cycle spanning a 4-space has sum of consecutive arcsin\|.\| >= pi | PROVED | proof.md, Step 8 |
| R9: assembly D >= sum_K e_K pi/2 >= (N-d) pi/2 = pi | PROVED | proof.md, Step 9 |
| Sharpness: e1,e1,e2,e2,e3 and e1,e1,e2,e2,e3,e4 attain the bounds | PROVED | proof.md, 10.2 |
| Floating-point sanity: formulas of Steps 7-8 match sampled cycles; hill-climbing never exceeds bounds | CHECKED (evidence only, not load-bearing) | code/check_cycles.py, code/random_search.py |
| Symbolic re-check of hand identities in Steps 2, 7 | CHECKED (support only; hand derivations are in proof.md) | code/check_identities.py |
