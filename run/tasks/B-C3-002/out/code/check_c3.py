#!/usr/bin/env python3
"""Exact exhaustive checks for B-C3 (stdlib only).
Usage: python3 check_c3.py K
  For every k in [2, K] and every n with T_{k-1} < n <= T_k - 1 computes D_B(n) by
  brute force over all partitions of n (cycle detection on the functional graph of B).
  Checks:
   (A) D_B(n) <= k^2-2k-1 for k >= 4 and T_{k-1} < n < T_k            [finite range only]
   (B) D_B(T_k - 1) = k^2-2k-1 for 4 <= k <= K; prints small-k values
   (C) lambda*_k = (k-1,k-2,k-2,k-3,...,2,1,1) attains it; lists maximizer count;
       for k>=6 checks {lambda: d=F} == {lambda: B^(k^2-4k-2)(lambda) = mu_k},
       mu_k = (k,k-1,k-1,k-3,k-4,...,3,1)
   (L) Lemma Phi1 closed formula: for every partition of n=T_{k-1}+r (2<=r<=k-1) of
       'case B' shape (delta_{k-1} full, one cell on diagonal k at row c, holes H on
       diagonal k-1), d = 1 - c + (k+1)*min_{a in H} ((c-1-a) mod k).
"""
import sys
from itertools import combinations

def partitions(n, maxp=None):
    if maxp is None: maxp = n
    if n == 0:
        yield (); return
    for p in range(min(n, maxp), 0, -1):
        for rest in partitions(n - p, p):
            yield (p,) + rest

def B(l):
    s = len(l)
    return tuple(sorted([x - 1 for x in l if x > 1] + [s], reverse=True))

def depths(n):
    P = list(partitions(n))
    nxt = {p: B(p) for p in P}
    cyc = set()
    state = {}  # 0 unvisited, 1 on stack, 2 done
    for p in P:
        if p in state: continue
        path = []; x = p
        while x not in state:
            state[x] = 1; path.append(x); x = nxt[x]
        if state[x] == 1:  # new cycle found, starting at x
            y = x
            while True:
                cyc.add(y); y = nxt[y]
                if y == x: break
        for y in path: state[y] = 2
    d = {p: 0 for p in cyc}
    for p in P:
        path = []; x = p
        while x not in d:
            path.append(x); x = nxt[x]
        v = d[x]
        for y in reversed(path):
            v += 1; d[y] = v
    return d

T = lambda k: k * (k + 1) // 2

def Bpow(l, m):
    for _ in range(m): l = B(l)
    return l

def main(K):
    ok = True
    for k in range(2, K + 1):
        for n in range(T(k - 1) + 1, T(k)):
            d = depths(n)
            D = max(d.values())
            F = k * k - 2 * k - 1
            if k >= 4 and D > F:
                print("FAIL (A)", k, n, D); ok = False
            if n == T(k) - 1:
                maxi = sorted(p for p in d if d[p] == D)
                line = f"k={k} n={n} D_B={D} k^2-2k-1={F} #maximizers={len(maxi)}"
                if k <= 5: line += f" maximizers={maxi}"
                print(line)
                if k >= 4:
                    if D != F: print("FAIL (B)", k); ok = False
                    lam = tuple([k - 1, k - 2] + list(range(k - 2, 0, -1)) + [1])
                    assert sum(lam) == n
                    if d[lam] != F: print("FAIL (C) lambda*", k); ok = False
                if k >= 6:
                    mu = tuple([k, k - 1, k - 1] + list(range(k - 3, 2, -1)) + [1])
                    assert sum(mu) == n
                    m = k * k - 4 * k - 2
                    S1 = set(maxi); S2 = set(p for p in d if Bpow(p, m) == mu)
                    print(f"   d(mu_k)={d[mu]} (2k+1={2*k+1}); trunk characterization holds: {S1 == S2}")
                    if S1 != S2 or d[mu] != 2 * k + 1: ok = False
            # (L) closed formula for case-B Phi=1 configurations
            r = n - T(k - 1)
            if k >= 3 and 2 <= r <= k - 1:
                h = k - r + 1
                cnt = 0
                for c in range(k + 1):
                    for H in combinations(range(k), h):
                        if (c >= 1 and c - 1 in H) or (c <= k - 1 and c in H): continue
                        rows = [k - 1 - i + (0 if i in H else 1) for i in range(k)] + [0]
                        rows[c] += 1
                        lam = tuple(x for x in rows if x > 0)
                        assert list(lam) == sorted(lam, reverse=True) and sum(lam) == n
                        pred = 1 - c + (k + 1) * min((c - 1 - a) % k for a in H)
                        if d[lam] != pred:
                            print("FAIL (L)", k, n, c, H, d[lam], pred); ok = False
                        cnt += 1
                print(f"   (L) k={k} n={n} r={r}: {cnt} case-B Phi=1 partitions match closed formula; max={(k+1)*(r-2)+2}")
        if k >= 4:
            print(f"k={k}: (A) checked for all n in ({T(k-1)},{T(k)})")
    print("ALL OK" if ok else "SOME CHECK FAILED")

if __name__ == "__main__":
    main(int(sys.argv[1]))
