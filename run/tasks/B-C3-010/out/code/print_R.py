"""Print R_k = {lambda |- T_k-1 : B^{M-1}(lambda) = nu_k}, M = k^2-2k-1, as an explicit sorted list,
by iterating the preimage rule of proof.md Lemma 2.1 (M-1 times) from nu_k = (k+1,k-1,...,3,1).
Every printed partition is re-checked against the definition of B.  Stdlib only.
Usage: python3 print_R.py k    (k >= 4).  R_k is a subset of E_k for every k (proof.md Prop. 4.1);
R_k = E_k is CHECKED only for 4 <= k <= 11 (check_E.py)."""
import sys
def B(l):
    s=len(l); r=[x-1 for x in l if x>1]+[s]; return tuple(sorted(r,reverse=True))
def preimages(mu):
    L=len(mu); res=[]
    for idx,s in enumerate(mu):
        if idx>0 and mu[idx-1]==s: continue
        if s>=L-1:
            rest=[x+1 for j,x in enumerate(mu) if j!=idx]+[1]*(s-(L-1))
            res.append(tuple(sorted(rest,reverse=True)))
    return res
k=int(sys.argv[1]); M=k*k-2*k-1
nu=tuple([k+1]+list(range(k-1,2,-1))+[1])
level={nu}
for _ in range(M-1):
    level=set(p for m in level for p in preimages(m))
for l in sorted(level,reverse=True):
    x=l
    for _ in range(M-1): x=B(x)
    assert x==nu
    print(l)
print("k=%d |R_k|=%d"%(k,len(level)))
