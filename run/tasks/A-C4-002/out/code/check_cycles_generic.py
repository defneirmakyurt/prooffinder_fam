# EVIDENCE ONLY (floating point). Not part of the proof in out/proof.md. stdlib-only.
# Independent of the parametrisations in Lemmas 7/8: build n-cycle configurations in R^(n-2) (n=5,6)
# by gradient descent on sum of squared inner products of non-adjacent pairs from random starts,
# then check that the edge-deficit sum D = sum arcsin|<y_i,y_{i+1}>| is >= pi (up to float error).
from math import *
import random
random.seed(7)
def unit(v):
    l=sqrt(sum(a*a for a in v)); return [a/l for a in v]
def dot(u,v): return sum(a*b for a,b in zip(u,v))
for n in (5,6):
    d=n-2
    pairs=[(i,j) for i in range(n) for j in range(i+1,n) if (j-i)%n not in (1,n-1)]
    worst=9; cnt=0
    for trial in range(300):
        X=[unit([random.gauss(0,1) for _ in range(d)]) for _ in range(n)]
        for it in range(4000):
            G=[[0.0]*d for _ in range(n)]
            for (i,j) in pairs:
                c=dot(X[i],X[j])
                for t in range(d):
                    G[i][t]+=c*X[j][t]; G[j][t]+=c*X[i][t]
            X=[unit([X[i][t]-0.3*G[i][t] for t in range(d)]) for i in range(n)]
        res=max(abs(dot(X[i],X[j])) for (i,j) in pairs)
        if res>1e-10: continue
        edges=[abs(dot(X[i],X[(i+1)%n])) for i in range(n)]
        if min(edges)<1e-6: continue
        cnt+=1
        D=sum(asin(min(1,e)) for e in edges)
        worst=min(worst,D-pi)
    print("n=%d: %d valid cycle configurations, min(D-pi)=%.3e"%(n,cnt,worst))
