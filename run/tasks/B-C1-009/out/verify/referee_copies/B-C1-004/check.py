"""Independent referee check for B-C1 (stdlib only, exact integer arithmetic).
Usage: python3 check.py NMAX KMAX_EPS KMAX_NECK NMAX_LOCAL NMAX_COMP
 A. exhaustive n<=NMAX: cyclic set (functional-graph colouring, independent of subject code)
    == {lambda(eps)}; #cycles == N(k,r) formula AND == #rotation-orbits computed directly
    (canonical min rotation); triangular n: every partition reaches delta_k; Lemma 6 on
    every cyclic partition; C(B^t lam) = R^t(C(lam)) along each cycle.
 B. n<=NMAX_LOCAL, every partition: R is a bijection C(lam)->C(U(lam)); E(U)=E(lam);
    E(B lam)<=E(lam), equality iff U(lam) weakly decreasing, then C(B lam)=R(C(lam)).
 C. Lemma 3 on every composition of n<=NMAX_COMP.
 D. B(lambda(eps)) == lambda(rho eps) for every k<=KMAX_EPS and every eps in {0,1}^k, sum>=1.
 E. N(k,r) formula == direct orbit count of rotation on W(k,r), k<=KMAX_NECK.
 F. statement example (S6)."""
import sys
from math import comb, gcd

def partitions(n, maxpart=None):
    if maxpart is None: maxpart = n
    if n == 0:
        yield (); return
    for p in range(min(n, maxpart), 0, -1):
        for rest in partitions(n - p, p):
            yield (p,) + rest

def U(lam):
    s = len(lam)
    return (s,) + tuple(x - 1 for x in lam if x >= 2)

def B(lam):
    return tuple(sorted(U(lam), reverse=True))

def cells(c):
    return {(j + 1, h) for j, cj in enumerate(c) for h in range(1, cj + 1)}

def E(c):
    return sum(j + h - 1 for (j, h) in cells(c))

def Rc(x):
    j, h = x
    return (j + 1, h - 1) if h >= 2 else (1, j)

def isdec(c):
    return all(c[i] >= c[i + 1] for i in range(len(c) - 1))

def rank(n):
    k = 1
    while k * (k + 1) // 2 < n: k += 1
    return k

def lam_eps(eps):
    k = len(eps)
    return tuple(v for v in (k - (j + 1) + eps[j] for j in range(k)) if v > 0)

def rho(eps):
    return (eps[-1],) + tuple(eps[:-1])

def phi(m):
    return sum(1 for i in range(1, m + 1) if gcd(i, m) == 1)

