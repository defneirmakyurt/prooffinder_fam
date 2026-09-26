import sys
rows=[l.strip() for l in open(sys.argv[1]) if l.strip()]
d=len(rows[0]); n=1<<d
order=[int(r,2) for r in rows]; f={v:i for i,v in enumerate(order)}
N={}; V=0; extra=0; peaks=0; tot=0; hist={}
for v in order:
    lo=[v^(1<<j) for j in range(d) if f[v^(1<<j)]<f[v]]
    val = not lo
    N[v]=(1 if val else 0)+sum(N[w] for w in lo); V+=val; tot+=N[v]
for v in order:
    up=sum(1 for j in range(d) if f[v^(1<<j)]>f[v]); k=d-up
    if up and N[v]>1: extra+=up*(N[v]-1); hist[(k,N[v])]=hist.get((k,N[v]),0)+1
    peaks+= (up==0)
print("total",tot,"V",V,"E",d*n//2,"extra",extra,"peaks",peaks,"extra-vertices (down,N):count",hist)
