# tested (exploratory, floating point, confirms nothing by itself)
Script: out/cex_search/search.py (stdlib only), log out/cex_search/log.txt, stdout.txt, wall time in runtime.txt (469 s).
Parametrisation: weights w >= 0, scaled by t = 1/lambda_max(A(w)) (bisection on LDL pivots, 200 steps) so I - tA is PSD singular.
- R3 equal weights, m = 2..60: min gap 0 (m = 2, 3; equality), gap grows with m (29.37 at m = 60).
- R4 random, m = 2..12, 20000 instances each (uniform, uniform^6, 40%-sparse), seed 12345: min gap -2.1e-8 at a single a_j = 1 (rounding at the equality point).
- R5 local search (random-perturbation descent, 3000 iters, adaptive step), m = 3..10, 200 restarts each, seed 777: same minimisers, same rounding value.
Worst case: out/worst.json (m = 3, exact equality, margin 0), reproduced exactly by out/reproduce.py.
