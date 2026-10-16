"""Counterexample hunt: try hard to find a labelling of Q_3 with < 14 or of Q_4 with < 34
uphill paths, scoring with the LITERAL path enumeration (indep.py), not any recursion.
Random restarts + best-improvement swap hill climbing.  Also checks the two submitted
artefacts byte by byte against the hand-in format."""
import os, random, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from indep import count_literal

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))

for d, name, claimed in ((3, "Q3.txt", 14), (4, "Q4.txt", 34)):
    raw = open(os.path.join(ROOT, "inbox", "subject", name), "rb").read()
    txt = raw.decode("ascii")
    assert txt.endswith("\n") and not txt.endswith("\n\n"), "newline layout"
    rows = txt[:-1].split("\n")
    assert len(rows) == 2 ** d, "line count %d" % len(rows)
    assert all(len(r) == d and set(r) <= set("01") for r in rows), "bad row"
    assert len(set(rows)) == 2 ** d, "repeat"
    assert count_literal(d, [int(r, 2) for r in rows]) == claimed
    print("%s: %d bytes, %d lines of length %d, all distinct, literal count = %d  FORMAT OK"
          % (name, len(raw), len(rows), d, claimed))

for d, target, restarts in ((3, 14, 4000), (4, 34, 1200)):
    n = 1 << d
    rng = random.Random(4242 + d)
    best = None
    for _ in range(restarts):
        order = list(range(n))
        rng.shuffle(order)
        c = count_literal(d, order)
        improved = True
        while improved:
            improved = False
            for i in range(n):
                for j in range(i + 1, n):
                    order[i], order[j] = order[j], order[i]
                    c2 = count_literal(d, order)
                    if c2 < c:
                        c = c2
                        improved = True
                    else:
                        order[i], order[j] = order[j], order[i]
        if best is None or c < best:
            best = c
        if c < target:
            print("COUNTEREXAMPLE d=%d count=%d order=%s" % (d, c, order))
            sys.exit(1)
    print("d=%d: %d hill-climb restarts, best found = %d, none below %d"
          % (d, restarts, best, target))
