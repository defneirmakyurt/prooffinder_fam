"""Non-load-bearing sanity check for A-C1 (lines in the plane).

The proof in out/proof.md does NOT rest on this script. It uses floating point only, to
spot-check (1) the bound S <= (pi/2) floor(N^2/4) on random and hill-climbed configurations,
and (2) the identity  int_0^{2pi} |g(u-psi) - g(v-psi)| dpsi = 2 delta(u-v)  by a midpoint
Riemann sum. Stdlib only.
"""
import math
import random


def theta(a, b):
    """Acute angle between lines with direction angles a, b, straight from the definition."""
    c = math.cos(a) * math.cos(b) + math.sin(a) * math.sin(b)
    return math.acos(min(1.0, abs(c)))


def S(angles):
    n = len(angles)
    return sum(theta(angles[i], angles[j]) for i in range(n) for j in range(i + 1, n))


def bound(n):
    return (math.pi / 2) * (n * n // 4)


def g(x):
    r = x - 2 * math.pi * math.floor(x / (2 * math.pi))
    return 1 if r < math.pi else 0


def delta(t):
    k = round(t / (2 * math.pi))
    return abs(t - 2 * math.pi * k)


def main():
    rng = random.Random(12345)
    worst_ratio = 0.0
    # (1a) random configurations
    for n in range(1, 13):
        for _ in range(2000):
            a = [rng.uniform(0, math.pi) for _ in range(n)]
            s = S(a)
            assert s <= bound(n) + 1e-9, (n, a, s)
            if n >= 2:
                worst_ratio = max(worst_ratio, s / bound(n))
    # (1b) crude hill climbing, to see that the max approaches the bound
    best = {}
    for n in range(2, 10):
        a = [rng.uniform(0, math.pi) for _ in range(n)]
        s = S(a)
        step = 0.5
        for it in range(20000):
            i = rng.randrange(n)
            b = list(a)
            b[i] += rng.uniform(-step, step)
            t = S(b)
            if t >= s:
                a, s = b, t
            if it % 2000 == 1999:
                step *= 0.5
        assert s <= bound(n) + 1e-9
        best[n] = (s, bound(n))
    # (2) Crofton-type identity via midpoint Riemann sum
    M = 20000
    h = 2 * math.pi / M
    max_err = 0.0
    for _ in range(200):
        u, v = rng.uniform(-10, 10), rng.uniform(-10, 10)
        tot = sum(abs(g(u - (m + 0.5) * h) - g(v - (m + 0.5) * h)) for m in range(M)) * h
        max_err = max(max_err, abs(tot - 2 * delta(u - v)))
    print("random configs N=1..12 x 2000: all within bound; max S/bound =", round(worst_ratio, 6))
    for n, (s, b) in best.items():
        print(f"hill-climb N={n}: best S={s:.9f}  bound={b:.9f}  gap={b - s:.2e}")
    print("identity check (200 random u,v, M=20000): max |error| =", f"{max_err:.2e}",
          "(Riemann-sum resolution ~ 2h =", f"{2 * h:.2e})")


if __name__ == "__main__":
    main()
