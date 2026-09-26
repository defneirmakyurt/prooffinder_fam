# Exhaustive computation of D_B(n) for small n (stdlib only, exact integer arithmetic).
import sys
def B(p):
    s=len(p); q=[x-1 for x in p if x>1]; q.append(s); q.sort(reverse=True); return tuple(q)
def partitions(n, m=None):
    if m is None: m=n
    if n==0: yield (); return
    for f in range(min(n,m),0,-1):
        for rest in partitions(n-f,f): yield (f,)+rest
def DB(n):
    parts=list(partitions(n)); nxt={p:B(p) for p in parts}
    # cyclic: on a cycle of functional graph
    cyc=set()
    for p in parts:
        # detect via iteration
        pass
    # compute cyclic set: iterate each from p, find cycle
    state={}
    for p in parts:
        if p in state: continue
        path=[];x=p
        while x not in state:
            state[x]=1; path.append(x); x=nxt[x]
        if state[x]==1:
            # new cycle found within path
            i=path.index(x)
            for y in path[i:]: cyc.add(y)
        for y in path: state[y]=2
    d={}
    for p in cyc: d[p]=0
    def dist(p):
        st=[];x=p
        while x not in d: st.append(x); x=nxt[x]
        v=d[x]
        for y in reversed(st): v+=1; d[y]=v
        return d[p]
    best=-1;arg=[]
    for p in parts:
        v=dist(p)
        if v>best: best=v;arg=[p]
        elif v==best: arg.append(p)
    return best,arg
if __name__=="__main__":
    N=int(sys.argv[1])
    for n in range(1,N+1):
        k=1
        while k*(k+1)//2<n: k+=1
        r=n-(k-1)*k//2
        b,a=DB(n)
        print(n,k,r,b,k*k-k-b, len(a), a[:3] if n<=40 else len(a))
