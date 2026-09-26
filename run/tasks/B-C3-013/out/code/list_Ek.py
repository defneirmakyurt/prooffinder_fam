#!/usr/bin/env python3
"""Writes the explicit list E_k (exhaustive, exact) for k in [KMIN,KMAX] to lists/E_<k>.txt,
one partition per line, sorted lexicographically decreasing. Stdlib only."""
import sys, os
from check_Ek import dvals
KMIN = int(sys.argv[1]) if len(sys.argv) > 1 else 4
KMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 10
os.makedirs("lists", exist_ok=True)
for k in range(KMIN, KMAX + 1):
    n = k*(k+1)//2 - 1; d = dvals(n); M = max(d.values())
    E = sorted((p for p in d if d[p] == M), reverse=True)
    with open(f"lists/E_{k}.txt", "w") as f:
        f.write(f"# k={k} n={n} max d_B={M} |E_k|={len(E)}\n")
        for p in E: f.write(" ".join(map(str, p)) + "\n")
    print(k, len(E))
