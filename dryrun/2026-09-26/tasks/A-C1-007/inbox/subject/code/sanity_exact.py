"""Exact (fractions.Fraction, stdlib only) sanity checks for A-C1-003. NOT load-bearing.
Angles are measured in units of pi; a line is represented by a in [0,1) (direction angle a*pi).
Checks:
 (1) Proof B, Lemma B1: rho(z) + rho(z - 1/2) == 1/2 for z on the grid {k/D}.
 (2) Proof A, Lemma A2: measure{t in [0,1): chi(a-t) != chi(b-t)} == 2*rho(a-b), chi(u)=1[u mod 1 in [0,1/2)],
     computed by exact breakpoints, for all a,b on the grid.
 (3) Target on a grid: max over multisets of N angles from {k/D2} of S (units of pi) <= floor(N^2/4)/2.
Usage: python3 sanity_exact.py [D] [NMAX] [D2]
"""
import sys
from fractions import Fraction as F
from itertools import combinations_with_replacement

def rho(z):  # distance from z to the integers (units of pi: distance to pi*Z)
    z = z - (z.numerator // z.denominator)  # z mod 1 in [0,1)
    return min(z, 1 - z)

def chi(u):
    u = u - (u.numerator // u.denominator)
    return 1 if u < F(1, 2) else 0

def cut_measure(a, b):
    pts = {F(0), F(1)}
    for c in (a, b):
        for s in (c, c - F(1, 2)):
            s = s - (s.numerator // s.denominator)
            pts.add(s)
    pts = sorted(pts)
    m = F(0)
    for lo, hi in zip(pts, pts[1:]):
        mid = (lo + hi) / 2
        if chi(a - mid) != chi(b - mid):
            m += hi - lo
    return m

def main():
    D = int(sys.argv[1]) if len(sys.argv) > 1 else 48
    NMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 7
    D2 = int(sys.argv[3]) if len(sys.argv) > 3 else 8
    grid = [F(k, D) for k in range(D)]
    bad1 = sum(1 for z in grid if rho(z) + rho(z - F(1, 2)) != F(1, 2))
    print(f"check1 (rho(z)+rho(z-1/2)=1/2): {len(grid)} values, failures={bad1}")
    bad2 = 0
    for a in grid:
        for b in grid:
            if cut_measure(a, b) != 2 * rho(a - b):
                bad2 += 1
    print(f"check2 (cut identity): {len(grid)**2} pairs, failures={bad2}")
    grid2 = [F(k, D2) for k in range(D2)]
    ok3 = True
    for N in range(0, NMAX + 1):
        best = F(0)
        for conf in combinations_with_replacement(grid2, N):
            s = sum((rho(conf[i] - conf[j]) for i in range(N) for j in range(i + 1, N)), F(0))
            best = max(best, s)
        bound = F((N * N) // 4, 2)
        ok3 &= best <= bound
        print(f"check3 N={N}: grid max S/pi = {best}, bound = {bound}, {'OK' if best <= bound else 'VIOLATION'}")
    print("ALL OK" if (bad1 == 0 and bad2 == 0 and ok3) else "FAILURE")

if __name__ == "__main__":
    main()
