| claim | status | where proved (file, step) |
|---|---|---|
| Every line through 0 in R^2 is spanned by u(a)=(cos a, sin a), a in [0,pi) | PROVED | proof.md, Step 1 |
| theta well defined; <u(a),u(b)> = cos(a-b) | PROVED | proof.md, Step 2 |
| rho(z)=min_k abs(z-k pi) exists, in [0,pi/2], pi-periodic, even, =abs(z) on [-pi/2,pi/2], =z+pi on [-pi,-pi/2] | PROVED | proof.md, Step 3 |
| arccos abs(cos(a-b)) = rho(a-b), so theta(l_a,l_b)=rho(a-b) | PROVED | proof.md, Step 4 |
| g = 1[rho < pi/4] is pi-periodic, even, a step function; g=1 on [-pi/2,pi/2] iff abs(z)<pi/4 | PROVED | proof.md, Step 5 |
| Integral of a pi-periodic function over any period equals int_0^pi; int_0^pi g = pi/2 | PROVED | proof.md, Step 6 |
| Overlap: int_{-pi/2}^{pi/2} g(s)g(s-theta) ds = pi/2 - theta for theta in [0,pi/2] | PROVED | proof.md, Step 7 |
| Cut identity: int_0^pi abs(g(t-x)-g(t-y)) dt = 2 rho(x-y) | PROVED (also exact sanity check on rational grids D=48, D=45: CHECKED, non-load-bearing) | proof.md, Step 8; out/code/check_cut_identity.py |
| k(N-k) <= floor(N^2/4) for integers k, N>=0 | PROVED | proof.md, Step 9 |
| sum_{i<j} abs(g(t-a_i)-g(t-a_j)) = k(t)(N-k(t)) | PROVED | proof.md, Step 10 |
| TARGET: S(l_1..l_N) <= (pi/2) floor(N^2/4), all N>=0, repetitions allowed | PROVED | proof.md, Steps 11-12 |
| Sharpness: balanced two perpendicular directions attain the bound | PROVED (not required) | proof.md, Step 13 |
