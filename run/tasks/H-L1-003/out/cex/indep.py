#!/usr/bin/env python3
"""Referee's independent checks for H-L1 (stdlib only, exact integers).
T1  Q_3: all 8! labellings, count by explicit enumeration of uphill SEQUENCES (BFS over
    partial paths, no recurrence); min P, and #labellings with P = 13 = |E|+1 (must be 0).
T2  ALL (graph, labelling) pairs on n <= NMAXG vertices: WLOG labelling = identity and graph
    ranges over all 2^C(n,2) labelled graphs (every pair (G,f) is isomorphic to exactly such a
    pair via relabelling v -> f(v)).  Checks Step 5 identity, Step 6 bound P >= |E|+|Val|,
    Step 7: if no isolated vertex and P = |E|+1, then |Val|=1, down(v)=1 on R, and
    |E| = n-1-m + sum_{M} deg.  Also records whether any P=|E|+1 case exists at all.
T3  Step 8: k does not divide 2^k - 1 for 2 <= k <= KMAX (finite, sanity only).
T4  Step 10 algebra: for d = 3..DMAX, the unique rational m solving (**) is non-integral,
    and the identity 2^(d-1)-1 = (d-1)(2^(d-1)-m) holds for the rational m (Fraction).
T5  Local search (swap hill-climb with restarts) on Q_4 and Q_5 minimising P; reports the
    least P found and whether any labelling with P <= |E|+1 was ever seen.
"""
import itertools, random, sys, time
from fractions import Fraction

def cube(d):
    return [[v ^ (1 << i) for i in range(d)] for v in range(1 << d)]

def P_enum(adj, lab):
    """Enumerate uphill sequences explicitly (stack of partial paths)."""
    n = len(adj)
    cnt = 0
    stack = [(v,) for v in range(n) if all(lab[w] > lab[v] for w in adj[v])]
    while stack:
        p = stack.pop()
        cnt += 1
        last = p[-1]
        for w in adj[last]:
            if lab[w] > lab[last]:
                stack.append(p + (w,))
    return cnt

def P_rec(adj, lab):
    n = len(adj)
    order = sorted(range(n), key=lambda v: lab[v])
    N = [0] * n
    for v in order:
        low = [w for w in adj[v] if lab[w] < lab[v]]
        N[v] = (0 if low else 1) + sum(N[w] for w in low)
    return sum(N), N

def T1():
    adj = cube(3); E = 12
    hist = {}
    for perm in itertools.permutations(range(1, 9)):
        P = P_enum(adj, perm)
        hist[P] = hist.get(P, 0) + 1
    return min(hist), hist.get(E + 1, 0), sum(hist.values()), sorted(hist.items())

def T2(nmax):
    out = []
    for n in range(1, nmax + 1):
        pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
        lab = list(range(n))  # identity labelling (labels 0..n-1, order is all that matters)
        n_eq = 0; n_graphs = 0; n_noiso_eq = 0
        for mask in range(1 << len(pairs)):
            adj = [[] for _ in range(n)]
            E = 0
            for b, (i, j) in enumerate(pairs):
                if mask >> b & 1:
                    adj[i].append(j); adj[j].append(i); E += 1
            n_graphs += 1
            # identity labelling: lower neighbours of v are those w < v
            N = [0] * n; up = [0] * n; down = [0] * n
            for v in range(n):
                low = [w for w in adj[v] if w < v]
                down[v] = len(low); up[v] = len(adj[v]) - len(low)
                N[v] = (0 if low else 1) + sum(N[w] for w in low)
            P = sum(N)
            Val = [v for v in range(n) if down[v] == 0]
            assert sum(up) == E == sum(down)
            assert P == len(Val) + sum(N[v] * up[v] for v in range(n)), (n, mask)
            assert all(x >= 1 for x in N)
            assert P >= E + len(Val) >= E + 1
            if n <= 5:
                assert P == P_enum(adj, lab)
            if P == E + 1:
                n_eq += 1
                if all(adj[v] for v in range(n)):
                    n_noiso_eq += 1
                    assert len(Val) == 1
                    v0 = Val[0]
                    M = [v for v in range(n) if up[v] == 0]
                    assert v0 not in M
                    for v in range(n):
                        if v != v0 and v not in M:
                            assert down[v] == 1 and N[v] == 1
                    assert E == n - 1 - len(M) + sum(len(adj[v]) for v in M)
        out.append((n, n_graphs, n_eq, n_noiso_eq))
    return out

def T3(kmax):
    for k in range(2, kmax + 1):
        if pow(2, k, k) == 1 % k:
            return k
    return None

def T4(dmax):
    for d in range(3, dmax + 1):
        rhs = 2 ** (d - 1) * (d - 2) + 1
        m = Fraction(rhs, d - 1)
        assert m.denominator != 1, d
        assert 2 ** (d - 1) - 1 == (d - 1) * (2 ** (d - 1) - m)
        assert d * 2 ** (d - 1) == (2 ** d - 1 - m) + m * d
    # d = 2 sanity: m = 1 is integral (Remark 2)
    assert Fraction(2 ** 1 * 0 + 1, 1) == 1
    return True

def T5(d, restarts, iters, seed):
    rng = random.Random(seed)
    adj = cube(d); n = 1 << d; E = d * 2 ** (d - 1)
    best = None; seen_le = False
    for _ in range(restarts):
        lab = list(range(1, n + 1)); rng.shuffle(lab)
        cur = P_rec(adj, lab)[0]
        for _ in range(iters):
            a, b = rng.randrange(n), rng.randrange(n)
            lab[a], lab[b] = lab[b], lab[a]
            new = P_rec(adj, lab)[0]
            if new <= cur:
                cur = new
            else:
                lab[a], lab[b] = lab[b], lab[a]
            if cur <= E + 1:
                seen_le = True
        best = cur if best is None else min(best, cur)
    return E + 2, best, seen_le

if __name__ == "__main__":
    t0 = time.time()
    mn, n13, tot, hist = T1()
    print("T1 Q_3 all %d labellings: min P = %d, #P=13 = %d" % (tot, mn, n13), hist, "%.2fs" % (time.time() - t0))
    t0 = time.time()
    NMAXG = int(sys.argv[1]) if len(sys.argv) > 1 else 7
    print("T2 all graphs n<=%d (n, #graphs, #P=|E|+1, #of those w/o isolated vtx):" % NMAXG, T2(NMAXG), "%.2fs" % (time.time() - t0))
    t0 = time.time()
    print("T3 first k in [2,10^6] with k | 2^k-1:", T3(10 ** 6), "%.2fs" % (time.time() - t0))
    t0 = time.time()
    print("T4 Step-10 algebra d=3..3000 OK:", T4(3000), "%.2fs" % (time.time() - t0))
    t0 = time.time()
    print("T5 Q_4 local search (|E|+2, best P, any P<=|E|+1 seen):", T5(4, 40, 3000, 1), "%.2fs" % (time.time() - t0))
    t0 = time.time()
    print("T5 Q_5 local search (|E|+2, best P, any P<=|E|+1 seen):", T5(5, 10, 4000, 2), "%.2fs" % (time.time() - t0))
