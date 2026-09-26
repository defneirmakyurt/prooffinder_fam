#!/usr/bin/env python3
"""sanity.py -- stdlib only. For random labellings and SA-style perturbations of Q_d, check
   (1) D_f = {v : down(v) >= 2} is decycling (Q_d - D_f is a forest), and
   (2) P(f) >= 2^d + (d-1)|D_f|   (Step 5 of out/proof.md).  Exact integers."""
import random, sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from decycle import is_decycling
def count(d, order):
    n = 1 << d; f = [0]*n
    for i, v in enumerate(order): f[v] = i
    N = [0]*n; tot = 0; down = [0]*n
    for v in order:
        lower = [v ^ (1 << j) for j in range(d) if f[v ^ (1 << j)] < f[v]]
        down[v] = len(lower)
        N[v] = (1 if not lower else 0) + sum(N[w] for w in lower); tot += N[v]
    return tot, down
random.seed(int(sys.argv[2]) if len(sys.argv) > 2 else 1)
trials = int(sys.argv[1]); bad = 0
for t in range(trials):
    d = random.choice([3, 4, 5, 6])
    order = list(range(1 << d)); random.shuffle(order)
    # bias toward low counts: sort a random fraction by weight parity
    if t % 2:
        order.sort(key=lambda v: (bin(v).count("1") % 2, random.random()))
    P, down = count(d, order)
    D = [v for v in range(1 << d) if down[v] >= 2]
    if not is_decycling(d, D) or P < 2**d + (d-1)*len(D):
        bad += 1
print("trials=%d violations=%d" % (trials, bad))
