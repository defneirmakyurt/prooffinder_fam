#!/usr/bin/env python3
"""sat_cegar.py -- search for a decycling set S of Q_d with |S| <= K by SAT + lazy cycle clauses (CEGAR).

Variables: y_o = 1 iff orbit o is in S. Orbits are cosets v + W of an optional translation subgroup W
(generators given with --trans, as integers); W = {0} by default (no symmetry assumption).
Clauses: for every cycle C found in Q_d[V \\ S]: OR_{v in C} y_{orbit(v)}. Initially all 4-cycles and all
6-cycles of Q_d. Cardinality: |W| * sum y <= K. Loop: solve; if UNSAT -> no S of this class with |S|<=K
(only meaningful if the solver finished; UNSAT here is NOT reported as a proof, no DRAT is produced);
if SAT, test whether V \\ S is a forest; if yes print it and stop; else add clauses for cycles and repeat.

This is a SEARCH tool. A found S is verified independently (check_forest / checker). A timeout or UNSAT is
not used as a claim.
Usage: sat_cegar.py d K [--trans g1,g2,...] [--seed s] [--time T] [--out file] [--fix0]
"""
import sys, time, random, argparse
from pysat.solvers import Solver
from pysat.card import CardEnc, EncType
from pysat.formula import IDPool

ap = argparse.ArgumentParser()
ap.add_argument('d', type=int); ap.add_argument('K', type=int)
ap.add_argument('--trans', default='')
ap.add_argument('--seed', type=int, default=0)
ap.add_argument('--time', type=float, default=300.0)
ap.add_argument('--out', default='')
ap.add_argument('--fix0', action='store_true', help='force vertex 0 in S (sound by vertex-transitivity, only without --trans)')
ap.add_argument('--solver', default='cd15')
ap.add_argument('--maxcuts', type=int, default=400)
ap.add_argument('--oddmax', type=int, default=-1, help='near-parity class: |S cap O| <= z and |S cap E| <= K - z (replaces the |S| <= K constraint)')
a = ap.parse_args()
d, K = a.d, a.K
n = 1 << d
random.seed(a.seed)

# translation subgroup W
gens = [int(x) for x in a.trans.split(',') if x.strip()]
W = [0]
for g in gens:
    if g not in W:
        W = W + [w ^ g for w in W]
W = sorted(set(W))
orbit = [-1] * n
reps = []
for v in range(n):
    if orbit[v] < 0:
        for w in W:
            orbit[v ^ w] = len(reps)
        reps.append(v)
no = len(reps)
if K // len(W) < 0:
    print('K too small'); sys.exit(1)
Kr = K // len(W)
print('d=%d n=%d |W|=%d orbits=%d K=%d -> orbit budget %d' % (d, n, len(W), no, K, Kr), flush=True)

pool = IDPool(start_from=no + 1)
clauses = set()

def add_cycle(cyc):
    cl = tuple(sorted({orbit[v] + 1 for v in cyc}))
    if cl not in clauses:
        clauses.add(cl)
        return cl
    return None

def nb(v):
    return [v ^ (1 << j) for j in range(d)]

init = []
# 4-cycles: v, v^a, v^a^b, v^b
for v in range(n):
    for i in range(d):
        for j in range(i + 1, d):
            c = add_cycle([v, v ^ (1 << i), v ^ (1 << i) ^ (1 << j), v ^ (1 << j)])
            if c: init.append(c)
# 6-cycles: in each Q_3 subcube, the 6-cycles are complements of antipodal pairs: Q_3 minus {x, x^abc}
for v in range(n):
    for i in range(d):
        for j in range(i + 1, d):
            for k in range(j + 1, d):
                m = (1 << i) | (1 << j) | (1 << k)
                base = v & ~m
                cube = [base | (((t >> 0) & 1) << i) | (((t >> 1) & 1) << j) | (((t >> 2) & 1) << k) for t in range(8)]
                for x in cube:
                    if (x & m) < ((x ^ m) & m):
                        cyc = [y for y in cube if y != x and y != (x ^ m)]
                        c = add_cycle(cyc)
                        if c: init.append(c)
