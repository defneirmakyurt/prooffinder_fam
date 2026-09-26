#!/usr/bin/env python3
"""Stdlib-only exploration (NOT load-bearing). For k in [kmin,kmax], n = T_{k-1}+1, count the
partitions lambda of n for which EVERY one-cell removal nu (nu a partition of T_{k-1}) has
d_B(nu) > (k-1)(k-3), i.e. for which the monotonicity bound d_B(lambda) <= min_nu d_B(nu)
cannot give the target bound directly. Also reports max over lambda of min_nu d_B(nu)."""
import sys
sys.path.insert(0, __import__('os').path.dirname(__file__))
from check_r1 import depths

def removals(lam):
    out = []
    for i in range(len(lam)):
        if i == len(lam) - 1 or lam[i] > lam[i + 1]:
            nu = list(lam); nu[i] -= 1
            out.append(tuple(x for x in nu if x > 0))
    return out

kmin, kmax = map(int, sys.argv[1:3])
for k in range(kmin, kmax + 1):
    n = k * (k - 1) // 2 + 1
    F = (k - 1) * (k - 3)
    P, cyc, d = depths(n)
    _, _, d0 = depths(n - 1)
    bad = 0; worst = 0
    for lam in P:
        m = min(d0[nu] for nu in removals(lam))
        worst = max(worst, m)
        if m > F:
            bad += 1
    print("k=%d n=%d F=%d (k-1)(k-2)=%d  #lambda with all removals d_B>F: %d   max_lambda min_nu d_B(nu)=%d"
          % (k, n, F, (k - 1) * (k - 2), bad, worst))
