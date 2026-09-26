"""Referee A-C3-007 counterexample search. Stdlib only. FLOATING POINT = EVIDENCE ONLY.
Searches:
 A. target: minimise T = sum_{i<j} arcsin|<x_i,x_j>| over d+1 unit vectors in R^d (d=1..7), random restarts + hill-climb.
    Target <=> T >= pi/2.
 B. Lemma L (Step 2): minimise sin D - sum sin(a_j) cos(D-a_j), a_j>=0, D<=pi/2, k=1..7, random + hill-climb.
 C. Key Lemma (Step 3): minimise min_i (p_i - sum_{j!=i} sin(alpha_ij) p_j)/p_i over alpha>=0 with T<pi/2, n=2..7;
    also checks sub-step (b): p_j <= cos(D_i - alpha_ij), and sub-step (c) chain, on every sample.
 D. consequence of Steps 3+4: unit-diagonal symmetric G with |G_ij| = sin(alpha_ij), random signs, T<pi/2
    must be nonsingular (in fact PD by continuity); test via Cholesky.
 E. equality configurations (S2): orthogonal+repeat d=1..10, d=2 gap family, 60-degree triple.
"""
import math, random, itertools
random.seed(7007)
PI2 = math.pi/2

def unit(v):
    s = math.sqrt(sum(t*t for t in v)); return [t/s for t in v]

def Tval(xs):
    T = 0.0
    for i, j in itertools.combinations(range(len(xs)), 2):
        g = abs(sum(a*b for a, b in zip(xs[i], xs[j])))
        T += math.asin(min(1.0, g))
    return T

# ---- A
print("A. target search: min T - pi/2 found, per d")
for d in range(1, 8):
    best = float('inf')
    for restart in range(60):
        xs = [unit([random.gauss(0, 1) for _ in range(d)]) for _ in range(d+1)]
        cur = Tval(xs); step = 0.3
        for it in range(1500):
            k = random.randrange(d+1)
            old = xs[k]
            xs[k] = unit([a + step*random.gauss(0, 1) for a in old])
            new = Tval(xs)
            if new <= cur: cur = new
            else: xs[k] = old
            if it % 300 == 299: step *= 0.5
        best = min(best, cur)
    print("  d=%d  min(T - pi/2) = %.3e" % (d, best - PI2))

# ---- B
def slackL(a):
    D = sum(a); return math.sin(D) - sum(math.sin(t)*math.cos(D-t) for t in a)
print("B. Lemma L: min slack found, per k")
for k in range(1, 8):
    best = float('inf')
    for restart in range(200):
        w = [random.random() for _ in range(k)]; D = random.random()*PI2; s = sum(w)
        a = [D*t/s for t in w]; cur = slackL(a); step = 0.1
        for it in range(300):
            b = [max(0.0, t + step*random.gauss(0, 1)) for t in a]
            if sum(b) > PI2: b = [t*PI2/sum(b) for t in b]
            v = slackL(b)
            if v < cur: cur, a = v, b
            if it % 100 == 99: step *= 0.5
        best = min(best, cur)
    print("  k=%d  min slack = %.3e" % (k, best))

# ---- C
def keyslack(n, al, checksub=False):
    T = sum(al[(i, j)] for i, j in itertools.combinations(range(n), 2))
    s = PI2 - T
    D = [sum(al[(i, j)] for j in range(n) if j != i) for i in range(n)]
    p = [math.sin(D[i] + s) for i in range(n)]
    worst = float('inf'); subfail = 0
    for i in range(n):
        lhs = sum(math.sin(al[(i, j)])*p[j] for j in range(n) if j != i)
        mid = sum(math.sin(al[(i, j)])*math.cos(D[i]-al[(i, j)]) for j in range(n) if j != i)
        if checksub:
            for j in range(n):
                if j != i and p[j] > math.cos(D[i]-al[(i, j)]) + 1e-13: subfail += 1
            if lhs > mid + 1e-13 or mid > math.sin(D[i]) + 1e-13 or math.sin(D[i]) >= p[i] + 1e-15: subfail += 1
        worst = min(worst, (p[i]-lhs)/p[i])
    return worst, subfail
