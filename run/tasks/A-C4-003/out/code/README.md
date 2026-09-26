# Code for A-C4-003

NO PROOF STEP RESTS ON THIS CODE. The proof in ../proof.md is fully analytic. These scripts are
sanity checks (floating point) and a symbolic re-check of identities that proof.md derives by hand.

Python: /Users/defneirmakyurt/bainsahackathon/.venv/bin/python3 (check_identities.py needs sympy;
the other two are stdlib-only).

| script | what it checks | command | measured runtime |
|---|---|---|---|
| check_cycles.py | (1) 200000 random 5-cycles in R^3 (explicit 2-parameter family): sum of consecutive phi equals pi + F(u,v) of Step 7, and min(sum - pi) >= 0; grid min of F on [0,pi/2]x(0,pi/2] (301x300 grid). (2) 100000 random 6-cycles in R^4 (explicit 3-parameter family): the (a,b,s,t) description of Step 8.3 holds, the sign claim of 8.5 holds, and sum phi >= pi. | `/usr/bin/time -p <PY> check_cycles.py` | real 5.57 s |
| check_identities.py | sympy: 4x4 tridiagonal determinant (7.1), psi'' formula (Lemma T), g'' (7.6), (1+cucv)^2 - su^2 sv^2 = (cu+cv)^2, w' and h'' (7.6), cos(phi1+phi2) = w (7.4), consistency of the solved values (7.3). All differences print 0. | `/usr/bin/time -p <PY> check_identities.py` | real 0.57 s |
| random_search.py | random-restart hill climbing (40 restarts x 6000 steps) for max S; best found stays below 4pi (N=5,d=3) and 13pi/2 (N=6,d=4). | `/usr/bin/time -p <PY> random_search.py` | real 2.73 s |

Scratch scans (out/tmp/cyc5.py, out/tmp/cyc6.py) grid-scan the same cycle families; the maxima found
(4.712388980384703 vs 3pi/2 and 6.283185307179587 vs 2pi, differences at rounding level) sit on the
boundary of the families, where the cycles degenerate. Runtimes 1.38 s and 7.94 s.
