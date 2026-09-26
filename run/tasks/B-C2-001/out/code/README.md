# code/ for B-C2-001

`check_triangular.py` uses only the standard library and exact integers (tuples of ints, no floats).

Run: `python3 check_triangular.py KMAX KWIT` (defaults 10, 60).

What it checks:
- Part A (exhaustive, k = 1..KMAX): enumerates every partition of T_k, iterates B until delta_k
  (termination guaranteed by proof.md Step 5), computes the hitting time (= d_B by Step 6.3),
  and prints the maximum over all partitions next to k^2 - k. This establishes
  D_B(T_k) = k^2 - k for k = 1..KMAX only (proof.md Step 8). It says nothing about larger k.
- Part B (k = 2..KWIT): simulates the witness lambda^(k) = (k-1, k-1, k-2, ..., 1, 1) and prints
  its hitting time. This only sanity-checks proof.md Step 7, which is proved for all k.

Recorded runs (macOS laptop, /usr/bin/time -p):
- `python3 check_triangular.py 10 60`: A k=1..10 all max_t = k^2-k OK; B k=2..60 all OK; "ALL OK"; real 2.53 s.
- `python3 check_triangular.py 11 60`: adds A k=11 (T_11 = 66, 2323520 partitions, max_t = 110 = k^2-k OK);
  "ALL OK"; real 18.04 s.
