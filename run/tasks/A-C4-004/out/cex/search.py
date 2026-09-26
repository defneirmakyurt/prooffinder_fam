"""Referee A-C4-004 independent checks (evidence only except part 1, which uses arb balls).
1. S2 equality configurations evaluated with python-flint arb (rigorous enclosures).
2. Random + clustered + perturbed-extremiser configurations: D(x) >= pi (i.e. S <= bound), floats.
3. Independent hill climbing (different moves/seeds) for max S.
4. Own 5-cycle construction in R^3 (cross products): D = pi + F(u), sin/cos formulas of 7.3, D >= pi.
5. Own 6-cycle construction in R^4 (random rotation of A+B): Step 8.3 formulas, (8.3.1), 8.5 sign, D >= pi.
6. Tridiagonal rank claim 5.2 on random instances; Lemma T concavity on random (alpha,beta,I).
"""
import math, random, sys
from flint import arb, arb_mat
random.seed(20260926)
PI = math.pi
def dot(u,v): return sum(a*b for a,b in zip(u,v))
def unit(v):
    n = math.sqrt(dot(v,v)); return [a/n for a in v]
def phi(u,v): return math.asin(min(1.0, abs(dot(u,v))))
def Dsum(X): return sum(phi(X[i],X[j]) for i in range(len(X)) for j in range(i+1,len(X)))
def Ssum(X): return sum(math.acos(min(1.0,abs(dot(X[i],X[j])))) for i in range(len(X)) for j in range(i+1,len(X)))

# ---- 1. S2 configurations with arb
def S_arb(X):
    t = arb(0)
    for i in range(len(X)):
        for j in range(i+1,len(X)):
            ip = sum((X[i][k]*X[j][k] for k in range(len(X[i]))), arb(0))
            t += abs(ip).acos() if not (abs(ip) > 1) else arb(0)
    return t
z = arb(0); o = arb(1); h = arb(1)/2; r3 = arb(3).sqrt()/2
cfgA1 = [[o,z,z],[o,z,z],[z,o,z],[z,o,z],[z,z,o]]
cfgA2 = [[o,z,z],[h,r3,z],[-h,r3,z],[z,z,o],[z,z,o]]
cfgB1 = [[o,z,z,z],[o,z,z,z],[z,o,z,z],[z,o,z,z],[z,z,o,z],[z,z,z,o]]
cfgB2 = [[o,z,z,z],[h,r3,z,z],[-h,r3,z,z],[z,z,o,z],[z,z,h,r3],[z,z,-h,r3]]
P = arb.pi()
for name,X,bd in (("A axes e1,e1,e2,e2,e3",cfgA1,4*P),("A 60deg triple + z twice",cfgA2,4*P),
                  ("B axes e1,e1,e2,e2,e3,e4",cfgB1,13*P/2),("B two 60deg triples",cfgB2,13*P/2)):
    s = S_arb(X); diff = s - bd
    print(f"[1] {name}: S-bound = {diff}  contains0={diff.contains(0)}")

