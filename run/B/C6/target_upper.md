# Target: B-C6, UPPER bound D_B(n) <= F(n) (the open half)

Definitions as in run/B/statement.md. For n = T_{k-1} + r (rank k, 1 <= r <= k), F(1) = F(2) = 0 and for n >= 3
  F(n) = max{ n - k + 1 ;  r(k+1) - 2k  if r >= 2 ;  (k-1)(k-2-r)  if k >= 4 and r <= k-3 }.
Known (gated): D_B(n) >= F(n) is claimed with explicit witnesses (being refereed); D_B(T_k) = k^2 - k (r = k, Cell 2);
D_B(n) <= k^2-2k-1 for every non-triangular n of rank k >= 4, with equality at r = k-1 (Cell 3). Exhaustive computation
(not a proof) gives D_B(n) = F(n) for every n <= 62.
Prove d_B(lambda) <= F(n) for every partition lambda of n, for as large an INFINITE family of n as you can: all n if
possible; otherwise e.g. r = k-2, r = k-3, all r >= k - c for a fixed c, all r >= k/2, or r = 1, 2, ... for every k >= k_0.
State exactly which (k, r) each result covers. Every result must hold for every k in its range (finite checks prove nothing for all k).
