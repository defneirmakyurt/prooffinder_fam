"""Independent branch-and-bound over labellings of Q_d: "is there a labelling with total <= T?"
Written deliberately WITHOUT the state merging used by dp_lower.py, so that the two programs
agree only if both the bound and the merging in dp_lower.py are right.

Usage: python3 bb_lower.py d T [--no-fix] [--basic] [outfile]
  --no-fix : do not fix label 1 at vertex 0 (default: fixed; sound by the translation symmetry
             v |-> v XOR u of Q_d, see README).
  --basic  : use the weaker, one-line-obvious bound  sum_{v unplaced} A(v)  only.

BOUND (written out in README/claims):  with S = placed set, N(w) known for w in S,
A(v) = sum_{w in S, w ~ v} N(w) for unplaced v, every completion satisfies
   sum_{v unplaced} N(v)  =  #future valleys + sum_v A(v) + sum_{edges inside the unplaced set}
                             N(lower endpoint)
                          >= sum_v A(v) + sum_{such edges uv} min(max(1,A(u)), max(1,A(v))),
because N(x) >= 1 for every vertex and N(x) >= A(x) for every unplaced x.
Output: "NONE ..." or "FOUND <total> <order>".
"""
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))
from uphill import count_uphill, to_lines

args = [a for a in sys.argv[1:] if not a.startswith("--")]
flags = {a for a in sys.argv[1:] if a.startswith("--")}
d, T = int(args[0]), int(args[1])
outfile = args[2] if len(args) > 2 else None
fix = "--no-fix" not in flags
basic = "--basic" in flags
n = 1 << d
NB = [[v ^ (1 << j) for j in range(d)] for v in range(n)]
EDGES = [(u, v) for u in range(n) for v in NB[u] if u < v]

placed = [False] * n
N = [0] * n
order = []
nodes = 0
found = [None]


def bound():
    A = [0] * n
    lb = 0
    for v in range(n):
        if not placed[v]:
            a = sum(N[w] for w in NB[v] if placed[w])
            A[v] = a
            lb += a
    if not basic:
        for u, v in EDGES:
            if not placed[u] and not placed[v]:
                lb += min(max(1, A[u]), max(1, A[v]))
    return lb


def rec(k, tot):
    global nodes
    nodes += 1
    if k == n:
        if tot <= T and found[0] is None:
            found[0] = (tot, list(order))
        return found[0] is not None
    if tot + bound() > T:
        return False
    for v in range(n):
        if placed[v]:
            continue
        pn = [w for w in NB[v] if placed[w]]
        Nv = (0 if pn else 1) + sum(N[w] for w in pn)
        if tot + Nv > T:
            continue
        placed[v] = True
        N[v] = Nv
        order.append(v)
        if rec(k + 1, tot + Nv):
            return True
        order.pop()
        placed[v] = False
        N[v] = 0
    return False


starts = [0] if fix else list(range(n))
for s in starts:
    placed[s] = True
    N[s] = 1
    order.append(s)
    if rec(1, 1):
        break
    order.pop()
    placed[s] = False
    N[s] = 0

print("d = %d, T = %d, label-1-fixed-at-0 = %s, basic-bound = %s, search nodes = %d"
      % (d, T, fix, basic, nodes))
if found[0] is None:
    print("NONE: no labelling%s of Q_%d has at most %d uphill paths => U(Q_%d) >= %d"
          % (" with label 1 at vertex 0" if fix else "", d, T, d, T + 1))
else:
    tot, o = found[0]
    assert sorted(o) == list(range(n)) and count_uphill(d, o) == tot
    print("FOUND %d %s" % (tot, [format(v, "0%db" % d) for v in o]))
    if outfile:
        open(outfile, "w").write(to_lines(d, o))
        print("wrote", outfile)
