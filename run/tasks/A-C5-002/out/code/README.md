# Code — A-C5-002

None of these scripts are load-bearing for the d=2 proof in `out/proof.md` (Part IV, Steps
16-21), which is a self-contained symbolic/elementary derivation. They are included as exact
illustrative cross-checks of specific algebraic claims made along the way, as required by the
brief whenever a numeric/symbolic statement is asserted.

- `approach_A_check.py` — evaluates (with mpmath, 50 decimal digits, i.e. error < 1e-45) the
  Jensen-type lower bound of proof.md Step 6 at d=2, N=4, and confirms it is ~2.039 < pi
  (needed: >= pi), substantiating the "Approach A is too weak" claim of Step 7.
  Run: `/home/user/bainsahackathon/.venv/bin/python3 approach_A_check.py` (~0.06s).

- `approach_B_check.py` — verifies symbolically (sympy, exact rational/pi arithmetic, no
  floating point) the Veronese-embedding formula cos(ang_P)=(d cos^2(theta)-1)/(d-1) of proof.md
  Step 10, the exact value ang_P=2*pi/3 < pi=2*theta at d=3,theta=pi/2 (Step 12), and the exact
  rational inequality 2d/(d-1) < 4 for several d>=3 (Step 13).
  Run: `/home/user/bainsahackathon/.venv/bin/python3 approach_B_check.py` (~0.7s).

- `approach_d2_check.py` — verifies symbolically (sympy, exact) the identity
  ang(y,y')=2*theta of proof.md Step 17 at 8 sample angles (both branches Delta<=pi/2 and
  Delta>pi/2), and the separation-probability claim of Step 18 at beta=pi/2 and beta=pi/3 by
  exact interval-membership tests (no floating point).
  Run: `/home/user/bainsahackathon/.venv/bin/python3 approach_d2_check.py` (~0.6s).

All three scripts together run in well under 10 minutes (total ~1.4s measured).
