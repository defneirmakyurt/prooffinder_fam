"""S6: hand-computed Q_1 and Q_2, and brute force of U(Q_1), U(Q_2), U(Q_3)."""
import itertools, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from indep import count_literal

# Hand computation, Q_1, labelling 0 -> 1, 1 -> 2.
# Valleys: 0 (its only neighbour 1 has bigger label).  1 is not a valley.
# Uphill paths: (0), (0,1).  Total 2.
assert count_literal(1, [0, 1]) == 2, count_literal(1, [0, 1])
assert count_literal(1, [1, 0]) == 2
print("Q1 hand check OK: every labelling of Q_1 has 2 uphill paths -> U(Q_1)=2")

# Hand computation, Q_2 = 4-cycle 00-01-11-10-00, labelling 00,01,10,11 (labels 1,2,3,4).
# f(00)=1,f(01)=2,f(10)=3,f(11)=4.  Neighbours: 00~01,10 ; 01~00,11 ; 10~00,11 ; 11~01,10.
# Valleys: 00 only.
# Uphill paths from 00: (00); (00,01); (00,10); (00,01,11); (00,10,11).  Total 5.
assert count_literal(2, [0b00, 0b01, 0b10, 0b11]) == 5, count_literal(2, [0, 1, 2, 3])
print("Q2 hand check OK: labelling 00,01,10,11 has 5 uphill paths")

for d in (1, 2, 3):
    n = 1 << d
    hist = {}
    best, arg = None, None
    for order in itertools.permutations(range(n)):
        c = count_literal(d, order)
        hist[c] = hist.get(c, 0) + 1
        if best is None or c < best:
            best, arg = c, order
    print("d=%d  labellings=%d  min=%d  #minimisers=%d  smallest5=%s"
          % (d, sum(hist.values()), best, hist[best], sorted(hist.items())[:5]))
    print("   a minimiser:", [format(v, "0%db" % d) for v in arg])
