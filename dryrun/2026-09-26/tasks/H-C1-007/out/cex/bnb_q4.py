"""Referee H-C1-007: independent exhaustive lower bound for U(Q_d), by branch and bound
over ALL labellings (does NOT use the subject's Steps 5-7).  Stdlib, exact integers.

Search space.  A labelling f of Q_d is the same thing as an ordering v_1,...,v_{2^d} of the
vertices (f(v_i) = i).  We build the ordering left to right; every ordering is reached
exactly once, so the space searched is exactly all (2^d)! labellings.

Cost.  N(v) = #uphill paths ending at v.  Processing in increasing label order,
   N(v_i) = 1                                  if no neighbour of v_i is in {v_1..v_{i-1}}
          = sum of N(w) over those neighbours   otherwise
(first case: v_i is then a valley and contributes exactly the length-1 path; second case:
v_i is not a valley so the length-1 term is 0).  Total = sum_i N(v_i).  This scorer is
cross-checked below against the literal path enumerator of independent.py.

Pruning bound.  Let S = placed set, T = V \ S, and for u in T let
  partial[u] = sum of N(w) over w in nbrs(u) cap S,   cnt[u] = |nbrs(u) cap S|,
  dT(u)      = #neighbours of u inside T that end up BEFORE u (unknown, but >= 0),
  E_T        = #edges of Q_d with both ends in T.
When u is placed its smaller-labelled neighbours are exactly (nbrs(u) cap S) plus dT(u) of
its T-neighbours, and every N >= 1, so
   N(u) >= partial[u] + dT(u)      (also when both are 0, since then N(u) = 1 >= 0)
   N(u) >= 1                       (every vertex ends at least one uphill path)
Summing the first over T and using sum_{u in T} dT(u) = E_T, and the second over T:
   sum_{u in T} N(u) >= max( sum_u max(1, partial[u]) ,  sum_u partial[u] + E_T ).
So LB(S) = cost(S) + that max is a valid lower bound for every completion of S; we cut the
branch as soon as LB(S) >= TARGET.

Symmetry.  Every automorphism of Q_d maps a labelling to a labelling with the same number
of uphill paths (it preserves adjacency and the label order).  Q_d is vertex-transitive, so
WLOG v_1 = 0...0.  The stabiliser of 0...0 is the coordinate-permutation group S_d, whose
orbits on the remaining vertices are the Hamming-weight classes, so WLOG v_2 is one fixed
representative of each weight 1..d.  Runs are done BOTH with (`reduce=True`) and without
(`reduce=False`) this reduction.

A COMPLETED run with no labelling found proves U(Q_d) >= TARGET.
A run that hits the node cap is PARTIAL and proves nothing.
"""
import random
import sys
import time


def nbrs_cube(d):
    return [tuple(v ^ (1 << j) for j in range(d)) for v in range(1 << d)]


def search(d, target, reduce=True, node_cap=None):
    """Return (found_order_or_None, nodes, completed_bool)."""
    n = 1 << d
    nbr = nbrs_cube(d)
    N = [0] * n
    placed = [False] * n
    order = []
    partial = [0] * n
    cnt = [0] * n
    unplaced = list(range(n))
    state = {"nodes": 0, "found": None, "capped": False,
             "E_T": d * (1 << (d - 1))}

    def rec(i, cost):
        if state["found"] is not None or state["capped"]:
            return
        state["nodes"] += 1
        if node_cap is not None and state["nodes"] > node_cap:
            state["capped"] = True
            return
        if i == n:
            if cost < target:
                state["found"] = list(order)
            return
        # --- bound ---
        a = cost
        b = cost + state["E_T"]
        for u in range(n):
            if not placed[u]:
                p = partial[u]
                a += p if cnt[u] else 1
                b += p
        if a >= target and b >= target:
            return
        if i == 0:
            cands = [0] if reduce else list(range(n))
        elif i == 1 and reduce:
            seen_w = set()
            cands = []
            for u in range(n):
                if not placed[u]:
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
            de = 0
            for w in nbr[u]:
                partial[w] += nu
                cnt[w] += 1
                if not placed[w]:
                    de += 1
            state["E_T"] -= de
            rec(i + 1, cost + nu)
            state["E_T"] += de
            for w in nbr[u]:
                partial[w] -= nu
                cnt[w] -= 1
            order.pop()
            placed[u] = False
            if state["found"] is not None or state["capped"]:
                return

    sys.setrecursionlimit(10000)
    rec(0, 0)
    return state["found"], state["nodes"], not state["capped"]


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


def literal_score(order, d):
    """Fully independent count: build every uphill path as an explicit tuple."""
    n = 1 << d
    nbr = nbrs_cube(d)
    lab = [0] * n
    for i, v in enumerate(order, 1):
        lab[v] = i
    valleys = [v for v in range(n) if all(lab[w] > lab[v] for w in nbr[v])]
    tot = 0
    stack = [(v,) for v in valleys]
    while stack:
        p = stack.pop()
        assert p[0] in valleys
        for x, y in zip(p, p[1:]):
            assert y in nbr[x] and lab[x] < lab[y]
        tot += 1
        for w in nbr[p[-1]]:
            if lab[w] > lab[p[-1]]:
                stack.append(p + (w,))
    return tot


def run(label, d, target, reduce, node_cap):
    t0 = time.time()
    f, nodes, done = search(d, target, reduce=reduce, node_cap=node_cap)
    el = time.time() - t0
    if not done:
        print("%s : PARTIAL - node cap %d hit after %.1fs; proves nothing"
              % (label, node_cap, el))
    elif f is None:
        print("%s : COMPLETED, no labelling of Q_%d has < %d uphill paths "
              "=> U(Q_%d) >= %d  (nodes=%d, %.1fs)" % (label, d, target, d, target, nodes, el))
    else:
        s, ls = score(f, d), literal_score(f, d)
        assert s == ls
        print("%s : COMPLETED, FOUND a labelling with %d (< %d) uphill paths %s "
              "(nodes=%d, %.1fs)"
              % (label, s, target,
                 ["".join(str((v >> (d - 1 - j)) & 1) for j in range(d)) for v in f],
                 nodes, el))
    sys.stdout.flush()
    return f, done


if __name__ == "__main__":
    cap = int(sys.argv[1]) if len(sys.argv) > 1 else 400_000_000

    # scorer cross-check: memoised recurrence vs literal tuple enumeration
    rng = random.Random(4242)
    for d in (2, 3, 4):
        for _ in range(300):
            o = list(range(1 << d))
            rng.shuffle(o)
            assert score(o, d) == literal_score(o, d)
    print("scorer cross-check: 300 random labellings per d=2,3,4, memoised count == "
          "literal enumeration of explicit path tuples")
    sys.stdout.flush()

    # positive controls: the search must FIND a labelling when one exists
    run("d=3 target=15 (control, reduced)", 3, 15, True, cap)
    run("d=4 target=35 (control, reduced)", 4, 35, True, cap)

    # the real lower bounds
    run("d=3 target=14 (reduced)      ", 3, 14, True, cap)
    run("d=3 target=14 (NO reduction) ", 3, 14, False, cap)
    run("d=4 target=34 (reduced)      ", 4, 34, True, cap)
    run("d=4 target=34 (NO reduction) ", 4, 34, False, cap)
