# Exact-rational evaluation of the published lower-bound formulas for nabla(Q_n), n = 5..13,
# to compare with Hertz (2021) Table 4 column L(Q_n) ("Bounds from [25]" = Pike 2003).
# stdlib only.
from fractions import Fraction as Fr
from math import ceil

hertz_L = {9: 225, 10: 456, 11: 922, 12: 1862, 13: 3755}      # Hertz 2021, Table 4 (opened)
hertz_U = {9: 236, 10: 472, 11: 952, 12: 1904, 13: 3840}      # Hertz 2021, Table 4 (opened)
A_n4 = {5: 2, 6: 4, 7: 8, 8: 16, 9: 20, 10: 40, 11: 72, 12: 144, 13: 256}  # standard table values (cited)

def cdiv(q):  # exact ceiling of a Fraction
    return -((-q.numerator) // q.denominator)

print("n | [1] (Bau et al., as quoted on Pike p.547): 2^{n-1}-(2^{n-1}-1)/(n-1) | "
      "Pike per Wodlinger Thm 2.31: 2^{n-1}+(n+1-2^{n-1})/(n-1) | Hertz L | 2^{n-1}-A(n,4) | Hertz U | even-code packing 2^{n-1}/n")
for n in range(5, 14):
    h = 2 ** (n - 1)
    old = Fr(h) - Fr(h - 1, n - 1)
    pike = Fr(h) + Fr(n + 1 - h, n - 1)
    print(n, "|", old, "->", cdiv(old), "|", pike, "->", cdiv(pike), "|", hertz_L.get(n, "-"), "|",
          h - A_n4[n], "|", hertz_U.get(n, "-"), "|", Fr(h, n), "->", h // n)

# Identity for Q_9 (8|S| = 1792 + c + e(S), valid whenever Q_9 - S is a forest):
for s in (225, 226, 232, 233, 235, 236):
    print("Q_9: |S| =", s, " requires c(F) + e(S) =", 8 * s - 1792)
