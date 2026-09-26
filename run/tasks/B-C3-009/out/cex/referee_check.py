#!/usr/bin/env python3
"""Referee's independent checks for B-C3(b) lower half (stdlib only, exact integers).
Usage: python3 referee_check.py KEX KORB KL NRAND
 1. Exhaustive d_B (definition: first index whose element recurs) for every partition of every n<=T_KEX:
    check (a) for non-triangular n, rank 4..KEX; D_B(T_k-1) vs k^2-2k-1; maximiser counts; d_B(lambda*_k);
    cyclic set vs Cell-1 characterisation (delta_{k-1} + r cells of diagonal k-1).
 2. Witness orbit by definition for 3<=k<=KORB: d_B(lambda*_k) == k^2-2k-1, and every iterate before entry
    equals Lambda({0,1}+t, (k+t) mod (k+1)) (proof step 4.2).
 3. Lemma R4 closed formula vs d_B by definition for every case-B partition, 3<=k<=KL, 2<=r<=k-1.
 4. Lemma R1 / Cor 1.4 on NRAND random partitions (energy equality iff lambda_1<=s+1, and R(C)=C(B)).
"""
import sys, random
from itertools import combinations

def B(l):
    s = len(l)
    return tuple(sorted([x-1 for x in l if x > 1] + [s], reverse=True))

def dB_def(l):
    seen = {}; x = l; i = 0
    while x not in seen:
        seen[x] = i; x = B(x); i += 1
    return seen[x]          # index of first orbit element that lies on the cycle

def parts(n, m=None):
    if m is None: m = n
    if n == 0: yield (); return
    for p in range(min(n, m), 0, -1):
        for r in parts(n-p, p): yield (p,)+r

T = lambda k: k*(k+1)//2
def rank(n):
    k = 1
    while T(k) < n: k += 1
    return k

def cell1_cyclic(l, n):
    k = rank(n)
    rows = list(l) + [0]*(k+2)
    for i in range(k):
        if rows[i] - (k-1-i) not in (0, 1): return False
    return all(x == 0 for x in rows[k:])

def energy(l):
    return sum(i*li + li*(li-1)//2 for i, li in enumerate(l))

def lamstar(k):
    rows = [k-1, k-2] + [k-i for i in range(2, k)] + [1]
    return tuple(rows)

def Lam(H, c, k):
    rows = [k-1-i + (0 if i in H else 1) for i in range(k)] + [0]
    rows[c] += 1
    assert rows == sorted(rows, reverse=True)
    return tuple(x for x in rows if x > 0)

def part1(KEX):
    ok = True
    for n in range(1, T(KEX)+1):
        P = list(parts(n))
        # memoised d_B via functional graph
        nxt = {p: B(p) for p in P}
        cyc = set()
        for p in P:
            # p cyclic iff returns to itself within |P| steps; do cheaper: Floyd-free marking
            pass
        state = {}
        for p in P:
            if p in state: continue
            path = []; x = p
            while x not in state:
                state[x] = len(path); path.append(x); x = nxt[x]
                if x in state and state[x] is not None and x in path[-1:] + path: break
            # mark
            if x in path:
                j = path.index(x)
                for y in path[j:]: cyc.add(y)
            for y in path: state[y] = None
        d = {}
        for p in cyc: d[p] = 0
        for p in P:
            stack = []; x = p
            while x not in d: stack.append(x); x = nxt[x]
            v = d[x]
            for y in reversed(stack): v += 1; d[y] = v
        k = rank(n)
        # cyclic set vs Cell 1
        for p in P:
            if (p in cyc) != cell1_cyclic(p, n):
                print("CELL1 MISMATCH", n, p); ok = False
        D = max(d.values())
        if n != T(k) and k >= 4 and D > k*k-2*k-1:
            print("FAIL (a)", n, k, D); ok = False
        if n == T(k)-1 and k >= 3:
            ls = lamstar(k); assert sum(ls) == n
            mx = sum(1 for p in P if d[p] == D)
            print(f"k={k} n={n} p(n)={len(P)} D_B={D} F={k*k-2*k-1} d(lam*)={d[ls]} dB_def(lam*)={dB_def(ls)} #max={mx}")
            if d[ls] != k*k-2*k-1 or dB_def(ls) != d[ls]: ok = False; print("FAIL lam*", k)
            if D < k*k-2*k-1: ok = False; print("FAIL lower bound", k)
        if n != T(k) and k >= 4:
            pass
    print("PART1", "OK" if ok else "FAIL")
    return ok

def part2(KORB):
    ok = True
    for k in range(3, KORB+1):
        ls = lamstar(k); n = T(k)-1
        assert sum(ls) == n and list(ls) == sorted(ls, reverse=True)
        F = k*k-2*k-1
        d = dB_def(ls)
        x = ls
        for t in range(F):
            H = {(0+t) % k, (1+t) % k}; c = (k+t) % (k+1)
            if x != Lam(H, c, k): ok = False; print("ORBIT SHAPE FAIL", k, t); break
            if cell1_cyclic(x, n): ok = False; print("CYCLIC TOO EARLY", k, t); break
            x = B(x)
        if not cell1_cyclic(x, n): ok = False; print("NOT CYCLIC AT F", k)
        if d != F: ok = False; print("dB FAIL", k, d, F)
    print("PART2 k=3..%d" % KORB, "OK" if ok else "FAIL")
    return ok

def part3(KL):
    ok = True; cnt = 0
    for k in range(3, KL+1):
        for r in range(2, k):
            h = k-r+1
            for c in range(k+1):
                for H in combinations(range(k), h):
                    if (c >= 1 and c-1 in H) or (c <= k-1 and c in H): continue
                    l = Lam(set(H), c, k)
                    pred = 1-c+(k+1)*min((c-1-a) % k for a in H)
                    if dB_def(l) != pred: ok = False; print("R4 FAIL", k, r, H, c)
                    cnt += 1
    print("PART3 k=3..%d: %d case-B partitions" % (KL, cnt), "OK" if ok else "FAIL")
    return ok

def part4(NRAND):
    rng = random.Random(12345); ok = True
    for _ in range(NRAND):
        n = rng.randint(1, 300)
        # random partition via random composition sorted
        cuts = sorted(rng.sample(range(1, n), rng.randint(0, min(n-1, 40)))) if n > 1 else []
        pts = [b-a for a, b in zip([0]+cuts, cuts+[n])]
        l = tuple(sorted(pts, reverse=True)); s = len(l)
        e0, e1 = energy(l), energy(B(l))
        if l[0] <= s+1:
            ell = [s] + [x-1 for x in l]
            if e0 != e1 or tuple(x for x in ell if x > 0) != B(l): ok = False; print("R1(i) FAIL", l)
        else:
            if e1 > e0-1: ok = False; print("R1(ii) FAIL", l)
    print("PART4 %d random partitions" % NRAND, "OK" if ok else "FAIL")
    return ok

if __name__ == "__main__":
    KEX, KORB, KL, NRAND = map(int, sys.argv[1:5])
    res = [part2(KORB), part3(KL), part4(NRAND), part1(KEX)]
    print("ALL OK" if all(res) else "SOME FAILED")
