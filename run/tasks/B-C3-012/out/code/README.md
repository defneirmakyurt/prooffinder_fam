# code/ (stdlib only)

`phase_stats.py KMAX`: for 4 <= k <= KMAX, every non-triangular n with T_{k-1} < n < T_k, and every partition of n, it
iterates B until the Cell-1 cyclic criterion holds and records d_B, t_A (diagonals 0..k-2 full), t_B (nothing on a
diagonal >= k+1) and t_C = entry time into C_k. It also checks N_{>=e}(B lam) <= N_{>=e}(lam) on every step and
d_B <= k^2-2k-1.

Run (measured): `/usr/bin/time -p python3 phase_stats.py 8` gives ALL OK in real 22.46 s. Output: run_phase_stats_8.txt.
This is a finite check (k <= 8 only). It proves nothing for larger k.
