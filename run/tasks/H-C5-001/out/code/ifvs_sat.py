#!/usr/bin/env python3
"""
ifvs_sat.py -- search for an INDEPENDENT FEEDBACK VERTEX SET S of Q_d with |S| <= K,
optionally restricted to sets invariant under a group G of automorphisms of Q_d.

  S independent            : no edge of Q_d has both ends in S
  S feedback vertex set    : Q_d - S has no cycle (is a forest)

By the reduction (out/reduction.md, part (b)) such an S gives a labelling of Q_d with
exactly 2^d + (d-1)|S| uphill paths; for d = 9 that is 512 + 8|S|.

Method: SAT over one boolean per G-orbit (x_O = "orbit O is inside S"), with
  * independence clauses  (not x_[u] or not x_[v]) for every edge uv,
  * all 4-cycle clauses   (every 4-cycle meets S),
  * a cardinality bound   sum |O| x_O <= K  (orbit literal repeated |O| times, sequential counter/totalizer),
  * lazily generated cycle clauses: after each model, the fundamental cycles of the spanning
    forest of Q_d - S are turned into clauses "some vertex of this cycle is in S" (lifted to orbits),
until the model's complement is acyclic (=> SOLUTION) or the solver says UNSAT (=> no G-invariant
IFVS of size <= K exists; this is NOT used for any claim in the report).

Group generators: --gen "p=a0,a1,...,a_{d-1}"  (coordinate i goes to coordinate a_i)
                  --gen "t=<d-bit string>"      (translation by that vector; bit string written
                                                 with coordinate 0 as the LEFTMOST char)
                  --gen "p=...;t=..."           (permutation then translation)
Output: the set S as a list of d-bit strings (coordinate 0 leftmost) in --out, and a summary line.
"""
import argparse
import random
import sys
import time

from pysat.card import CardEnc, EncType
from pysat.formula import IDPool
from pysat.solvers import Solver


def parse_gen(s, d):
    perm = list(range(d))
    trans = 0
    for part in s.split(";"):
        part = part.strip()
        if part.startswith("p="):
            perm = [int(x) for x in part[2:].split(",")]
            assert sorted(perm) == list(range(d)), "bad permutation"
        elif part.startswith("t="):
            bits = part[2:]
            assert len(bits) == d and set(bits) <= set("01")
            trans = sum(1 << i for i, c in enumerate(bits) if c == "1")
        else:
            raise ValueError("bad generator " + s)

    def f(v):
        w = 0
        for i in range(d):
            if (v >> i) & 1:
                w |= 1 << perm[i]
        return w ^ trans
    return f


def vstr(v, d):
    return "".join("1" if (v >> i) & 1 else "0" for i in range(d))


def orbits(d, gens):
    n = 1 << d
    par = list(range(n))

    def find(x):
        while par[x] != x:
            par[x] = par[par[x]]
            x = par[x]
        return x
    for g in gens:
        for v in range(n):
            a, b = find(v), find(g(v))
            if a != b:
                par[a] = b
    roots = {}
    orb = [0] * n
    for v in range(n):
        r = find(v)
        if r not in roots:
            roots[r] = len(roots)
        orb[v] = roots[r]
    return orb, len(roots)


