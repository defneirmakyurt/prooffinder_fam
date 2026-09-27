#!/usr/bin/env python3
"""Floating-point SANITY checks (evidence only; the proof does not rest on them).
(1) Formulas of Steps 7-9 of out/proof.md: D_5 = pi + Phi(p,q); for m = 6,
    D_6 = pi + Phi(q,r) + T1 + (A-A') + (B-B') and D_6 >= pi + Phi(q,r) + Phi(p,A').
(2) Random 5-cycles in R^3 and 6-cycles in R^4 built WITHOUT the Gram-Schmidt normal form
    (by successive orthogonality constraints) satisfy D >= pi.
stdlib only."""
import math, random
random.seed(12345)
asin = lambda x: math.asin(max(-1.0, min(1.0, x)))
def dot(u, v): return sum(a*b for a, b in zip(u, v))
def nrm(v):
    r = math.sqrt(dot(v, v)); return [a/r for a in v]
def Phi(p, q):
    W = math.sqrt(1 - math.sin(p)**2*math.cos(q)**2)
    return (asin(math.sin(p)*math.cos(q)) + asin(math.cos(p)*math.cos(q)/W)
            + asin(math.sin(p)*math.sin(q)/W) - p + q - math.pi/2)
def Dcyc(X):
    m = len(X); return sum(asin(abs(dot(X[i], X[(i+1) % m]))) for i in range(m))
def orth_err(X):
    m = len(X); e = 0.0
    for i in range(m):
        for j in range(i+1, m):
            if (j-i) % m not in (1, m-1): e = max(e, abs(dot(X[i], X[j])))
    return e
worst = {}
def upd(k, v):
    worst[k] = min(worst.get(k, 1e9), v)
T = 200000
for _ in range(T):
    p, q, r = [random.uniform(1e-3, math.pi/2-1e-3) for _ in range(3)]
    # m = 5 normal form
    W = math.sqrt(1 - math.sin(p)**2*math.cos(q)**2)
    X5 = [[1,0,0], [math.cos(p), math.sin(p), 0], [0, math.cos(q), math.sin(q)], [0,0,1],
          [math.sin(p)*math.sin(q)/W, -math.cos(p)*math.sin(q)/W, math.cos(p)*math.cos(q)/W]]
    assert orth_err(X5) < 1e-9
    upd('|D5 - pi - Phi(p,q)| (negated)', -abs(Dcyc(X5) - math.pi - Phi(p, q)))
    upd('Phi(p,q)', Phi(p, q))
    # m = 6 normal form
    W1 = math.sqrt(1 - math.sin(q)**2*math.cos(r)**2)
    y6 = [0, math.sin(q)*math.sin(r)/W1, -math.cos(q)*math.sin(r)/W1, math.cos(q)*math.cos(r)/W1]
    sA1 = math.sin(q)*math.sin(r)/W1; A1 = asin(sA1)
    sB1 = math.cos(q)*math.cos(r)/W1; B1 = asin(sB1)
    Wp = math.sqrt(1 - math.sin(p)**2*math.cos(A1)**2)
    x6 = [(math.sin(p)*sA1 - 0)/Wp] + [-math.cos(p)*c/Wp for c in y6[1:]]
    X6 = [[1,0,0,0], [math.cos(p), math.sin(p), 0, 0], [0, math.cos(q), math.sin(q), 0],
          [0, 0, math.cos(r), math.sin(r)], [0,0,0,1], x6]
    assert orth_err(X6) < 1e-9 and abs(dot(x6, x6) - 1) < 1e-9, (orth_err(X6), dot(x6,x6), p, q, r)
    D6 = Dcyc(X6)
    A = asin(abs(dot(x6, X6[0]))); B = asin(abs(dot(x6, X6[4])))
    T1 = asin(math.sin(p)*math.cos(q)) + q - p
    upd('|D6 - (pi+Phi(q,r)+T1+(A-A1)+(B-B1))| (negated)', -abs(D6 - (math.pi + Phi(q, r) + T1 + (A-A1) + (B-B1))))
    upd('D6 - pi - Phi(q,r) - Phi(p,A1)', D6 - math.pi - Phi(q, r) - Phi(p, A1))
    upd('A1 <= q slack', q - A1); upd('B1 <= pi/2 - A1 slack', math.pi/2 - A1 - B1)
    # random 5-cycle in R^3 without normal form
    g = lambda d: nrm([random.gauss(0, 1) for _ in range(d)])
    def perp(v, basis):
        # Gram-Schmidt v against an orthonormalised copy of basis
        ob = []
        for b in basis:
            w = list(b)
            for o in ob: c = dot(w, o); w = [a - c*oo for a, oo in zip(w, o)]
            ob.append(nrm(w))
        w = list(v)
        for o in ob: c = dot(w, o); w = [a - c*oo for a, oo in zip(w, o)]
        return nrm(w)
    x1, x2 = g(3), g(3); x3 = perp(g(3), [x1])
    x4 = perp(g(3), [x1, x2]); x5 = perp(g(3), [x2, x3])
    Y = [x1, x2, x3, x4, x5]; assert orth_err(Y) < 1e-9
    upd('random 5-cycle D - pi', Dcyc(Y) - math.pi)
    x1, x2 = g(4), g(4); x3 = perp(g(4), [x1]); x4 = perp(g(4), [x1, x2])
    x5 = perp(g(4), [x1, x2, x3]); x6 = perp(g(4), [x2, x3, x4])
    Y = [x1, x2, x3, x4, x5, x6]; assert orth_err(Y) < 1e-9
    upd('random 6-cycle D - pi', Dcyc(Y) - math.pi)
for k, v in worst.items(): print(f"min over {T} samples of {k}: {v:.3e}")
