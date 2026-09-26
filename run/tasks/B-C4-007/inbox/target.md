# Target: B-C4 (One Above a Triangular Number, 5 points, written proof)

Definitions (verbatim, run/B/statement.md): partition, shift B (positive numbers among lambda_i - 1, plus one part s),
cyclic (B^i(lambda) = lambda for some i >= 1), d_B(lambda) = min{i >= 0: B^i(lambda) cyclic},
D_B(n) = max over partitions of n of d_B; T_k = k(k+1)/2; rank.

Cell text (verbatim): "The first family just above a triangular number: n = T_{k-1} + 1, that is, n = 11, 16, 22, 29, ...
for k = 5, 6, 7, 8, .... Determine D_B(T_{k-1} + 1) for every k >= 5, with proof of both bounds."

Exact target (exact extremal value; the halves are gated separately):
- A formula F(k) with D_B(T_{k-1} + 1) = F(k) for EVERY k >= 5.
- UPPER: d_B(lambda) <= F(k) for every partition lambda of T_{k-1} + 1, every k >= 5.
- LOWER: an explicit partition lambda^(k) of T_{k-1} + 1 (a function of k) with d_B(lambda^(k)) = F(k), every k >= 5,
  its orbit tracked symbolically in k.
Hand-in: written proof (LaTeX). Computation only if exhaustive over a finite set the argument reduced the problem to
(code included, < 10 min); tables for finitely many k prove nothing for all k.
