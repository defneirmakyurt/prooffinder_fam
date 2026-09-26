#!/usr/bin/env python3
"""cluster_tau.py -- stdlib only, exact (integers / bitmasks).  Used by proof.md Steps 13-15.

For every cluster size k = 1..KMAX it enumerates, up to the automorphisms of Q_9 that preserve parity,
ALL sets C of odd vertices of Q_9 that are connected in the distance-2 graph and have |C| = k
("clusters"), and for each computes
    tau*(C) = max { tau(G_2[M']) : M' subset of N_E(C), Q_9[M' u (N_O(M') \\ C)] acyclic }
where N_E(C) = even vertices adjacent to C, N_O(M') = odd vertices adjacent to M', G_2 = distance-2 graph and
tau = vertex-cover number.  It prints, per k, the number of classes and max over classes of tau*(C) - k.

Enumeration: start from C = {o0}, o0 = 1 (weight 1).  Every connected k-set containing a given vertex is
obtained from a connected (k-1)-subset (remove a non-cut vertex of a spanning tree: a leaf) plus one
distance-2 neighbour of it, so extending every class representative of size k-1 by every distance-2
neighbour of every element, and taking canonical forms, yields every class of size k.
Canonical form of C: min over o in C and over orderings of the k rows of the matrix whose rows are the
vectors c XOR o (c in C), with columns then sorted -- i.e. min over (o, row order) of the column-sorted
matrix.  Two clusters are equivalent under x -> pi(x) XOR v (pi a coordinate permutation, v even) iff their
canonical forms agree (see README).

tau*(C): depth-first enumeration of all valid M' (the family is closed under subsets, so every valid set is
reached by adding candidates in increasing index order, each step checked for acyclicity with a fresh
union-find); tau(G_2[M']) = |M'| - alpha(G_2[M']) with alpha computed by exhaustive branching.
"""
import sys, itertools
D = 9
FULL = (1 << D) - 1
def wt(x): return bin(x).count("1")
DIST2 = [(1 << i) | (1 << j) for i in range(D) for j in range(i + 1, D)]

def canon(C):
    C = list(C); k = len(C); best = None
    for o in C:
        rows0 = [c ^ o for c in C]
        for perm in itertools.permutations(rows0):
            cols = sorted(tuple((r >> b) & 1 for r in perm) for b in range(D))
            key = tuple(cols)
            if best is None or key < best: best = key
    return best

def acyclic(verts):
    vs = list(verts); par = {v: v for v in vs}; S = set(vs)
    def f(x):
        while par[x] != x:
            par[x] = par[par[x]]; x = par[x]
        return x
    for v in vs:
        for i in range(D):
            w = v ^ (1 << i)
            if w > v and w in S:
                a, b = f(v), f(w)
                if a == b: return False
                par[a] = b
    return True

def alpha(vs, adj):
    # exhaustive max independent set on small graph; vs list, adj dict of bitmasks over indices
    n = len(vs)
    best = 0
    def rec(cand, size):
        nonlocal best
        if cand == 0:
            if size > best: best = size
            return
        if size + bin(cand).count("1") <= best: return
        i = (cand & -cand).bit_length() - 1
        rec(cand & ~(1 << i) & ~adj[i], size + 1)
        rec(cand & ~(1 << i), size)
    rec((1 << n) - 1, 0)
    return best

def tau(Mp):
    vs = list(Mp); n = len(vs)
    adj = [0] * n
    for a in range(n):
        for b in range(n):
            if a != b and wt(vs[a] ^ vs[b]) == 2: adj[a] |= 1 << b
    return n - alpha(vs, adj)

def tau_star(C, thr):
    """Returns (flag, witness): flag False iff some valid M' has tau(G_2[M']) > thr (witness returned);
    flag True certifies tau*(C) <= thr.  Branch and bound: tau(G_2[M' u R]) <= tau(G_2[M']) + |R|."""
    Cs = set(C)
    cand = sorted({o ^ (1 << i) for o in C for i in range(D)})
    bad = [None]
    def labels(Mp):
        # components of Q_9[Mp u (N_O(Mp) minus C)] -> dict vertex -> label (BFS)
        verts = set(Mp)
        for x in Mp:
            for i in range(D):
                w = x ^ (1 << i)
                if w not in Cs: verts.add(w)
        lab = {}; c = 0
        for v in verts:
            if v in lab: continue
            lab[v] = c; st = [v]
            while st:
                u = st.pop()
                for i in range(D):
                    w = u ^ (1 << i)
                    if w in verts and w not in lab: lab[w] = c; st.append(w)
            c += 1
        return lab
    def addable(x, lab):
        seen = set()
        for i in range(D):
            w = x ^ (1 << i)
            if w in Cs or w not in lab: continue
            l = lab[w]
            if l in seen: return False
            seen.add(l)
        return True
    def rec(start, Mp):
        if bad[0] is not None: return
        lab = labels(Mp)
        later = [idx for idx in range(start, len(cand)) if addable(cand[idx], lab)]
        t = tau(Mp)
        if t > thr: bad[0] = list(Mp); return
        if t + len(later) <= thr: return
        for idx in later:
            Mp.append(cand[idx]); rec(idx + 1, Mp); Mp.pop()
    rec(0, [])
    return bad[0] is None, bad[0]

def main():
    KMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 4
    o0 = 1
    layer = {canon([o0]): [o0]}
    worst_overall = []
    for k in range(1, KMAX + 1):
        if k > 1:
            new = {}
            for rep in layer.values():
                S = set(rep)
                for o in rep:
                    for d2 in DIST2:
                        w = o ^ d2
                        if w in S: continue
                        C2 = rep + [w]
                        key = canon(C2)
                        if key not in new: new[key] = C2
            layer = new
        cnt = 0; nviol = 0; wit = None
        for key, C in layer.items():
            ok, Mp = tau_star(C, k)
            cnt += 1
            if not ok:
                nviol += 1; wit = (C, Mp)
        print("k=%d classes=%d  clusters with tau*(C) > k: %d %s" % (k, cnt, nviol, "" if wit is None else "witness C=%s M'=%s" % wit), flush=True)
main()
