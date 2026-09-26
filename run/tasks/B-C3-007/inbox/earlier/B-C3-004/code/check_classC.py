#!/usr/bin/env python3
"""Sanity check (stdlib only) of Lemma 2 (class-C dynamics) and Proposition 4 (class-C bound).
Class C_k: delta_{k-1} <= lambda <= delta_{k+1}, encoded by 0/1 vectors A (length k), Bv (length k+1),
row i = (k-i) + A[i-1] + Bv[i-1] (A[k] := 0).  For k = 3..K and all valid (A,Bv) with |A|+|Bv| <= k-1:
 (i) B(lambda) equals the predicted rotation (+ annihilation) of (A,Bv);
 (ii) d_B(lambda) <= k^2-2k-1 (cyclic test: lambda <= delta_k, by Cell 1).  Usage: python3 check_classC.py K"""
import sys
from itertools import product

def B(l):
    s = len(l); new = [x - 1 for x in l if x > 1]; new.append(s); new.sort(reverse=True); return tuple(new)

def part(k, A, Bv):
    rows = []
    for i in range(1, k + 2):
        a = A[i - 1] if i <= k else 0
        v = max(k - i, 0) + a + Bv[i - 1]
        rows.append(v)
    return tuple(x for x in rows if x > 0)

def valid(k, A, Bv):
    for q in range(k + 1):
        if Bv[q]:
            if q <= k - 1 and not A[q]: return False
            if q >= 1 and not A[q - 1]: return False
    return True

def step(k, A, Bv):
    drop = (A[k - 1] == 0 and Bv[0] == 1)
    A2 = [A[(x - 1) % k] for x in range(k)]
    B2 = [Bv[(q - 1) % (k + 1)] for q in range(k + 1)]
    if drop:
        A2[0] = 1; B2[1] = 0
    return A2, B2

def main(K):
    ok = True
    for k in range(3, K + 1):
        worst = 0; cnt = 0
        for A in product((0, 1), repeat=k):
            for Bv in product((0, 1), repeat=k + 1):
                if sum(A) + sum(Bv) > k - 1 or sum(A) + sum(Bv) == 0: continue
                if not valid(k, A, Bv): continue
                cnt += 1
                lam = part(k, A, Bv)
                A2, B2 = step(k, list(A), list(Bv))
                if B(lam) != part(k, A2, B2):
                    ok = False; print("dynamics mismatch", k, A, Bv)
                # depth: cyclic iff Bv == 0 (lambda inside delta_k)
                t = 0; a, b = list(A), list(Bv)
                while any(b):
                    a, b = step(k, a, b); t += 1
                worst = max(worst, t)
        good = worst <= k * k - 2 * k - 1
        ok &= good
        print(f"k={k} class-C configs={cnt} max d={worst} bound={k*k-2*k-1} {'OK' if good else 'VIOLATION'}")
    print("ALL CHECKS PASSED" if ok else "SOME CHECK FAILED")

if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 9)
