# Sanity check (not load-bearing): d_B of the three witness families vs the proved formulas, 4<=k<=29. Stdlib only.
import sys
sys.path.insert(0,'.')
from table import B
def dB(p):
    p=tuple(sorted(p,reverse=True)); seen={}; x=p; i=0
    while x not in seen: seen[x]=i; x=B(x); i+=1
    return seen[x]
def delta(m): return list(range(m,0,-1))
bad=[]
for k in range(4,30):
    for r in range(1,k-2):
        v=dB(delta(k-2)+[k-2,r+1])
        if v!=(k-1)*(k-2-r): bad.append((k,r,v,(k-1)*(k-2-r)))
    for r in range(2,k+1):
        v=dB(delta(k-1)+[r-1,1])
        if v!=r*(k+1)-2*k: bad.append(('U',k,r,v))
    for r in range(1,k+1):
        n=(k-1)*k//2+r
        if dB([1]*n)!=n-k+1: bad.append(('O',k,r))
print(bad[:20], len(bad))
