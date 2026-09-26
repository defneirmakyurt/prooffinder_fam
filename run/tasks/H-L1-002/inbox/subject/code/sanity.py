#!/usr/bin/env python3
"""Sanity checks for out/proof.md (H-L1).  Stdlib only, exact integer arithmetic.
NONE of these checks is used as a step of the proof; the proof is computation-free.

 A. n does not divide 2^n - 1 for 2 <= n <= NMAX            (Lemma 8, finite range only)
 B. (d-1) does not divide 2^(d-1)(d-2)+1 for 3 <= d <= DMAX   (Step 9, finite range only)
 C. Q_3: all 8! labellings. For each: P by explicit DFS enumeration of uphill paths,
    P by the recurrence (Lemma 3), identity P = |Val| + sum N*up (Lemma 5); min P.
 D. Q_1, Q_2 (where P = |E|+1 IS attainable) and a few small non-regular graphs: for every
    labelling with P = |E|+1, check the Lemma 7 count |E| = n-1-m + sum_{up=0} deg.
 E. Random labellings of Q_d, d = 3..8 (fixed seed): recurrence count >= d*2^(d-1)+2,
    and for d <= 5 the DFS count agrees with the recurrence.
"""
import itertools, random, sys

def cube(d):
    n = 1 << d
    return n, [[v ^ (1 << i) for i in range(d)] for v in range(n)]

def count_rec(adj, lab):
    """lab[v] = label of v (a permutation of 1..n). Returns (P, N, up, down, valleys)."""
    n = len(adj)
    order = sorted(range(n), key=lambda v: lab[v])
    N = [0] * n
    up = [0] * n
    down = [0] * n
    for v in order:
        lower = [w for w in adj[v] if lab[w] < lab[v]]
        down[v] = len(lower)
        up[v] = len(adj[v]) - len(lower)
        N[v] = (1 if not lower else 0) + sum(N[w] for w in lower)
    val = [v for v in range(n) if down[v] == 0]
    return sum(N), N, up, down, val

def count_dfs(adj, lab):
    n = len(adj)
    total = 0
    def ext(v):
        c = 1
        for w in adj[v]:
            if lab[w] > lab[v]:
                c += ext(w)
        return c
    for v in range(n):
        if all(lab[w] > lab[v] for w in adj[v]):
            total += ext(v)
    return total

def edges(adj):
    return sum(len(a) for a in adj) // 2

def check_A(NMAX):
    for n in range(2, NMAX + 1):
        assert pow(2, n, n) != 1 % n, n
    return True

def check_B(DMAX):
    for d in range(3, DMAX + 1):
        assert (2 ** (d - 1) * (d - 2) + 1) % (d - 1) != 0, d
    return True

def check_C():
    n, adj = cube(3)
    E = edges(adj)
    best = None
    hist = {}
    for perm in itertools.permutations(range(1, n + 1)):
        lab = list(perm)
        P, N, up, down, val = count_rec(adj, lab)
        assert P == count_dfs(adj, lab)
        assert P == len(val) + sum(N[v] * up[v] for v in range(n))
        assert sum(up) == E == sum(down)
        assert P >= E + len(val)
        hist[P] = hist.get(P, 0) + 1
        best = P if best is None else min(best, P)
    return best, sorted(hist.items())

def check_D_graph(adj, name):
    n = len(adj)
    E = edges(adj)
    eq = 0
    for perm in itertools.permutations(range(1, n + 1)):
        lab = list(perm)
        P, N, up, down, val = count_rec(adj, lab)
        assert P == count_dfs(adj, lab)
        assert P >= E + 1
        if P == E + 1:
            eq += 1
            M = [v for v in range(n) if up[v] == 0]
            assert len(val) == 1
            assert E == n - 1 - len(M) + sum(len(adj[v]) for v in M), (name, lab)
    return eq

def check_E(seed, trials):
    rng = random.Random(seed)
    out = []
    for d in range(3, 9):
        n, adj = cube(d)
        E = edges(adj)
        assert E == d * 2 ** (d - 1)
        mn = None
        for _ in range(trials):
            lab = list(range(1, n + 1))
            rng.shuffle(lab)
            P = count_rec(adj, lab)[0]
            if d <= 5:
                assert P == count_dfs(adj, lab)
            assert P >= E + 2
            mn = P if mn is None else min(mn, P)
        out.append((d, E + 2, mn))
    return out

if __name__ == "__main__":
    NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 10 ** 5
    DMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 2000
    print("A: n does not divide 2^n-1 for 2..%d:" % NMAX, check_A(NMAX))
    print("B: (d-1) does not divide 2^(d-1)(d-2)+1 for d=3..%d:" % DMAX, check_B(DMAX))
    best, hist = check_C()
    print("C: Q_3 exhaustive min P =", best, "histogram", hist)
    for d in (1, 2):
        n, adj = cube(d)
        print("D: Q_%d labellings with P=|E|+1:" % d, check_D_graph(adj, "Q%d" % d))
    path4 = [[1], [0, 2], [1, 3], [2]]
    star = [[1, 2, 3, 4], [0], [0], [0], [0]]
    k4 = [[1, 2, 3], [0, 2, 3], [0, 1, 3], [0, 1, 2]]
    c5 = [[(i - 1) % 5, (i + 1) % 5] for i in range(5)]
    paw = [[1, 2, 3], [0, 2], [0, 1], [0]]
    for name, g in (("P4", path4), ("K1,4", star), ("K4", k4), ("C5", c5), ("paw", paw)):
        print("D: %s labellings with P=|E|+1:" % name, check_D_graph(g, name))
    print("E: random labellings (d, |E|+2, min P seen):", check_E(20260926, 200))

# F. The Q_3 / Q_4 labellings of inbox/earlier-proof.md Step 8 (vertices in increasing label order).
def check_F():
    res = []
    for d, lst in ((3, "000 001 010 011 101 110 100 111"),
                   (4, "1010 0111 0101 1011 1000 0010 0001 0011 1101 1110 1001 0100 0000 0110 1111 1100")):
        n, adj = cube(d)
        verts = [int(s, 2) for s in lst.split()]
        assert sorted(verts) == list(range(n))
        lab = [0] * n
        for i, v in enumerate(verts):
            lab[v] = i + 1
        P = count_rec(adj, lab)[0]
        assert P == count_dfs(adj, lab)
        res.append((d, P))
    return res

if __name__ == "__main__":
    print("F: earlier-proof witnesses (d, P):", check_F())
