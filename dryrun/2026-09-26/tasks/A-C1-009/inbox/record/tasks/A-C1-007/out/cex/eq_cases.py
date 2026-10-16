"""Referee A-C1-007: equality cases and cross-cell arithmetic (exact, stdlib only). Angles in units of pi.
E1 balanced split floor(N/2) x {0}, ceil(N/2) x {1/2}: S == floor(N^2/4)/2, N = 0..40.
E2 Proof A tightness at balanced split: k(t)(N-k(t)) == floor(N^2/4) on every breakpoint piece, N = 0..40.
E3 Proof B tightness: B2 removal at the balanced split leaves the balanced split of N-2 (value check), N = 2..40.
E4 Remark claims (non-load-bearing): regular odd-N configuration {k/N} attains the bound, N odd 3..41;
   three lines at mutual angle 1/3 give S = 1.
E5 S5 arithmetic: binom(N,2) - M(N,2) == floor(N^2/4), N = 0..300; S6 values N=2..5.
"""
from fractions import Fraction as F
from itertools import combinations
from math import comb
import importlib.util, sys, os
spec = importlib.util.spec_from_file_location("cex", os.path.join(os.path.dirname(os.path.abspath(__file__)), "cex.py"))
cex = importlib.util.module_from_spec(spec); spec.loader.exec_module(cex)
rho, S, chi, breakpoints = cex.rho, cex.S, cex.chi, cex.breakpoints

def bal(N):
    return [F(0)] * (N // 2) + [F(1, 2)] * (N - N // 2)

bad = {k: 0 for k in ["E1", "E2", "E3", "E4", "E5"]}
for N in range(0, 41):
    a = bal(N); b = F((N * N) // 4, 2)
    if S(a) != b: bad["E1"] += 1
    pts = breakpoints(a)
    for lo, hi in zip(pts, pts[1:]):
        t = (lo + hi) / 2
        k = sum(chi(x - t) for x in a)
        if k * (N - k) != (N * N) // 4: bad["E2"] += 1
    if N >= 2:
        rest = bal(N)[:]; rest.remove(F(0)) if N // 2 >= 1 else None; rest.remove(F(1, 2))
        if S(a) != F(N - 1, 2) + S(rest) or S(rest) != F(((N - 2) ** 2) // 4, 2): bad["E3"] += 1
for N in range(3, 42, 2):
    if S([F(k, N) for k in range(N)]) != F((N * N) // 4, 2): bad["E4"] += 1
if S([F(0), F(1, 3), F(2, 3)]) != 1: bad["E4"] += 1
def M(N, d):
    q, s = divmod(N, d); return s * comb(q + 1, 2) + (d - s) * comb(q, 2)
for N in range(0, 301):
    if comb(N, 2) - M(N, 2) != (N * N) // 4: bad["E5"] += 1
s6 = {N: S(bal(N)) for N in (2, 3, 4, 5)}
if s6 != {2: F(1, 2), 3: F(1), 4: F(2), 5: F(3)}: bad["E5"] += 1
print("E-checks failures:", bad, "S6 values (units of pi):", {k: str(v) for k, v in s6.items()})
print("ALL OK" if not any(bad.values()) else "FAILURE")
