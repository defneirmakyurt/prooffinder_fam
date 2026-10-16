"""S5/S6: binom(N,2) - M(N,2) == floor(N^2/4) for N in 0..10000; balanced split values; Setting example at d=2."""
from math import comb
from fractions import Fraction as F
def M(N, d):
    q, s = divmod(N, d)
    return s * comb(q + 1, 2) + (d - s) * comb(q, 2)
bad = sum(1 for N in range(0, 10001) if comb(N, 2) - M(N, 2) != N * N // 4)
print("binom(N,2)-M(N,2)==floor(N^2/4), N=0..10000: failures =", bad)
for N in (2, 3, 4, 5):
    m = N // 2
    print(f"N={N}: balanced split S/pi = {F(m*(N-m),2)}, bound/pi = {F(N*N//4,2)}")
for k in (0, 1, 2):
    N = 2 + k
    print(f"Setting example d=2,k={k}: (binom(N,2)-k)/2 = {F(comb(N,2)-k,2)}, floor(N^2/4)/2 = {F(N*N//4,2)}")
