#!/usr/bin/env python3
"""Independent recount (referee): enumerate every uphill path of a labelling EXPLICITLY by DFS
(sequence by sequence, no DP), directly from the statement's definitions.  Stdlib, exact.
Also validates the artefact format (2^d lines, d-char 0/1 strings, bijection)."""
import sys
def load(fn):
    rows = open(fn, 'rb').read().decode('ascii').split('\n')
    if rows and rows[-1] == '': rows = rows[:-1]
    d = len(rows[0])
    assert all(len(r) == d and set(r) <= set('01') for r in rows), "bad row"
    assert len(rows) == 2 ** d, "wrong number of lines"
    assert len(set(rows)) == 2 ** d, "not a bijection"
    return d, rows
def main(fn):
    d, rows = load(fn)
    f = {r: i + 1 for i, r in enumerate(rows)}        # label = 1-based line number
    def nbrs(v):
        return [v[:j] + ('1' if v[j] == '0' else '0') + v[j+1:] for j in range(d)]
    # valley: every neighbour has larger label (Q_d, d>=1, has no isolated vertex)
    valleys = [v for v in rows if all(f[w] > f[v] for w in nbrs(v))]
    count = 0; longest = 0
    stack = [(v, 1) for v in valleys]                 # each stack item = one uphill path (its last vertex, length)
    while stack:
        v, k = stack.pop()
        count += 1; longest = max(longest, k)
        for w in nbrs(v):
            if f[w] > f[v]:
                stack.append((w, k + 1))
    print("%s: d=%d valleys=%d uphill paths (explicit enumeration)=%d longest=%d" % (fn, d, len(valleys), count, longest))
for fn in sys.argv[1:]:
    main(fn)
