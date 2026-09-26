# Algebraic-lens counterexample search for A-C2 (stdlib only).
# Admissible configs <-> Jacobi (tridiagonal) Gram matrices J with unit diagonal, off-diagonals c_j,
# PSD and rank <= m-1 (any PSD rank<=m-1 matrix is a Gram matrix in R^(m-1)).
# Sign flips x_i -> -x_i conjugate J by diag(+-1) and can make all c_j >= 0, so WLOG c_j in [0,1].
# Generation: rational c_1..c_{m-2}; leading minors D_k exact (continuant D_k = D_{k-1} - c_{k-1}^2 D_{k-2});
# c_{m-1}^2 := D_{m-1}/D_{m-2} makes D_m = 0 exactly (singular), PSD since D_1..D_{m-1} > 0.
# Checks: (a) Sum arcsin c_j >= pi/2 (target (*)); (b) Step 4 pivot bound p_k = D_k/D_{k-1} >= cos^2(B_{k-1})
# whenever B_{k-1} < pi/2. Float checks with margin 1e-9 (math.asin/cos errors are ~1e-15 per call,
# m<=12 terms), so a reported violation needs slack < -1e-9 to count; anything in [-1e-9,1e-9] is flagged "near".
import random, math
from fractions import Fraction as F
random.seed(20260926)
viol=0; near=0; tested=0; pivviol=0; minslack=1e9; minpiv=1e9
for trial in range(200000):
    m = random.randint(3, 12)
    cs=[]; D=[F(1),F(1)]  # D_0=1, D_1=1
    ok=True
    for j in range(1, m-1):
        # choose c_j so D_{j+1} > 0
        den=random.choice([7,13,50,101,1000])
        c=F(random.randint(0,den),den)
        if random.random()<0.2: c=F(0)
        if random.random()<0.05: c=F(1)
        Dn=D[-1]-c*c*D[-2]
        if Dn<=0: ok=False;break
        cs.append(c); D.append(Dn)
    if not ok: continue
    c2=D[-1]/D[-2]           # c_{m-1}^2
    if c2>1: continue        # must be a valid inner product of unit vectors (|c|<=1)
    D.append(D[-1]-c2*D[-2]); assert D[-1]==0
    tested+=1
    al=[math.asin(float(c)) for c in cs]+[math.asin(math.sqrt(float(c2)))]
    B=sum(al); slack=B-math.pi/2
    minslack=min(minslack,slack)
    if slack< -1e-9: viol+=1; print("VIOLATION",m,cs,c2,slack)
    elif slack<1e-9: near+=1
    # pivot check
    Bk=0.0
    for k in range(2,m+1):
        Bk+=al[k-2]
        if Bk<math.pi/2-1e-9:
            p=float(D[k]/D[k-1]); s=p-math.cos(Bk)**2
            minpiv=min(minpiv,s)
            if s< -1e-9: pivviol+=1; print("PIVOT VIOLATION",m,k,s)
print("tested",tested,"violations",viol,"near-equality",near,"min slack B-pi/2",minslack)
print("pivot-bound violations",pivviol,"min pivot slack",minpiv)
# Exact checks of S2 tuple and m=3 example Gram data
for m in range(2,9):
    # (e1,e1,e2,...,e_{m-1}): c_1=1, others 0 -> chain sum (m-2)pi/2 exactly
    cs=[1]+[0]*(m-2); th=[math.acos(abs(c)) for c in cs]
    assert th[0]==0 and all(t==math.acos(0) for t in th[1:])
print("S2 tuple: chain sum = (m-2)*acos(0) for m=2..8 (exact: acos(1)=0, acos(0)=pi/2)")
# R^m sanity (S4c): identity Gram (e_1..e_m) is PSD rank m, nonsingular -> excluded by det=0 requirement