print("C. Key Lemma: min relative slack found (T<pi/2 scaled to T = frac*pi/2), per n")
totsub = 0
for n in range(2, 8):
    pairs = list(itertools.combinations(range(n), 2))
    for frac in (0.5, 0.9, 0.999):
        best = float('inf')
        for restart in range(80):
            w = [random.random()*(random.random() < 0.6) for _ in pairs]
            if sum(w) == 0: w[0] = 1.0
            def mk(w):
                s = sum(w); al = {}
                for (i, j), t in zip(pairs, w): al[(i, j)] = al[(j, i)] = frac*PI2*t/s
                return al
            cur, sf = keyslack(n, mk(w), True); totsub += sf; step = 0.2
            for it in range(200):
                w2 = [max(0.0, t + step*random.gauss(0, 1)) for t in w]
                if sum(w2) == 0: continue
                v, sf = keyslack(n, mk(w2), True); totsub += sf
                if v < cur: cur, w = v, w2
                if it % 50 == 49: step *= 0.5
            best = min(best, cur)
        print("  n=%d T=%.3f*pi/2  min rel slack = %.3e" % (n, frac, best))
print("  sub-step (b)/(c)/(d) violations beyond 1e-13:", totsub)

# ---- D
def chol_ok(G):
    n = len(G); L = [[0.0]*n for _ in range(n)]
    for i in range(n):
        for j in range(i+1):
            s = G[i][j] - sum(L[i][k]*L[j][k] for k in range(j))
            if i == j:
                if s <= 0: return False
                L[i][i] = math.sqrt(s)
            else: L[i][j] = s/L[j][j]
    return True
fails = 0; cnt = 0
for trial in range(20000):
    n = random.randint(2, 8); pairs = list(itertools.combinations(range(n), 2))
    w = [random.random()**3 for _ in pairs]; frac = random.random()*0.999999
    s = sum(w); G = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
    for (i, j), t in zip(pairs, w):
        v = math.sin(frac*PI2*t/s)*random.choice((-1, 1)); G[i][j] = G[j][i] = v
    cnt += 1
    if not chol_ok(G): fails += 1
print("D. unit-diag G with sum arcsin|G_ij| < pi/2, random signs: %d samples, non-PD: %d" % (cnt, fails))

# ---- E
print("E. equality configurations")
for d in range(1, 11):
    xs = [[1.0 if c == k else 0.0 for c in range(d)] for k in range(d)] + [[1.0] + [0.0]*(d-1)]
    # all |g| in {0,1} exactly: count pairs with |g|=1
    ones = sum(1 for i, j in itertools.combinations(range(d+1), 2) if abs(sum(a*b for a, b in zip(xs[i], xs[j]))) == 1.0)
    zeros = sum(1 for i, j in itertools.combinations(range(d+1), 2) if sum(a*b for a, b in zip(xs[i], xs[j])) == 0.0)
    print("  orth+repeat d=%d: pairs with |g|=1: %d, pairs with g=0: %d of %d  => T = pi/2 exactly, S = (C(d+1,2)-1)pi/2" % (d, ones, zeros, (d+1)*d//2))
worst = 0.0
for trial in range(2000):
    g1 = random.random()*PI2; g2 = random.uniform(max(0.0, PI2-g1), PI2)  # g3 = pi - g1 - g2 <= pi/2
    ang = [0.0, g1, g1+g2]
    xs = [[math.cos(t), math.sin(t)] for t in ang]
    S = sum(math.acos(min(1.0, abs(sum(a*b for a, b in zip(xs[i], xs[j]))))) for i, j in itertools.combinations(range(3), 2))
    worst = max(worst, abs(S - math.pi))
print("  d=2 gap family (all gaps <= pi/2), 2000 samples: max |S - pi| = %.3e" % worst)
xs = [[math.cos(t), math.sin(t)] for t in (0, math.pi/3, 2*math.pi/3)]
print("  60-degree triple: T - pi/2 = %.3e" % (Tval(xs) - PI2))
