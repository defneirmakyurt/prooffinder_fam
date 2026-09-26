# Code for B-C4-005

`check.py` (stdlib only, exact integer arithmetic):

    python3 check.py 11 80

1. For k = 5..11 (first argument): enumerates ALL partitions of n = T_{k-1}+1, finds cyclic
   partitions by direct cycle detection (independent of B-C1) and checks they match the B-C1
   description; computes d_B for every partition; checks max d_B = (k-1)(k-3); checks
   d_B(lambda^(k)) = (k-1)(k-3) for lambda^(k) = (k-2,k-2,k-3,...,3,2,2,1); checks every
   near state D(p,Q) (|Q| = 2, valid Young diagram) has d_B <= (k-1)(k-3).
2. For k = 5..80 (second argument): simulates the orbit of lambda^(k) and checks
   d_B = (k-1)(k-3).

Measured: `/usr/bin/time -p python3 check.py 11 80` -> ALL OK, real 7.26 s.
These are finite checks: they prove nothing for k outside the range and are NOT used as a
step of the lower-bound proof (which is symbolic, proof.md Step 5). The upper bound for
general partitions is not reduced to a finite set, so check (1) is evidence only.

Exploratory (not load-bearing): `out/tmp/explore.py`, `out/tmp/orbit.py`, `out/tmp/reduce.py`.
