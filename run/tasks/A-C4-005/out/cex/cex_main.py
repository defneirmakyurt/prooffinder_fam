"""Referee A-C4-005: counterexample search for the target (floating point; EVIDENCE ONLY).
(a) 5 lines in R^3 vs 4pi, (b) 6 lines in R^4 vs 13pi/2.
 - 200000 uniformly random configurations each;
 - 150 random restarts of adaptive hill climbing (4000 steps, one line moved at a time);
 - 100 restarts started near each S2 extremiser (perturbation 0.2) to probe for a nearby ascent direction.
Report max S found minus bound."""
import math, random
random.seed(31415)
def unit(v):
    n=math.sqrt(sum(a*a for a in v)); return [a/n for a in v]
def S(X):
    t=0.0
    for i in range(len(X)):
        for j in range(i+1,len(X)):
            t+=math.acos(min(1.0,abs(sum(a*b for a,b in zip(X[i],X[j])))))
    return t
def climb(X, iters=4000, step=0.4):
    X=[x[:] for x in X]; cur=S(X)
    for it in range(iters):
        k=random.randrange(len(X)); old=X[k]
        X[k]=unit([a+step*random.gauss(0,1) for a in old]); new=S(X)
        if new>=cur: cur=new
        else: X[k]=old
        if it%400==399: step*=0.6
    return cur
h=math.sqrt(3)/2
starts={ (5,3): [[[1,0,0],[1,0,0],[0,1,0],[0,1,0],[0,0,1]], [[1,0,0],[.5,h,0],[-.5,h,0],[0,0,1],[0,0,1]]],
         (6,4): [[[1,0,0,0],[1,0,0,0],[0,1,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]],
                 [[1,0,0,0],[.5,h,0,0],[-.5,h,0,0],[0,0,1,0],[0,0,.5,h],[0,0,-.5,h]]] }
for (N,d),bound,name in (((5,3),4*math.pi,"4pi"),((6,4),6.5*math.pi,"13pi/2")):
    rnd=max(S([unit([random.gauss(0,1) for _ in range(d)]) for _ in range(N)]) for _ in range(200000))
    hc=max(climb([unit([random.gauss(0,1) for _ in range(d)]) for _ in range(N)]) for _ in range(150))
    near=-1e9
    for X0 in starts[(N,d)]:
        for _ in range(50):
            X=[unit([a+0.2*random.gauss(0,1) for a in x]) for x in X0]
            near=max(near, climb(X, 3000, 0.1))
    print(f"N={N} d={d} bound {name}: random max - bound = {rnd-bound:.3e}; hill-climb max - bound = {hc-bound:.3e}; near-extremiser climb max - bound = {near-bound:.3e}")
