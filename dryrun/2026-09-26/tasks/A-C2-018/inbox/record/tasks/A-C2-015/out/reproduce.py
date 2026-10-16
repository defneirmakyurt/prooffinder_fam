"""Reproduce worst case (equality) for A-C2. Stdlib exact check + mpmath interval evaluation if available."""
from fractions import Fraction as F
x = [(F(1), F(0)), (F(3,5), F(4,5)), (F(0), F(1))]
ip = lambda u, v: u[0]*v[0] + u[1]*v[1]
assert all(ip(v, v) == 1 for v in x) and ip(x[0], x[2]) == 0
a1, a2 = abs(ip(x[0], x[1])), abs(ip(x[1], x[2]))
print("a1, a2 =", a1, a2, " a1^2+a2^2 =", a1*a1 + a2*a2)
# exact: a1^2+a2^2=1 with a1,a2>=0 => arccos(a2) = arcsin(a1) = pi/2 - arccos(a1), so LHS = pi/2 = RHS exactly
print("LHS = arccos(3/5)+arccos(4/5) = pi/2 exactly (since (3/5)^2+(4/5)^2 = 1); RHS = (m-2)pi/2 = pi/2; margin = 0")
# illustration only (the margin 0 is exact by the identity above):
import math
print("float LHS =", math.acos(0.6) + math.acos(0.8), " float RHS =", math.pi/2)
