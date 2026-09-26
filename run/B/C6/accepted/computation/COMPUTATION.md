# COMPUTER-VERIFIED (finite range only): D_B(n) = F(n) for every 1 <= n <= 60

Two independently written programs (blind provers B-C6-002 and B-C6-004, no shared code), exact integer arithmetic,
stdlib Python, exhaustive over ALL partitions of each n (no symmetry reduction), d_B by cycle-entry time.
- prog_A_B-C6-002/conj_table.py 60 : 0 mismatches for n = 1..60; head re-run 40 s (head_rerun_n60.txt).
- prog_B_B-C6-004/conj_check.py 55 : 0 mismatches for n = 1..55; head re-run 15 s. Author's run n = 56..62: 0 mismatches (69 s).
F(n) as in run/B/C6/target_lower.md. This proves nothing for n > 60 (n > 62 for program B alone).
