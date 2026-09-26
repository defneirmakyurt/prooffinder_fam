"""Referee B-C1-005 independent checker. Stdlib only, exact integer arithmetic.
Usage: python3 referee_check.py NMAX_FULL NMAX_LEMMAS KMAX_NECK
Part A (n in [1, NMAX_FULL]): exhaustive functional graph of B on P(n); cyclic set (nodes on cycles)
   vs C(k,r) built independently; #cycles vs necklace formula AND vs brute-force rotation orbit count;
   cycle lengths vs rotation-orbit sizes; (i): at n=T_k every partition reaches delta_k.
Part B (n in [1, NMAX_LEMMAS]): per-partition checks of Lemma 1 (E(mu)=E(lambda)), Lemma 3(a),(b),
   Lemma 4 (Y(B lam)=tau(Y lam) whenever s>=lam0-1), Lemma 6(b) on cyclic partitions, Prop 7 on cyclic
   partitions, and the converse sanity (Lemma 4 fails when s<lam0-1 -> must differ).
Part C (k in [1, KMAX_NECK]): Theorem 9(d) B(lambda(eps)) = lambda(rho eps) for all eps in {0,1}^k with sum>=1,
   and the formula N(k,r) vs brute-force orbit count on W(k,r).
Part D: statement example chain S6.
"""
import sys, random
from itertools import combinations, product
from math import comb, gcd

def parts_of(n):
    # iterative ascending-composition based generator (independent from subject's recursive one)
    a = [0] * (n + 1)
    k = 1
    a[1] = n
    while k != 0:
        x = a[k - 1] + 1
        y = a[k] - 1
        k -= 1
        while x <= y:
            a[k] = x
            y -= x
            k += 1
        a[k] = x + y
        yield tuple(sorted(a[:k + 1], reverse=True))

def B(lam):
    s = len(lam)
    out = [x - 1 for x in lam if x - 1 > 0]
    out.append(s)
    out.sort(reverse=True)
    return tuple(out)

