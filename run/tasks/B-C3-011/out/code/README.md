# Code for B-C3-011 (stdlib only; plain python3 works)

`check_c3a.py K` — SANITY CHECK ONLY. The proof in ../proof.md does not rest on it (no step of the proof uses a computation).
Exact integer arithmetic throughout.
- Part 1: for every partition of every n = 1..T_K - 1, computes c_1..c_{3n+10} (c_i = number of parts of B^{i-1}(lambda)),
  finds every pattern (c_p..c_q) = (x-1, x, ..., x, x+1) (q >= p+2) and checks Lemma 6 (q-p != x, q-p <= x+1),
  Lemma 5 (p <= (q-p-1) x; this also covers Lemma 3 at q-p = 2) and Lemma 7 (q-p = x+1 => q <= T_x + 2).
- Part 2: for every rank 4 <= k <= K, every n with T_{k-1} < n < T_k and every partition lambda of n, with t = d_B(lambda)
  (cyclic test = the B-C1 form): checks Lemma 8.2(b), Lemma 9, the certificate used in Lemma 10 / Lemma 11
  (cases A1, A2, B, with the index ranges stated in the proof), and t <= k^2 - 2k - 1. Prints max d_B per rank and case counts.

Run (measured):
- `/usr/bin/time -p python3 check_c3a.py 7` -> ALL CHECKS PASSED, real 1.19 s
- `/usr/bin/time -p python3 check_c3a.py 9` -> ALL CHECKS PASSED, real 46.78 s (output in run_K9.txt)
A finite check proves nothing beyond 4 <= k <= K; it only guards against slips in the written lemmas.
