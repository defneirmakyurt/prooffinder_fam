# Plan: A-C4-001 (prover, BLIND, phase 1)

TARGET: (a) any 5 lines in R^3 have S <= 4pi; (b) any 6 lines in R^4 have S <= 13pi/2.
Throughout N = d+2, a_ij := arcsin|<x_i,x_j>| = pi/2 - theta_ij, D := sum_{i<j} a_ij.
Since S = C(N,2) pi/2 - D, the target is: D >= pi.

Ladder (status as of end of run):

- R1 PROVED. (Convexity along a great circle.) For unit x and a great circle gamma(s) = cos s u + sin s w,
  s -> theta(gamma(s), x) is convex on every interval on which <gamma(s),x> has no zero.
  Deps: none.
- R2 PROVED. (Vertex lemma / choice of maximiser.) For every N, d there is a global maximiser of S such that
  every line x_l is either orthogonal to all other lines, or the lines orthogonal to it have rank d-1.
  Deps: R1, compactness.
- R3 PROVED. (Degree bound.) In such a maximiser with N = d+2 the non-orthogonality graph H has max degree <= 2,
  so each component is an isolated vertex, a path or a cycle. Deps: R2, elementary graph fact (proved inline).
- R4 PROVED. (Rank of a path.) If x_1..x_p (p >= 2) have <x_i,x_{i+1}> != 0 and <x_i,x_j> = 0 for |i-j| >= 2,
  then rank >= p-1. Deps: none.
- R5 PROVED. (Component bookkeeping.) With k_a = |V_a| - dim span V_a: k_a >= 0, sum k_a >= 2,
  D = sum_a D(V_a); a component with k_a >= 1 has D(V_a) >= pi/2 (uses A-C3); a component with k_a >= 2 is a cycle.
  Deps: R3, R4, A-C3.
- R6 PROVED. (Analytic core.) Phi(p,q) > 0 on (0,pi/2)^2, where
  Phi = arcsin(sin p cos q) + arcsin(cos p cos q / W) + arcsin(sin p sin q / W) - p + q - pi/2, W = sqrt(1 - sin^2 p cos^2 q).
  (Equivalent to: in a spherical right triangle, leg+leg-hypotenuse > excess.) Deps: exact polynomial identity (checked by
  hand and by out/code/check_identities.py).
- R7 PROVED. (Normal form of a Hamiltonian cycle.) If x_1..x_m (m = d+2) span R^d, <x_i,x_{i+1}> != 0 (cyclically) and
  <x_i,x_j> = 0 for cyclically non-adjacent i,j, then x_1..x_{m-2} are independent and, in the Gram-Schmidt frame,
  the configuration is given by angles sigma_2..sigma_{m-2} in (0,pi/2). Deps: none.
- R8 PROVED. (5-cycle lemma.) m = 5, d = 3: D = pi + Phi(sigma_2, sigma_3) > pi. Deps: R6, R7.
- R9 PROVED. (6-cycle lemma.) m = 6, d = 4: D >= pi + Phi(sigma_3, sigma_4) + Phi(sigma_2, A') > pi. Deps: R6, R7, R8 formulas.
- R10 PROVED. (Target (a).) Deps: R2-R5, R8, A-C1, A-C3.
- R11 PROVED. (Target (b).) Deps: R2-R5, R9, R10 (for 5 lines in a 3-dim subspace), A-C1, A-C3.

Assumptions used: A-C1 (only N = 4), A-C3 (d' = 1, 2, 3). A-C2 is NOT used.
