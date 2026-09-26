# Compares exhaustive D_B(n) (from table.DB) with the conjectured formula F(n), n=1..N. Stdlib only.
import sys
from table import DB
def F(n):
    k=1
    while k*(k+1)//2<n: k+=1
    r=n-(k-1)*k//2
    c=[n-k+1] if n>=3 else [0]
    if 2<=r<=k: c.append(r*(k+1)-2*k)
    if k>=4 and 1<=r<=k-3: c.append((k-1)*(k-2-r))
    return max(c),k,r
N=int(sys.argv[1]); S=int(sys.argv[2]) if len(sys.argv)>2 else 1; mism=[]
for n in range(S,N+1):
    f,k,r=F(n); d,_=DB(n)
    if f!=d: mism.append((n,k,r,d,f))
print("n from",S,"to",N,"mismatches (n,k,r,D_B,F):",mism)
