# stdlib only. Independent exhaustive check of D_B(T_k) for k = 1..K.
# For every partition of T_k: follow the orbit with memoisation and explicit cycle detection
# (does NOT assume delta_k is the unique cyclic partition; it finds all cyclic partitions).
# d_B(lambda) = cycle-ENTRY time (number of shifts until the first cyclic partition).
import sys
sys.setrecursionlimit(10000)
def partitions(n, m=None):
    if m is None: m = n
    if n == 0:
        yield (); return
    for a in range(min(n, m), 0, -1):
        for rest in partitions(n - a, a):
            yield (a,) + rest
def B(l):
    s = len(l)
    return tuple(sorted([x - 1 for x in l if x > 1] + [s], reverse=True))
def analyse(n):
    d = {}          # partition -> d_B
    cyclic = set()
    for l in partitions(n):
        if l in d: continue
        path = []; pos = {}; x = l
        while x not in d and x not in pos:
            pos[x] = len(path); path.append(x); x = B(x)
        if x in pos:            # new cycle found: path[pos[x]:] is the cycle
            cyc = path[pos[x]:]
            for y in cyc: d[y] = 0; cyclic.add(y)
            path = path[:pos[x]]
            x = cyc[0]
        base = d[x]
        for y in reversed(path):
            base += 1; d[y] = base
    return d, cyclic
K = int(sys.argv[1]); bad = 0
for k in range(1, K + 1):
    n = k * (k + 1) // 2
    d, cyc = analyse(n)
    delta = tuple(range(k, 0, -1))
    D = max(d.values()); maxim = sorted([l for l in d if d[l] == D], reverse=True)
    lam = (1,) if k == 1 else tuple([k - 1] + [k + 1 - j for j in range(2, k + 1)] + [1])
    ok = (cyc == {delta}) and D == k * k - k and d[lam] == k * k - k
    if not ok: bad += 1
    print("k=%d n=%d #partitions=%d cyclic=%s D_B=%d k^2-k=%d d(witness)=%d #maximisers=%d first=%s ok=%s"
          % (k, n, len(d), sorted(cyc), D, k*k-k, d[lam], len(maxim), maxim[:3], ok))
    sys.stdout.flush()
print("failures:", bad)
