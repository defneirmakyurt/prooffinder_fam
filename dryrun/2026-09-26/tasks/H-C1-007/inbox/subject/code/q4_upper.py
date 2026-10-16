"""Upper bound for U(Q_4): deterministic seeded local search over labellings of Q_4.

This only ever CERTIFIES an upper bound (the labelling it prints is scored exactly);
it proves nothing about optimality.  The matching lower bound is the hand proof in
out/proof.md.
"""
import random, sys
from uphill import neighbours, count_recurrence, count_bruteforce, write_labelling

d = int(sys.argv[1]) if len(sys.argv) > 1 else 4
target = int(sys.argv[2]) if len(sys.argv) > 2 else 34
out = sys.argv[3] if len(sys.argv) > 3 else None
n = 1 << d
nbr = neighbours(d)

best = None
best_order = None
for seed in range(40):
    rng = random.Random(seed)
    order = list(range(n))
    rng.shuffle(order)
    cur = count_recurrence(order, nbr)[0]
    improved = True
    while improved:                       # first-improvement transposition local search
        improved = False
        for i in range(n):
            for j in range(i + 1, n):
                order[i], order[j] = order[j], order[i]
                t = count_recurrence(order, nbr)[0]
                if t < cur:
                    cur = t
                    improved = True
                else:
                    order[i], order[j] = order[j], order[i]
    if best is None or cur < best:
        best, best_order = cur, list(order)
    if best <= target:
        break
assert count_recurrence(best_order, nbr)[0] == count_bruteforce(best_order, nbr)
print("d =", d, "best found:", best, "(seeds used:", seed + 1, ")")
print("order:", ["".join("1" if (v >> (d - 1 - j)) & 1 else "0" for j in range(d)) for v in best_order])
if out:
    write_labelling(out, best_order, d)
    print("wrote", out)
