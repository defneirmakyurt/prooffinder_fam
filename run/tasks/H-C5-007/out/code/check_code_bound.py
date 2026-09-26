#!/usr/bin/env python3
"""check_code_bound.py -- stdlib only, exact (Fractions / integers).
Re-checks the arithmetic of proof.md Lemma 3 (every set C of even-weight words of length 9 with pairwise
distance >= 4 has |C| <= 21):
  (a) K1(i) = 9 - 2i and K2(i) = ((9-2i)^2 - 9)/2 agree with the Krawtchouk sums
      K_k(i) = sum_j (-1)^j C(i,j) C(9-i,k-j) for k = 1, 2 and every i = 0..9;
  (b) the identity  sum_{j<l} eps_j eps_l = ((sum eps)^2 - 9)/2  for all 2^9 sign vectors
      (brute force), which is what makes K2 the right kernel;
  (c) the dual certificate y1 = y2 = 1/3, u = 16/3:  for i in {4,6,8},
      -(y1 K1(i) + y2 K2(i)) + u [i = 8] >= 1, and 1 + y1 K1(0) + y2 K2(0) + u = 64/3 < 22;
  (d) brute force on words: for each of the 2^9 words x, the words at distance 8 from x are pairwise at
      distance 2 (so a code with min distance 4 has at most one of them).
It proves nothing by itself beyond these finite identities; the argument is in proof.md."""
from fractions import Fraction as Fr
from math import comb
from itertools import product

n = 9
def K(k, i):
    return sum((-1) ** j * comb(i, j) * comb(n - i, k - j) for j in range(k + 1))

ok = True
for i in range(n + 1):
    ok &= K(1, i) == 9 - 2 * i
    ok &= K(2, i) * 2 == (9 - 2 * i) ** 2 - 9
print("(a) K1, K2 closed forms:", ok)

okb = True
for eps in product((1, -1), repeat=n):
    s2 = sum(eps[j] * eps[l] for j in range(n) for l in range(j + 1, n))
    okb &= 2 * s2 == sum(eps) ** 2 - 9
print("(b) pair-sum identity over all 512 sign vectors:", okb)

y1, y2, u = Fr(1, 3), Fr(1, 3), Fr(16, 3)
okc = True
for i in (4, 6, 8):
    lhs = -(y1 * K(1, i) + y2 * K(2, i)) + (u if i == 8 else 0)
    print("    i=%d: K1=%d K2=%d  multiplier value %s (need >= 1)" % (i, K(1, i), K(2, i), lhs))
    okc &= lhs >= 1
bound = 1 + y1 * K(1, 0) + y2 * K(2, 0) + u
print("(c) certificate valid:", okc, " bound =", bound, "-> |C| <= %d" % (bound.numerator // bound.denominator))

okd = True
for x in range(2 ** n):
    far = [y for y in range(2 ** n) if bin(x ^ y).count("1") == 8]
    okd &= len(far) == 9
    okd &= all(bin(a ^ b).count("1") == 2 for a in far for b in far if a != b)
print("(d) distance-8 words pairwise at distance 2:", okd)
print("ALL OK" if (ok and okb and okc and okd) else "FAILURE")
