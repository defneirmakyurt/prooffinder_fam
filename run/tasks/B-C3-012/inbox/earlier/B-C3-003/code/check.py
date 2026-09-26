"""Exact (integer) finite checks for B-C3.  stdlib only.
Usage: python3 check.py [KMAX_EXHAUSTIVE] [KMAX_ORBIT]
 (1) exhaustive over all partitions of n, T_{k-1}<n<T_k, 4<=k<=KMAX_EXHAUSTIVE:
     D_B(n) <= k^2-2k-1, D_B(T_k-1) = k^2-2k-1, X_k attains it, extremal counts.
     Cyclic partitions found by generic cycle detection (independent of Cell 1).
 (2) for 4<=k<=KMAX_ORBIT: d_B(X_k) = k^2-2k-1 by direct iteration, cyclicity tested
     with the Cell-1 criterion (delta_m contained, other r cells on diagonal m).
 (3) for 4<=k<=KMAX_ORBIT: over the class L (delta_m + (m-1) cells on diag m + one cell on
     diag m+1) max d_B = k^2-2k-1, attained only by X_k.
"""
import sys
def partitions(n, mx=None):
    if mx is None: mx = n
    if n == 0:
        yield (); return
    for p in range(min(n, mx), 0, -1):
        for rest in partitions(n - p, p):
            yield (p,) + rest
def B(l):
    s = len(l)
    return tuple(sorted([x - 1 for x in l if x > 1] + [s], reverse=True))
def dvals(n):
    ps = list(partitions(n)); cyc = set()
    for p in ps:
        seen = {}; x = p; order = []
        while x not in seen and x not in cyc:
            seen[x] = len(order); order.append(x); x = B(x)
        if x in seen:
            for y in order[seen[x]:]: cyc.add(y)
    d = {c: 0 for c in cyc}
    for p in ps:
        x = p; path = []
        while x not in d:
            path.append(x); x = B(x)
        v = d[x]
        for y in reversed(path):
            v += 1; d[y] = v
    return d
def T(k): return k * (k + 1) // 2
def X(k):
    m = k - 1
    return tuple([m, m - 1] + [m + 2 - i for i in range(3, m + 2)] + [1])
def cells(l): return {(i, j) for i, x in enumerate(l) for j in range(x)}
def cyclic_cell1(l, m):
    # Cell 1: cyclic iff l = (m+e_1, m-1+e_2, ..., 1+e_m, e_{m+1}), e in {0,1}^{m+1}
    # i.e. delta_m contained and every other cell on diagonal m
    if len(l) not in (m, m + 1): return False
    ll = list(l) + [0] * (m + 1 - len(l))
    return all(ll[i] - (m - i) in (0, 1) for i in range(m + 1))
def d_iter(l, m, cap=10**6):
    t = 0
    while not cyclic_cell1(l, m):
        l = B(l); t += 1
        if t > cap: raise RuntimeError
    return t
def from_diag(m, occ_m, c):
    # delta_m plus diag-m cells at rows occ_m plus diag-(m+1) cell at row c; None if not a partition
    cs = {(i, j) for i in range(m) for j in range(m - i)} | {(i, m - i) for i in occ_m} | {(c, m + 1 - c)}
    for (i, j) in cs:
        if (i > 0 and (i - 1, j) not in cs) or (j > 0 and (i, j - 1) not in cs): return None
    rows = {}
    for (i, j) in cs: rows[i] = rows.get(i, 0) + 1
    return tuple(rows[i] for i in range(len(rows)))
if __name__ == "__main__":
    K1 = int(sys.argv[1]) if len(sys.argv) > 1 else 9
    K2 = int(sys.argv[2]) if len(sys.argv) > 2 else 20
    ok = True
    for k in range(4, K1 + 1):
        bound = k * k - 2 * k - 1
        mx = 0
        for n in range(T(k - 1) + 1, T(k)):
            d = dvals(n); M = max(d.values()); mx = max(mx, M)
            if M > bound: ok = False; print("FAIL (a)", k, n, M)
            if n == T(k) - 1:
                E = sorted(p for p in d if d[p] == M)
                good = (M == bound) and d[X(k)] == M
                ok &= good
                print(f"k={k} n={n} D={M} bound={bound} X_k={X(k)} d(X_k)={d[X(k)]} #extremal={len(E)} {'OK' if good else 'FAIL'}")
                if k <= 5: print("   extremal:", E)
        print(f"k={k}: max over T_(k-1)<n<T_k of D(n) = {mx} <= {bound}", flush=True)
    for k in range(4, K2 + 1):
        m = k - 1
        dx = d_iter(X(k), m)
        best = -1; arg = []
        for c in range(m + 2):
            for a in range(m + 1):
                for b in range(a + 1, m + 1):
                    occ = [i for i in range(m + 1) if i not in (a, b)]
                    l = from_diag(m, occ, c)
                    if l is None: continue
                    dv = d_iter(l, m)
                    if dv > best: best = dv; arg = [l]
                    elif dv == best: arg.append(l)
        good = dx == k * k - 2 * k - 1 and best == dx and arg == [X(k)]
        ok &= good
        print(f"k={k}: d(X_k)={dx}, class-L max={best}, unique maximiser X_k: {arg == [X(k)]} {'OK' if good else 'FAIL'}", flush=True)
    print("ALL OK" if ok else "SOME FAIL")
