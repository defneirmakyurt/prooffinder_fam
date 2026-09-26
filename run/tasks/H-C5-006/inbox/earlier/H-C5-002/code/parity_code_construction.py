#!/usr/bin/env python3
"""
parity_code_construction.py -- stdlib only, deterministic.

Construction ("parity class minus a distance-4 code"):
  E = even-weight vertices of Q_d, O = odd-weight vertices.
  M = a set of even-weight vertices with pairwise Hamming distance >= 4 (a binary
      code of length d, minimum distance 4, all words of even weight).
  F = O u M  induces a forest: two M-words at distance >= 4 have no common neighbour,
      so F is |M| disjoint stars K_{1,d} (centre in M, leaves = its d odd neighbours)
      plus 2^{d-1} - d|M| isolated odd vertices.
  S = E \ M is an independent set (all even).
Labelling: the stars first (centre, then its d leaves), then the isolated odd
vertices, then S.  Every vertex of F has exactly one lower neighbour in F except the
roots (star centres, isolated odd vertices), which are the valleys; every vertex of S
is a local maximum.  Number of uphill paths = |E(Q_d)| + #valleys
                                            = d 2^{d-1} + |M| + 2^{d-1} - d|M|.
With |M| = A(d,4): d=3..9 -> 14, 34, 88, 204, 464, 1040, 2400.

The code M is found by a seeded min-conflicts local search on even-weight words
(target size given on the command line, default = A(d,4) for d <= 9).

Usage: python3 parity_code_construction.py d outfile [target] [seed]
"""
import random
import sys

A_D4 = {1: 1, 2: 1, 3: 1, 4: 2, 5: 2, 6: 4, 7: 8, 8: 16, 9: 20}


def popcount(x):
    return bin(x).count("1")


def find_code(d, target, seed):
    rng = random.Random(seed)
    E = [v for v in range(2 ** d) if popcount(v) % 2 == 0]
    if target == 1:
        return [0]
    # min-conflicts: keep `target` words, minimise number of pairs at distance < 4
    for restart in range(1000):
        code = rng.sample(E, target)
        for it in range(20000):
            conf = [sum(1 for w in code if w != c and popcount(w ^ c) < 4) for c in code]
            tot = sum(conf)
            if tot == 0:
                return sorted(code)
            # pick a conflicting word, move it to the best replacement
            bad = [i for i in range(target) if conf[i] > 0]
            i = rng.choice(bad)
            others = code[:i] + code[i + 1:]
            best, bestc = [], None
            for v in E:
                if v in others:
                    continue
                c = sum(1 for w in others if popcount(w ^ v) < 4)
                if bestc is None or c < bestc:
                    best, bestc = [v], c
                elif c == bestc:
                    best.append(v)
            code[i] = rng.choice(best)
    raise RuntimeError("no code found")


def labelling(d, M):
    n = 2 ** d
    Mset = set(M)
    order, placed = [], set()
    for c in M:                       # stars: centre then its d odd neighbours
        order.append(c)
        placed.add(c)
        for j in range(d):
            w = c ^ (1 << j)
            assert w not in placed, "code distance < 4"
            order.append(w)
            placed.add(w)
    for v in range(n):                # isolated odd vertices (valleys)
        if popcount(v) % 2 == 1 and v not in placed:
            order.append(v)
            placed.add(v)
    for v in range(n):                # S = E \ M, all local maxima
        if popcount(v) % 2 == 0 and v not in Mset:
            order.append(v)
            placed.add(v)
    assert len(order) == n and len(placed) == n
    return order


def main():
    d = int(sys.argv[1])
    out = sys.argv[2]
    target = int(sys.argv[3]) if len(sys.argv) > 3 else A_D4[d]
    seed = int(sys.argv[4]) if len(sys.argv) > 4 else 1
    M = find_code(d, target, seed)
    order = labelling(d, M)
    with open(out, "w") as fh:
        for v in order:
            fh.write(format(v, "0%db" % d) + "\n")
    pred = d * 2 ** (d - 1) + len(M) + 2 ** (d - 1) - d * len(M)
    print("d=%d |M|=%d predicted=%d code=%s" % (d, len(M), pred,
          " ".join(format(c, "0%db" % d) for c in M)))


if __name__ == "__main__":
    main()
