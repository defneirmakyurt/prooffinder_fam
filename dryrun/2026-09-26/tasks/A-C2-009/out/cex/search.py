"""Referee counterexample search for A-C2 (chain orthogonality lemma).
(A) General random admissible chains in R^(m-1), m=2..9: x_1 random unit; x_{k+1} random unit in V_{k-1}^perp
    (the most general admissible choice). 50-digit mpmath. Checks: target, Step-1 recursion (when t_k>0),
    and the induction claim Q(k): t_k >= cos psi_{k-1} whenever psi_{k-1} < pi/2.
(B) Adversarial hill-climb (floats, then mpmath recheck of best) maximizing chain sum, m=3..6.
(C) Exact (sympy) check of S2 equality tuples, m=2..8, and exact check of the Step-3 identity.
(D) Interval check (mpmath.iv) of the trig lemma on a 200x200 grid of rational boxes.
"""
import random, math
import mpmath as mp
from mpmath import mpf
mp.mp.dps = 50
rng = random.Random(2026)

def dot(u,v): return mp.fsum(a*b for a,b in zip(u,v))
def nrm(u): return mp.sqrt(dot(u,u))
def proj_out(v, basis):
    r = list(v)
    for b in basis:
        c = dot(r,b); r = [ri - c*bi for ri,bi in zip(r,b)]
    return r
def onb(vecs, tol=mpf(10)**-35):
    B=[]
    for v in vecs:
        r = proj_out(proj_out(v,B),B)
        n = nrm(r)
        if n > tol: B.append([ri/n for ri in r])
    return B

def rand_unit_in_perp(n, basis):
    while True:
        g = [mpf(rng.gauss(0,1)) for _ in range(n)]
        r = proj_out(proj_out(g,basis),basis)
        if nrm(r) > mpf('1e-6'): return [ri/nrm(r) for ri in r]

def gen_chain(m, special=False):
    n = m-1
    xs=[]
    for k in range(m):
        B = onb(xs[:max(0,k-1)])  # V_{k-1} in 1-based terms: span of x_1..x_{k-1}
        if special and k>=1 and rng.random()<0.3:
            # push toward parallel to previous (projected), when possible
            r = proj_out(proj_out(xs[k-1],B),B)
            if nrm(r)>mpf('1e-20'):
                x=[ri/nrm(r) for ri in r]
                if rng.random()<0.5: x=[-a for a in x]
                xs.append(x); continue
        if len(B) >= n: return None
        xs.append(rand_unit_in_perp(n,B))
    return xs

def theta(x,y): return mp.acos(min(mpf(1),abs(dot(x,y))))

def check(xs):
    m=len(xs)
    for i in range(m):
        for j in range(i+2,m):
            assert abs(dot(xs[i],xs[j]))<mpf(10)**-40
    s = mp.fsum(theta(xs[i],xs[i+1]) for i in range(m-1))
    slack = (m-2)*mp.pi/2 - s
    # t_k and psi
    t=[]; 
    for k in range(m):
        B=onb(xs[:k]); h=proj_out(proj_out(xs[k],B),B); t.append(nrm(h))
    psi=[mpf(0)]
    for k in range(m-1):
        a=abs(dot(xs[k],xs[k+1])); psi.append(psi[-1]+mp.asin(min(mpf(1),a)))
    qviol=mpf(0); rviol=mpf(0)
    for k in range(m):
        if psi[k] < mp.pi/2 - mpf(10)**-30:
            qviol=max(qviol, mp.cos(psi[k]) - t[k])
        if k<m-1 and t[k]>mpf(10)**-20:
            a=dot(xs[k],xs[k+1]); rviol=max(rviol, abs(t[k+1]**2 - (1-a*a/t[k]**2)))
    mint=min(t)
    return slack,qviol,rviol,mint

