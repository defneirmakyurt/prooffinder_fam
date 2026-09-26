#!/usr/bin/env python3
"""Referee's independent computation of F_d = max size of an induced forest of Q_d, d <= 5.
Different method from the subject's lb_forest.py:
  * acyclicity test = (#edges == #vertices - #components), components by iterative DFS
    (the subject uses union-find cycle detection);
  * F_1..F_4 by brute force over all subsets;
  * Q_5 is split by its two LOWEST bits (c = v & 3) into FOUR copies of Q_3 (coordinates = bits 2,3,4)
    (the subject splits by the highest bit into two copies of Q_4).
Soundness of the Q_5 search: if T is an induced forest of Q_5, then for each c in {0,1,2,3},
A_c = {y in {0,1}^3 : 4y + c in T} induces a subgraph of Q_5[T] isomorphic (via y -> 4y+c) to
Q_3[A_c]; so each A_c is an induced forest of Q_3, |A_c| <= F_3, and |T| = sum |A_c|.
Moreover for adjacent copies c, c' (c xor c' in {1,2}) the set A_c x {c} u A_c' x {c'} induces a
subgraph of Q_5[T] isomorphic to an induced subgraph of Q_3 x K_2 = Q_4, hence acyclic; this is the
only pruning used (hereditary property).  Every quadruple (A_0..A_3) of Q_3-forests with sum >= 19
that survives pruning is tested for acyclicity in Q_5 directly.  If none is acyclic, F_5 <= 18.
"""
import itertools, time

def is_forest(S, d):
    """S: set of ints (vertices of Q_d).  Forest iff |E| = |V| - #components."""
    S = set(S)
    E = sum(1 for v in S for j in range(d) if (v ^ (1 << j)) in S) // 2
    seen = set(); comps = 0
    for r in S:
        if r in seen: continue
        comps += 1; seen.add(r); st = [r]
        while st:
            v = st.pop()
            for j in range(d):
                w = v ^ (1 << j)
                if w in S and w not in seen:
                    seen.add(w); st.append(w)
    return E == len(S) - comps

def F_brute(d):
    n = 1 << d; best = 0; arg = None
    for mask in range(1 << n):
        S = [v for v in range(n) if mask >> v & 1]
        if len(S) > best and is_forest(S, d):
            best = len(S); arg = S
    return best, arg

t0 = time.time()
for d in (1, 2, 3):
    print("F_%d = %d (brute force, all %d subsets)" % (d, F_brute(d)[0], 1 << (1 << d)))
F4, w4 = F_brute(4)
print("F_4 = %d (brute force, all 65536 subsets), witness %s" % (F4, w4))

# Q_3 forests by size
q3 = {}
for mask in range(256):
    S = frozenset(v for v in range(8) if mask >> v & 1)
    if is_forest(S, 3):
        q3.setdefault(len(S), []).append(S)
F3 = max(q3)
print("Q_3 forests by size:", {k: len(q3[k]) for k in sorted(q3)})

def emb(A, c):  # embed Q_3 vertex y into copy c of Q_5: v = 4y + c
    return {4 * y + c for y in A}

# pair compatibility across one Q_5 direction inside {0,1,2,3} (bit 0 or bit 1):
# A in copy 0, B in copy 1 (differ in bit 0).  Isomorphic for any adjacent pair of copies.
compat_cache = {}
def compat(A, B):
    key = (A, B)
    if key not in compat_cache:
        compat_cache[key] = is_forest(emb(A, 0) | emb(B, 1), 5)
    return compat_cache[key]

def search(total):
    """all quadruples of Q_3-forests with sizes summing to `total` (each <= F3)."""
    tested = 0; pruned = 0; hits = []
    for sizes in itertools.product(range(F3 + 1), repeat=4):
        if sum(sizes) != total: continue
        L = [q3.get(s, []) for s in sizes]
        # copies 0,1,2,3; adjacency of copies: 0-1, 0-2, 1-3, 2-3
        for A0 in L[0]:
            for A1 in L[1]:
                if not compat(A0, A1): pruned += 1; continue
                for A2 in L[2]:
                    if not compat(A0, A2): pruned += 1; continue
                    for A3 in L[3]:
                        if not (compat(A1, A3) and compat(A2, A3)): pruned += 1; continue
                        tested += 1
                        T = emb(A0, 0) | emb(A1, 1) | emb(A2, 2) | emb(A3, 3)
                        assert len(T) == total
                        if is_forest(T, 5):
                            hits.append(sorted(T))
                            return tested, pruned, hits
    return tested, pruned, hits

for m in range(4 * F3, 17, -1):
    tested, pruned, hits = search(m)
    print("Q_5, |T| = %d: quadruples fully tested = %d, pruned = %d, acyclic found = %s"
          % (m, tested, pruned, hits[0] if hits else "NONE"))
    if hits:
        break
print("elapsed %.2f s" % (time.time() - t0))
