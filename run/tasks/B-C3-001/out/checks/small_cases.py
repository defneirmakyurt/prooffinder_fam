# Exact (integer) computation of d_B and D_B for small n. stdlib only.
import sys, time
from functools import lru_cache
sys.setrecursionlimit(100000)

def partitions(n, maxpart=None):
    if maxpart is None: maxpart = n
    if n == 0:
        yield ()
        return
    for p in range(min(n, maxpart), 0, -1):
        for rest in partitions(n - p, p):
            yield (p,) + rest

def B(lam):
    s = len(lam)
    parts = [x - 1 for x in lam if x > 1] + [s]
    return tuple(sorted(parts, reverse=True))

def rank(n):
    k = 1
    while k*(k+1)//2 < n: k += 1
    return k

def analyse(n):
    P = list(partitions(n))
    succ = {p: B(p) for p in P}
    # cyclic = on a cycle of the functional graph
    cyclic = set()
    state = {}
    for p in P:
        if p in state: continue
        path = []; q = p
        while q not in state:
            state[q] = 1; path.append(q); q = succ[q]
        if state[q] == 1:  # found new cycle
            i = path.index(q)
            for c in path[i:]: cyclic.add(c)
        for c in path: state[c] = 2
    d = {}
    for c in cyclic: d[c] = 0
    def dist(p):
        stack = []
        q = p
        while q not in d:
            stack.append(q); q = succ[q]
        v = d[q]
        while stack:
            v += 1; d[stack.pop()] = v
        return d[p]
    for p in P: dist(p)
    D = max(d.values())
    ext = sorted([p for p in P if d[p] == D], reverse=True)
    return D, ext, cyclic, d

if __name__ == "__main__":
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 40
    t0 = time.time()
    print("n rank k  D_B(n)  k^2-2k-1  k^2-k  slack  #ext  extremizers(if<=6)")
    for n in range(1, N+1):
        k = rank(n)
        D, ext, cyc, d = analyse(n)
        tri = (n == k*(k+1)//2)
        b = k*k - 2*k - 1
        print(n, k, D, b, k*k-k, ("T" if tri else ("T-1" if n == k*(k+1)//2 - 1 else "")), (b - D) if not tri else "", len(ext), ext if len(ext) <= 6 else ext[:3])
        sys.stdout.flush()
    print("runtime %.2fs" % (time.time() - t0))
