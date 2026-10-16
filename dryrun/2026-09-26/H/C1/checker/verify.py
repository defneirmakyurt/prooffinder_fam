#!/usr/bin/env python3
"""
verify.py -- checker for "Uphill Paths on the Hypercube" (cell C1: U(Q_3), U(Q_4);
works for any Q_d with d >= 1).  Python standard library only, exact integers.

Usage:   python3 verify.py <artefact.txt> [--d D]      (also accepts --d=D)
Output:  "VERIFIED <number of uphill paths>"  exit 0,   or   "FAILED: <reason>"  exit 1.

ARTEFACT FORMAT (hand-in: "a list of the 2^d vertices in increasing label order,
written as 0/1 strings"): exactly 2^d lines; line i (1-based) is the 0/1 string of
length d of the vertex that gets label i.  d is read off the length of line 1 and must
equal --d when that is given.

DEFINITIONS, exactly as in the statement:
  Q_d        vertex set {0,1}^d; v ~ w iff v and w differ in exactly one coordinate.
  labelling  a bijection f : V -> {1,...,n}, n = 2^d.  Here f(v) = line number of v.
  valley     v such that every neighbour w of v has f(w) > f(v) (isolated vertex counts;
             Q_d with d >= 1 has none).
  uphill     a sequence (v_1,...,v_k), k >= 1, with v_1 a valley, v_i ~ v_{i+1} for each i,
  path       and f(v_1) < ... < f(v_k).  A valley alone (k = 1) is an uphill path.
The score is the number of uphill paths of the given labelling.

COUNTING.  Let N(v) = number of uphill paths ending at v.  The only path with k = 1 ending
at v is (v), and it is uphill iff v is a valley.  A path with k >= 2 ending at v is uphill
iff dropping v leaves an uphill path ending at some w ~ v with f(w) < f(v).  Hence
      N(v) = [v is a valley] + sum of N(w) over neighbours w of v with f(w) < f(v),
and the score is the sum of N(v) over all v.  Vertices are processed in increasing label
order (= file order), so every N(w) on the right is already known.

INTERPRETATION CHOICES (see KNOWN GAPS in the report):
  * Whitespace: trailing spaces, tabs and CR (from CRLF) at the end of a line are ignored,
    and the file may end with one final newline.  Everything else is FAILED: leading or
    inner spaces, blank lines (including a second newline at the end of the
    file), non-ASCII bytes, any character other than 0 and 1.
  * The checker counts uphill paths of ONE labelling.  It does not (and cannot) check the
    lower-bound half of "determine U(Q_d)".
"""
import re
import sys


def parse(text, d_expected=None):
    """Return (d, order): order[i-1] is the vertex that gets label i, encoded as the int
    whose binary digits are its 0/1 string.  Raise ValueError(reason) on bad input."""
    if text.endswith("\n"):
        text = text[:-1]                           # one final newline is tolerated
    rows = [line.rstrip(" \t\r") for line in text.split("\n")]  # trailing blanks tolerated
    for i, r in enumerate(rows, 1):
        if r == "":
            raise ValueError("line %d is empty" % i)
        if any(c not in "01" for c in r):
            raise ValueError("line %d contains a character other than 0 and 1: %r" % (i, r))
    d = len(rows[0])
    for i, r in enumerate(rows, 1):
        if len(r) != d:
            raise ValueError("line %d has length %d but line 1 has length %d" % (i, len(r), d))
    if d_expected is not None and d != d_expected:
        raise ValueError("strings have length d = %d but --d %d was given" % (d, d_expected))
    if len(rows) != 2 ** d:
        raise ValueError("found %d lines, expected 2^%d lines" % (len(rows), d))
    first_line = {}
    for i, r in enumerate(rows, 1):
        if r in first_line:
            raise ValueError("line %d repeats vertex %s from line %d" % (i, r, first_line[r]))
        first_line[r] = i
    # 2^d distinct strings of length d over {0,1}: every vertex of Q_d appears exactly once.
    return d, [int(r, 2) for r in rows]


def count_uphill(d, order):
    """Number of uphill paths of the labelling f(order[i-1]) = i of Q_d (exact int)."""
    n = len(order)
    f = [0] * n
    for i, v in enumerate(order, 1):
        f[v] = i
    N = [0] * n                                    # N[v] = uphill paths ending at v
    total = 0
    for v in order:                                # increasing label order
        nbrs = [v ^ (1 << j) for j in range(d)]    # differ in exactly one coordinate
        valley = all(f[w] > f[v] for w in nbrs)
        N[v] = (1 if valley else 0) + sum(N[w] for w in nbrs if f[w] < f[v])
        total += N[v]
    return total


def fail(reason):
    print("FAILED: " + reason)
    sys.exit(1)


def main(argv):
    if hasattr(sys, "set_int_max_str_digits"):
        sys.set_int_max_str_digits(0)              # allow printing huge exact counts
    args = list(argv[1:])
    d_expected = None
    rest = []
    k = 0
    while k < len(args):
        a = args[k]
        if a == "--d" or a.startswith("--d="):
            if a == "--d":
                if k + 1 >= len(args):
                    fail("--d needs a value")
                val, k = args[k + 1], k + 2
            else:
                val, k = a[len("--d="):], k + 1
            if d_expected is not None:
                fail("--d given more than once")
            if not re.fullmatch(r"[0-9]+", val) or int(val) < 1:
                fail("--d must be a positive integer, got %r" % val)
            d_expected = int(val)
        else:
            rest.append(a)
            k += 1
    if len(rest) != 1:
        fail("usage: verify.py <artefact.txt> [--d D]")
    try:
        with open(rest[0], "rb") as fh:
            raw = fh.read()
    except OSError as e:
        fail("cannot read %s: %s" % (rest[0], e))
    try:
        text = raw.decode("ascii")
    except UnicodeDecodeError:
        fail("file is not plain ASCII")
    try:
        d, order = parse(text, d_expected)
    except ValueError as e:
        fail(str(e))
    print("VERIFIED %d" % count_uphill(d, order))
    sys.exit(0)


if __name__ == "__main__":
    main(sys.argv)
