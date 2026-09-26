"""Referee B-C1-003: independent exhaustive check (stdlib only, exact integers).
Usage: python3 search.py NMAX KMAX SEED
 Part A (exhaustive, every n in [1, NMAX]): enumerate all partitions, build the functional graph of B,
   find ALL cyclic partitions and ALL cycles (graph method, independent of the proof's code),
   compare with (a) the proof's lambda(eps) set and (b) the Young-diagram description
   'staircase delta_{k-1} plus r cells of D_k'; compare #cycles with N(k,r) (Burnside formula) and with
   a direct necklace count; for triangular n check every partition reaches delta_k; check 4.2 (U(lambda)
   already sorted on every cyclic lambda) and E invariance.
 Part B (every k in [1, KMAX], every eps in {0,1}^k with sum >= 1): check 8.3 B(lambda(eps)) = lambda(rho eps),
   injectivity 8.2, and N(k,r) = #necklaces by brute force; check 10.3 fixed-point counts.
 Part C (random): Lemma 3 (sorting lemma incl. strict equality case) on random sequences;
   2.1/2.2 (R bijection C(lambda) -> C(U(lambda)), weight preserved) on random partitions.
 Part D: statement example values (S6)."""
import sys, random
from math import comb, gcd

def partitions(n):
    # iterative generator of partitions of n in reverse-lex order (tuples, weakly decreasing)
    a = [n]
    while True:
        yield tuple(a)
        # find rightmost part > 1
        i = len(a) - 1
        while i >= 0 and a[i] == 1:
            i -= 1
        if i < 0:
            return
        rem = len(a) - i   # parts from i onward: a[i] and (len-1-i) ones
        v = a[i] - 1
        total = v + (len(a) - 1 - i) + 1
        a = a[:i]
        while total > 0:
            p = min(v, total)
            a.append(p)
            total -= p

def pnum(n):
    # Euler pentagonal-number recurrence, independent of the generator
    p = [1] + [0] * n
    for m in range(1, n + 1):
        t = 0; q = 1
        while True:
            g1 = q * (3 * q - 1) // 2; g2 = q * (3 * q + 1) // 2
            if g1 > m: break
            sg = 1 if q % 2 else -1
            t += sg * p[m - g1]
            if g2 <= m: t += sg * p[m - g2]
            q += 1
        p[m] = t
    return p[n]

def B(lam):
    s = len(lam)
    parts = [x - 1 for x in lam if x - 1 > 0]
    parts.append(s)
    parts.sort(reverse=True)
    return tuple(parts)

def U(lam):
    s = len(lam)
    return (s,) + tuple(x - 1 for x in lam if x >= 2)

def cells(c):
    return {(j, h) for j in range(1, len(c) + 1) for h in range(1, c[j - 1] + 1)}

def R(cell):
    j, h = cell
    return (j + 1, h - 1) if h >= 2 else (1, j)

def E(c):
    return sum(j + h - 1 for (j, h) in cells(c))