# ---- 2. random configurations
def rand_unit(d): return unit([random.gauss(0,1) for _ in range(d)])
def perturb(X, eps): return [unit([a+eps*random.gauss(0,1) for a in x]) for x in X]
fl = {3:[[1,0,0],[1,0,0],[0,1,0],[0,1,0],[0,0,1]], 4:[[1,0,0,0],[1,0,0,0],[0,1,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]}
fl60 = {3:[[1,0,0],[.5,math.sqrt(3)/2,0],[-.5,math.sqrt(3)/2,0],[0,0,1],[0,0,1]],
        4:[[1,0,0,0],[.5,math.sqrt(3)/2,0,0],[-.5,math.sqrt(3)/2,0,0],[0,0,1,0],[0,0,.5,math.sqrt(3)/2],[0,0,-.5,math.sqrt(3)/2]]}
for d in (3,4):
    N = d+2; worst = 1e9; cnt = 0
    for trial in range(60000):
        kind = trial % 4
        if kind == 0: X = [rand_unit(d) for _ in range(N)]
        elif kind == 1:  # clustered: few directions with small noise
            base = [rand_unit(d) for _ in range(random.randint(1,d))]
            X = [unit([a+0.05*random.gauss(0,1) for a in random.choice(base)]) for _ in range(N)]
        elif kind == 2: X = perturb(fl[d], 10**random.uniform(-6,-1))
        else: X = perturb(fl60[d], 10**random.uniform(-6,-1))
        cnt += 1; worst = min(worst, Dsum(X) - PI)
    print(f"[2] d={d} N={N}: {cnt} configs, min(D - pi) = {worst:.3e}  (negative would be a counterexample)")

# ---- 3. hill climbing (rotation moves on single vector, adaptive step)
def climb(N,d,iters):
    X = [rand_unit(d) for _ in range(N)]; cur = Ssum(X); step = 1.0
    for it in range(iters):
        k = random.randrange(N); old = X[k]
        X[k] = unit([a+step*random.gauss(0,1) for a in old]); new = Ssum(X)
        if new >= cur: cur = new
        else: X[k] = old
        if it % 400 == 399: step = max(step*0.7, 1e-7)
    return cur
for d,bd,nm in ((3,4*PI,"4pi"),(4,6.5*PI,"13pi/2")):
    best = max(climb(d+2,d,8000) for _ in range(60))
    print(f"[3] d={d}: best S = {best:.12f}, bound {nm} = {bd:.12f}, excess = {best-bd:.3e}")

# ---- 4. 5-cycles in R^3, own construction: y3,y4 random, y1 = y3 x y4, y5 in y3^perp, y2 = y4 x y5
def cross(a,b): return [a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0]]
def F(u,v): return u+v-math.acos(math.cos(u)*math.cos(v))-math.asin(math.sin(u)*math.sin(v)/(1+math.cos(u)*math.cos(v)))
maxerr = 0; worst = 1e9; n = 0
for _ in range(100000):
    y3 = rand_unit(3); y4 = rand_unit(3)
    y1 = unit(cross(y3,y4))
    q = unit(cross(y3, rand_unit(3))); qq = cross(y3,q); ang = random.uniform(0,2*PI)
    y5 = [math.cos(ang)*a+math.sin(ang)*b for a,b in zip(q,qq)]
    c = cross(y4,y5)
    if dot(c,c) < 1e-12: continue
    y2 = unit(c)
    Y = [y1,y2,y3,y4,y5]
    for i in range(5):
        assert abs(dot(Y[i],Y[(i+2)%5])) < 1e-9
    ph = [phi(Y[i],Y[(i+1)%5]) for i in range(5)]
    if min(ph) < 1e-7 or max(ph) > PI/2-1e-7: continue
    n += 1; u, v = ph[2], ph[4]; cc = math.sqrt(1-math.cos(u)**2*math.cos(v)**2)
    e = max(abs(sum(ph)-(PI+F(u,v))), abs(math.sin(ph[0])-math.sin(u)*math.cos(v)/cc),
            abs(math.cos(ph[0])-math.sin(v)/cc), abs(math.sin(ph[1])-math.cos(u)*math.sin(v)/cc),
            abs(math.sin(ph[3])-math.cos(u)*math.cos(v)))
    maxerr = max(maxerr, e); worst = min(worst, sum(ph)-PI)
print(f"[4] 5-cycles: {n} tested, max formula error = {maxerr:.3e}, min(D-pi) = {worst:.3e}")
# F >= 0 on a fine grid (floats, evidence)
mF = min(F(PI/2*i/600, PI/2*j/600) for i in range(601) for j in range(1,600))
print(f"[4] grid min F on [0,pi/2]x(0,pi/2) (601x599) = {mF:.3e}")

# ---- 5. 6-cycles in R^4, own construction: random orthonormal basis f1..f4; A=span(f1,f2), B=span(f3,f4)
def rand_onb(d):
    B = []
    while len(B) < d:
        v = rand_unit(d)
        for b in B: v = [a-dot(v,b)*bb for a,bb in zip(v,b)]
        if dot(v,v) > 1e-6: B.append(unit(v))
    return B
