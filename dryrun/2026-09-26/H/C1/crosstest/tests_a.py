#!/usr/bin/env python3
"""
tests.py -- tests for verify.py (uphill paths on Q_d).  Run:  python3 tests.py
Standard library only.  Prints one line per failure and a PASS/FAIL summary.

Contents
  A. Hand-computed cases (hand computation in comments): all labellings of Q_1 and Q_2,
     Gray code on Q_3, closed formulas for weight-ordered and bipartite-ordered labellings.
  B. Brute force: a second, deliberately naive implementation (0/1 strings, adjacency by
     Hamming distance, valleys by the literal definition, explicit DFS listing every
     uphill path) compared with verify.count_uphill on ALL 8! labellings of Q_3, and on
     random labellings of Q_1..Q_6.  A third implementation (forward recursion from the
     valleys) is compared on random and structured labellings of Q_1..Q_9.
  C. Hypercube automorphisms (coordinate permutation + XOR mask) leave the count unchanged.
  D. The command line: accepted inputs, malformed inputs that must be FAILED, exit codes,
     and the Q_9 runtime.
"""
import itertools
import math
import os
import random
import subprocess
import sys
import tempfile
import time
from functools import lru_cache

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import verify  # noqa: E402

VERIFY = os.path.join(HERE, "verify.py")
TMP = os.path.join(HERE, "tmp")
os.makedirs(TMP, exist_ok=True)

passed = 0
failed = 0


def check(cond, what):
    global passed, failed
    if cond:
        passed += 1
    else:
        failed += 1
        print("FAIL:", what)


def strings(d):
    return ["".join(t) for t in itertools.product("01", repeat=d)]


def main_count(rows):
    """verify.py's own parse + count on a list of 0/1 strings."""
    d, order = verify.parse("\n".join(rows) + "\n")
    return verify.count_uphill(d, order)


# ---------------------------------------------------------------- naive implementations
def brute_dfs(rows):
    """Enumerate every uphill path explicitly.  Strings, no bit tricks."""
    f = {v: i for i, v in enumerate(rows, 1)}                      # labelling
    adj = {v: [w for w in rows if sum(a != b for a, b in zip(v, w)) == 1] for v in rows}
    valleys = [v for v in rows if all(f[w] > f[v] for w in adj[v])]
    count = 0
    stack = [(v,) for v in valleys]                                # paths with k = 1
    while stack:
        path = stack.pop()
        count += 1                                                 # this path is uphill
        last = path[-1]
        for w in adj[last]:
            if f[w] > f[last]:
                stack.append(path + (w,))
    return count


def forward_count(rows):
    """Sum over valleys v of S(v), S(v) = 1 + sum of S(w) over higher neighbours w
    (number of increasing adjacent sequences starting at v)."""
    f = {v: i for i, v in enumerate(rows, 1)}
    d = len(rows[0])

    def nbrs(v):
        return [v[:j] + ("1" if v[j] == "0" else "0") + v[j + 1:] for j in range(d)]

    @lru_cache(maxsize=None)
    def S(v):
        return 1 + sum(S(w) for w in nbrs(v) if f[w] > f[v])

    return sum(S(v) for v in rows if all(f[w] > f[v] for w in nbrs(v)))


# ---------------------------------------------------------------- structured orders
def lex(d):
    return strings(d)


def revlex(d):
    return strings(d)[::-1]


def by_weight(d):
    return sorted(strings(d), key=lambda s: (s.count("1"), s))


def bipartite(d):
    return sorted(strings(d), key=lambda s: (s.count("1") % 2, s))


def gray(d):
    return [format(i ^ (i >> 1), "0%db" % d) for i in range(2 ** d)]


