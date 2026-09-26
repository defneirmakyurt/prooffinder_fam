#!/usr/bin/env python3
"""Exact (integer-only, stdlib-only) checks for D_B(T_k).

Part A (exhaustive, k = 1..KMAX): for every partition lam of T_k, iterate B until
         delta_k is reached, compute t(lam) = min{t : B^t(lam) = delta_k}, and report
         max t over all lam, compared with k^2 - k.  (Finite check only.)
Part B (k = 2..KWIT): simulate the explicit witness
         lam^(k) = (k-1, k-1, k-2, ..., 2, 1, 1) and report the first t with
         B^t(lam^(k)) = delta_k, compared with k^2 - k.
Usage: python3 check_triangular.py [KMAX] [KWIT]
"""
import sys

def B(l):
    s = len(l)
    return tuple(sorted([x - 1 for x in l if x > 1] + [s], reverse=True))

def partitions(n, m=None):
    if m is None:
        m = n
    if n == 0:
        yield ()
        return
    for p in range(min(n, m), 0, -1):
        for r in partitions(n - p, p):
            yield (p,) + r

def time_to_delta(l, delta, memo):
    path = []
    x = l
    while x != delta and x not in memo:
        path.append(x)
        x = B(x)
    base = 0 if x == delta else memo[x]
    for i, y in enumerate(reversed(path)):
        memo[y] = base + i + 1
    return memo.get(l, 0)

def main():
    KMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    KWIT = int(sys.argv[2]) if len(sys.argv) > 2 else 60
    ok = True
    for k in range(1, KMAX + 1):
        n = k * (k + 1) // 2
        delta = tuple(range(k, 0, -1))
        memo = {delta: 0}
        best, cnt = -1, 0
        for l in partitions(n):
            t = time_to_delta(l, delta, memo)
            cnt += 1
            if t > best:
                best = t
        good = (best == k * k - k)
        ok &= good
        print(f"A k={k} T_k={n} #partitions={cnt} max_t={best} k^2-k={k*k-k} {'OK' if good else 'MISMATCH'}")
    for k in range(2, KWIT + 1):
        delta = tuple(range(k, 0, -1))
        l = tuple([k - 1] + list(range(k - 1, 0, -1)) + [1])
        assert sum(l) == k * (k + 1) // 2
        t = 0
        while l != delta:
            l = B(l)
            t += 1
        good = (t == k * k - k)
        ok &= good
        if not good or k <= 6 or k % 10 == 0:
            print(f"B k={k} witness time={t} k^2-k={k*k-k} {'OK' if good else 'MISMATCH'}")
    print("ALL OK" if ok else "SOME MISMATCH")

if __name__ == "__main__":
    main()
