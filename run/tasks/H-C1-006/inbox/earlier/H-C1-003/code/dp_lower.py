"""Exact prefix dynamic programme for "is there a labelling of Q_d with at most T uphill paths?"
(stdlib only, exact integers).

Usage: python3 dp_lower.py d T [--no-fix] [--no-prune] [outfile]

A labelling is built by placing vertices in increasing label order.  A partial state is
(S, N|S): S = set of placed vertices (the labels 1..|S|), N(w) for w in S = number of
uphill paths ending at w (fully determined by the order of S alone, see README/claims).
  * placing v next:  N(v) = [no neighbour of v in S] + sum_{w in S, w ~ v} N(w).
  * two partial states with the same S and the same N on the BOUNDARY (placed vertices with an
    unplaced neighbour) have identical sets of possible futures, with identical future cost;
    so only the minimum running total per (S, boundary N) is kept (exact, no loss).
  * pruning: a state is discarded when  running_total + LB(S, N) > T,  where
        LB = sum_{v unplaced} A(v) + sum_{edges uv, u,v unplaced} min(max(1,A(u)), max(1,A(v))),
        A(v) = sum_{w in S, w ~ v} N(w).
    LB is a valid lower bound on the sum of N over the unplaced vertices for EVERY completion.
  * --no-fix: do not fix label 1 at vertex 0 (default: fixed, sound by translation symmetry).
  * --no-prune: disable LB pruning (used only for the Q_3 cross-check).
Output: number of complete labellings-classes surviving (distinct final states) and, if any,
the minimum total and one witness order (written to outfile if given)."""
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))
from uphill import count_uphill, to_lines

args = [a for a in sys.argv[1:] if not a.startswith("--")]
flags = {a for a in sys.argv[1:] if a.startswith("--")}
d = int(args[0])
T = int(args[1])
outfile = args[2] if len(args) > 2 else None
fix = "--no-fix" not in flags
prune = "--no-prune" not in flags
n = 1 << d
NB = [[v ^ (1 << j) for j in range(d)] for v in range(n)]
NBMASK = [sum(1 << w for w in NB[v]) for v in range(n)]
EDGES = [(u, v) for u in range(n) for v in NB[u] if u < v]
FULL = (1 << n) - 1


def boundary(S):
    """placed vertices having at least one unplaced neighbour, in increasing order"""
    return [w for w in range(n) if (S >> w) & 1 and (NBMASK[w] & ~S & FULL)]


def lower_bound(S, Nd):
    """Nd: dict boundary vertex -> N.  Valid lower bound on sum of N over unplaced vertices."""
    A = {}
    lb = 0
    for v in range(n):
        if not (S >> v) & 1:
            a = sum(Nd[w] for w in NB[v] if (S >> w) & 1)
            A[v] = a
            lb += a
    for u, v in EDGES:
        if u in A and v in A:
            lb += min(max(1, A[u]), max(1, A[v]))
    return lb


# layer k: dict S -> dict key(tuple of boundary N) -> (total, order_prefix)
if fix:
    starts = [0]
else:
    starts = list(range(n))
layer = {}
for s in starts:
    S = 1 << s
    b = boundary(S)
    key = tuple(1 for _ in b)  # N(s) = 1 (valley)
    layer.setdefault(S, {})[key] = (1, (s,))
states_total = sum(len(x) for x in layer.values())
for k in range(1, n):
    new = {}
    for S, table in layer.items():
        b = boundary(S)
        for key, (tot, pref) in table.items():
            Nd = dict(zip(b, key))
            for v in range(n):
                if (S >> v) & 1:
                    continue
                placed_nb = [w for w in NB[v] if (S >> w) & 1]
                Nv = (0 if placed_nb else 1) + sum(Nd[w] for w in placed_nb)
                S2 = S | (1 << v)
                tot2 = tot + Nv
                b2 = boundary(S2)
                Nd2 = {w: (Nv if w == v else Nd[w]) for w in b2}
                if prune and tot2 + lower_bound(S2, Nd2) > T:
                    continue
                if tot2 > T:
                    continue
                key2 = tuple(Nd2[w] for w in b2)
                t2 = new.setdefault(S2, {})
                old = t2.get(key2)
                if old is None or tot2 < old[0] or (tot2 == old[0] and pref + (v,) < old[1]):
                    t2[key2] = (tot2, pref + (v,))
    layer = new
    cnt = sum(len(x) for x in layer.values())
    states_total += cnt
    print("layer %2d: %7d placed-sets, %8d states" % (k + 1, len(layer), cnt))
    if not layer:
        break

print("d = %d, threshold T = %d, label-1-fixed-at-0 = %s, pruning = %s" % (d, T, fix, prune))
print("total states generated:", states_total)
final = [(tot, pref) for table in layer.values() for (tot, pref) in table.values()] if layer else []
if not final:
    print("RESULT: no labelling%s of Q_%d has at most %d uphill paths  => U(Q_%d) >= %d"
          % (" with label 1 at vertex 0" if fix else "", d, T, d, T + 1))
else:
    tot, pref = min(final)
    assert len(pref) == n and sorted(pref) == list(range(n))
    assert count_uphill(d, pref) == tot
    print("RESULT: found labelling with %d uphill paths (<= %d); witness: %s"
          % (tot, T, [format(v, "0%db" % d) for v in pref]))
    if outfile:
        with open(outfile, "w") as fh:
            fh.write(to_lines(d, pref))
        print("wrote", outfile)
