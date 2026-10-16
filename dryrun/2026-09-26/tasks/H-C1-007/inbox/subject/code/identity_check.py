"""Numerical sanity check of the two identities used in out/proof.md.

  (I1)  total = #valleys + sum_v N(v) * updeg(v)
  (I2)  |E|   = sum_v downdeg(v)
and of the consequence  total >= |E| + #valleys.
Checked on random labellings of Q_d for d = 2..5 and, for d = 3, on ALL 8! labellings.
"""
import itertools, random
from uphill import neighbours, count_recurrence

def check(order, nbr, d):
    n = 1 << d
    total, N, lab = count_recurrence(order, nbr)
    up = [sum(1 for w in nbr[v] if lab[w] > lab[v]) for v in range(n)]
    down = [sum(1 for w in nbr[v] if lab[w] < lab[v]) for v in range(n)]
    valleys = sum(1 for v in range(n) if down[v] == 0)
    assert total == valleys + sum(N[v] * up[v] for v in range(n)), "I1 fails"
    assert sum(down) == d * (1 << (d - 1)), "I2 fails"
    assert total >= d * (1 << (d - 1)) + valleys, "corollary fails"
    return total

rng = random.Random(20260926)
for d in range(2, 6):
    nbr = neighbours(d)
    n = 1 << d
    for _ in range(2000):
        order = list(range(n))
        rng.shuffle(order)
        check(order, nbr, d)
    print("d =", d, ": 2000 random labellings, I1 and I2 hold")

nbr = neighbours(3)
for order in itertools.permutations(range(8)):
    check(order, nbr, 3)
print("d = 3 : all 8! = 40320 labellings, I1 and I2 hold")
