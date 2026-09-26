# Code for B-C3-002

`check_c3.py` (stdlib only, exact integer arithmetic).

Run: `python3 check_c3.py K`   (K = largest rank k; the reported run used K = 10)

It enumerates all partitions of every n with T_{k-1} < n < T_k, 2 <= k <= K. It computes d_B for each
by exact cycle detection on the functional graph of B (independent of Cell 1), and checks:
- (A) D_B(n) <= k^2-2k-1 for 4 <= k <= K (finite range only; not a proof for k > K);
- (B) D_B(T_k-1) = k^2-2k-1 for 4 <= k <= K; prints D_B(2), D_B(5) and the maximiser lists for k <= 5;
- (C) lambda*_k attains it; for k >= 6 the maximiser set equals {lambda : B^{k^2-4k-2}(lambda) = mu_k}, and d_B(mu_k) = 2k+1;
- (L) the closed formula of Lemma R4 against brute-force d_B for every case-B Phi=1 partition, 2 <= r <= k-1.

Prints "ALL OK" if every check passes.
Measured: `/usr/bin/time -p python3 check_c3.py 10` gave real 28.71 s, output ALL OK.
