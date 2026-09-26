#!/usr/bin/env python3
"""sat_forest.py -- H-C5-003.  Lazy (CEGAR) SAT search for an induced forest of Q_d with >= K vertices.

Variables x_v (v in F).  Static clauses: for every 4-cycle (2-dim face) of Q_d, not all 4 in F; for every
3-dim subcube and every antipodal pair {a, a'} in it, the induced 6-cycle Q_3 - {a, a'} is not all in F.
Cardinality sum x_v >= K (pysat CardEnc, seqcounter or totalizer).  Symmetry breaking: x_0 = 0
(sound for K < 2^d: F != V, so some vertex s is not in F; translating by s (an automorphism of Q_d,
v -> v xor s, which maps induced forests to induced forests of equal size) moves s to 0).
Loop: solve; if the model's F is a forest, stop (FOUND); else find a cycle of G[F] (DFS) and add the clause
"not all vertices of this cycle in F"; repeat.  UNSAT means: no induced forest with >= K vertices exists
(every added clause is implied by forest-ness, the symmetry breaking is sound) -- but only a DRAT-checked
UNSAT would be a proof, and none is claimed here.  Time limited by the caller (timeout).
Usage: sat_forest.py d K [solver] [maxiter]
"""
import sys
import time
from itertools import combinations
from pysat.solvers import Solver
from pysat.card import CardEnc, EncType


def main():
    d = int(sys.argv[1])
    K = int(sys.argv[2])
    sname = sys.argv[3] if len(sys.argv) > 3 else "cadical153"
    maxiter = int(sys.argv[4]) if len(sys.argv) > 4 else 10 ** 9
    n = 1 << d
    var = lambda v: v + 1
    clauses = []
    # faces
    for i, j in combinations(range(d), 2):
        for v in range(n):
            if (v >> i) & 1 or (v >> j) & 1:
                continue
            cyc = [v, v ^ (1 << i), v ^ (1 << i) ^ (1 << j), v ^ (1 << j)]
            clauses.append([-var(w) for w in cyc])
    # hexagons in 3-subcubes
    nh = 0
    for i, j, k in combinations(range(d), 3):
        mask = (1 << i) | (1 << j) | (1 << k)
        for base in range(n):
            if base & mask:
                continue
            cube = [base ^ a for a in (0, 1 << i, 1 << j, 1 << k, (1 << i) | (1 << j), (1 << i) | (1 << k),
                                       (1 << j) | (1 << k), mask)]
            for a in cube:
                if a > (a ^ mask):
                    continue
                hexa = [w for w in cube if w != a and w != (a ^ mask)]
                clauses.append([-var(w) for w in hexa])
                nh += 1
    clauses.append([-var(0)])
    card = CardEnc.atleast(lits=[var(v) for v in range(n)], bound=K, top_id=n, encoding=EncType.seqcounter)
    s = Solver(name=sname, bootstrap_with=clauses + card.clauses)
    t0 = time.time()
    it = 0
    added = 0
    while it < maxiter:
        it += 1
        ok = s.solve()
        if not ok:
            print("UNSAT d=%d K=%d after %d iterations, %d cycle clauses, %.1fs" % (d, K, it, added, time.time() - t0))
            return
        model = s.get_model()
        F = [model[v] > 0 for v in range(n)]
        # find cycles via union-find over edges; for each edge closing a cycle, extract the tree path
        par = list(range(n))

        def find(x):
            while par[x] != x:
                par[x] = par[par[x]]
                x = par[x]
            return x
        adj = {v: [] for v in range(n) if F[v]}
        newcl = 0
        closing = []
        for v in range(n):
            if not F[v]:
                continue
            for j in range(d):
                w = v ^ (1 << j)
                if w > v and F[w]:
                    a, b = find(v), find(w)
                    if a == b:
                        closing.append((v, w))
                    else:
                        par[a] = b
                        adj[v].append(w)
                        adj[w].append(v)
        if not closing:
            with open("sat_F_d%d_K%d.txt" % (d, K), "w") as fo:
                fo.write("".join("1" if F[v] else "0" for v in range(n)) + "\n")
            print("FOUND forest |F|=%d d=%d K=%d after %d iterations, %d cycle clauses, %.1fs"
                  % (sum(F), d, K, it, added, time.time() - t0))
            return
        for (v, w) in closing:
            # path v -> w in the spanning forest (BFS)
            prev = {v: None}
            q = [v]
            h = 0
            while h < len(q):
                x = q[h]
                h += 1
                if x == w:
                    break
                for y in adj[x]:
                    if y not in prev:
                        prev[y] = x
                        q.append(y)
            path = []
            x = w
            while x is not None:
                path.append(x)
                x = prev[x]
            s.add_clause([-var(u) for u in path])
            added += 1
            newcl += 1
        if it % 20 == 0:
            print("iter %d: |F|=%d cycles cut %d (total %d) %.1fs" % (it, sum(F), newcl, added, time.time() - t0),
                  flush=True)
    print("STOPPED (maxiter) d=%d K=%d" % (d, K))


if __name__ == "__main__":
    main()
