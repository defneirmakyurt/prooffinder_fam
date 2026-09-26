# Target: B-C6, general LOWER bound (gated separately)

Definitions as in run/B/statement.md (partition, shift B, cyclic, d_B, D_B, T_k, delta_k, rank).
For n >= 1 write n = T_{k-1} + r with k the rank of n and 1 <= r <= k. Define F(1) = F(2) = 0 and, for n >= 3,
  F(n) = max{ n - k + 1 ;  r(k+1) - 2k  if r >= 2 ;  (k-1)(k-2-r)  if k >= 4 and r <= k-3 }.
Claim to verify: for EVERY n >= 1, D_B(n) >= F(n), each term of the maximum attained exactly (d_B equal to the term)
by an explicit partition of n given as a function of (k, r), proved symbolically for every (k, r) in the term's range.
Cyclicity facts may use gated Cell 1. The upper bound D_B(n) <= F(n) is NOT part of this target.
