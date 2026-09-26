# Target: B-C3(a) and the UPPER half of B-C3(b)

Definitions as in run/B/statement.md (partition, shift B, cyclic, d_B, D_B, T_k, rank).
(a) For every k >= 4, every non-triangular n with T_{k-1} < n < T_k, and every partition lambda of n:
    d_B(lambda) <= k^2 - 2k - 1.
(b-upper) In particular D_B(T_k - 1) <= k^2 - 2k - 1 for every k >= 4 (n = T_k - 1 is non-triangular of rank k).
    (Lower half D_B(T_k-1) >= k^2-2k-1 is already proved; with (a) this gives D_B(T_k-1) = k^2-2k-1.)
A complete, self-contained, line-by-line written proof valid for every k >= 4; finite checks prove nothing for all k.
