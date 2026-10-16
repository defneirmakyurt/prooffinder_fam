# Clean-room CEX search for A-C2 (analysis lens). Exact rationals + arb ball arithmetic (python-flint, rigorous).
# Admissible m-chains <-> tridiagonal Gram G (1 on diag, c_i off-diag) PSD with rank <= m-1.
# Leading minors D_0=1, D_1=1, D_k = D_{k-1} - c_{k-1}^2 D_{k-2}.
# Generator: pick rational c_1..c_{m-2} with D_2..D_{m-1} > 0, then c_{m-1}^2 := D_{m-1}/D_{m-2}
# (det G = 0, G PSD of rank m-1 -> realisable in R^(m-1)); every such chain is admissible.
# Checks:
#  (T) target sum arccos|c_i| <= (m-2) pi/2: counts certified violations (ball entirely above bound).
#  (R) proof Step 4: reduced (m-1)-chain with c'^2 = c_{m-2}^2/(1-c_{m-1}^2) is admissible in dim m-2
#      (exact: its tridiagonal det = 0, leading minors D_0..D_{m-2} > 0, c'^2 <= 1).
#  (L) proof Step 5 on each instance: if a+b < pi/2 then arcsin(sqrt c'^2) <= a+b, counts certified failures.
#  (D) dimension trap: G = I_m (basis of R^m) exceeds the bound by exactly pi/2 (exact arithmetic).
import random, sys, time
from fractions import Fraction as F
import flint
flint.ctx.prec = 200
arb = flint.arb
random.seed(int(sys.argv[1]) if len(sys.argv) > 1 else 7)
PI = arb.pi()

def A(q): return arb(q.numerator) / q.denominator

def minors(sq):   # sq = list of c_i^2
    D = [F(1), F(1)]
    for k in range(2, len(sq) + 2):
        D.append(D[-1] - sq[k-2] * D[-2])
    return D

def gen(m, den):
    while True:
        c = []
        for i in range(m - 2):
            c.append(F(random.randint(-den, den), den))
            if minors([x*x for x in c])[-1] <= 0: break
        else:
            D = minors([x*x for x in c])
            return c, D[m-1] / D[m-2]

t0 = time.time()
ntot = nviol = nred = nlem = 0
minslack = None
for m in range(2, 10):
    for den in (2, 3, 5, 7, 12, 50, 1000):
        for _ in range(200):
            if m == 2: c, s2 = [], F(1)
            else: c, s2 = gen(m, den)
            ntot += 1
            absc = [A(abs(x)) for x in c] + [A(s2).sqrt()]
            S = sum((a.acos() for a in absc), arb(0))
            slack = (m - 2) * PI / 2 - S
            if slack < 0: nviol += 1; print("CERTIFIED VIOLATION", m, c, s2)
            lo = float(slack.lower())
            if minslack is None or lo < minslack[0]: minslack = (lo, m, c, s2)
            if m >= 3 and s2 < 1:
                last2 = c[-1]**2 / (1 - s2)
                sq = [x*x for x in c[:-1]] + [last2]
                D = minors(sq)            # D_0..D_{m-1} for the (m-1)-chain
                if not (D[m-1] == 0 and all(d > 0 for d in D[:m-1]) and last2 <= 1):
                    nred += 1; print("REDUCTION FAIL", m, c, s2)
                a = absc[-2].asin(); b = absc[-1].asin()
                if a + b < PI / 2:
                    ap = A(last2).sqrt().asin()
                    if ap > a + b: nlem += 1; print("LEMMA FAIL", m, c, s2)
trap = all((m - 1) * F(1, 2) - (m - 2) * F(1, 2) == F(1, 2) for m in range(2, 50))
print("instances:", ntot, "| certified target violations:", nviol,
      "| reduction failures:", nred, "| lemma certified failures:", nlem)
print("smallest certified lower bound of slack (bound - sum):", minslack[0], "at m =", minslack[1])
print("dimension trap: R^m basis exceeds bound by exactly pi/2 for m=2..49:", trap)
print("elapsed %.2fs" % (time.time() - t0))
