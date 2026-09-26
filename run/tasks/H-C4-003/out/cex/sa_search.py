#!/usr/bin/env python3
"""Referee counterexample search (stdlib, exact counts, fixed seeds and iteration counts).
(a) Simulated annealing over labellings of Q_d (move: swap two labels; 50% nearby positions),
    minimising the exact uphill count; tries to beat the claimed lower bounds
    U(Q_4)>=34, U(Q_5)>=88, U(Q_6)>=204, U(Q_7)>=464, U(Q_8)>=1040.
(b) Same search minimising slack = count - (2^d + (d-1)|S|) (Lemma A (ii)); a negative value
    would refute Lemma A.
A heuristic search proves nothing; it can only find counterexamples."""
import math, random, sys, time

def score(d, order, pos):
    n = 1 << d; N = [0] * n; tot = 0; s = 0
    for v in order:
        pv = pos[v]; acc = 0; k = 0
        for j in range(d):
            w = v ^ (1 << j)
            if pos[w] < pv: acc += N[w]; k += 1
        N[v] = acc if k else 1; tot += N[v]
        if k >= 2: s += 1
    return tot, n + (d - 1) * s

def sa(d, iters, seed, mode, start=None):
    rng = random.Random(seed); n = 1 << d
    if start is None:
        order = list(range(n)); order.sort(key=lambda v: bin(v).count("1") + rng.random() * 1.5)
    else:
        order = list(start)
    pos = [0] * n
    for i, v in enumerate(order): pos[v] = i
    def obj():
        tot, b = score(d, order, pos)
        return (tot if mode == 'count' else tot - b), tot, b
    cur, tot, b = obj(); best = (cur, tot, b)
    T0 = 3.0
    for it in range(iters):
        T = T0 * (1 - it / iters) + 0.05
        i = rng.randrange(n)
        j = min(n - 1, max(0, i + rng.randint(-8, 8))) if rng.random() < 0.5 else rng.randrange(n)
        if i == j: continue
        order[i], order[j] = order[j], order[i]; pos[order[i]] = i; pos[order[j]] = j
        new, nt, nb = obj()
        if new <= cur or rng.random() < math.exp((cur - new) / T):
            cur = new
            if new < best[0]: best = (new, nt, nb)
        else:
            order[i], order[j] = order[j], order[i]; pos[order[i]] = i; pos[order[j]] = j
    return best

def load(fn):
    return [int(r, 2) for r in open(fn).read().split()]

claimed = {4: 34, 5: 88, 6: 204, 7: 464, 8: 1040}
t0 = time.time()
plan = [(4, 20000, 3), (5, 20000, 3), (6, 15000, 2), (7, 8000, 1)]
for d, iters, runs in plan:
    for r in range(runs):
        t1 = time.time()
        bc = sa(d, iters, 1000 * d + r, 'count')
        bs = sa(d, iters, 5000 * d + r, 'slack')
        print("d=%d run %d (%d iters each): min count found=%d (claimed LB %d)%s; min slack found=%d%s (%.1fs)"
              % (d, r, iters, bc[1], claimed[d], "  ** BELOW CLAIM **" if bc[1] < claimed[d] else "",
                 bs[0], "  ** LEMMA A VIOLATED **" if bs[0] < 0 else "", time.time() - t1))
for d, fn in ((7, sys.argv[1]), (8, sys.argv[2])):
    t1 = time.time()
    bc = sa(d, 6000 if d == 7 else 3000, 77 + d, 'count', start=load(fn))
    print("d=%d SA started from subject artefact (%s): min count found=%d (claimed %d)%s (%.1fs)"
          % (d, fn.split('/')[-1], bc[1], claimed[d], "  ** BELOW CLAIM **" if bc[1] < claimed[d] else "", time.time() - t1))
print("total elapsed %.1fs" % (time.time() - t0))
