#!/usr/bin/env python3
"""zsat.py -- exact SAT + lazy cycle cuts for induced forests F of Q_9 of the form
      F = (O \\ Z) u M,   O = odd-weight vertices, Z subset of O with zmin <= |Z| <= zmax, M subset of even,
with |F| >= K, and (symmetry breaking) the odd vertex 000000001 in Z.
Symmetry breaking is sound: translations x -> x XOR t with t of even weight are automorphisms of Q_9 that map
O onto O and E onto E, so they map the class onto itself, preserve |F|, |Z| and acyclicity; they act
transitively on O (t = z XOR 000000001 sends z to 000000001, and t has even weight because z is odd). So if
some member of the class has Z nonempty, a translate of it has 000000001 in Z. (zmin >= 1 is required.)
Usage: zsat.py K zmin zmax [--budget_s seconds]"""
import sys, time, itertools
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from sym_forest_sat import find_cycles, is_forest
from pysat.solvers import Solver
from pysat.card import CardEnc, EncType

d, n = 9, 512


def main():
    K, zmin, zmax = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    assert zmin >= 1
    t0 = time.time()
    S = Solver(name="cadical153")
    var = lambda v: v + 1
    odd = [v for v in range(n) if bin(v).count("1") % 2]
    even = [v for v in range(n) if bin(v).count("1") % 2 == 0]
    seen = set()

    def cut(cy):
        c = tuple(sorted({-var(v) for v in cy}))
        if c not in seen:
            seen.add(c)
            S.add_clause(list(c))
            return True
        return False
    for x in range(n):
        for a in range(d):
            for b in range(a + 1, d):
                if not (x >> a) & 1 and not (x >> b) & 1:
                    cut([x, x ^ (1 << a), x ^ (1 << b), x ^ (1 << a) ^ (1 << b)])
        for a, b, c in itertools.combinations(range(d), 3):
            if (x >> a) & 1 or (x >> b) & 1 or (x >> c) & 1:
                continue
            cube = [x ^ (((s >> 0) & 1) << a) ^ (((s >> 1) & 1) << b) ^ (((s >> 2) & 1) << c) for s in range(8)]
            for s in range(4):
                cut([cube[r] for r in range(8) if r != s and r != 7 - s])
    top = n
    enc = CardEnc.atleast(lits=[var(v) for v in range(n)], bound=K, top_id=top, encoding=EncType.totalizer)
    S.append_formula(enc.clauses); top = max(top, enc.nv)
    # at most zmax odd vertices outside F  <=>  at least 256 - zmax odd vertices in F
    enc = CardEnc.atleast(lits=[var(v) for v in odd], bound=256 - zmax, top_id=top, encoding=EncType.totalizer)
    S.append_formula(enc.clauses); top = max(top, enc.nv)
    enc = CardEnc.atmost(lits=[var(v) for v in odd], bound=256 - zmin, top_id=top, encoding=EncType.totalizer)
    S.append_formula(enc.clauses); top = max(top, enc.nv)
    S.add_clause([-var(1)])
    print("K=%d |Z| in [%d,%d], setup %.1fs, %d short-cycle clauses" % (K, zmin, zmax, time.time() - t0,
          len(seen)), flush=True)
    it = 0
    while True:
        it += 1
        if not S.solve():
            print("UNSAT after %d iterations, %.1fs" % (it, time.time() - t0), flush=True)
            return
        m = S.get_model()
        F = [1 if m[v] > 0 else 0 for v in range(n)]
        cys = find_cycles(F, d, 400)
        if not cys:
            assert is_forest(F, d)
            with open("tmp/zsat_found.txt", "w") as fh:
                fh.write("".join(map(str, F)) + "\n")
            print("SAT after %d iterations %.1fs: |F|=%d" % (it, time.time() - t0, sum(F)), flush=True)
            return
        new = sum(1 for cy in cys if cut(cy))
        if it % 10 == 0:
            print("  it %d cuts %d %.1fs" % (it, len(seen), time.time() - t0), flush=True)
        if not new:
            print("ERROR no new cut"); return


if __name__ == "__main__":
    main()
