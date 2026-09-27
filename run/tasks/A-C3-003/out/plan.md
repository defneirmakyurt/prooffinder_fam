# Plan: A-C3-003 (BLIND, Phase 1)

TARGET: for every integer d >= 1 and all lines l_1,...,l_{d+1} through the origin of R^d
(repetitions allowed), S = sum_{i<j} theta(l_i,l_j) <= (C(d+1,2) - 1) pi/2.

Notation: x_i a unit vector spanning l_i, g_ij = <x_i,x_j>, theta_ij = arccos|g_ij|,
phi_ij = pi/2 - theta_ij in [0, pi/2], so sin(phi_ij) = |g_ij|.  T = sum_{i<j} phi_ij.
Target  <=>  T >= pi/2  (since S = C(d+1,2) pi/2 - T).

## Ladder

R1  Well-definedness and reformulation: theta_ij does not depend on the choice of spanning
    unit vectors; phi_ij in [0,pi/2], sin(phi_ij) = |g_ij|; S <= (C(d+1,2)-1)pi/2  <=>  T >= pi/2.
    deps: none.                                                     STATUS: PROVED (proof.md Step 1)

R2  Trig lemma: k >= 1, a_1..a_k >= 0, D = sum a_j <= pi/2  ==>
    sum_j sin(a_j) cos(D - a_j) <= sin(D).
    deps: none (induction on k, addition formula).                  STATUS: PROVED (proof.md Step 2)

R3  Positive certificate: n >= 2, symmetric phi_ij in [0,pi/2] (i != j), T = sum_{i<j} phi_ij < pi/2,
    D_i = sum_{j != i} phi_ij, u_i = cos(T - D_i).  Then u_i > 0 and
    sum_{j != i} sin(phi_ij) u_j < u_i for every i.
    deps: R2.                                                       STATUS: PROVED (proof.md Step 3)

R4  Positive-vector criterion: A symmetric, entries >= 0, zero diagonal; u > 0 with (Au)_i < u_i
    for all i  ==>  y^T A y < y^T y for every nonzero real y.
    deps: none (AM-GM).                                             STATUS: PROVED (proof.md Step 4)

R5  Matrix lemma: with phi as in R3 (T < pi/2) and A_ij = sin(phi_ij) (i != j), A_ii = 0:
    y^T A y < y^T y for every nonzero y.
    deps: R3, R4.                                                   STATUS: PROVED (proof.md Step 5)

R6  Dependence: d+1 vectors in R^d are linearly dependent, so there is c != 0 in R^{d+1}
    with c^T G c = |sum c_i x_i|^2 = 0, G the Gram matrix.
    deps: none (dimension count).                                   STATUS: PROVED (proof.md Step 6)

R7  TARGET.  If T < pi/2, then c^T G c >= |c|^2 - |c|^T A |c| > 0 (R5 applied to |c|),
    contradicting R6.  Hence T >= pi/2, i.e. S <= (C(d+1,2)-1) pi/2, for every d >= 1,
    with coincident lines / lower-dimensional span allowed; d = 1 included.
    deps: R1, R5, R6.                                               STATUS: PROVED (proof.md Steps 7-8)

## Evidence (not proof steps)
E1  floating-point random tests of R2, R3, R5 and of the target for d = 1..8 (out/code/evidence.py).
