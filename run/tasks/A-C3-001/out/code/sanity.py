"""Evidence-only sanity checks for A-C3-001 (floating point; NOT proof steps).

1. h(t) = arcsin(r cos t): compare the closed form h'' = r c (r^2-1)/(1-r^2 c^2)^{3/2}
   (c = cos t) with central finite differences at random (r, t), |t| < pi/2, r < 1.
2. F(x) = sum_{i<j} arcsin|<x_i,x_j>| >= pi/2 for random unit x_1..x_{d+1} in R^d, d = 1..6.
3. Crude local search (random single-vector moves, accept if F decreases) from random starts;
   report the smallest F found per d (expected: about pi/2, never below).
4. Along random great circles y(t) = cos t x_i + sin t v (v unit, v perp x_i, v perp x_j for j in O),
   g(t) = sum_j arcsin|<y(t),x_j>| has non-positive second differences between consecutive zeros.
Stdlib only.  Run: python3 sanity.py
"""
import math, random

random.seed(20260926)

def unit(d):
    while True:
        v = [random.gauss(0, 1) for _ in range(d)]
        n = math.sqrt(sum(a * a for a in v))
        if n > 1e-9:
            return [a / n for a in v]

def dot(u, v):
    return sum(a * b for a, b in zip(u, v))

def asn(t):
    return math.asin(min(1.0, abs(t)))

def F(xs):
    n = len(xs)
    return sum(asn(dot(xs[i], xs[j])) for i in range(n) for j in range(i + 1, n))

# 1. second derivative formula
worst = 0.0
for _ in range(20000):
    r = random.uniform(0, 0.999)
    t = random.uniform(-1.5, 1.5)
    hstep = 1e-4
    h = lambda s: math.asin(r * math.cos(s))
    fd = (h(t + hstep) - 2 * h(t) + h(t - hstep)) / hstep ** 2
    c = math.cos(t)
    cf = r * c * (r * r - 1) / (1 - r * r * c * c) ** 1.5
    worst = max(worst, abs(fd - cf) / (1 + abs(cf)))
print("check1 h'' formula: max rel err %.2e (expect small, ~1e-5 or less)" % worst)

# 2. random configurations
for d in range(1, 7):
    m = min(F([unit(d) for _ in range(d + 1)]) for _ in range(5000))
    print("check2 d=%d: min F over 5000 random configs = %.6f  (pi/2 = %.6f)" % (d, m, math.pi / 2))

# 3. local search
for d in range(1, 7):
    best = float("inf")
    for start in range(20):
        xs = [unit(d) for _ in range(d + 1)]
        f = F(xs)
        step = 0.5
        for it in range(3000):
            i = random.randrange(d + 1)
            old = xs[i]
            cand = [a + step * random.gauss(0, 1) for a in old]
            nn = math.sqrt(sum(a * a for a in cand))
            if nn < 1e-12:
                continue
            xs[i] = [a / nn for a in cand]
            g = F(xs)
            if g < f:
                f = g
            else:
                xs[i] = old
            if it % 500 == 499:
                step *= 0.5
        best = min(best, f)
    print("check3 d=%d: min F by local search = %.6f  (pi/2 = %.6f)" % (d, best, math.pi / 2))

# 4. concavity of g between zeros along great circles
viol = 0
tested = 0
for trial in range(300):
    d = random.randint(2, 6)
    xs = [unit(d) for _ in range(d + 1)]
    i = 0
    # make x_i orthogonal to a random subset O of the others (project x_j off x_i), |O| <= d-2
    others = list(range(1, d + 1))
    O = random.sample(others, random.randint(0, max(0, d - 2)))
    for j in O:
        p = dot(xs[j], xs[i]); v = [a - p * b for a, b in zip(xs[j], xs[i])]
        n = math.sqrt(dot(v, v)); xs[j] = [a / n for a in v]
    # v: unit, perp x_i and perp x_j (j in O): Gram-Schmidt a random vector
    basis = [xs[i]] + [xs[j] for j in O]
    ob = []
    for b in basis:
        w = b[:]
        for q in ob:
            p = dot(w, q); w = [a - p * c for a, c in zip(w, q)]
        n = math.sqrt(dot(w, w))
        if n > 1e-9:
            ob.append([a / n for a in w])
    w = unit(d)
    for q in ob:
        p = dot(w, q); w = [a - p * c for a, c in zip(w, q)]
    n = math.sqrt(dot(w, w))
    if n < 1e-6:
        continue
    v = [a / n for a in w]
    J = [j for j in others if j not in O]
    K = 4000
    ts = [-math.pi + 2 * math.pi * k / K for k in range(K + 1)]
    vals = []
    signs = []
    for t in ts:
        y = [math.cos(t) * a + math.sin(t) * b for a, b in zip(xs[i], v)]
        vals.append(sum(asn(dot(y, xs[j])) for j in J))
        signs.append(tuple(dot(y, xs[j]) > 0 for j in J))
    for k in range(1, K):
        if signs[k - 1] == signs[k] == signs[k + 1]:
            tested += 1
            if vals[k + 1] - 2 * vals[k] + vals[k - 1] > 1e-9:
                viol += 1
print("check4 concavity between zeros: %d second differences tested, %d violations" % (tested, viol))
