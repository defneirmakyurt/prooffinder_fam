# code for A-C1-001

The proof in ../proof.md does NOT rest on any computation. This script is an exact
(fractions.Fraction, stdlib only) sanity check.

Run:
    /usr/bin/time -p python3 check_cut_identity.py [D] [NMAX] [D2]
defaults D=48, NMAX=7, D2=8. Angles are in units of pi.

Checks:
1. Cut identity (proof.md Step 8): for all x, y in {k/D : 0<=k<D},
   measure{t in [0,1): g(t-x) != g(t-y)} == 2 rho(x-y), computed exactly by breakpoints.
2. Target on a grid (proof.md Step 11): for every multiset of N <= NMAX angles from {k/D2},
   S <= floor(N^2/4)/2 (units of pi); prints the grid maximum.

Runs recorded:
- `python3 check_cut_identity.py 48 7 8`: check1 failures=0 (2304 pairs); check2 max = bound for N=0..7; ALL OK; real 0.41 s.
- `python3 check_cut_identity.py 45 6 9`: check1 failures=0 (2025 pairs); check2 no violation for N=0..6 (max < bound for even N since the grid lacks perpendicular pairs); ALL OK; real 0.26 s.
