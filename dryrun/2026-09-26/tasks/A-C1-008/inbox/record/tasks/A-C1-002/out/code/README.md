# Code for A-C1-002

`sanity_check.py` (stdlib only, floating point). **Not load-bearing**: the proof in `out/proof.md` does not rest on it.

Run:

    /usr/bin/time -p python3 sanity_check.py

What it checks (numerically, with float tolerance 1e-9):
1. S <= (pi/2) floor(N^2/4) on 2000 random configurations for each N = 1..12 (angles uniform in [0, pi)),
   with theta computed straight from the definition arccos|<x, x'>|.
2. Random-perturbation hill climbing for N = 2..9 approaches but does not exceed the bound.
3. The identity int_0^{2pi} |g(u-psi) - g(v-psi)| dpsi = 2 delta(u - v) (proof Step 10) for 200 random (u, v),
   via a midpoint Riemann sum with 20000 nodes; the error is within the grid resolution (about 2h = 6.3e-4).

Measured: COMPLETED, real 3.62 s (user 2.43 s) on the author's laptop, seed 12345.
