# Runlog: H-C1-006 (literature, phase 1L)

PYTHON = /Users/raducucu/bainsahackathon/.venv/bin/python3. All code in out/code/ is stdlib-only
and runs under plain python3 as well. All arithmetic is exact Python integer arithmetic; no float
enters any claim (the only randomness is `random.Random(seed)` with seeds 0.. in q4_upper.py and
seed 20260926 in identity_check.py, and randomness only proposes candidates -- every reported value
is recomputed exactly). Runtimes measured with `/usr/bin/time -p`, `real` reported.
CWD for every command: /Users/raducucu/bainsahackathon/run/tasks/H-C1-006/out/code/

| # | command | range covered | status | real | result |
|---|---|---|---|---|---|
| 1 | `python3 uphill.py ../Q3.txt 3` | the single labelling in out/Q3.txt | COMPLETED | 0.02 s | `uphill_paths=14 (recurrence) =14 (explicit enumeration) valleys=1 local_maxima=2` |
| 2 | `python3 q3_exhaustive.py ../Q3.txt` | ALL 8! = 40320 labellings of Q_3, no symmetry reduction | COMPLETED | 0.09 s (0.12 s on re-run without writing) | `min = 14`; distribution `[(14,7104),(16,14112),(17,6720),(18,4704),(19,576),(20,3648)]`; wrote ../Q3.txt |
| 3 | `python3 q4_upper.py 4 34 ../Q4.txt` | heuristic local search over labellings of Q_4, seeds 0..39, stops at the first seed reaching 34 | COMPLETED | 0.02 s (0.04 s on re-run without writing) | `best found: 34` with seed 0; wrote ../Q4.txt. NOT exhaustive: it certifies only the upper bound |
| 4 | `python3 uphill.py ../Q4.txt 4` | the single labelling in out/Q4.txt | COMPLETED | 0.01-0.03 s | `uphill_paths=34 (recurrence) =34 (explicit enumeration) valleys=2 local_maxima=6` |
| 5 | `python3 identity_check.py` | 2000 random labellings for each d = 2,3,4,5 plus ALL 8! labellings of Q_3 | COMPLETED | 0.48-0.59 s | identities (I1) `total = #valleys + sum_v N(v)*up(v)` and (I2) `|E| = sum_v down(v)` hold in every case, as does `total >= |E| + #valleys` |

The lower bounds U(Q_3) >= 14 and U(Q_4) >= 34 are NOT obtained from any of these runs: they are
proved by hand in out/proof.md (Steps 1-7). Run 2 is an independent confirmation for d = 3 only;
run 5 is a sanity check of the two identities the proof uses; runs 1, 3, 4 certify the upper bounds.

Total rerun cost for a judge: runs 1-5, under 1 second.
