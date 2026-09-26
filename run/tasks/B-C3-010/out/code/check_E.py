"""Exact (integer tuple) check for n = T_k - 1, 4 <= k <= K.  Stdlib only.
For each k: (1) builds the backward tree of nu_k = (k+1,k-1,...,3,1) using the explicit preimage rule
(Lemma 1 of proof.md) up to depth M-1, M = k^2-2k-1, and checks the rule against the definition of B;
(2) enumerates ALL partitions of T_k-1, computes d_B exactly, and checks that
    E_k := {d_B = M} equals the depth-(M-1) level of the tree, that max d_B = M,
    and that every member of E_k is a Garden-of-Eden partition (lambda_1 <= len(lambda)-2).
Prints |E_k|."""
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
def partitions(n,m=None):
    if m is None: m=n
    if n==0: yield (); return
    for f in range(min(n,m),0,-1):
        for r in partitions(n-f,f): yield (f,)+r
K=int(sys.argv[1])
for k in range(4,K+1):
    n=k*(k+1)//2-1; M=k*k-2*k-1
    nu=tuple([k+1]+list(range(k-1,2,-1))+[1])
    assert sum(nu)==n
    level={nu}
    for d in range(1,M):
        nxt=set()
        for m in level:
            for p in preimages(m):
                assert B(p)==m
                nxt.add(p)
        level=nxt
    parts=list(partitions(n))
    # preimage rule completeness: count of preimages over all partitions equals number of partitions
    img={}
    for p in parts: img.setdefault(B(p),set()).add(p)
    for mu in parts:
        assert set(preimages(mu))==img.get(mu,set()), mu
    # d_B: cyclic iff delta_{k-1} <= lambda <= delta_k (Cell 1)
    def cyc(l):
        if len(l)>k: return False
        for i in range(k):
            r=l[i] if i<len(l) else 0
            if not (k-1-i<=r<=k-i): return False
        return True
    d={}
    def dB(l):
        path=[]
        x=l
        while x not in d and not cyc(x): path.append(x); x=B(x)
        base=d.get(x,0)
        if x not in d: d[x]=0
        for y in reversed(path): base+=1; d[y]=base
        return d[l]
    E=set(p for p in parts if dB(p)==M)
    assert max(d[p] for p in parts)==M
    assert E==level
    assert all(l[0]<=len(l)-2 for l in E)
    print(f"k={k} n={n} M={M} #partitions={len(parts)} |E_k|={len(E)} E_k==level_(M-1)(nu_k): True, all GoE: True")
print("ALL CHECKS PASSED")
