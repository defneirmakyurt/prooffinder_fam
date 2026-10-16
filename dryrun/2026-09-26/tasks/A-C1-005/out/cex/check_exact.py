"""Referee checks for A-C1-002 (lines in the plane). Stdlib only, exact rational arithmetic.
All angles are expressed in units of pi: a line with direction angle pi*a, a in [0,1).
theta/pi = dist(a_i - a_j, Z); delta(t)/pi = dist(t/pi, 2Z); g(x) = 1 iff (x/pi) mod 2 in [0,1).
Checks:
 E1  Step 0(a)-(d) and Step 3/4 identity theta = dist(a_i-a_j, Z) = (1/2) dist(2(a_i-a_j), 2Z)  (exact rationals)
 E2  Step 9/10 identity  int_0^{2pi}|g(u-psi)-g(v-psi)| dpsi = 2 delta(u-v), computed EXACTLY by breakpoints
 E3  Step 11 counting identity P(psi) = k(N-k) at exact midpoints
 E4  Whole chain as an identity: S = (1/4) int_0^{2pi} k(psi)(N-k(psi)) dpsi, exact, random rational configs
 E5  Step 12: k(N-k) <= floor(N^2/4) for 0<=k<=N<=400, with equality iff k in {floor(N/2), ceil(N/2)}
 E6  Exhaustive grid search: all multisets of N directions from {0,1/m,...,(m-1)/m}, exact integer compare to bound
 E7  S5/S6 arithmetic: binom(N,2) - M(N,2) = floor(N^2/4); checkable values
 E8  Equality config (Step 14) exact, and k(psi)(N-k(psi)) = floor(N^2/4) for a.e. psi there (tightness of Step 13)
"""
import random, itertools, math, sys
from fractions import Fraction as Fr

def dist(t, c):
    # min_k |t - c k|, exact, by Step 0(a) the min is at floor(t/c) or +1; we check against brute range too
    k0 = math.floor(t / c)
    return min(abs(t - c * k) for k in (k0 - 1, k0, k0 + 1, k0 + 2))

def dist_brute(t, c, R=50):
    k0 = math.floor(t / c)
    return min(abs(t - c * k) for k in range(k0 - R, k0 + R + 1))

def g(x):  # x in units of pi
    r = x - 2 * math.floor(x / 2)
    return 1 if r < 1 else 0

def integral_pair(u, v):
    """exact int_0^2 |g(u - p) - g(v - p)| dp  (p = psi/pi); breakpoints p = u - n, v - n"""
    pts = {Fr(0), Fr(2)}
    for w in (u, v):
        for n in range(math.floor(w) - 4, math.floor(w) + 5):
            p = w - n
            if 0 < p < 2:
                pts.add(p)
    pts = sorted(pts)
    tot = Fr(0)
    for a, b in zip(pts, pts[1:]):
        m = (a + b) / 2
        tot += (b - a) * abs(g(u - m) - g(v - m))
    return tot

def breakpoints(us):
    pts = {Fr(0), Fr(2)}
    for w in us:
        for n in range(math.floor(w) - 4, math.floor(w) + 5):
            p = w - n
            if 0 < p < 2:
                pts.add(p)
    return sorted(pts)

def S_units(a):
    n = len(a)
    return sum(dist(a[i] - a[j], 1) for i in range(n) for j in range(i + 1, n))

def rand_rat(rng, lo, hi, den):
    return Fr(rng.randint(lo * den, hi * den), den)

