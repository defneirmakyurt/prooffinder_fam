# EVIDENCE ONLY (floating point). Not part of the proof in out/proof.md. stdlib-only.
# Checks Lemma 8 (6-cycle): orthogonality of the parametrised y_i, closed-form Delta vs direct sum, D >= pi, h decreasing (5000 random points).
from math import *
import random
random.seed(2)
def dot(u,v): return sum(a*b for a,b in zip(u,v))
def add(*vs): return tuple(sum(c) for c in zip(*vs))
def sc(k,u): return tuple(k*a for a in u)
phi=lambda u,v: asin(min(1,abs(dot(u,v))))
f1,f2,f3,f4=(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1)
mx=0; worst=9
for _ in range(5000):
    al=random.uniform(0.01,1.56); be=random.uniform(0.01,1.56); s=random.uniform(-3.1,3.1)
    a,b,A,B=sin(al),sin(be),cos(al),cos(be)
    x1=f1; x2=add(sc(A,f1),sc(a,f2)); x4=f3; x5=add(sc(B,f3),sc(b,f4))
    f5p=add(sc(-b,f3),sc(B,f4)); f2p=add(sc(-a,f1),sc(A,f2))
    x3=add(sc(cos(s),f2),sc(sin(s),f5p))
    # tau: cos(al)cos(s)cos(t)+cos(be)sin(s)sin(t)=0 -> (cos t, sin t) ~ (-B sin s, A cos s)
    n=hypot(B*sin(s),A*cos(s)); ct,st=-B*sin(s)/n, A*cos(s)/n
    x6=add(sc(ct,f2p),sc(st,f4))
    X=[x1,x2,x3,x4,x5,x6]
    for i in range(6):
        assert abs(dot(X[i],X[i])-1)<1e-12
        for d in (2,3):
            assert abs(dot(X[i],X[(i+d)%6]))<1e-12
    Dd=sum(phi(X[i],X[(i+1)%6]) for i in range(6))
    c,ss=abs(cos(s)),abs(sin(s)); N=hypot(A*c,B*ss)
    Df=pi-al-be+asin(a*c)+asin(b*ss)+asin(b*A*c/N)+asin(a*B*ss/N)
    mx=max(mx,abs(Dd-Df)); worst=min(worst,Dd-pi)
    # h decreasing check
    def h(sig):
        c,ss=cos(sig),sin(sig); N2=A*A*c*c+B*B*ss*ss
        R1=sqrt(1-a*a*c*c); R2=sqrt(1-b*b*ss*ss)
        return c*R1*(b*N2+a*A*B)/(ss*R2*(a*N2+b*A*B))
    sig=random.uniform(0.01,1.55)
    assert h(sig+1e-4)<h(sig)
print("C6 formula max discrepancy",mx,"min D-pi",worst)
