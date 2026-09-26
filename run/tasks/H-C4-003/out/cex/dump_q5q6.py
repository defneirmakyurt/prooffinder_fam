#!/usr/bin/env python3
"""Referee: SA (same as sa_search.py, mode 'count', seeds 5000/6000) to produce Q_5 / Q_6 labellings,
written to out/cex/Q5_ref.txt, Q6_ref.txt for scoring by the accepted checker. Stdlib, exact."""
import math, random, os
def score(d, order, pos):
    n = 1 << d; N = [0] * n; tot = 0
    for v in order:
        acc = 0; k = 0
        for j in range(d):
            w = v ^ (1 << j)
            if pos[w] < pos[v]: acc += N[w]; k += 1
        N[v] = acc if k else 1; tot += N[v]
    return tot
def sa(d, iters, seed):
    rng = random.Random(seed); n = 1 << d
    order = list(range(n)); order.sort(key=lambda v: bin(v).count("1") + rng.random() * 1.5)
    pos = [0] * n
    for i, v in enumerate(order): pos[v] = i
    cur = score(d, order, pos); best = (cur, list(order))
    for it in range(iters):
        T = 3.0 * (1 - it / iters) + 0.05
        i = rng.randrange(n)
        j = min(n - 1, max(0, i + rng.randint(-8, 8))) if rng.random() < 0.5 else rng.randrange(n)
        if i == j: continue
        order[i], order[j] = order[j], order[i]; pos[order[i]] = i; pos[order[j]] = j
        new = score(d, order, pos)
        if new <= cur or rng.random() < math.exp((cur - new) / T):
            cur = new
            if new < best[0]: best = (new, list(order))
        else:
            order[i], order[j] = order[j], order[i]; pos[order[i]] = i; pos[order[j]] = j
    return best
here = os.path.dirname(os.path.abspath(__file__))
for d, seed in ((5, 5000), (6, 6000)):
    c, order = sa(d, 20000, seed)
    with open(os.path.join(here, "Q%d_ref.txt" % d), "w") as fh:
        fh.write("".join(format(v, "0%db" % d) + "\n" for v in order))
    print("d=%d SA best count %d -> Q%d_ref.txt" % (d, c, d))
