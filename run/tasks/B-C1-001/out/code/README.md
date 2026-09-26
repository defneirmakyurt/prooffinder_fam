# out/code

`check_c1.py`: stdlib-only, exact integer arithmetic. It is a sanity check, not part of the proof.
No step of proof.md depends on it.

Run: `python3 check_c1.py 45` (the argument is NMAX, default 45).

For every n in [1, NMAX] the script:
- enumerates all partitions of n;
- applies the shift B;
- asserts E(B(lambda)) <= E(lambda);
- finds all partitions lying on a cycle and asserts that this set equals C(k, r) (k = rank, r = n - T_{k-1});
- counts the cycles and asserts the count equals (1/k) sum_{d | gcd(k,r)} phi(d) binom(k/d, r/d);
- for r = k, asserts that the cyclic set is {delta_k}.

Measured: `/usr/bin/time -p python3 check_c1.py 45` prints "ALL OK up to n = 45" (real 4.22 s and 4.32 s on two runs).
