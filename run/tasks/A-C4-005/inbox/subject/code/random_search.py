"""Random-restart hill climbing for max S (floating point; EVIDENCE ONLY).
Reports the best S found for 5 lines in R^3 and 6 lines in R^4, versus 4*pi and 13*pi/2."""
import math, random
random.seed(7)
def unit(v):
    n=math.sqrt(sum(a*a for a in v)); return [a/n for a in v]
def S(X):
    t=0.0
    for i in range(len(X)):
        for j in range(i+1,len(X)):
            t+=math.acos(min(1.0,abs(sum(a*b for a,b in zip(X[i],X[j])))))
    return t
def climb(N,d,iters=6000):
    X=[unit([random.gauss(0,1) for _ in range(d)]) for _ in range(N)]
    cur=S(X); step=0.5
    for it in range(iters):
        k=random.randrange(N)
        old=X[k]; X[k]=unit([a+step*random.gauss(0,1) for a in old])
        new=S(X)
        if new>=cur: cur=new
        else: X[k]=old
        if it%500==499: step*=0.6
    return cur
for N,d,bound,name in ((5,3,4*math.pi,"4pi"),(6,4,6.5*math.pi,"13pi/2")):
    best=max(climb(N,d) for _ in range(40))
    print(f"N={N} d={d}: best S found = {best:.10f}, bound {name} = {bound:.10f}, excess = {best-bound:.3e}")
