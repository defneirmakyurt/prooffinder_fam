#!/usr/bin/env python3
"""build_labelling.py -- stdlib only. From an induced forest F of Q_d (file: one line of 2^d chars, char v = '1'
iff vertex v in F) build a labelling: every component of F in BFS order from its smallest vertex, components one
after another; then the vertices of S = V \\ F, component of Q_d[S] by component, each S-component in the order
minimising sum of N over it (all orders if the component has <= 8 vertices, else greedy + random restarts).
Writes the labelling (line i = 0/1 string of the vertex with label i, most significant bit first = bit d-1)
and prints the exact number of uphill paths computed by the same recursion as the checker
(the reported score must still come from inbox/checker/verify.py).
Usage: build_labelling.py forest.txt out.txt [seed]
"""
import sys, itertools, random

fn, outfn = sys.argv[1], sys.argv[2]
seed = int(sys.argv[3]) if len(sys.argv) > 3 else 0
random.seed(seed)
s = open(fn).read().strip()
n = len(s); d = n.bit_length() - 1
assert 1 << d == n
inF = [c == '1' for c in s]
nb = lambda v: [v ^ (1 << j) for j in range(d)]

order = []
seen = [False] * n
for r in range(n):
    if inF[r] and not seen[r]:
        seen[r] = True; q = [r]; h = 0
        while h < len(q):
            v = q[h]; h += 1; order.append(v)
            for w in nb(v):
                if inF[w] and not seen[w]:
                    seen[w] = True; q.append(w)
degF = [sum(1 for w in nb(v) if inF[w]) for v in range(n)]

def cost(seq):
    """sum of N over seq, placed after all of F (N = 1 on F), in this order"""
    pos = {v: i for i, v in enumerate(seq)}
    N = {}
    tot = 0
    for v in seq:
        low = [w for w in nb(v) if w in pos and pos[w] < pos[v]]
        x = degF[v] + sum(N[w] for w in low)
        if x == 0: x = 1  # valley (no lower neighbour at all)
        N[v] = x; tot += x
    return tot

for r in range(n):
    if not inF[r] and not seen[r]:
        comp = []; seen[r] = True; q = [r]; h = 0
        while h < len(q):
            v = q[h]; h += 1; comp.append(v)
            for w in nb(v):
                if not inF[w] and not seen[w]:
                    seen[w] = True; q.append(w)
        if len(comp) <= 8:
            best = min(itertools.permutations(comp), key=cost)
        else:
            best = None; bc = None
            for rep in range(200):
                # greedy: repeatedly place the vertex with the smallest current N (random tie-break)
                rem = set(comp); seq = []; Ncur = {}
                while rem:
                    cand = []
                    for v in rem:
                        x = degF[v] + sum(Ncur[w] for w in nb(v) if w in Ncur)
                        cand.append((x, random.random(), v))
                    cand.sort(); v = cand[0][2] if rep else cand[0][2]
                    if rep and random.random() < 0.2 and len(cand) > 1: v = cand[1][2]
                    x = degF[v] + sum(Ncur[w] for w in nb(v) if w in Ncur)
                    Ncur[v] = x if x else 1; seq.append(v); rem.discard(v)
                c = cost(seq)
                if bc is None or c < bc: bc, best = c, seq
        order.extend(best)
assert sorted(order) == list(range(n))

lab = [0] * n
for i, v in enumerate(order): lab[v] = i
N = [0] * n; tot = 0
for v in order:
    low = [w for w in nb(v) if lab[w] < lab[v]]
    N[v] = (0 if low else 1) + sum(N[w] for w in low); tot += N[v]
with open(outfn, 'w') as fo:
    for v in order:
        fo.write(format(v, '0%db' % d) + '\n')
print('built labelling: |F|=%d |S|=%d uphill paths (internal count) = %d' % (sum(inF), n - sum(inF), tot))
