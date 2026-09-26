"""EVIDENCE ONLY (floating point; no proof step rests on this script). Stdlib only.
Checks, on random samples:
 (a) target: for d+1 random unit vectors in R^d, T = sum_{i<j} arcsin|<x_i,x_j>| >= pi/2
     (equivalently S <= (C(d+1,2)-1) pi/2), for d = 1..8;
 (b) Lemma L: sum_j sin a_j cos(D - a_j) <= sin D  for a_j >= 0, D = sum a_j <= pi/2;
 (c) Key Lemma (R4): for alpha_ij >= 0 with T = sum alpha < pi/2, p_i = sin(D_i + pi/2 - T),
     sum_{j != i} sin(alpha_ij) p_j < p_i for every i.
Reports the minimum slack seen in each test (a negative slack beyond ~1e-12 would be a red flag)."""
import math, random, itertools
random.seed(20260926)
def unit(d):
    while True:
        v=[random.gauss(0,1) for _ in range(d)]
        s=math.sqrt(sum(t*t for t in v))
        if s>1e-9: return [t/s for t in v]
# (a)
mins={}
for d in range(1,9):
    m=float('inf')
    for trial in range(3000):
        mode=random.random()
        xs=[unit(d) for _ in range(d+1)]
        if mode<0.3 and d>=2:
            # push toward near-degenerate: many vectors near coordinate axes
            for k in range(d+1):
                ax=random.randrange(d); eps=random.random()*0.3
                v=[eps*random.gauss(0,1) for _ in range(d)]; v[ax]+=1
                s=math.sqrt(sum(t*t for t in v)); xs[k]=[t/s for t in v]
        T=0.0
        for i,j in itertools.combinations(range(d+1),2):
            g=abs(sum(a*b for a,b in zip(xs[i],xs[j])))
            T+=math.asin(min(1.0,g))
        m=min(m,T-math.pi/2)
    mins[d]=m
print("(a) min over samples of T - pi/2, by d:",{d:round(v,6) for d,v in mins.items()})
# (b)
m=float('inf')
for trial in range(20000):
    k=random.randint(1,6); w=[random.random()*(random.random()<0.8) for _ in range(k)]
    D=random.random()*math.pi/2
    s=sum(w)
    a=[D*t/s for t in w] if s>0 else [0.0]*k
    D=sum(a)
    m=min(m,math.sin(D)-sum(math.sin(t)*math.cos(D-t) for t in a))
print("(b) min slack of Lemma L:",m)
# (c)
m=float('inf')
for trial in range(20000):
    n=random.randint(2,7); pairs=list(itertools.combinations(range(n),2))
    w=[random.random()*(random.random()<0.6) for _ in pairs]
    s=sum(w)
    if s==0: continue
    T=random.random()*math.pi/2*0.999999
    al={}
    for (i,j),t in zip(pairs,w): al[(i,j)]=al[(j,i)]=T*t/s
    Dv=[sum(al[(i,j)] for j in range(n) if j!=i) for i in range(n)]
    sl=math.pi/2-T
    p=[math.sin(Dv[i]+sl) for i in range(n)]
    for i in range(n):
        lhs=sum(math.sin(al[(i,j)])*p[j] for j in range(n) if j!=i)
        m=min(m,(p[i]-lhs)/p[i])
print("(c) min relative slack of Key Lemma (should be > 0):",m)
