#!/usr/bin/env python3
"""
lb_forest.py -- exact, exhaustive computation of F_4 and F_5, where
    F_d = maximum number of vertices of an induced forest (acyclic induced subgraph) of Q_d.
Python standard library only; exact integer/bitmask arithmetic.

Method.
  Step 1 (exhaustive over all 2^16 subsets of V(Q_4)): test each subset for acyclicity of
          its induced subgraph with union-find; F_4 = max size; keep all forests with
          their sizes and component counts.
  Step 2 (exhaustive over all pairs of Q_4-forests): split V(Q_5) = {0,1}^5 by the last
          coordinate into two copies of Q_4 (vertex x0 and x1, x in {0,1}^4).  If T is an
          induced forest of Q_5 then T0 = {x : x0 in T} and T1 = {x : x1 in T} are induced
          forests of Q_4 (induced subgraphs of a forest are forests), and
          |T| = |T0| + |T1|.  So every induced forest of Q_5 with >= m vertices arises from a
          pair (T0, T1) of Q_4-forests with |T0| + |T1| >= m.  For every such pair we test
          whether the induced subgraph of Q_5 on T0 x {0} u T1 x {1} is acyclic:
          first the necessary edge count  e = e(T0) + e(T1) + |T0 & T1| <= |T| - 1,
          then (if that passes) a full union-find check.
  Output: F_1..F_4 (exhaustive over all subsets), F_5 and the number of pairs examined.
"""
import sys
import time


def forest_info(mask, nv, d):
    """Return (is_forest, #vertices, #edges, #components) of the subgraph of Q_d induced
    on the vertex set encoded by bitmask `mask` (bit x set <=> vertex x in the set)."""
    par = list(range(nv))

    def find(x):
        while par[x] != x:
            par[x] = par[par[x]]
            x = par[x]
        return x

    t = 0
    e = 0
    comps = 0
    forest = True
    for v in range(nv):
        if not (mask >> v) & 1:
            continue
        t += 1
        comps += 1
        for j in range(d):
            w = v ^ (1 << j)
            if w < v and (mask >> w) & 1:
                e += 1
                a, b = find(v), find(w)
                if a == b:
                    forest = False
                else:
                    par[a] = b
                    comps -= 1
    return forest, t, e, comps


def main():
    t0 = time.time()
    for dd in (1, 2, 3):  # by-product: F_1, F_2, F_3 exhaustively over all subsets
        nn = 1 << dd
        print("Q_%d: F_%d = %d (exhaustive over all %d subsets)" % (dd, dd, max(
            bin(m).count("1") for m in range(1 << nn) if forest_info(m, nn, dd)[0]), 1 << nn))
    d4, n4 = 4, 16
    forests = []  # (mask, size, edges)
    for mask in range(1 << n4):
        ok, t, e, c = forest_info(mask, n4, d4)
        if ok:
            forests.append((mask, t, e))
    F4 = max(t for (_, t, _) in forests)
    by_size = {}
    for (m, t, e) in forests:
        by_size.setdefault(t, []).append((m, e))
    print("Q_4: %d induced forests (incl. empty); F_4 = %d; counts by size >= 7: %s"
          % (len(forests), F4, {k: len(by_size[k]) for k in sorted(by_size) if k >= 7}))

    # Step 2: Q_5.  Vertex of Q_5 = x + 16*b (b = last coordinate); x0 ~ x1 matching edges.
    best = F4  # T0 alone is a forest of Q_5 (T1 empty), so F_5 >= F_4
    target = int(sys.argv[1]) if len(sys.argv) > 1 else None
    # we look for the largest m such that some pair with |T0|+|T1| = m is acyclic
    pairs = 0
    passed_edge = 0
    found_at = {}
    for m in range(2 * F4, F4, -1):
        hit = None
        for s0 in range(max(0, m - F4), min(F4, m) + 1):
            s1 = m - s0
            for (m0, e0) in by_size.get(s0, []):
                for (m1, e1) in by_size.get(s1, []):
                    pairs += 1
                    inter = bin(m0 & m1).count("1")
                    if e0 + e1 + inter > m - 1:
                        continue
                    passed_edge += 1
                    ok, t, e, c = forest_info(m0 | (m1 << 16), 32, 5)
                    if ok:
                        hit = (m0, m1)
                        break
                if hit:
                    break
            if hit:
                break
        found_at[m] = hit
        if hit:
            best = m
            break
        print("Q_5: no induced forest with %d vertices (all pairs of Q_4-forests with |T0|+|T1| = %d rejected)"
              % (m, m))
    print("Q_5: F_5 = %d; witness T0=%s T1=%s" % (best, bin(found_at[best][0]), bin(found_at[best][1])))
    print("pairs examined = %d, passed edge-count filter = %d" % (pairs, passed_edge))
    print("elapsed %.1f s" % (time.time() - t0))


if __name__ == "__main__":
    main()
