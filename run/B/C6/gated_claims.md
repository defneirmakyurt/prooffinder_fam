# Gated results of lower cells (passed the verification gate; may be used as stated, cite them as "Cell 1", "Cell 2", "Cell 3 lower bound")

Cell 1: for n = T_{k-1} + r with 1 <= r <= k, lambda is cyclic iff lambda = (k-1+e_1, k-2+e_2, ..., 1+e_{k-1}, e_k)
(a final 0 dropped) with e in {0,1}^k and e_1 + ... + e_k = r. In particular delta_k is the unique cyclic partition of T_k.

Cell 2: D_B(T_k) = k^2 - k for every k >= 1.

Cell 3 lower bound: for every k >= 3, lambda*_k = (k-1, k-2, k-2, k-3, ..., 2, 1, 1) is a partition of T_k - 1 with
d_B(lambda*_k) = k^2 - 2k - 1; hence D_B(T_k - 1) >= k^2 - 2k - 1.
