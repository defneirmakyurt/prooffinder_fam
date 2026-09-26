#!/usr/bin/env python3
"""build_labelling.py -- from an induced forest F of Q_d (one line of 2^d chars, '1' = in F) build a labelling:
  1. the vertices of F, component by component, each component in BFS order from a root (so every non-root
     vertex of F has exactly one lower neighbour, its BFS parent; roots are valleys);
  2. the vertices of S = V \\ F: for each connected component C of G[S], the order of C minimising
     sum_{u in C} (N(u)-2) up(u) (all |C|! orders if |C| <= 7, otherwise the best of 20000 random orders),
     components one after another.
Writes the labelling (line i = vertex with label i, d-character 0/1 string) and prints |S|, e(S), the
internal count (same recursion as the checker). The score that counts is inbox/checker/verify.py's.
Usage: build_labelling.py forest_file out_labelling [seed]"""
import sys, random, itertools
from collections import deque


def main():
    s = open(sys.argv[1]).read().split()[0]
    out = sys.argv[2]
    rng = random.Random(int(sys.argv[3]) if len(sys.argv) > 3 else 0)
    n = len(s)
    d = n.bit_length() - 1
    F = [c == "1" for c in s]
    nb = [[v ^ (1 << j) for j in range(d)] for v in range(n)]
    order = []
    seen = [False] * n
    roots = [v for v in range(n) if F[v]]
    rng.shuffle(roots)
    for r in roots:
        if seen[r]:
            continue
        seen[r] = True
        q = deque([r])
        while q:
            v = q.popleft()
            order.append(v)
            for w in nb[v]:
                if F[w] and not seen[w]:
                    seen[w] = True
                    q.append(w)
    fdeg = [sum(1 for w in nb[v] if F[w]) for v in range(n)]
    Sset = [v for v in range(n) if not F[v]]
    comp = {}
    comps = []
    for v in Sset:
        if v in comp:
            continue
        c = [v]
        comp[v] = len(comps)
        k = 0
        while k < len(c):
            x = c[k]; k += 1
            for w in nb[x]:
                if not F[w] and w not in comp:
                    comp[w] = len(comps)
                    c.append(w)
        comps.append(c)

    def cost(seq):
        N = {}
        tot = 0
        pos = {v: i for i, v in enumerate(seq)}
        for v in seq:
            N[v] = fdeg[v] + sum(N[w] for w in nb[v] if w in pos and pos[w] < pos[v])
        for v in seq:
            up = sum(1 for w in nb[v] if w in pos and pos[w] > pos[v])
            tot += (N[v] - 2) * up
        return tot
    extra = 0
    eS = 0
    for c in comps:
        eS += sum(1 for v in c for w in nb[v] if w in comp and w > v)
        if len(c) == 1:
            order.append(c[0]); continue
        if len(c) <= 7:
            best = min(itertools.permutations(c), key=cost)
        else:
            best, bc = None, None
            for _ in range(20000):
                p = list(c); rng.shuffle(p)
                cc = cost(p)
                if bc is None or cc < bc:
                    best, bc = p, cc
        extra += cost(best)
        order.extend(best)
    assert sorted(order) == list(range(n))
    lab = [0] * n
    for i, v in enumerate(order):
        lab[v] = i
    Nn = [0] * n
    P = 0
    for v in order:
        low = [w for w in nb[v] if lab[w] < lab[v]]
        Nn[v] = sum(Nn[w] for w in low) + (0 if low else 1)
        P += Nn[v]
    with open(out, "w") as fh:
        for v in order:
            fh.write(format(v, "0%db" % d) + "\n")
    print("|F|=%d |S|=%d e(S)=%d S-components>1: %d extra=%d internal count=%d (512+8|S|+extra=%d)"
          % (n - len(Sset), len(Sset), eS, sum(1 for c in comps if len(c) > 1), extra, P,
             n + (d - 1) * len(Sset) + extra))


if __name__ == "__main__":
    main()
