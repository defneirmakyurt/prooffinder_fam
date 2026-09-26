#!/usr/bin/env python3
"""make_fixed_doubled.py -- stdlib. Fixed-vertex file for fsa.c, class "doubled":
half 0 (bit 8 = 0) is forced to be the perfect induced forest of Q_8: F_0 = (odd words of Q_8) u H,
H = first-order Reed-Muller code of length 8 (16 even words, minimum distance 4; every odd word of Q_8 is
adjacent to exactly one word of H, so F_0 is 16 disjoint stars K_{1,8}, |F_0| = 144). Half 1 is free.
Prints the check that H has 16 words, min distance 4, and covers every odd word exactly once."""
import itertools
pts = list(itertools.product([0, 1], repeat=3))
H = set()
for a in itertools.product([0, 1], repeat=4):
    w = 0
    for i, x in enumerate(pts):
        if (a[0] + a[1] * x[0] + a[2] * x[1] + a[3] * x[2]) % 2: w |= 1 << i
    H.add(w)
pc = lambda x: bin(x).count('1')
assert len(H) == 16 and all(pc(h) % 2 == 0 for h in H)
assert min(pc(a ^ b) for a in H for b in H if a != b) == 4
for x in range(256):
    if pc(x) % 2: assert sum(1 for h in H if pc(h ^ x) == 1) == 1
s = []
for v in range(512):
    if v >> 8: s.append('.')
    else: s.append('1' if (pc(v) % 2 == 1 or v in H) else '0')
open('tmp/fixed_doubled.txt', 'w').write(''.join(s) + '\n')
print('H ok: 16 words, min distance 4, perfect on odd words; fixed file written: tmp/fixed_doubled.txt')
