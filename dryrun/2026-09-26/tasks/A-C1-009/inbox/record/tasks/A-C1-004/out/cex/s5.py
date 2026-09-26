"""S5: binom(N,2) - M(N,2) == floor(N^2/4) for N = 0..10000 (exact integers, stdlib)."""
from math import comb
bad = 0
for N in range(0, 10001):
    q, s = divmod(N, 2)
    M = s * comb(q + 1, 2) + (2 - s) * comb(q, 2)
    if comb(N, 2) - M != N * N // 4:
        bad += 1
print(f"S5: N=0..10000, failures = {bad}")
