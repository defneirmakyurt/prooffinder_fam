"""Exact (integer) checks for B-C4.  stdlib only.
Usage: python3 check.py KMAX_EXHAUSTIVE KMAX_ORBIT
 (1) For k = 5..KMAX_EXHAUSTIVE: computes D_B(T_{k-1}+1) exhaustively over ALL
     partitions of n = T_{k-1}+1 and compares with (k-1)(k-3).  (Finite range only;
     proves nothing for larger k.)  Also checks: d_B(lam) = (k-1)(k-3) is attained by
     lam^(k) = (k-2,k-2,k-3,...,3,2,2,1), and that every near state D(p,Q), |Q|=2,
     has d_B <= (k-1)(k-3) (sanity check of Theorem N).
 (2) For k = 5..KMAX_ORBIT: simulates the orbit of lam^(k) directly and checks
     d_B(lam^(k)) = (k-1)(k-3) (sanity check of the symbolic orbit in proof.md, Part L).
"""
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

def is_cyclic_k(lam, k):
    # cyclic partitions of T_{k-1}+1 (gated B-C1, r=1): delta_{k-1} plus one cell
    if len(lam) > k:
        return False
    L = list(lam) + [0] * (k - len(lam))
    diff = [L[i] - (k - 1 - i) for i in range(k)]
    return all(x in (0, 1) for x in diff) and sum(diff) == 1

def all_depths(n):
    parts = list(partitions(n))
    nxt = {p: B(p) for p in parts}
    cyc = set()
    for p in parts:           # generic cycle detection, independent of B-C1
        seen = set(); x = p
        while x not in seen:
            seen.add(x); x = nxt[x]
        y = x
        while True:
            cyc.add(y); y = nxt[y]
            if y == x:
                break
    d = {c: 0 for c in cyc}
    for p in parts:
        path = []; x = p
        while x not in d:
            path.append(x); x = nxt[x]
        base = d[x]
        for q in reversed(path):
            base += 1; d[q] = base
    return d, cyc

def lam_k(k):
    return tuple([k - 2] + [k - i for i in range(2, k - 1)] + [2, 1])

def near_state(k, p, Q):
    # diagram: delta_{k-2} full, diag k-1 minus position p, diag k positions in Q
    cells = set()
    for d in range(1, k - 1):
        for pos in range(1, d + 1):
            cells.add((pos, d - pos + 1))
    for pos in range(1, k):
        if pos != p:
            cells.add((pos, k - pos))
    for pos in Q:
        cells.add((pos, k - pos + 1))
    # valid Young diagram iff closed under moving up / left
    for (i, j) in cells:
        if (i > 1 and (i - 1, j) not in cells) or (j > 1 and (i, j - 1) not in cells):
            return None
    rows = {}
    for (i, j) in cells:
        rows[i] = rows.get(i, 0) + 1
    lam = tuple(rows[i] for i in sorted(rows))
    return lam

def depth_single(lam, k):
    t = 0
    while not is_cyclic_k(lam, k):
        lam = B(lam); t += 1
    return t

def main():
    K1 = int(sys.argv[1]); K2 = int(sys.argv[2])
    ok = True
    for k in range(5, K1 + 1):
        n = k * (k - 1) // 2 + 1
        d, cyc = all_depths(n)
        cyc_ok = all(is_cyclic_k(c, k) for c in cyc) and \
            sum(1 for p in d if is_cyclic_k(p, k)) == len(cyc)
        F = (k - 1) * (k - 3)
        M = max(d.values())
        lk = lam_k(k)
        nmax = 0; nn = 0
        for p in range(1, k):
            for q1 in range(1, k + 1):
                for q2 in range(q1 + 1, k + 1):
                    lam = near_state(k, p, (q1, q2))
                    if lam is None:
                        continue
                    nn += 1
                    nmax = max(nmax, d[lam])
        good = (M == F) and (d[lk] == F) and cyc_ok and (nmax <= F)
        ok &= good
        print(f"k={k} n={n} #partitions={len(d)} D_B={M} (k-1)(k-3)={F} "
              f"d(lam^(k))={d[lk]} cyclic-set-matches-B-C1={cyc_ok} "
              f"#near-states={nn} max-d-near={nmax} {'OK' if good else 'FAIL'}")
    for k in range(5, K2 + 1):
        F = (k - 1) * (k - 3)
        dk = depth_single(lam_k(k), k)
        if dk != F:
            ok = False
            print(f"orbit k={k}: d={dk} != {F} FAIL")
    print(f"orbit check lam^(k), k=5..{K2}: {'all d=(k-1)(k-3)' if ok else 'FAIL somewhere'}")
    print("ALL OK" if ok else "FAILURE")

if __name__ == "__main__":
    main()