def weight_formula(d):
    # Any labelling in which lower Hamming weight means lower label (lex, reverse lex
    # after complementing, weight order): adjacent vertices differ in weight by exactly
    # one, so the lower neighbours of v are exactly the |v| vertices obtained by deleting
    # a 1.  The only valley is 0...0, N(0...0) = 1 and N(v) = sum of N over those, so
    # N(v) = |v|!.  Total = sum_k C(d,k) k! = sum_k d!/(d-k)!.
    return sum(math.factorial(d) // math.factorial(d - k) for k in range(d + 1))


def bipartite_formula(d):
    # Even-weight vertices get labels 1..2^(d-1), odd-weight ones the rest.  Every even
    # vertex has only odd (higher) neighbours: 2^(d-1) valleys, N = 1 each.  Every odd
    # vertex has d even (lower) neighbours and is not a valley: N = d each.  Paths stop
    # there (all neighbours of an odd vertex are lower).  Total = 2^(d-1) (1 + d).
    return 2 ** (d - 1) * (d + 1)


# ---------------------------------------------------------------- A. hand computations
def test_hand():
    # Q_1: vertices 0 - 1.  Either labelling: the label-1 vertex is the only valley
    # (its one neighbour has label 2); paths (v1), (v1, v2).  Count 2.
    check(main_count(["0", "1"]) == 2, "Q1 [0,1] -> 2")
    check(main_count(["1", "0"]) == 2, "Q1 [1,0] -> 2")

    # Q_2 is the 4-cycle 00-01-11-10-00.  Write the labels in cyclic order.  Up to the
    # 8 symmetries of the square there are 3 classes (8 labellings each):
    #  (1,2,3,4): valleys {1}. N1=1, N2=N1=1, N3=N2=1, N4=N3+N1=2.        Total 5.
    #  (1,2,4,3): valleys {1}. N1=1, N2=N1=1, N3=N1=1, N4=N2+N3=2.        Total 5.
    #  (1,3,2,4): valleys {1,2}. N1=1, N2=1, N3=N1+N2=2, N4=N2+N1=2.      Total 6.
    # The third class is exactly "labels 1 and 2 on opposite corners", i.e. lines 1 and 2
    # at Hamming distance 2.  So 16 labellings give 5 and 8 give 6.
    seen = {5: 0, 6: 0}
    for p in itertools.permutations(strings(2)):
        opposite = sum(a != b for a, b in zip(p[0], p[1])) == 2
        c = main_count(list(p))
        check(c == (6 if opposite else 5), "Q2 %s -> %d" % (p, c))
        if c in seen:
            seen[c] += 1
    check(seen == {5: 16, 6: 8}, "Q2 class sizes %s" % seen)
    check(main_count(["00", "01", "11", "10"]) == 5, "Q2 cycle order -> 5")
    check(main_count(["00", "11", "01", "10"]) == 6, "Q2 opposite 1,2 -> 6")

    # Q_3 in reflected Gray order: labels 000:1 001:2 011:3 010:4 110:5 111:6 101:7 100:8.
    # Only valley: 000 (every other vertex has a lower neighbour).
    # N(000)=1; N(001)=N(000)=1; N(011)=N(001)=1; N(010)=N(000)+N(011)=2;
    # N(110)=N(010)=2; N(111)=N(011)+N(110)=3; N(101)=N(001)+N(111)=4;
    # N(100)=N(000)+N(101)+N(110)=1+4+2=7.   Total 1+1+1+2+2+3+4+7 = 21.
    check(main_count(gray(3)) == 21, "Q3 Gray -> 21")

    # Lexicographic order of Q_3: weight formula 1 + 3 + 6 + 6 = 16.
    check(main_count(lex(3)) == 16, "Q3 lex -> 16")
    # Bipartite order of Q_3: 4 valleys + 4 odd vertices * 3 = 16.
    check(main_count(bipartite(3)) == 16, "Q3 bipartite -> 16")
    # Lexicographic order of Q_4: 1 + 4 + 12 + 24 + 24 = 65.
    check(main_count(lex(4)) == 65, "Q4 lex -> 65")
    # Bipartite order of Q_4: 8 + 8*4 = 40.
    check(main_count(bipartite(4)) == 40, "Q4 bipartite -> 40")

    for d in range(1, 10):
        w = weight_formula(d)
        check(main_count(lex(d)) == w, "lex d=%d" % d)
        check(main_count(revlex(d)) == w, "revlex d=%d" % d)
        check(main_count(by_weight(d)) == w, "weight d=%d" % d)
        check(main_count(bipartite(d)) == bipartite_formula(d), "bipartite d=%d" % d)
    check(main_count(gray(2)) == 5, "Q2 Gray -> 5")


# ---------------------------------------------------------------- B. brute-force cross-checks
def test_brute():
    # Every one of the 8! = 40320 labellings of Q_3: explicit DFS == verify.
    bad = 0
    for p in itertools.permutations(strings(3)):
        if brute_dfs(list(p)) != main_count(list(p)):
            bad += 1
    check(bad == 0, "Q3 exhaustive DFS cross-check: %d mismatches" % bad)

    rng = random.Random(20260926)
    for d, trials in [(1, 5), (2, 20), (3, 50), (4, 200), (5, 100), (6, 10)]:
        for _ in range(trials):
            rows = strings(d)
            rng.shuffle(rows)
            m = main_count(rows)
            check(brute_dfs(rows) == m, "DFS vs verify d=%d %s" % (d, rows))
            check(forward_count(rows) == m, "forward vs verify d=%d" % d)
    for d in range(1, 10):
        for _ in range(20):
            rows = strings(d)
            rng.shuffle(rows)
            check(forward_count(rows) == main_count(rows), "forward vs verify random d=%d" % d)
        for name, fn in [("lex", lex), ("revlex", revlex), ("weight", by_weight),
                         ("bipartite", bipartite), ("gray", gray)]:
            rows = fn(d)
            check(forward_count(rows) == main_count(rows), "forward vs verify %s d=%d" % (name, d))
            if d <= 5:
                check(brute_dfs(rows) == main_count(rows), "DFS vs verify %s d=%d" % (name, d))


# ---------------------------------------------------------------- C. automorphisms
def test_symmetry():
    rng = random.Random(7)
    for d in range(1, 10):
        for _ in range(5):
            rows = strings(d)
            rng.shuffle(rows)
            base = main_count(rows)
            perm = list(range(d))
            rng.shuffle(perm)
            mask = [rng.choice("01") for _ in range(d)]
            image = ["".join(str(int(s[perm[j]]) ^ int(mask[j])) for j in range(d)) for s in rows]
            check(main_count(image) == base, "automorphism invariance d=%d" % d)


# ---------------------------------------------------------------- D. command line
def run(content, extra=(), raw=False):
    fd, path = tempfile.mkstemp(suffix=".txt", dir=TMP)
    with os.fdopen(fd, "wb") as fh:
        fh.write(content if raw else content.encode("utf-8"))
    try:
        p = subprocess.run([sys.executable, VERIFY, path] + list(extra),
                           capture_output=True, text=True)
    finally:
        os.remove(path)
    return p.returncode, p.stdout.strip()


def expect_ok(content, score, what, extra=(), raw=False):
    code, out = run(content, extra, raw)
    check(code == 0 and out == "VERIFIED %d" % score, "%s: got %r exit %d" % (what, out, code))


def expect_fail(content, what, extra=(), raw=False, reason=None):
    code, out = run(content, extra, raw)
    ok = code == 1 and out.startswith("FAILED: ") and (reason is None or reason in out)
    check(ok, "%s must FAIL: got %r exit %d" % (what, out, code))


def test_cli():
    q2 = "00\n01\n11\n10\n"                            # count 5 (hand, above)
    # accepted
    expect_ok(q2, 5, "Q2 plain")
    expect_ok(q2.rstrip("\n"), 5, "Q2 no final newline")
    expect_ok(q2.replace("\n", "\r\n"), 5, "Q2 CRLF")
    expect_ok("00  \n01\t\n11 \n10\n", 5, "Q2 trailing blanks")
    expect_ok(q2, 5, "Q2 --d 2", extra=["--d", "2"])
    expect_ok(q2, 5, "Q2 --d=2", extra=["--d=2"])
    expect_ok("\n".join(gray(3)) + "\n", 21, "Q3 Gray file", extra=["--d", "3"])
    expect_ok("\n".join(lex(4)) + "\n", 65, "Q4 lex file", extra=["--d", "4"])
    # malformed
    expect_fail("", "empty file", reason="empty")
    expect_fail("\n", "single newline", reason="empty")
    expect_fail("0\n", "Q1 with one line", reason="lines")
    expect_fail("0\n1\n0\n", "Q1 with three lines", reason="lines")
    expect_fail("00\n01\n11\n", "Q2 with three lines", reason="lines")
    expect_fail("00\n01\n11\n10\n00\n", "Q2 with five lines", reason="lines")
    expect_fail("00\n01\n10\n10\n", "duplicate vertex", reason="repeats")
    expect_fail("000\n001\n010\n011\n100\n101\n110\n000\n", "Q3 duplicate, 111 missing",
                reason="repeats")
    expect_fail("00\n01\n12\n10\n", "digit 2", reason="character")
    expect_fail("00\n01\n1\n10\n", "short line", reason="length")
    expect_fail("00\n01\n111\n10\n", "long line", reason="length")
    expect_fail(" 00\n01\n11\n10\n", "leading space", reason="character")
    expect_fail("0 0\n01\n11\n10\n", "inner space", reason="character")
    expect_fail("0_0\n0_1\n1_1\n1_0\n", "underscores (int() would accept)", reason="character")
    expect_fail("+0\n+1\n", "sign character", reason="character")
    expect_fail("00\n\n01\n11\n10\n", "blank line inside", reason="empty")
    expect_fail(q2 + "\n", "extra blank line at end", reason="empty")
    expect_fail("00\r01\r11\r10\r", "CR-only line endings", reason="character")
    expect_fail("0\n1 \n", "non-ASCII byte", reason="ASCII")
    expect_fail("００\n01\n11\n10\n", "full-width digits", reason="ASCII")
    expect_fail(q2, "--d mismatch", extra=["--d", "3"], reason="--d")
    expect_fail(q2, "--d not an integer", extra=["--d", "two"], reason="--d")
    expect_fail(q2, "--d zero", extra=["--d", "0"], reason="--d")
    expect_fail(q2, "--d without value", extra=["--d"], reason="--d")
    expect_fail(q2, "--d twice", extra=["--d", "2", "--d", "2"], reason="--d")
    expect_fail(q2, "extra positional", extra=["other.txt"], reason="usage")
    p = subprocess.run([sys.executable, VERIFY], capture_output=True, text=True)
    check(p.returncode == 1 and p.stdout.startswith("FAILED: "), "no arguments must FAIL")
    p = subprocess.run([sys.executable, VERIFY, os.path.join(TMP, "does-not-exist.txt")],
                       capture_output=True, text=True)
    check(p.returncode == 1 and p.stdout.startswith("FAILED: "), "missing file must FAIL")

    # Q_9 runtime (spec: well under 10 s) and value = forward_count on the same labelling.
    rng = random.Random(9)
    rows = strings(9)
    rng.shuffle(rows)
    t0 = time.perf_counter()
    code, out = run("\n".join(rows) + "\n", ["--d", "9"])
    dt = time.perf_counter() - t0
    check(code == 0 and out == "VERIFIED %d" % forward_count(rows), "Q9 random: %r" % out)
    check(dt < 10, "Q9 runtime %.2f s" % dt)
    print("Q9 random labelling via CLI: %s in %.3f s" % (out, dt))


if __name__ == "__main__":
    t = time.perf_counter()
    for name, fn in [("hand", test_hand), ("brute", test_brute),
                     ("symmetry", test_symmetry), ("cli", test_cli)]:
        before = failed
        fn()
        print("section %-8s %s" % (name, "ok" if failed == before else "HAS FAILURES"))
    print("%s: %d/%d checks passed (%.1f s)" % ("PASS" if failed == 0 else "FAIL",
                                                passed, passed + failed, time.perf_counter() - t))
    sys.exit(0 if failed == 0 else 1)
