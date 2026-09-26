# Brute force over all 8! labellings of Q_3 (stdlib, exact). Independent of lbdp.c.
import itertools
d=3; n=8
def T(order):
    f=[0]*n
    for i,v in enumerate(order): f[v]=i
    N=[0]*n; t=0
    for v in order:
        nb=[v^(1<<j) for j in range(d)]
        N[v]=(1 if all(f[w]>f[v] for w in nb) else 0)+sum(N[w] for w in nb if f[w]<f[v])
        t+=N[v]
    return t
from collections import Counter
c=Counter(T(p) for p in itertools.permutations(range(n)))
print("labellings:",sum(c.values()),"min T:",min(c),"count attaining min:",c[min(c)])
