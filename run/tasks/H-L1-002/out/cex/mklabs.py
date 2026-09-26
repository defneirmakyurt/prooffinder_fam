#!/usr/bin/env python3
"""Write structured and random labelling files of Q_3..Q_6 (vertices in increasing label order)."""
import random, os
D = '/home/user/bainsahackathon/run/tasks/H-L1-002/out/cex/labs'
os.makedirs(D, exist_ok=True)
rng = random.Random(7)
def w(name, d, order):
    assert sorted(order) == list(range(1 << d))
    with open(os.path.join(D, name), 'w') as fh:
        fh.write('\n'.join(format(v, '0%db' % d) for v in order) + '\n')
for d in range(3, 7):
    n = 1 << d
    w('Q%d_lex.txt' % d, d, list(range(n)))
    w('Q%d_revlex.txt' % d, d, list(range(n))[::-1])
    w('Q%d_weight.txt' % d, d, sorted(range(n), key=lambda v: (bin(v).count('1'), v)))
    w('Q%d_gray.txt' % d, d, [i ^ (i >> 1) for i in range(n)])
    for t in range(5):
        o = list(range(n)); rng.shuffle(o); w('Q%d_rand%d.txt' % (d, t), d, o)
# Q_3 / Q_4 witnesses quoted in subject sanity.py check F
w('Q3_witness.txt', 3, [int(s, 2) for s in "000 001 010 011 101 110 100 111".split()])
w('Q4_witness.txt', 4, [int(s, 2) for s in "1010 0111 0101 1011 1000 0010 0001 0011 1101 1110 1001 0100 0000 0110 1111 1100".split()])
