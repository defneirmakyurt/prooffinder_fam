"""Rigorous (python-flint arb, 200 bits) evaluation of T - pi/2 at the float minimisers saved by search.py (B).
The float coordinates are taken as exact dyadic rationals v_i (not renormalised); the lines spanned by v_i
form a genuine configuration, and T = sum_{i<j} arcsin(|<v_i,v_j>| / (|v_i||v_j|)) is enclosed by arb balls."""
import itertools
from flint import arb, ctx
ctx.prec = 200
for d in range(2, 7):
    xs = eval(open(f"bestB_d{d}.txt").read())
    vs = [[arb(t) for t in x] for x in xs]
    T = arb(0)
    for i, j in itertools.combinations(range(len(vs)), 2):
        ip = sum((a*b for a, b in zip(vs[i], vs[j])), arb(0))
        ni = sum((a*a for a in vs[i]), arb(0)).sqrt(); nj = sum((a*a for a in vs[j]), arb(0)).sqrt()
        g = abs(ip)/(ni*nj)
        if g > 1: g = arb(1)  # cannot happen for exact data; guard
        T += g.asin()
    diff = T - arb.pi()/2
    print(f"d={d}: T - pi/2 in {diff.str(12, radius=True)}; certified >= 0: {diff >= 0}; certified > 0: {diff > 0}")
