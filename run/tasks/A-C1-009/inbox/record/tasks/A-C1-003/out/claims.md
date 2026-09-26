# Claims: A-C1-003 (literature, Phase 1L)

| claim | status | where proved |
|---|---|---|
| Every line in R^2 is R u(a), u(a) = (cos a, sin a); theta(R u(a), R u(b)) = arccos abs(cos(a-b)) = rho(a-b), rho = dist(., pi Z) | PROVED | out/proof.md Steps 0.1-0.4 |
| rho: attained, in [0, pi/2], pi-periodic, even, = abs(z) on [-pi/2, pi/2], 1-Lipschitz | PROVED | out/proof.md Step 0.3 |
| k(N-k) <= floor(N^2/4) for integers k, N >= 0 | PROVED | out/proof.md Step 0.5 |
| If theta(l,l') = pi/2 then theta(l,m) + theta(l',m) = pi/2 for every line m | PROVED (idea: FVZ 2016 Sec. 2, stated without proof there) | out/proof.md Step B1 |
| Removing a perpendicular pair: S = (N-1) pi/2 + S(rest) | PROVED | out/proof.md Step B2 |
| Maximum M(N) of S over N lines exists | PROVED | out/proof.md Step B3 |
| A maximiser with no perpendicular pair has no coincident lines and balanced sides at each line | PROVED | out/proof.md Step B4 |
| For N >= 2 some maximiser has a perpendicular pair | PROVED (idea: FVZ rotation argument) | out/proof.md Step B5 |
| TARGET via Proof B: S <= (pi/2) floor(N^2/4), all N >= 0, repetitions allowed | PROVED | out/proof.md Steps B6-B7 |
| Cut identity int_0^pi abs(chi(a-t) - chi(b-t)) dt = 2 rho(a-b) (quarter-turn cuts) | PROVED (technique: Bilyk-Matzke 2018 Sec. 4.3, quadrant identity) | out/proof.md Step A2 |
| TARGET via Proof A | PROVED | out/proof.md Steps A1-A4 |
| Bound attained by floor(N/2), ceil(N/2) copies of two perpendicular lines | PROVED (not required) | out/proof.md Remark |
| Exact sanity check of B1 and A2 on grid D=48 and of the target on grid D2=8, N<=7 | COMPUTER-VERIFIED (code public: y, out/code/sanity_exact.py), non-load-bearing, proves nothing beyond the grid | out/code/README.md |
| Planar case appears in the literature as FVZ 2016 Theorem 2.1 (with proof) and Bilyk-Matzke 2018 Sec. 4 (alternative proofs) | PROVED in those sources (citation only, not used as proof) | out/sources.md |
