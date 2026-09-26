# Plan (A-C2-011, BRANCH ANALYSIS, BLIND)

Notation: c_i = <x_i, x_{i+1}>, alpha_i = arcsin|c_i| in [0, pi/2], B_0 = 0, B_j = alpha_1 + ... + alpha_j.

- R1 PROVED — theta_i = pi/2 - alpha_i; so target <=> sum_{i=1}^{m-1} alpha_i >= pi/2. (uses: arccos y + arcsin y = pi/2)
- R2 PROVED — Two-term weighted AM-GM: a, b >= 0, ab >= c^2 => 2|c||ts| <= a t^2 + b s^2.
- R3 PROVED — Angle inequality: 0 <= u <= v <= pi/2 => cos u sin v >= sin(v-u) (so cos^2 u * sin^2 v >= sin^2(v-u)).
- R4 PROVED — Key lemma: if B_{k-1} <= pi/2 then ||sum_{i<=k} t_i x_i||^2 >= cos^2(B_{k-1}) t_k^2 for all real t. (uses R2, R3, orthogonality hypothesis)
- R5 PROVED — If B_{m-1} < pi/2 then x_1..x_m are linearly independent. (uses R4, backward induction)
- R6 PROVED — Target: dim R^{m-1} forbids R5's conclusion, so B_{m-1} >= pi/2; conclude via R1. (uses R1, R5)

Sanity (not load-bearing): out/tmp/sanity.py float test of R4 on random chains, m in 2..8.
