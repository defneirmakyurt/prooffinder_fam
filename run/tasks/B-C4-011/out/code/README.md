# Code (stdlib-only, exact integer arithmetic; evidence only, nothing here proves the target for all k)

- check_r1.py kmin kmax nmax : exhaustive d_B over all partitions of T_{k-1}+1 for kmin <= k <= kmax;
  checks max = (k-1)(k-3), cyclic set = {gamma_j}, d_B(lambda^(k)) = (k-1)(k-3); prints D_B(n) for n <= nmax
  (compare Griggs-Ho 1998, Figure 1).
  Measured: `python3 check_r1.py 5 12 36` -> ALL OK, real 7.82 s.
- corner_obstruction.py kmin kmax : counts lambda of T_{k-1}+1 all of whose one-cell removals nu have
  d_B(nu) > (k-1)(k-3), and max_lambda min_nu d_B(nu). Measured: `python3 corner_obstruction.py 5 10`, real 0.81 s.
