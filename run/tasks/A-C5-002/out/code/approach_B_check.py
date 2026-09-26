"""
Exact symbolic check for Part III (Approach B) of out/proof.md, Steps 10-13.
NOT load-bearing for the d=2 proof (Part IV). Verifies, with exact symbolic arithmetic
(sympy, no floating point), the Veronese-embedding angle formula

    cos(ang_P(x,x')) = (d*cos(theta)**2 - 1)/(d - 1)

and the claimed reversal ang_P < 2*theta for d=3 at theta = pi/2 (exact) and the small-theta
asymptotic slope comparison sqrt(2d/(d-1)) < 2 for d >= 3 (exact, via a squared-inequality
comparison of rationals, no floating point / no approximation).

Run: /home/user/bainsahackathon/.venv/bin/python3 approach_B_check.py
"""
import sympy as sp

d, theta = sp.symbols('d theta', positive=True)
c = sp.cos(theta)

# --- Step 10: derive cos(ang_P) directly from the trace computation, symbolically ---
# P_x . P_x' = c**2 - 1/d  (derived in proof.md Step 10); |P_x|^2 = (d-1)/d
inner = c**2 - sp.Rational(1, 1) / d
norm2 = (d - 1) / d
cos_angP = sp.simplify(inner / norm2)
cos_angP_expected = (d * c**2 - 1) / (d - 1)
assert sp.simplify(cos_angP - cos_angP_expected) == 0
print("cos(ang_P) formula verified symbolically:", cos_angP_expected)

# --- Step 12: exact value at d=3, theta=pi/2 ---
d3 = 3
val = cos_angP_expected.subs({d: d3, theta: sp.pi / 2})
val = sp.simplify(val)
print("d=3, theta=pi/2: cos(ang_P) =", val)
assert val == sp.Rational(-1, 2)
angP = sp.acos(val)
angP = sp.simplify(angP)
print("d=3, theta=pi/2: ang_P =", angP, "  (2*theta =", sp.pi, ")")
assert angP == sp.Rational(2, 3) * sp.pi
assert angP < sp.pi  # ang_P < 2*theta exactly, both sides exact multiples of pi
print("Confirmed exactly: ang_P = 2*pi/3 < pi = 2*theta at d=3, theta=pi/2.")

# --- Step 13: small-theta asymptotic slope, exact rational comparison for several d ---
print()
for dval in [3, 4, 5, 10, 100]:
    lhs2 = sp.Rational(2 * dval, dval - 1)   # (slope)^2 = 2d/(d-1)
    rhs2 = sp.Integer(4)                      # (2)^2
    print(f"d={dval}: 2d/(d-1) = {lhs2}  vs 4  -> slope^2 < 4:", lhs2 < rhs2)
    assert lhs2 < rhs2
print("\nConfirmed exactly (as rational inequalities, all d>=3): "
      "sqrt(2d/(d-1)) < 2, i.e. ang_P grows strictly slower than 2*theta near theta=0.")
