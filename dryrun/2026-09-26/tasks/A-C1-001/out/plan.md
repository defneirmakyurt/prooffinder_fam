# Plan: A-C1-001 (Lines in the Plane), BLIND, Phase 1

Target: for every integer N >= 0 and all lines l_1, ..., l_N through the origin of R^2
(repetitions allowed), S(l_1,...,l_N) = sum_{i<j} theta(l_i,l_j) <= (pi/2) floor(N^2/4),
theta(l,l') = arccos|<x,x'>| for unit vectors x, x' spanning l, l'.

Idea: represent each line by a direction angle a in [0, pi); theta becomes the distance
rho(a-b) of a-b to pi*Z. Write rho as an average over t of a "cut" indicator
(one open quarter-arc of the circle R/piZ, centred at t), then count cut pairs.

## Ladder

- R1 (parametrisation) Every line through 0 in R^2 is spanned by u(a) = (cos a, sin a) for some
  a in [0, pi); theta(l,l') does not depend on the choice of spanning unit vectors.
  Deps: none. Status: PROVED (proof.md Steps 1-2).
- R2 (angle formula) For real a, b: arccos|cos(a-b)| = rho(a-b), where rho(z) = min_{k in Z}|z - k pi|.
  Also rho is pi-periodic, even, and rho(z) = |z| for |z| <= pi/2.
  Deps: none. Status: PROVED (proof.md Steps 3-4).
- R3 (cut identity) With g(z) = 1[rho(z) < pi/4]: for all real x, y,
  int_0^pi |g(t-x) - g(t-y)| dt = 2 rho(x-y).
  Deps: R2. Status: PROVED (proof.md Steps 5-8). Exact sanity check (non-load-bearing): CHECKED on a
  rational grid, out/code/check_cut_identity.py.
- R4 (counting) For integers 0 <= k <= N: k(N-k) <= floor(N^2/4).
  Deps: none. Status: PROVED (proof.md Step 9).
- R5 (pair count) For each t, with k(t) = #{i : g(t-a_i) = 1}:
  sum_{i<j} |g(t-a_i) - g(t-a_j)| = k(t)(N-k(t)).
  Deps: none. Status: PROVED (proof.md Step 10).
- R6 (target) S <= (pi/2) floor(N^2/4), all N >= 0 (N = 0, 1 give empty sums).
  Deps: R1, R2, R3, R4, R5. Status: PROVED (proof.md Step 11-12).
- R7 (sharpness, not required) equality for the balanced two-perpendicular-directions configuration.
  Deps: R1, R2. Status: PROVED (proof.md Step 13).

## Checklist-G pass
G1 full statement, all N >= 0, repetitions allowed: yes. G2 no forbidden phrases (grep-checked). G3 N=0,1,
repeated lines, theta=0 and theta=pi/2 in Step 7: handled. G4 n/a. G5 sharpness construction for every N.
G6 no citations. G7 no load-bearing computation; sanity script exact. G8 only textbook tools
(polar coordinates, cosine subtraction formula, Riemann integral). G9 status stated in proof.md.
