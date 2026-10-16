"""Independent slow cross-check of out/Q3.txt and out/Q4.txt: enumerate every uphill path
explicitly (DFS from each valley) and compare with the recurrence-based count.
Usage: python3 check_artefacts.py <file> ..."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from uphill import count_uphill, brute_paths
for p in sys.argv[1:]:
    rows = [r.strip() for r in open(p) if r.strip()]
    d = len(rows[0])
    order = [int(r, 2) for r in rows]
    assert sorted(order) == list(range(1 << d)), p
    a, b = count_uphill(d, order), brute_paths(d, order)
    print("%s: d=%d recurrence=%d explicit-enumeration=%d %s" % (p, d, a, b, "OK" if a == b else "MISMATCH"))
    assert a == b
