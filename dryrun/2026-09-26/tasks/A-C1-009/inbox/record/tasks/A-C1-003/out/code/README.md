# code for A-C1-003 (NOT load-bearing)

`sanity_exact.py`: stdlib only, exact arithmetic (fractions.Fraction); angles in units of pi.

Run: `/usr/bin/time -p python3 sanity_exact.py [D] [NMAX] [D2]` (defaults 48 7 8).

Checks: (1) rho(z) + rho(z - 1/2) = 1/2 on {k/D} (Proof B, Step B1 in coordinates);
(2) cut identity of Proof A, Step A2, for all pairs on {k/D}, measure computed exactly from breakpoints;
(3) max of S over all multisets of N <= NMAX angles from {k/D2} vs floor(N^2/4)/2.
A finite grid check proves nothing beyond the grid; the proofs in ../proof.md do not use it.

Measured run: `python3 sanity_exact.py 48 7 8` -> check1 failures=0 (48 values), check2 failures=0 (2304 pairs),
check3 grid max equals the bound for N = 0..7, ALL OK; real 0.54 s.
