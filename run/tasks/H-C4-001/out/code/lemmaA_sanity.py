#!/usr/bin/env python3
"""
lemmaA_sanity.py -- numerical sanity check (NOT a proof; the proof is written in claims.md)
of Lemma A: for every labelling of Q_d,
    #uphill paths >= 2^d + (d-1)*|S|,  S = {v : v has >= 2 neighbours with smaller label},
and T = V \\ S induces a forest.
Checks it on random labellings (seeded) and on labelling files given on the command line.
Stdlib only, exact integers.
usage: python3 lemmaA_sanity.py [file ...]
"""
import random
import sys


def count(d, order):
    n = 1 << d
    f = [0] * n
    for i, v in enumerate(order):
        f[v] = i
    N = [0] * n
    tot = 0
    for v in order:
        nb = [v ^ (1 << j) for j in range(d)]
        low = [w for w in nb if f[w] < f[v]]
        N[v] = (0 if low else 1) + sum(N[w] for w in low)
        tot += N[v]
    return tot, f


def check(d, order):
    n = 1 << d
    tot, f = count(d, order)
    S = [v for v in range(n) if sum(1 for j in range(d) if f[v ^ (1 << j)] < f[v]) >= 2]
    inS = [False] * n
    for v in S:
        inS[v] = True
    par = list(range(n))

    def find(x):
        while par[x] != x:
            par[x] = par[par[x]]
            x = par[x]
        return x
    forest = True
    for v in range(n):
        if inS[v]:
            continue
        for j in range(d):
            w = v ^ (1 << j)
            if w < v and not inS[w]:
                a, b = find(v), find(w)
                if a == b:
                    forest = False
                par[a] = b
    bound = n + (d - 1) * len(S)
    return tot, bound, len(S), forest


def main():
    rng = random.Random(20260926)
    bad = 0
    trials = 0
    for d in range(1, 8):
        for _ in range(300 if d <= 5 else 40):
            order = list(range(1 << d))
            rng.shuffle(order)
            # also partially sorted orders (closer to good labellings)
            if rng.random() < 0.5:
                order.sort(key=lambda v: bin(v).count("1") + rng.random() * 3)
            tot, bound, s, forest = check(d, order)
            trials += 1
            if tot < bound or not forest:
                bad += 1
                print("VIOLATION d=%d tot=%d bound=%d forest=%s" % (d, tot, bound, forest))
    print("random trials: %d, violations: %d" % (trials, bad))
    for fn in sys.argv[1:]:
        rows = open(fn).read().split()
        d = len(rows[0])
        order = [int(r, 2) for r in rows]
        tot, bound, s, forest = check(d, order)
        print("%s: d=%d count=%d |S|=%d bound 2^d+(d-1)|S|=%d T-forest=%s" % (fn, d, tot, s, bound, forest))


if __name__ == "__main__":
    main()
