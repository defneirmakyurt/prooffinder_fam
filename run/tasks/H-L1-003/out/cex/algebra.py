# Symbolic check of Step 10 algebra (exact, sympy). Not stdlib; referee-only sanity.
import sympy as sp
d, m, T = sp.symbols('d m T')  # T stands for 2^(d-1); 2^d = 2T
eq = sp.Eq(d*T, (2*T - 1 - m) + m*d)
msol = sp.solve(eq, m)[0]
print("m from Step-7 identity:", sp.simplify(msol), " ; (d-1)*m - (T*(d-2)+1) =", sp.simplify((d-1)*msol - (T*(d-2)+1)))
print("T*(d-1) - (T*(d-2)+1) - (T-1) =", sp.expand(T*(d-1) - (T*(d-2)+1) - (T-1)))
print("with (d-1)m = T(d-2)+1: T-1 - (d-1)(T-m) =", sp.simplify((T-1) - (d-1)*(T-msol)))
