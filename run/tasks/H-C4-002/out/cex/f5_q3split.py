#!/usr/bin/env python3
"""Referee's independent computation of F_4 and an upper bound on F_5 (stdlib, exact).
Different decomposition from the subject: Q_5 = Q_3 x Q_2. Vertex v in 0..31, low 3 bits = Q_3
coordinate x, high 2 bits = block b in {0,1,2,3}. Block b induces a copy of Q_3 (flip one of the low
3 bits), so T ∩ block_b is an induced forest of Q_3 (induced subgraph of a forest), and
|T| = sum_b |T_b|. Enumerate ALL induced forests of Q_3 (all 256 subsets tested), then ALL ordered
4-tuples (T_0..T_3) with sum of sizes >= 19, and test acyclicity of Q_5[T] directly (DFS: forest iff
#edges = #vertices - #components; no pre-filter). If none is acyclic, F_5 <= 18.
Also: F_1..F_4 by testing all subsets with the same acyclicity test, and a witness of size 18."""
import itertools, time

def is_forest(mask, d):
    n = 1 << d
    verts = [v for v in range(n) if mask >> v & 1]
    e = 0
    for v in verts:
        for j in range(d):
            w = v ^ (1 << j)
            if w > v and mask >> w & 1:
                e += 1
    seen = 0; comps = 0
    for r in verts:
        if seen >> r & 1: continue
        comps += 1; seen |= 1 << r; st = [r]
        while st:
            x = st.pop()
            for j in range(d):
                w = x ^ (1 << j)
                if mask >> w & 1 and not seen >> w & 1:
                    seen |= 1 << w; st.append(w)
    return e == len(verts) - comps

t0 = time.time()
for d in range(1, 5):
    F = max(bin(m).count('1') for m in range(1 << (1 << d)) if is_forest(m, d))
    print("F_%d = %d (all %d subsets)" % (d, F, 1 << (1 << d)))
q3 = [m for m in range(256) if is_forest(m, 3)]
bys = {}
for m in q3:
    bys.setdefault(bin(m).count('1'), []).append(m)
print("Q_3 induced forests by size:", {k: len(v) for k, v in sorted(bys.items())})
F3 = max(bys)
for target in (20, 19):
    tested = 0; hits = 0
    for sizes in itertools.product(range(F3 + 1), repeat=4):
        if sum(sizes) != target: continue
        for combo in itertools.product(*(bys[s] for s in sizes)):
            mask = combo[0] | combo[1] << 8 | combo[2] << 16 | combo[3] << 24
            tested += 1
            if is_forest(mask, 5):
                hits += 1
    print("sum=%d: 4-tuples tested=%d acyclic=%d" % (target, tested, hits))
# witness of size 18 (lower bound, not needed for the proof)
wit = None
for sizes in itertools.product(range(F3 + 1), repeat=4):
    if sum(sizes) != 18 or wit: continue
    for combo in itertools.product(*(bys[s] for s in sizes)):
        mask = combo[0] | combo[1] << 8 | combo[2] << 16 | combo[3] << 24
        if is_forest(mask, 5):
            wit = mask; break
print("size-18 induced forest witness mask =", hex(wit) if wit else None)
print("elapsed %.1f s" % (time.time() - t0))
