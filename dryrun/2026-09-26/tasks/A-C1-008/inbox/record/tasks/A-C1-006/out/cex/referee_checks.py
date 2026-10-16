"""Referee checks for A-C1 (lines in the plane). Stdlib only.
Angles in units of pi: a line is a in R (mod 1), rho(z) = dist(z, Z), g(z) = 1[rho(z) < 1/4].
Exact parts use fractions.Fraction. Float parts are exploratory only (flagged as such).
"""
from fractions import Fraction as F
from itertools import combinations_with_replacement
import math, random, sys

random.seed(20260926)

def frac_mod1(z):
    return z - (z.numerator // z.denominator)

def rho(z):
    z = frac_mod1(z)
    return min(z, 1 - z)

def g(z):
    return 1 if rho(z) < F(1, 4) else 0

def breakpoints(centers, lo, hi):
    """all points c +- 1/4 + k (k integer) inside [lo, hi], plus lo, hi"""
    pts = {lo, hi}
    for c in centers:
        for s in (F(1, 4), -F(1, 4)):
            p = c + s
            k0 = (lo - p).__floor__() - 1
            q = p + k0
            while q <= hi:
                if q >= lo:
                    pts.add(q)
                q += 1
    return sorted(pts)

def integrate(fun, centers, lo, hi):
    """exact integral over [lo,hi] of a function piecewise constant between breakpoints"""
    pts = breakpoints(centers, lo, hi)
    tot = F(0)
    for a, b in zip(pts, pts[1:]):
        if b > a:
            tot += (b - a) * fun((a + b) / 2)
    return tot

def rand_frac(maxden=997, span=5):
    d = random.randint(1, maxden)
    return F(random.randint(-span * d, span * d), d)

def check_step8(trials):
    bad = 0
    for _ in range(trials):
        x, y = rand_frac(), rand_frac()
        val = integrate(lambda t: abs(g(t - x) - g(t - y)), [x, y], F(0), F(1))
        if val != 2 * rho(x - y):
            bad += 1
    # extremal: rho(x-y) in {0, 1/4, 1/2}, differences exactly at breakpoints
    for x in [F(0), F(1, 4), F(-3, 4), F(7, 3)]:
        for dlt in [F(0), F(1, 4), F(1, 2), F(-1, 2), F(3, 4), F(1), F(-5, 4)]:
            y = x + dlt
            val = integrate(lambda t: abs(g(t - x) - g(t - y)), [x, y], F(0), F(1))
            if val != 2 * rho(x - y):
                bad += 1
    return bad

def check_step7(trials):
    bad = 0
    thetas = [F(0), F(1, 4), F(1, 2)] + [F(random.randint(0, 500), 1000) for _ in range(trials)]
    for th in thetas:
        val = integrate(lambda s: g(s) * g(s - th), [F(0), th], F(-1, 2), F(1, 2))
        if val != F(1, 2) - th:
            bad += 1
    return bad, len(thetas)

def check_step11(trials, Nmax):
    """S/pi == (1/2) int_0^1 k(t)(N-k(t)) dt exactly, and <= floor(N^2/4)/2"""
    bad_id = bad_bd = 0
    for _ in range(trials):
        N = random.randint(0, Nmax)
        a = [rand_frac(60, 2) for _ in range(N)]
        if random.random() < 0.3 and N:
            a = [random.choice(a) for _ in range(N)]  # force repetitions
        S = sum((rho(a[i] - a[j]) for i in range(N) for j in range(i + 1, N)), F(0))
        def kk(t):
            k = sum(g(t - ai) for ai in a)
            return k * (N - k)
        I = integrate(kk, a, F(0), F(1)) / 2
        if I != S:
            bad_id += 1
        if S > F(N * N // 4, 2):
            bad_bd += 1
    return bad_id, bad_bd

def check_step9(Nmax, K):
    bad = 0
    for N in range(0, Nmax + 1):
        for k in range(-K, Nmax + K + 1):
            if k * (N - k) > N * N // 4:
                bad += 1
    return bad

def check_step4(trials):
    """float sanity: arccos|cos(pi z)| == pi*rho(z)"""
    worst = 0.0
    for _ in range(trials):
        z = random.uniform(-20, 20)
        zf = F(z)
        lhs = math.acos(min(1.0, abs(math.cos(math.pi * z))))
        rhs = math.pi * float(rho(zf))
        worst = max(worst, abs(lhs - rhs))
    return worst

def grid_exhaustive(Nmax, D):
    out = []
    grid = [F(k, D) for k in range(D)]
    for N in range(0, Nmax + 1):
        best = F(-1); viol = 0
        for conf in combinations_with_replacement(grid, N):
            S = sum((rho(conf[i] - conf[j]) for i in range(N) for j in range(i + 1, N)), F(0))
            if S > F(N * N // 4, 2):
                viol += 1
            best = max(best, S)
        out.append((N, best, F(N * N // 4, 2), viol))
    return out

def float_ascent(Nmax, restarts, iters):
    """exploratory (floating point, NOT a proof): maximise S/bound by random local search"""
    res = []
    for N in range(2, Nmax + 1):
        bound = (N * N // 4) / 2
        best = 0.0
        for _ in range(restarts):
            a = [random.random() for _ in range(N)]
            def S(a):
                s = 0.0
                for i in range(N):
                    for j in range(i + 1, N):
                        d = (a[i] - a[j]) % 1.0
                        s += min(d, 1 - d)
                return s
            cur = S(a); step = 0.25
            for it in range(iters):
                i = random.randrange(N)
                old = a[i]
                a[i] = (old + random.uniform(-step, step)) % 1.0
                new = S(a)
                if new >= cur:
                    cur = new
                else:
                    a[i] = old
                if it % 200 == 199:
                    step *= 0.7
            best = max(best, cur)
        res.append((N, best, bound, best / bound))
    return res

def main():
    T = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
    b8 = check_step8(T)
    print(f"step8 cut identity: {T}+28 exact rational (x,y) pairs, denominators<=997, |x|,|y|<=5: failures={b8}")
    b7, n7 = check_step7(T // 3)
    print(f"step7 overlap lemma: {n7} exact rational theta in [0,1/2] (units of pi): failures={b7}")
    bi, bb = check_step11(T // 3, 12)
    print(f"step11 identity S = (1/2)int k(N-k): {T//3} exact random configs N<=12 (30% with forced repeats): identity failures={bi}, bound violations={bb}")
    b9 = check_step9(300, 100)
    print(f"step9 k(N-k)<=floor(N^2/4): N in 0..300, k in -100..400: failures={b9}")
    w4 = check_step4(T)
    print(f"step4 (float sanity only): max |arccos|cos(pi z)| - pi rho(z)| over {T} z in [-20,20] = {w4:.3e}")
    for N, best, bound, viol in grid_exhaustive(7, 12):
        print(f"grid D=12 exhaustive exact: N={N} max S/pi={best} bound={bound} violations={viol} attained={best==bound}")
    for N, best, bound, r in float_ascent(12, 20, 2000):
        print(f"float ascent (exploratory): N={N} best S/pi={best:.9f} bound={bound} ratio={r:.9f}")

if __name__ == "__main__":
    main()
