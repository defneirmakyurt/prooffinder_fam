#!/usr/bin/env python3
"""
quotients.py -- translation-invariant induced forests of Q_9 via covering quotients.
Stdlib only, exact integer arithmetic.

A binary linear code C <= F_2^9 of dimension r is given by 9 "columns" col_0..col_8 in F_2^r
(the generator matrix G has these columns; C = row space of G, i.e. C = { (u.col_j)_j : u in F_2^r }).
Up to coordinate permutation (S_9) and change of basis of C (GL(r,2)), a code is the multiset of
its columns up to GL(r,2).  Conditions used:
  * rank r (columns span F_2^r)  -> dim C = r;
  * no codeword of weight 1      -> for every u != 0, #{j : u.col_j = 1} != 1.
The quotient multigraph Q_9/C: vertex set F_2^9 / C, identified with F_2^(9-r) via x -> Hx where the
rows of H form a basis of the dual code C^perp; coordinate direction i gives the generator h_i = H e_i.
Vertex y is joined to y ^ h_i for each i (parallel edges when h_i = h_j for i != j).
"""
import itertools


def popcount(x):
    return bin(x).count("1")


def dot(u, c):
    return popcount(u & c) & 1


def gl_perms(r):
    """All invertible r x r matrices over F_2, as permutations of F_2^r (ints 0..2^r-1)."""
    n = 1 << r
    perms = []
    for cols in itertools.product(range(1, n), repeat=r):
        # matrix with columns cols[0..r-1]: image of basis vector e_k is cols[k]
        img = [0] * n
        for x in range(n):
            y = 0
            for k in range(r):
                if (x >> k) & 1:
                    y ^= cols[k]
            img[x] = y
        if len(set(img)) == n:
            perms.append(tuple(img))
    return perms


def compositions(total, parts):
    if parts == 1:
        yield (total,)
        return
    for first in range(total, -1, -1):
        for rest in compositions(total - first, parts - 1):
            yield (first,) + rest


def code_classes(r, d=9):
    """Return list of canonical count vectors (length 2^r, sum d) of codes of dim r with no
    weight-1 word, one per class up to S_d x GL(r,2)."""
    n = 1 << r
    G = gl_perms(r)
    seen = set()
    out = []
    for cnt in compositions(d, n):
        # canonical form: lexicographically largest image under GL
        best = max(tuple(cnt[g_inv] for g_inv in _inv_apply(g, n)) for g in G)
        if best in seen:
            continue
        seen.add(best)
        cols = [c for c in range(n) for _ in range(best[c])]
        # rank r?
        if rank_f2(cols) != r:
            continue
        ok = True
        for u in range(1, n):
            w = sum(dot(u, c) for c in cols)
            if w == 1:
                ok = False
                break
        if ok:
            out.append(best)
    return out


def _inv_apply(g, n):
    """g is a permutation of F_2^r; the image count vector cnt' with cnt'[g[x]] = cnt[x], so
    cnt'[y] = cnt[g^{-1}[y]]; return g^{-1} as a list."""
    inv = [0] * n
    for x in range(n):
        inv[g[x]] = x
    return inv


def rank_f2(vecs):
    basis = []
    for v in vecs:
        for b in basis:
            v = min(v, v ^ b)
        if v:
            basis.append(v)
    return len(basis)


def codewords_from_counts(cnt, r):
    cols = [c for c in range(1 << r) for _ in range(cnt[c])]
    words = []
    for u in range(1 << r):
        w = 0
        for j, c in enumerate(cols):
            if dot(u, c):
                w |= 1 << j
        words.append(w)
    return sorted(set(words))


def dual_basis(words, d=9):
    """Basis (list of ints) of C^perp = {y : popcount(y & c) even for all c in C}."""
    return [y for y in _span_basis([y for y in range(1 << d) if all(dot(y, c) == 0 for c in words)])]


def _span_basis(vecs):
    basis = []
    for v in vecs:
        w = v
        for b in basis:
            w = min(w, w ^ b)
        if w:
            basis.append(w)
            basis.sort(reverse=True)
    return basis


def quotient(words, d=9):
    """Return (k, H, gens, proj): k = 9 - r, H = list of k dual-basis rows,
    gens[i] = H e_i as a k-bit int, proj(x) = Hx."""
    H = dual_basis(words, d)
    k = len(H)

    def proj(x):
        y = 0
        for t, h in enumerate(H):
            if dot(h, x):
                y |= 1 << t
        return y
    gens = [proj(1 << i) for i in range(d)]
    return k, H, gens, proj


def quotient_graph(gens, k):
    """Adjacency: nbr[y] = list of y ^ g (with multiplicity), vertex set 0..2^k-1."""
    n = 1 << k
    return [[y ^ g for g in gens] for y in range(n)]


def is_forest_multi(F, nbr):
    """F: set of vertices of the quotient multigraph. True iff the induced sub-multigraph has no
    loop, no parallel pair and no cycle (union-find over edge multiset)."""
    parent = {v: v for v in F}

    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a
    for y in F:
        for z in nbr[y]:                   # each edge seen twice (from y and from z); use y < z
            if z == y:
                return False               # loop
            if z in F and y < z:
                a, b = find(y), find(z)
                if a == b:
                    return False           # cycle or parallel edge
                parent[a] = b
    return True


def lift(F, proj, d=9):
    return [x for x in range(1 << d) if proj(x) in F]


def is_forest_qd(T, d=9):
    """Direct check that T (iterable of ints) induces an acyclic subgraph of Q_d."""
    Ts = set(T)
    parent = {v: v for v in Ts}

    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a
    for v in Ts:
        for i in range(d):
            w = v ^ (1 << i)
            if w in Ts and v < w:
                a, b = find(v), find(w)
                if a == b:
                    return False
                parent[a] = b
    return True


if __name__ == "__main__":
    for r in (1, 2, 3):
        cl = code_classes(r)
        print("r=%d: %d classes" % (r, len(cl)))
        for cnt in cl:
            words = codewords_from_counts(cnt, r)
            wts = sorted(popcount(w) for w in words)
            k, H, gens, proj = quotient(words)
            print("   counts=%s  weights=%s  distinct_gens=%d" % (cnt, wts, len(set(gens))))
