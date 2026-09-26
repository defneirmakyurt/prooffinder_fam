#!/usr/bin/env python3
"""make_code_forest.py -- stdlib. Given even words C (comma list, decimal, bit i = coordinate i) pairwise at
distance >= 4, write the indicator of F = C u (all odd words) of Q_9. F is an induced forest: every edge of Q_9
joins an even and an odd word; the only even words in F are the words of C; two words of C have no common
neighbour (distance >= 4), so Q_9[F] is a disjoint union of stars K_{1,9} and isolated odd vertices.
Usage: make_code_forest.py c1,c2,... out.txt"""
import sys
C = [int(x) for x in sys.argv[1].split(',')]
pc = lambda x: bin(x).count('1')
assert all(pc(c) % 2 == 0 for c in C), 'odd word in C'
assert all(pc(a ^ b) >= 4 for i, a in enumerate(C) for b in C[i + 1:]), 'distance < 4'
s = ''.join('1' if (pc(v) % 2 == 1 or v in C) else '0' for v in range(512))
open(sys.argv[2], 'w').write(s + '\n')
print('code of %d even words, min distance >= 4; |F| = %d, |S| = %d' % (len(C), s.count('1'), 512 - s.count('1')))
