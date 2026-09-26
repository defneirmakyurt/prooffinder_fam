# Target: B-C5 (Two Above a Triangular Number, 8 points, written proof)

Definitions (verbatim, run/B/statement.md): partition, shift B, cyclic, d_B, D_B(n), T_k = k(k+1)/2, rank.

Cell text (verbatim): "The next family: n = T_{k-1} + 2, that is, n = 3, 5, 8, 12, 17, 23, ... for k = 2, 3, 4, 5, 6, 7, ....
Determine D_B(T_{k-1} + 2) for every k, with proof of both bounds.
- State exactly for which k your formula holds, and give the remaining values separately.
- Your upper bound must be a single argument valid for all k in that range, not a separate treatment of each k.
- You must give the extremal partitions explicitly as a function of k.
- Say also where the straightforward extension of the Cell 3 argument stops: give the bound it does yield, show it is
  strictly weaker than the truth, and identify precisely what your proof supplies in its place."
(Cell 3(a), verbatim: "Prove that for every k >= 4 and every non-triangular n with T_{k-1} < n < T_k, D_B(n) <= k^2 - 2k - 1.")

Exact targets (for every k >= 2):
(1) A formula F(k) with D_B(T_{k-1}+2) = F(k) on an explicitly stated k-range, and the remaining values (every other
    k >= 2) given separately and proved.
(2) UPPER: one uniform argument giving d_B(lambda) <= F(k) for every partition of T_{k-1}+2, every k in the range.
(3) LOWER: explicit extremal partition(s) lambda^(k) (functions of k) with d_B(lambda^(k)) = F(k), every k in range.
(4) The Cell 3 extension analysis: the bound that the straightforward extension of a Cell 3(a)-type argument yields for
    n = T_{k-1}+2, proof that it is strictly weaker than F(k), and what the proof of (2) supplies in its place.
Hand-in: written proof (LaTeX). Computation only if exhaustive over a finite set the argument reduced the problem to.
