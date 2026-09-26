# code/

`check.py` (stdlib only, exact integer arithmetic).

Run: `python3 check.py [KMAX_EXHAUSTIVE=9] [KMAX_ORBIT=20]`

What it checks:
1. For 4 <= k <= KMAX_EXHAUSTIVE and every n with T_{k-1} < n < T_k, it enumerates all partitions of n. It finds the
   cyclic ones by generic cycle detection (independent of Cell 1) and computes every d_B. Then it checks:
   - D_B(n) <= k^2-2k-1;
   - D_B(T_k-1) = k^2-2k-1 and d_B(X_k) equals it;
   - it prints the number of extremal partitions of T_k-1 (and the list when k <= 5).
2. For 4 <= k <= KMAX_ORBIT it checks d_B(X_k) = k^2-2k-1 by direct iteration of B, testing cyclicity with the Cell 1
   criterion.
3. For 4 <= k <= KMAX_ORBIT it enumerates every member of the class L_k of proof.md Step 5 (delta_m + (m-1) cells on
   diagonal m + one cell on diagonal m+1, all valid shapes). It checks that max d_B = k^2-2k-1 and that X_k is the only
   maximiser.

These checks are finite. They prove nothing beyond the listed k and do not replace Steps 4-5 or the GAP in Step 7.

Measured: `python3 check.py 9 25` gave ALL OK, real 25.35 s (log: run_9_25.log).
