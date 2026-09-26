#!/usr/bin/env python3
"""
forest_search.py -- local search for an independent set P of Q_d with |P| = p such that
the induced subgraph Q_d - P is a forest; then builds the labelling of rung R4:
    labels 1..|A| : the trees of the forest A = V - P, each in BFS order from its root,
    labels |A|+1..2^d : the vertices of P (any order).
Stdlib only, exact integers, deterministic given --seed.

Usage: python3 forest_search.py --d 6 --p 26 --seed S --out Q6.txt [--steps K]
Prints the number of annealing steps used, the forest's component count, and the
predicted number of uphill paths V + |E| (V = number of trees).  The artefact must then
be scored with verify.py (the provided checker); this script does NOT score it.

Cost of a candidate P (fixed size p) =
      (#edges with both ends in P)                      -- independence violations
    + (e(A) - |A| + c(A))                               -- cyclomatic number of Q_d[A]
where A = V - P and c(A) = number of connected components of Q_d[A].  Cost 0 <=> P is
independent and Q_d[A] is a forest.  Moves: swap one vertex of P with one vertex of A.
Metropolis acceptance at temperature T, geometric cooling, restarts until cost 0.
"""
import argparse
import math
import random
import sys


def components(d, inA):
    n = 1 << d
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    e = 0
    for v in range(n):
        if not inA[v]:
            continue
        for j in range(d):
            w = v ^ (1 << j)
            if w > v and inA[w]:
                e += 1
                a, b = find(v), find(w)
                if a != b:
                    parent[a] = b
    comps = len({find(v) for v in range(n) if inA[v]})
    return e, comps


def cost(d, inA):
    n = 1 << d
    bad = 0
    for v in range(n):
        if inA[v]:
            continue
        for j in range(d):
            w = v ^ (1 << j)
            if w > v and not inA[w]:
                bad += 1
    e, c = components(d, inA)
    nA = sum(inA)
    return bad + (e - nA + c)


def search(d, p, rng, steps, T0=2.0, T1=0.05):
    n = 1 << d
    total_steps = 0
    restarts = 0
    while True:
        restarts += 1
        P = rng.sample(range(n), p)
        inA = [True] * n
        for v in P:
            inA[v] = False
        cur = cost(d, inA)
        for t in range(steps):
            total_steps += 1
            if cur == 0:
                return inA, total_steps, restarts
            T = T0 * (T1 / T0) ** (t / steps)
            Plist = [v for v in range(n) if not inA[v]]
            Alist = [v for v in range(n) if inA[v]]
            x = rng.choice(Plist)
            y = rng.choice(Alist)
            inA[x], inA[y] = True, False
            new = cost(d, inA)
            if new <= cur or rng.random() < math.exp((cur - new) / T):
                cur = new
            else:
                inA[x], inA[y] = False, True
        if cur == 0:
            return inA, total_steps, restarts


def build_order(d, inA, rng):
    """Trees of Q_d[A] in BFS order from a root (root chosen at random), then P."""
    n = 1 << d
    seen = [False] * n
    order = []
    Averts = [v for v in range(n) if inA[v]]
    rng.shuffle(Averts)
    ntrees = 0
    for r in Averts:
        if seen[r]:
            continue
        ntrees += 1
        seen[r] = True
        queue = [r]
        k = 0
        while k < len(queue):
            v = queue[k]
            k += 1
            order.append(v)
            for j in range(d):
                w = v ^ (1 << j)
                if inA[w] and not seen[w]:
                    seen[w] = True
                    queue.append(w)
    P = [v for v in range(n) if not inA[v]]
    rng.shuffle(P)
    order.extend(P)
    return order, ntrees


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--d", type=int, default=6)
    ap.add_argument("--p", type=int, default=26)
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--steps", type=int, default=20000)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    rng = random.Random(a.seed)
    inA, used, restarts = search(a.d, a.p, rng, a.steps)
    e, c = components(a.d, inA)
    order, ntrees = build_order(a.d, inA, rng)
    assert ntrees == c
    with open(a.out, "w") as fh:
        for v in order:
            fh.write(format(v, "0%db" % a.d) + "\n")
    E = a.d * (1 << (a.d - 1))
    P = sorted(v for v in range(1 << a.d) if not inA[v])
    print("d=%d p=%d seed=%d steps_used=%d restarts=%d |A|=%d e(A)=%d trees=%d predicted=%d"
          % (a.d, a.p, a.seed, used, restarts, sum(inA), e, c, c + E))
    print("P =", " ".join(format(v, "0%db" % a.d) for v in P))


if __name__ == "__main__":
    main()
