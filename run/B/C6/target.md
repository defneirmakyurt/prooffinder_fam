# Target: B-C6 (D_B(n) for Every n, 13 points, OPEN question, written proof)

Definitions (verbatim, run/B/statement.md): a partition of n >= 1 is a weakly decreasing sequence of positive
integers with sum n (s piles). B(lambda): the positive numbers among lambda_1 - 1, ..., lambda_s - 1, together with
one extra part equal to s. lambda is cyclic if B^i(lambda) = lambda for some i >= 1.
d_B(lambda) = min{ i >= 0 : B^i(lambda) cyclic }, D_B(n) = max{ d_B(lambda) : lambda a partition of n }.
T_k = k(k+1)/2, delta_k = (k, ..., 1); rank of n = the unique k with T_{k-1} < n <= T_k (T_0 = 0).

Cell text (verbatim): "Open question. Finally, the whole function n -> D_B(n). Determine D_B(n) for every n."

Exact target: an explicit formula F(n) (e.g. in terms of the rank k and the position r = n - T_{k-1}, 1 <= r <= k)
with D_B(n) = F(n) for EVERY n >= 1, both halves proved: (upper) d_B(lambda) <= F(n) for every partition lambda of n;
(lower) an explicit partition of n, as a function of the parameters, with d_B = F(n).

PARTIAL PROGRESS COUNTS (the cell is open). Valuable partial results, each with BOTH bounds proved for every
parameter value in an infinite family: D_B(n) exactly on further infinite families (e.g. n = T_{k-1} + j or
n = T_k - j for fixed j, or ranges of r in terms of k); a general upper bound for every n of rank k sharper than
what is known; explicit witness families giving general lower bounds for every n. State exactly which n each
result covers. Small-n tables prove nothing beyond the n computed; a formula checked for finitely many n is CONJECTURED.

Hand-in: a written proof (LaTeX). Computation only if exhaustive over a finite set the argument has reduced the
problem to (code included, < 10 min).
