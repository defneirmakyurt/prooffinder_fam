#!/usr/bin/env python3
"""Tests for verify.py (run: python3 tests.py).  Standard library only."""
import itertools
import os
import random
import subprocess
import sys
import tempfile
from math import factorial

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from verify import count_uphill, parse  # noqa: E402

VERIFY = os.path.join(HERE, "verify.py")
RESULTS = []


def check(name, cond, detail=""):
    RESULTS.append((name, bool(cond), detail))


# ---------------------------------------------------------------- orders
def lex(d):
    return [format(x, f"0{d}b") for x in range(2 ** d)]


def gray(d):
    return [format(i ^ (i >> 1), f"0{d}b") for i in range(2 ** d)]


def by_weight(d):
    return sorted(lex(d), key=lambda s: (s.count("1"), s))


# ------------------------------------------------ independent reference 1
def naive_count(order):
    """Explicit enumeration of every uphill path, string-based adjacency."""
    f = {s: i + 1 for i, s in enumerate(order)}

    def adjacent(a, b):
        return sum(x != y for x, y in zip(a, b)) == 1
    N = {a: [b for b in order if adjacent(a, b)] for a in order}
    valleys = [v for v in order if all(f[w] > f[v] for w in N[v])]
    count, stack = 0, [[v] for v in valleys]
    while stack:
        p = stack.pop()
        assert len(set(p)) == len(p)
        count += 1
        stack.extend(p + [w] for w in N[p[-1]] if f[w] > f[p[-1]])
    return count


# ------------------------------------------------ independent reference 2
def forward_count(order):
    """end[v] = uphill paths ending at v = [v valley] + sum over lower nbrs."""
    d = len(order[0])
    f = {s: i + 1 for i, s in enumerate(order)}

    def nb(s):
        return [s[:j] + ("1" if s[j] == "0" else "0") + s[j + 1:] for j in range(d)]
    end = {}
    for s in order:                          # increasing label
        valley = all(f[w] > f[s] for w in nb(s))
        end[s] = int(valley) + sum(end[w] for w in nb(s) if f[w] < f[s])
    return sum(end.values())


def automorphism(order, rng):
    d = len(order[0])
    perm = list(range(d))
    rng.shuffle(perm)
    mask = [rng.randrange(2) for _ in range(d)]
    return ["".join(str(int(s[perm[j]]) ^ mask[j]) for j in range(d)) for s in order]


# ============================================================ hand cases
# Q_1: vertices 0 - 1.  Order [0,1]: f(0)=1, f(1)=2.  Valley: 0 only
# (its neighbour has label 2 > 1; vertex 1 has neighbour label 1 < 2).
# Uphill paths: (0), (0,1)  ->  2.  Order [1,0] is symmetric -> 2.
check("Q1 [0,1] = 2", count_uphill(["0", "1"]) == 2)
check("Q1 [1,0] = 2", count_uphill(["1", "0"]) == 2)

# Q_2 is the 4-cycle 00-01-11-10-00.  Put label 1 at a vertex and read the
# labels around the cycle; up to reflection there are three classes
# (8 labellings each, 24 in total):
#  A: 1-2-3-4-1.  Valley {1}.  up(4)=1, up(3)=1+up(4)=2, up(2)=1+up(3)=3,
#     up(1)=1+up(2)+up(4)=5.  Paths (1),(1,2),(1,2,3),(1,2,3,4),(1,4): 5.
#  B: 1-2-4-3-1.  Valley {1}.  up(4)=1, up(3)=1+1=2, up(2)=1+1=2,
#     up(1)=1+2+2=5.  Paths (1),(1,2),(1,2,4),(1,3),(1,3,4): 5.
#  C: 1-3-2-4-1.  Valleys {1,2} (both neighbours are 3 and 4).
#     up(1)=1+1+1=3, up(2)=3.  Total 6.
# Class C is exactly "labels 1 and 2 on opposite vertices", i.e. the first two
# strings differ in both bits.  So: count = 6 if so, else 5 (16 x 5, 8 x 6).
q2 = [(list(p), count_uphill(list(p))) for p in itertools.permutations(lex(2))]
check("Q2 all 24 labellings match hand rule",
      all(c == (6 if p[0][0] != p[1][0] and p[0][1] != p[1][1] else 5) for p, c in q2))
check("Q2 distribution 16x5 + 8x6",
      sorted(c for _, c in q2) == [5] * 16 + [6] * 8)
