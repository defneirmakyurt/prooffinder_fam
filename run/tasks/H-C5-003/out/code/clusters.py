#!/usr/bin/env python3
"""clusters.py -- H-C5-003, stdlib only.  Structural sub-search (rung R6).

Setting (proved in out/claims.md, "cluster reduction"): for an induced forest F of Q_9 put M = F n E (even
words kept), Z = S n O (odd words removed).  Then |S| = 256 - (|M| - |Z|).  A cluster is a connected
component K of the distance-2 graph on M.  An odd vertex adjacent to >= 2 words of M ("witness") has all
its M-neighbours in one cluster.  Inside a cluster, the witnesses not in Z must form a Berge-acyclic
hypergraph on K (hyperedge of witness o = its K-neighbours), otherwise G[F] has a cycle.
delta(K) := minimum number of witnesses of K to delete so that the rest is Berge-acyclic.
net(K) := |K| - delta(K) is the most K can contribute to |M| - |Z|.

This program enumerates, up to translation (by words of K) and coordinate permutation, every cluster K
(G2-connected set of even words of Q_9) with |K| <= SMAX, and prints the maximum of net(K) per size and
the clusters attaining net >= 2 (if any).
Usage: clusters.py SMAX
"""
import sys
from itertools import combinations, permutations

D = 9


def pc(x):
    return bin(x).count("1")


def canon(K):
    best = None
    Kl = list(K)
    for t in Kl:
        rows = [k ^ t for k in Kl if k != t]
        for perm in permutations(rows):
            cols = sorted((tuple((r >> c) & 1 for r in perm) for c in range(D)), reverse=True)
            key = tuple(cols)
            if best is None or key < best:
                best = key
    return best


def acyclic(hedges, nverts):
    par = list(range(nverts + len(hedges)))

    def find(x):
        while par[x] != x:
            par[x] = par[par[x]]
            x = par[x]
        return x
    for h, e in enumerate(hedges):
        node = nverts + h
        for v in e:
            a, b = find(node), find(v)
            if a == b:
                return False
            par[a] = b
    return True


def delta(K):
    Kl = sorted(K)
    idx = {k: i for i, k in enumerate(Kl)}
    cnt = {}
    for k in Kl:
        for j in range(D):
            o = k ^ (1 << j)
            cnt.setdefault(o, []).append(idx[k])
    W = [e for e in cnt.values() if len(e) >= 2]
    for r in range(len(W) + 1):
        for Zs in combinations(range(len(W)), r):
            zs = set(Zs)
            kept = [W[i] for i in range(len(W)) if i not in zs]
            if acyclic(kept, len(Kl)):
                return r, len(W)
    return len(W), len(W)


def main():
    smax = int(sys.argv[1])
    level = {canon({0}): {0}}
    for s in range(1, smax + 1):
        best = None
        good = []
        for key, K in level.items():
            dl, nw = delta(K)
            net = len(K) - dl
            if best is None or net > best:
                best = net
            if net >= 2:
                good.append((sorted(format(k, "09b") for k in K), dl, nw))
        print("size %d: %d clusters (up to symmetry), max net = %d, clusters with net >= 2: %d"
              % (s, len(level), best, len(good)), flush=True)
        for g in good[:5]:
            print("   net>=2 example:", g)
        if s == smax:
            break
        nxt = {}
        for K in level.values():
            for k in K:
                for i, j in combinations(range(D), 2):
                    w = k ^ (1 << i) ^ (1 << j)
                    if w in K:
                        continue
                    K2 = set(K)
                    K2.add(w)
                    c = canon(K2)
                    if c not in nxt:
                        nxt[c] = K2
        level = nxt


if __name__ == "__main__":
    main()
