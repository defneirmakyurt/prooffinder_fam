#!/usr/bin/env python3
"""check_indep_structure.py -- H-C5-006, stdlib only. SANITY CHECK (not part of any proof) of proof.md Lemma I:
for every INDEPENDENT decycling set S of Q_d, every component of Q_d - S is an isolated vertex or a star
K_{1,d} whose centre has all d neighbours outside S, the centres are pairwise at distance >= 4, and
|S| = 2^{d-1} - (#centres). Exhaustive over ALL independent sets of Q_d for d = 2..5 (backtracking)."""
import sys

def run(d):
    n = 1 << d
    nb = [[v ^ (1 << j) for j in range(d)] for v in range(n)]
    cnt_indep = cnt_dec = bad = 0
    minS = None
    inS = [False] * n

    def check():
        nonlocal cnt_dec, bad, minS
        F = [not inS[v] for v in range(n)]
        # forest test via union-find
        par = list(range(n))
        def f(x):
            while par[x] != x:
                par[x] = par[par[x]]; x = par[x]
            return x
        for v in range(n):
            if F[v]:
                for w in nb[v]:
                    if w > v and F[w]:
                        a, b = f(v), f(w)
                        if a == b:
                            return
                        par[a] = b
        cnt_dec += 1
        deg = [sum(F[w] for w in nb[v]) if F[v] else -1 for v in range(n)]
        centres = [v for v in range(n) if F[v] and deg[v] == d]
        ok = all(deg[v] in (0, 1, d) for v in range(n) if F[v])
        for c in centres:
            ok = ok and all(deg[w] == 1 for w in nb[c])
        for v in range(n):  # every degree-1 vertex is a leaf of a centre
            if F[v] and deg[v] == 1:
                w = next(w for w in nb[v] if F[w])
                ok = ok and deg[w] == d
        for i in range(len(centres)):
            for j in range(i + 1, len(centres)):
                ok = ok and bin(centres[i] ^ centres[j]).count("1") >= 4
        s = sum(inS)
        ok = ok and s == (n >> 1) - len(centres)
        if not ok:
            bad += 1
        if minS is None or s < minS:
            minS = s

    def rec(v):
        nonlocal cnt_indep
        if v == n:
            cnt_indep += 1
            check()
            return
        rec(v + 1)                      # v not in S
        if not any(inS[w] for w in nb[v] if w < v):
            inS[v] = True
            rec(v + 1)
            inS[v] = False
    rec(0)
    print("d=%d independent sets=%d independent decycling sets=%d violations=%d min |S| (independent)=%s"
          % (d, cnt_indep, cnt_dec, bad, minS))

for d in range(2, 6):
    run(d)