check("Q2 gray = class A = 5", count_uphill(gray(2)) == 5)

# Q_3 lexicographic: vertex x (as integer) gets label x+1.  A step flipping a
# 0 to 1 increases the integer, flipping 1 to 0 decreases it, so the only
# valley is 000 and the uphill paths are the ordered choices of distinct bits
# to switch on: 1 + 3 + 3*2 + 3*2*1 = 16.
check("Q3 lex = 16 (hand)", count_uphill(lex(3)) == 16)

# Same argument for every d and for every order extending the subset order
# (by Hamming weight; reverse lex is lex composed with the complement map):
# count = sum_{k=0}^{d} d!/(d-k)!.  d=4 by hand: 1+4+12+24+24 = 65.
check("Q4 lex = 65 (hand)", count_uphill(lex(4)) == 65)
for d in range(1, 10):
    L = sum(factorial(d) // factorial(d - k) for k in range(d + 1))
    check(f"Q{d} lex = {L}", count_uphill(lex(d)) == L)
    check(f"Q{d} reverse lex = {L}", count_uphill(lex(d)[::-1]) == L)
    check(f"Q{d} by weight = {L}", count_uphill(by_weight(d)) == L)

# Q_3 Gray code 000,001,011,010,110,111,101,100 gets labels 1..8.
# Neighbours with labels: 1:{2,4,8} 2:{1,3,7} 3:{4,2,6} 4:{3,1,5}
#                         5:{6,8,4} 6:{5,7,3} 7:{8,6,2} 8:{7,5,1}
# Only label 1 (000) is a valley.  up by decreasing label:
# up8=1, up7=1+up8=2, up6=1+up7=3, up5=1+up6+up8=5, up4=1+up5=6,
# up3=1+up4+up6=10, up2=1+up3+up7=13, up1=1+up2+up4+up8=21.  Total 21.
check("Q3 gray = 21 (hand)", count_uphill(gray(3)) == 21)

# Q_3 parity: even-weight vertices 000,011,101,110 get labels 1..4, odd ones
# 001,010,100,111 get 5..8.  Every even vertex is a valley (its 3 neighbours
# are odd, labels >= 5); no odd vertex is.  From an even vertex: itself and
# the 3 one-step paths; odd vertices have no higher neighbour.  4 * 4 = 16.
check("Q3 parity = 16 (hand)",
      count_uphill(["000", "011", "101", "110", "001", "010", "100", "111"]) == 16)

# ================================================= brute-force cross-checks
bad = [p for p in itertools.permutations(lex(3))
       if count_uphill(list(p)) != naive_count(list(p))]
check("Q3 all 40320 labellings: main == naive DFS", not bad, str(bad[:1]))

rng = random.Random(20260926)
for d in range(1, 10):
    # Gray order: the labels run along a Hamiltonian path, so the count grows
    # super-exponentially (Q6: ~1e9, Q9: ~2e70); explicit DFS only for d <= 4,
    # the forward DP (exact big integers) for all d.
    order = gray(d)
    ok = count_uphill(order) == forward_count(order)
    if d <= 4:
        ok = ok and count_uphill(order) == naive_count(order)
    check(f"Q{d} gray: main == reference(s)", ok)
    trials = {1: 5, 2: 30, 3: 200, 4: 200, 5: 100, 6: 50, 7: 20, 8: 20, 9: 10}[d]
    for t in range(trials):
        order = lex(d)
        rng.shuffle(order)
        c = count_uphill(order)
        ok = c == forward_count(order)
        if d <= 7:
            ok = ok and c == naive_count(order)
        ok = ok and count_uphill(automorphism(order, rng)) == c
        if not ok:
            check(f"Q{d} random #{t}", False, repr(order))
            break
    else:
        check(f"Q{d} {trials} random labellings: main == references, "
              f"automorphism-invariant", True)


# ============================================================ CLI / format
def run(content, *args, raw=False):
    with tempfile.NamedTemporaryFile("wb", suffix=".txt", delete=False) as fh:
        fh.write(content if raw else content.encode("utf-8"))
        name = fh.name
    try:
        p = subprocess.run([sys.executable, VERIFY, name, *args],
                           capture_output=True, text=True)
    finally:
        os.unlink(name)
    return p.returncode, p.stdout.strip()


Q3 = "\n".join(lex(3)) + "\n"
accept = [
    ("Q3 lex, final newline", Q3, ()),
    ("Q3 lex, no final newline", Q3.rstrip("\n"), ()),
    ("Q3 lex, CRLF", Q3.replace("\n", "\r\n"), ()),
    ("Q3 lex, trailing spaces/tabs", "\n".join(s + " \t " for s in lex(3)), ()),
    ("Q3 lex, --d 3", Q3, ("--d", "3")),
    ("Q3 lex, --d=3", Q3, ("--d=3",)),
]
for name, content, args in accept:
    code, out = run(content, *args)
    check(f"accept: {name}", code == 0 and out == "VERIFIED 16", out)

code, out = run("\n".join(gray(3)) + "\n")
check("accept: Q3 gray -> VERIFIED 21", code == 0 and out == "VERIFIED 21", out)
code, out = run("0\n1\n")
check("accept: Q1 -> VERIFIED 2", code == 0 and out == "VERIFIED 2", out)

L3 = lex(3)
reject = [
    ("empty file", "", ()),
    ("single newline", "\n", ()),
    ("7 lines", "\n".join(L3[:7]), ()),
    ("9 lines", "\n".join(L3 + ["000"]), ()),
    ("duplicate vertex", "\n".join(L3[:7] + ["000"]), ()),
    ("line too long", "\n".join(L3[:7] + ["1110"]), ()),
    ("line too short", "\n".join(L3[:7] + ["11"]), ()),
    ("0b prefix", "\n".join(["0b1"] + L3[1:]), ()),
    ("underscore", "\n".join(["0_1"] + L3[1:]), ()),
    ("digit 2", "\n".join(["002"] + L3[1:]), ()),
    ("leading space", "\n".join([" 001"] + L3[1:]), ()),
    ("inner tab", "\n".join(["0\t01"] + L3[1:]), ()),
    ("blank line in middle", "\n".join(L3[:4] + [""] + L3[4:]), ()),
    ("extra blank line at end", Q3 + "\n", ()),
    ("whitespace-only last line", Q3 + "  ", ()),
    ("CR-only line endings", Q3.replace("\n", "\r"), ()),
    ("comma separated", ",".join(L3), ()),
    ("--d mismatch", Q3, ("--d", "4")),
    ("--d not a number", Q3, ("--d", "x")),
    ("--d zero", Q3, ("--d", "0")),
    ("--d missing value", Q3, ("--d",)),
    ("unknown option", Q3, ("--foo",)),
]
for name, content, args in reject:
    code, out = run(content, *args)
    check(f"reject: {name}", code == 1 and out.startswith("FAILED: "), out)

code, out = run("﻿" + Q3)
check("reject: UTF-8 BOM", code == 1 and out.startswith("FAILED: "), out)
code, out = run(Q3.replace("000", "０" + "00", 1))
check("reject: fullwidth digit", code == 1 and out.startswith("FAILED: "), out)
code, out = run(b"\xff" + Q3.encode(), raw=True)
check("reject: invalid byte", code == 1 and out.startswith("FAILED: "), out)

p = subprocess.run([sys.executable, VERIFY], capture_output=True, text=True)
check("reject: no arguments", p.returncode == 1 and p.stdout.startswith("FAILED: "), p.stdout)
p = subprocess.run([sys.executable, VERIFY, os.path.join(HERE, "tmp", "no_such_file.txt")],
                   capture_output=True, text=True)
check("reject: missing file", p.returncode == 1 and p.stdout.startswith("FAILED: "), p.stdout)

for name, text in [("parse rejects d=0 empty line", "\n\n"),
                   ("parse rejects 2^d mismatch", "0\n")]:
    try:
        parse(text)
        check(name, False)
    except ValueError:
        check(name, True)

# Q_9 end to end through the CLI (runtime requirement: well under 10 s).
import time  # noqa: E402
order9 = lex(9)
random.Random(9).shuffle(order9)
t0 = time.perf_counter()
code, out = run("\n".join(order9) + "\n", "--d", "9")
dt = time.perf_counter() - t0
check(f"Q9 random via CLI matches forward DP ({dt:.2f} s)",
      code == 0 and out == f"VERIFIED {forward_count(order9)}" and dt < 10, out)

# ================================================================ summary
failed = [r for r in RESULTS if not r[1]]
for name, ok, detail in RESULTS:
    if not ok:
        print(f"FAIL  {name}  {detail}")
print(f"{len(RESULTS) - len(failed)}/{len(RESULTS)} tests passed")
sys.exit(1 if failed else 0)
