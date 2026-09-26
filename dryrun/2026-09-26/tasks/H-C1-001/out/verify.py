#!/usr/bin/env python3
"""Checker for H-C1: number of uphill paths of a labelling of the hypercube Q_d.

Usage:   python3 verify.py <path to Q<d>.txt> [--d D]      (also --d=D)

Artefact (TARGET): exactly 2^d lines; line i (1-based) is the 0/1 string of
length d of the vertex that gets label i.  d is inferred from the line length
and must equal D when --d is given.

Definitions (statement, verbatim in substance):
  * labelling: bijection f : V -> {1, ..., n}, here n = 2^d;
  * Q_d: vertex set {0,1}^d, u ~ v iff they differ in exactly one coordinate;
  * v is a valley iff f(w) > f(v) for every neighbour w of v;
  * uphill path: (v_1, ..., v_k), k >= 1, v_1 a valley, v_i ~ v_{i+1},
    f(v_1) < f(v_2) < ... < f(v_k); the valley alone (k = 1) counts.
Output: 'VERIFIED <number of uphill paths>' and exit 0,
        or 'FAILED: <reason>' and exit 1.
Exact Python integers throughout; no floats anywhere.

Interpretation choices (also listed as KNOWN GAPS in the report):
  * "trailing whitespace" = spaces, tabs or '\\r' at the end of a line
    (so CRLF files pass); the file may end with one final newline.  A blank
    or whitespace-only line anywhere, including an extra empty line at the
    end, leading or inner whitespace, and any character other than 0/1
    (non-ASCII included) are rejected.
  * d >= 1 (a first line of length 0 is rejected).
  * The file name (Q<d>.txt) is not checked; only the contents and --d.
"""
import sys


def parse(text, d_arg=None):
    """Return (order, d), order[i] = 0/1 string of the vertex labelled i+1.
    Raise ValueError with the exact reason if the artefact is malformed."""
    lines = text.split("\n")
    if lines[-1] == "":                  # tolerate one final newline
        lines.pop()
    if not lines:
        raise ValueError("empty file")
    lines = [ln.rstrip(" \t\r") for ln in lines]   # tolerate trailing whitespace
    d = len(lines[0])
    for i, ln in enumerate(lines, 1):
        if ln == "":
            raise ValueError(f"line {i} is blank")
        bad = [c for c in ln if c not in "01"]
        if bad:
            raise ValueError(f"line {i} contains {bad[0]!r}, only 0/1 allowed: {ln!r}")
        if len(ln) != d:
            raise ValueError(f"line {i} has length {len(ln)}, line 1 has length {d}")
    if d_arg is not None and d != d_arg:
        raise ValueError(f"lines have length {d} but --d {d_arg} was given")
    if len(lines) != 2 ** d:
        raise ValueError(f"{len(lines)} lines, expected 2^{d} = {2 ** d}")
    first = {}
    for i, ln in enumerate(lines, 1):
        if ln in first:
            raise ValueError(f"line {i} repeats line {first[ln]}: {ln}")
        first[ln] = i
    # 2^d distinct strings from {0,1}^d: every vertex appears exactly once,
    # so label(order[i]) = i + 1 is a bijection V(Q_d) -> {1, ..., 2^d}.
    return lines, d


def count_uphill(order):
    """Number of uphill paths when order[i] (a 0/1 string) gets label i + 1.

    Vertex s is encoded as the integer int(s, 2); flipping one character of s
    is flipping one bit, so the neighbours of v are v ^ (1 << j), 0 <= j < d.
    up[v] = number of sequences starting at v with adjacent consecutive
    vertices and strictly increasing labels (v alone included).  Such a
    sequence is either (v) or v followed by such a sequence starting at a
    neighbour w with f(w) > f(v), hence up[v] = 1 + sum of those up[w].
    Strictly increasing labels force distinct vertices, so these are paths.
    Uphill paths = sequences starting at a valley: sum of up[v] over valleys.
    """
    d = len(order[0])
    f = {int(s, 2): i + 1 for i, s in enumerate(order)}      # vertex -> label

    def nbrs(v):
        return [v ^ (1 << j) for j in range(d)]

    up = {}
    for s in reversed(order):            # decreasing label: higher ones done
        v = int(s, 2)
        up[v] = 1 + sum(up[w] for w in nbrs(v) if f[w] > f[v])
    return sum(up[v] for v in f if all(f[w] > f[v] for w in nbrs(v)))


def main(argv):
    path, d_arg, args = None, None, argv[1:]
    i = 0
    while i < len(args):
        a = args[i]
        if a == "--d" or a.startswith("--d="):
            if a == "--d":
                if i + 1 >= len(args):
                    return "--d needs a value"
                val, i = args[i + 1], i + 2
            else:
                val, i = a[4:], i + 1
            if d_arg is not None:
                return "--d given twice"
            if val == "" or any(c not in "0123456789" for c in val) or int(val) < 1:
                return f"bad --d value {val!r}"
            d_arg = int(val)
        elif path is None and not a.startswith("--"):
            path, i = a, i + 1
        else:
            return f"unexpected argument {a!r}"
    if path is None:
        return "usage: verify.py <artefact file> [--d D]"
    try:
        with open(path, "rb") as fh:
            raw = fh.read()
    except OSError as e:
        return f"cannot read {path}: {e}"
    try:
        text = raw.decode("ascii")
    except UnicodeDecodeError as e:
        return f"non-ASCII byte at offset {e.start}"
    try:
        order, d = parse(text, d_arg)
    except ValueError as e:
        return str(e)
    print(f"VERIFIED {count_uphill(order)}")
    return None


if __name__ == "__main__":
    err = main(sys.argv)
    if err is not None:
        print(f"FAILED: {err}")
        sys.exit(1)
    sys.exit(0)
