"""Referee A-C4-005 checks (floating point + mpmath high precision; EVIDENCE ONLY).
1. S2 equality configurations (mpmath 50 digits).
2. Lemma A / step 3.5 consistency at the non-orthogonal extremisers: Phi constant on I.
3. Independent random 5-cycles in R^3 (y3 in y1^perp, y4 = y1 x y2, y5 = y2 x y3): all 5 relations, D >= pi, D = pi + F(u).
4. Independent random 6-cycles in R^4 (y3 in y1^perp, y4 in {y1,y2}^perp, y5 = perp(y1,y2,y3), y6 = perp(y2,y3,y4)):
   D >= pi, Step 8.3 formulas, (8.3.1), sign claim 8.5, and the lower bound of 8.4.
5. Local minimisation of D over the 5-cycle / 6-cycle families (try to push D below pi).
"""
import math, random
import mpmath as mp
random.seed(2026)
mp.mp.dps = 50

def dot(u,v): return sum(a*b for a,b in zip(u,v))
def unit(v):
    n = math.sqrt(dot(v,v)); return [a/n for a in v]
def phi(u,v): return math.asin(min(1.0, abs(dot(u,v))))
def S(X):
    return sum(math.acos(min(1.0,abs(dot(X[i],X[j])))) for i in range(len(X)) for j in range(i+1,len(X)))
def perp_rand(vs, d):
    """random unit vector orthogonal to all vs (Gram-Schmidt)"""
    x = [random.gauss(0,1) for _ in range(d)]
    basis = []
    for v in vs:
        w = v[:]
        for b in basis: c = dot(w,b); w = [wi-c*bi for wi,bi in zip(w,b)]
        n = math.sqrt(dot(w,w))
        if n > 1e-12: basis.append([wi/n for wi in w])
    for b in basis: c = dot(x,b); x = [xi-c*bi for xi,bi in zip(x,b)]
    return unit(x)

# ---- 1. equality configurations
def Smp(X):
    tot = mp.mpf(0)
    for i in range(len(X)):
        for j in range(i+1,len(X)):
            ip = abs(sum(mp.mpf(a)*mp.mpf(b) for a,b in zip(X[i],X[j])))
            if ip > 1: ip = mp.mpf(1)
            tot += mp.acos(ip)
    return tot
h = mp.sqrt(3)/2; hf = mp.mpf(1)/2
confs = {
 "(a) e1,e1,e2,e2,e3": ([[1,0,0],[1,0,0],[0,1,0],[0,1,0],[0,0,1]], 4*mp.pi),
 "(b) e1,e1,e2,e2,e3,e4": ([[1,0,0,0],[1,0,0,0],[0,1,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]], 13*mp.pi/2),
 "(a) 3 planar at 60deg + z twice": ([[1,0,0],[hf,h,0],[-hf,h,0],[0,0,1],[0,0,1]], 4*mp.pi),
 "(b) 60deg triple (x1,x2) + 60deg triple (x3,x4)": ([[1,0,0,0],[hf,h,0,0],[-hf,h,0,0],[0,0,1,0],[0,0,hf,h],[0,0,-hf,h]], 13*mp.pi/2),
}
print("== 1. equality configurations (mpmath, 50 digits)")
for name,(X,bd) in confs.items():
    print(f"  {name}: S - bound = {mp.nstr(Smp(X)-bd, 5)}")

# ---- 2. step 3.5 at non-orthogonal extremisers: rotate x_1 inside L, check Phi constant on I
print("== 2. Phi(s) on I at non-orthogonal extremisers (step 3.5 consistency)")
for name,(X,bd) in list(confs.items())[2:]:
    Xf = [[float(a) for a in x] for x in X]
    d = len(Xf[0]); k = 0
    J = [j for j in range(len(Xf)) if j!=k and abs(dot(Xf[j],Xf[k]))<1e-14]
    R = [j for j in range(len(Xf)) if j!=k and j not in J]
    w = [0.0,1.0]+[0.0]*(d-2)   # unit, in L = (x1,x2)-plane, orthogonal to x_1 = e1
    def xs(s): return [math.cos(s)*a+math.sin(s)*b for a,b in zip(Xf[k],w)]
    def Phi(s): return sum(math.acos(min(1.0,abs(dot(xs(s),Xf[j])))) for j in range(len(Xf)) if j!=k)
    # I = [s_-, s_+] from zeros of g_j
    vals = [Phi(-math.pi/6 + i*(math.pi/3)/200) for i in range(201)]
    print(f"  {name}: J_1={J}, R={R}, Phi range on [-pi/6,pi/6]: max-min = {max(vals)-min(vals):.2e}; Phi(pi/6+0.05)-Phi(0) = {Phi(math.pi/6+0.05)-Phi(0):.3e}")

