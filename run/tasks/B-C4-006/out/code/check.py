#!/usr/bin/env python3
"""Stdlib-only checks for B-C4 (n = T_{k-1}+1). Exact integer arithmetic throughout.
Usage: python3 check.py [KMAX_EXHAUSTIVE] [KMAX_FAMILY] [KMAX_LEVEL1]
 (1) exhaustive D_B(T_{k-1}+1) for 5<=k<=KMAX_EXHAUSTIVE (evidence only, not a proof for all k);
 (2) lower-bound family lambda^(k): d_B = (k-1)(k-3), B^{F-1} = (k,k-1,k-3,...,2), B^F = lambda(e_3), 5<=k<=KMAX_FAMILY;
 (3) level-1 theorem: over ALL partitions with E = Emin+1 (enumerated via (Q,{P,P'})), max d_B = (k-1)(k-3)
     and d_B equals the closed form T of proof.md Step 14, 5<=k<=KMAX_LEVEL1.
Cyclicity is tested by E == Emin (proof.md Step 6, from B-C1)."""
import sys
def partitions(n, maxp=None):
    if maxp is None: maxp = n
    if n == 0:
        yield (); return
    for p in range(min(n, maxp), 0, -1):
        for rest in partitions(n - p, p):
            yield (p,) + rest
def B(l):
    s = len(l)
    return tuple(sorted([x - 1 for x in l if x > 1] + [s], reverse=True))
def E(l):
    return sum(i * r + r * (r - 1) // 2 for i, r in enumerate(l, start=1))
def Emin(k):
    return sum(d * d for d in range(1, k)) + k
def is_cyclic_bc1(l, k):
    # B-C1 form with r=1: delta_{k-1} plus one cell in position e_j
    d = [k - i for i in range(1, k)] + [0]
    for j in range(k):
        c = d[:]; c[j] += 1
        c = tuple(x for x in c if x > 0)
        if c == l: return True
    return False
def exhaustive(k):
    n = k * (k - 1) // 2 + 1; em = Emin(k)
    dmap = {}
    for p in partitions(n):
        path = []; q = p
        while q not in dmap and E(q) != em:
            path.append(q); q = B(q)
        base = 0 if q not in dmap else dmap[q]
        if q not in dmap: dmap[q] = 0
        for x in reversed(path):
            base += 1; dmap[x] = base
    return max(dmap.values())
def dB(l, k):
    em = Emin(k); t = 0
    while E(l) != em:
        l = B(l); t += 1
    return t, l
def family(k):
    lam = tuple([k - 2] + [k - i for i in range(2, k - 1)] + [2, 1])
    assert sum(lam) == k * (k - 1) // 2 + 1
    F = (k - 1) * (k - 3); l = lam
    for t in range(F - 1):
        assert not is_cyclic_bc1(l, k); l = B(l)
    assert l == tuple([k, k - 1] + [k - i for i in range(3, k - 1)]), (k, l)
    assert not is_cyclic_bc1(l, k)
    l = B(l)
    assert l == tuple([k - 1, k - 2, k - 2] + [k - i for i in range(4, k)]) and is_cyclic_bc1(l, k)
    return True
def config_to_partition(k, Q, Ps):
    # diag d cell at 0-indexed position P is (P+1, d-P); diags 1..k-2 full, diag k-1 minus position Q, diag k at Ps
    rows = [0] * (k + 1)
    cells = set()
    for d in range(1, k - 1):
        for P in range(d): cells.add((P + 1, d - P))
    for P in range(k - 1):
        if P != Q: cells.add((P + 1, k - 1 - P))
    for P in Ps: cells.add((P + 1, k - P))
    for (i, j) in cells: rows[i] = max(rows[i], j)
    lam = tuple(r for r in rows[1:] if r > 0)
    # Young test: set of cells equals the diagram of lam
    diag = {(i, j) for i in range(1, len(lam) + 1) for j in range(1, lam[i - 1] + 1)}
    decreasing = all(lam[i] >= lam[i + 1] for i in range(len(lam) - 1))
    return lam if (diag == cells and decreasing) else None
def closed_form_T(k, Q, P, P2):
    t0 = (k - 1 - Q) % (k - 1)
    pi, pi2 = (P + t0) % k, (P2 + t0) % k
    return t0 + (min(pi, pi2) - 1) * (k - 1)
def level1(k):
    em = Emin(k); best = 0; count = 0
    for Q in range(k - 1):
        for P in range(k):
            for P2 in range(P + 1, k):
                lam = config_to_partition(k, Q, (P, P2))
                ok = (P not in (Q, Q + 1)) and (P2 not in (Q, Q + 1))
                assert (lam is not None) == ok
                if lam is None: continue
                assert E(lam) == em + 1
                count += 1
                t, _ = dB(lam, k)
                assert t == closed_form_T(k, Q, P, P2), (k, Q, P, P2, t)
                best = max(best, t)
    # every partition at level 1 arises this way: compare counts by brute force for small k
    return best, count
if __name__ == "__main__":
    K1 = int(sys.argv[1]) if len(sys.argv) > 1 else 11
    K2 = int(sys.argv[2]) if len(sys.argv) > 2 else 60
    K3 = int(sys.argv[3]) if len(sys.argv) > 3 else 25
    for k in range(5, K1 + 1):
        m = exhaustive(k)
        print("exhaustive k=%d n=%d D_B=%d (k-1)(k-3)=%d %s" % (k, k*(k-1)//2+1, m, (k-1)*(k-3), "OK" if m == (k-1)*(k-3) else "MISMATCH"))
    for k in range(5, K2 + 1): family(k)
    print("family lambda^(k): d_B=(k-1)(k-3) with predicted B^{F-1}, B^F for k=5..%d OK" % K2)
    for k in range(5, K3 + 1):
        best, cnt = level1(k)
        assert best == (k - 1) * (k - 3)
        if k <= 9:  # brute-force count of level-1 partitions
            n = k*(k-1)//2+1; em = Emin(k)
            assert cnt == sum(1 for p in partitions(n) if E(p) == em + 1)
    print("level-1: max d_B=(k-1)(k-3), closed form T matches, k=5..%d OK (count cross-checked k<=9)" % K3)
