#!/usr/bin/env python3
"""prime_order_classes.py -- print one representative generator (format perm:t of sym_forest_sat.py) for
each conjugacy class of elements of prime order in Aut(Q_9) = Z_2^9 : S_9, with its orbit count.

Classes (signed cycle types; see out/claims.md, argument A2):
  order 2: k positive transpositions (0 1)(2 3)... and j sign flips on fixed coordinates, (k,j) != (0,0);
  order 3: k disjoint 3-cycles, k = 1,2,3;   order 5: one 5-cycle;   order 7: one 7-cycle.
Output lines: <orbits> <order> <label> <generator>, sorted by orbit count."""
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from sym_forest_sat import parse_gen, orbits_of

d = 9
reps = []


def gen_str(cycles, flips):
    perm = list(range(d))
    for cyc in cycles:
        for a, b in zip(cyc, cyc[1:] + cyc[:1]):
            perm[a] = b
    t = sum(1 << f for f in flips)
    return ",".join(map(str, perm)) + ":" + str(t)


for k in range(0, 5):
    for j in range(0, d - 2 * k + 1):
        if k == 0 and j == 0:
            continue
        cycles = [[2 * i, 2 * i + 1] for i in range(k)]
        flips = list(range(2 * k, 2 * k + j))
        reps.append((2, "2:transp%d_flip%d" % (k, j), gen_str(cycles, flips)))
for k in (1, 2, 3):
    reps.append((3, "3:3cyc%d" % k, gen_str([[3 * i, 3 * i + 1, 3 * i + 2] for i in range(k)], [])))
reps.append((5, "5:5cyc", gen_str([[0, 1, 2, 3, 4]], [])))
reps.append((7, "7:7cyc", gen_str([[0, 1, 2, 3, 4, 5, 6]], [])))
out = []
for order, label, g in reps:
    _, orbs = orbits_of([parse_gen(g, d)], d)
    out.append((len(orbs), order, label, g))
for row in sorted(out):
    print(*row)
