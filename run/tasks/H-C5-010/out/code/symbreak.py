#!/usr/bin/env python3
"""
symbreak.py -- symmetry-breaking constraints (soundness: proof.md section 3).

Modes (comma-separated in --sb):
  root     : x_0 = 1  (vertex 00..0 is in T).
"""


def add(d, sb, pool, clauses):
    modes = [x for x in sb.split(",") if x]
    for md in modes:
        if md == "root":
            clauses.append([1])
        else:
            raise ValueError("unknown sb mode " + md)