def partA():
    worst=None; worstq=mpf(-1); worstr=mpf(0); cnt=0; maxmint=mpf(0)
    for m in range(2,10):
        for it in range(400):
            xs=gen_chain(m, special=(it%2==1))
            if xs is None: continue
            sl,q,r,mt=check(xs); cnt+=1
            worst = sl if worst is None or sl<worst else worst
            worstq=max(worstq,q); worstr=max(worstr,r); maxmint=max(maxmint,mt)
    print("A: chains",cnt,"min slack (bound - sum)",mp.nstr(worst,8),
          " max Q(k) violation",mp.nstr(worstq,5)," max Step1 residual",mp.nstr(worstr,5),
          " max over chains of min_k t_k",mp.nstr(maxmint,5))

def fchain(params, m):
    # parametrize: x_{k+1} = unit in V_{k-1}^perp given by params (floats), via mp at low prec
    n=m-1; xs=[]; p=0
    for k in range(m):
        B=onb(xs[:max(0,k-1)])
        g=[mpf(params[p+i]) for i in range(n)]; p+=n
        r=proj_out(proj_out(g,B),B)
        if nrm(r)<mpf('1e-12') or len(B)>=n: return None
        xs.append([ri/nrm(r) for ri in r])
    return xs

def partB():
    mp.mp.dps=20
    out=[]
    for m in range(3,7):
        best=-1e9; bp=None
        for restart in range(6):
            params=[rng.gauss(0,1) for _ in range(m*(m-1))]
            xs=fchain(params,m); cur = -1e9 if xs is None else float(mp.fsum(theta(xs[i],xs[i+1]) for i in range(m-1)))
            step=0.5
            for it in range(400):
                q=[a+rng.gauss(0,step) for a in params]
                xs=fchain(q,m)
                if xs is None: continue
                v=float(mp.fsum(theta(xs[i],xs[i+1]) for i in range(m-1)))
                if v>cur: cur=v; params=q
                else: step=max(step*0.995,1e-4)
            if cur>best: best=cur; bp=params
        out.append((m,best,(m-2)*math.pi/2))
    mp.mp.dps=50
    for m,b,bd in out:
        print("B: m=%d best chain sum found %.12f  bound %.12f  gap %.3e"%(m,b,bd,bd-b))

def partC():
    import sympy as sp
    for m in range(2,9):
        n=m-1
        E=[sp.Matrix([1 if i==j else 0 for i in range(n)]) for j in range(n)]
        xs=[E[k] for k in range(m-1)]+[E[m-2]]
        for i in range(m):
            for j in range(i+2,m): assert (xs[i].T*xs[j])[0]==0
        s=sum(sp.acos(abs((xs[i].T*xs[i+1])[0])) for i in range(m-1))
        assert sp.simplify(s-(m-2)*sp.pi/2)==0
    print("C: S2 tuples (e1..e_{m-1}, e_{m-1}) exact equality for m=2..8: OK")
    ps,ph=sp.symbols('psi phi')
    d=sp.cos(ps)*sp.sin(ps+ph)-sp.sin(ph)-sp.cos(ps+ph)*sp.sin(ps)
    print("C: Step-3 identity cos psi sin(psi+phi) - sin phi == cos(psi+phi) sin psi:", sp.simplify(sp.expand_trig(d))==0)

def partD():
    iv=mp.iv; iv.dps=30; N=200; bad=0; tested=0
    half=iv.pi/2
    for i in range(N):
        for j in range(N-i):
            psi=iv.mpf([mp.mpf(i)/N, mp.mpf(i+1)/N])*half
            phi=iv.mpf([mp.mpf(j)/N, mp.mpf(j+1)/N])*half
            # difference = cos(psi+phi)*sin(psi); lower bound must be >= 0 when psi+phi<=pi/2
            d=iv.cos(psi+phi)*iv.sin(psi)
            tested+=1
            if d.a < -mp.mpf(10)**-25: bad+=1
    print("D: interval boxes tested",tested,"with certified-negative lower bound beyond 1e-25:",bad)

partC(); partD(); partA(); partB()
