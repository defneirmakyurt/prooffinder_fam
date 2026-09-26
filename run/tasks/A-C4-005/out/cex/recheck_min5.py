"""Re-run the 5-cycle minimisation of referee_checks.py section 5 (float search), then recompute the best
configuration's D in mpmath (60 digits), rebuilding the cycle exactly-orthogonal in high precision from the
same generators. Tests whether the float value D - pi = -2e-9 is rounding (near-degenerate cycle)."""
import math, random
import mpmath as mp
mp.mp.dps = 60
random.seed(99)
def dot(u,v): return sum(a*b for a,b in zip(u,v))
def unit(v):
    n=math.sqrt(dot(v,v)); return [a/n for a in v]
def cross(a,b): return [a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0]]
def phi(u,v): return math.asin(min(1.0,abs(dot(u,v))))
def build(p, U=unit, D=dot):
    y1=U(p[0:3]); y2=U(p[3:6]); z=p[6:9]; c=D(z,y1); y3=U([zi-c*a for zi,a in zip(z,y1)])
    return [y1,y2,y3,U(cross(y1,y2)),U(cross(y2,y3))]
def Dm(Y): return sum(phi(Y[i],Y[(i+1)%5]) for i in range(5))
def munit(v):
    n=mp.sqrt(sum(a*a for a in v)); return [a/n for a in v]
def mdot(u,v): return sum(a*b for a,b in zip(u,v))
def Dmp(p):
    Y=build([mp.mpf(x) for x in p], munit, mdot)
    orth=max(abs(mdot(Y[i],Y[(i+2)%5])) for i in range(5))
    ph=[mp.asin(abs(mdot(Y[i],Y[(i+1)%5]))) for i in range(5)]
    return sum(ph)-mp.pi, orth, ph
worst=None
for rs in range(60):
    p=[random.gauss(0,1) for _ in range(9)]
    cur=Dm(build(p)); step=0.3
    for it in range(3000):
        q=[a+step*random.gauss(0,1) for a in p]
        try: val=Dm(build(q))
        except ZeroDivisionError: continue
        if val<cur: p,cur=q,val
        if it%300==299: step*=0.6
    exc,orth,ph=Dmp(p)
    if worst is None or exc<worst[0]: worst=(exc,cur-math.pi,orth,ph)
    if exc<0: print("NEGATIVE in mp:",mp.nstr(exc,10))
print("min over restarts of (D - pi) in mpmath:", mp.nstr(worst[0],10), " float value:", worst[1],
      " max non-consecutive |<.,.>|:", mp.nstr(worst[2],3), " phis:", [mp.nstr(x,6) for x in worst[3]])
