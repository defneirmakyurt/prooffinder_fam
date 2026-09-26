"""Exhaustive computation of D_B(T_{k-1}+1) for k in [KMIN, KMAX] (stdlib only).
Evidence for the formula F(k)=(k-1)(k-3); NOT a proof for any k outside the range.
Cyclic partitions are found directly as the points lying on cycles of the
functional graph of B (no theory assumed). Usage: python3 exhaustive_DB.py KMIN KMAX"""
import sys

def partitions(n, maxp=None):
    if maxp is None:
        maxp = n
    if n == 0:
        yield ()
        return
    for p in range(min(n, maxp), 0, -1):
        for rest in partitions(n - p, p):
            yield (p,) + rest

def B(lam):
    s = len(lam)
    new = [x - 1 for x in lam if x > 1] + [s]
    return tuple(sorted(new, reverse=True))

def DB(n):
    P = list(partitions(n))
    nxt = {p: B(p) for p in P}
    state = {}          # 0 = unvisited, 1 = on current path, 2 = finished
    cyclic = set()
    for p in P:
        if p in state:
            continue
        path = []
        pos = {}
        q = p
        while q not in state and q not in pos:
            pos[q] = len(path)
            path.append(q)
            q = nxt[q]
        if q in pos:                      # closed a new cycle
            cyclic.update(path[pos[q]:])
        for r in path:
            state[r] = 2
    d = {p: 0 for p in cyclic}
    for p in P:
        stack = []
        q = p
        while q not in d:
            stack.append(q)
            q = nxt[q]
        v = d[q]
        while stack:
            v += 1
            d[stack.pop()] = v
    m = max(d.values())
    return m, len(P), sorted(cyclic, reverse=True)

if __name__ == "__main__":
    kmin, kmax = int(sys.argv[1]), int(sys.argv[2])
    ok = True
    for k in range(kmin, kmax + 1):
        n = k * (k - 1) // 2 + 1
        m, npart, cyc = DB(n)
        F = (k - 1) * (k - 3)
        # cyclic set should be delta_{k-1} + e_j, j=1..k
        delta = list(range(k - 1, 0, -1))
        expected = set()
        for j in range(k):
            mu = delta + [0]
            mu[j] += 1
            expected.add(tuple(sorted([x for x in mu if x > 0], reverse=True)))
        cyc_ok = set(cyc) == expected
        print(f"k={k} n={n} #partitions={npart} D_B={m} F(k)={F} match={m == F} cyclic_set_is_delta+e_j={cyc_ok}", flush=True)
        ok = ok and (m == F) and cyc_ok
    print("ALL MATCH" if ok else "MISMATCH")
