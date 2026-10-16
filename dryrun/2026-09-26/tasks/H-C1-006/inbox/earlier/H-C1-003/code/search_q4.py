"""Heuristic upper-bound search for Q_d (default d=4): random restarts + first-improvement
local search over label transpositions, with occasional random kicks.  Deterministic seeds.
Usage: python3 search_q4.py [d] [restarts] [seed] [outfile]"""
import random
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))
from uphill import count_uphill, to_lines

d = int(sys.argv[1]) if len(sys.argv) > 1 else 4
restarts = int(sys.argv[2]) if len(sys.argv) > 2 else 200
seed = int(sys.argv[3]) if len(sys.argv) > 3 else 1
out = sys.argv[4] if len(sys.argv) > 4 else None
n = 1 << d
rng = random.Random(seed)
best, best_order = None, None
per_restart = []
for r in range(restarts):
    order = list(range(n))
    rng.shuffle(order)
    cur = count_uphill(d, order)
    for kick in range(30):
        improved = True
        while improved:
            improved = False
            pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
            rng.shuffle(pairs)
            for i, j in pairs:
                order[i], order[j] = order[j], order[i]
                c = count_uphill(d, order)
                if c < cur:
                    cur = c
                    improved = True
                    break
                order[i], order[j] = order[j], order[i]
        if best is None or cur < best:
            best, best_order = cur, list(order)
        # kick: 2 random swaps from best-of-restart
        i, j = rng.randrange(n), rng.randrange(n)
        order[i], order[j] = order[j], order[i]
        cur = count_uphill(d, order)
    per_restart.append(best)
print("d =", d, "restarts =", restarts, "seed =", seed)
print("best uphill paths found:", best)
print("best order:", [format(v, "0%db" % d) for v in best_order])
if out:
    with open(out, "w") as fh:
        fh.write(to_lines(d, best_order))
    print("wrote", out)