print('initial cycle clauses:', len(init), flush=True)

s = Solver(name=a.solver)
for c in init:
    s.add_clause(list(c))
if a.oddmax >= 0:
    assert len(W) == 1
    ev = [v + 1 for v in range(n) if bin(v).count('1') % 2 == 0]
    od = [v + 1 for v in range(n) if bin(v).count('1') % 2 == 1]
    c1 = CardEnc.atmost(lits=od, bound=a.oddmax, vpool=pool, encoding=EncType.seqcounter)
    # |S cap E| <= K - z  <=>  at least (n/2 - K + z) even vertices NOT in S
    c2 = CardEnc.atleast(lits=[-x for x in ev], bound=n // 2 - K + a.oddmax, vpool=pool, encoding=EncType.seqcounter)
    class _C: pass
    card = _C(); card.clauses = c1.clauses + c2.clauses
    print('near-parity class: |S cap O| <= %d, |S cap E| <= %d' % (a.oddmax, K - a.oddmax), flush=True)
else:
    card = CardEnc.atmost(lits=list(range(1, no + 1)), bound=Kr, vpool=pool, encoding=EncType.seqcounter)
for c in card.clauses:
    s.add_clause(c)
if a.fix0 and len(W) == 1:
    s.add_clause([orbit[0] + 1])

def find_cycles(inS):
    """Return a list of cycles (vertex lists) in Q_d[V\\S]: for each non-tree edge of a BFS forest,
    the shortest cycle through that edge (BFS in the forest graph avoiding the edge)."""
    par = [-2] * n
    depth = [0] * n
    nontree = []
    for r in range(n):
        if inS[r] or par[r] != -2: continue
        par[r] = -1
        q = [r]; h = 0
        while h < len(q):
            v = q[h]; h += 1
            for w in nb(v):
                if inS[w]: continue
                if par[w] == -2:
                    par[w] = v; depth[w] = depth[v] + 1; q.append(w)
                elif w != par[v] and v < w and par[w] != v:
                    nontree.append((v, w))
    random.shuffle(nontree)
    cycles = []
    for (u, w) in nontree[:a.maxcuts]:
        # shortest u-w path avoiding edge uw
        prev = {u: None}
        q = [u]; h = 0; found = False
        while h < len(q) and not found:
            x = q[h]; h += 1
            for y in nb(x):
                if inS[y] or y in prev: continue
                if x == u and y == w: continue
                prev[y] = x
                if y == w: found = True; break
                q.append(y)
        if found:
            cyc = []
            y = w
            while y is not None:
                cyc.append(y); y = prev[y]
            cycles.append(cyc)
    return cycles, len(nontree)

t0 = time.time()
it = 0
while True:
    it += 1
    left = a.time - (time.time() - t0)
    if left <= 0:
        print('TIMED OUT after %d iterations, %.1fs, clauses=%d' % (it - 1, time.time() - t0, len(clauses))); sys.exit(2)
    ok = s.solve()
    if not ok:
        print('UNSAT (class: |W|=%d, K=%d) after %d iterations, %.1fs (no DRAT; not a claim)' % (len(W), K, it, time.time() - t0)); sys.exit(3)
    model = s.get_model()
    inS = [model[orbit[v]] > 0 for v in range(n)]
    cycles, nnt = find_cycles(inS)
    if not cycles:
        sz = sum(inS)
        print('FOUND decycling set |S|=%d after %d iterations, %.1fs' % (sz, it, time.time() - t0), flush=True)
        if a.out:
            open(a.out, 'w').write(''.join('0' if inS[v] else '1' for v in range(n)) + '\n')
        sys.exit(0)
    added = 0
    for cyc in cycles:
        c = add_cycle(cyc)
        if c:
            s.add_clause(list(c)); added += 1
    if it % 20 == 0:
        print('it %d: |S|=%d nontree=%d added=%d total clauses=%d t=%.1fs' % (it, sum(inS), nnt, added, len(clauses), time.time() - t0), flush=True)
