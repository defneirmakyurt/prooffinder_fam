# Claims: A-C1-002

| claim | status | where proved (file, step) |
|---|---|---|
| dist(t, cZ) exists, is attained, is <= c/2; symmetric, c-periodic, dist(2t,2cZ) = 2 dist(t,cZ) | PROVED | out/proof.md, Step 0 |
| theta(l_i, l_j) = dist(a_i - a_j, pi Z) for l_i spanned by (cos a_i, sin a_i) | PROVED | out/proof.md, Steps 1-3 |
| theta(l_i, l_j) = (1/2) delta(u_i - u_j), u_i = 2 a_i, delta = dist(., 2 pi Z) | PROVED | out/proof.md, Step 4 |
| g (half-period indicator) is 2pi-periodic step function; all integrands Riemann integrable | PROVED | out/proof.md, Step 5 |
| integral of a 2pi-periodic function over any period interval is the same | PROVED | out/proof.md, Step 6 |
| int_0^{2pi} abs(g(u-psi) - g(v-psi)) dpsi = D(v-u) | PROVED | out/proof.md, Step 7 |
| D is even and 2pi-periodic | PROVED | out/proof.md, Step 8 |
| D(s) = 2s for s in [0, pi] | PROVED | out/proof.md, Step 9 |
| int_0^{2pi} abs(g(u-psi) - g(v-psi)) dpsi = 2 delta(u - v) for all real u, v | PROVED | out/proof.md, Step 10 |
| sum_{i<j} abs(g(u_i-psi) - g(u_j-psi)) = k(N-k) | PROVED | out/proof.md, Step 11 |
| k(N-k) <= floor(N^2/4) for integers 0 <= k <= N | PROVED | out/proof.md, Step 12 |
| TARGET: S(l_1..l_N) <= (pi/2) floor(N^2/4) for all N >= 0, all lines in R^2, repetitions allowed | PROVED | out/proof.md, Step 13 |
| Bound attained by floor(N/2), ceil(N/2) copies of two perpendicular lines (remark) | PROVED | out/proof.md, Step 14 |
| Floating-point spot-check of bound and of identity (10.1) (not load-bearing) | n/a (sanity only) | out/code/sanity_check.py |
