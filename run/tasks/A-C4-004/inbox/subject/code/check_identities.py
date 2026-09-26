"""Symbolic (sympy) re-check of the algebraic identities written out by hand in proof.md.
Support only: every identity is also derived by hand in proof.md."""
import sympy as sp
p,q,r,u,v,A,s,al,be=sp.symbols('p q r u v A s alpha beta', real=True)
# Step 7: tridiagonal 4x4 Gram determinant
G=sp.Matrix([[1,p,0,0],[p,1,q,0],[0,q,1,r],[0,0,r,1]])
print("det4 - ((1-p^2)(1-r^2)-q^2) =", sp.simplify(G.det()-((1-p**2)*(1-r**2)-q**2)))
# Step 2: psi''=g(A^2-1)/(1-g^2)^{3/2} for psi=asin(g), g=al cos s+be sin s
g=al*sp.cos(s)+be*sp.sin(s)
psi2=sp.diff(sp.asin(g),s,2)
target=g*(al**2+be**2-1)/(1-g**2)**sp.Rational(3,2)
print("psi'' - formula =", sp.simplify(psi2-target))
# Step 7: second derivative of acos(cos u cos v) in u
gg=sp.acos(sp.cos(u)*sp.cos(v))
D=1-sp.cos(u)**2*sp.cos(v)**2
print("g'' - formula =", sp.simplify(sp.diff(gg,u,2)-sp.cos(u)*sp.cos(v)*sp.sin(v)**2/D**sp.Rational(3,2)))
# Step 7: (1+cu cv)^2-(su sv)^2 = (cu+cv)^2
print("identity (1+cucv)^2-su^2sv^2-(cu+cv)^2 =", sp.simplify(sp.expand((1+sp.cos(u)*sp.cos(v))**2-sp.sin(u)**2*sp.sin(v)**2-(sp.cos(u)+sp.cos(v))**2)))
# Step 7: derivative of w=su sv/(1+cu cv)
w=sp.sin(u)*sp.sin(v)/(1+sp.cos(u)*sp.cos(v))
print("dw/du - sv(cu+cv)/(1+cucv)^2 =", sp.simplify(sp.diff(w,u)-sp.sin(v)*(sp.cos(u)+sp.cos(v))/(1+sp.cos(u)*sp.cos(v))**2))
hp=sp.sin(v)/(1+sp.cos(u)*sp.cos(v))
print("d/du[sv/(1+cucv)] - sv cv su/(1+cucv)^2 =", sp.simplify(sp.diff(hp,u)-sp.sin(v)*sp.cos(v)*sp.sin(u)/(1+sp.cos(u)*sp.cos(v))**2))
# Step 7: cos(phi1+phi2) computation
c4=sp.sqrt(1-sp.cos(u)**2*sp.cos(v)**2)
expr=(sp.sin(v)/c4)*(sp.sin(u)/c4)-(sp.sin(u)*sp.cos(v)/c4)*(sp.cos(u)*sp.sin(v)/c4)
print("cos(phi1+phi2) - w =", sp.simplify(expr-w))
# Step 7: the solved values satisfy sin phi1 = cos v cos phi2, sin phi2 = cos phi1 cos u, and sin^2+cos^2=1
sph1=sp.sin(u)*sp.cos(v)/c4; cph1=sp.sin(v)/c4; sph2=sp.cos(u)*sp.sin(v)/c4; cph2=sp.sin(u)/c4
print("checks:", [sp.simplify(e) for e in (sph1-sp.cos(v)*cph2, sph2-cph1*sp.cos(u), sph1**2+cph1**2-1, sph2**2+cph2**2-1)])