def find_cycles(d, inS, maxcyc):
    """Fundamental cycles of Q_d - S w.r.t. a BFS spanning forest (list of vertex lists)."""
    n = 1 << d
    parent = [-1] * n
    depth = [-1] * n
    cycles = []
    for r in range(n):
        if inS[r] or depth[r] >= 0:
            continue
        depth[r] = 0
        queue = [r]
        qi = 0
        while qi < len(queue):
            u = queue[qi]
            qi += 1
            for j in range(d):
                w = u ^ (1 << j)
                if inS[w]:
                    continue
                if depth[w] < 0:
                    depth[w] = depth[u] + 1
                    parent[w] = u
                    queue.append(w)
                elif w != parent[u] and u < w and parent[w] != u:
                    # non-tree edge u-w: fundamental cycle
                    a, b = u, w
                    pa, pb = [a], [b]
                    while depth[a] > depth[b]:
                        a = parent[a]; pa.append(a)
                    while depth[b] > depth[a]:
                        b = parent[b]; pb.append(b)
                    while a != b:
                        a = parent[a]; pa.append(a)
                        b = parent[b]; pb.append(b)
                    cycles.append(pa + pb[:-1][::-1])
                    if len(cycles) >= maxcyc:
                        return cycles
    return cycles


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--d", type=int, required=True)
    ap.add_argument("--K", type=int, required=True)
    ap.add_argument("--gen", action="append", default=[])
    ap.add_argument("--solver", default="cadical195")
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--maxcyc", type=int, default=100000)
    ap.add_argument("--timeout", type=float, default=550.0)
    ap.add_argument("--out", default=None)
    ap.add_argument("--card", default="seqcounter")
    ap.add_argument("--noindep", action="store_true", help="drop the independence clauses (plain feedback vertex set)")
    ap.add_argument("--evenonly", action="store_true", help="(no-group mode only) forbid odd-weight vertices in S")
    ap.add_argument("--mixed", action="store_true",
                    help="(no-group mode only) require vertex 0 in S and some odd-weight vertex in S")
    args = ap.parse_args()
    d, K = args.d, args.K
    n = 1 << d
    t0 = time.time()
    gens = [parse_gen(s, d) for s in args.gen]
    orb, norb = orbits(d, gens)
    size = [0] * norb
    for v in range(n):
        size[orb[v]] += 1
    pool = IDPool()
    X = [pool.id(("x", o)) for o in range(norb)]
    clauses = set()

    def add(cl):
        cl = tuple(sorted(set(cl)))
        clauses.add(cl)
        return cl
    # independence
    for v in (range(n) if not args.noindep else []):
        for j in range(d):
            w = v ^ (1 << j)
            if v < w:
                add((-X[orb[v]], -X[orb[w]]))
    # 4-cycles
    for v in range(n):
        for i in range(d):
            for j in range(i + 1, d):
                if (v >> i) & 1 or (v >> j) & 1:
                    continue
                cyc = [v, v ^ (1 << i), v ^ (1 << i) ^ (1 << j), v ^ (1 << j)]
                add([X[orb[u]] for u in cyc])
    if args.mixed:
        assert not gens
        add((X[orb[0]],))
        add([X[orb[v]] for v in range(n) if bin(v).count("1") % 2 == 1])
    if args.evenonly:
        assert not gens
        for v in range(n):
            if bin(v).count("1") % 2 == 1:
                add((-X[orb[v]],))
    solver = Solver(name=args.solver)
    for cl in clauses:
        solver.add_clause(list(cl))
    lits = []
    for o in range(norb):
        lits += [X[o]] * size[o]
    enc = {"seqcounter": EncType.seqcounter, "totalizer": EncType.totalizer,
           "sortnetwrk": EncType.sortnetwrk, "cardnetwrk": EncType.cardnetwrk}[args.card]
    card = CardEnc.atmost(lits=lits, bound=K, vpool=pool, encoding=enc)
    for cl in card.clauses:
        solver.add_clause(cl)
    it = 0
    ncyc = 0
    result = None
    while True:
        it += 1
        if time.time() - t0 > args.timeout:
            result = "TIMEOUT"
            break
        ok = solver.solve()
        if not ok:
            result = "UNSAT"
            break
        model = solver.get_model()
        mset = set(l for l in model if l > 0)
        inS = [X[orb[v]] in mset for v in range(n)]
        cycles = find_cycles(d, inS, args.maxcyc)
        if not cycles:
            result = "FOUND"
            break
        new = 0
        for cyc in cycles:
            cl = tuple(sorted(set(X[orb[u]] for u in cyc)))
            if cl not in clauses:
                clauses.add(cl)
                solver.add_clause(list(cl))
                new += 1
        ncyc += new
        if it % 20 == 0:
            print("iter %d  |S|=%d  cycles=%d new=%d total_cycle_clauses=%d  t=%.1fs" %
                  (it, sum(inS), len(cycles), new, ncyc, time.time() - t0), flush=True)
    dt = time.time() - t0
    if result == "FOUND":
        S = [v for v in range(n) if inS[v]]
        print("FOUND d=%d |S|=%d orbits=%d iters=%d cycle_clauses=%d time=%.1fs uphill=%d" %
              (d, len(S), norb, it, ncyc, dt, n + (d - 1) * len(S)))
        if args.out:
            with open(args.out, "w") as fh:
                for v in S:
                    fh.write(vstr(v, d) + "\n")
    else:
        print("%s d=%d K=%d orbits=%d iters=%d cycle_clauses=%d time=%.1fs" %
              (result, d, K, norb, it, ncyc, dt))


if __name__ == "__main__":
    main()
