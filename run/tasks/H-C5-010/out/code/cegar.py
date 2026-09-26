#!/usr/bin/env python3
"""
cegar.py -- CEGAR search for an induced forest of Q_d with >= m vertices.

  python cegar.py --d 9 --m 280 --kset 2,3,4,5,6,7,8 [--sb root] [--solver cd195]
                  [--maxit N] [--tlimit SEC] [--out PREFIX]

Base formula = enc.py constraints (K) for k in kset, (G) sum >= m, optional symmetry breaking
(see symbreak.py).  Loop: solve; if SAT, read T from the model; if Q_d[T] is acyclic, report
SAT (T is an induced forest with >= m vertices); otherwise add one cycle clause for a shortest
cycle through every non-tree edge of a BFS forest of Q_d[T] and repeat.  On UNSAT write
PREFIX.cycles (one cycle per line) so that certify.py can rebuild and certify the final formula.
"""
import argparse
import sys
import time

import enc
import symbreak


def build_base(d, m, kset, sb, gl_enc="stdlib", exact=False):
    pool = enc.Pool(1 << d)
    clauses = []
    if exact:
        enc.global_exact_and_edges(d, m, pool, clauses)
    if kset:
        enc.build_subcube_counters(d, set(kset), pool, clauses)
    if sb:
        symbreak.add(d, sb, pool, clauses)
    if gl_enc == "stdlib":
        enc.global_atleast_stdlib(d, m, pool, clauses)
    else:
        enc.global_atleast(d, m, pool, clauses, gl_enc)
    return pool, clauses


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--d", type=int, required=True)
    ap.add_argument("--m", type=int, required=True)
    ap.add_argument("--kset", default="2,3,4,5")
    ap.add_argument("--sb", default="")
    ap.add_argument("--solver", default="cd195")
    ap.add_argument("--gl", default="stdlib")
    ap.add_argument("--exact", type=int, default=0, help="1: add |T|<=m and e(S) bound (E1,E2)")
    ap.add_argument("--maxit", type=int, default=100000)
    ap.add_argument("--tlimit", type=float, default=550.0)
    ap.add_argument("--out", default=None)
    ap.add_argument("--init", default=None, help="file of cycles to preload")
    a = ap.parse_args()
    from pysat.solvers import Solver
    t0 = time.time()
    kset = [int(x) for x in a.kset.split(",") if x]
    pool, clauses = build_base(a.d, a.m, kset, a.sb, a.gl, bool(a.exact))
    print("base: vars=%d clauses=%d (%.1fs)" % (pool.top, len(clauses), time.time() - t0), flush=True)
    s = Solver(name=a.solver, bootstrap_with=clauses)
    cycles = []
    if a.init:
        for line in open(a.init):
            c = [int(x) for x in line.split()]
            if c:
                cycles.append(c)
                s.add_clause([-(v + 1) for v in c])
    it = 0
    status = "TIMEOUT"
    hist = {}
    while it < a.maxit:
        if time.time() - t0 > a.tlimit:
            break
        it += 1
        r = s.solve()
        if not r:
            status = "UNSAT"
            break
        model = s.get_model()
        T = set(v for v in range(1 << a.d) if model[v] > 0)
        cyc = enc.shortest_cycles(a.d, T)
        if not cyc:
            status = "SAT"
            print("SAT: induced forest with %d vertices" % len(T))
            if a.out:
                with open(a.out + ".forest", "w") as f:
                    f.write(" ".join(map(str, sorted(T))) + "\n")
            break
        for c in cyc:
            assert enc.is_cycle_of_Qd(a.d, c)
            cycles.append(c)
            hist[len(c)] = hist.get(len(c), 0) + 1
            s.add_clause([-(v + 1) for v in c])
        if it % 50 == 0:
            print("it=%d cycles=%d lens=%s t=%.1f" % (it, len(cycles), dict(sorted(hist.items())), time.time() - t0), flush=True)
    print("RESULT d=%d m=%d kset=%s sb=%s exact=%d: %s after %d iterations, %d cycle clauses, %.1fs"
          % (a.d, a.m, a.kset, a.sb or "-", a.exact, status, it, len(cycles), time.time() - t0))
    print("cycle length histogram:", dict(sorted(hist.items())))
    if a.out:
        with open(a.out + ".cycles", "w") as f:
            for c in cycles:
                f.write(" ".join(map(str, c)) + "\n")


if __name__ == "__main__":
    main()
