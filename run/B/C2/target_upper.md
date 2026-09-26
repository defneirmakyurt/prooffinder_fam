# Target: B-C2, UPPER-BOUND half (the open rung R9 of lineage diagonal-rotation-CRT)

Definitions as in run/B/statement.md (partition, shift B, cyclic, d_B, D_B, T_k, delta_k).

Prove: for every k >= 1 and EVERY partition lambda of T_k, d_B(lambda) <= k^2 - k,
i.e. B^{k^2-k}(lambda) = delta_k (delta_k is the only cyclic partition of T_k: gated Cell 1).
The proof must be valid for all k (a check for k <= 11 exists and is not a proof for larger k).
Together with the lower bound (witness (k-1,k-1,k-2,...,1,1) with d_B = k^2-k), this gives D_B(T_k) = k^2 - k.
