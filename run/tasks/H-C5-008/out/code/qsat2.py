#!/usr/bin/env python3
"""
qsat2.py -- SAT/CEGAR: does a quotient multigraph (graph file as written by affquot.py:
first line n, then n lines 'deg w_1 .. w_deg') have an induced forest with >= m vertices?
Needs python-sat. Exploratory: SAT answers are verified (forest check + lift is done by caller);
UNSAT answers carry no proof certificate.
Usage: qsat2.py graph.txt m timeout_s outfile
"""
import sys, time, itertools
from pysat.solvers import Cadical153
from pysat.card import CardEnc, EncType
from pysat.formula import IDPool
from qsat import cycles_in


def main():
    gfile, m, tl, outf = sys.argv[1], int(sys.argv[2]), float(sys.argv[3]), sys.argv[4]
    tok = open(gfile).read().split()
    n = int(tok[0]); p = 1
    nbr = []
    for v in range(n):
        dv = int(tok[p]); p += 1
        nbr.append([int(x) for x in tok[p:p + dv]]); p += dv
    var = lambda y: y + 1
    pool = IDPool(start_from=n + 1)
    s = Cadical153()
    adj = [sorted(set(r)) for r in nbr]
    for y in range(n):
        for z in set(nbr[y]):
            if nbr[y].count(z) > 1 and y < z:
                s.add_clause([-var(y), -var(z)])
    nc4 = 0
    for u in range(n):
        for v, x in itertools.combinations(adj[u], 2):
            for w in set(adj[v]) & set(adj[x]):
                if w != u and u < w and u < v and u < x:
                    s.add_clause([-var(u), -var(v), -var(w), -var(x)]); nc4 += 1
    card = CardEnc.atleast(lits=[var(y) for y in range(n)], bound=m, vpool=pool,
                           encoding=EncType.seqcounter)
    for cl in card.clauses:
        s.add_clause(cl)
    t0 = time.time(); it = 0; ncl = 0
    while True:
        if time.time() - t0 > tl:
            print("TIMEOUT iters=%d cycle_clauses=%d c4=%d %.1fs" % (it, ncl, nc4, time.time() - t0)); return
        ok = s.solve(); it += 1
        if not ok:
            print("UNSAT iters=%d cycle_clauses=%d c4=%d %.1fs" % (it, ncl, nc4, time.time() - t0)); return
        model = s.get_model()
        F = [y for y in range(n) if model[y] > 0]
        cyc = cycles_in(F, nbr)
        if not cyc:
            with open(outf, "w") as fh:
                fh.write("\n".join(map(str, F)) + "\n")
            print("SAT |F|=%d iters=%d %.1fs -> %s" % (len(F), it, time.time() - t0, outf)); return
        for c in cyc:
            s.add_clause([-var(y) for y in c]); ncl += 1


if __name__ == "__main__":
    main()
