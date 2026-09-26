#!/usr/bin/env python3
"""Stdlib-only exhaustive check (corroboration only, NOT a proof for all k).
For each k in [kmin, kmax], n = T_{k-1}+1: computes d_B for every partition of n,
reports max d_B, compares with (k-1)(k-3), counts maximisers, checks that
lambda^(k) = (k-2,k-2,k-3,...,3,2,2,1) is a maximiser, and checks that the set of
cyclic partitions found by cycle detection equals {delta_{k-1} + one cell on diagonal k}.
Also prints D_B(n) for n = 1..nmax (to compare with Griggs-Ho 1998, Figure 1).
Usage: check_r1.py kmin kmax nmax
"""
import sys

def partitions(n):
    # iterative generation of all partitions of n as tuples (weakly decreasing)
    a = [0] * (n + 1)
    k = 1
    a[1] = n
    out = []
    # standard "rule_asc" algorithm (ascending compositions), reversed
    a = [0] * (n + 1)
    k = 1
    y = n - 1
    while k != 0:
        x = a[k - 1] + 1
        k -= 1
        while 2 * x <= y:
            a[k] = x
            y -= x
            k += 1
        l = k + 1
        while x <= y:
            a[k] = x
            a[l] = y
            out.append(tuple(reversed(a[:k + 2])))
            x += 1
            y -= 1
        a[k] = x + y
        y = x + y - 1
        out.append(tuple(reversed(a[:k + 1])))
    return out

def B(lam):
    s = len(lam)
    r = [x - 1 for x in lam if x > 1]
    r.append(s)
    r.sort(reverse=True)
    return tuple(r)

def depths(n):
    P = partitions(n)
    succ = {p: B(p) for p in P}
    state = {}  # 0 unvisited, 1 on stack, 2 done
    cyc = set()
    for p in P:
        if p in state:
            continue
        path = []
        pos = {}
        x = p
        while x not in state:
            state[x] = 1
            pos[x] = len(path)
            path.append(x)
            x = succ[x]
        if state[x] == 1:  # found a new cycle
            for y in path[pos[x]:]:
                cyc.add(y)
        for y in path:
            state[y] = 2
    d = {c: 0 for c in cyc}
    for p in P:
        if p in d:
            continue
        path = []
        x = p
        while x not in d:
            path.append(x)
            x = succ[x]
        base = d[x]
        for y in reversed(path):
            base += 1
            d[y] = base
    return P, cyc, d

def main():
    kmin, kmax, nmax = map(int, sys.argv[1:4])
    ok = True
    print("D_B(n), n=1..%d:" % nmax, [max(depths(n)[2].values()) for n in range(1, nmax + 1)])
    for k in range(kmin, kmax + 1):
        n = k * (k - 1) // 2 + 1
        P, cyc, d = depths(n)
        delta = [k - i for i in range(1, k)]  # delta_{k-1} = (k-1,...,1)
        expected = set()
        for j in range(1, k + 1):
            g = delta[:] + [0]
            g[j - 1] += 1
            expected.add(tuple(x for x in g if x > 0))
        M = max(d.values())
        F = (k - 1) * (k - 3)
        lam = tuple([k - 2] + [k - i for i in range(2, k - 1)] + [2, 1])
        nmax_ = sum(1 for v in d.values() if v == M)
        good = (M == F) and (cyc == expected) and (sum(lam) == n) and (d[lam] == F)
        ok &= good
        print("k=%d n=%d #partitions=%d maxd=%d F=%d #maximisers=%d cyclic_ok=%s d(lambda^k)=%d %s"
              % (k, n, len(P), M, F, nmax_, cyc == expected, d[lam], "OK" if good else "FAIL"))
    print("ALL OK" if ok else "SOME FAILURE")

if __name__ == "__main__":
    main()
