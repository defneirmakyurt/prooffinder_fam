# Code for B-C3-010 (stdlib-only Python 3, exact integer arithmetic)

- `check_E.py K` : for 4 <= k <= K, enumerates ALL partitions of T_k-1, computes d_B exactly (definition of B plus the
  Cell-1 cyclic test), and asserts: max d_B = M = k^2-2k-1; E_k = {d_B = M} equals R_k = level M-1 of the backward tree of
  nu_k built with the preimage rule (proof.md Lemma 2.1, re-checked against B for every partition); every member of E_k is
  a Garden of Eden. Does NOT use (H). Proves target items 1-3 for 4<=k<=K only.
  Run: `/usr/bin/time -p python3 check_E.py 11` -> output in `run_K11.txt` (about 30 s).
- `print_R.py k` : prints the explicit list R_k (subset of E_k for all k by proof.md Prop 4.1; equal to E_k for k<=11 by
  check_E.py), verifying B^{M-1}(lambda) = nu_k for each member.
- `check_families.py K` : cross-check (not load-bearing) of proof.md Prop 3.6 (D_1 list), 4.2 (lambda*_k in R_k) and 4.3
  (B^3 agreement of alpha_k, beta_k, lambda*_k; d_B = M) for 4 <= k <= K. Run: `python3 check_families.py 60` (about 1 s).
- `heights.py k` : exploratory; prints the preimage-tree height of each element of D_1. `heights_out.txt` = k=4..9.
