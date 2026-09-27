#!/usr/bin/env python3
"""Exact (stdlib-only, Fraction arithmetic) check of the polynomial/rational identities
used in Step 6 of out/proof.md.  Polynomials are dicts {exponent-tuple: Fraction}.
Variables are indexed 0,1,2,... ; each identity states which variables it uses."""
from fractions import Fraction as F
from itertools import product

NV = 3  # variables: 0 -> first, 1 -> second, 2 -> third

def const(c):
    return {(0,)*NV: F(c)} if c != 0 else {}
def var(i):
    e = [0]*NV; e[i] = 1
    return {tuple(e): F(1)}
def add(p, q):
    r = dict(p)
    for k, v in q.items():
        r[k] = r.get(k, F(0)) + v
        if r[k] == 0: del r[k]
    return r
def neg(p): return {k: -v for k, v in p.items()}
def sub(p, q): return add(p, neg(q))
def mul(p, q):
    r = {}
    for (k1, v1), (k2, v2) in product(p.items(), q.items()):
        k = tuple(a+b for a, b in zip(k1, k2))
        r[k] = r.get(k, F(0)) + v1*v2
        if r[k] == 0: del r[k]
    return r
def pw(p, n):
    r = const(1)
    for _ in range(n): r = mul(r, p)
    return r
def S(*ps):
    r = {}
    for p in ps: r = add(r, p)
    return r
def M(*ps):
    r = const(1)
    for p in ps: r = mul(r, p)
    return r

ok = True
def report(name, zero_poly):
    global ok
    good = (zero_poly == {})
    ok = ok and good
    print(("PASS " if good else "FAIL ") + name)

one = const(1)
# ---- (I2): with a = cos s, b = cos t:
#  (1 - a^2 b^2) + a (1 - b^2) + b (1 - a^2) == (1+a)(1+b)(1-ab)
a, b = var(0), var(1)
lhs = S(sub(one, M(a,a,b,b)), mul(a, sub(one, mul(b,b))), mul(b, sub(one, mul(a,a))))
rhs = M(add(one,a), add(one,b), sub(one, mul(a,b)))
report("I2  sin^2h + cos s sin^2t + cos t sin^2s = (1+cos s)(1+cos t)(1-cos s cos t)", sub(lhs, rhs))

# ---- (I1a),(I1b): sin^2 h - sin^2 s cos^2 t = sin^2 t ; sin^2 h - cos^2 s sin^2 t = sin^2 s
sin2h = sub(one, M(a,a,b,b))
report("I1a (1-a^2b^2) - (1-a^2)b^2 = 1-b^2", sub(sub(sin2h, mul(sub(one,mul(a,a)), mul(b,b))), sub(one, mul(b,b))))
report("I1b (1-a^2b^2) - a^2(1-b^2) = 1-a^2", sub(sub(sin2h, mul(mul(a,a), sub(one,mul(b,b)))), sub(one, mul(a,a))))

# ---- (I3): a = (1-P^2)/(1+P^2), b = (1-Q^2)/(1+Q^2) ;  (1-ab)/(1+ab) = (P^2+Q^2)/(1+P^2 Q^2).
# Clear denominators: with A = 1+P^2, B = 1+Q^2, a = (1-P^2)/A, b=(1-Q^2)/B:
#  (1-ab)/(1+ab) = (AB - (1-P^2)(1-Q^2)) / (AB + (1-P^2)(1-Q^2)); cross-multiply.
P, Q = var(0), var(1)
A_, B_ = add(one, mul(P,P)), add(one, mul(Q,Q))
num = sub(mul(A_,B_), mul(sub(one,mul(P,P)), sub(one,mul(Q,Q))))
den = add(mul(A_,B_), mul(sub(one,mul(P,P)), sub(one,mul(Q,Q))))
report("I3  tan^2(h/2) = (P^2+Q^2)/(1+P^2Q^2)  [num*(1+P^2Q^2) == den*(P^2+Q^2)]",
       sub(mul(num, add(one, M(P,P,Q,Q))), mul(den, add(mul(P,P), mul(Q,Q)))))
