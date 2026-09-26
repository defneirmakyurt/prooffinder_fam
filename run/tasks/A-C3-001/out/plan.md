# Plan: A-C3-001 (BLIND, Phase 1)

TARGET: for every integer d >= 1 and all lines l_1..l_{d+1} through the origin of R^d (repetitions allowed),
S = sum_{i<j} theta(l_i,l_j) <= (C(d+1,2) - 1) pi/2.

Idea: pass to the "defect" F = sum_{i<j} arcsin|<x_i,x_j>| (= C(d+1,2) pi/2 - S); show F >= pi/2.
Take a global minimiser of F that has the maximum number of orthogonal pairs. Along a great circle
that keeps a vector orthogonal to the vectors it is already orthogonal to, the function
"sum of arcsin|<y,x_j>|" is concave between consecutive new orthogonalities, so a minimiser can be
slid (F constant) until it gains a new orthogonal pair. Hence in the extremal minimiser each vector is
either orthogonal to all others (induction on d) or orthogonal to >= d-1 others (Gram matrix is a
matching; singularity forces a pair with |<x_i,x_j>| = 1).

A-C1 and A-C2 are NOT used.

## Ladder

- R1 PROVED (proof.md Step 1) — Reformulation: S = C(n,2) pi/2 - F(x), F(x) = sum_{i<j} arcsin|<x_i,x_j>|,
  x_i any unit spanning vectors; TARGET <=> P(d): F(x) >= pi/2 for all unit x_1..x_{d+1} in R^d.
  Depends: definitions only.
- R2 PROVED (Step 2) — Concavity: for r in [0,1], tau in R, and an interval I on which cos(t - tau) >= 0,
  h(t) = arcsin(r cos(t - tau)) is concave on I. Depends: calculus.
- R3 PROVED (Step 3) — Sinusoid facts: for orthonormal u, v and unit w with a = <u,w> != 0,
  f(t) = <cos t u + sin t v, w> = a cos t + b sin t vanishes somewhere in (0,pi) and in (-pi,0);
  on an interval where f has no sign change, |f(t)| = r cos(t - tau) with r in (0,1], cos(t-tau) >= 0.
  Depends: Bessel, IVT.
- R4 PROVED (Step 4) — Sliding lemma: if x minimises F, O_i != [n]\{i} and dim L_i >= 2
  (L_i = {y : <y,x_j> = 0 for all j in O_i}), then some minimiser has strictly more orthogonal pairs.
  Depends: R2, R3.
- R5 PROVED (Step 5) — Matching lemma: if n = d+1 unit vectors in R^d each have at most one
  non-orthogonal partner, then some pair has |<x_i,x_j>| = 1, so F >= pi/2. Depends: rank of Gram matrix.
- R6 PROVED (Step 6) — Base case P(1). Depends: R1 definitions.
- R7 PROVED (Step 7) — Induction step P(d-1) => P(d) for d >= 2. Depends: R4, R5, compactness.
- R8 PROVED (Step 8) — TARGET for all d >= 1. Depends: R1, R6, R7.

## Checks (evidence only, not proof steps)
- out/code/sanity.py: stdlib float checks of the h'' formula (finite differences), of F >= pi/2 on
  random and locally-optimised configurations for d = 1..6. Evidence only.
