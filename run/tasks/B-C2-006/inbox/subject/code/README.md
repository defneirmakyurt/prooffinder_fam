# Code for B-C2-002

`check_DB_triangular.py` (stdlib only, exact integer arithmetic).

Run:  `python3 check_DB_triangular.py KMIN KMAX`   (e.g. `python3 check_DB_triangular.py 1 11`)

For each k in [KMIN, KMAX] it
1. enumerates all partitions of T_k and asserts the count equals p(T_k) computed by an independent DP
   (so the enumeration is complete);
2. computes d_B(lambda) for every partition by iterating B until delta_k is reached (a cycle avoiding delta_k
   would be detected and reported as failure);
3. prints D_B(T_k) = max d_B and compares with k^2 - k;
4. checks d_B(witness) = k^2 - k for the witness (1) (k=1), (k-1,k-1,k-2,...,2,1,1) (k>=2);
5. checks max d_B over the two-track region delta_{k-1} <= lambda <= delta_{k+1} is <= k^2 - k.

Measured: `/usr/bin/time -p python3 check_DB_triangular.py 1 11` -> ALL OK, real 14.85 s.

What this establishes: D_B(T_k) = k^2 - k for 1 <= k <= 11 exactly (exhaustive over all partitions of T_k).
It proves nothing for k >= 12.

`../tmp/` holds exploratory scripts (not relied upon): explore.py (small-k maximisers), explore2.py (refutes the
"final pair" invariant A1), explore3.py (time to enter the two-track region).
