# Run log H-C5-001 (searcher, BLIND, phase 1, UPPER route)

Reading of the brief: UPPER route only; target = labelling of Q_9 with <= 2399 uphill paths, scored by
inbox/checker/verify.py. No ambiguity found. Time box 13:10 - 14:25 UTC.

## Method
1. Proved the reduction (reduction.md): total = 2^d + (d-1)|S| + sum_{S-edges}(N(w)-2) >= 512 + 8|S| for
   d = 9, S = {v : N(v) >= 2} a feedback vertex set (FVS); and an independent FVS (IFVS) S gives a labelling
   with exactly 512 + 8|S|.  So the target needs an FVS of size <= 235; with an IFVS of size <= 235 it is met.
2. Searched for (I)FVS of Q_9 of size <= 235: SAT with lazy cycle cuts (full, symmetry-restricted, parity-
   restricted), SA over independent sets (fixed / variable size), SA over plain FVS, SA over arbitrary S
   scored by the exact uphill count.

Timings: "wall" = bash `time` real; "cpu" = the program's own clock() limit (process was run alone,
but the machine is shared). Python SAT "t=" = time.time() inside the script.

## Runs (all d = 9 unless stated)
| # | command (from out/) | range | status | measured time | result |
|---|---|---|---|---|---|
| 1 | ifvs_sat.py --d D --K k (no group), D=3,4,5, k=2.. until FOUND | d=3..5 | COMPLETED | internal 0.0-0.1 s each (wall not measured) | min IFVS 3, 6, 14; builder+checker: VERIFIED 14, 34, 88 (= 2^d+(d-1)|S|) |
| 2 | ifvs_sat.py --d 6 --K 26/27/28 | d=6 | COMPLETED | wall 0.07/0.08/0.06 s | UNSAT, UNSAT, FOUND 28 |
| 3 | ifvs_sat.py --d 7 --K 55/56 | d=7 | COMPLETED | wall 0.25/0.07 s | UNSAT, FOUND 56 |
| 4 | ifvs_sat.py --d 8 --K 111/112 | d=8 | COMPLETED | wall 4.9/0.14 s | UNSAT (30 iters, 1567 cycle clauses), FOUND 112 |
| 5 | ifvs_sat.py --d 9 --K 235 (no group) | K=235 | TIMED OUT | wall 9m40s | 120 lazy iterations by 22.9 s (4678 cycle clauses), then one SAT call did not return |
| 6 | code/symbatch.sh: 12 groups (comp, cyc9, cyc3, swap4, t2, swap4t, cyc9comp, cyc3t, rev, cyc8, cyc8t, cyc7), K=235 | G-invariant IFVS | COMPLETED | wall 0.23-25.2 s each | all 12 UNSAT (no DRAT; exploratory only) |
| 7 | ifvs_ls 9 235 1 90 2 0.1 | K=235 | COMPLETED (time limit, target not hit) | wall 1m36s, cpu 90 s, 7.4e8 iters | best c=89 vs needed 88 (rank 1) |
| 8 | ifvs_ls 9 235 2 150 1.0 0.2 | K=235 | COMPLETED (time limit, target not hit) | wall 2m31s, cpu 150 s, 1.2e9 iters | best c=89 (rank 1) |
| 9 | ifvs_ls 9 236 3 60 1.0 0.2 | K=236 | COMPLETED (target hit) | wall 48.6 s, 4.0e8 iters | IFVS |S|=236 (all even), -> Q9.txt, VERIFIED 2400 |
| 10 | ifvs_ls2 D K 1 20 12 4 0.5 0 for (6,28),(7,56),(8,112) | d=6,7,8 | COMPLETED | cpu 0.0/20/20 s | d=6 found 28; d=7,8 stuck on small maximal mixed independent sets |
| 11 | ls3 9 1 20 1.5 0.3 S236 2399 | exact-count SA | COMPLETED (time limit) | cpu 20 s, 2.6e6 evals | best 2400 (internal count = checker 2400) |
| 12 | ls3 9 2 150 6 0.7 S236 2399 | exact-count SA | COMPLETED (time limit) | wall 2m31s, 1.9e7 evals | best 2400 -> Q9_ls3.txt VERIFIED 2400 |
| 13 | ifvs_sat.py --d 9 --K 235 --mixed | IFVS containing 0 and an odd vertex | COMPLETED | wall 3.8 s, 131 iters, 4881 cycle clauses | UNSAT (no DRAT; exploratory only) |
| 14 | ifvs_sat.py --d 9 --K 235 --evenonly | IFVS inside even class | TIMED OUT | wall 5m30s | no answer |
| 15 | ifvs_sat.py --d 9 --K 235 --noindep | plain FVS | TIMED OUT | wall 3m20s | 40 iterations, models of size 235 with ~200 cycles |
| 16 | fvs_ls D K 1 10 10 3 0.3 1 for (6,26),(7,50),(8,105) | plain FVS, d=6,7,8 | COMPLETED (time limit) | cpu 10 s each | best 28, 56, 112 (never below the IFVS values) |
| 17 | ifvs_sat.py --d 5/6/7 --K 13/27/55 --noindep | plain FVS | COMPLETED/COMPLETED/TIMED OUT | wall 0.26 s / 17.0 s / 1m50s | UNSAT, UNSAT, timeout (no DRAT) |
| 18 | fvs_ls 9 235 5 120 10 3 0.3 1 | plain FVS | TIMED OUT (killed by 130 s wall timeout) | wall 2m10s | last log line: best |S|=236 rank 0 |
| 19 | fvs_ls 9 235 6 150 9 4 0.5 0 | plain FVS from empty | COMPLETED (time limit) | wall 3m10s, cpu 150 s, 5.3e7 iters | best |S|=236 rank 0 (234 even + 2 odd, non-independent) |
| 20 | code/symbatch_fvs.sh: same 12 groups, plain FVS (--noindep), K=235, 40 s cap each | G-invariant FVS | COMPLETED batch (wall 6m43s) | per group 1.3-45 s | UNSAT: t2, cyc9comp, cyc7 (exploratory, no DRAT); TIMEOUT: the other 9; nothing found |

Seeds: as given in the command lines (3rd argument of the C programs; SAT runs are deterministic).
Best score per method: IFVS-SA (run 9) 2400; exact-count SA (run 12) 2400. Nothing <= 2399 found.

## Hand-in
out/Q9.txt = out/best.txt = out/Q9_ifvsLS.txt (from run 9 via build_labelling.py; S saved as
S236_ifvsLS.txt); out/Q9_ls3.txt (run 12). Checker: VERIFIED 2400 for each. Target (<= 2399) NOT met.
