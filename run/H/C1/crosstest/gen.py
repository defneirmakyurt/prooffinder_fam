#!/usr/bin/env python3
"""Head's cross-test generator: prints one labelling of Q_d (vertices in label order). Usage: gen.py SEED"""
import random
import sys

seed = int(sys.argv[1])
rng = random.Random(seed)
d = 1 + seed % 9
verts = [format(i, f"0{d}b") for i in range(2 ** d)]
kind = (seed // 9) % 6
if kind == 0:
    order = verts
elif kind == 1:
    order = verts[::-1]
elif kind == 2:
    order = sorted(verts, key=lambda v: (v.count("1"), v))
elif kind == 3:
    order = [format(i ^ (i >> 1), f"0{d}b") for i in range(2 ** d)]
else:
    order = verts[:]
    rng.shuffle(order)
print("\n".join(order))
