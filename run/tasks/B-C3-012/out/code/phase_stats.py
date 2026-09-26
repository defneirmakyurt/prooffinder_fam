"""Exact phase statistics for Bulgarian solitaire (stdlib only).

For every rank k in [4, KMAX] and every non-triangular n with T_{k-1} < n < T_k, and every partition lam of n,
compute (0-based diagonals, cell (i,j) on diagonal i+j):
  d      = d_B(lam), cyclic test = Cell-1 criterion: D_{k-2} subset C subset D_{k-1}
           (diagonals 0..k-2 full, no cell on a diagonal >= k), i.e. k-i-1 <= lam_{i+1} <= k-i  (rows 0..k-1), no row k.
  tA     = first t with diagonals 0..k-2 full           (monotone: cells never move to a higher diagonal)
  tB     = first t with no cell on a diagonal >= k+1    (monotone, same reason)
  tC     = max(tA, tB) = entry time into C_k = {D_{k-2} subset C subset D_k}
Also checks, for every step of every orbit, that no cell moves to a higher diagonal in the sense
N_{>=e}(B lam) <= N_{>=e}(lam) for all e (the counting form of Lemma 1 in proof.md).
Prints per k: max d, max tA, max tB, max tC, max (d - tC).
This is a finite check; it proves nothing beyond the listed k.
"""
import sys

def partitions(n, maxpart=None):
    if maxpart is None:
        maxpart = n
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

def Nge(lam, e):
    # number of cells (i,j) with i+j >= e; row i has cells j=0..lam[i]-1
    c = 0
    for i, L in enumerate(lam):
        lo = max(0, e - i)
        if L > lo:
            c += L - lo
    return c

def full_upto(lam, m):
    # diagonals 0..m all full  <=> row i has length >= m+1-i for i=0..m
    for i in range(m + 1):
        L = lam[i] if i < len(lam) else 0
        if L < m + 1 - i:
            return False
    return True

def cyclic(lam, k):
    return full_upto(lam, k - 2) and Nge(lam, k) == 0

def main():
    KMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 8
    ok = True
    for k in range(4, KMAX + 1):
        Tk1 = (k - 1) * k // 2
        Tk = k * (k + 1) // 2
        mx = dict(d=0, tA=0, tB=0, tC=0, dmtC=-10**9)
        for n in range(Tk1 + 1, Tk):
            for lam in partitions(n):
                t = 0
                cur = lam
                tA = tB = None
                while True:
                    if tA is None and full_upto(cur, k - 2):
                        tA = t
                    if tB is None and Nge(cur, k + 1) == 0:
                        tB = t
                    if cyclic(cur, k):
                        break
                    nxt = B(cur)
                    maxdiag = len(cur) + cur[0]
                    for e in range(1, maxdiag + 2):
                        if Nge(nxt, e) > Nge(cur, e):
                            ok = False
                            print("MONOTONICITY FAIL", k, n, cur, nxt, e)
                    cur = nxt
                    t += 1
                d = t
                tC = max(tA, tB)
                mx['d'] = max(mx['d'], d)
                mx['tA'] = max(mx['tA'], tA)
                mx['tB'] = max(mx['tB'], tB)
                mx['tC'] = max(mx['tC'], tC)
                mx['dmtC'] = max(mx['dmtC'], d - tC)
                if d > k * k - 2 * k - 1:
                    ok = False
                    print("BOUND FAIL", k, n, lam, d)
        print(f"k={k}: max d={mx['d']} (bound {k*k-2*k-1}), max tA={mx['tA']}, max tB={mx['tB']}, "
              f"max tC={mx['tC']}, max(d-tC)={mx['dmtC']}, max tC + max(d-tC)={mx['tC']+mx['dmtC']}")
    print("ALL OK" if ok else "FAILURES")

if __name__ == "__main__":
    main()
