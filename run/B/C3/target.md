# Target: B-C3 (A General Upper Bound, 3 points, written proof)

Definitions (verbatim, run/B/statement.md): a partition of n >= 1 is a weakly decreasing sequence of positive
integers with sum n (s piles). B(lambda): the positive numbers among lambda_1 - 1, ..., lambda_s - 1, together with
one extra part equal to s. lambda is cyclic if B^i(lambda) = lambda for some i >= 1.
d_B(lambda) = min{ i >= 0 : B^i(lambda) cyclic }, D_B(n) = max{ d_B(lambda) : lambda a partition of n }.
T_k = k(k+1)/2, delta_k = (k, ..., 1); rank of n = the unique k with T_{k-1} < n <= T_k.

Cell text (verbatim): "Now the numbers strictly between two consecutive triangular numbers.
(a) Prove that for every k >= 4 and every non-triangular n with T_{k-1} < n < T_k, D_B(n) <= k^2 - 2k - 1.
(b) Determine D_B(T_k - 1) exactly.
(c) Determine also, for that n, which partitions attain the maximum."

Exact targets:
(a) For every k >= 4, every n with T_{k-1} < n < T_k, and every partition lambda of n: d_B(lambda) <= k^2 - 2k - 1.
(b) A formula F(k) with D_B(T_k - 1) = F(k); state explicitly the k-range proved (the cell states none; cover as
    many k >= 1 as possible and give any small-k values separately). Both halves: upper bound over every partition
    of T_k - 1, and an explicit partition (function of k) attaining F(k), each proved for every k in the range.
(c) The exact set of partitions lambda of T_k - 1 with d_B(lambda) = D_B(T_k - 1), as explicit functions of k,
    with proof that every listed partition attains the maximum and that no other partition does.

Hand-in: a written proof (LaTeX). Computation only if exhaustive over a finite set the argument has reduced the
problem to (code included, < 10 min); small-k tables alone prove nothing for all k.
