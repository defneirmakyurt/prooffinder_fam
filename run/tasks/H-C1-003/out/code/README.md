# Code: H-C1-003 (U(Q_3), U(Q_4))

Stdlib-only Python 3, exact integer arithmetic. Everything below runs in well under 10 minutes
(total for the whole reproduction script: about 15 s, dominated by the heuristic search).
`PY` below is any Python 3; the brief's interpreter works:
`PY=/Users/raducucu/bainsahackathon/.venv/bin/python3`.

## Files
* `uphill.py` -- shared helpers. Vertices of Q_d are ints 0..2^d-1 (bit j = coordinate j);
  v ~ w iff v XOR w is a power of two. An "order" is the vertex list in increasing label order.
  - `count_uphill(d, order)` -- fast scorer by the recurrence
    `N(v) = [v is a valley] + sum_{w ~ v, f(w) < f(v)} N(w)`, score = `sum_v N(v)`.
  - `brute_paths(d, order)` -- independent slow count: enumerates every uphill path explicitly
    by DFS from each valley. Used only to cross-check the recurrence.
* `brute_q3.py` -- exhaustive over ALL 8! = 40320 labellings of Q_3, no symmetry reduction.
* `search_q4.py` -- heuristic upper-bound search (seeded random restarts + first-improvement
  transposition local search + kicks). Not exhaustive; only produces candidates.
* `dp_lower.py` -- exact prefix dynamic programme deciding "is there a labelling of Q_d with at
  most T uphill paths?", with state merging and the lower-bound pruning described below.
* `bb_lower.py` -- the same decision problem by a plain depth-first branch and bound with NO
  state merging, written separately as an independent check of `dp_lower.py`.
* `check_artefacts.py` -- re-counts `out/Q3.txt` and `out/Q4.txt` two ways and compares.

## Reproduce everything
```
PY=python3
$PY brute_q3.py /tmp/Q3.txt                 # -> min 14, writes a minimiser        (~0.2 s)
$PY dp_lower.py 4 33 --no-fix               # -> "no labelling ... => U(Q_4) >= 34" (~0.1 s)
$PY bb_lower.py 4 33 --no-fix               # -> "NONE ... => U(Q_4) >= 34"         (~1.3 s)
$PY dp_lower.py 4 34 /tmp/Q4.txt            # -> "found labelling with 34 ..."      (~0.3 s)
$PY dp_lower.py 3 13 --no-prune --no-fix    # -> none (cross-check of Q_3)          (~0.1 s)
$PY check_artefacts.py ../Q3.txt ../Q4.txt  # -> 14 and 34, both counting methods   (~0.1 s)
$PY ../../inbox/checker/verify.py ../Q3.txt --d 3   # -> VERIFIED 14
$PY ../../inbox/checker/verify.py ../Q4.txt --d 4   # -> VERIFIED 34
$PY search_q4.py 4 200 1 /tmp/q4.txt        # -> best 34 (heuristic, seeded)        (~11 s)
```

## Why the searches prove the lower bounds
Both `dp_lower.py` and `bb_lower.py` build a labelling by choosing the vertices in increasing
label order, so after k steps the placed set S carries labels 1..k and N(w) is already final for
every w in S. Writing `A(v) = sum_{w in S, w ~ v} N(w)` for unplaced v, the full derivation in
`../claims.md` shows that for EVERY completion

    sum_{v unplaced} N(v)  >=  sum_{v unplaced} A(v)
                               + sum_{edges uv inside the unplaced set} min(max(1,A(u)), max(1,A(v))),

using only `N(x) >= 1` and `N(x) >= A(x)`. So cutting a branch whose running total plus this
bound exceeds T discards no labelling of score <= T. `dp_lower.py` additionally merges partial
labellings with the same (S, N restricted to the boundary of S), which `../claims.md` proves
lossless; `bb_lower.py` does no merging, which is why the two programs agreeing on
"nothing at T = 33 for d = 4" is a real cross-check.

`--no-fix` disables the (separately proved, and unnecessary) reduction that puts label 1 at
0...0; the reported lower-bound runs use `--no-fix`, so they range over all labellings.
