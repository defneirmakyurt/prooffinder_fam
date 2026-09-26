# EVIDENCE ONLY (floating point). Not part of the proof in out/proof.md. stdlib-only.
# Random-restart hill climbing for max S; usage: python3 hillclimb.py N d seed. Expect best S just below (C(N,2)-2)pi/2.
from math import *
import random, sys
random.seed(int(sys.argv[3]) if len(sys.argv)>3 else 0)
N=int(sys.argv[1]); d=int(sys.argv[2])
def unit(v):
    l=sqrt(sum(a*a for a in v)); return [a/l for a in v]
def S(X):
    t=0
    for i in range(N):
        for j in range(i+1,N):
            c=abs(sum(a*b for a,b in zip(X[i],X[j])))
            t+=acos(min(1,c))
    return t
best=0
for rs in range(60):
    X=[unit([random.gauss(0,1) for _ in range(d)]) for _ in range(N)]
    cur=S(X); step=0.5
    for it in range(6000):
        k=random.randrange(N)
        old=X[k]
        X[k]=unit([a+step*random.gauss(0,1) for a in old])
        v=S(X)
        if v>=cur: cur=v
        else: X[k]=old
        if it%500==499: step*=0.6
    best=max(best,cur)
print(N,d,"best S found",best,"bound",(comb(N,2)-2)*pi/2,"excess",best-(comb(N,2)-2)*pi/2)
