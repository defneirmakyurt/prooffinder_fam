#!/usr/bin/env python3
"""forest_to_labelling.py -- stdlib only, exact integers.  H-C5-003.

Input : a file with one line of 2^d chars; char v = '1' iff vertex v (binary of v, MSB first = the
        0/1 string written by format(v, '0{d}b')) is in the induced forest F.
Output: a labelling file (line i = vertex with label i) written to argv[2].

Order: (1) every component of F in BFS order from a root (so every non-root forest vertex has exactly
one lower neighbour, its BFS parent, and N = 1 on F); roots are chosen as the component vertex listed
first.  (2) then S = V minus F, greedily: repeatedly place the unplaced S-vertex with the smallest current
N (= sum of N over already placed neighbours), ties broken by more unplaced S-neighbours first, then by
vertex index.  This is only a heuristic ordering; the score that counts is the checker's.
Also prints |F|, |S|, e(S), components, and the internally computed path count (same recursion as the
checker) for information.
"""
import sys


def main():
    s = open(sys.argv[1]).read().strip()
    n = len(s)
    d = n.bit_length() - 1
    assert 2 ** d == n
    F = [c == "1" for c in s]
    placed = [False] * n
    order = []
    comps = 0
    for r in range(n):
        if F[r] and not placed[r]:
            comps += 1
            placed[r] = True
            q = [r]
            h = 0
            while h < len(q):
                v = q[h]
                h += 1
                order.append(v)
                for j in range(d):
                    w = v ^ (1 << j)
                    if F[w] and not placed[w]:
                        placed[w] = True
                        q.append(w)
    # N on F (BFS order => every non-root has exactly one earlier neighbour; verified below)
    lab = {}
    for i, v in enumerate(order):
        lab[v] = i
    N = [0] * n
    for v in order:
        lower = [v ^ (1 << j) for j in range(d) if (v ^ (1 << j)) in lab and lab[v ^ (1 << j)] < lab[v]]
        N[v] = 1 if not lower else sum(N[w] for w in lower)
    S = [v for v in range(n) if not F[v]]
    Sset = set(S)
    remaining = set(S)
    while remaining:
        best = None
        for u in remaining:
            cur = sum(N[u ^ (1 << j)] for j in range(d) if (u ^ (1 << j)) in lab)
            freeS = sum(1 for j in range(d) if (u ^ (1 << j)) in remaining)
            key = (cur, -freeS, u)
            if best is None or key < best[0]:
                best = (key, u)
        u = best[1]
        remaining.discard(u)
        lab[u] = len(order)
        order.append(u)
        lower = [u ^ (1 << j) for j in range(d) if (u ^ (1 << j)) in lab and lab[u ^ (1 << j)] < lab[u]]
        N[u] = 1 if not lower else sum(N[w] for w in lower)
    eS = sum(1 for v in S for j in range(d) if (v ^ (1 << j)) > v and (v ^ (1 << j)) in Sset)
    total = sum(N)
    with open(sys.argv[2], "w") as fo:
        for v in order:
            fo.write(format(v, "0%db" % d) + "\n")
    print("|F|=%d |S|=%d e(S)=%d components=%d internal_count=%d" % (n - len(S), len(S), eS, comps, total))


if __name__ == "__main__":
    main()
