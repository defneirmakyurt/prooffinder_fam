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

def tau_star(C):
    Cs = set(C)
    cand = sorted({o ^ (1 << i) for o in C for i in range(D)})
    best = [0, None]
    def local_set(Mp):
        s = set(Mp)
        for x in Mp:
            for i in range(D):
                w = x ^ (1 << i)
                if w not in Cs: s.add(w)
        return s
    def rec(start, Mp):
        maximal = True
        for idx in range(start, len(cand)):
            x = cand[idx]
            Mp.append(x)
            if acyclic(local_set(Mp)):
                rec(idx + 1, Mp)
            Mp.pop()
        # evaluate tau at every node whose set cannot be extended by any LATER candidate is not enough
        # for maximality, so evaluate at every node (tau is monotone, cost is small).
        t = tau(Mp)
        if t > best[0]: best[0] = t; best[1] = list(Mp)
    rec(0, [])
    return best[0], best[1]

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
        worst = None; cnt = 0; hist = {}
        for key, C in layer.items():
            t, Mp = tau_star(C)
            cnt += 1
            hist[t - k] = hist.get(t - k, 0) + 1
            if worst is None or t - k > worst[0]: worst = (t - k, C, Mp)
        print("k=%d classes=%d  histogram of tau*(C)-k: %s  max tau*(C)-k = %d  (witness C=%s M'=%s)"
              % (k, cnt, dict(sorted(hist.items())), worst[0], worst[1], worst[2]), flush=True)
main()
