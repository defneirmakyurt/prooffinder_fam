# Number of drop events (energy decreases) along the transient of every extremizer of T_k - 1. Exact, stdlib only.
import time
from collections import Counter
from small_cases import analyse, B
from translations import energy
t0 = time.time()
for k in range(4, 10):
    n = k*(k+1)//2 - 1
    D, ext, cyc, d = analyse(n)
    prof = Counter()
    for l in ext:
        x = l; drops = []
        for i in range(D):
            y = B(x)
            if energy(y) < energy(x): drops.append(i)
            x = y
        prof[tuple(drops)] += 1
    print(f"k={k} n={n} #ext={len(ext)} drop-step patterns (step indices, 0-based) -> count: {dict(prof)}")
print("runtime %.2fs" % (time.time()-t0))
