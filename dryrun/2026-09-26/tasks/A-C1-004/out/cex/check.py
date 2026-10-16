"""Referee A-C1-004: independent checks of proof A-C1-001 (lines in the plane). Stdlib only.

Angles in units of pi: a line is a in Q, rho(z) = dist(z, Z) (proof Step 3 rescaled), theta = rho(a-b).
g(z) = 1[rho(z) < 1/4].  All checks exact (fractions.Fraction) except:
  - check A (Step 4, arccos|cos| = rho) is a float sanity check (tolerance 1e-9), not load-bearing;
  - check F search runs in floats, and every best point found is re-evaluated EXACTLY on a rational rounding.
"""
import math, random, sys
from fractions import Fraction as F
from itertools import combinations_with_replacement

random.seed(20260926)

def frac_part(z):
    return z - (z.numerator // z.denominator)

def rho(z):
    z = frac_part(z)
    return min(z, 1 - z)

def g(z):
    return 1 if rho(z) < F(1, 4) else 0

def S_exact(a):
    n = len(a)
    return sum((rho(a[i] - a[j]) for i in range(n) for j in range(i + 1, n)), F(0))

def bound(N):
    return F(N * N // 4, 2)

def integral_exact(fun, centers, lo, hi):
    """Exact integral over [lo,hi] of a function that is constant between breakpoints c +- 1/4 + Z."""
    pts = {lo, hi}
    for c in centers:
        for s in (F(1, 4), F(-1, 4)):
            p = c + s
            base = p - (p.numerator // p.denominator)  # in [0,1)
            k = (lo - base).__floor__() - 1
            while base + k <= hi:
                q = base + k
                if lo < q < hi:
                    pts.add(q)
                k += 1
    pts = sorted(pts)
    tot = F(0)
    for u, v in zip(pts, pts[1:]):
        if v > u:
            tot += (v - u) * fun((u + v) / 2)
    return tot

def rand_rat(lo, hi, maxden=97):
    d = random.randint(1, maxden)
    return F(random.randint(math.floor(lo * d), math.ceil(hi * d)), d)

out = []
def log(s):
    print(s); sys.stdout.flush()

# A. Step 4 float sanity
worst = 0.0
for _ in range(200000):
    a = random.uniform(-10, 10); b = random.uniform(-10, 10)
    lhs = math.acos(min(1.0, abs(math.cos(a - b))))
    z = (a - b) / math.pi
    r = abs(z - round(z)) * math.pi
    worst = max(worst, abs(lhs - r))
log(f"A Step4 float sanity: 200000 random (a,b) in [-10,10]^2, max |arccos|cos(a-b)| - rho(a-b)| = {worst:.3e} (tol 1e-9) {'OK' if worst < 1e-9 else 'FAIL'}")

# B. Step 7 overlap lemma exact: int_{-1/2}^{1/2} g(s) g(s-th) ds = 1/2 - th, th in [0,1/2]
badB = 0; nB = 0
for D in range(1, 61):
    for k in range(0, D // 2 + 1):
        th = F(k, D)
        if th > F(1, 2):
            continue
        val = integral_exact(lambda s: g(s) * g(s - th), [F(0), th], F(-1, 2), F(1, 2))
        nB += 1
        if val != F(1, 2) - th:
            badB += 1
log(f"B Step7 exact: all theta = k/D in [0,1/2], D=1..60 ({nB} values), failures = {badB}")

# C. Step 8 cut identity exact, x,y random rationals in [-3,3] (Step 8 claims all real x,y)
badC = 0
for _ in range(3000):
    x = rand_rat(-3, 3); y = rand_rat(-3, 3)
    val = integral_exact(lambda t: abs(g(t - x) - g(t - y)), [x, y], F(0), F(1))
    if val != 2 * rho(x - y):
        badC += 1
log(f"C Step8 exact: 3000 random rational (x,y) in [-3,3]^2, den<=97, failures = {badC}")

# D. Step 10+11 exact: S == (1/2) int_0^1 k(t)(N-k(t)) dt and S <= bound, random rational configs
badD = 0; viol = 0
for _ in range(1500):
    N = random.randint(0, 14)
    a = [rand_rat(0, 1, 60) for _ in range(N)]
    if N >= 2 and random.random() < 0.3:
        a[1] = a[0]  # force repetitions
    def kN(t):
        k = sum(g(t - ai) for ai in a)
        return k * (N - k)
    def pair_sum(t):
        return sum(abs(g(t - a[i]) - g(t - a[j])) for i in range(N) for j in range(i + 1, N))
    I = integral_exact(kN, a, F(0), F(1))
    S = S_exact(a)
    # Step 10 pointwise at a few random rational t
    for _ in range(3):
        t = rand_rat(0, 1, 199)
        if pair_sum(t) != kN(t):
            badD += 1
    if S != I / 2:
        badD += 1
    if S > bound(N):
        viol += 1
log(f"D Steps10-11 exact: 1500 random rational configs N=0..14 (30% with forced repeat), identity failures = {badD}, bound violations = {viol}")

# E. Step 9 exhaustive
badE = 0
for N in range(0, 301):
    for k in range(-20, N + 21):
        if k * (N - k) > N * N // 4:
            badE += 1
log(f"E Step9: N=0..300, k=-20..N+20, failures = {badE}")

# G. exhaustive exact grid D=12, N<=8 (includes perpendicular pairs, repeats)
grid = [F(k, 12) for k in range(12)]
for N in range(0, 9):
    best = F(-1); arg = None
    for conf in combinations_with_replacement(grid, N):
        s = S_exact(conf)
        if s > best:
            best, arg = s, conf
    log(f"G exhaustive grid D=12 N={N}: max S/pi = {best}, bound = {bound(N)}, {'<=' if best <= bound(N) else 'VIOLATION'}, eq={best == bound(N)}")

# F. float local search (coordinate hill-climb from random starts), best re-certified exactly
def S_float(a):
    n = len(a); s = 0.0
    for i in range(n):
        for j in range(i + 1, n):
            z = a[i] - a[j]; z -= math.floor(z)
            s += min(z, 1 - z)
    return s
for N in range(2, 13):
    bestS = -1.0; bestA = None
    for start in range(40):
        a = [random.random() for _ in range(N)]
        cur = S_float(a); step = 0.25
        while step > 1e-7:
            improved = False
            for i in range(N):
                for d in (step, -step):
                    old = a[i]; a[i] = old + d
                    v = S_float(a)
                    if v > cur + 1e-15:
                        cur = v; improved = True
                    else:
                        a[i] = old
            if not improved:
                step /= 2
        if cur > bestS:
            bestS, bestA = cur, a[:]
    ra = [F(x).limit_denominator(10**6) for x in bestA]
    se = S_exact(ra)
    log(f"F local search N={N}: best float S/pi = {bestS:.12f}, bound = {float(bound(N))}, exact S/pi at rational rounding = {float(se):.12f}, exact <= bound: {se <= bound(N)}")

# H. equality configurations and tightness of the proof chain
badH = 0
for N in range(1, 31):
    m = N // 2
    c = rand_rat(-2, 2, 50)
    a = [c] * m + [c + F(1, 2)] * (N - m)
    if S_exact(a) != bound(N):
        badH += 1
    # tightness: k(t)(N-k(t)) = floor(N^2/4) except at finitely many t -> integral equals pi*floor(N^2/4)
    I = integral_exact(lambda t: (lambda k: k * (N - k))(sum(g(t - ai) for ai in a)), [c, c + F(1, 2)], F(0), F(1))
    if I != N * N // 4:
        badH += 1
log(f"H equality: balanced split (floor(N/2) on c, ceil(N/2) on c+1/2), N=1..30, random rational rotation c; S == bound and int k(N-k) == floor(N^2/4) exactly; failures = {badH}")
# S6 values
for N, want in [(2, F(1, 2)), (3, F(1)), (4, F(2)), (5, F(3))]:
    m = N // 2
    a = [F(0)] * m + [F(1, 2)] * (N - m)
    log(f"S6 N={N}: S/pi = {S_exact(a)} (expected {want}) {'OK' if S_exact(a) == want else 'FAIL'}")
