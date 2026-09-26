# Sanity check of Lemma 3 (T = E + sum_v [valley] + (N(v)-1)*up(v)) on random labellings, stdlib only.
import random
def stats(d, order):
    n=1<<d; f=[0]*n
    for i,v in enumerate(order): f[v]=i
    N=[0]*n; T=0; X=0
    for v in order:
        nb=[v^(1<<j) for j in range(d)]
        low=[w for w in nb if f[w]<f[v]]; up=d-len(low)
        N[v]=(0 if low else 1)+sum(N[w] for w in low); T+=N[v]
        X+=(0 if low else 1)+(N[v]-1)*up
    return T, X
random.seed(12345); bad=0; cnt=0
for d in range(1,7):
    E=d*(1<<(d-1))
    for _ in range(300):
        o=list(range(1<<d)); random.shuffle(o); T,X=stats(d,o); cnt+=1
        if T!=E+X: bad+=1
print("labellings tested:",cnt,"identity failures:",bad)
