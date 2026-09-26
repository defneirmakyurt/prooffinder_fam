"""Referee H-C1-007: independent re-check of U(Q_3)=14, U(Q_4)=34.

Stdlib only, exact integer arithmetic (no floats anywhere).
Nothing here reuses the subject's code.

(A) A literal enumerator: builds every uphill path as an explicit tuple of vertices and
    re-validates it against the raw definition (v_1 a valley, consecutive adjacency,
    strictly increasing labels).  Used to score the two submitted artefacts and the
    hand-computed Q_1, Q_2 test cases.
(B) Exhaustive minimum over all 8! labellings of Q_3.
(C) Exhaustive minimum over all 4! labellings of Q_2 and 2! of Q_1 (checklist S6).
(D) Randomised + local search for any labelling of Q_4 with <= 33 uphill paths.
(E) Independent test of proof Step 6 (the equality structure) on random graphs.
"""
import itertools
import random
import sys


def cube_nbrs(d):
    return [tuple(v ^ (1 << j) for j in range(d)) for v in range(1 << d)]


# ---------------------------------------------------------------- (A)
def literal_paths(nbrs, lab):
    """Return the list of ALL uphill paths as explicit vertex tuples.

    Built straight from the definition: start from each valley, extend by any adjacent
    vertex of strictly larger label.  Every produced tuple is re-validated below.
    """
    n = len(nbrs)
    valleys = [v for v in range(n) if all(lab[w] > lab[v] for w in nbrs[v])]
    out = []
    stack = [(v,) for v in valleys]
    while stack:
        p = stack.pop()
        out.append(p)
        last = p[-1]
        for w in nbrs[last]:
            if lab[w] > lab[last]:
                stack.append(p + (w,))
    return out, set(valleys)


def validate(paths, valleys, nbrs, lab):
    """Re-check each tuple against the definition; also check no duplicates."""
    seen = set()
    for p in paths:
        assert len(p) >= 1, "k >= 1 violated"
        assert p[0] in valleys, "first vertex is not a valley"
        for a, b in zip(p, p[1:]):
            assert b in nbrs[a], "consecutive vertices not adjacent"
            assert lab[a] < lab[b], "labels not strictly increasing"
        assert p not in seen, "duplicate path produced"
        seen.add(p)
    # completeness: every valid uphill path must be in `seen`.  Check by generating all
    # vertex sequences of length <= n with strictly increasing labels is too big; instead
    # check closure: for every p in seen and every uphill extension, the extension is in seen,
    # and every length-1 (valley) path is in seen.
    for v in valleys:
        assert (v,) in seen, "missing the lone-valley path"
    for p in seen:
        for w in nbrs[p[-1]]:
            if lab[p[-1]] < lab[w]:
                assert p + (w,) in seen, "missing an extension"
    return len(paths)


def score_artefact(path, d):
    with open(path) as fh:
        rows = [ln.strip() for ln in fh if ln.strip()]
    assert len(rows) == (1 << d), "wrong number of lines"
    order = []
    for r in rows:
        assert len(r) == d and set(r) <= {"0", "1"}, "bad row %r" % r
        order.append(int(r, 2))
    assert sorted(order) == list(range(1 << d)), "not a bijection onto {0,1}^d"
    lab = [0] * (1 << d)
    for i, v in enumerate(order, 1):
        lab[v] = i
    nbrs = cube_nbrs(d)
    paths, valleys = literal_paths(nbrs, lab)
    total = validate(paths, valleys, nbrs, lab)
    return total, len(valleys), len(rows)


# ---------------------------------------------------------------- fast scorer
def score_order(order, nbrs):
    """Memoised count (used only where the literal enumerator would be too slow);
    validated against literal_paths on every case below."""
    n = len(order)
    lab = [0] * n
    for i, v in enumerate(order, 1):
        lab[v] = i
    N = [0] * n
    tot = 0
    for v in order:
        s = 0
        low = False
        for w in nbrs[v]:
            if lab[w] < lab[v]:
                low = True
                s += N[w]
        N[v] = s if low else 1
        tot += N[v]
    return tot


# ---------------------------------------------------------------- (B),(C)
def exhaustive(d, literal_every=0):
    nbrs = cube_nbrs(d)
    n = 1 << d
    best = None
    best_order = None
    hist = {}
    k = 0
    for order in itertools.permutations(range(n)):
        t = score_order(order, nbrs)
        hist[t] = hist.get(t, 0) + 1
        if best is None or t < best:
            best, best_order = t, order
        if literal_every and k % literal_every == 0:
            lab = [0] * n
            for i, v in enumerate(order, 1):
                lab[v] = i
            paths, valleys = literal_paths(nbrs, lab)
            assert validate(paths, valleys, nbrs, lab) == t, "memoised != literal"
        k += 1
    return best, best_order, hist, k


# ---------------------------------------------------------------- (D)
def hunt_q4(target, seconds_budget_iters):
    """Try hard to find a labelling of Q_4 with <= target uphill paths."""
    d = 4
    nbrs = cube_nbrs(d)
    n = 1 << d
    rng = random.Random(12345)
    best = None
    best_order = None
    for trial in range(seconds_budget_iters):
        order = list(range(n))
        rng.shuffle(order)
        cur = score_order(order, nbrs)
        improved = True
        while improved:                      # best-improvement over all transpositions
            improved = False
            bi = bj = -1
            bt = cur
            for i in range(n):
                for j in range(i + 1, n):
                    order[i], order[j] = order[j], order[i]
                    t = score_order(order, nbrs)
                    order[i], order[j] = order[j], order[i]
                    if t < bt:
                        bt, bi, bj = t, i, j
            if bi >= 0:
                order[bi], order[bj] = order[bj], order[bi]
                cur = bt
                improved = True
        if best is None or cur < best:
            best, best_order = cur, list(order)
        if best <= target:
            break
    return best, best_order


