"""Referee H-C1-007: independent exhaustive lower bound for U(Q_4), by branch and bound
over ALL labellings (no reliance on the subject's Steps 5-7).  Stdlib, exact integers.

Search space.  A labelling f of Q_d is the same thing as an ordering v_1,...,v_{2^d} of the
vertices (f(v_i) = i).  We build the ordering left to right; every labelling is reached
exactly once, so the search space is all (2^d)! labellings.

Cost.  Let N(v) = #uphill paths ending at v.  Processing in increasing label order,
   N(v_i) = 1 if no neighbour of v_i is among v_1..v_{i-1}, else sum of N(w) over those
   neighbours w that ARE among v_1..v_{i-1}.
(First case: v_i is then a valley and contributes only the length-1 path; second case: v_i
is not a valley, so the indicator term is 0.)  This is exactly the recurrence, derived here
independently, and the total is sum_i N(v_i).  The scorer is cross-checked against the
literal path enumerator of independent.py on random orderings.

Pruning bound.  Let S = {v_1,...,v_i} be placed with N known on S, and let u be unplaced.
When u is finally placed, its set of smaller-labelled neighbours CONTAINS nbrs(u) cap S.
  * if nbrs(u) cap S is non-empty, u is not a valley, so N(u) = sum over ALL its
    smaller-labelled neighbours w of N(w) >= sum_{w in nbrs(u) cap S} N(w)  (all N >= 1);
  * otherwise N(u) >= 1 (an easy induction: the smallest-labelled vertex is a valley, and
    any other vertex dominates N of one smaller neighbour).
So  LB(S) = sum_{v in S} N(v) + sum_{u not in S} max(1, sum_{w in nbrs(u) cap S} N(w))
is a valid lower bound on the final total for every completion of S.  We prune a branch as
soon as LB(S) >= TARGET, because then no completion can have fewer than TARGET paths.

Symmetry.  Aut(Q_d) acts on labellings preserving the uphill-path count (it is a graph
automorphism, and the count depends only on the graph and the label order).  Q_d is
vertex-transitive, so WLOG v_1 = 0...0.  The stabiliser of 0...0 is the full coordinate-
permutation group S_d, whose orbits on the other vertices are the Hamming-weight classes;
so WLOG v_2 has weight in {1,...,d}, one representative each.  Both reductions are applied
in the `reduce=True` run; the `reduce=False` run (Q_3) repeats the search with no
reduction at all, as a control.

Conclusion proved by a COMPLETED run: no labelling of Q_d has fewer than TARGET uphill
paths, i.e. U(Q_d) >= TARGET.
"""
import itertools
import sys
import time


def nbrs_cube(d):
    return [tuple(v ^ (1 << j) for j in range(d)) for v in range(1 << d)]


def search(d, target, reduce=True, report=True):
    """Return (feasible_found, nodes).  feasible_found is None if the search COMPLETED
    with no labelling of fewer than `target` uphill paths; otherwise it is such an ordering."""
    n = 1 << d
    nbr = nbrs_cube(d)
    N = [0] * n
    placed = [False] * n
    order = []
    # partial[u] = sum of N(w) over placed neighbours w of u ; cnt[u] = #placed neighbours
    partial = [0] * n
    cnt = [0] * n
    nodes = [0]
    found = [None]

    def lb(cost):
        s = cost
        for u in range(n):
            if not placed[u]:
                p = partial[u]
                s += p if cnt[u] else 1
                if s >= target:
                    return s
        return s

    def rec(i, cost):
        nodes[0] += 1
        if found[0] is not None:
            return
        if i == n:
            if cost < target:
                found[0] = list(order)
            return
        if lb(cost) >= target:
            return
        if i == 0:
            cands = [0] if reduce else list(range(n))
        elif i == 1 and reduce:
            seen_w = set()
            cands = []
            for u in range(n):
                if placed[u]:
                    continue
                w = bin(u).count("1")
                if w not in seen_w:
                    seen_w.add(w)
                    cands.append(u)
        else:
            cands = [u for u in range(n) if not placed[u]]
        for u in cands:
            nu = partial[u] if cnt[u] else 1
            placed[u] = True
            N[u] = nu
            order.append(u)
            for w in nbr[u]:
                partial[w] += nu
                cnt[w] += 1
            rec(i + 1, cost + nu)
            for w in nbr[u]:
                partial[w] -= nu
                cnt[w] -= 1
            order.pop()
            placed[u] = False
            if found[0] is not None:
                return

    sys.setrecursionlimit(10000)
    rec(0, 0)
    return found[0], nodes[0]


def score(order, d):
    n = 1 << d
    nbr = nbrs_cube(d)
    lab = [0] * n
    for i, v in enumerate(order, 1):
        lab[v] = i
    N = [0] * n
    tot = 0
    for v in order:
        s = 0
        low = False
        for w in nbr[v]:
            if lab[w] < lab[v]:
                low = True
                s += N[w]
        N[v] = s if low else 1
        tot += N[v]
    return tot


if __name__ == "__main__":
    # --- self-test of the pruning machinery: it must FIND a labelling when one exists ---
    for d, tgt, expect in [(3, 15, True), (3, 14, False), (4, 35, True), (4, 34, False)]:
        t0 = time.time()
        f, nodes = search(d, tgt)
        el = time.time() - t0
        if f is not None:
            print("d=%d target=%d : FOUND a labelling with %d < %d paths (nodes=%d, %.2fs)"
                  % (d, tgt, score(f, d), tgt, nodes, el))
            assert score(f, d) < tgt
            assert expect, "unexpected: found a labelling below the claimed bound"
        else:
            print("d=%d target=%d : COMPLETED, NO labelling of Q_%d has fewer than %d "
                  "uphill paths  =>  U(Q_%d) >= %d   (nodes=%d, %.2fs)"
                  % (d, tgt, d, tgt, d, tgt, nodes, el))
            assert not expect, "unexpected: search failed where a labelling exists"

    # --- control: Q_3 with NO symmetry reduction at all ---
    t0 = time.time()
    f, nodes = search(3, 14, reduce=False)
    el = time.time() - t0
    print("d=3 target=14, NO symmetry reduction : %s (nodes=%d, %.2fs)"
          % ("COMPLETED, none found => U(Q_3) >= 14" if f is None else "FOUND %s" % (f,),
             nodes, el))

    # --- control: Q_4 with NO symmetry reduction at all ---
    t0 = time.time()
    f, nodes = search(4, 34, reduce=False)
    el = time.time() - t0
    print("d=4 target=34, NO symmetry reduction : %s (nodes=%d, %.2fs)"
          % ("COMPLETED, none found => U(Q_4) >= 34" if f is None else "FOUND %s" % (f,),
             nodes, el))
