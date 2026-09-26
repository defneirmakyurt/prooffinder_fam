#!/usr/bin/env python3
"""
decode.py -- turn an induced forest T of Q_9 into a labelling (stdlib only).
Usage: decode.py forest.txt out_labelling.txt
forest.txt: one 9-character 0/1 string per line (the vertices of T).
Order: each tree of Q_9[T] in BFS order from its smallest vertex (trees one after another), then
the vertices of S = V \\ T, in the order (number of S-neighbours, vertex) ascending.
The count printed is only a convenience; the score that counts is inbox/checker/verify.py.
"""
import sys

D = 9


def main():
    T = [int(l.strip(), 2) for l in open(sys.argv[1]) if l.strip()]
    Ts = set(T)
    assert len(Ts) == len(T)
    order, seen = [], set()
    for s in sorted(Ts):
        if s in seen:
            continue
        seen.add(s)
        q = [s]
        for v in q:
            order.append(v)
            for i in range(D):
                w = v ^ (1 << i)
                if w in Ts and w not in seen:
                    seen.add(w)
                    q.append(w)
    S = [v for v in range(1 << D) if v not in Ts]
    sdeg = {v: sum(1 for i in range(D) if (v ^ (1 << i)) not in Ts) for v in S}
    order += sorted(S, key=lambda v: (sdeg[v], v))
    assert sorted(order) == list(range(1 << D))
    # convenience count (same recurrence as the checker)
    f = {v: i for i, v in enumerate(order)}
    N = {}
    tot = 0
    for v in order:
        low = [v ^ (1 << i) for i in range(D) if f[v ^ (1 << i)] < f[v]]
        N[v] = (1 if not low else 0) + sum(N[w] for w in low)
        tot += N[v]
    with open(sys.argv[2], "w") as fh:
        fh.write("\n".join(format(v, "09b") for v in order) + "\n")
    print("|T|=%d |S|=%d e(S)=%d count=%d" % (len(T), len(S), sum(sdeg.values()) // 2, tot))


if __name__ == "__main__":
    main()
