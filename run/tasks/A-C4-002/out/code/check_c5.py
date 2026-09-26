# EVIDENCE ONLY (floating point). Not part of the proof in out/proof.md. stdlib-only.
# Checks Lemma 7 (5-cycle): closed-form D(b,A) vs direct vectors; g'(A) = -cos b/(1+sin b cos A); D >= pi on 2000 random points.
from math import *
import random
random.seed(1)
# C5: check g'(A) formula and D(A) formula vs direct vectors
def cross(u,v): return (u[1]*v[2]-u[2]*v[1],u[2]*v[0]-u[0]*v[2],u[0]*v[1]-u[1]*v[0])
def dot(u,v): return sum(a*b for a,b in zip(u,v))
def nrm(u):
    l=sqrt(dot(u,u)); return tuple(a/l for a in u)
phi=lambda u,v: asin(min(1,abs(dot(u,v))))
mx=0
for _ in range(2000):
    b=random.uniform(0.01,1.56); A=random.uniform(0.01,1.56)
    x1=(1,0,0); x3=(0,1,0); x2=(cos(b),sin(b)*cos(A),sin(b)*sin(A))
    x4=nrm(cross(x1,x2)); x5=nrm(cross(x2,x3))
    X=[x1,x2,x3,x4,x5]
    # orthogonality check
    for i in range(5):
        assert abs(dot(X[i],X[(i+2)%5]))<1e-12
    Dd=sum(phi(X[i],X[(i+1)%5]) for i in range(5))
    M=sqrt(cos(b)**2+sin(b)**2*sin(A)**2)
    Df=(pi/2-b)+asin(sin(b)*cos(A))+A+asin(sin(b)*sin(A)/M)+asin(cos(b)*cos(A)/M)
    mx=max(mx,abs(Dd-Df))
    g=lambda t: atan(tan(b)*sin(t))+atan(cos(b)/tan(t))
    h=1e-6
    gp=(g(A+h)-g(A-h))/(2*h)
    assert abs(gp+cos(b)/(1+sin(b)*cos(A)))<1e-6, (gp, -cos(b)/(1+sin(b)*cos(A)))
    assert Dd>=pi-1e-12
print("C5 formula max discrepancy",mx)
