# Code for B-C2-006 (stdlib only, exact integers)

check_DB_triangular.py  (copied unchanged from subject B-C2-002)
  Run: /usr/bin/time -p python3 check_DB_triangular.py 1 11
  For each k in range: enumerates ALL partitions of T_k (count asserted = p(T_k) by independent DP),
  iterates B to delta_k, prints max d_B and compares with k^2-k; also checks the witness and the two-track region.
  Measured here: ALL OK, real 40.57 s. Establishes d_B(l) <= k^2-k for all l |- T_k, 1 <= k <= 11 only.

check_monotone_queue.py  (sanity only; proof.md Steps 19-20 are proved by hand and do not rest on it)
  Run: /usr/bin/time -p python3 check_monotone_queue.py 16
  Checks (B l)'_j = l'_{j+1} + [j <= l'_1] for all partitions of n <= 16, and D(a) subset D(b) => D(Ba) subset D(Bb)
  for all comparable pairs of partitions of sizes <= 16. Measured: OK (914 partitions, 67389 pairs), real 0.34 s.