# ---- 3. independent 5-cycles in R^3
def cross(a,b): return [a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0]]
def F(u,v):
    return u+v-math.acos(math.cos(u)*math.cos(v))-math.asin(math.sin(u)*math.sin(v)/(1+math.cos(u)*math.cos(v)))
def cyc5():
    y1 = unit([random.gauss(0,1) for _ in range(3)]); y2 = unit([random.gauss(0,1) for _ in range(3)])
    y3 = perp_rand([y1],3); y4 = unit(cross(y1,y2)); y5 = unit(cross(y2,y3))
    return [y1,y2,y3,y4,y5]
print("== 3. independent random 5-cycles in R^3")
n=0; worst=1e9; relerr=0; ferr=0
for _ in range(200000):
    Y = cyc5()
    assert max(abs(dot(Y[i],Y[(i+2)%5])) for i in range(5)) < 1e-12
    ph = [phi(Y[i],Y[(i+1)%5]) for i in range(5)]
    if min(ph) < 1e-7 or max(ph) > math.pi/2-1e-7: continue
    n+=1
    for i in range(5):   # sin phi_{i+1} = cos phi_i cos phi_{i+2}
        relerr = max(relerr, abs(math.sin(ph[(i+1)%5]) - math.cos(ph[i])*math.cos(ph[(i+2)%5])))
    D = sum(ph); worst = min(worst, D-math.pi)
    ferr = max(ferr, abs(D - (math.pi + F(ph[2], ph[4]))))
print(f"  tested {n}; max relation error {relerr:.2e}; max |D-(pi+F(phi3,phi5))| {ferr:.2e}; min(D-pi) = {worst:.3e}")

# ---- 4. independent 6-cycles in R^4
def perp3(a,b,c):
    res=[]
    for k in range(4):
        sub=[[r[j] for j in range(4) if j!=k] for r in (a,b,c)]
        m=sub
        dt=(m[0][0]*(m[1][1]*m[2][2]-m[1][2]*m[2][1])-m[0][1]*(m[1][0]*m[2][2]-m[1][2]*m[2][0])+m[0][2]*(m[1][0]*m[2][1]-m[1][1]*m[2][0]))
        res.append((-1)**k*dt)
    return unit(res)
def cyc6():
    y1 = unit([random.gauss(0,1) for _ in range(4)]); y2 = unit([random.gauss(0,1) for _ in range(4)])
    y3 = perp_rand([y1],4); y4 = perp_rand([y1,y2],4); y5 = perp3(y1,y2,y3); y6 = perp3(y2,y3,y4)
    return [y1,y2,y3,y4,y5,y6]
print("== 4. independent random 6-cycles in R^4")
n=0; worst=1e9; e83=0; e831=0; signbad=0; lbbad=0
for _ in range(100000):
    Y = cyc6()
    for i in range(6):
        for j in range(i+1,6):
            if (j-i)%6 not in (1,5): assert abs(dot(Y[i],Y[j]))<1e-10
    ph = [phi(Y[i],Y[(i+1)%6]) for i in range(6)]
    if min(ph) < 1e-7 or max(ph) > math.pi/2-1e-7: continue
    n+=1
    D = sum(ph); worst = min(worst, D-math.pi)
    a, b = ph[1], ph[4]
    # A = span(y2,y3): orthonormal basis; |lam| = norm of projection of y1 onto A, etc.
    def onb(u,v):
        w=[vi-dot(u,v)*ui for ui,vi in zip(u,v)]; return [u, unit(w)]
    OA = onb(Y[1],Y[2]); OB = onb(Y[4],Y[5])
    pn = lambda v,B: math.sqrt(sum(dot(v,e)**2 for e in B))
    lam, mu, lam2, mu2 = pn(Y[0],OA), pn(Y[0],OB), pn(Y[3],OA), pn(Y[3],OB)
    s = math.atan2(mu,lam); t = math.atan2(mu2,lam2)
    pred = [math.cos(s)*math.cos(a), math.cos(t)*math.cos(a), math.sin(t)*math.cos(b), math.sin(s)*math.cos(b)]
    act = [math.sin(ph[0]), math.sin(ph[2]), math.sin(ph[3]), math.sin(ph[5])]
    e83 = max(e83, max(abs(p-q) for p,q in zip(pred,act)), abs(lam*lam+mu*mu-1), abs(lam2*lam2+mu2*mu2-1))
    e831 = max(e831, abs(math.cos(s)*math.cos(t)*math.sin(a)-math.sin(s)*math.sin(t)*math.sin(b)))
    if (a-b)*(s+t-math.pi/2) < -1e-9: signbad+=1
    if D < math.pi + (a-b)*(2*(s+t)/math.pi-1) - 1e-9: lbbad+=1
