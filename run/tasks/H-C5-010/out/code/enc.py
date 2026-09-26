#!/usr/bin/env python3
"""
enc.py -- CNF encoder for "Q_d has an induced forest T with |T| >= m" (implied constraints only).

Variables 1..2^d: x_{v+1} true <=> vertex v (bitmask of its 0/1 string, bit j = coordinate j+1) in T.
Constraints (each one is satisfied by EVERY induced forest of Q_d, see proof.md section 2):
  (K)  subcube bounds: every k-dim subcube (k in KSET) holds at most FB[k] vertices of T,
       with FB = {1:2, 2:3, 3:5, 4:10, 5:18, 6:36, 7:72, 8:144}.  Encoded by a shared unary
       counter hierarchy (totalizer): counter(Q) for a k-subcube Q is the merge of the counters of
       its two (k-1)-halves along its highest free coordinate; only the direction
       "at least j of Q in T  =>  o_{Q,j}" is encoded, and  NOT o_{Q,FB[k]+1}  is asserted.
  (G)  global:  sum_v x_v >= m   (pysat CardEnc, totalizer on negated literals).
  (C)  cycle clauses: for a cycle C of Q_d (given as vertex list), clause OR_{v in C} NOT x_v.
       The 4-cycle clauses are exactly the k=2 subcube bounds (at most 3 of 4).
stdlib + pysat (pysat only for the global cardinality encoding).
"""
from itertools import combinations


FB = {0: 1, 1: 2, 2: 3, 3: 5, 4: 10, 5: 18, 6: 36, 7: 72, 8: 144}


class Pool:
    def __init__(self, start):
        self.top = start

    def new(self):
        self.top += 1
        return self.top


def subcubes(d, k):
    """All k-dim subcubes of Q_d as (freemask, base) with base & freemask == 0."""
    n = 1 << d
    out = []
    for coords in combinations(range(d), k):
        fm = 0
        for c in coords:
            fm |= 1 << c
        for b in range(n):
            if b & fm == 0:
                out.append((fm, b))
    return out


def build_subcube_counters(d, kset, pool, clauses, fb=FB):
    """Hierarchical totalizer.  cnt[(fm, b)] = list o[1..cap] (o[0] unused) where
    o[j] is implied by 'at least j vertices of the subcube in T'.  cap = fb[k]+1 for
    k in kset (and we assert NOT o[cap]); for k not in kset but needed as intermediate,
    cap = fb[k] + 1 as well (the bound fb[k] is still valid, and we assert it too if the
    subcube level is in kset; otherwise counts above fb[k]+1 are simply not tracked -- see
    note below)."""
    kmax = max(kset)
    cnt = {}
    # level 0: single vertices
    for v in range(1 << d):
        cnt[(0, v)] = [None, v + 1]
    for k in range(1, kmax + 1):
        cap = fb[k] + 1
        for (fm, b) in subcubes(d, k):
            hi = fm.bit_length() - 1
            sub = fm & ~(1 << hi)
            A = cnt[(sub, b)]
            B = cnt[(sub, b | (1 << hi))]
            la, lb = len(A) - 1, len(B) - 1
            top = min(la + lb, cap)
            o = [None] + [pool.new() for _ in range(top)]
            for i in range(0, la + 1):
                for j in range(0, lb + 1):
                    s = i + j
                    if s == 0:
                        continue
                    s = min(s, top)
                    lits = []
                    if i > 0:
                        lits.append(-A[i])
                    if j > 0:
                        lits.append(-B[j])
                    clauses.append(lits + [o[s]])
            cnt[(fm, b)] = o
            if k in kset and top >= cap:
                clauses.append([-o[cap]])
    return cnt


def global_atleast(d, m, pool, clauses, enc="totalizer"):
    """sum x_v >= m, via pysat CardEnc (auxiliary variables above pool.top)."""
    from pysat.card import CardEnc, EncType
    lits = [v + 1 for v in range(1 << d)]
    et = {"totalizer": EncType.totalizer, "seqcounter": EncType.seqcounter,
          "cardnetwrk": EncType.cardnetwrk, "sortnetwrk": EncType.sortnetwrk,
          "kmtotalizer": EncType.kmtotalizer, "mtotalizer": EncType.mtotalizer}[enc]
    cnf = CardEnc.atleast(lits=lits, bound=m, top_id=pool.top, encoding=et)
    for c in cnf.clauses:
        for l in c:
            if abs(l) > pool.top:
                pool.top = abs(l)
        clauses.append(list(c))


