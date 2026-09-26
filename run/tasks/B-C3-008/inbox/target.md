# Target: B-C3(b), LOWER-BOUND half (gated separately)

Definitions as in run/B/statement.md (partition, shift B, cyclic, d_B, D_B, T_k, delta_k).

Claim to verify: for every k >= 3, the explicit partition of T_k - 1
  lambda*_k = (k-1, k-2, k-2, k-3, ..., 2, 1, 1)
satisfies d_B(lambda*_k) = k^2 - 2k - 1 exactly; consequently D_B(T_k - 1) >= k^2 - 2k - 1 for every k >= 3.
Requires: lambda*_k is a partition of T_k - 1 (check the part list for every k >= 3, incl. k = 3, 4 where the
pattern is short); the cyclic partitions of T_k - 1 (gated Cell 1: delta_{k-1} plus k-1 of the k cells of the
k-th diagonal) may be used; B^i(lambda*_k) is not cyclic for i < k^2-2k-1 and is cyclic at i = k^2-2k-1, proved for
EVERY k >= 3 symbolically. The upper bound (a) and the maximiser classification (c) are NOT part of this target.
