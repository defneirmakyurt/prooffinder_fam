# Code (stdlib Python 3 only, exact integer arithmetic)

- `conj_table.py N`: for every 1 <= n <= N enumerates all partitions of n, builds the functional graph of B,
  finds cyclic partitions directly (as nodes on cycles), computes D_B(n) exactly, and compares with
  L(n) of proof.md (0 for n <= 2). Output: one line `n rank D_B(n) L(n) OK|MISMATCH`, then the mismatch count.
  Run: `/usr/bin/time -p python3 conj_table.py 60 > conj_table_out.txt`.
  This supports the CONJECTURE only; it proves D_B(n)=L(n) only for the n it covers (1..60).
- `witness_check.py KMAX`: sanity check (not load-bearing; the formulas are proved in proof.md) that the three
  witness families have the proved d_B values for all ranks 2 <= k <= KMAX (cyclicity tested via the Cell 1
  characterisation). Run: `/usr/bin/time -p python3 witness_check.py 30`.

Measured runs (this session):
- `conj_table.py 60`: COMPLETED, n = 1..60, 0 mismatches, real 103.82 s (machine loaded; an earlier identical-logic run took 48.15 s). Output in conj_table_out.txt.
- `witness_check.py 30`: COMPLETED, ranks 2..30, 1276 cases, 0 failures, real 3.03 s. Output in witness_check_out.txt.
