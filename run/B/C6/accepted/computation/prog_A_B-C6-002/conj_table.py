# Exhaustive computation of D_B(n) for 1<=n<=N (stdlib only, exact integers),
# compared with the conjectured formula F(n) = max(A,Bv,C) (see proof.md).
import sys
def parts(n, m=None):
    if m is None: m=n
    if n==0: yield (); return
    for a in range(min(n,m),0,-1):
        for rest in parts(n-a,a):
            yield (a,)+rest
def B(l):
    s=len(l)
    return tuple(sorted([x-1 for x in l if x>1]+[s],reverse=True))
def rank(n):
    k=1
    while k*(k+1)//2<n: k+=1
    return k
def DB(n):
    P=list(parts(n)); nxt={p:B(p) for p in P}
    cyc=set(); color={}
    for p in P:
        if p in color: continue
        path=[]; q=p
        while q not in color:
            color[q]=p; path.append(q); q=nxt[q]
        if color[q]==p: cyc.update(path[path.index(q):])
    d={p:0 for p in cyc}
    for p in P:
        st=[]; q=p
        while q not in d: st.append(q); q=nxt[q]
        v=d[q]
        while st: v+=1; d[st.pop()]=v
    return max(d.values())
def F(n):
    if n<=2: return 0
    k=rank(n); r=n-(k-1)*k//2
    c=[n-k+1]
    if r>=2: c.append(r*(k+1)-2*k)
    if k>=4 and r<=k-3: c.append((k-1)*(k-2-r))
    return max(c)
N=int(sys.argv[1]); bad=0
for n in range(1,N+1):
    D=DB(n); f=F(n)
    print(n,rank(n),D,f,"OK" if D==f else "MISMATCH"); sys.stdout.flush()
    if D!=f: bad+=1
print("mismatches:",bad)