def E_formula(c):
    return sum((j) * c[j] for j in range(len(c))) + sum(x * (x + 1) // 2 for x in c)

def rank(n):
    k = 1
    while k * (k + 1) // 2 < n:
        k += 1
    return k

def lam_eps(eps):
    k = len(eps)
    return tuple(v for v in (k - j + eps[j - 1] for j in range(1, k + 1)) if v > 0)

def young_desc(k, r):
    """independent construction: all diagrams = staircase delta_{k-1} cells plus r cells of D_k."""
    out = set()
    stair = {(j, h) for j in range(1, k) for h in range(1, k - j + 1)}
    Dk = [(j, k + 1 - j) for j in range(1, k + 1)]
    for mask in range(1 << k):
        if bin(mask).count("1") != r:
            continue
        cs = set(stair) | {Dk[i] for i in range(k) if (mask >> i) & 1}
        cols = {}
        for (j, h) in cs:
            cols[j] = cols.get(j, 0) + 1
        seq = tuple(cols[j] for j in sorted(cols))
        # must be a genuine Young diagram: columns 1..m contiguous, heights = 1..len
        assert sorted(cols) == list(range(1, len(cols) + 1))
        for j in cols:
            assert {h for (jj, h) in cs if jj == j} == set(range(1, cols[j] + 1))
        if list(seq) == sorted(seq, reverse=True):
            out.add(seq)
    return out

def phi(m):
    return sum(1 for i in range(1, m + 1) if gcd(i, m) == 1)

def N_formula(k, r):
    g = gcd(k, r)
    num = sum(phi(d) * comb(k // d, r // d) for d in range(1, g + 1) if g % d == 0)
    assert num % k == 0
    return num // k

def necklaces(k, r):
    seen = set(); cnt = 0
    for mask in range(1 << k):
        if bin(mask).count("1") != r or mask in seen:
            continue
        cnt += 1
        w = mask
        for _ in range(k):
            seen.add(w)
            w = ((w << 1) | (w >> (k - 1))) & ((1 << k) - 1)
    return cnt

def rho(eps):
    return (eps[-1],) + tuple(eps[:-1])

def partA(NMAX):
    for n in range(1, NMAX + 1):
        k = rank(n); r = n - (k - 1) * k // 2
        assert 1 <= r <= k
        P = list(partitions(n))
        assert len(P) == len(set(P)) == pnum(n), (n, len(P))
        assert all(sum(p) == n and list(p) == sorted(p, reverse=True) and min(p) >= 1 for p in P)
        idx = {p: i for i, p in enumerate(P)}
        nxt = [idx[B(p)] for p in P]
        # cyclic nodes: standard colouring on functional graph
        state = [0] * len(P)   # 0 unvisited, 1 on stack, 2 done
        oncyc = [False] * len(P)
        for s0 in range(len(P)):
            if state[s0]:
                continue
            path = []; x = s0
            while state[x] == 0:
                state[x] = 1; path.append(x); x = nxt[x]
            if state[x] == 1:  # found new cycle starting at x
                y = x
                while True:
                    oncyc[y] = True; y = nxt[y]
                    if y == x: break
            for z in path: state[z] = 2
        cyc = {P[i] for i in range(len(P)) if oncyc[i]}
        # definition check: cyclic <=> B^i(lam)=lam for some 1<=i<=|P|
        for i in range(len(P)):
            # definition: cyclic iff B^j(lam)=lam for some j>=1; walk until the first repeat;
            # lam is cyclic iff the first repeated node is lam itself
            vis = {i}; x = nxt[i]
            while x not in vis:
                vis.add(x); x = nxt[x]
            assert (x == i) == oncyc[i], (n, P[i])
        pred = {lam_eps(e) for e in
                (tuple((m >> t) & 1 for t in range(k)) for m in range(1 << k)) if sum(e) == r}
        yd = young_desc(k, r)
        assert cyc == pred == yd, (n, k, r, sorted(cyc), sorted(pred))
        assert len(cyc) == comb(k, r)
        # count cycles
        left = set(i for i in range(len(P)) if oncyc[i]); ncyc = 0; lens = []
        while left:
            x = left.pop(); L = 1; y = nxt[x]
            while y != x:
                left.discard(y); y = nxt[y]; L += 1
            ncyc += 1; lens.append(L)
        assert ncyc == N_formula(k, r) == necklaces(k, r), (n, k, r, ncyc)
        # 4.2: on cyclic lambda, U(lambda) already weakly decreasing, E constant along cycle
        for lam in cyc:
            u = U(lam)
            assert list(u) == sorted(u, reverse=True), lam
            assert E(B(lam)) == E(lam)
            assert all(k % L == 0 for L in lens)
        if r == k:
            delta = tuple(range(k, 0, -1))
            assert cyc == {delta} and B(delta) == delta
            # every partition reaches delta: backward closure from delta covers all
            for i in range(len(P)):
                x = i
                for _ in range(len(P) + 1):
                    if P[x] == delta: break
                    x = nxt[x]
                assert P[x] == delta, (n, P[i])
        print(f"A n={n} k={k} r={r} p(n)={len(P)} cyclic={len(cyc)} cycles={ncyc} lens={sorted(lens)} OK", flush=True)

def partB(KMAX):
    for k in range(1, KMAX + 1):
        seen = {}
        for m in range(1 << k):
            e = tuple((m >> t) & 1 for t in range(k))
            r = sum(e)
            if r == 0:
                continue
            lam = lam_eps(e)
            assert sum(lam) == k * (k - 1) // 2 + r
            assert list(lam) == sorted(lam, reverse=True) and min(lam) >= 1
            assert B(lam) == lam_eps(rho(e)), (k, e)
            assert lam not in seen; seen[lam] = e
        for r in range(1, k + 1):
            assert N_formula(k, r) == necklaces(k, r), (k, r)
            # 10.3 fixed point count of rho^j on W(k,r)
            W = [tuple((m >> t) & 1 for t in range(k)) for m in range(1 << k) if bin(m).count("1") == r]
            for j in range(k):
                fix = 0
                for e in W:
                    f = e
                    for _ in range(j): f = rho(f)
                    fix += (f == e)
                g = gcd(j, k)
                pred = comb(g, r * g // k) if r % (k // g) == 0 else 0
                assert fix == pred, (k, r, j, fix, pred)
        print(f"B k={k}: 8.2, 8.3, 10.3, N(k,r)=necklaces for all r OK", flush=True)

def partC(seed, trials):
    rnd = random.Random(seed)
    for _ in range(trials):
        m = rnd.randint(1, 9)
        c = tuple(rnd.randint(1, 8) for _ in range(m))
        lam = tuple(sorted(c, reverse=True))
        assert E(c) == E_formula(c)
        if c == lam:
            assert E(c) == E(lam)
        else:
            assert E(lam) < E(c), (c, lam)
    for _ in range(trials):
        n = rnd.randint(1, 40)
        # random partition via random composition sorted
        parts = []; rest = n
        while rest > 0:
            p = rnd.randint(1, rest); parts.append(p); rest -= p
        lam = tuple(sorted(parts, reverse=True))
        C = cells(lam); CU = cells(U(lam))
        img = {R(x) for x in C}
        assert len(img) == len(C) and img == CU, lam
        assert E(U(lam)) == E(lam)
        assert E(B(lam)) <= E(lam)
        assert (E(B(lam)) == E(lam)) == (list(U(lam)) == sorted(U(lam), reverse=True))
    print(f"C seed={seed} trials={trials}: Lemma 3 (strict), 2.1, 2.2, 4.1 OK", flush=True)

def partD():
    assert B((2, 1, 1, 1, 1)) == (5, 1)
    assert B((5, 1)) == (4, 2)
    assert B((4, 2)) == (3, 2, 1)
    assert B((3, 2, 1)) == (3, 2, 1)
    print("D statement example values OK", flush=True)

if __name__ == "__main__":
    NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 40
    KMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 12
    SEED = int(sys.argv[3]) if len(sys.argv) > 3 else 1
    partD()
    partC(SEED, 20000)
    partB(KMAX)
    partA(NMAX)
    print(f"ALL OK NMAX={NMAX} KMAX={KMAX} SEED={SEED}")
