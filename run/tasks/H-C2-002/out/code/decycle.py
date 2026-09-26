#!/usr/bin/env python3
"""
decycle.py -- exhaustive search for a decycling set of a given size in Q_d.
Python standard library only; exact.

Usage: python3 decycle.py d k [--no-edge-prune]
Answers: does Q_d have a set D of exactly k vertices such that Q_d - D (the subgraph
induced by the other vertices) has no cycle?  Prints FOUND <D> or NONE, plus node count.

Reduction / pruning used (each is proved in out/proof.md, Step 7):
  (i)  Q_d is vertex-transitive (x -> x XOR a is an automorphism), so if such a D exists,
       one exists containing vertex 0.  The search fixes 0 in D.
  (ii) Edge identity: if F = V - D induces a forest with c >= 1 components then
       (d-1)|D| = (d-2)2^(d-1) + c + e(D),  e(D) = #edges inside D.
       Hence e(D) <= (d-1)k - (d-2)2^(d-1) - 1.  Branches violating this are cut
       (disable with --no-edge-prune; used only as a cross-check on small d).
  (iii) Vertices are decided in the order 0,1,...,2^d-1.  When v is put in F, its
       neighbours already in F must lie in pairwise distinct components of F (else a
       cycle closes); tracked with a union-find with rollback.  This test is exact:
       adding v creates a cycle iff two of its earlier F-neighbours are already connected.
"""
import sys

def search(d, k, edge_prune=True):
    n = 1 << d
    nbrs = [[v ^ (1 << j) for j in range(d)] for v in range(n)]
    emax = (d - 1) * k - (d - 2) * (1 << (d - 1)) - 1 if edge_prune else 10**9
    if emax < 0:
        return None, 0
    side = [0] * n            # 0 undecided, 1 in D, 2 in F
    parent = list(range(n))
    size = [1] * n
    def find(x):
        while parent[x] != x:
            x = parent[x]
        return x
    nodes = [0]
    sys.setrecursionlimit(10000)
    def rec(v, nd, ed):
        nodes[0] += 1
        if nd > k:
            return None
        if nd + (n - v) < k:
            return None
        if v == n:
            return [u for u in range(n) if side[u] == 1] if nd == k else None
        # option A: v in D  (vertex 0 is forced into D)
        e_add = sum(1 for w in nbrs[v] if w < v and side[w] == 1)
        if nd + 1 <= k and ed + e_add <= emax:
            side[v] = 1
            r = rec(v + 1, nd + 1, ed + e_add)
            side[v] = 0
            if r is not None:
                return r
        if v == 0:
            return None
        # option B: v in F
        roots = []
        for w in nbrs[v]:
            if w < v and side[w] == 2:
                roots.append(find(w))
        if len(set(roots)) != len(roots):
            return None          # cycle would close
        side[v] = 2
        changes = []
        for r in roots:          # union v's singleton with each root (union by size)
            a, b = find(v), r
            if size[a] < size[b]:
                a, b = b, a
            parent[b] = a
            size[a] += size[b]
            changes.append((a, b))
        res = rec(v + 1, nd, ed)
        for a, b in reversed(changes):
            parent[b] = b
            size[a] -= size[b]
        side[v] = 0
        return res
    res = rec(0, 0, 0)
    return res, nodes[0]

def is_decycling(d, D):
    """Independent check: Q_d - D is a forest iff #edges = #vertices - #components."""
    n = 1 << d
    Dset = set(D)
    F = [v for v in range(n) if v not in Dset]
    Fs = set(F)
    edges = sum(1 for v in F for j in range(d) if (v ^ (1 << j)) in Fs) // 2
    seen, comps = set(), 0
    for s in F:
        if s in seen:
            continue
        comps += 1
        stack = [s]; seen.add(s)
        while stack:
            x = stack.pop()
            for j in range(d):
                y = x ^ (1 << j)
                if y in Fs and y not in seen:
                    seen.add(y); stack.append(y)
    return edges == len(F) - comps

if __name__ == "__main__":
    d, k = int(sys.argv[1]), int(sys.argv[2])
    ep = "--no-edge-prune" not in sys.argv
    D, nodes = search(d, k, ep)
    if D is None:
        print("d=%d k=%d edge_prune=%s: NONE (search nodes %d)" % (d, k, ep, nodes))
    else:
        print("d=%d k=%d edge_prune=%s: FOUND %s  independent-check=%s (search nodes %d)"
              % (d, k, ep, D, is_decycling(d, D), nodes))
