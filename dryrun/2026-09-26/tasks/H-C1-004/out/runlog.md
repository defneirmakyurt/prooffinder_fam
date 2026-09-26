# Runlog: H-C1-004

Machine: macOS (darwin 25.6.0), laptop.  PYTHON = /Users/raducucu/bainsahackathon/.venv/bin/python3
(only stdlib is used; plain python3 would work too).  All runtimes measured with `/usr/bin/time -p`,
`real` reported.  CWD for every command below: /Users/raducucu/bainsahackathon/run/tasks/H-C1-004/

## Method

1. Re-derived the counting recursion N(v) = [v valley] + sum of N over lower neighbours (out/claims.md R2)
   and implemented it independently in out/code/uphill.py.
2. Q_3: full enumeration of all 8! bijections (out/code/brute_q3.py).
3. Q_4 upper bound: simulated annealing with transposition moves (out/code/sa_q4.py), 20 seeds.
4. Q_4 lower bound: depth-first branch and bound over all 16! bijections (out/code/bnb.py), building
   the labelling one label at a time, with (a) a trivial prune cost + N(v) >= T, (b) an admissible
   lower bound LB(S) on the cost of the unplaced part (proved in out/claims.md R5), and (c) an
   optional state memo (proved in out/claims.md R6, switchable off with --nomemo).
   The headline lower-bound run uses --nomemo, so it depends only on (a) and (b).
5. Everything cross-checked: internal counter vs the provided checker on random labellings; the
   branch and bound against the full Q_3 enumeration; the branch and bound against itself with each
   prune switched off; a sweep over the threshold T.

## Runs

| # | command | range covered | status | real time | result |
|---|---|---|---|---|---|
| 1 | `$PY inbox/checker/verify.py out/tmp/q3_weight.txt --d 3` | one labelling of Q_3 | COMPLETED | 0.04 s | `VERIFIED 16` (matches the hand computation 1+3+6+6) |
| 2 | `$PY out/code/brute_q3.py out/tmp/q3_brute.txt` | all 8! = 40320 bijections of Q_3 | COMPLETED | 0.25 s | `min = 14  #minimisers = 7104`; histogram tail `[(14,7104),(16,14112),(17,6720),(18,4704),(19,576)]` |
| 3 | `$PY out/code/sa_q4.py 4 20 out/tmp/q4_sa.txt 60000` | Q_4, seeds 0..19, 60000 iters each, T0=3.0 -> T1=0.05 geometric | COMPLETED | 13.11 s | every seed reaches 34, `overall best 34` |
| 4 | `$PY out/code/bnb.py 3 14` | all 8! bijections of Q_3 | COMPLETED | 0.03 s | `NONE BELOW 14`, 385 nodes |
| 5 | `$PY out/code/bnb.py 3 15` | all 8! bijections of Q_3 | COMPLETED | 0.02 s | `FOUND 14` + labelling |
| 6 | `$PY out/code/bnb.py 3 14 --nomemo` | all 8! bijections of Q_3 | COMPLETED | 0.04 s | `NONE BELOW 14`, 1841 nodes |
| 7 | `$PY out/code/bnb.py 3 14 --nolb` | all 8! bijections of Q_3 | COMPLETED | 0.03 s | `NONE BELOW 14`, 3457 nodes |
| 8 | `$PY out/code/bnb.py 3 14 --nomemo --nolb` | all 8! bijections of Q_3, no LB and no memo | COMPLETED | 0.10 s | `NONE BELOW 14`, 59681 nodes |
| 9 | **`$PY out/code/bnb.py 4 34 --nomemo`** | **all 16! = 20922789888000 bijections of Q_4** | **COMPLETED** | **0.85 s** | **`NONE BELOW 34`, 135169 nodes** |
| 10 | `$PY out/code/bnb.py 4 34` | all 16! bijections of Q_4 | COMPLETED | 0.09 s | `NONE BELOW 34`, 9425 nodes, 2120 memo hits |
| 11 | `$PY out/code/bnb.py 4 34 --nolb` | Q_4, memo only | TIMED OUT (cut at 10 min) | > 600 s | no verdict; the memo alone is not enough.  Not used for any claim. |
| 12 | `$PY out/code/bnb.py 4 35` | Q_4 | COMPLETED | 0.03 s | `FOUND 34` + labelling, 47 nodes |
| 13 | `$PY out/code/bnb.py 4 35 --nomemo --nolb` | Q_4, no LB and no memo | COMPLETED | 451.59 s | `FOUND 34`, 160457098 nodes |
| 14 | `$PY out/code/bnb.py 4 35 --out out/Q4.txt` | Q_4 | COMPLETED | < 0.1 s | wrote out/Q4.txt |
| 15 | `$PY out/code/bnb.py 3 15 --out out/Q3.txt` | Q_3 | COMPLETED | < 0.1 s | wrote out/Q3.txt |
| 16 | `$PY inbox/checker/verify.py out/Q3.txt --d 3` | the artefact | COMPLETED | < 0.1 s | `VERIFIED 14` |
| 17 | `$PY inbox/checker/verify.py out/Q4.txt --d 4` | the artefact | COMPLETED | < 0.1 s | `VERIFIED 34` |
| 18 | `$PY out/code/crosscheck.py counter 3 300 inbox/checker/verify.py` | 300 random labellings of Q_3, seed 12345 | COMPLETED | 9.54 s | `mismatches=0` |
| 19 | `$PY out/code/crosscheck.py counter 4 300 inbox/checker/verify.py` | 300 random labellings of Q_4, seed 12345 | COMPLETED | 8.75 s | `mismatches=0` |
| 20 | `$PY out/code/crosscheck.py sweep 3 16` | T = 1..16 on Q_3 | COMPLETED | 0.38 s | `NONE BELOW T` for T = 1..14, `FOUND 14` for T = 15,16 |
| 21 | `for T in 30..36: $PY out/code/bnb.py 4 $T` | T = 30..36 on Q_4 | COMPLETED | < 1 s total | `NONE BELOW T` for T = 30..34, `FOUND 34` for T = 35,36 |

Seeds: brute force and branch and bound are deterministic (no randomness).  Annealing used seeds
0..19 (Python `random.Random(seed)`).  The cross-check sampler used seed 12345.

## Best score per run

Run 2 (Q_3 full enumeration): 14.  Run 3 (Q_4 annealing): 34, every seed.  Runs 12/13 (Q_4 branch
and bound with T = 35): 34.  No run of anything ever produced a labelling of Q_3 below 14 or of Q_4
below 34, and runs 2, 4, 6, 7, 8, 9, 10 prove that none exists.

## Judge rerun budget

The two runs a judge must rerun to reproduce the claim are
`bnb.py 3 14 --nomemo --nolb` (0.10 s) and `bnb.py 4 34 --nomemo` (0.85 s), plus
`bnb.py 3 15 --out ...` / `bnb.py 4 35 --out ...` and the provided checker.  Under 5 seconds total,
well inside the 10 minute budget.  Everything uses exact Python integers.

## Interpretation choices

The brief's artefact format and the provided checker's format agree exactly, so no choice was
needed: `Q<d>.txt` has 2^d lines, line i is the 0/1 string of the vertex with label i, most
significant bit = coordinate d-1 (this convention is irrelevant to the count, since relabelling the
coordinates is a graph automorphism of Q_d).
