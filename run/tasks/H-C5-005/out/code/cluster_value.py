#!/usr/bin/env python3
"""cluster_value.py -- stdlib only, exact. For every set K of even-weight vertices of Q_9 with 2 <= |K| <= smax that
is connected in the "distance 2" graph D and contains {0, e0+e1} (every D-connected K with |K| >= 2 is mapped to
such a set by an automorphism of Q_9 that preserves weight parity: translate a vertex of K to 0 [translation by
an even vector preserves parity], then permute coordinates so one of its D-neighbours in K becomes e0+e1), compute
  tau(K) = min |Z| over sets Z of odd vertices such that Q_9[K u (A_K minus Z)] is a forest,
where A_K = odd vertices with >= 2 neighbours in K (an odd vertex with <= 1 neighbour in K has degree <= 1 in
Q_9[K u O'] for any O', so it is on no cycle and never needs removing; odd vertices are pairwise non-adjacent and
so are even ones, so all edges of Q_9[K u O'] go between K and O').
Prints, per size, the number of sets and the maximum of value(K) = |K| - tau(K).
Usage: cluster_value.py smax
"""
import sys, itertools
d = 9; n = 1 << d
smax = int(sys.argv[1])
ev = [v for v in range(n) if bin(v).count('1') % 2 == 0]
D = {v: [v ^ (1 << i) ^ (1 << j) for i in range(d) for j in range(i + 1, d)] for v in ev}

def is_forest(K, keep):
    par = {}
    def fp(x):
        while par.setdefault(x, x) != x:
            par[x] = par[par[x]]; x = par[x]
        return x
    for o in keep:
        for j in range(d):
            m = o ^ (1 << j)
            if m in K:
                a, b = fp(o), fp(m)
                if a == b: return False
                par[a] = b
    return True

def tau(K):
    cnt = {}
    for m in K:
        for j in range(d):
            o = m ^ (1 << j); cnt[o] = cnt.get(o, 0) + 1
    A = [o for o, c in cnt.items() if c >= 2]
    for z in range(len(A) + 1):
        for Z in itertools.combinations(A, z):
            Zs = set(Z)
            if is_forest(K, [o for o in A if o not in Zs]):
                return z, len(A), len(cnt)
    raise RuntimeError

start = frozenset([0, 3])
level = {start}
for s in range(2, smax + 1):
    best = None; cntsets = 0; hist = {}
    for K in level:
        cntsets += 1
        t, a, nk = tau(K)
        val = len(K) - t
        hist[val] = hist.get(val, 0) + 1
        if best is None or val > best[0] or (val == best[0] and nk < best[2]):
            best = (val, sorted(K), nk)
    print('size %d: %d sets containing {0,e0+e1}; value histogram %s; best value %d (|N(K)|=%d, K=%s)' %
          (s, cntsets, dict(sorted(hist.items())), best[0], best[2], best[1]), flush=True)
    if s < smax:
        nxt = set()
        for K in level:
            for v in K:
                for w in D[v]:
                    if w not in K: nxt.add(K | {w})
        level = nxt
