#!/usr/bin/env python3
"""
construct.py d outfile -- stdlib only.
Labelling of Q_d from an independent decycling set (literature idea: decycling sets of
hypercubes built from distance-4 codes, see out/sources.md).
  S = even-weight vertices with pairwise Hamming distance >= 4 (found by exhaustive
      max-clique search in the "distance >= 4" graph on even vertices; small d only).
  F = odd-weight vertices  +  S   (induces disjoint stars centred at S + isolated odd vertices)
  D = even-weight vertices - S    (independent; every vertex of D is a peak)
Label order: for each s in S: s, then its d neighbours; then the remaining odd vertices;
then D.  Predicted count = d*2^(d-1) + |S| + 2^(d-1) - d*|S|.
"""
import sys

def best_code(d):
    even = [v for v in range(1 << d) if bin(v).count("1") % 2 == 0]
    best = []
    def rec(chosen, cand):
        nonlocal best
        if len(chosen) > len(best):
            best = list(chosen)
        if len(chosen) + len(cand) <= len(best):
            return
        for i, c in enumerate(cand):
            if len(chosen) + len(cand) - i <= len(best):
                return
            rec(chosen + [c], [x for x in cand[i + 1:] if bin(x ^ c).count("1") >= 4])
    rec([0], [x for x in even if bin(x).count("1") >= 4])
    return best

def build(d):
    n = 1 << d
    S = best_code(d)
    order, used = [], set()
    for s in S:
        for v in [s] + [s ^ (1 << j) for j in range(d)]:
            assert v not in used
            order.append(v); used.add(v)
    order += [v for v in range(n) if bin(v).count("1") % 2 == 1 and v not in used]
    used = set(order)
    order += [v for v in range(n) if v not in used]
    assert sorted(order) == list(range(n))
    return S, order

if __name__ == "__main__":
    d = int(sys.argv[1])
    S, order = build(d)
    with open(sys.argv[2], "w") as fh:
        for v in order:
            fh.write(format(v, "0%db" % d) + "\n")
    print("d=%d |S|=%d S=%s predicted=%d" % (d, len(S), [format(s, "0%db" % d) for s in S],
          d * 2 ** (d - 1) + len(S) + 2 ** (d - 1) - d * len(S)))
