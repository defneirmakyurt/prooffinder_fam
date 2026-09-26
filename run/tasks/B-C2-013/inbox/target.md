# Target: B-C2 (D_B at Triangular n, 2 points, written proof)

Definitions (verbatim from the official statement, run/B/statement.md): a partition of n >= 1 is a weakly
decreasing sequence lambda = (lambda_1, ..., lambda_s) of positive integers with sum n (s piles).
The shift B(lambda) is the partition whose parts are the positive numbers among lambda_1 - 1, ..., lambda_s - 1
together with one extra part equal to s. lambda is cyclic if B^i(lambda) = lambda for some i >= 1.
d_B(lambda) = min{ i >= 0 : B^i(lambda) is cyclic },  D_B(n) = max{ d_B(lambda) : lambda a partition of n }.
T_k = k(k+1)/2, delta_k = (k, k-1, ..., 2, 1).

Cell text (verbatim): "Next, how long the process can take to reach a cycle, starting with the triangular
numbers. Determine D_B(T_k) for every k, with proof of both bounds."

Exact target (exact extremal value; the two halves are gated separately):
- Give an explicit formula F(k) (with any small-k exceptions stated separately and exactly) such that
  D_B(T_k) = F(k) for EVERY k >= 1.
- UPPER bound: prove d_B(lambda) <= F(k) for every partition lambda of T_k, for every k >= 1.
- LOWER bound: give an explicit partition lambda^(k) of T_k, as a function of k, and prove d_B(lambda^(k)) = F(k)
  (in particular >= F(k)) for every k >= 1.
- Any fact about which partitions of T_k are cyclic must itself be proved in the submission (no gated
  lower-cell results are available as assumptions yet).

Hand-in: a written proof (LaTeX), stating clearly what is established. Computation may be used only if exhaustive
over a finite set the argument has reduced the problem to (code included, < 10 min); small-k tables alone
prove nothing for all k.
