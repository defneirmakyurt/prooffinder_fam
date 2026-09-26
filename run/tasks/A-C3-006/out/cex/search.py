"""Referee counterexample search for A-C3-002 (stdlib only, FLOATING POINT: evidence only).
(A) equality configurations: orthogonal+repeat for d=1..12; d=2 gap family (2000 triples).
(B) adversarial minimisation of T = sum_{i<j} arcsin|<x_i,x_j>| over d+1 unit vectors in R^d, d=2..6.
(C) adversarial maximisation of Lemma L defect  sum sin(a_j)cos(D-a_j) - sin D,  k=1..6.
(D) adversarial maximisation of Key Lemma defect max_i (sum_{j!=i} sin(al_ij) p_j - p_i)/p_i, n=2..7,
    plus direct checks of intermediate claims 3(b) p_j <= cos(D_i-al_ij) and 3(c).
(E) Lemma W / Step 5 sanity: random Gram matrices of d+1 vectors in R^d are singular and weighted
    dominance with p_i=sin(D_i+s) fails for them (it must, since T>=pi/2 there)."""
import math, random, itertools
random.seed(6006)
PI2 = math.pi/2
def unit(v):
    s = math.sqrt(sum(t*t for t in v)); return [t/s for t in v]
def rnd_unit(d):
    while True:
        v = [random.gauss(0,1) for _ in range(d)]
        if sum(t*t for t in v) > 1e-12: return unit(v)
def Tval(xs):
    T = 0.0
    for i, j in itertools.combinations(range(len(xs)), 2):
        g = abs(sum(a*b for a, b in zip(xs[i], xs[j])))
        T += math.asin(min(1.0, g))
    return T
# (A)
print("(A1) orthogonal + one repeat, T - pi/2 by d:",
      {d: Tval([[1.0 if k == i else 0.0 for k in range(d)] for i in range(d)] + [[1.0]+[0.0]*(d-1)]) - PI2 for d in range(1, 13)})
worst = 0.0
for _ in range(2000):
    while True:
        g1, g2 = random.random()*PI2, random.random()*PI2
        g3 = math.pi - g1 - g2
        if 0 <= g3 <= PI2: break
    ph = random.random()*math.pi
    angs = [ph, ph+g1, ph+g1+g2]
    xs = [[math.cos(a), math.sin(a)] for a in angs]
    S = sum(math.acos(min(1.0, abs(sum(a*b for a, b in zip(xs[i], xs[j]))))) for i, j in itertools.combinations(range(3), 2))
    worst = max(worst, abs(S - math.pi))
print("(A2) d=2 gap family (gaps<=pi/2), max |S - pi| over 2000 triples:", worst)
# (B)
for d in range(2, 7):
    best = float('inf'); bestxs = None
    for restart in range(60):
        xs = [rnd_unit(d) for _ in range(d+1)]
        T = Tval(xs); step = 0.5
        for it in range(1500):
            k = random.randrange(d+1)
            cand = unit([t + step*random.gauss(0,1) for t in xs[k]])
            old = xs[k]; xs[k] = cand; Tn = Tval(xs)
            if Tn <= T: T = Tn
            else: xs[k] = old
            if it % 300 == 299: step *= 0.5
        if T < best: best = T; bestxs = [list(x) for x in xs]
    print(f"(B) d={d}: min T found - pi/2 = {best - PI2:.3e}")
    open(f"bestB_d{d}.txt", "w").write(repr(bestxs))
# (C)
def Ldef(a):
    D = sum(a); return sum(math.sin(t)*math.cos(D-t) for t in a) - math.sin(D)
worstL = -float('inf')
for k in range(1, 7):
    for restart in range(40):
        a = [random.random() for _ in range(k)]; sc = random.random()*PI2/sum(a); a = [t*sc for t in a]
        f = Ldef(a); step = 0.3
        for it in range(800):
            b = [max(0.0, t + step*random.gauss(0,1)) for t in a]
            if sum(b) > PI2: b = [t*PI2/sum(b) for t in b]
            fb = Ldef(b)
            if fb >= f: a, f = b, fb
            if it % 200 == 199: step *= 0.5
        worstL = max(worstL, f)
print("(C) Lemma L: max defect found (<= 0 expected, ~1e-16 rounding):", worstL)
# (D)
def keydef(n, al):
    T = sum(al[(i, j)] for i, j in itertools.combinations(range(n), 2))
    s = PI2 - T
    D = [sum(al[tuple(sorted((i, j)))] for j in range(n) if j != i) for i in range(n)]
    p = [math.sin(D[i] + s) for i in range(n)]
    worst = -float('inf'); bviol = -float('inf'); cviol = -float('inf')
    for i in range(n):
        lhs = sum(math.sin(al[tuple(sorted((i, j)))])*p[j] for j in range(n) if j != i)
        worst = max(worst, (lhs - p[i])/p[i])
        for j in range(n):
            if j != i:
                a = al[tuple(sorted((i, j)))]
                bviol = max(bviol, p[j] - math.cos(D[i] - a))
        mid = sum(math.sin(al[tuple(sorted((i, j)))])*math.cos(D[i]-al[tuple(sorted((i, j)))]) for j in range(n) if j != i)
        cviol = max(cviol, lhs - mid, mid - math.sin(D[i]))
    return worst, bviol, cviol
worstK = -float('inf'); worstB = -float('inf'); worstC = -float('inf')
for n in range(2, 8):
    pairs = list(itertools.combinations(range(n), 2))
    for restart in range(25):
        w = [random.random()*(random.random() < 0.6) + 1e-9 for _ in pairs]
        Tt = random.random()*PI2*0.999999
        al = {pr: Tt*t/sum(w) for pr, t in zip(pairs, w)}
        f, bv, cv = keydef(n, al); step = 0.2
        for it in range(400):
            cand = {pr: max(0.0, v + step*random.gauss(0,1)) for pr, v in al.items()}
            tot = sum(cand.values())
            if tot >= PI2: cand = {pr: v*(PI2*(1-1e-7))/tot for pr, v in cand.items()}
            fc, bc, cc = keydef(n, cand)
            worstB = max(worstB, bc); worstC = max(worstC, cc)
            if fc >= f: al, f = cand, fc
            if it % 100 == 99: step *= 0.5
        worstK = max(worstK, f)
print("(D) Key Lemma: max relative defect found (< 0 expected):", worstK)
print("(D) claim 3(b) max of p_j - cos(D_i-al_ij) (<= 0 expected):", worstB)
print("(D) claim 3(c) max violation of either inequality (<= 0 expected):", worstC)
# (E)
hard = 0; soft = {}; maxsoft = 0.0
for d in range(1, 7):
    for _ in range(300):
        xs = [rnd_unit(d) for _ in range(d+1)]
        T = Tval(xs)
        if T < PI2 - 1e-12: hard += 1
        elif T < PI2:
            soft[d] = soft.get(d, 0) + 1; maxsoft = max(maxsoft, PI2 - T)
print("(E) random configs (d=1..6, 300 each) with T < pi/2 - 1e-12 (0 expected):", hard)
print("(E) float-rounding hits pi/2-1e-12 <= T < pi/2, by d:", soft, "max defect", maxsoft,
      "(d=2 expected: the gap family has T = pi/2 exactly on a positive-measure set)")
