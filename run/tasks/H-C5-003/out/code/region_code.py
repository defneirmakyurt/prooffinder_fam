#!/usr/bin/env python3
"""region_code.py -- H-C5-003. Max code (pairwise Hamming distance >= 4) among even-weight words of Q_9
whose last-5-coordinate part y has weight >= t (i.e. at distance >= t from the Q_4 cluster's outer point 0).
SAT with pysat: x_c for each allowed word, clause (-x_a or -x_b) for distance-2 pairs, sum >= K.
Usage: region_code.py t K"""
import sys, time
from pysat.solvers import Solver
from pysat.card import CardEnc, EncType
t = int(sys.argv[1]); K = int(sys.argv[2])
W = [v for v in range(512) if bin(v).count("1") % 2 == 0 and bin(v >> 4).count("1") >= t]
idx = {v: i + 1 for i, v in enumerate(W)}
cl = [[-idx[a], -idx[b]] for a in W for b in W if a < b and bin(a ^ b).count("1") == 2]
card = CardEnc.atleast([idx[v] for v in W], bound=K, top_id=len(W), encoding=EncType.seqcounter)
s = Solver(name="cadical153", bootstrap_with=cl + card.clauses)
t0 = time.time()
r = s.solve()
print("region wt(y)>=%d: %d words; code of size >= %d: %s (%.1fs)" % (t, len(W), K, "SAT" if r else "UNSAT", time.time() - t0))
if r:
    m = s.get_model()
    print([format(v, "09b") for v in W if m[idx[v] - 1] > 0])
