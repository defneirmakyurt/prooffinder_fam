"""Cross-check (not load-bearing) of the hand computations in proof.md, Steps 3 and 4. Stdlib only, exact integers.
For 4 <= k <= K:
  (i)  D_1 := {mu |- T_k-1 : mu non-cyclic, B(mu) cyclic}, computed as the non-cyclic preimages (definition of B,
       via the preimage rule, itself re-checked against B) of the k cyclic partitions, equals the list of Step 3.4:
       {mu_j : 3<=j<=k} u {omega_k};
  (ii) B^{M-1}(lambda*_k) = nu_k, and (k>=5) B^3(alpha_k) = B^3(beta_k) = B^3(lambda*_k);
  (iii) d_B of lambda*_k, alpha_k, beta_k (by forward iteration and the Cell-1 cyclic test) equals M."""
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
def cyc(l,k):
    if len(l)>k: return False
    return all(k-1-i <= (l[i] if i<len(l) else 0) <= k-i for i in range(k))
def d(l,k):
    t=0
    while not cyc(l,k): l=B(l); t+=1
    return t
def Bpow(l,m):
    for _ in range(m): l=B(l)
    return l
K=int(sys.argv[1])
for k in range(4,K+1):
    n=k*(k+1)//2-1; M=k*k-2*k-1
    C=[tuple(x for x in [k-i+(0 if i==j else 1) for i in range(1,k+1)] if x>0) for j in range(1,k+1)]
    assert all(sum(c)==n and cyc(c,k) for c in C)
    for c in C:
        for p in preimages(c): assert B(p)==c and sum(p)==n
    D1=set(p for c in C for p in preimages(c) if not cyc(p,k))
    base=list(range(k-1,1,-1))            # (k-1,...,2)
    L=set()
    for j in range(3,k+1):
        v=k+2-j; b=[x if x!=v else v-1 for x in base]
        L.add(tuple(sorted([k+1]+b,reverse=True)))
    L.add(tuple([k+1,k]+list(range(k-2,2,-1))))
    assert D1==L, (k,D1,L)
    nu=tuple([k+1]+list(range(k-1,2,-1))+[1])
    ls=tuple([k-1,k-2]+list(range(k-2,0,-1))+[1])
    assert sum(ls)==n and Bpow(ls,M-1)==nu and d(ls,k)==M
    if k>=5:
        H=[k-1,k-2]+list(range(k-2,3,-1))
        al=tuple(H+[2,2,1,1,1]); be=tuple(H+[2,2,2,1])
        assert ls==tuple(H+[3,2,1,1])
        assert sum(al)==n and sum(be)==n
        assert Bpow(al,3)==Bpow(ls,3)==Bpow(be,3)
        assert d(al,k)==M and d(be,k)==M
print("ALL CHECKS PASSED for 4<=k<=%d"%K)
