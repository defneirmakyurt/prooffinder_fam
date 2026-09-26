#!/usr/bin/env python3
"""
crosscheck_F5_sat.py -- INDEPENDENT cross-check (different method from lb_forest.py) that
Q_5 has no induced forest on m = 19 vertices, and that m = 18 is attainable.
Method: CEGAR with a SAT solver (python-sat, CaDiCaL).  Variable x_v = [v in T].
Constraints: sum x_v >= m (sequential-counter cardinality encoding), and for every cycle C
found so far the clause OR_{v in C} not x_v (a cycle cannot lie entirely in an induced
forest).  Loop: solve; if SAT, the model T is checked for acyclicity; if it has a cycle, add
that cycle's clause and repeat; if acyclic, T is an induced forest of size >= m (report);
if UNSAT, no induced forest of size >= m exists (each added clause is valid for every
induced forest, so UNSAT of the relaxation implies the claim).  All 4-cycles are added up front.
Needs the venv python (python-sat).  Not the headline proof; lb_forest.py is.
"""
import sys, time
from pysat.solvers import Cadical153
from pysat.card import CardEnc, EncType

d = 5; n = 1 << d

def var(v): return v + 1

def find_cycle(T):
    """return a list of vertices forming a cycle in the subgraph induced on T, or None"""
    Ts = set(T); parent = {}; depth = {}
    for r in T:
        if r in parent: continue
        parent[r] = None; depth[r] = 0; stack = [r]
        while stack:
            v = stack.pop()
            for j in range(d):
                w = v ^ (1 << j)
                if w not in Ts or w == parent[v]: continue
                if w in parent:
                    # cycle: path v..lca..w
                    a, b = v, w; pa, pb = [a], [b]
                    while depth[a] > depth[b]: a = parent[a]; pa.append(a)
                    while depth[b] > depth[a]: b = parent[b]; pb.append(b)
                    while a != b: a = parent[a]; b = parent[b]; pa.append(a); pb.append(b)
                    return pa + pb[-2::-1]
                parent[w] = v; depth[w] = depth[v] + 1; stack.append(w)
    return None

def run(m):
    t0 = time.time()
    s = Cadical153()
    top = n
    enc = CardEnc.atleast(lits=[var(v) for v in range(n)], bound=m, top_id=top, encoding=EncType.seqcounter)
    for c in enc.clauses: s.add_clause(c)
    nc = 0
    for v in range(n):
        for i in range(d):
            for j in range(i + 1, d):
                if (v >> i) & 1 or (v >> j) & 1: continue
                cyc = [v, v ^ (1 << i), v ^ (1 << i) ^ (1 << j), v ^ (1 << j)]
                s.add_clause([-var(u) for u in cyc]); nc += 1
    it = 0
    while True:
        it += 1
        if not s.solve():
            print("m=%d: UNSAT after %d iterations, %d cycle clauses, %.1fs" % (m, it, nc, time.time() - t0)); return False
        model = s.get_model()
        T = [v for v in range(n) if model[v] > 0]
        cyc = find_cycle(T)
        if cyc is None:
            print("m=%d: SAT, induced forest of size %d found after %d iterations, %.1fs" % (m, len(T), it, time.time() - t0)); return True
        s.add_clause([-var(u) for u in cyc]); nc += 1

run(19)
run(18)
