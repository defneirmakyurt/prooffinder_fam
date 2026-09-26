# Counterexample search / sanity checks for A-C2 (orthogonality lemma) and the lemmas of proof A-C2-011.
# Gram-matrix model: x_1..x_m unit in R^(m-1) with <x_i,x_j>=0 for |i-j|>=2  <=>  tridiagonal G=I+offdiag(c)
# PSD with rank <= m-1 (det G = 0). Determinant recursion D_k = D_{k-1} - c_{k-1}^2 D_{k-2}.
# We draw rational c_1..c_{m-2} with leading block PD, then set c_{m-1}^2 = D_{m-1}/D_{m-2} (exact) if <= 1.
import random, sys
from fractions import Fraction as F
import mpmath as mp
mp.mp.dps = 60
random.seed(12345)

def dets(cs2):  # cs2 = list of c_i^2 (Fractions); returns D_0..D_n
    D=[F(1),F(1)]
    for c2 in cs2:
        D.append(D[-1]-c2*D[-2])
    return D

worst = None; tried=0; admissible=0; viol=0
for m in range(2, 13):
    for trial in range(3000):
        tried+=1
        if m==2:
            cs2=[F(1)]   # only admissible: x2=+-x1
        else:
            cs2=[F(random.randint(0,1000),1000)**2 * (1 if random.random()<0.8 else 0) for _ in range(m-2)]
            D=dets(cs2)
            if any(d<=0 for d in D[1:]): continue  # leading (m-1) block must be PD (else rank already < m-1; handled separately)
            last=D[m-1]/D[m-2]
            if last>1: continue
            cs2.append(last)
        D=dets(cs2)
        assert D[m]==0 and all(d>0 for d in D[1:m])  # PSD rank m-1 tridiagonal Gram: realizable in R^(m-1)
        admissible+=1
        B=mp.fsum(mp.asin(mp.sqrt(mp.mpf(c2.numerator)/c2.denominator)) for c2 in cs2)
        chain=(m-1)*mp.pi/2 - B
        slack=(m-2)*mp.pi/2 - chain
        if slack < -mp.mpf(10)**-40: viol+=1; print("VIOLATION", m, cs2)
        if worst is None or slack<worst[0]: worst=(slack,m)
print("tried",tried,"admissible",admissible,"violations",viol,"min slack",mp.nstr(worst[0],10),"at m",worst[1])

# Equality tuple (e1,e1,e2,...,e_{m-1}): c_1=1, others 0
for m in range(2,12):
    cs2=[F(1)]+[F(0)]*(m-2)
    assert dets(cs2)[m]==0
    chain=(m-1)*mp.pi/2 - mp.fsum(mp.asin(mp.sqrt(c)) for c in cs2)
    assert abs(chain-(m-2)*mp.pi/2)<mp.mpf(10)**-50
print("S2 equality tuple: chain sum == (m-2)pi/2 for m=2..11 (to 1e-50)")

# Step 3: cos u sin v >= sin(v-u) on 0<=u<=v<=pi/2, random + grid
bad=0
for _ in range(200000):
    u=mp.rand()*mp.pi/2; v=mp.rand()*mp.pi/2
    if u>v: u,v=v,u
    if mp.cos(u)*mp.sin(v) - mp.sin(v-u) < -mp.mpf(10)**-50: bad+=1
print("Step3 random 200000 pts, failures:",bad)

# Step 4 lemma: ||sum t_i x_i||^2 >= cos^2(B_{k-1}) t_k^2 when B_{k-1}<=pi/2; check min over t with t_k=1:
# min_t Q = 1/ (G^{-1})_{kk} (Schur complement) for PD G.  Random signed c.
bad=0; cnt=0
for _ in range(20000):
    k=random.randint(1,9)
    c=[mp.mpf(random.uniform(-1,1)) for _ in range(k-1)]
    if random.random()<0.3 and k>1: c[random.randrange(k-1)]=mp.mpf(1)*random.choice([-1,1])
    B=mp.fsum(mp.asin(abs(x)) for x in c)
    if B>mp.pi/2: continue
    G=mp.eye(k)
    for i in range(k-1): G[i,i+1]=G[i+1,i]=c[i]
    # Schur complement of the leading (k-1) block
    if k==1: s=mp.mpf(1)
    else:
        A=G[0:k-1,0:k-1]
        if mp.det(A)<=mp.mpf(10)**-40: continue
        b=G[0:k-1,k-1]
        s=1-(b.T*mp.inverse(A)*b)[0,0]
    cnt+=1
    if s - mp.cos(B)**2 < -mp.mpf(10)**-30: bad+=1; print("Step4 FAIL",k,c,s,mp.cos(B)**2)
print("Step4 Schur-complement check, instances:",cnt,"failures:",bad)