def adj(d, v):
    return [v ^ (1 << j) for j in range(d)]


def shortest_cycles(d, T):
    """For the induced subgraph Q_d[T] (T a set of ints): return a list of induced cycles
    (vertex lists), one shortest cycle through each non-tree edge of a BFS forest.
    Returns [] iff Q_d[T] is acyclic."""
    from collections import deque
    parent = {}
    order = []
    for r in sorted(T):
        if r in parent:
            continue
        parent[r] = None
        dq = deque([r])
        while dq:
            u = dq.popleft()
            order.append(u)
            for w in adj(d, u):
                if w in T and w not in parent:
                    parent[w] = u
                    dq.append(w)
    cycles = []
    seen = set()
    for u in order:
        for w in adj(d, u):
            if w in T and u < w and parent.get(u) != w and parent.get(w) != u:
                # non-tree edge u-w: shortest u..w path in T avoiding edge (u,w)
                prev = {u: None}
                dq = deque([u])
                found = False
                while dq and not found:
                    a = dq.popleft()
                    for b in adj(d, a):
                        if b in T and b not in prev and not (a == u and b == w):
                            prev[b] = a
                            if b == w:
                                found = True
                                break
                            dq.append(b)
                path = [w]
                while path[-1] != u:
                    path.append(prev[path[-1]])
                key = frozenset(path)
                if key not in seen:
                    seen.add(key)
                    cycles.append(path)
    return cycles


def is_cycle_of_Qd(d, cyc):
    """Exact check that cyc is a cycle of Q_d: >= 4 distinct vertices, consecutive
    (cyclically) ones differ in exactly one coordinate."""
    if len(cyc) < 4 or len(set(cyc)) != len(cyc):
        return False
    n = 1 << d
    for i in range(len(cyc)):
        a, b = cyc[i], cyc[(i + 1) % len(cyc)]
        if not (0 <= a < n and 0 <= b < n):
            return False
        x = a ^ b
        if x == 0 or x & (x - 1):
            return False
    return True


def global_atleast_stdlib(d, m, pool, clauses):
    """sum_v x_v >= m, stdlib totalizer on the negated literals y_v = NOT x_v:
    sum_v y_v <= K := 2^d - m.  Tree = the subcube hierarchy along coordinates 0..d-1
    (node at level k = subcube with free coordinates 0..k-1).  Each node carries outputs
    p[1..cap], cap = min(size, K+1), with clauses encoding 'at least j of the y's in the node
    => p[j]' (p[j] for j = cap also covers every count >= cap), and NOT p[K+1] is asserted at the
    root.  Validity: set p_{Q,j} := [#(non-T vertices of Q) >= j]; every clause holds (proof.md 2.3)."""
    n = 1 << d
    K = n - m
    if K < 0:
        clauses.append([])
        return
    cap_all = K + 1
    cur = {v: [None, -(v + 1)] for v in range(n)}   # level 0: p[1] = y_v = NOT x_v
    for k in range(1, d + 1):
        nxt = {}
        step = 1 << (k - 1)
        for b in range(0, n, 1 << k):
            A, B = cur[b], cur[b + step]
            la, lb = len(A) - 1, len(B) - 1
            top = min(la + lb, cap_all)
            o = [None] + [pool.new() for _ in range(top)]
            for i in range(0, la + 1):
                for j in range(0, lb + 1):
                    s = i + j
                    if s == 0:
                        continue
                    s = min(s, top)
                    lits = []
                    if i > 0:
                        lits.append(-A[i])
                    if j > 0:
                        lits.append(-B[j])
                    clauses.append(lits + [o[s]])
            nxt[b] = o
        cur = nxt
    root = cur[0]
    if len(root) - 1 >= K + 1:
        clauses.append([-root[K + 1]])


def write_dimacs(path, nvars, clauses):
    with open(path, "w") as f:
        f.write("p cnf %d %d\n" % (nvars, len(clauses)))
        for c in clauses:
            f.write(" ".join(map(str, c)) + " 0\n")
