# Target: B-C6, structural results (gated separately from the lower bound)

Definitions as in run/B/statement.md. Diagram of a partition = its Young diagram; lambda subset mu means diagram
containment (lambda_i <= mu_i for all i, partitions of possibly different sizes). n = T_{k-1} + r, rank k, 1 <= r <= k.
Claims to verify, each for EVERY n, k, partition in range:
 (i)   Containment monotonicity: lambda subset mu implies B(lambda) subset B(mu).
 (ii)  For every lambda |- n (n >= 1, rank k): d_B(lambda) = max{a(lambda), b(lambda)}, where a(lambda) = min{t >= 0 :
       delta_{k-1} subset B^t(lambda)} ("fill time") and b(lambda) = min{t >= 0 : B^t(lambda) subset delta_k} ("fit time");
       hence on each block T_{k-1} <= n <= T_k, D_B(n) = max(A_k(n), B_k(n)) with A_k(n) = max over lambda |- n of a,
       B_k(n) = max over lambda |- n of b, A_k non-increasing and B_k non-decreasing in n on the block (exact definitions
       and block-endpoint conventions as in the proof under review; check them).
 (iii) Quasi-convexity: D_B(n) <= max(D_B(n_1), D_B(n_2)) whenever T_{k-1} <= n_1 <= n <= n_2 <= T_k.
 (iv)  D_B(n) <= k^2 - k for every n >= 2 of rank k.
 (v)   B_k(n) >= max{n-k+1, (k+1)(r-2)+2} and, for r <= k-3, A_k(n) >= (k-1)(k-r-2).
Gated Cells 1 and 2 may be used. The general upper bound D_B(n) <= F(n) is NOT part of this target.
