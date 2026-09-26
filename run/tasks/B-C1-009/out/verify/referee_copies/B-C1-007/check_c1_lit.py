"""Sanity check for B-C1 (literature run B-C1-007). Stdlib only, exact integers.
NOT load-bearing: proof.md does not depend on it.

For every n in [1, NMAX]:
  * enumerate all partitions of n, apply the shift B;
  * check Lemma 3 of proof.md: E(B(lam)) <= E(lam), with equality iff lam_1 - 1 <= s;
  * find the cyclic partitions (points on cycles of the functional graph of B);
  * check they are exactly {lambda(eps) : eps in {0,1}^k, |eps| = r} (k = rank, r = n - T_{k-1});
  * count the cycles and compare with N(k,r) = (1/k) sum_{d | gcd(k,r)} phi(d) C(k/d, r/d);
  * for r = k check the cyclic set is {delta_k} (so every orbit reaches delta_k).
Usage: python3 check_c1_lit.py NMAX
"""
import sys
from math import comb, gcd
from itertools import combinations

def partitions(n, maxpart=None):
    if maxpart is None:
        maxpart = n
    if n == 0:
        yield ()
        return
    for first in range(min(n, maxpart), 0, -1):
        for rest in partitions(n - first, first):
            yield (first,) + rest

def shift(lam):
    s = len(lam)
    parts = [x - 1 for x in lam if x > 1] + [s]
    return tuple(sorted(parts, reverse=True))

def energy(c):  # sum over cells (pile q, height h), 1-based, of level q + h - 1
    return sum((q - 1) * x + x * (x + 1) // 2 for q, x in enumerate(c, start=1))

def phi(m):
    return sum(1 for i in range(1, m + 1) if gcd(i, m) == 1)

def necklaces(k, r):
    g = gcd(k, r)
    tot = sum(phi(d) * comb(k // d, r // d) for d in range(1, g + 1) if g % d == 0)
    assert tot % k == 0
    return tot // k

def rank(n):
    k = 1
    while k * (k + 1) // 2 < n:
        k += 1
    return k

def lam_eps(k, ones):
    L = [k - i + (1 if i in ones else 0) for i in range(1, k + 1)]
    if L[-1] == 0:
        L.pop()
    return tuple(L)

def check(n):
    parts = list(partitions(n))
    nxt = {}
    for lam in parts:
        mu = shift(lam)
        assert sum(mu) == n
        e0, e1 = energy(lam), energy(mu)
        assert e1 <= e0
        assert (e1 == e0) == (lam[0] - 1 <= len(lam)), (lam, mu)
        nxt[lam] = mu
    # cyclic points: iterate B |P(n)| times from everything -> image set of B^M is the set of cyclic points
    cur = set(parts)
    for _ in range(len(parts)):
        new = {nxt[x] for x in cur}
        if new == cur:
            break
        cur = new
    cyc = cur
    for x in cyc:  # verify each is really periodic
        y, steps = nxt[x], 1
        while y != x:
            y, steps = nxt[y], steps + 1
            assert steps <= len(parts)
    k = rank(n); r = n - (k - 1) * k // 2
    pred = {lam_eps(k, set(S)) for S in combinations(range(1, k + 1), r)}
    assert len(pred) == comb(k, r)
    assert cyc == pred, (n, sorted(cyc), sorted(pred))
    seen = set(); ncyc = 0
    for x in cyc:
        if x in seen:
            continue
        ncyc += 1
        y = x
        while y not in seen:
            seen.add(y); y = nxt[y]
    assert ncyc == necklaces(k, r), (n, ncyc, necklaces(k, r))
    if r == k:
        assert cyc == {tuple(range(k, 0, -1))}
    return len(parts), k, r, len(cyc), ncyc

if __name__ == "__main__":
    NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 40
    for n in range(1, NMAX + 1):
        p, k, r, c, nc = check(n)
        print(f"n={n} |P|={p} k={k} r={r} cyclic={c} cycles={nc} OK")
    print(f"ALL OK up to n = {NMAX}")
