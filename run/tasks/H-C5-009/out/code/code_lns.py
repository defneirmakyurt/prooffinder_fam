#!/usr/bin/env python3
"""code_lns.py -- heuristic large-neighbourhood search around a 20-word even code (needs python-sat).
NOT exhaustive, proves nothing; a SAT verdict without a DRAT proof is reported as "solver verdict only".

Start: a code C of even words of Q_9, pairwise distance >= 4 (the parity construction F = C u O, |S| = 256 - |C|).
Neighbourhood: remove a set R of r codewords (a codeword and its r-1 nearest codewords). Let
  X  = even words at distance >= 4 from every word of C \\ R   (so X-words share no odd neighbour with C \\ R),
  NX = odd words adjacent to some word of X.
Ask SAT: is there M' subset of X and Z subset of NX with Q_9[M' u (NX \\ Z)] a forest and |M'| - |Z| >= r + 1?
If yes, M = (C \\ R) u M' has Phi(M) >= 20 - r + r + 1 = 21 (claims.md V2): the clusters of C \\ R are singletons
at distance >= 4 from X, their odd neighbourhoods are disjoint from NX, and odd words outside NX u N(C \\ R) are
isolated in F. Then F = M u (O \\ Z) is an induced forest with |S| = 256 - 21 = 235 (written to a file and
re-checked with check_forest.py by the caller).
Forest constraint by lazy cycle clauses (CEGAR): for every cycle found in a candidate solution, at least one of its
even vertices is dropped from M' or one of its odd vertices is put in Z.
Usage: code_lns.py c1,c2,...,c20 r [--time T] [--maxtries N] [--out F.txt]
"""
import sys, time, argparse
from pysat.solvers import Cadical153
from pysat.card import CardEnc, EncType
from pysat.formula import IDPool

ap = argparse.ArgumentParser()
ap.add_argument('code'); ap.add_argument('r', type=int)
ap.add_argument('--time', type=float, default=60.0)
ap.add_argument('--maxtries', type=int, default=20)
ap.add_argument('--out', default='tmp/lns_found.txt')
a = ap.parse_args()
pc = lambda x: bin(x).count('1')
C = [int(x) for x in a.code.split(',')]
assert all(pc(u ^ v) >= 4 for i, u in enumerate(C) for v in C[i + 1:])

def find_cycle(Mset, Oset):
    """return (evens, odds) of one cycle in Q_9[Mset u Oset] (bipartite), or None"""
    par = {}; vis = set()
    for s in Mset:
        if s in vis: continue
        stack = [(s, None)]; parent = {s: None}; vis.add(s)
        # iterative DFS with explicit neighbour iterators
        it = {s: iter([s ^ (1 << b) for b in range(9)])}
        path = [s]
        while path:
            v = path[-1]
            nxt = None
            for u in it[v]:
                if (u in Mset or u in Oset) and u != parent[v]:
                    nxt = u; break
            if nxt is None:
                path.pop(); continue
            if nxt in vis:
                # back edge to an ancestor on the current path
                cyc = path[path.index(nxt):]
                return [x for x in cyc if pc(x) % 2 == 0], [x for x in cyc if pc(x) % 2 == 1]
            vis.add(nxt); parent[nxt] = v; it[nxt] = iter([nxt ^ (1 << b) for b in range(9)]); path.append(nxt)
    return None

t0 = time.time()
results = []
for ci, c in enumerate(C[:a.maxtries]):
    if time.time() - t0 > a.time: break
    R = sorted(C, key=lambda u: (pc(u ^ c), u))[:a.r]
    rest = [u for u in C if u not in R]
    X = [x for x in range(512) if pc(x) % 2 == 0 and all(pc(x ^ u) >= 4 for u in rest)]
    NX = sorted({x ^ (1 << b) for x in X for b in range(9)})
    pool = IDPool()
    mv = {x: pool.id(('m', x)) for x in X}
    zv = {o: pool.id(('z', o)) for o in NX}
    lits = [mv[x] for x in X] + [-zv[o] for o in NX]
    bound = a.r + 1 + len(NX)
    if bound > len(lits):
        print('center %d r=%d |X|=%d |NX|=%d -> IMPOSSIBLE (|X| < r + 1: even keeping all of X and deleting nothing is too small)' % (c, a.r, len(X), len(NX)), flush=True)
        results.append('IMPOSSIBLE'); continue
    card = CardEnc.atleast(lits=lits, bound=bound, vpool=pool, encoding=EncType.seqcounter)
    s = Cadical153(bootstrap_with=card.clauses)
    # 4-cycles up front: two X words at distance 2 with both common neighbours kept
    for i, x in enumerate(X):
        for y in X[i + 1:]:
            d = x ^ y
            if pc(d) == 2:
                lo = d & -d; hi = d ^ lo
                s.add_clause([-mv[x], -mv[y], zv[x ^ lo], zv[x ^ hi]])
    iters = 0; verdict = None
    while True:
        if time.time() - t0 > a.time: verdict = 'TIMEOUT'; break
        if not s.solve(): verdict = 'UNSAT (solver verdict only)'; break
        model = set(l for l in s.get_model() if l > 0)
        Ms = {x for x in X if mv[x] in model}
        Os = {o for o in NX if zv[o] not in model}
        cyc = find_cycle(Ms, Os)
        iters += 1
        if cyc is None:
            verdict = 'SAT'
            Z = set(NX) - Os
            M = set(rest) | Ms
            Fs = ''.join('1' if (v in M or (pc(v) % 2 == 1 and v not in Z)) else '0' for v in range(512))
            open(a.out, 'w').write(Fs + '\n')
            break
        ev, od = cyc
        s.add_clause([-mv[x] for x in ev] + [zv[o] for o in od])
    print('center %d r=%d |X|=%d |NX|=%d cegar_iters=%d -> %s  (%.1fs)' % (c, a.r, len(X), len(NX), iters, verdict, time.time() - t0), flush=True)
    results.append(verdict)
    s.delete()
    if verdict == 'SAT':
        print('FOUND: forest written to', a.out); break
print('summary:', {v: results.count(v) for v in set(results)})
