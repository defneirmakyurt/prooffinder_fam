"""Exhaustive over all 8! = 40320 labellings of Q_3. No symmetry reduction."""
import itertools, sys
from uphill import neighbours, count_recurrence, count_bruteforce, write_labelling

d = 3
n = 1 << d
nbr = neighbours(d)
best = None
best_order = None
hist = {}
k = 0
for order in itertools.permutations(range(n)):
    t, _, _ = count_recurrence(order, nbr)
    hist[t] = hist.get(t, 0) + 1
    if best is None or t < best:
        best, best_order = t, order
    if k % 997 == 0:                      # cross-check the recurrence against explicit enumeration
        assert t == count_bruteforce(order, nbr)
    k += 1
assert count_recurrence(best_order, nbr)[0] == count_bruteforce(best_order, nbr)
print("labellings examined:", k)
print("min uphill paths over ALL 8! labellings of Q_3 =", best)
print("value distribution (lowest 6):", sorted(hist.items())[:6])
if len(sys.argv) > 1:
    write_labelling(sys.argv[1], best_order, d)
    print("wrote", sys.argv[1])
