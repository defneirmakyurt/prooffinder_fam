# Code for B-C3-004 (stdlib only; run with plain python3)

- `check_small.py K`: for every rank k = 2..K and every n with T_{k-1} < n < T_k, builds the whole functional
  graph of B on the partitions of n (exact integer tuples), finds the cyclic partitions by in-degree peeling,
  computes d_B for all partitions and D_B(n). Checks (k >= 4): D_B(n) <= k^2-2k-1; D_B(T_k-1) = k^2-2k-1;
  d_B(lambda*_k) = D_B(T_k-1); every extremal lambda of T_k-1 has B^{D-1}(lambda) = nu_k. Prints #extremals.
  Run: `/usr/bin/time -p python3 check_small.py 10` -> "ALL CHECKS PASSED", real 39.42 s (measured).
  (`check_small.py 9`: real 8.23 s.) Output of the K=10 run: `run_K10.txt`.
  This proves the statements ONLY for 2 <= k <= 10; it is evidence, not a proof, for larger k.
- `check_classC.py K`: for k = 3..K enumerates all pairs (A,P) satisfying the support rule with
  1 <= |A|+|P| <= k-1, checks that B(lambda) equals the rotation/absorption rule of Lemma 3.1, and that the
  class-C depth is <= k^2-2k-1 (it equals it for every k). Run: `/usr/bin/time -p python3 check_classC.py 10`
  -> "ALL CHECKS PASSED", real 3.41 s. Cross-check only; Theorem 6.1 does not rest on it.
