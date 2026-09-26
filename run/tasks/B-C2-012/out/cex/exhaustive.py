# stdlib only, exact integer arithmetic.
# For k = 1..K: enumerate ALL partitions of T_k, compute d_B exactly as the cycle-ENTRY time
# (independently of the proof: detect cycles by path revisits, do not assume delta_k is the only cycle),
# check: (1) delta_k is the only cyclic partition; (2) D_B(T_k) == k^2-k; (3) witness (k-1,k-1,k-2,..,1,1) attains it.
import sys
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
    # d[l] = transient length; cyc = set of cyclic partitions. Computed from the functional graph only.
    parts = list(partitions(n))
    cyc = set(); d = {}
    state = {}  # 0 unvisited, 1 on stack, 2 done
    for l in parts:
        if l in d: continue
        path = []; x = l; pos = {}
        while x not in d and x not in pos:
            pos[x] = len(path); path.append(x); x = B(x)
        if x in pos:  # new cycle found: path[pos[x]:] are cyclic
            cycle = path[pos[x]:]
            for y in cycle: cyc.add(y); d[y] = 0
            path = path[:pos[x]]
        # now x has d; back-propagate
        for y in reversed(path):
            d[y] = d[B(y)] + 1
    return parts, d, cyc
K = int(sys.argv[1]); bad = 0
for k in range(1, K + 1):
    n = k * (k + 1) // 2
    delta = tuple(range(k, 0, -1))
    parts, d, cyc = analyse(n)
    D = max(d.values())
    maxim = [l for l in parts if d[l] == D]
    wit = (1,) if k == 1 else tuple([k - 1] + [k + 1 - j for j in range(2, k + 1)] + [1])
    ok = (cyc == {delta}) and D == k * k - k and d[wit] == k * k - k and sum(wit) == n
    if not ok: bad += 1
    print(f"k={k} T_k={n} #partitions={len(parts)} cyclic={sorted(cyc)} D_B={D} k^2-k={k*k-k} "
          f"d(witness)={d[wit]} #maximisers={len(maxim)} sample={maxim[:4]} ok={ok}")
    # extra spot checks from S3/S6
    if k == 3: print("  d((2,1,1,1,1))=", d[(2,1,1,1,1)], " d((6))=", d[(6,)], " d((1^6))=", d[(1,)*6])
print("k=1..%d, failures: %d" % (K, bad))
