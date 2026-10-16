# Referee checks for A-C2 proof (A-C2-001). Run with the venv python (sympy, mpmath).
import random, sympy as sp
from fractions import Fraction as F
from mpmath import mp, mpf
mp.prec = 256
random.seed(20260926)

# 1. Symbolic: recurrence (2) vs sympy determinant, m = 2..9
for m in range(2, 10):
    a = sp.symbols('a1:%d' % m)
    G = sp.zeros(m, m)
    for i in range(m): G[i, i] = 1
    for i in range(m - 1): G[i, i+1] = G[i+1, i] = a[i]
    D = [sp.Integer(1), sp.Integer(1)]
    for k in range(2, m + 1): D.append(sp.expand(D[k-1] - a[k-2]**2 * D[k-2]))
    for k in range(1, m + 1):
        assert sp.expand(G[:k, :k].det() - D[k]) == 0, (m, k)
print("recurrence (2) matches det for all leading minors, m=2..9: OK")

# 2. Symbolic: lemma identity (a) and (b)
p, f = sp.symbols('psi phi', real=True)
e1 = sp.simplify(sp.expand_trig(sp.cos(p+f)*sp.cos(p-f)) - (sp.cos(p)**2 - sp.sin(f)**2))
e2 = sp.simplify(sp.expand_trig(sp.cos(p-f) - sp.cos(p+f)) - 2*sp.sin(p)*sp.sin(f))
print("identity (a) residual:", e1, "; identity (b) residual:", e2)

# 3. Lemma inequality on random/extremal points (high precision)
worst = mpf(10)
for _ in range(20000):
    ps = mpf(random.random()) * mp.pi/2
    ph = mpf(random.random()) * (mp.pi/2 - ps)
    if random.random() < 0.1: ps = mpf(0)
    if random.random() < 0.1: ph = mpf(0)
    lhs = mp.cos(ps)**2 - mp.sin(ph)**2; rhs = mp.cos(ps)**2 * mp.cos(ps+ph)**2
    worst = min(worst, lhs - rhs)
print("lemma: min lhs-rhs over 20000 samples:", mp.nstr(worst, 5))

# 4. Counterexample search on the target. Admissible configurations <-> tridiagonal
# unit-diagonal PSD G of rank <= m-1. Generate exactly: rational a_1..a_{m-2} with
# D_1..D_{m-1} > 0, then a_{m-1}^2 = D_{m-1}/D_{m-2} (forces D_m = 0) if <= 1.
# Then G is PSD of rank m-1, so realisable by m unit vectors in R^{m-1}.
# Check sum phi_i >= pi/2 (phi_i = arcsin|a_i|) at 256-bit precision; flag if slack < 1e-40.
tested = 0; minslack = None; flagged = 0; viol = []; maxabs_hi = mpf(0)
for trial in range(60000):
    m = random.randint(2, 14)
    a2 = []
    for i in range(m - 2):
        r = random.random()
        if r < 0.1: q = F(0)
        elif r < 0.15: q = F(1)
        else: q = F(random.randint(0, 1000), 1000) ** random.choice([1, 2, 3])
        a2.append(q * q)  # store a_i^2
    D = [F(1), F(1)]
    for k in range(2, m):
        D.append(D[k-1] - a2[k-2] * D[k-2])
    if any(d <= 0 for d in D[1:m]): continue
    t = D[m-1] / D[m-2]
    if t > 1: continue
    a2.append(t)
    Dm = D[m-1] - t * D[m-2]; assert Dm == 0
    s = sum(mp.asin(mp.sqrt(mpf(x.numerator) / x.denominator)) for x in a2)
    slack = s - mp.pi/2
    tested += 1
    if minslack is None or slack < minslack: minslack = slack
    if slack < mpf(10)**-40:
        flagged += 1
        # re-evaluate at 2048 bits: an equality case shrinks to ~0, a true violation would not
        with mp.workprec(2048):
            s2 = sum(mp.asin(mp.sqrt(mpf(x.numerator) / x.denominator)) for x in a2) - mp.pi/2
        if s2 < -mpf(10)**-300: viol.append((m, a2, s2))
        maxabs_hi = max(maxabs_hi, abs(s2))
print("admissible random chains tested:", tested, "flagged (slack<1e-40):", flagged,
      "min slack sum(phi)-pi/2:", mp.nstr(minslack, 5))
print("flagged cases re-evaluated at 2048 bits: violations (<-1e-300):", len(viol),
      "; max |slack| among flagged at 2048 bits:", mp.nstr(maxabs_hi, 5), "(i.e. exact equality cases)")

# 5. Equality tuple (e1,e1,e2,...,e_{m-1}): exact
for m in range(2, 12):
    X = [[0]*(m-1) for _ in range(m)]
    X[0][0] = 1
    for j in range(1, m): X[j][j-1] = 1
    ok = all(sum(X[i][k]*X[j][k] for k in range(m-1)) == 0 for i in range(m) for j in range(m) if abs(i-j) >= 2)
    dots = [abs(sum(X[i][k]*X[i+1][k] for k in range(m-1))) for i in range(m-1)]
    # theta = arccos(1)=0 for dot 1, arccos(0)=pi/2 for dot 0
    tot_halfpi = sum(0 if d == 1 else 1 for d in dots)
    assert ok and all(d in (0, 1) for d in dots) and tot_halfpi == m - 2
print("equality tuple: hypotheses hold and chain sum = (m-2)pi/2 exactly, m=2..11: OK")

# 6. Hill-climb (float, exploratory): maximise chain sum over admissible chains
def chain_sum(a2):
    import math
    return sum(math.acos(math.sqrt(x)) for x in a2)
import math
best = {}
for m in range(3, 9):
    bmax = -1
    for rep in range(300):
        x = [random.random()*0.3 for _ in range(m-2)]
        for it in range(300):
            y = [min(1.0, max(0.0, v + random.gauss(0, 0.05))) for v in x] if it else x
            D = [1.0, 1.0]
            for k in range(2, m): D.append(D[k-1] - y[k-2]*D[k-2])
            if any(d <= 0 for d in D[1:m]): continue
            t = D[m-1]/D[m-2]
            if t > 1: continue
            val = chain_sum(y + [t])
            if val > bmax: bmax = val
            x = y if val >= bmax - 1e-12 else x
    best[m] = (bmax, (m-2)*math.pi/2)
print("hill-climb max chain sum vs bound (float, exploratory):", {m: (round(v[0], 9), round(v[1], 9)) for m, v in best.items()})
