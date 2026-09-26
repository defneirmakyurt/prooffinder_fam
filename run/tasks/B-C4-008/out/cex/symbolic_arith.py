"""Referee B-C4-008: symbolic check (sympy, exact) of the polynomial identities used in proof Step 7/8."""
import sympy as sp
k = sp.symbols('k', integer=True)
tstar = k**2 - 4*k + 2
h0, m = 1, k - 2
tau = lambda j: (k - 1 - h0) + (j - 1)*(k - 1)
print("tau_{m-1} - t* =", sp.expand(tau(m - 1) - tstar))                    # 0
print("t* - ((k-1)(k-3) - 1) =", sp.expand(tstar - ((k-1)*(k-3) - 1)))     # 0  => t* = -1 mod (k-1)
print("t* - 1 - (k(k-4) + 1) =", sp.expand(tstar - 1 - (k*(k-4) + 1)))       # 0  => t*-1 = 1 mod k
print("d formula at h0=1,m=k-2 minus (k-1)(k-3) =", sp.expand((k - h0) + (m - 2)*(k - 1) - (k-1)*(k-3)))  # 0
i = sp.symbols('i', integer=True)
lam_sum = (k - 2) + sp.summation(k - i, (i, 2, k - 2)) + 2 + 1
print("sum(lambda^(k)) - (T_{k-1}+1) =", sp.simplify(lam_sum - (k*(k-1)/2 + 1)))   # 0
print("C3(a) bound slack (k^2-2k-1) - (k-1)(k-3) =", sp.expand(k**2 - 2*k - 1 - (k-1)*(k-3)))  # 2k-4 >= 0
