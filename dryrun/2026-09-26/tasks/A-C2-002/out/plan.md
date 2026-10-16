# Plan: A-C2 (chain orthogonality lemma)

Notation: c_i = <x_i, x_{i+1}>, a_i = arcsin|c_i| in [0, pi/2], so theta(x_i,x_{i+1}) = pi/2 - a_i.

R1 PROVED — Reformulation: target  <=>  sum_{i=1}^{m-1} a_i >= pi/2.  (uses arccos t + arcsin t = pi/2 on [0,1])
R2 PROVED — Base m = 2: x_1, x_2 unit in R^1, so x_2 = ±x_1, a_1 = pi/2.
R3 PROVED — Degenerate step: if |c_{m-1}| = 1 then a_{m-1} = pi/2 and the sum is >= pi/2.
R4 PROVED — Reduction (m >= 3, |c_{m-1}| < 1): y = (x_{m-1} - c_{m-1} x_m)/cos a_{m-1}; the list
            x_1..x_{m-2}, y is a valid chain of m-1 unit vectors in x_m^perp (dim m-2), with new last
            coefficient |<x_{m-2},y>| = sin a_{m-2} / cos a_{m-1}.
R5 PROVED — Trig lemma: alpha,beta in [0,pi/2], sin(alpha) <= cos(beta), cos beta > 0 =>
            arcsin(sin alpha / cos beta) <= alpha + beta when alpha+beta<pi/2 (and <= pi/2 always).
R6 PROVED — Induction on m (uses R2, R3, R4, R5) gives sum a_i >= pi/2 for all m >= 2.
R7 PROVED — Target (uses R1, R6).
