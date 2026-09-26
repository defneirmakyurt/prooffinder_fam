# Plan: A-C3-002 (BLIND, Phase 1)

TARGET: for every integer d >= 1 and all lines l_1..l_{d+1} through the origin of R^d
(repetitions allowed), S = sum_{i<j} theta(l_i,l_j) <= (C(d+1,2) - 1) pi/2.

Idea: put alpha_ij = pi/2 - theta_ij = arcsin|<x_i,x_j>|. The target is equivalent to
T := sum_{i<j} alpha_ij >= pi/2. If T < pi/2, a weighted diagonal-dominance argument shows the
Gram matrix of the d+1 vectors is nonsingular, contradicting linear dependence in R^d.
Assumptions A-C1, A-C2 are NOT used.

## Ladder

- R1 (reformulation). With alpha_ij := arcsin|<x_i,x_j>| in [0,pi/2], theta_ij = pi/2 - alpha_ij,
  so S = C(n,2) pi/2 - T for n lines; for n = d+1 the target is equivalent to T >= pi/2.
  Deps: none. Status: PROVED (proof.md Step 1).
- R2 (Lemma L). For k >= 0, a_1..a_k >= 0 with D = sum a_j <= pi/2:
  sum_j sin(a_j) cos(D - a_j) <= sin D.
  Deps: none. Status: PROVED (proof.md Step 2).
- R3 (Key Lemma). n >= 2, alpha_ij = alpha_ji >= 0 (i != j), T = sum_{i<j} alpha_ij < pi/2,
  s = pi/2 - T, D_i = sum_{j != i} alpha_ij, p_i = sin(D_i + s). Then p_i > 0 and
  sum_{j != i} sin(alpha_ij) p_j < p_i for every i.
  Deps: R2. Status: PROVED (proof.md Step 3).
- R4 (weighted diagonal dominance). If G is n x n real, G_ii = 1, and there is p > 0 with
  sum_{j != i} |G_ij| p_j < p_i for all i, then Gc = 0 implies c = 0.
  Deps: none. Status: PROVED (proof.md Step 4).
- R5 (linear dependence gives a kernel vector of the Gram matrix). d+1 unit vectors in R^d:
  there is c != 0 with G c = 0, G_ij = <x_i,x_j>.
  Deps: none. Status: PROVED (proof.md Step 5).
- R6 (TARGET). Combine: if T < pi/2 then R3 + R4 contradict R5; so T >= pi/2, so by R1
  S <= (C(d+1,2) - 1) pi/2. Includes d = 1 and all repetition / degenerate configurations.
  Deps: R1, R3, R4, R5. Status: PROVED (proof.md Step 6).
- R7 (sharpness, remark only). Equality is attained (coordinate axes with one repeated);
  not needed for the target. Status: PROVED (proof.md Step 7).
