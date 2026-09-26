# Target: B-C2, LOWER-BOUND half (gated separately from the upper bound)

Definitions as in run/B/statement.md (partition, shift B, cyclic, d_B, D_B, T_k, delta_k).

Claim to verify: for every k >= 1, the explicit partition lambda^(k) of T_k defined by
  lambda^(1) = (1), and for k >= 2: lambda^(k) = (k-1, k-1, k-2, ..., 2, 1, 1)
  (i.e. lambda_1 = k-1, lambda_i = k+1-i for 2 <= i <= k, lambda_{k+1} = 1)
satisfies d_B(lambda^(k)) = k^2 - k exactly. Consequently D_B(T_k) >= k^2 - k for every k >= 1.
This requires: (1) that lambda^(k) is a partition of T_k; (2) the identification of the cyclic partitions of T_k
(delta_k is the only one; gated in Cell 1 and may be used); (3) that B^i(lambda^(k)) != delta_k for i < k^2-k and
B^{k^2-k}(lambda^(k)) = delta_k, proved for EVERY k >= 1 (symbolically in k, not by a table).
The upper bound D_B(T_k) <= k^2 - k is NOT part of this target; the proof's own upper-bound sections are out of scope
(judge only the parts the lower-bound argument depends on).
