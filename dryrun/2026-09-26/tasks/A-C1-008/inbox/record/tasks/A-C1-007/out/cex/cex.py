"""Referee A-C1-007: independent checks of A-C1-003's proof. stdlib only.
Angles in units of pi. Exact parts use fractions.Fraction / integers; the float part (P6) is exploratory only.
P1  Step 0.5: k(N-k) <= floor(N^2/4) for all integers k in [-60,60], N in [0,120] (exact ints).
P2  Step B1 / 0.3: rho(z)+rho(z-1/2)=1/2 and rho(z)=|z| on [-1/2,1/2] for random rationals (exact).
P3  Step B2: S = (N-1)/2 + S(rest) for random rational configs containing a perpendicular pair (exact).
P4  Steps A2-A4: cut identity and S = (1/2) int_0^1 k(t)(N-k(t)) dt for random rational configs (exact, breakpoints).
P5  Target on integer grids {k/D}: exact max of S over all multisets vs floor(N^2/4)/2; and on grid maximisers
    attaining the bound: structural claims of B4 (no perp pair => no coincidence, P=Q) and B5 (rotation keeps max),
    and parity consequence (N even => every maximiser has a perpendicular pair).
P6  Float random search + coordinate hill-climbing, N<=16 (exploratory; not a proof of anything).
"""
import sys, random, math
from fractions import Fraction as F
from itertools import combinations

random.seed(20260926)

def rho(z):  # distance to Z (units of pi), exact
    z = z - (z.numerator // z.denominator)
    return min(z, 1 - z)

def S(a):
    return sum((rho(a[i] - a[j]) for i, j in combinations(range(len(a)), 2)), F(0))

def rand_rat():
    den = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 12, 24, 97, 1000])
    return F(random.randint(-5 * den, 5 * den), den)

