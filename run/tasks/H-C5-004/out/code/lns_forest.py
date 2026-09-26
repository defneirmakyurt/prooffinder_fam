#!/usr/bin/env python3
"""lns_forest.py -- large-neighbourhood search for a large induced forest of Q_9.
Start: an induced forest F (0/1 indicator line file, or a labelling file -> F = {v : N(v) = 1}).
Step: pick a region R (random subcube of dimension k, or random ball); keep F outside R fixed; solve EXACTLY
(SAT + lazy cycle cuts, as in sym_forest_sat.py) "is there F' with F' \\ R = F \\ R, F' a forest,
|F' n R| >= |F n R| + 1"?  SAT -> improvement (verified by union-find).  UNSAT -> R cannot improve; then with
probability p make a plateau move: a random different forest with |F' n R| = |F n R| (diversification).
A per-step conflict budget bounds each SAT call (budget exhausted -> step skipped).
k > 0: subcube of dim k; k < 0: ball of the -k closest vertices; k = 0: mixed.
Usage: lns_forest.py init_file seed steps k out_file [--target T] [--plateau p] [--budget B]"""
import sys, random, time, itertools
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from sym_forest_sat import find_cycles, is_forest
from pysat.solvers import Solver
from pysat.card import CardEnc, EncType

d = 9
n = 1 << d


def load(fn):
    rows = open(fn).read().split()
    if len(rows) == 1 and len(rows[0]) == n:
        return [int(c) for c in rows[0]]
    order = [int(r, 2) for r in rows]
    lab = [0] * n
    for i, v in enumerate(order):
        lab[v] = i
    N = [0] * n
    for v in order:
        low = [v ^ (1 << j) for j in range(d) if lab[v ^ (1 << j)] < lab[v]]
        N[v] = sum(N[w] for w in low) + (0 if low else 1)
    return [1 if N[v] == 1 else 0 for v in range(n)]


SHORT = []
for x in range(n):
    for a in range(d):
        for b in range(a + 1, d):
            if not (x >> a) & 1 and not (x >> b) & 1:
                SHORT.append((x, x ^ (1 << a), x ^ (1 << b), x ^ (1 << a) ^ (1 << b)))
for x in range(n):
    for a, b, c in itertools.combinations(range(d), 3):
        if (x >> a) & 1 or (x >> b) & 1 or (x >> c) & 1:
            continue
        cube = [x ^ (((s >> 0) & 1) << a) ^ (((s >> 1) & 1) << b) ^ (((s >> 2) & 1) << c) for s in range(8)]
        for s in range(4):
            SHORT.append(tuple(cube[r] for r in range(8) if r != s and r != 7 - s))
VCYC = [[] for _ in range(n)]
for idx, cy in enumerate(SHORT):
    for v in cy:
        VCYC[v].append(idx)


def region_subcube(rng, k):
    coords = rng.sample(range(d), k)
    base = rng.randrange(n)
    for c in coords:
        base &= ~(1 << c)
    R = []
    for s in range(1 << k):
        v = base
        for i, c in enumerate(coords):
            if (s >> i) & 1:
                v |= 1 << c
        R.append(v)
    return R


def region_ball(rng, size):
    c = rng.randrange(n)
    by = sorted(range(n), key=lambda v: (bin(v ^ c).count("1"), rng.random()))
    return by[:size]


def solve_region(F, R, extra, budget, rng, forbid_same=False):
    """Return new F (list) or None. extra = required |F' n R| - |F n R|."""
    idx = {v: i + 1 for i, v in enumerate(R)}
    inR = set(R)
    S = Solver(name="cadical153")
    seen = set()

    def add_cut(cy):
        lits = []
        for v in cy:
            if v in inR:
                lits.append(-idx[v])
            elif not F[v]:
                return
        c = tuple(sorted(set(lits)))
        if c and c not in seen:
            seen.add(c)
            S.add_clause(list(c))
            return True
        return False
    cand = set()
    for v in R:
        cand.update(VCYC[v])
    for ci in cand:
        add_cut(SHORT[ci])
    cur = sum(F[v] for v in R)
    lits = list(range(1, len(R) + 1))
    top = len(R)
    card = CardEnc.atleast(lits=lits, bound=cur + extra, top_id=top, encoding=EncType.totalizer)
    for c in card.clauses:
        S.add_clause(c)
    if forbid_same:
        S.add_clause([-idx[v] if F[v] else idx[v] for v in R])
    # random phases for diversity
    S.set_phases([(i + 1) * (1 if rng.random() < 0.55 else -1) for i in range(len(R))])
    while True:
        S.conf_budget(budget)
        r = S.solve_limited()
        if r is None:
            return "BUDGET"
        if not r:
            return None
        model = S.get_model()
        G = list(F)
        for v in R:
            G[v] = 1 if model[idx[v] - 1] > 0 else 0
        cys = find_cycles(G, d, 300)
        if not cys:
            assert is_forest(G, d)
            return G
        new = 0
        for cy in cys:
            if add_cut(cy):
                new += 1
        if new == 0:
            raise RuntimeError("no new cut")


def main():
    a = sys.argv[1:]
    init, seed, steps, k, outf = a[0], int(a[1]), int(a[2]), int(a[3]), a[4]
    target = 277
    plateau = 0.5
    budget = 20000
    i = 5
    while i < len(a):
        if a[i] == "--target":
            target = int(a[i + 1])
        elif a[i] == "--plateau":
            plateau = float(a[i + 1])
        elif a[i] == "--budget":
            budget = int(a[i + 1])
        i += 2
    rng = random.Random(seed)
    F = load(init)
    assert is_forest(F, d)
    best = sum(F)
    t0 = time.time()
    print("seed %d start |F|=%d |S|=%d k=%d" % (seed, best, n - best, k), flush=True)
    stats = {"improve": 0, "unsat": 0, "budget": 0, "plateau": 0}
    for st in range(steps):
        if k > 0:
            R = region_subcube(rng, k)
        elif k < 0:
            R = region_ball(rng, -k)
        else:  # mixed: subcube of dimension 7 or a ball of 130..170 closest vertices
            R = region_subcube(rng, 7) if rng.random() < 0.5 else region_ball(rng, rng.randrange(130, 171))
        res = solve_region(F, R, 1, budget, rng)
        if res == "BUDGET":
            stats["budget"] += 1
            continue
        if res is not None:
            F = res
            stats["improve"] += 1
            best = sum(F)
            print("step %d IMPROVED |F|=%d |S|=%d (%.1fs)" % (st, best, n - best, time.time() - t0), flush=True)
            with open(outf, "w") as fh:
                fh.write("".join(map(str, F)) + "\n")
            if best >= target:
                break
            continue
        stats["unsat"] += 1
        if rng.random() < plateau:
            res = solve_region(F, R, 0, budget, rng, forbid_same=True)
            if res not in (None, "BUDGET"):
                F = res
                stats["plateau"] += 1
        if st % 50 == 0:
            print("step %d |F|=%d stats %s (%.1fs)" % (st, sum(F), stats, time.time() - t0), flush=True)
    print("END |F|=%d |S|=%d stats %s (%.1fs)" % (sum(F), n - sum(F), stats, time.time() - t0), flush=True)
    with open(outf + ".final", "w") as fh:
        fh.write("".join(map(str, F)) + "\n")


if __name__ == "__main__":
    main()