def E(x):
    return sum(i * v + v * (v - 1) // 2 for i, v in enumerate(x))

def Y(lam):
    return frozenset((a, b) for a, v in enumerate(lam) for b in range(v))

def tau(p):
    a, b = p
    return (a + 1, b - 1) if b >= 1 else (0, a)

def rank_r(n):
    k = 0
    while k * (k + 1) // 2 < n:
        k += 1
    return k, n - (k - 1) * k // 2

def lam_eps(eps):
    k = len(eps)
    L = [k - 1 - a + eps[a] for a in range(k)]
    if L[-1] == 0:
        L = L[:-1]
    return tuple(L)

def C_set(k, r):
    res = set()
    for ones in combinations(range(k), r):
        eps = tuple(1 if a in ones else 0 for a in range(k))
        res.add(lam_eps(eps))
    return res

def phi(m):
    return sum(1 for i in range(1, m + 1) if gcd(i, m) == 1)

def N_formula(k, r):
    g = gcd(k, r)
    tot = sum(phi(d) * comb(k // d, r // d) for d in range(1, g + 1) if g % d == 0)
    assert tot % k == 0
    return tot // k

def rot(eps):
    return (eps[-1],) + eps[:-1]

def orbits_brute(k, r):
    seen = set(); cnt = 0; sizes = []
    for ones in combinations(range(k), r):
        e = tuple(1 if a in ones else 0 for a in range(k))
        if e in seen: continue
        cnt += 1; o = set(); x = e
        while x not in o:
            o.add(x); x = rot(x)
        seen |= o; sizes.append(len(o))
    return cnt, sorted(sizes)

def cycles_of(Bmap):
    # standard colouring for functional graph
    state = {}
    cyc_nodes = set(); cycles = []
    for s0 in Bmap:
        if s0 in state: continue
        path = []; x = s0
        while x not in state:
            state[x] = 1; path.append(x); x = Bmap[x]
        if state[x] == 1:  # new cycle found, x on current path
            c = [x]; y = Bmap[x]
            while y != x:
                c.append(y); y = Bmap[y]
            cycles.append(c); cyc_nodes |= set(c)
        for p in path: state[p] = 2
    return cyc_nodes, cycles

def partA(nmax):
    for n in range(1, nmax + 1):
        k, r = rank_r(n)
        assert 1 <= r <= k
        P = list(parts_of(n))
        assert len(set(P)) == len(P) and all(sum(p) == n for p in P)
        Bm = {p: B(p) for p in P}
        cyc, cycles = cycles_of(Bm)
        C = C_set(k, r)
        assert cyc == C, ("cyclic set mismatch", n)
        assert len(C) == comb(k, r)
        nb, sizes = orbits_brute(k, r)
        assert len(cycles) == N_formula(k, r) == nb, ("cycle count mismatch", n, len(cycles), N_formula(k, r), nb)
        assert sorted(len(c) for c in cycles) == sizes, ("cycle lengths mismatch", n)
        if r == k:
            delta = tuple(range(k, 0, -1))
            assert cyc == {delta}
            for p in P:
                x = p
                for _ in range(len(P) + 1):
                    if x == delta: break
                    x = Bm[x]
                assert x == delta
        print(f"A n={n} k={k} r={r} p(n)={len(P)} cyclic={len(cyc)} cycles={len(cycles)} formula={N_formula(k,r)} lens={sorted(len(c) for c in cycles)}")

def partB(nmax):
    tot = 0; sortfree = 0
    for n in range(1, nmax + 1):
        P = list(parts_of(n))
        Bm = {p: B(p) for p in P}
        cyc, _ = cycles_of(Bm)
        for lam in P:
            tot += 1
            s = len(lam)
            mu = (s,) + tuple(v - 1 for v in lam)
            assert E(mu) == E(lam)                          # Lemma 1
            b = Bm[lam]
            assert E(b) <= E(lam)                           # Lemma 3(a)
            if E(b) == E(lam): assert s >= lam[0] - 1       # Lemma 3(b)
            ty = frozenset(tau(p) for p in Y(lam))
            if s >= lam[0] - 1:                             # Lemma 4
                sortfree += 1
                assert Y(b) == ty
                assert tuple(v for v in mu if v > 0) == b   # Lemma 3(c)
            else:
                assert E(b) < E(lam)                        # strictness when not sort-free
            if lam in cyc:
                assert s >= lam[0] - 1                      # Lemma 6(b)
                Yl = Y(lam)
                maxd = max(a + bb for a, bb in Yl)
                for d in range(0, maxd):
                    holes = [(a, d - a) for a in range(d + 1) if (a, d - a) not in Yl]
                    if holes:
                        for d2 in range(d + 1, maxd + 1):
                            assert not any((a, d2 - a) in Yl for a in range(d2 + 1)), ("Prop7 fails", lam)
    print(f"B checked {tot} partitions (n<= {nmax}); sort-free steps {sortfree}; Lemmas 1,3,4,6(b), Prop 7 OK")

def partC(kmax):
    for k in range(1, kmax + 1):
        for eps in product((0, 1), repeat=k):
            r = sum(eps)
            if r == 0: continue
            lam = lam_eps(eps)
            assert sum(lam) == (k - 1) * k // 2 + r
            assert all(lam[i] >= lam[i + 1] for i in range(len(lam) - 1)) and all(v > 0 for v in lam)
            assert len(lam) == k - 1 + eps[-1]
            assert B(lam) == lam_eps(rot(eps)), ("Thm 9(d) fails", eps)
        for r in range(1, k + 1):
            nb, _ = orbits_brute(k, r)
            assert nb == N_formula(k, r), (k, r)
    print(f"C Thm 9(a),(d) for all eps in {{0,1}}^k, sum>=1, k<= {kmax}; N(k,r) == brute orbit count for all 1<=r<=k<= {kmax}")

def partD():
    assert B((2, 1, 1, 1, 1)) == (5, 1)
    assert B((5, 1)) == (4, 2)
    assert B((4, 2)) == (3, 2, 1)
    assert B((3, 2, 1)) == (3, 2, 1)
    print("D statement example chain OK")

def partR(trials, seed=12345):
    # random tests of Lemma 2 (sorting lowers E, strictly if unsorted) on arbitrary nonneg sequences
    rng = random.Random(seed)
    for _ in range(trials):
        m = rng.randint(1, 12)
        x = [rng.randint(0, 15) for _ in range(m)]
        xs = sorted(x, reverse=True)
        if xs == x: assert E(xs) == E(x)
        else: assert E(xs) < E(x)
    print(f"R Lemma 2 random test: {trials} sequences OK (seed {seed})")

if __name__ == "__main__":
    nA = int(sys.argv[1]); nB = int(sys.argv[2]); kC = int(sys.argv[3])
    partD(); partR(200000); partC(kC); partB(nB); partA(nA)
    print("ALL REFEREE CHECKS PASSED")
