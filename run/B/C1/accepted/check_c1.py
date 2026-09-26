"""Sanity check for B-C1 (stdlib only, exact integer arithmetic).
For every n in [1, NMAX]: enumerate all partitions of n, compute the cyclic ones by
iterating B (functional graph), compare with the predicted set {lambda(eps)}, count
cycles and compare with (1/k) sum_{d | gcd(k,r)} phi(d) C(k/d, r/d).
Also checks for triangular n that every orbit reaches delta_k.
Not load-bearing: the proof does not rest on this computation."""
import sys
from math import comb, gcd

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

def phi(m):
    return sum(1 for i in range(1, m + 1) if gcd(i, m) == 1)

def rank(n):
    k = 1
    while k * (k + 1) // 2 < n:
        k += 1
    return k

def predicted(k, r):
    out = set()
    for mask in range(1 << k):
        eps = [(mask >> (j)) & 1 for j in range(k)]  # eps[0..k-1] = eps_1..eps_k
        if sum(eps) != r:
            continue
        lam = tuple(x for x in (k - (j + 1) + eps[j] for j in range(k)) if x > 0)
        out.add(lam)
    return out

def main(NMAX):
    for n in range(1, NMAX + 1):
        k = rank(n)
        r = n - (k - 1) * k // 2
        parts = list(partitions(n))
        cyc = set()
        for lam in parts:
            seen = {}
            x = lam
            i = 0
            while x not in seen:
                seen[x] = i
                x = B(x)
                i += 1
            # x is the first repeated element: it lies on the cycle
            y = x
            while True:
                cyc.add(y)
                y = B(y)
                if y == x:
                    break
        pred = predicted(k, r)
        assert cyc == pred, (n, k, r)
        # count cycles
        left = set(cyc)
        ncyc = 0
        while left:
            x = left.pop()
            y = B(x)
            while y != x:
                left.discard(y)
                y = B(y)
            ncyc += 1
        g = gcd(k, r)
        num = sum(phi(d) * comb(k // d, r // d) for d in range(1, g + 1) if g % d == 0)
        assert num % k == 0 and num // k == ncyc, (n, k, r, ncyc, num)
        if r == k:
            delta = tuple(range(k, 0, -1))
            assert cyc == {delta}
            for lam in parts:
                x = lam
                for _ in range(len(parts) + 1):
                    if x == delta:
                        break
                    x = B(x)
                assert x == delta, (n, lam)
        print(f"n={n} k={k} r={r} #partitions={len(parts)} #cyclic={len(cyc)} #cycles={ncyc} OK")
    print("ALL OK up to", NMAX)

if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 40)