def Nformula(k, r):
    g = gcd(k, r)
    num = sum(phi(d) * comb(k // d, r // d) for d in range(1, g + 1) if g % d == 0)
    assert num % k == 0
    return num // k

def W(k, r):
    out = []
    for m in range(1 << k):
        e = tuple((m >> j) & 1 for j in range(k))
        if sum(e) == r: out.append(e)
    return out

def orbits_direct(k, r):
    canon = set()
    for e in W(k, r):
        rots = [e[i:] + e[:i] for i in range(k)]
        canon.add(min(rots))
    return len(canon)

def partA(NMAX):
    tot = 0
    for n in range(1, NMAX + 1):
        k = rank(n); r = n - k * (k - 1) // 2
        assert 1 <= r <= k
        P = list(partitions(n)); tot += len(P)
        nxt = {p: B(p) for p in P}
        assert all(q in nxt for q in nxt.values())  # B maps P(n) into P(n)
        # functional graph colouring: 0 unvisited, 1 on stack, 2 done
        state = {p: 0 for p in P}; cyc = set(); cycles = []
        for p in P:
            if state[p]: continue
            path = []; x = p
            while state[x] == 0:
                state[x] = 1; path.append(x); x = nxt[x]
            if state[x] == 1:  # new cycle found
                i = path.index(x); c = path[i:]; cycles.append(c); cyc.update(c)
            for y in path: state[y] = 2
        pred = {lam_eps(e) for e in W(k, r)}
        assert cyc == pred, ("cyclic set", n)
        assert len(pred) == comb(k, r)
        assert len(cycles) == Nformula(k, r) == orbits_direct(k, r), ("cycles", n)
        # cycles are disjoint as sets
        assert sum(len(c) for c in cycles) == len(cyc)
        # Lemma 6 and rotation law on cyclic partitions
        for lam in cyc:
            C = cells(lam)
            dmax = max(j + h - 1 for (j, h) in C)
            for d in range(1, dmax + 2):
                Dd = {(j, d + 1 - j) for j in range(1, d + 1)}
                Dd1 = {(j, d + 2 - j) for j in range(1, d + 2)}
                if not Dd <= C: assert not (Dd1 & C), ("Lemma6", lam, d)
            x = lam; Cx = C
            for t in range(len(lam) + k + 2):
                x = nxt[x]; Cx = {Rc(c) for c in Cx}
                assert cells(x) == Cx, ("rotation law", lam, t)
        if r == k:
            delta = tuple(range(k, 0, -1))
            assert cyc == {delta}
            reach = {delta}
            # every partition reaches delta: since delta is the only cyclic node and the
            # graph is functional + finite, check explicitly by iteration with memo
            for p in P:
                path = []; x = p
                while x not in reach:
                    path.append(x); x = nxt[x]
                    assert len(path) <= len(P) + 1
                reach.update(path)
            assert reach == set(P)
        print(f"A n={n} k={k} r={r} p(n)={len(P)} cyclic={len(cyc)} cycles={len(cycles)} OK")
    print("A done, total partitions", tot)

def partB(NMAX):
    cnt = 0; eqc = 0
    for n in range(1, NMAX + 1):
        for lam in partitions(n):
            u = U(lam); C = cells(lam); Cu = cells(u)
            img = {Rc(x) for x in C}
            assert len(img) == len(C) and img == Cu, ("R bijection", lam)
            assert E(u) == E(lam)
            b = B(lam)
            assert E(b) <= E(lam)
            if E(b) == E(lam):
                eqc += 1
                assert isdec(u) and cells(b) == img
            else:
                assert not isdec(u)
            cnt += 1
    print("B done: partitions checked", cnt, "equality cases", eqc)

def compositions(n):
    if n == 0:
        yield (); return
    for f in range(1, n + 1):
        for rest in compositions(n - f):
            yield (f,) + rest

def partC(NMAX):
    cnt = 0
    for n in range(1, NMAX + 1):
        for c in compositions(n):
            s = tuple(sorted(c, reverse=True))
            assert E(s) <= E(c)
            assert (E(s) == E(c)) == isdec(c)
            cnt += 1
    print("C done: compositions checked", cnt)

def partD(KMAX):
    cnt = 0
    for k in range(1, KMAX + 1):
        for m in range(1, 1 << k):
            e = tuple((m >> j) & 1 for j in range(k))
            assert B(lam_eps(e)) == lam_eps(rho(e)), (k, e)
            cnt += 1
    print("D done: eps checked", cnt)

def partE(KMAX):
    for k in range(1, KMAX + 1):
        for r in range(1, k + 1):
            assert Nformula(k, r) == orbits_direct(k, r), (k, r)
    print("E done: k<=", KMAX)

def partF():
    assert B((2, 1, 1, 1, 1)) == (5, 1)
    assert B((5, 1)) == (4, 2)
    assert B((4, 2)) == (3, 2, 1)
    assert B((3, 2, 1)) == (3, 2, 1)
    assert B((1,)) == (1,)
    print("F done")

if __name__ == "__main__":
    a = [int(x) for x in sys.argv[1:]]
    NMAX, KE, KN, NL, NC = (a + [40, 14, 16, 30, 13])[:5]
    partF(); partC(NC); partD(KE); partE(KN); partB(NL); partA(NMAX)
    print("ALL CHECKS PASSED")
