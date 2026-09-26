"""Referee check of the number-theoretic steps of the proof (stdlib, exact integers).
(A) Prop. 7 step (2): for all 0<=d<d'<=40, 0<=x<=d, 0<=y<=d', build t exactly as the proof does
    (t0, c*, Bezout u, m, j, t) and verify (x+t) mod P == 0 and (y+t) mod Q == c* with 0<=c*<=Q-P,
    and that (0,d) <= (c*, d'-c*) componentwise.
(B) Step 6.4: |Fix(rho^j) cap W(k,r)| equals binom(g, rg/k) if (k/g)|r else 0, brute force, 1<=r<=k<=14.
(C) Step 6.5: #{0<=j<k: gcd(j,k)=g} = phi(k/g) for all g|k, k<=200.
"""
from math import gcd, comb
from itertools import combinations

def ext_gcd(a, b):
    if b == 0:
        return (a, 1, 0)
    g, u, v = ext_gcd(b, a % b)
    return (g, v, u - (a // b) * v)

def phi(m):
    return sum(1 for i in range(1, m + 1) if gcd(i, m) == 1)

cnt = 0
for d in range(0, 41):
    for dp in range(d + 1, 41):
        P, Q = d + 1, dp + 1
        g, u, v = ext_gcd(P, Q)
        assert u * P + v * Q == g == gcd(P, Q)
        assert g <= Q - P
        for x in range(d + 1):
            for y in range(dp + 1):
                t0 = (-x) % P
                cs = [c for c in range(0, Q - P + 1) if (c - y - t0) % g == 0]
                assert cs
                c = cs[0]
                m = (c - y - t0) // g
                j = (u * m) % Q
                assert (j * P - (c - y - t0)) % Q == 0
                t = t0 + j * P
                assert t >= 0 and (x + t) % P == 0 and (y + t) % Q == c
                assert 0 <= c and dp - c >= d
                cnt += 1
print("(A) Prop 7 time-choice verified for", cnt, "tuples (d<d'<=40)")

for k in range(1, 15):
    for r in range(1, k + 1):
        W = []
        for ones in combinations(range(k), r):
            e = [0] * k
            for a in ones:
                e[a] = 1
            W.append(tuple(e))
        for j in range(k):
            g = gcd(j, k)
            fix = sum(1 for e in W if tuple(e[(a - j) % k] for a in range(k)) == e)
            pred = comb(g, r * g // k) if r % (k // g) == 0 else 0
            assert fix == pred, (k, r, j, fix, pred)
print("(B) fixed-point counts verified for 1<=r<=k<=14, all j")

for k in range(1, 201):
    for g in range(1, k + 1):
        if k % g == 0:
            assert sum(1 for j in range(k) if gcd(j, k) == g) == phi(k // g)
print("(C) gcd-class counts verified for k<=200")
