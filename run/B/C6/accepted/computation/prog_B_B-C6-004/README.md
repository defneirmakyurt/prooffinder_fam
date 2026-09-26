# Code (stdlib Python 3 only; exact integer arithmetic)

- `table.py N` : exhaustive D_B(n) for n = 1..N (all partitions, functional-graph cycle detection). Columns: n k r D_B k^2-k-D_B #maximizers sample.
- `conj_check.py N [S]` : compares exhaustive D_B(n) with the conjectured F(n) for n = S..N (default S=1). Prints mismatches.
  Runs: `python3 conj_check.py 55` -> no mismatches, real 26.60 s (run_conj_1_55.txt);
        `.venv/bin/python3 conj_check.py 62 56` -> no mismatches, real 69.01 s (run_conj_56_62.txt).
- `witness_check.py` : sanity check (not load-bearing) of d_B for 1^n, delta_{k-1} u {r-1,1}, delta_{k-2} u {k-2,r+1}
  against Props A, B, C for 4 <= k <= 29. Output `[] 0` = no discrepancy. real 0.53 s.
The written proofs in proof.md do not rest on any of this code; the finite check only supports the conjecture for n <= 62.