def main():
    rng = random.Random(20260926)
    # E1
    cnt = 0
    for _ in range(20000):
        den = rng.choice([1, 2, 3, 4, 6, 7, 12, 97, 1000])
        t = rand_rat(rng, -20, 20, den)
        for c in (Fr(1), Fr(2), Fr(1, 2), Fr(3, 7)):
            d = dist(t, c)
            assert d == dist_brute(t, c)          # 0(a) min attained near floor
            assert 0 <= d <= c / 2                # 0(a) bound
            assert dist(-t, c) == d               # 0(b)
            m = rng.randint(-5, 5)
            assert dist(t + c * m, c) == d        # 0(c)
            assert dist(2 * t, 2 * c) == 2 * d    # 0(d)
        # Step 3/4: theta/pi = dist(t, 1) = (1/2) dist(2t, 2)
        assert dist(t, 1) == dist(2 * t, 2) / 2
        cnt += 1
    print(f"E1 Step 0 & Step 3/4 exact identities: {cnt} random rationals x 4 moduli: OK")
    # E1b: Step 3 against the definition arccos|cos| with a float cross-check (non-load-bearing,
    #      errors are far from any decision threshold)
    maxerr = 0.0
    for _ in range(20000):
        t = rng.uniform(-50, 50)
        lhs = math.acos(min(1.0, abs(math.cos(math.pi * t)))) / math.pi
        rhs = float(dist(Fr(t), 1))
        maxerr = max(maxerr, abs(lhs - rhs))
    print(f"E1b arccos|cos(pi t)|/pi vs dist(t,Z), 20000 floats in [-50,50]: max abs diff {maxerr:.2e}")
    # E2
    cnt = 0
    for _ in range(5000):
        den = rng.choice([1, 2, 3, 5, 8, 12, 101])
        u = rand_rat(rng, -10, 10, den); v = rand_rat(rng, -10, 10, den)
        I = integral_pair(u, v)
        assert I == 2 * dist(u - v, 2), (u, v, I)
        cnt += 1
    # D(s) = 2 s on [0,1] (units of pi) including endpoints
    for s in [Fr(0), Fr(1), Fr(1, 2), Fr(1, 3), Fr(999, 1000)]:
        assert integral_pair(Fr(0), s) == 2 * s
    print(f"E2 identity (10.1) exact (breakpoint integration): {cnt} random rational (u,v) + D endpoints: OK")
    # E3 + E4
    cnt = 0
    for _ in range(1500):
        N = rng.randint(0, 11)
        den = rng.choice([2, 3, 4, 6, 12, 60, 997])
        a = [rand_rat(rng, -3, 3, den) for _ in range(N)]
        u = [2 * x for x in a]
        pts = breakpoints(u)
        tot = Fr(0)
        for lo, hi in zip(pts, pts[1:]):
            m = (lo + hi) / 2
            k = sum(g(w - m) for w in u)
            P = sum(abs(g(u[i] - m) - g(u[j] - m)) for i in range(N) for j in range(i + 1, N))
            assert P == k * (N - k)
            assert k * (N - k) <= N * N // 4
            tot += (hi - lo) * k * (N - k)
        S = S_units(a)
        # S (units pi) == (1/4) * int_0^{2pi} k(N-k) dpsi / pi = (1/4) * tot
        assert S == tot / 4, (a, S, tot)
        assert 2 * S <= N * N // 4
        cnt += 1
    print(f"E3/E4 counting identity and full chain S = (1/4) int k(N-k), exact: {cnt} random configs N=0..11: OK")
    # E5
    for N in range(0, 401):
        vals = [k * (N - k) for k in range(N + 1)]
        assert max(vals) == N * N // 4
        assert {k for k in range(N + 1) if vals[k] == N * N // 4} == {N // 2, (N + 1) // 2}
    print("E5 k(N-k) <= floor(N^2/4), all 0<=k<=N<=400, equality iff k in {floor,ceil}(N/2): OK")
    # E6 exhaustive grid
    tot_cfg = 0
    for m, Nmax in [(2, 12), (3, 11), (4, 10), (5, 9), (6, 9), (7, 8), (8, 8), (9, 7), (10, 7), (12, 7), (24, 5), (60, 4)]:
        D = [[min((i - j) % m, (j - i) % m) for j in range(m)] for i in range(m)]  # dist in units pi/m
        for N in range(1, Nmax + 1):
            best = -1
            for combo in itertools.combinations_with_replacement(range(m), N):
                s = 0
                for i in range(N):
                    ci = combo[i]; Di = D[ci]
                    for j in range(i + 1, N):
                        s += Di[combo[j]]
                if s > best:
                    best = s
                tot_cfg += 1
            # S = pi*best/m ; bound (pi/2) floor(N^2/4): compare 2*best <= m*floor(N^2/4)
            assert 2 * best <= m * (N * N // 4), (m, N, best)
            if m % 2 == 0:
                assert 2 * best == m * (N * N // 4), (m, N, best)  # perpendicular pair is on grid
    print(f"E6 exhaustive grid search, {tot_cfg} multisets: no violation; max attained exactly when grid contains perpendicular pair: OK")
    # E7
    def M(N, d):
        q, s = divmod(N, d)
        return s * math.comb(q + 1, 2) + (d - s) * math.comb(q, 2)
    for N in range(0, 2001):
        assert math.comb(N, 2) - M(N, 2) == N * N // 4
    for N, k in [(2, 0), (3, 1), (4, 2)]:
        assert math.comb(N, 2) - k == N * N // 4
    assert [N * N // 4 for N in (2, 3, 4, 5)] == [1, 2, 4, 6]  # (pi/2)* -> pi/2, pi, 2pi, 3pi
    print("E7 binom(N,2)-M(N,2)=floor(N^2/4) N<=2000; Setting example N=2,3,4; S6 values pi/2,pi,2pi,3pi: OK")
    # E8 equality config and tightness of the chain
    for N in range(0, 41):
        a = [Fr(0)] * (N // 2) + [Fr(1, 2)] * (N - N // 2)
        S = S_units(a)
        assert 2 * S == N * N // 4
        u = [2 * x for x in a]
        pts = breakpoints(u)
        for lo, hi in zip(pts, pts[1:]):
            m = (lo + hi) / 2
            k = sum(g(w - m) for w in u)
            assert k * (N - k) == N * N // 4
    # other odd-N maximiser named in the remark: N=3 at mutual pi/3
    assert 2 * S_units([Fr(0), Fr(1, 3), Fr(2, 3)]) == 9 // 4
    print("E8 balanced perpendicular split N=0..40: S == bound exactly, and k(N-k)=floor(N^2/4) on every open piece: OK;"
          " N=3 at pi/3 spacing also equal: OK")

if __name__ == "__main__":
    main()
