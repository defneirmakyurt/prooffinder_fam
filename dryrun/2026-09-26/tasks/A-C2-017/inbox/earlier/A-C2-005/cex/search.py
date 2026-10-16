# Referee counterexample search / sanity checks for A-C2 proof (A-C2-002).
# High-precision (mpmath, 50 digits) random + local-search over admissible chains; sympy symbolic lemma check.
import random, sympy as sp
from mpmath import mp, mpf, sqrt, asin, acos, pi, fabs
mp.dps = 50
random.seed(12345)

# 1. Symbolic identity used in Step 5
a, b = sp.symbols('a b', real=True)
expr = sp.sin(a+b)*sp.cos(b) - sp.sin(a) - sp.sin(b)*sp.cos(a+b)
print("Step5 identity residual simplifies to:", sp.simplify(sp.expand_trig(expr)))

def dot(u, v): return sum(x*y for x, y in zip(u, v))
def normalize(u):
    n = sqrt(dot(u, u)); return [x/n for x in u]
def proj_out(v, basis):  # basis orthonormal
    for q in basis:
        c = dot(v, q); v = [vi - c*qi for vi, qi in zip(v, q)]
    return v

def random_chain(m, special=0.0):
    d = m - 1
    xs = []
    for k in range(m):
        # x_k must be orthogonal to x_0..x_{k-2}
        basis = []
        for w in xs[:max(0, k-1)]:
            r = proj_out(list(w), basis)
            if sqrt(dot(r, r)) > mpf(10)**-30: basis.append(normalize(r))
        while True:
            v = [mpf(random.gauss(0, 1)) for _ in range(d)]
            if k >= 1 and random.random() < special:  # bias toward previous vector (near-parallel)
                v = [vi*mpf(random.choice([1e-3, 1e-1, 1])) + wi for vi, wi in zip(v, xs[-1])]
            v = proj_out(v, basis)
            if sqrt(dot(v, v)) > mpf(10)**-20: break
        xs.append(normalize(v))
    return xs

def check_hyp(xs):
    m = len(xs); err = mpf(0)
    for i in range(m):
        err = max(err, fabs(dot(xs[i], xs[i]) - 1))
        for j in range(i+2, m): err = max(err, fabs(dot(xs[i], xs[j])))
    return err

def A(xs):
    return sum(asin(min(mpf(1), fabs(dot(xs[i], xs[i+1])))) for i in range(len(xs)-1))

def theta_sum(xs):
    return sum(acos(min(mpf(1), fabs(dot(xs[i], xs[i+1])))) for i in range(len(xs)-1))

def reduction(xs):  # Step 4 construction; returns z-chain and checks
    m = len(xs); c = dot(xs[m-2], xs[m-1])
    u = [p - c*q for p, q in zip(xs[m-2], xs[m-1])]
    y = [ui/sqrt(1-c*c) for ui in u]
    zs = xs[:m-2] + [y]
    return zs, c

worst_margin = None; worst_red = mpf(0); worst_lemma = None; n = 0
for m in range(2, 9):
    for t in range(400):
        xs = random_chain(m, special=0.5)
        assert check_hyp(xs) < mpf(10)**-40
        margin = (m-2)*pi/2 - theta_sum(xs)
        n += 1
        if worst_margin is None or margin < worst_margin[0]: worst_margin = (margin, m)
        assert margin > -mpf(10)**-30, ("VIOLATION", m, margin)
        if m >= 3:
            c = dot(xs[m-2], xs[m-1])
            if fabs(c) < 1 - mpf(10)**-20:
                zs, c = reduction(xs)
                # z chain hypotheses, orthogonal to x_m
                e = max(check_hyp(zs), max(fabs(dot(z, xs[m-1])) for z in zs))
                worst_red = max(worst_red, e)
                am2 = asin(fabs(dot(xs[m-3], xs[m-2]))); am1 = asin(fabs(c))
                ap = asin(min(1, fabs(dot(zs[m-3], zs[m-2]))))
                # formula a' = arcsin(sin a_{m-2}/cos a_{m-1})
                worst_red = max(worst_red, fabs(ap - asin(min(1, fabs(dot(xs[m-3], xs[m-2]))/sqrt(1-c*c)))))
                if am2 + am1 < pi/2:
                    g = am2 + am1 - ap
                    assert g > -mpf(10)**-30
                    if worst_lemma is None or g < worst_lemma: worst_lemma = g
print("random chains tested:", n, " m in 2..8")
print("min margin (bound - chain sum):", mp.nstr(worst_margin[0], 8), "at m =", worst_margin[1])
print("max error in Step-4 reduction identities:", mp.nstr(worst_red, 5))
print("min (a_{m-2}+a_{m-1}-a') when sum<pi/2:", mp.nstr(worst_lemma, 8))

# 2. Local search minimizing margin (hill climbing on raw gaussian seeds via perturbation of vectors + reprojection)
def repair(xs):
    # re-impose constraints sequentially (Gram-Schmidt against x_0..x_{k-2})
    out = []
    for k, v in enumerate(xs):
        basis = []
        for w in out[:max(0, k-1)]:
            r = proj_out(list(w), basis)
            if sqrt(dot(r, r)) > mpf(10)**-30: basis.append(normalize(r))
        v = proj_out(list(v), basis)
        if sqrt(dot(v, v)) < mpf(10)**-20: return None
        out.append(normalize(v))
    return out
mp.dps = 30
for m in range(3, 7):
    best = None
    for restart in range(6):
        xs = random_chain(m); cur = (m-2)*pi/2 - theta_sum(xs); step = 0.5
        for it in range(600):
            ys = repair([[vi + mpf(random.gauss(0, step)) for vi in v] for v in xs])
            if ys is None: continue
            val = (m-2)*pi/2 - theta_sum(ys)
            if val < cur: xs, cur = ys, val
            else: step *= 0.995
        assert cur > -mpf(10)**-20, ("VIOLATION local", m, cur)
        if best is None or cur < best: best = cur
    print("local search m=%d: min margin found %s" % (m, mp.nstr(best, 8)))

# 3. Equality tuple and R^m trap
for m in range(2, 9):
    d = m - 1
    e = lambda i: [mpf(1) if k == i else mpf(0) for k in range(d)]
    xs = [e(0)] + [e(i) for i in range(d)]
    assert check_hyp(xs) == 0
    print("m=%d equality tuple: chain sum - bound = %s ; A-pi/2 = %s" % (m, mp.nstr(theta_sum(xs)-(m-2)*pi/2, 5), mp.nstr(A(xs)-pi/2, 5)))
    E = lambda i: [mpf(1) if k == i else mpf(0) for k in range(m)]
    print("   R^m trap: standard basis e_1..e_m chain sum - bound = %s (>0 shows dim hypothesis needed)" % mp.nstr(theta_sum([E(i) for i in range(m)])-(m-2)*pi/2, 5))
