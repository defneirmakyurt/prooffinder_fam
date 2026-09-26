# code/

`check_c1.py` (stdlib only, exact integer arithmetic). Sanity check, NOT load-bearing for the proof.

Run: `python3 check_c1.py 45`   (argument = NMAX; default 40)

For each n in [1, NMAX] it enumerates all partitions of n, finds the cyclic ones by iterating B,
checks they equal the predicted set {lambda(eps): eps in {0,1}^k, |eps| = r} (k = rank, r = n - T_{k-1}),
counts the cycles and compares with (1/k) sum_{d | gcd(k,r)} phi(d) C(k/d, r/d), and for triangular n
checks every orbit reaches delta_k.

Measured: `/usr/bin/time -p python3 check_c1.py 45` -> "ALL OK up to 45", real 18.58 s.
