# Stuck / limits

none for the target (both halves of U(Q_5) = 88 are in hand).

Limits worth knowing:
- The lower bound is computer-assisted (layered DP, proof.md); run L5-H' takes 2m40s on this shared
  4-core machine, L5-S0 1m16s, L5-S 1.3 s.
- A run with neither the matching heuristic nor orbit merging (the fewest-assumption variant) was not
  attempted for d = 5: extrapolating layer sizes (heuristic off multiplies the peak layer by
  ~100 in the orbit-merged runs: 282,314 vs 2,543) it would need far more than the 2.3e6-state peak
  layer of L5-H', too much memory for a laptop hash table.
- Nothing is claimed for d != 5 beyond the d = 3, 4 sanity checks.
