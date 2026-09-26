"""Exact sanity checks for A-C1 (lines in the plane). Stdlib only. NOT load-bearing.

All angles are measured in units of pi, so a line is a rational a in [0, 1),
rho(z) = dist(z, Z), and theta(l_a, l_b) = rho(a - b) (proof.md Step 4).
g(z) = 1 if rho(z) < 1/4 else 0.

Check 1 (Lemma, proof.md Step 8): for x, y on the grid {k/D : 0 <= k < D},
    measure{t in [0,1) : g(t-x) != g(t-y)} == 2 * rho(x - y),
computed exactly: the integrand is constant between consecutive breakpoints
x +- 1/4, y +- 1/4 (mod 1), so it is evaluated at interval midpoints.
(In units of pi the identity int_0^pi |...| dt = 2 rho reads measure = 2 rho.)

Check 2 (target, proof.md Step 12): for every multiset of N grid angles
(N <= NMAX, grid denominator D2), S = sum_{i<j} rho(a_i - a_j) <= floor(N^2/4)/2,
and the maximum over the grid equals floor(N^2/4)/2 whenever 2 divides D2.
"""
from fractions import Fraction as F
from itertools import combinations_with_replacement
import sys


def rho(z):
    z = z - (z.numerator // z.denominator)  # z mod 1 in [0,1)
    return min(z, 1 - z)


def g(z):
    return 1 if rho(z) < F(1, 4) else 0


def cut_measure(x, y):
    pts = set()
    for c in (x, y):
        for s in (F(1, 4), -F(1, 4)):
            p = c + s
            p = p - (p.numerator // p.denominator)
            pts.add(p)
    pts.add(F(0))
    pts = sorted(pts) + [F(1)]
    total = F(0)
    for lo, hi in zip(pts, pts[1:]):
        if hi > lo:
            mid = (lo + hi) / 2
            if g(mid - x) != g(mid - y):
                total += hi - lo
    return total


def main():
    D = int(sys.argv[1]) if len(sys.argv) > 1 else 48
    NMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 7
    D2 = int(sys.argv[3]) if len(sys.argv) > 3 else 8
    grid = [F(k, D) for k in range(D)]
    bad = 0
    for x in grid:
        for y in grid:
            if cut_measure(x, y) != 2 * rho(x - y):
                bad += 1
    print(f"check1: grid D={D}, pairs={D*D}, failures={bad}")
    grid2 = [F(k, D2) for k in range(D2)]
    ok2 = True
    for N in range(0, NMAX + 1):
        bound = F(N * N // 4, 2)
        best = F(-1)
        for conf in combinations_with_replacement(grid2, N):
            S = sum((rho(conf[i] - conf[j]) for i in range(N) for j in range(i + 1, N)), F(0))
            if S > bound:
                ok2 = False
                print("VIOLATION", N, conf, S)
            best = max(best, S)
        print(f"check2: N={N}, grid D2={D2}, max S (units of pi) = {best}, bound = {bound}, equal = {best == bound}")
    print("ALL OK" if bad == 0 and ok2 else "FAILURE")


if __name__ == "__main__":
    main()