def comb(cs, vs): return [sum(c*v[i] for c,v in zip(cs,vs)) for i in range(len(vs[0]))]
maxerr = 0; worst = 1e9; n = 0; signbad = 0
for _ in range(100000):
    f = rand_onb(4)
    a2,a3,b5,b6 = [random.uniform(0,2*PI) for _ in range(4)]
    y2 = comb([math.cos(a2),math.sin(a2)],f[0:2]); y3 = comb([math.cos(a3),math.sin(a3)],f[0:2])
    y5 = comb([math.cos(b5),math.sin(b5)],f[2:4]); y6 = comb([math.cos(b6),math.sin(b6)],f[2:4])
    n2 = comb([-math.sin(a2),math.cos(a2)],f[0:2]); n3 = comb([-math.sin(a3),math.cos(a3)],f[0:2])
    n5 = comb([-math.sin(b5),math.cos(b5)],f[2:4]); n6 = comb([-math.sin(b6),math.cos(b6)],f[2:4])
    th = random.uniform(0,2*PI)
    y1 = [math.cos(th)*p+math.sin(th)*q for p,q in zip(n3,n5)]
    # y4 in span(n2,n6) orthogonal to y1
    al_, be_ = dot(n2,y1), dot(n6,y1)
    if al_*al_+be_*be_ < 1e-14: continue
    y4 = unit([-be_*p+al_*q for p,q in zip(n2,n6)])
    Y = [y1,y2,y3,y4,y5,y6]
    ok = all(abs(dot(Y[i],Y[j])) < 1e-9 for i in range(6) for j in range(i+1,6) if (j-i)%6 not in (1,5))
    assert ok
    ph = [phi(Y[i],Y[(i+1)%6]) for i in range(6)]
    if min(ph) < 1e-7 or max(ph) > PI/2-1e-7: continue
    n += 1
    a, b = ph[1], ph[4]
    s = math.atan2(abs(dot(y1,n5)), abs(dot(y1,n3))); t = math.atan2(abs(dot(y4,n6)), abs(dot(y4,n2)))
    e = max(abs(math.sin(ph[0])-math.cos(s)*math.cos(a)), abs(math.sin(ph[2])-math.cos(t)*math.cos(a)),
            abs(math.sin(ph[3])-math.sin(t)*math.cos(b)), abs(math.sin(ph[5])-math.sin(s)*math.cos(b)),
            abs(math.cos(s)*math.cos(t)*math.sin(a)-math.sin(s)*math.sin(t)*math.sin(b)))
    maxerr = max(maxerr, e)
    if (a-b)*(s+t-PI/2) < -1e-9: signbad += 1
    fr = lambda r: math.asin(math.cos(a)*math.cos(r))+math.asin(math.cos(b)*math.sin(r))
    lb = PI + (a-b)*(2*(s+t)/PI-1)
    assert sum(ph) >= lb - 1e-9, (sum(ph), lb)
    worst = min(worst, sum(ph)-PI)
print(f"[5] 6-cycles: {n} tested, max formula error = {maxerr:.3e}, 8.5 sign violations = {signbad}, min(D-pi) = {worst:.3e}")

# ---- 6. tridiagonal rank (5.2) and Lemma T concavity
bad = 0
for _ in range(3000):
    m = random.randint(2,7)
    # build chain with Gram tridiagonal: random symmetric tridiagonal with small off-diagonals -> PSD Gram -> check rank >= m-1
    off = [random.choice([-1,1])*random.uniform(0.01,0.49) for _ in range(m-1)]
    G = arb_mat(m,m)
    for i in range(m): G[i,i] = 1
    for i in range(m-1): G[i,i+1] = off[i]; G[i+1,i] = off[i]
    # delete row 0 and last column: upper-triangular minor determinant = prod of off-diagonals != 0
    M = arb_mat(m-1,m-1)
    for r_ in range(m-1):
        for c_ in range(m-1): M[r_,c_] = G[r_+1,c_]
    dm = M.det()
    if dm.contains(0): bad += 1
print(f"[6] 5.2 minor nonzero check: {bad} failures out of 3000")
badT = 0
for _ in range(20000):
    A = random.uniform(0,1)**0.3; sg = random.uniform(0,2*PI)
    al, be = A*math.cos(sg), A*math.sin(sg)
    g = lambda s_: al*math.cos(s_)+be*math.sin(s_)
    # interval where g >= 0: around sg, width < pi
    lo = sg - random.uniform(0,PI/2); hi = sg + random.uniform(0,PI/2)
    for _k in range(5):
        x1, x2 = sorted([random.uniform(lo,hi), random.uniform(lo,hi)]); lam = random.random()
        xm = lam*x1+(1-lam)*x2
        ps = lambda s_: math.asin(max(-1,min(1,g(s_))))
        if ps(xm) < lam*ps(x1)+(1-lam)*ps(x2) - 1e-12: badT += 1
print(f"[6] Lemma T concavity violations: {badT} out of 100000 triples")
