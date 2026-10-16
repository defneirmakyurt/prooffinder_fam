# runlog H-C1-002 (checker-builder, clean-room)

All runs are from /Users/raducucu/bainsahackathon/run/tasks/H-C1-002/out, on Python 3.14.0.

1. `/usr/bin/time -p python3 tests.py`
   Output: all four sections ok (hand, brute, symmetry, cli). "Q9 random labelling via CLI: VERIFIED 106426 in 0.030 s". "PASS: 1175/1175 checks passed (3.5 s)".
   real 3.61 s, user 2.89 s, sys 0.34 s. COMPLETED.
   Coverage: all labellings of Q_1 (2) and Q_2 (24) checked against hand values; all 8! = 40320 labellings of Q_3 checked with explicit DFS against verify;
   random labellings of d=1..6 checked with DFS and forward recursion; d=1..9 checked with forward recursion and the structured orders (lex, revlex, weight, bipartite, Gray);
   closed formulas for d=1..9; automorphism invariance for d=1..9; 8 accepted and 26 malformed CLI inputs plus the no-argument and missing-file cases; Q_9 runtime.

2. `/usr/bin/time -p /Users/raducucu/bainsahackathon/.venv/bin/python3 tests.py`
   Output: "PASS: 1175/1175 checks passed (3.0 s)". real 3.08 s. COMPLETED.

3. Mutation check (scratch copies in tmp/mut, removed afterwards). Each mutant of verify.py was run against tests.py:
   - valley `all` -> `any`: FAIL 177/1175 (caught)
   - valley term dropped: FAIL 74/1175 (caught)
   - `f[w] < f[v]` -> `f[w] <= f[v]`: PASS 1175/1175. This is an equivalent mutant, because w != v and labels are distinct.
   - line-count check disabled: FAIL 1171/1175 (caught)
   - duplicate check disabled: FAIL 1173/1175 (caught)
   COMPLETED, about 3 s each.

4. `/usr/bin/time -p python3 verify.py tmp/gray3.txt --d 3` (Q_3 Gray order): `VERIFIED 21`, exit 0, real 0.02 s. This matches the hand value.
   `python3 verify.py tmp/dup2.txt`: `FAILED: line 4 repeats vertex 10 from line 3`, exit 1. COMPLETED.
