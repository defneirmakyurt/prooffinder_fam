"""Independent referee check for B-C1 (stdlib only, exact integer arithmetic).
Written from the statement's definitions, not from the subject's code.
For each n in [1, NMAX]:
  * enumerate P(n) (non-recursive, different generator from the subject's);
  * B implemented literally: take one card from each pile, drop empty piles, add a pile of s cards, sort;
  * cyclic set = nodes of the functional graph of B lying on cycles, computed by peeling
    in-degree-0 nodes (Kahn), a different method from the subject's;
  * for n <= DEFN_MAX additionally the literal definition: exists 1<=i<=|P(n)| with B^i(lam)=lam;
  * cycles counted as connected components among cyclic nodes; cycle lengths recorded;
  * compare with the claimed set C(k,r), |C(k,r)| = binom(k,r), the claimed formula N(k,r),
    and with a brute-force necklace count (orbits of rotation on 0/1 words), and the orbit-size multiset;
  * intermediate claims: Lemma 1 (E(mu)=E(lam)), Lemma 3(a)(b)(c), Lemma 4 (Y(B lam)=tau(Y lam) when s>=lam_0-1),
    Lemma 6(b) (on cycles s>=lam_0-1), Cor 8 shape (full diagonals below e, cells only on D_e, none above),
    Thm 9(d) B(lam(eps))=lam(rho eps), (i): every lam of T_k reaches delta_k (by direct iteration).
"""
import sys, random
from math import comb, gcd
from itertools import combinations

def parts_of(n):
    # ascending-composition style generator (Kelleher), output as weakly decreasing tuples
    # standard accel_asc
    a = [0 for _ in range(n + 1)]
    k = 1
    y = n - 1
    while k != 0:
        x = a[k - 1] + 1
        k -= 1
        while 2 * x <= y:
            a[k] = x
            y -= x
            k += 1
        l = k + 1
        while x <= y:
            a[k] = x
            a[l] = y
            yield tuple(sorted(a[:k + 2], reverse=True))
            x += 1
            y -= 1
        a[k] = x + y
        y = x + y - 1
        yield tuple(sorted(a[:k + 1], reverse=True))

def pcount(n):
    # Euler pentagonal recurrence, independent count of partitions
    p = [1] + [0] * n
    for m in range(1, n + 1):
        tot, j = 0, 1
        while True:
            g1 = j * (3 * j - 1) // 2
            if g1 > m:
                break
            sg = 1 if j % 2 == 1 else -1
            tot += sg * p[m - g1]
            g2 = j * (3 * j + 1) // 2
            if g2 <= m:
                tot += sg * p[m - g2]
            j += 1
        p[m] = tot
    return p[n]

def B(lam):
    s = len(lam)
    piles = []
    for p in lam:
        if p - 1 > 0:
            piles.append(p - 1)
    piles.append(s)
    piles.sort(reverse=True)
    return tuple(piles)

