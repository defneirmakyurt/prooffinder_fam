import sys
exec(open(__file__.replace("heights.py","print_R.py")).read().split("k=int")[0])
def cyc(l,k):
    if len(l)>k: return False
    return all(k-1-i <= (l[i] if i<len(l) else 0) <= k-i for i in range(k))
k=int(sys.argv[1]); M=k*k-2*k-1
C=[tuple(x for x in [k-i+(0 if i==j else 1) for i in range(1,k+1)] if x>0) for j in range(1,k+1)]
D1=set(p for c in C for p in preimages(c) if not cyc(p,k))
for mu in sorted(D1):
    lev={mu}; h=0
    while True:
        nxt=set(q for m in lev for q in preimages(m))
        if not nxt: break
        lev=nxt; h+=1
    print(mu,'height',h,'(M-1=%d)'%(M-1))
