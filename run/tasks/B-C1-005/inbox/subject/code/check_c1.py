"""Sanity check (NOT load-bearing) for B-C1. Stdlib only, exact integer arithmetic.
For every n in [1, NMAX]: enumerate all partitions of n, apply the shift B, find the cyclic
partitions (those on a cycle of the functional graph) and the cycles; compare with
  C(k,r) = {(k-1+e_0, k-2+e_1, ..., e_{k-1}) minus trailing 0 : e in {0,1}^k, sum e = r}
and with the necklace count (1/k) sum_{d | gcd(k,r)} phi(d) binom(k/d, r/d).
Also checks the energy monotonicity E(B(l)) <= E(l), and that every orbit at n = T_k reaches delta_k.
"""
import sys
from itertools import combinations
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


def shift(lam):
    s = len(lam)
    parts = [x - 1 for x in lam if x > 1] + [s]
    return tuple(sorted(parts, reverse=True))


def energy(x):
    return sum(a * v + v * (v - 1) // 2 for a, v in enumerate(x))


def totient(m):
    return sum(1 for j in range(1, m + 1) if gcd(j, m) == 1)


def rank(n):
    k = 1
    while k * (k + 1) // 2 < n:
        k += 1
    return k


def predicted(k, r):
    out = set()
    for ones in combinations(range(k), r):
        rows = [k - 1 - a + (1 if a in ones else 0) for a in range(k)]
        out.add(tuple(x for x in rows if x > 0))
    return out


def necklaces(k, r):
    g = gcd(k, r)
    tot = sum(totient(d) * comb(k // d, r // d) for d in range(1, g + 1) if g % d == 0)
    assert tot % k == 0
    return tot // k


def main(nmax):
    for n in range(1, nmax + 1):
        k = rank(n)
        r = n - (k - 1) * k // 2
        assert 1 <= r <= k
        parts = list(partitions(n))
        B = {lam: shift(lam) for lam in parts}
        for lam in parts:
            assert energy(B[lam]) <= energy(lam)
        # cyclic = on a cycle: iterate |P| times lands on a cycle; collect the image set
        cyc = set()
        for lam in parts:
            x = lam
            seen = {}
            i = 0
            while x not in seen:
                seen[x] = i
                x = B[x]
                i += 1
            # x is the first repeated element: on a cycle
            y = x
            while True:
                cyc.add(y)
                y = B[y]
                if y == x:
                    break
        assert cyc == predicted(k, r), (n, k, r)
        # count cycles
        left = set(cyc)
        ncyc = 0
        while left:
            x = left.pop()
            y = B[x]
            while y != x:
                left.discard(y)
                y = B[y]
            ncyc += 1
        assert ncyc == necklaces(k, r), (n, ncyc, necklaces(k, r))
        if r == k:
            delta = tuple(range(k, 0, -1))
            assert cyc == {delta}
        print(f"n={n} k={k} r={r} #partitions={len(parts)} #cyclic={len(cyc)} #cycles={ncyc} OK")
    print("ALL OK up to n =", nmax)


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 45)
