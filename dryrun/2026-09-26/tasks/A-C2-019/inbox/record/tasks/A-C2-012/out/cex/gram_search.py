# Referee A-C2-012 (ALGEBRAIC lens). Stdlib only.
# An admissible chain x_1..x_m in R^(m-1) <=> Gram G = I + tridiag(c_1..c_{m-1}) that is PSD with rank <= m-1,
# i.e. PSD and det G = 0. Tridiagonal leading minors (continuant) depend only on s_i = c_i^2:
#   D_0 = 1, D_1 = 1, D_k = D_{k-1} - s_{k-1} D_{k-2}.
# Part A: exact rational s_1..s_{m-2}; s_{m-1} := D_{m-1}/D_{m-2} forces det = 0; keep if D_1..D_{m-1} > 0
#   (then G PSD, rank m-1) and s_{m-1} <= 1. Check sum asin(sqrt(s_i)) >= pi/2 (float, tolerance 1e-12;
#   any violation would be reported with its exact data).
# Part B: exact check of the proof's Step 4 in Gram terms (Schur complement): the reduced chain has squares
#   s_1..s_{m-3}, s' = s_{m-2}/(1 - s_{m-1}); verify its continuant determinant is exactly 0 (rank drops by 1)
#   and leading minors >= 0 (PSD), i.e. it is an admissible (m-1)-chain in R^(m-2).
# Part C: equality tuples (e1,e1,e2,...,e_{m-1}) and S4(c) in R^m (identity basis) evaluated exactly.
# Part D: Step-5 lemma sin a/cos b <= sin(a+b) on rational-tangent grid, exact: with t=tan a, u=tan b,
#   compare squares: sin^2 a / cos^2 b = t^2/(1+t^2)*(1+u^2) vs sin^2(a+b) = T^2/(1+T^2), T=(t+u)/(1-tu), tu<1.
import math, random, sys
from fractions import Fraction as F

def minors(s):  # s list of squares c_1^2..c_{n-1}^2 ; returns D_0..D_n
    D = [F(1), F(1)]
    for k in range(2, len(s) + 2):
        D.append(D[k-1] - s[k-2] * D[k-2])
    return D

random.seed(12)
tested = 0; worst = {}; viol = []
for m in range(3, 13):
    for _ in range(4000):
        s = [F(random.randint(0, 1000), random.randint(1000, 4000)) if random.random() > 0.1 else F(0)
             for _ in range(m - 2)]
        D = minors(s)  # D_0..D_{m-1}
        if any(d <= 0 for d in D[1:m]):
            continue
        last = D[m-1] / D[m-2]
        if last > 1:
            continue
        s2 = s + [last]
        Dm = minors(s2)
        assert Dm[m] == 0 and all(d >= 0 for d in Dm)
        tested += 1
        A = sum(math.asin(math.sqrt(x)) for x in s2)
        gap = A - math.pi/2
        worst[m] = min(worst.get(m, 9), gap)
        if gap < -1e-12:
            viol.append((m, s2))
        # Part B: Step 4 reduction, exact
        if last < 1:
            sp = s2[:m-3] + [s2[m-3] / (1 - last)]
            assert sp[-1] <= 1, "Cauchy-Schwarz for reduced chain"
            Dp = minors(sp)
            assert Dp[m-1] == 0, ("reduced det", m, s2)
            assert all(d >= 0 for d in Dp), ("reduced PSD", m, s2)
print("Part A/B: admissible exact Gram chains tested:", tested)
for m in sorted(worst):
    print("  m=%d  min(sum asin|c_i| - pi/2) = %.3e" % (m, worst[m]))
print("  violations (gap < -1e-12):", len(viol))
# Part C
for m in range(2, 9):
    s = [F(1)] + [F(0)] * (m - 2)            # (e1,e1,e2,...,e_{m-1})
    D = minors(s)
    assert D[m] == 0 and all(d >= 0 for d in D)
    thsum = sum(math.acos(math.sqrt(x)) for x in s)
    print("  Part C m=%d equality tuple: chain sum/(pi/2) = %.12f (bound %d)" % (m, thsum/(math.pi/2), m-2))
    sR = [F(0)] * (m - 1)                    # e_1..e_m in R^m: det = 1 != 0, so not realisable in R^(m-1)
    print("        identity basis det =", minors(sR)[m], "(nonzero -> rank m, excluded by dimension)")
# Part D
cnt = 0
for p in range(0, 60):
    for q in range(0, 60):
        t = F(p, 20); u = F(q, 20)
        if t * u >= 1:
            continue
        lhs = t*t/(1+t*t) * (1+u*u)
        T = (t+u)/(1-t*u)
        rhs = T*T/(1+T*T)
        assert lhs <= rhs, (t, u); cnt += 1
print("Part D: Step-5 lemma checked exactly on", cnt, "rational-tangent pairs: OK")
