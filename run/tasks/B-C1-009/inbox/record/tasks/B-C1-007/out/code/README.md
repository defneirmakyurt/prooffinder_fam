# out/code (B-C1-007)

check_c1_lit.py: stdlib only, exact integer arithmetic; independent of the blind scripts. Sanity check, NOT load-bearing.
Checks, for each n in [1, NMAX]: Lemma 3 (E(B lam) <= E(lam), equality iff lam_1 - 1 <= #parts), the cyclic set equals
{lambda(eps)}, the number of cycles equals the necklace formula, and for triangular n the cyclic set is {delta_k}.

Runs (measured):
- `/usr/bin/time -p python3 check_c1_lit.py 45` -> "ALL OK up to n = 45", real 2.50 s (log: run45.log)
- `/usr/bin/time -p python3 check_c1_lit.py 50` -> "ALL OK up to n = 50", real 6.74 s (log: run50.log)
