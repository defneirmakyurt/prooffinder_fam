# Task 3: local analysis

Reformulated: minimise F(a) = sum arcsin a_i over the admissible set {a in [0,1]^(m-1): I - A(a) is PSD and singular}
(A(a) = weighted path adjacency; signs of <x_i,x_{i+1}> can be made nonnegative by x_i -> -x_i, and admissible chains in R^(m-1)
are exactly those whose unit-diagonal tridiagonal Gram matrix is PSD with rank <= m-1). Target <=> min F >= pi/2.

Minimisers (F = pi/2): (i) a single a_j = 1, others 0; (ii) a_j^2 + a_{j+1}^2 = 1, others 0 (includes (i)).

Is the optimum strict? NO. At m = 3, F is identically pi/2 on the whole singular curve a1^2+a2^2 = 1 — a flat direction to all
orders. So the conjectured optimum is a non-strict (degenerate) minimum. This does not threaten the target: step 10 of out/proof.md
shows min F >= pi/2 globally.

Transverse perturbation (m = 4, base point a = (c, s, 0), c^2+s^2 = 1, c,s in (0,1)): set a_3 = eps > 0. det(I - A) =
1 - a1^2 - a2^2 - a3^2 + a1^2 a3^2 = 0 forces a1^2 + a2^2 = 1 - eps^2 a2^2 (keeping the ratio a1:a2 fixed, radius r = 1 - eps^2 s^2/2 + O(eps^4)).
Then arcsin a1 + arcsin a2 = pi/2 - eps^2 s^2/2 * (c/s + s/c) + O(eps^4) = pi/2 - eps^2 s/(2c) + O(eps^4), while arcsin a3 = eps + O(eps^3).
Net F - pi/2 = eps - eps^2 s/(2c) + O(eps^3) > 0 for small eps: first-order strict increase transversally. Consistent with R1.
Numerically (out/cex_search/log.txt) every local-search run (m = 3..10, 200 restarts each) converged to minimisers of type (i)/(ii);
the reported -2.1e-8 is floating-point rounding of arcsin(1 - 2e-16) (square-root sensitivity), not a violation.
Evidence only for this file; the global statement rests on out/proof.md.
