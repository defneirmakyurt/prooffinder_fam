# Code — B-C4-007 (stdlib-only Python 3; integer arithmetic only, exact)

1. `exhaustive_DB.py KMIN KMAX`
   For each k in [KMIN, KMAX], enumerates ALL partitions of n = T_{k-1}+1, builds the functional graph of B,
   finds the cyclic partitions as the points on cycles (no theory assumed), computes d_B for every partition,
   and reports D_B(n), compares with F(k) = (k-1)(k-3), and checks that the cyclic set equals
   {delta_{k-1} + e_j : j = 1..k}.  Evidence only: it proves the formula for the k in range and nothing else.
   Run: `/usr/bin/time -p python3 exhaustive_DB.py 5 11`   (measured: real 2.10 s, ALL MATCH)
        `/usr/bin/time -l python3 exhaustive_DB.py 12 12`  (measured: real 11.33 s, ~1.27 GB RSS, match)

2. `verify_lower_orbit.py KMIN KMAX`
   Sanity check of proof.md Step 8: iterates B from lambda^(k) = (k-2,k-2,k-3,...,3,2,2,1) and asserts
   B^t(lambda) = Q(h(t); b(t), b(t)+1) for t <= k^2-4k+2, the two final states, cyclicity of gamma_3,
   the unit energy drop, and d_B = (k-1)(k-3). The proof itself is symbolic in k; this is not load-bearing.
   Run: `/usr/bin/time -p python3 verify_lower_orbit.py 5 60`   (measured: real 7.78 s)