def chi(u):
    u = u - (u.numerator // u.denominator)
    return 1 if u < F(1, 2) else 0

def breakpoints(a):
    pts = {F(0), F(1)}
    for c in a:
        for s in (c, c - F(1, 2)):
            pts.add(s - (s.numerator // s.denominator))
    return sorted(pts)

def P1():
    bad = 0
    for N in range(0, 121):
        for k in range(-60, 61):
            if k * (N - k) > (N * N) // 4:
                bad += 1
    print(f"P1 step0.5 k(N-k)<=floor(N^2/4): N in 0..120, k in -60..60, failures={bad}")
    return bad == 0

def P2(T=20000):
    bad = 0
    for _ in range(T):
        z = rand_rat()
        if rho(z) + rho(z - F(1, 2)) != F(1, 2):
            bad += 1
        if abs(z) <= F(1, 2) and rho(z) != abs(z):
            bad += 1
        if not (0 <= rho(z) <= F(1, 2)) or rho(-z) != rho(z) or rho(z + 1) != rho(z):
            bad += 1
    print(f"P2 B1/0.3 identities: {T} random rationals, failures={bad}")
    return bad == 0

def P3(T=3000):
    bad = 0
    for _ in range(T):
        N = random.randint(2, 9)
        a = [rand_rat() for _ in range(N)]
        p, q = random.sample(range(N), 2)
        a[q] = a[p] + F(1, 2) + random.randint(-3, 3)
        rest = [a[i] for i in range(N) if i not in (p, q)]
        if S(a) != F(N - 1, 2) + S(rest):
            bad += 1
    print(f"P3 B2 removal identity: {T} random configs N in 2..9, failures={bad}")
    return bad == 0

def P4(T=1500):
    bad_cut = bad_sum = bad_bound = 0
    for _ in range(T):
        a, b = rand_rat(), rand_rat()
        pts = breakpoints([a, b])
        m = F(0)
        for lo, hi in zip(pts, pts[1:]):
            t = (lo + hi) / 2
            if chi(a - t) != chi(b - t):
                m += hi - lo
        if m != 2 * rho(a - b):
            bad_cut += 1
        N = random.randint(0, 10)
        c = [rand_rat() for _ in range(N)]
        pts = breakpoints(c)
        integ = F(0)
        for lo, hi in zip(pts, pts[1:]):
            t = (lo + hi) / 2
            k = sum(chi(x - t) for x in c)
            integ += (hi - lo) * k * (N - k)
        if S(c) != integ / 2:
            bad_sum += 1
        if S(c) > F((N * N) // 4, 2):
            bad_bound += 1
    print(f"P4 A2 cut identity: {T} random pairs, failures={bad_cut}; "
          f"A3/A4 S=(1/2)int k(N-k): {T} random configs N in 0..10, failures={bad_sum}; bound violations={bad_bound}")
    return bad_cut == bad_sum == bad_bound == 0

def compositions(N, D):
    # count vectors c[0..D-1], sum N, with c[0] >= 1 when N >= 1 (rotation normalisation: some line at angle 0)
    c = [0] * D
    def rec(i, left):
        if i == D - 1:
            c[i] = left
            yield c
            return
        lo = 1 if (i == 0 and N >= 1) else 0
        for v in range(lo, left + 1):
            c[i] = v
            yield from rec(i + 1, left - v)
    if D == 1:
        c[0] = N
        yield c
        return
    yield from rec(0, N)

def P5(plan):
    ok = True
    for D, NMAX in plan:
        r = [min(k % D, D - k % D) for k in range(D)]  # rho in units of pi/D
        for N in range(0, NMAX + 1):
            bound2D = ((N * N) // 4) * D  # 2*D*bound(in units of pi) -> compare 2*S_int
            best = -1; nmax = 0; b4bad = 0; b5bad = 0; evenbad = 0; nperp_free = 0
            for c in compositions(N, D):
                occ = [x for x in range(D) if c[x]]
                s = 0
                for i, x in enumerate(occ):
                    for y in occ[i + 1:]:
                        s += c[x] * c[y] * r[(y - x) % D]
                if s > best:
                    best = s; nmax = 0
                if 2 * s == bound2D:
                    nmax += 1
                    perp = (D % 2 == 0) and any(c[(x + D // 2) % D] for x in occ)
                    if not perp and N >= 2:
                        nperp_free += 1
                        if N % 2 == 0:
                            evenbad += 1
                        for x in occ:
                            # z_i representatives in (-D/2, D/2] of a_n - a_i, n at x
                            C = c[x] - 1
                            P = sum(c[y] for y in occ if y != x and 0 < ((x - y) % D) < D / 2)
                            Q = sum(c[y] for y in occ if y != x and ((x - y) % D) > D / 2)
                            if C != 0 or P != Q:
                                b4bad += 1
                        # B5 rotation: move one line at x by e* (in grid units, e* integral on grid) and recheck value
                        x = occ[-1]
                        zs = []
                        for y in occ:
                            m = c[y] - (1 if y == x else 0)
                            if m == 0:
                                continue
                            z = (x - y) % D
                            if z > D / 2:
                                z -= D
                            zs.append(z)
                        cand = [-z for z in zs if z < 0] + [F(D, 2) - z for z in zs if z > 0]
                        e = min(cand)
                        # exact value after moving one copy of x to x+e (e may be half-integer if D odd)
                        pts = []
                        for y in occ:
                            pts += [F(y)] * c[y]
                        pts.remove(F(x)); pts.append(F(x) + e)
                        s2 = sum((rho((pts[i] - pts[j]) / D) for i, j in combinations(range(N), 2)), F(0))
                        if 2 * D * s2 != bound2D:
                            b5bad += 1
            good = 2 * best <= bound2D
            ok &= good and b4bad == 0 and b5bad == 0 and evenbad == 0
            print(f"P5 D={D} N={N}: grid max S/pi = {F(best, D)}, bound = {F((N*N)//4, 2)}, "
                  f"{'OK' if good else 'VIOLATION'}; maximisers attaining bound={nmax} "
                  f"(perp-free={nperp_free}), B4 failures={b4bad}, B5 failures={b5bad}, even-N perp-free={evenbad}")
    return ok

def P6(Ns=range(2, 17), restarts=60):
    worst = 0.0
    for N in Ns:
        bound = (N * N // 4) / 2
        bestN = 0.0
        for _ in range(restarts):
            a = [random.random() for _ in range(N)]
            def val(a):
                s = 0.0
                for i in range(N):
                    for j in range(i + 1, N):
                        d = (a[i] - a[j]) % 1.0
                        s += min(d, 1 - d)
                return s
            v = val(a); step = 0.25
            while step > 1e-9:
                improved = False
                for i in range(N):
                    for sg in (1, -1):
                        old = a[i]; a[i] = old + sg * step
                        w = val(a)
                        if w > v + 1e-15:
                            v = w; improved = True
                        else:
                            a[i] = old
                if not improved:
                    step /= 2
            bestN = max(bestN, v)
        worst = max(worst, bestN - bound)
        print(f"P6 float N={N}: best found S/pi = {bestN:.12f}, bound = {bound}, excess = {bestN - bound:.3e}")
    print(f"P6 max excess over bound (float, exploratory) = {worst:.3e}")
    return worst < 1e-9

if __name__ == "__main__":
    which = sys.argv[1:] or ["P1", "P2", "P3", "P4", "P5", "P6"]
    res = {}
    if "P1" in which: res["P1"] = P1()
    if "P2" in which: res["P2"] = P2()
    if "P3" in which: res["P3"] = P3()
    if "P4" in which: res["P4"] = P4()
    if "P5" in which: res["P5"] = P5([(12, 10), (7, 12), (10, 10), (24, 6)])
    if "P6" in which: res["P6"] = P6()
    print("RESULTS:", res, "ALL OK" if all(res.values()) else "SOME FAILURE")
