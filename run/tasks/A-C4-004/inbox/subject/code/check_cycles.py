"""Sanity checks (floating point; EVIDENCE ONLY, no proof step rests on this file).
(1) 5-cycles in R^3: sum of consecutive phi equals pi + F(u,v) (proof Step 7), and F >= 0.
(2) 6-cycles in R^4: the (a,b,s,t) description of Step 8 matches random 6-cycles, and sum phi >= pi.
"""
import math, random
random.seed(1)
def dot(u,v): return sum(p*q for p,q in zip(u,v))
def phi(u,v): return math.asin(min(1.0,abs(dot(u,v))))
def det3(m):
    return (m[0][0]*(m[1][1]*m[2][2]-m[1][2]*m[2][1])-m[0][1]*(m[1][0]*m[2][2]-m[1][2]*m[2][0])
            +m[0][2]*(m[1][0]*m[2][1]-m[1][1]*m[2][0]))
def cross4(u,v,w):
    res=[]
    for k in range(4):
        sub=[[r[j] for j in range(4) if j!=k] for r in (u,v,w)]
        res.append((-1)**k*det3(sub))
    n=math.sqrt(dot(res,res)); return [r/n for r in res]
def F(u,v):
    return u+v-math.acos(math.cos(u)*math.cos(v))-math.asin(math.sin(u)*math.sin(v)/(1+math.cos(u)*math.cos(v)))

# (1) 5-cycles: x1=e1, x3=e2, x4=(0,cos t,sin t), x2=(cos al,-sin al sin t, sin al cos t), x5=(cos be,0,sin be)
worst5=1e9; maxerr5=0; n5=0
for _ in range(200000):
    t=random.uniform(0,math.pi); al=random.uniform(0,2*math.pi)
    be=math.atan2(-math.cos(al), math.sin(al)*math.cos(t))
    x=[(1,0,0),(math.cos(al),-math.sin(al)*math.sin(t),math.sin(al)*math.cos(t)),(0,1,0),
       (0,math.cos(t),math.sin(t)),(math.cos(be),0,math.sin(be))]
    assert max(abs(dot(x[k],x[(k+2)%5])) for k in range(5))<1e-12
    ph=[phi(x[k],x[(k+1)%5]) for k in range(5)]
    if min(ph)<1e-6 or max(ph)>math.pi/2-1e-6: continue
    n5+=1
    s=sum(ph); u,v=ph[2],ph[4]
    maxerr5=max(maxerr5,abs(s-(math.pi+F(u,v))))
    worst5=min(worst5,s-math.pi)
print("5-cycles tested:",n5," max |sum phi - (pi+F)| =",maxerr5," min(sum phi - pi) =",worst5)
mF=min(F(math.pi/2*i/300,math.pi/2*j/300) for i in range(301) for j in range(1,301))
print("grid min of F on [0,pi/2]x(0,pi/2]:",mF)

# (2) 6-cycles: x1=e1,x2=(ca,sa,0,0),x3=(0,cb,sb,0),x4=(0,0,cc,sc),x5=e4,x6 orth x2,x3,x4
worst6=1e9; maxerr6=0; n6=0
for _ in range(100000):
    a,b,c=[random.uniform(0,2*math.pi) for _ in range(3)]
    x=[(1,0,0,0),(math.cos(a),math.sin(a),0,0),(0,math.cos(b),math.sin(b),0),(0,0,math.cos(c),math.sin(c)),(0,0,0,1)]
    try: x.append(tuple(cross4(x[1],x[2],x[3])))
    except ZeroDivisionError: continue
    for i in range(6):
        for j in range(i+1,6):
            if (j-i)%6 not in (1,5): assert abs(dot(x[i],x[j]))<1e-12
    ph=[phi(x[k],x[(k+1)%6]) for k in range(6)]
    if min(ph)<1e-6 or max(ph)>math.pi/2-1e-6: continue
    n6+=1
    # Step 8 description: A=span(x2,x3), B=span(x5,x6); x1=lam n3+mu n5, x4=lam' n2+mu' n6
    A2=ph[1]; B5=ph[4]
    def proj(v,basis):  # basis orthonormal list
        return [sum(dot(v,e)*e[i] for e in basis) for i in range(4)]
    def orthonormal(u,v):
        w=[vi-dot(u,v)*ui for ui,vi in zip(u,v)]; n=math.sqrt(dot(w,w)); return [u,[wi/n for wi in w]]
    OA=orthonormal(x[1],x[2]); OB=orthonormal(x[4],x[5])
    lam=math.sqrt(dot(proj(x[0],OA),proj(x[0],OA))); mu=math.sqrt(dot(proj(x[0],OB),proj(x[0],OB)))
    lam2=math.sqrt(dot(proj(x[3],OA),proj(x[3],OA))); mu2=math.sqrt(dot(proj(x[3],OB),proj(x[3],OB)))
    s_=math.atan2(mu,lam); t_=math.atan2(mu2,lam2)
    pred=[math.asin(math.cos(s_)*math.cos(A2)),A2,math.asin(math.cos(t_)*math.cos(A2)),
          math.asin(math.sin(t_)*math.cos(B5)),B5,math.asin(math.sin(s_)*math.cos(B5))]
    err=max(abs(p-q) for p,q in zip(pred,ph))
    err=max(err,abs(math.cos(s_)*math.cos(t_)*math.sin(A2)-math.sin(s_)*math.sin(t_)*math.sin(B5)))
    err=max(err,abs(lam*lam+mu*mu-1),abs(lam2*lam2+mu2*mu2-1))
    maxerr6=max(maxerr6,err)
    assert (A2-B5)*(s_+t_-math.pi/2)>=-1e-9
    worst6=min(worst6,sum(ph)-math.pi)
print("6-cycles tested:",n6," max description error =",maxerr6," min(sum phi - pi) =",worst6)
