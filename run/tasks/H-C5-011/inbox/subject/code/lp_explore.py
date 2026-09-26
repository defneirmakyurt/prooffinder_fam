#!/usr/bin/env python3
"""lp_explore.py -- exploratory (NOT used by the proof; needs sympy from the venv).
Delsarte LP for even-weight length-9 codes with min distance >= 4 (variables A4, A6, A8 = average number
of codewords at distance 4, 6, 8 from a codeword), exact rational simplex (sympy.solvers.simplex):
  plain LP, LP + (A8 <= 1); and the dual of the second, which yields the certificate y1 = y2 = 1/3, u = 16/3
  re-checked by check_code_bound.py."""
from sympy.solvers.simplex import lpmax, lpmin
from sympy import symbols, binomial
n = 9
def K(k, x): return sum((-1) ** j * binomial(x, j) * binomial(n - x, k - j) for j in range(k + 1))
A4, A6, A8 = symbols('A4 A6 A8')
A = {0: 1, 4: A4, 6: A6, 8: A8}
for extra in ([], [A8 <= 1]):
    cons = [A4 >= 0, A6 >= 0, A8 >= 0] + extra
    cons += [sum(A[i] * K(k, i) for i in A) >= 0 for k in range(n + 1)]
    print("primal", extra, lpmax(1 + A4 + A6 + A8, cons))
ys = symbols('y1:10'); u = symbols('u')
cons = [y >= 0 for y in ys] + [u >= 0]
for i in (4, 6, 8):
    cons.append(-sum(ys[k - 1] * K(k, i) for k in range(1, 10)) + (u if i == 8 else 0) >= 1)
print("dual", lpmin(1 + sum(ys[k - 1] * K(k, 0) for k in range(1, 10)) + u, cons))
