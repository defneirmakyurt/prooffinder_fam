#!/usr/bin/env python3
"""Scribe-side re-count (stdlib only). Not part of the submission.
Counts uphill paths of a labelling file of Q_d directly from the definition:
every sequence (v_1..v_k), k >= 1, v_1 a valley, consecutive vertices adjacent,
labels strictly increasing. Enumerates all such sequences by depth-first search.
Also reports the block structure claimed for Q9.txt (20 stars, 76 odd, 236 even).
Usage: python3 count_uphill.py FILE
"""
import sys

def main(path):
    with open(path) as fh:
        lines = fh.read().split("\n")
    if lines and lines[-1] == "":
        lines.pop()
    d = len(lines[0])
    n = 1 << d
    ok = (len(lines) == n and all(len(s) == d and set(s) <= {"0", "1"} for s in lines)
          and len(set(lines)) == n)
    print("FORMAT", "OK" if ok else "BAD", "lines=%d d=%d distinct=%d" % (len(lines), d, len(set(lines))))
    if not ok:
        return 1
    verts = [int(s, 2) for s in lines]
    f = {v: i + 1 for i, v in enumerate(verts)}          # label of vertex
    nbrs = {v: [v ^ (1 << j) for j in range(d)] for v in verts}
    valleys = [v for v in verts if all(f[w] > f[v] for w in nbrs[v])]
    count = 0
    stack = list(valleys)                                  # each stack item = end of a path
    while stack:
        v = stack.pop()
        count += 1                                         # the path ending here
        for w in nbrs[v]:
            if f[w] > f[v]:
                stack.append(w)
    print("VALLEYS", len(valleys))
    print("UPHILL_PATHS", count)
    # structure claimed in the artefact: [20 x (code word m, its 9 neighbours)] + 76 odd + 236 even
    if d == 9:
        wt = lambda v: bin(v).count("1") % 2
        stars = all(wt(verts[10 * k]) == 0 and set(verts[10 * k + 1:10 * k + 10]) == set(nbrs[verts[10 * k]])
                    for k in range(20))
        odd76 = all(wt(v) == 1 for v in verts[200:276])
        even236 = all(wt(v) == 0 for v in verts[276:512])
        print("STRUCTURE stars20=%s odd76=%s even236=%s" % (stars, odd76, even236))
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
