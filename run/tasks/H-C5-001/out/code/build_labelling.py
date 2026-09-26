#!/usr/bin/env python3
"""
build_labelling.py -- turn an independent feedback vertex set S of Q_d into a labelling
(stdlib only, exact integers).

Usage: python3 build_labelling.py S.txt OUT.txt
  S.txt : one d-bit 0/1 string per line (the set S); the string is written exactly as in the
          artefact format (character k of the string = coordinate k).
  OUT   : 2^d lines, line i = vertex with label i  (the hand-in format).

Construction (reduction.md, part (b)):
  F = V \\ S.  Checks: S independent, F induces a forest.  Labels 1..|F| go to F in BFS order
  of each tree of F (so every non-root F-vertex comes after its unique BFS parent), trees one
  after another; labels |F|+1..2^d go to S in any order (here: sorted).
Predicted count: |E| + (#trees of F) = 2^d + (d-1)|S|  (printed; the checker is authoritative).
"""
import sys


def main():
    src, dst = sys.argv[1], sys.argv[2]
    rows = [r.strip() for r in open(src) if r.strip()]
    d = len(rows[0])
    n = 1 << d
    S = set()
    for r in rows:
        assert len(r) == d and set(r) <= set("01"), r
        S.add(int(r, 2))
    assert len(S) == len(rows), "duplicate vertex in S"
    for v in S:
        for j in range(d):
            assert (v ^ (1 << j)) not in S, "S not independent"
    seen = [False] * n
    order = []
    trees = 0
    edgesF = 0
    for r in range(n):
        if r in S or seen[r]:
            continue
        trees += 1
        seen[r] = True
        queue = [r]
        qi = 0
        while qi < len(queue):
            u = queue[qi]; qi += 1
            order.append(u)
            for j in range(d):
                w = u ^ (1 << j)
                if w in S:
                    continue
                if u < w:
                    edgesF += 1
                if not seen[w]:
                    seen[w] = True
                    queue.append(w)
    nF = n - len(S)
    assert len(order) == nF
    # forest test: #edges = #vertices - #components
    assert edgesF == nF - trees, "F = V \\ S contains a cycle (edges %d, vertices %d, trees %d)" % (edgesF, nF, trees)
    order += sorted(S)
    with open(dst, "w") as fh:
        for v in order:
            fh.write(format(v, "0%db" % d) + "\n")
    E = d * n // 2
    print("d=%d |S|=%d |F|=%d trees=%d predicted_uphill=%d (= %d + %d)" %
          (d, len(S), nF, trees, E + trees, E, trees))


if __name__ == "__main__":
    main()
