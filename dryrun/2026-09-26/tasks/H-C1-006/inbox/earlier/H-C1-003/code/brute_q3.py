"""Exhaustive search over ALL 8! = 40320 labellings of Q_3 (no symmetry reduction).
Prints the minimum number of uphill paths, the number of labellings attaining it,
the distribution of values, and writes one lexicographically-first minimiser to the path in argv[1]."""
import itertools
import sys
from collections import Counter

sys.path.insert(0, __import__("os").path.dirname(__file__))
from uphill import count_uphill, brute_paths, to_lines

d = 3
best = None
best_order = None
hist = Counter()
for order in itertools.permutations(range(8)):
    c = count_uphill(d, order)
    hist[c] += 1
    if best is None or c < best:
        best, best_order = c, order
# cross-check recurrence with explicit path enumeration on the minimiser and a sample
assert brute_paths(d, best_order) == best
for order in itertools.islice(itertools.permutations(range(8)), 0, 40320, 997):
    assert brute_paths(d, order) == count_uphill(d, order)
print("labellings checked:", sum(hist.values()))
print("min uphill paths U(Q_3) =", best, "attained by", hist[best], "labellings")
print("value distribution (lowest 6):", sorted(hist.items())[:6])
if len(sys.argv) > 1:
    with open(sys.argv[1], "w") as fh:
        fh.write(to_lines(d, best_order))
    print("wrote", sys.argv[1])
