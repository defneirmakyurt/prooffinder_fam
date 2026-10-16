# Referee counterexample search for A-C2 (chain lemma).
# Exact rational Gram data + arb ball arithmetic (python-flint) for certified comparisons.
import random, sys, math
from fractions import Fraction as F
import flint
from flint import arb, fmpq
import sympy as sp
flint.ctx.prec = 256

def A(x): return arb(fmpq(x.numerator, x.denominator))

# ---- 1. symbolic check of the Step 5 identity
a, b = sp.symbols('a b', real=True)
lhs = sp.sin(a+b)*sp.cos(b) - sp.sin(a)
rhs = sp.sin(b)*sp.cos(a+b)
print("Step5 identity simplifies to 0:", sp.simplify(sp.expand_trig(lhs - rhs)) == 0)

# ---- 2. Exact Gram search.
# An admissible chain in R^(m-1) <=> tridiagonal m x m Gram G (unit diag, offdiag c_i) PSD with rank <= m-1.
# Generic family: s_i=c_i^2 rational in (0,1) for i<=m-2 with leading minors D_1..D_{m-1}>0,
# s_{m-1}=D_{m-1}/D_{m-2} so that D_m=0 (D_k = D_{k-1} - s_{k-1} D_{k-2}).
# Check certified: sum arcsin(sqrt s_i) >= pi/2, i.e. theta-sum <= (m-2)pi/2.
def chain(m, rng, den):
    s = []
    D = [F(1), F(1)]  # D_0=1, D_1=1
    for i in range(1, m-1):  # s_1..s_{m-2}
        for _ in range(50):
            si = F(rng.randint(0, den), den)
            Dn = D[-1] - si*D[-2]
            if Dn > 0: break
        else:
            return None
        s.append(si); D.append(Dn)
    # now D = [D0..D_{m-1}]
    s.append(D[-1]/D[-2])
    return s

pi2 = arb.pi()/2
rng = random.Random(12345)
tot = 0; worst = None; bad = 0
for m in range(2, 13):
    cnt = 0
    for trial in range(3000):
        den = rng.choice([2,3,5,7,10,97,1000,10**6])
        if m == 2:
            s = [F(1)]
        else:
            s = chain(m, rng, den)
            if s is None: continue
        assert all(0 <= t <= 1 for t in s)
        Asum = sum((A(t).sqrt().asin() for t in s), arb(0))
        th = sum((( 1 - A(t)).sqrt().asin() for t in s), arb(0))  # arccos sqrt(t) = arcsin sqrt(1-t)
        slack = (m-2)*pi2 - th
        # certified: slack >= 0 unless ball contains negatives; if ball straddles 0 need exact equality
        if slack < 0:
            bad += 1; print("VIOLATION", m, s)
        elif not (slack >= 0):
            # straddles 0: equality candidate; record
            pass
        mid = float(slack.mid())
        if m >= 3 and (worst is None or mid < worst[0]): worst = (mid, m, s)
        cnt += 1
    tot += cnt
    print(f"m={m}: {cnt} exact admissible chains checked")
print("total", tot, "certified violations:", bad, "min slack (float of ball midpoint):", worst[0], "at m=", worst[1])

# ---- 3. Equality tuple (e1,e1,e2,...,e_{m-1}): s = [1,0,...,0]
for m in range(2, 12):
    s = [F(1)] + [F(0)]*(m-2)
    th = sum((( 1 - A(t)).sqrt().asin() for t in s), arb(0))
    print("S2 tuple m=%d: theta-sum - (m-2)pi/2 =" % m, (th - (m-2)*pi2).str(5, radius=True))

# ---- 4. Float check of the Step 4 reduction formulas on explicit vectors (sanity only, stdlib)
# Bidiagonal Cholesky realisation in R^(m-1): x_1=e_1, x_{k+1} = (c_k/r_k) e_k + r_{k+1} e_{k+1}, r_{k+1}^2 = 1 - c_k^2/r_k^2, r_m = 0.
rs = random.Random(7)
def dot(u, v): return sum(p*q for p, q in zip(u, v))
maxerr = 0; nvec = 0
for m in range(3, 10):
    for _ in range(200):
        s = chain(m, rng, 10**6)
        if s is None: continue
        c = [math.sqrt(float(t))*rs.choice([-1,1]) for t in s]
        n = m-1
        x = []; r = 1.0
        v = [0.0]*n; v[0] = 1.0; x.append(v)
        for k in range(1, m):
            l = c[k-1]/r
            r2 = max(1 - l*l, 0.0); rn = math.sqrt(r2)
            v = [0.0]*n; v[k-1] = l
            if k < n: v[k] = rn
            x.append(v); r = rn
        # check hypotheses realised
        for i in range(m):
            maxerr = max(maxerr, abs(dot(x[i],x[i])-1))
            for j in range(i+2, m): maxerr = max(maxerr, abs(dot(x[i],x[j])))
        cc = c[-1]
        if abs(cc) >= 1: continue
        y = [(p - cc*q)/math.sqrt(1-cc*cc) for p, q in zip(x[m-2], x[m-1])]
        maxerr = max(maxerr, abs(dot(y, x[m-1])), abs(dot(y,y)-1), abs(dot(x[m-3], y) - c[m-3]/math.sqrt(1-cc*cc)))
        for i in range(m-3): maxerr = max(maxerr, abs(dot(x[i], y)))
        nvec += 1
print("Step 4 reduction: %d explicit chains, float max residual:" % nvec, maxerr)

# ---- 5. Float local search minimising A = sum arcsin|c_i| over the generic family (tries to push below pi/2)
best = 10
for m in range(3, 9):
    for start in range(300):
        u = [rs.random() for _ in range(m-2)]
        def Aval(u):
            D = [1.0, 1.0]; ss = []
            for i in range(m-2):
                si = min(max(u[i],0),1); Dn = D[-1]-si*D[-2]
                if Dn <= 0: return None
                ss.append(si); D.append(Dn)
            ss.append(D[-1]/D[-2])
            return sum(math.asin(math.sqrt(t)) for t in ss)
        v = Aval(u)
        if v is None: continue
        step = 0.1
        for it in range(400):
            cand = [p + rs.gauss(0, step) for p in u]
            cv = Aval(cand)
            if cv is not None and cv < v: u, v = cand, cv
            else: step *= 0.99
        best = min(best, v - math.pi/2)
print("Float local search: min of A - pi/2 over m=3..8:", best)
