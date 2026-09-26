# For n = T_k - 1: D_B, number of extremizers, the common descendant structure. Exact, stdlib only.
import sys, time
from small_cases import analyse, B
t0 = time.time()
K = int(sys.argv[1]) if len(sys.argv) > 1 else 9
for k in range(int(sys.argv[2]) if len(sys.argv)>2 else 2, K+1):
    n = k*(k+1)//2 - 1
    D, ext, cyc, d = analyse(n)
    # find first j at which all extremizers share image B^j
    imgs = list(ext); j = 0
    while len(set(imgs)) > 1 and j <= D:
        imgs = [B(x) for x in imgs]; j += 1
    common = imgs[0]
    # in-degree/ tree: count partitions at each depth
    from collections import Counter
    lv = Counter(d.values())
    print(f"k={k} n={n} D={D} k^2-2k-1={k*k-2*k-1} #ext={len(ext)} all ext merge after j={j} steps at {common} (d={d[common]})")
    print("   #partitions by d near top:", [(t, lv[t]) for t in range(max(0,D-4), D+1)])
    # number of parts / largest part among extremizers
    print("   largest parts:", sorted(Counter(x[0] for x in ext).items()), " #parts:", sorted(Counter(len(x) for x in ext).items()))
    if len(ext) <= 40: print("   ext:", ext)
    sys.stdout.flush()
print("runtime %.2fs" % (time.time()-t0))
