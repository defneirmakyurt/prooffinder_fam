"""R3: exhaustive over ALL 8! = 40320 bijections V(Q_3) -> {1..8}.  No symmetry reduction."""
import itertools, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from uphill import count, to_lines

d = 3
best, arg, hist = None, None, {}
for order in itertools.permutations(range(8)):
    c = count(d, order)
    hist[c] = hist.get(c, 0) + 1
    if best is None or c < best:
        best, arg = c, order
print("labellings checked:", sum(hist.values()))
print("min =", best, " #minimisers =", hist[best])
print("histogram (count: #labellings) smallest 5:", sorted(hist.items())[:5])
print("first minimiser (lex order of permutations):")
print(to_lines(d, arg), end="")
if len(sys.argv) > 1:
    open(sys.argv[1], "w").write(to_lines(d, arg))
