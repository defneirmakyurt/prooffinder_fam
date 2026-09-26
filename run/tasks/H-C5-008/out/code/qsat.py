#!/usr/bin/env python3
"""
qsat.py -- SAT/CEGAR search for an induced forest of size >= m in a covering quotient Q_9/C.
Needs python-sat (NOT used by any checker; exploratory / cross-check only).

Usage: qsat.py r m [timeout_per_class_s] [class_index ...]
For each code class of dimension r (quotients.code_classes), decide whether the quotient
multigraph has an induced forest (no loop, no parallel pair, no cycle) with >= m vertices.
Every SAT answer is re-verified with quotients.is_forest_multi and, after lifting to Q_9, with
quotients.is_forest_qd; a lifted forest is written to ../tmp/forest_r<r>_c<i>_<size>.txt.
UNSAT answers are solver answers without a proof certificate (not a verification).
"""
import sys, time, itertools
from pysat.solvers import Cadical153
from pysat.card import CardEnc, EncType
from pysat.formula import IDPool
import quotients as Q


def cycles_in(F, nbr):
    """Fundamental cycles (vertex lists) of the simple graph induced by F (parallel pairs are
    excluded by clauses beforehand, so neighbour lists are de-duplicated here): one cycle per
    non-tree edge of a BFS spanning forest."""
    Fs = set(F)
    parent, depth, cyc = {}, {}, []
    adj = {y: sorted(set(z for z in nbr[y] if z in Fs)) for y in F}
    for s in F:
        if s in parent:
            continue
        parent[s] = None; depth[s] = 0
        queue = [s]
        for y in queue:
            for z in adj[y]:
                if z not in parent:
                    parent[z] = y; depth[z] = depth[y] + 1; queue.append(z)
    for y in F:
        for z in adj[y]:
            if y < z and parent[z] != y and parent[y] != z:
                a, b = y, z
                pa, pb = [a], [b]
                while a != b:
                    if depth[a] >= depth[b]:
                        a = parent[a]; pa.append(a)
                    else:
                        b = parent[b]; pb.append(b)
                cyc.append(pa + pb[-2::-1])
    return cyc


def solve_class(r, idx, cnt, m, tlimit):
    words = Q.codewords_from_counts(cnt, r)
    k, H, gens, proj = Q.quotient(words)
    n = 1 << k
    nbr = Q.quotient_graph(gens, k)
    var = lambda y: y + 1
    pool = IDPool(start_from=n + 1)
    s = Cadical153()
    # parallel pairs
    for y in range(n):
        seenz = set()
        for z in nbr[y]:
            if z in seenz:
                s.add_clause([-var(y), -var(z)])
            seenz.add(z)
    # all 4-cycles y, y^a, y^a^b, y^b with a != b, a^b != 0
    g = sorted(set(gens))
    for a, b in itertools.combinations(g, 2):
        for y in range(n):
            s.add_clause([-var(y), -var(y ^ a), -var(y ^ a ^ b), -var(y ^ b)])
    card = CardEnc.atleast(lits=[var(y) for y in range(n)], bound=m, vpool=pool,
                           encoding=EncType.seqcounter)
    for cl in card.clauses:
        s.add_clause(cl)
    t0 = time.time()
    it = 0
    while True:
        if time.time() - t0 > tlimit:
            s.delete()
            return ("TIMEOUT", it, None, time.time() - t0)
        ok = s.solve()
        it += 1
        if not ok:
            s.delete()
            return ("UNSAT", it, None, time.time() - t0)
        model = s.get_model()
        F = [y for y in range(n) if model[y] > 0]
        cyc = cycles_in(F, nbr)
        if not cyc:
            assert Q.is_forest_multi(set(F), nbr)
            T = Q.lift(set(F), proj)
            assert Q.is_forest_qd(T), "lift not a forest"
            fn = "../tmp/forest_r%d_c%d_%d.txt" % (r, idx, len(T))
            with open(fn, "w") as fh:
                fh.write("\n".join(format(x, "09b") for x in sorted(T)) + "\n")
            s.delete()
            return ("SAT", it, (len(F), len(T), fn), time.time() - t0)
        for c in cyc:
            s.add_clause([-var(y) for y in c])


def main():
    r = int(sys.argv[1]); m = int(sys.argv[2])
    tl = float(sys.argv[3]) if len(sys.argv) > 3 else 60.0
    classes = Q.code_classes(r)
    sel = [int(a) for a in sys.argv[4:]] if len(sys.argv) > 4 else range(len(classes))
    T0 = time.time()
    for i in sel:
        res = solve_class(r, i, classes[i], m, tl)
        print("r=%d class=%d counts=%s m=%d -> %s iters=%d info=%s time=%.1fs" %
              (r, i, classes[i], m, res[0], res[1], res[2], res[3]), flush=True)
    print("total %.1fs" % (time.time() - T0))


if __name__ == "__main__":
    main()