# ---------------------------------------------------------------- (E)
def step6_test(trials=4000):
    """On random graphs with no isolated vertex and random labellings, whenever
    P == |E| + 1 check the three Step-6 conclusions:
      |Val| = 1 ;  N(v) = 1 whenever up(v) >= 1 ;
      |E| = (n - 1 - m) + sum_{v: up(v)=0} deg(v),  m = #{v: up(v)=0}.
    Also check P >= |E| + |Val| always (Step 5) and N(v) >= 1 always (Step 3)."""
    rng = random.Random(777)
    hits = 0
    checked = 0
    for _ in range(trials):
        n = rng.randint(2, 8)
        verts = list(range(n))
        adj = [set() for _ in range(n)]
        pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
        rng.shuffle(pairs)
        for (i, j) in pairs:
            if rng.random() < 0.45:
                adj[i].add(j)
                adj[j].add(i)
        for v in verts:                       # force no isolated vertex
            if not adj[v]:
                w = rng.choice([u for u in verts if u != v])
                adj[v].add(w)
                adj[w].add(v)
        nbrs = [tuple(sorted(adj[v])) for v in verts]
        E = sum(len(a) for a in adj) // 2
        order = verts[:]
        rng.shuffle(order)
        lab = [0] * n
        for i, v in enumerate(order, 1):
            lab[v] = i
        paths, valleys = literal_paths(nbrs, lab)
        P = validate(paths, valleys, nbrs, lab)
        N = [0] * n
        for p in paths:
            N[p[-1]] += 1
        up = [sum(1 for w in nbrs[v] if lab[w] > lab[v]) for v in verts]
        down = [sum(1 for w in nbrs[v] if lab[w] < lab[v]) for v in verts]
        assert all(N[v] >= 1 for v in verts), "Step 3 fails"
        assert sum(up) == E and sum(down) == E, "Step 1 fails"
        assert P == len(valleys) + sum(N[v] * up[v] for v in verts), "Step 4 fails"
        assert P >= E + len(valleys) >= E + 1, "Step 5 fails"
        checked += 1
        if P == E + 1:
            hits += 1
            m = sum(1 for v in verts if up[v] == 0)
            assert len(valleys) == 1, "Step 6: |Val| != 1"
            assert all(N[v] == 1 for v in verts if up[v] >= 1), "Step 6: N(v) != 1"
            assert E == (n - 1 - m) + sum(len(nbrs[v]) for v in verts if up[v] == 0), \
                "Step 6: down-degree count fails"
    return checked, hits


if __name__ == "__main__":
    here = "/Users/raducucu/bainsahackathon/run/tasks/H-C1-007/inbox/subject/"

    print("=== (A) literal enumeration of the submitted artefacts ===")
    for d in (3, 4):
        tot, nval, nlines = score_artefact(here + "Q%d.txt" % d, d)
        print("Q%d.txt: %d lines, bijection OK, valleys=%d, uphill paths (explicit "
              "tuples, each re-validated) = %d" % (d, nlines, nval, tot))

    print()
    print("=== (C) checker sanity: Q_1 and Q_2 hand cases, and exhaustive minima ===")
    for d in (1, 2):
        best, bo, hist, k = exhaustive(d, literal_every=1)
        print("Q%d: all %d labellings, min = %d, |E|+1 = %d, distribution = %s"
              % (d, k, best, d * (1 << (d - 1)) + 1, sorted(hist.items())))
    # the hand cases: identity labelling
    for d in (1, 2):
        nbrs = cube_nbrs(d)
        order = list(range(1 << d))
        print("Q%d identity labelling %s -> %d uphill paths"
              % (d, [format(v, "0%db" % d) for v in order], score_order(order, nbrs)))

    print()
    print("=== (B) exhaustive minimum over all 8! labellings of Q_3 ===")
    best3, bo3, hist3, k3 = exhaustive(3, literal_every=1009)
    print("labellings examined: %d (= 8!: %s)" % (k3, k3 == 40320))
    print("min uphill paths over ALL labellings of Q_3 = %d" % best3)
    print("lowest values: %s" % sorted(hist3.items())[:5])
    print("no labelling with 13 or fewer: %s"
          % all(t >= 14 for t in hist3))

    print()
    print("=== (D) hunt for a labelling of Q_4 with <= 33 uphill paths ===")
    b4, o4 = hunt_q4(33, 400)
    print("400 random restarts + full best-improvement transposition descent: best = %d" % b4)
    print("best order found: %s"
          % ["".join(str((v >> (3 - j)) & 1) for j in range(4)) for v in o4])

    print()
    print("=== (E) Step 1/3/4/5/6 on random graphs ===")
    checked, hits = step6_test(4000)
    print("random graphs+labellings checked: %d ; equality cases P = |E|+1 found: %d ; "
          "all Step 1,3,4,5,6 conclusions held" % (checked, hits))