def E(x):
    return sum(a * v + v * (v - 1) // 2 for a, v in enumerate(x))

def Y(lam):
    return frozenset((a, b) for a in range(len(lam)) for b in range(lam[a]))

def tau(c):
    a, b = c
    return (a + 1, b - 1) if b >= 1 else (0, a)

def T(k):
    return k * (k + 1) // 2

def rank(n):
    k = 1
    while T(k) < n:
        k += 1
    return k

def lam_of(eps):
    k = len(eps)
    L = [k - 1 - a + eps[a] for a in range(k)]
    if L[-1] == 0:
        L = L[:-1]
    return tuple(L)

def claimed_set(k, r):
    out = set()
    for ones in combinations(range(k), r):
        eps = [0] * k
        for a in ones:
            eps[a] = 1
        out.add(lam_of(tuple(eps)))
    return out

def phi(m):
    res, x, p = m, m, 2
    while p * p <= x:
        if x % p == 0:
            while x % p == 0:
                x //= p
            res -= res // p
        p += 1
    if x > 1:
        res -= res // x
    return res

def N_formula(k, r):
    g = gcd(k, r)
    tot = sum(phi(d) * comb(k // d, r // d) for d in range(1, g + 1) if g % d == 0)
    assert tot % k == 0, (k, r, tot)
    return tot // k

def necklace_orbits(k, r):
    words = set()
    for ones in combinations(range(k), r):
        w = [0] * k
        for a in ones:
            w[a] = 1
        words.add(tuple(w))
    sizes = []
    while words:
        w = words.pop()
        orb = {w}
        x = w
        while True:
            x = (x[-1],) + x[:-1]
            if x == w:
                break
            orb.add(x)
        words -= orb
        sizes.append(len(orb))
    return sorted(sizes)

def main(nmax, defn_max):
    for n in range(1, nmax + 1):
        k = rank(n)
        r = n - T(k - 1)
        assert 1 <= r <= k
        P = list(parts_of(n))
        Pset = set(P)
        assert len(Pset) == len(P) == pcount(n)
        for lam in P:
            assert sum(lam) == n and all(lam[i] >= lam[i + 1] for i in range(len(lam) - 1)) and lam[-1] >= 1
        Bm = {lam: B(lam) for lam in P}
        for lam in P:
            nu = Bm[lam]
            assert nu in Pset
            s = len(lam)
            mu = (s,) + tuple(p - 1 for p in lam)
            assert E(mu) == E(lam)                      # Lemma 1
            assert E(nu) <= E(lam)                      # Lemma 3(a)
            if E(nu) == E(lam):
                assert s >= lam[0] - 1                  # Lemma 3(b)
            if s >= lam[0] - 1:
                # Lemma 3(c): nu is mu with zeros deleted, zeros at end
                z = [i for i, v in enumerate(mu) if v == 0]
                assert all(i >= len(mu) - len(z) for i in z)
                assert nu == tuple(v for v in mu if v > 0)
                assert Y(nu) == frozenset(tau(c) for c in Y(lam))   # Lemma 4
            else:
                assert E(nu) < E(lam)                   # strictness (Lemma 2 consequence)
        # cyclic set by Kahn peeling
        indeg = {lam: 0 for lam in P}
        for lam in P:
            indeg[Bm[lam]] += 1
        stack = [lam for lam in P if indeg[lam] == 0]
        alive = set(P)
        while stack:
            x = stack.pop()
            alive.discard(x)
            y = Bm[x]
            indeg[y] -= 1
            if indeg[y] == 0:
                stack.append(y)
        cyc = alive
        if n <= defn_max:
            M = len(P)
            lit = set()
            for lam in P:
                x = lam
                for i in range(1, M + 1):
                    x = Bm[x]
                    if x == lam:
                        lit.add(lam)
                        break
            assert lit == cyc, n
        C = claimed_set(k, r)
        assert len(C) == comb(k, r)
        assert cyc == C, (n, sorted(cyc), sorted(C))
        # Lemma 6(b) and Cor 8 shape on cyclic partitions
        for lam in cyc:
            assert len(lam) >= lam[0] - 1
            Yl = Y(lam)
            diag = {}
            for (a, b) in Yl:
                diag[a + b] = diag.get(a + b, 0) + 1
            e = 0
            while diag.get(e, 0) == e + 1:
                e += 1
            assert all(d <= e for d in diag)
            assert n == T(e) + diag.get(e, 0)
        # cycles
        left = set(cyc)
        lens = []
        while left:
            x = left.pop()
            L = 1
            y = Bm[x]
            while y != x:
                assert y in left
                left.discard(y)
                y = Bm[y]
                L += 1
            lens.append(L)
        lens.sort()
        nf = N_formula(k, r)
        orb = necklace_orbits(k, r)
        assert len(lens) == nf == len(orb), (n, len(lens), nf, len(orb))
        assert lens == orb, (n, lens, orb)
        # Thm 9(d)
        for ones in combinations(range(k), r):
            eps = [0] * k
            for a in ones:
                eps[a] = 1
            eps = tuple(eps)
            rho = (eps[-1],) + eps[:-1]
            assert Bm[lam_of(eps)] == lam_of(rho)
        # (i)
        if r == k:
            delta = tuple(range(k, 0, -1))
            assert cyc == {delta}
            M = len(P)
            for lam in P:
                x = lam
                ok = (x == delta)
                i = 0
                while not ok and i <= M:
                    x = Bm[x]
                    i += 1
                    ok = (x == delta)
                assert ok, lam
        print(f"n={n} k={k} r={r} |P|={len(P)} cyclic={len(cyc)} cycles={len(lens)} formula={nf} lengths={lens} OK")
    # statement's example
    assert B((2, 1, 1, 1, 1)) == (5, 1) and B((5, 1)) == (4, 2) and B((4, 2)) == (3, 2, 1) and B((3, 2, 1)) == (3, 2, 1)
    # Lemma 2 random test (sorting lowers E, strictly if unsorted)
    rng = random.Random(12345)
    for _ in range(20000):
        m = rng.randint(1, 9)
        x = [rng.randint(0, 7) for _ in range(m)]
        xs = sorted(x, reverse=True)
        assert E(xs) <= E(x)
        if xs != x:
            assert E(xs) < E(x)
    # formula vs brute-force necklace counts for larger k (pure combinatorics, step 6)
    for k in range(1, 17):
        for r in range(1, k + 1):
            assert N_formula(k, r) == len(necklace_orbits(k, r)), (k, r)
    print("ALL OK up to n =", nmax, "; literal-definition cyclic check up to n =", defn_max,
          "; necklace formula vs brute force for 1<=r<=k<=16 OK; Lemma 2 random 20000 OK")

if __name__ == "__main__":
    nmax = int(sys.argv[1]) if len(sys.argv) > 1 else 40
    dm = int(sys.argv[2]) if len(sys.argv) > 2 else 25
    main(nmax, dm)
