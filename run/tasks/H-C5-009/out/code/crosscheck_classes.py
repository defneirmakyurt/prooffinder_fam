#!/usr/bin/env python3
"""crosscheck_classes.py -- stdlib only, exact. Independent cross-check of clusters.c for small sizes.
Enumerates ALL distance-2-connected sets K of even words of Q_9 with |K| = s containing {0, 3}
(3 = e0+e1; every D-connected set of size >= 2 has an image of this form under a parity-preserving automorphism:
translate one of its words to 0, then permute coordinates so a D-neighbour inside K becomes e0+e1),
and counts equivalence classes under G = {x -> pi(x) xor t, t even} using a DIFFERENT canonical form from clusters.c:
  key(K) = min over t in K, over all orderings of the rows of (K xor t) minus {0}, of the sorted tuple of columns.
(Column j of an ordered row list is the tuple of bit j of each row; a coordinate permutation permutes columns,
so sorting the columns removes it; minimising over t in K and over row orderings removes translation and row order.)
Also recomputes tau(K) by brute force over witness subsets (the subject's method) and prints the value histogram.
Usage: crosscheck_classes.py smax
"""
import sys, itertools
d = 9
smax = int(sys.argv[1])
D = {}
for v in range(512):
    if bin(v).count('1') % 2 == 0:
        D[v] = [v ^ (1 << i) ^ (1 << j) for i in range(d) for j in range(i + 1, d)]

def key(K):
    best = None
    for t in K:
        rows = [x ^ t for x in K if x != t]
        for perm in itertools.permutations(rows):
            cols = tuple(sorted(tuple((r >> j) & 1 for r in perm) for j in range(d)))
            if best is None or cols < best:
                best = cols
    return best

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
                return z

level = {frozenset([0, 3])}
for s in range(2, smax + 1):
    classes = {}
    for K in level:
        k = key(K)
        if k not in classes: classes[k] = K
    hist = {}
    for K in classes.values():
        v = len(K) - tau(K)
        hist[v if v >= 1 else '<=0'] = hist.get(v if v >= 1 else '<=0', 0) + 1
    print('size %d: %d sets containing {0,3}; %d classes; value histogram %s' % (s, len(level), len(classes), hist), flush=True)
    if s < smax:
        level = {K | {w} for K in level for v in K for w in D[v] if w not in K}