print(f"  tested {n}; max 8.3 error {e83:.2e}; max (8.3.1) residual {e831:.2e}; sign-claim violations {signbad}; 8.4 bound violations {lbbad}; min(D-pi) = {worst:.3e}")

# ---- 5. local minimisation of D over cycle families (random-restart hill climbing on the generators)
def D5(Y): return sum(phi(Y[i],Y[(i+1)%5]) for i in range(5))
def D6(Y): return sum(phi(Y[i],Y[(i+1)%6]) for i in range(6))
def build5(p):
    y1=unit(p[0:3]); y2=unit(p[3:6]); z=p[6:9]; c=dot(z,y1); y3=unit([zi-c*a for zi,a in zip(z,y1)])
    return [y1,y2,y3,unit(cross(y1,y2)),unit(cross(y2,y3))]
def build6(p):
    y1=unit(p[0:4]); y2=unit(p[4:8]); z=p[8:12]; c=dot(z,y1); y3=unit([zi-c*a for zi,a in zip(z,y1)])
    z=p[12:16]; B=[y1]; w=[b-dot(y2,y1)*a for a,b in zip(y1,y2)]; B.append(unit(w))
    for e in B: c=dot(z,e); z=[zi-c*ei for zi,ei in zip(z,e)]
    y4=unit(z); return [y1,y2,y3,y4,perp3(y1,y2,y3),perp3(y2,y3,y4)]
print("== 5. hill-climb minimising D over 5-cycles (R^3) and 6-cycles (R^4), degenerate edges not excluded, minima re-evaluated at 50 digits")
for name,build,Dm,dim,m in (("5-cycle",build5,D5,9,5),("6-cycle",build6,D6,16,6)):
    best=1e9; bestph=None
    for rs in range(60):
        p=[random.gauss(0,1) for _ in range(dim)]
        try: Y=build(p)
        except ZeroDivisionError: continue
        cur=Dm(Y); step=0.3
        for it in range(3000):
            q=[a+step*random.gauss(0,1) for a in p]
            try: Y=build(q)
            except ZeroDivisionError: continue
            val=Dm(Y)
            if val<cur: p,cur=q,val
            if it%300==299: step*=0.6
        Y=build(p); ph=[phi(Y[i],Y[(i+1)%m]) for i in range(m)]
        if cur<best: best=cur; bestph=ph; bestp=p
    # high-precision re-evaluation of the best generators (cycle rebuilt exactly orthogonal at 50 digits)
    mu_ = lambda v: [a/mp.sqrt(sum(b*b for b in v)) for a in v]
    md_ = lambda u,v: sum(a*b for a,b in zip(u,v))
    P=[mp.mpf(x) for x in bestp]
    if m==5:
        y1=mu_(P[0:3]); y2=mu_(P[3:6]); z=P[6:9]; c=md_(z,y1); y3=mu_([zi-c*a for zi,a in zip(z,y1)])
        cr=lambda a,b: [a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0]]
        YM=[y1,y2,y3,mu_(cr(y1,y2)),mu_(cr(y2,y3))]
    else:
        def p3(a,b,c_):
            M=mp.matrix([a,b,c_]); res=[]
            for k in range(4):
                sub=mp.matrix([[M[i,j] for j in range(4) if j!=k] for i in range(3)])
                res.append((-1)**k*mp.det(sub))
            return mu_(res)
        y1=mu_(P[0:4]); y2=mu_(P[4:8]); z=P[8:12]; c=md_(z,y1); y3=mu_([zi-c*a for zi,a in zip(z,y1)])
        z=P[12:16]; B=[y1, mu_([b-md_(y2,y1)*a for a,b in zip(y1,y2)])]
        for e in B: c=md_(z,e); z=[zi-c*ei for zi,ei in zip(z,e)]
        y4=mu_(z); YM=[y1,y2,y3,y4,p3(y1,y2,y3),p3(y2,y3,y4)]
    orth=max(abs(md_(YM[i],YM[j])) for i in range(m) for j in range(i+1,m) if (j-i)%m not in (1,m-1))
    Dhp=sum(mp.asin(abs(md_(YM[i],YM[(i+1)%m]))) for i in range(m))
    print(f"  {name}: min D found (float) = {best:.12f}, D - pi = {best-math.pi:.3e}, phis = {[round(x,4) for x in bestph]}")
    print(f"     same generators at 50 digits: D - pi = {mp.nstr(Dhp-mp.pi,6)}, max non-consecutive |<.,.>| = {mp.nstr(orth,3)}")
