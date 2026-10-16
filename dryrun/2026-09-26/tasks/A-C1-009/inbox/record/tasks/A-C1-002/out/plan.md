# Plan: A-C1-002 (Lines in the Plane), BLIND

Target: for every N >= 0 (the case N >= 1 is the one intended; N = 0 is the empty case) and all lines
l_1, ..., l_N through the origin of R^2 (repetitions allowed),
S(l_1, ..., l_N) = sum_{i<j} theta(l_i, l_j) <= (pi/2) floor(N^2/4).

Idea: double the direction angles, so that theta becomes half the arc distance on the circle; write the
arc distance as an average over half-open semicircles of "exactly one of the two points lies in the
semicircle" (a Crofton-type identity); for each semicircle the number of separated pairs is k(N-k).

## Ladder

- R1 (angle formula). If x = (cos a, sin a), x' = (cos b, sin b), then theta = arccos|cos(a-b)| = dist(a-b, pi Z).
  Depends on: nothing. STATUS: PROVED (proof.md Steps 0-3).
- R2 (doubling). dist(2s, 2 pi Z) = 2 dist(s, pi Z); hence theta(l_i, l_j) = (1/2) delta(u_i - u_j), where
  u_i = 2 a_i and delta(t) = dist(t, 2 pi Z) in [0, pi].
  Depends on: R1. STATUS: PROVED (Step 4).
- R3 (semicircle indicator). g(x) = 1 if x - 2 pi floor(x/(2 pi)) in [0, pi), else 0. g is 2pi-periodic,
  a step function on bounded intervals.
  Depends on: nothing. STATUS: PROVED (Step 5).
- R4 (Crofton-type identity). For all real u, v:
  integral_0^{2 pi} |g(u - psi) - g(v - psi)| d psi = 2 delta(u - v).
  Depends on: R3. STATUS: PROVED (Steps 6-10).
- R5 (counting). For each psi, sum_{i<j} |g(u_i - psi) - g(u_j - psi)| = k(N - k), with k = #{i : g(u_i - psi) = 1}.
  Depends on: R3. STATUS: PROVED (Step 11).
- R6 (integer bound). For integers 0 <= k <= N: k(N-k) <= floor(N^2/4).
  Depends on: nothing. STATUS: PROVED (Step 12).
- R7 (target). S <= (pi/2) floor(N^2/4).
  Depends on: R2, R4, R5, R6. STATUS: PROVED (Step 13).
- R8 (sharpness, not required). Equality for floor(N/2), ceil(N/2) copies of two perpendicular lines.
  Depends on: R1. STATUS: PROVED (Step 14, remark only).

Optional sanity check (not load-bearing): out/code/sanity_check.py, floating point, random configurations.
