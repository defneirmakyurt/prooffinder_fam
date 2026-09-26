#!/usr/bin/env python3
"""clusters_q5.py -- H-C5-003, stdlib only.  Every G2-connected set K of s even words inside ONE Q_5
subcube of Q_9 (WLOG coordinates 0..4 free, the other 4 fixed at 0: coordinate permutations and
translations by even words are automorphisms preserving parity, so any subcube of dimension 5 containing an
even word can be moved there), for s in the given sizes.  Witnesses of K are then odd words of the same
subcube (an odd vertex outside it has at most one neighbour inside).  Prints how many K have
net(K) = |K| - delta(K) >= 2, and the witness-degree profile of some of them.
Pruning (exact): deleting Z lowers the cycle rank r = sum_W (deg-1) - |K| + comps by at most
sum_Z (deg - 1), so if the |K|-2 largest values of deg-1 sum to less than r, then delta(K) > |K| - 2.
Usage: clusters_q5.py s1 [s2 ...]"""
import sys
from itertools import combinations
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from clusters import acyclic

EV = [v for v in range(32) if bin(v).count("1") % 2 == 0]


def g2conn(K):
    K = list(K)
    seen = {K[0]}
    st = [K[0]]
    while st:
        x = st.pop()
        for y in K:
            if y not in seen and bin(x ^ y).count("1") == 2:
                seen.add(y)
                st.append(y)
    return len(seen) == len(K)


def main():
    for s in map(int, sys.argv[1:]):
        tot = 0
        good = []
        for K in combinations(EV, s):
            if 0 not in K:
                continue  # translation by an even word of the subcube puts 0 in K
            if not g2conn(K):
                continue
            tot += 1
            idx = {k: i for i, k in enumerate(K)}
            cnt = {}
            for k in K:
                for j in range(5):
                    cnt.setdefault(k ^ (1 << j), []).append(idx[k])
            W = [e for e in cnt.values() if len(e) >= 2]
            r0 = sum(len(e) - 1 for e in W) - s + 1
            top = sorted((len(e) - 1 for e in W), reverse=True)[:s - 2]
            if sum(top) < r0:
                continue
            found = False
            for r in range(s - 1):
                for Zs in combinations(range(len(W)), r):
                    zs = set(Zs)
                    if acyclic([W[i] for i in range(len(W)) if i not in zs], s):
                        found = True
                        good.append((K, r, sorted(len(e) for e in W)))
                        break
                if found:
                    break
        print("Q5 subcube, |K| = %d: %d G2-connected sets containing 0; net >= 2 for %d of them"
              % (s, tot, len(good)), flush=True)
        sup = {}
        for g in good:
            o = 0
            for k in g[0]:
                o |= k
            sup[bin(o).count("1")] = sup.get(bin(o).count("1"), 0) + 1
        print("   support sizes (number of coordinates used) of the net>=2 sets:", sorted(sup.items()))
        for g in good[:3]:
            print("   example K =", [format(k, "05b") for k in g[0]], "delta =", g[1], "witness degrees", g[2])


if __name__ == "__main__":
    main()
