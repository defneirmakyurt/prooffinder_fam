# Plan: A-C4-003 (prover, BLIND, Phase 1)

TARGET: (a) any 5 lines in R^3 have S <= 4*pi; (b) any 6 lines in R^4 have S <= 13*pi/2.
Notation: phi(x,y) = arcsin|<x,y>| = pi/2 - theta(x,y) (the "deficit" of a pair).
Both claims read: for N = d+2 unit vectors in R^d (d = 3, 4), D := sum_{i<j} phi_ij >= pi,
since C(5,2)*pi/2 - pi = 4*pi and C(6,2)*pi/2 - pi = 13*pi/2.

## Ladder

R1  (existence) S attains its maximum on (S^{d-1})^N; among maximizers pick one, x, with the
    largest number omega(x) of orthogonal pairs.                       deps: none
R2  (one-line concavity) For g(s) = alpha cos s + beta sin s with alpha^2+beta^2 = A^2 <= 1,
    s -> arcsin(g(s)) is concave on every interval on which g >= 0 (A<1), resp. on every
    interval on whose interior g > 0 (A = 1).                           deps: none
R3  (Lemma A, local structure) For the x of R1 and every k: either x_k is orthogonal to all
    other x_j, or the x_j (j != k) orthogonal to x_k span x_k^perp.      deps: R1, R2
R4  (degree bound) For N = d+2, the non-orthogonality graph G' of x has max degree <= 2;
    so every component is a path or a cycle.                             deps: R3
R5  (component inequality) Component K with m vertices spanning U_K: vertex k in K has
    dim U_K <= m - deg(k). Hence: components are isolated vertices, coincident pairs, or
    cycles with dim U_K = m-2; paths with >= 3 vertices do not occur.    deps: R3, R4
R6  (cycles m=3,4) a 3-cycle in dim 1 has D = 3pi/2; a 4-cycle in dim 2 has D = pi.  deps: none
R7  (5-cycle) 5 unit vectors in a 3-dim space, x_i orth x_{i+2} (indices mod 5), all
    consecutive products nonzero: sum of the 5 consecutive phi >= pi.    deps: none
R8  (6-cycle) 6 unit vectors in a 4-dim space, x_i orth x_j for i,j non-adjacent in C_6,
    consecutive products nonzero: sum of the 6 consecutive phi >= pi.    deps: R2
R9  (assembly) D(x) >= sum_K (m_K - dim U_K) pi/2 >= (N - d) pi/2 = pi; so max S <= bound,
    proving (a) and (b).                                                 deps: R1, R4-R8

## Status
R1 PROVED   (proof.md Step 1)
R2 PROVED   (proof.md Step 2)
R3 PROVED   (proof.md Step 3)
R4 PROVED   (proof.md Step 4)
R5 PROVED   (proof.md Step 5)
R6 PROVED   (proof.md Step 6)
R7 PROVED   (proof.md Step 7)
R8 PROVED   (proof.md Step 8)
R9 PROVED   (proof.md Step 9)

Code in out/code/ is sanity checking only (floating point / sympy); no rung rests on it.
