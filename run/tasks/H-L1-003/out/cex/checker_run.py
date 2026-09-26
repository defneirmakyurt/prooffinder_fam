#!/usr/bin/env python3
"""S6: run the accepted checker (inbox/checker/verify.py) on the Remark-1 witnesses and on
random + structured labellings of Q_3..Q_6; confirm every count >= d*2^(d-1)+2 and that the
checker agrees with the referee's independent recurrence count. Stdlib only."""
import os, random, subprocess, sys, time
HERE = os.path.dirname(os.path.abspath(__file__))
CHK = os.path.join(HERE, "..", "..", "inbox", "checker", "verify.py")
TMP = os.path.join(HERE, "lab"); os.makedirs(TMP, exist_ok=True)
PY = sys.executable

def count(d, order):
    n = 1 << d; f = [0] * n
    for i, v in enumerate(order, 1): f[v] = i
    N = [0] * n
    for v in order:
        low = [v ^ (1 << j) for j in range(d) if f[v ^ (1 << j)] < f[v]]
        N[v] = (0 if low else 1) + sum(N[w] for w in low)
    return sum(N)

def run(d, order, tag):
    p = os.path.join(TMP, tag + ".txt")
    with open(p, "w") as fh:
        fh.write("\n".join(format(v, "0%db" % d) for v in order) + "\n")
    r = subprocess.run([PY, CHK, p, "--d", str(d)], capture_output=True, text=True)
    out = r.stdout.strip()
    assert out.startswith("VERIFIED "), out
    c = int(out.split()[1])
    assert c == count(d, order), (tag, c)
    assert c >= d * 2 ** (d - 1) + 2, (tag, c)
    return c

rng = random.Random(7)
res = []
w3 = [int(s, 2) for s in "000 001 010 011 101 110 100 111".split()]
w4 = [int(s, 2) for s in "1010 0111 0101 1011 1000 0010 0001 0011 1101 1110 1001 0100 0000 0110 1111 1100".split()]
res.append(("witness Q3", run(3, w3, "w3")))
res.append(("witness Q4", run(4, w4, "w4")))
for d in range(3, 7):
    n = 1 << d
    lex = list(range(n))
    weight = sorted(range(n), key=lambda v: (bin(v).count("1"), v))
    gray = [i ^ (i >> 1) for i in range(n)]
    mins = {}
    for tag, o in (("lex", lex), ("rev", lex[::-1]), ("weight", weight), ("gray", gray)):
        mins[tag] = run(d, o, "d%d_%s" % (d, tag))
    rmin = None
    for t in range(15):
        o = list(range(n)); rng.shuffle(o)
        c = run(d, o, "d%d_r%d" % (d, t)); rmin = c if rmin is None else min(rmin, c)
    mins["random15_min"] = rmin
    res.append(("Q%d bound %d" % (d, d * 2 ** (d - 1) + 2), mins))
for r in res: print(r)
print("all checker counts >= d*2^(d-1)+2 and agree with referee count")