# also the half-angle facts cos x = (1-T^2)/(1+T^2), sin x = 2T/(1+T^2) give
#  sin s sin t / ((1+cos s)(1+cos t)) = P Q :  (2P/A)(2Q/B) / ((2/A)(2/B)) = PQ  -- immediate.

# ---- (I5): (P+Q)(1-KPQ) - (K+PQ)(1-PQ) == (P+Q-PQ+P^2Q^2) - K(1-PQ+P^2Q+PQ^2)
K = var(2)   # K = tan(h/2) in out/proof.md
PQ = mul(P,Q)
lhs = sub(mul(add(P,Q), sub(one, mul(K,PQ))), mul(add(K,PQ), sub(one,PQ)))
Lp = S(P, Q, neg(PQ), mul(PQ,PQ))
Rp = S(one, neg(PQ), M(P,P,Q), M(P,Q,Q))
report("I5  cross-multiplied tangent inequality rearrangement", sub(lhs, sub(Lp, mul(K, Rp))))

# ---- (I4): Lp^2 (1+P^2Q^2) - (P^2+Q^2) Rp^2 == P Q (1-P)(1-Q)(1+P^2)(1+Q^2)(P^2Q^2+P^2Q+PQ^2-PQ+2)
lhs = sub(mul(mul(Lp,Lp), add(one, mul(PQ,PQ))), mul(add(mul(P,P),mul(Q,Q)), mul(Rp,Rp)))
last = S(mul(PQ,PQ), M(P,P,Q), M(P,Q,Q), neg(PQ), const(2))
rhs = M(P, Q, sub(one,P), sub(one,Q), add(one,mul(P,P)), add(one,mul(Q,Q)), last)
report("I4  main factorisation", sub(lhs, rhs))

# ---- (I6) m=5 normal vector: n = (sp*sq, -cp*sq, cp*cq) is orthogonal to x2=(cp,sp,0), x3=(0,cq,sq),
# and |n|^2 = 1 - sp^2 cq^2, as polynomials in cp,sp,cq,sq modulo cp^2+sp^2=1, cq^2+sq^2=1.
# We check the orthogonalities (exact polynomial zero) and the norm identity after substituting sp^2 = 1-cp^2, sq^2=1-cq^2.
NV = 4
cp, sp, cq, sq = var(0), var(1), var(2), var(3)
n = [M(sp,sq), neg(M(cp,sq)), M(cp,cq)]
x2 = [cp, sp, {}]
x3 = [{}, cq, sq]
dot = lambda u, v: S(*[mul(ui, vi) for ui, vi in zip(u, v)])
report("I6a <n,x2> = 0", dot(n, x2))
report("I6b <n,x3> = 0", dot(n, x3))
def reduce_sq(p):
    # replace sp^2 -> 1 - cp^2 and sq^2 -> 1 - cq^2 repeatedly
    changed = True
    while changed:
        changed = False
        r = {}
        for k, v in p.items():
            k = list(k)
            if k[1] >= 2:
                k2 = list(k); k2[1] -= 2
                t1 = {tuple(k2): v}
                k3 = list(k2); k3[0] += 2
                t2 = {tuple(k3): -v}
                r = add(r, add(t1, t2)); changed = True
            elif k[3] >= 2:
                k2 = list(k); k2[3] -= 2
                t1 = {tuple(k2): v}
                k3 = list(k2); k3[2] += 2
                t2 = {tuple(k3): -v}
                r = add(r, add(t1, t2)); changed = True
            else:
                r = add(r, {tuple(k): v})
        p = r
    return p
report("I6c |n|^2 = 1 - sp^2 cq^2", reduce_sq(sub(dot(n, n), sub(const(1), M(sp,sp,cq,cq)))))

print("ALL PASS" if ok else "SOME FAILED")
