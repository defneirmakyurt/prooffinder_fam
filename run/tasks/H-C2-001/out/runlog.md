# Runlog H-C2-001 (U(Q_5)), BLIND, phase 1

Interpretation: exactly the statement's definitions (valley = all neighbours have larger label; lone
valley is a path; paths counted as vertex sequences). No ambiguity found.
Timing: bash `time` (real = wall clock); /usr/bin/time is not installed on this machine. Machine is
shared (load average ~6 on 4 cores during the runs), so wall times are indicative.

## Checker sanity (R1)
- Q_2 lex order 00,01,10,11: by hand N = 1,1,1,2, T = 5. Checker: `VERIFIED 5`.

## Upper bound: simulated annealing (code/anneal.c)
Method: state = label order; moves = swap two positions or move one vertex to another position (50/50);
Metropolis acceptance on T; temperature 3.0 -> 0.05 geometric; start = random permutation from seed.
| run | d | seed | iterations | real time | internal best | checker on output |
|---|---|---|---|---|---|---|
| A3-1..3 | 3 | 1,2,3 | 2e5 each | 0.03 s each | 14 | VERIFIED 14 (each) |
| A4-1..3 | 4 | 1,2,3 | 2e6 each | 0.45-0.50 s each | 34 | VERIFIED 34 (each) |
| A5-1 | 5 | 1 | 2e7 | 7.57 s | 88 | VERIFIED 88  -> out/Q5.txt = out/best.txt |
| A5-2 | 5 | 2 | 2e7 | 7.53 s | 88 | VERIFIED 88  -> out/Q5_alt1.txt |
| A5-3 | 5 | 3 | 2e7 | 7.63 s | 88 | VERIFIED 88 |
| A5-4 | 5 | 4 | 2e7 | 7.60 s | 88 | VERIFIED 88 |
| A5-5 | 5 | 5 | 2e7 | 7.79 s | 88 | VERIFIED 88 |
| A5-6 | 5 | 6 | 2e7 | 7.53 s | 88 | VERIFIED 88 |
Stopping condition for the upper half met: 6 independent seeds, none below 88 (and 88 is proved optimal).
Seeds 1 and 2 re-run: outputs byte-identical to the saved files (deterministic).
Structure: Q5.txt has 8 valleys, 10 non-valleys with N=1, 14 local maxima (N=5); excess X = 8 valleys.
Q5_alt1.txt has 5 valleys, 13 non-valleys with N=1, one vertex with N=2, up=3 (cost 3), 13 local maxima;
X = 5 + 3 = 8. The two are structurally different (different valley counts, so not related by an
automorphism).

## Lower bound: exact layered DP (code/lbdp.c; argument in out/proof.md)
All: states = (placed set, N-values of placed vertices with unplaced neighbours), min cost per state,
vertex 0 gets label 1 (translation symmetry). "states visited" = sum of layer sizes (stored states).
| run | command | result | status | real time | states visited |
|---|---|---|---|---|---|
| L3a | ./lbdp 3 1 0 | no labelling with X<=1 | COMPLETED | 0.002 s | 29 |
| L3b | ./lbdp 3 2 0 / 3 5 0 | minimal X = 2 (U(Q_3)=14) | COMPLETED | 0.002 s | 193 / 504 |
| L3c | ./lbdp 3 1 1, 3 2 1, 3 5 1 | same answers | COMPLETED | 0.002 s | 5 / 21 / 48 |
| B3 | python3 brute_q3.py (all 40320 labellings, independent) | min T = 14 (7104 attain) | COMPLETED | 0.46 s | 40320 labellings |
| L4a | ./lbdp 4 1 0 | no labelling with X<=1 | COMPLETED | 0.002 s | 212 |
| L4b | ./lbdp 4 2 0 / 4 4 0 | minimal X = 2 (U(Q_4)=34) | COMPLETED | 0.005 / 0.023 s | 2289 / 10362 |
| L4c | ./lbdp 4 1 1 / 4 2 1 / 4 4 1 | same | COMPLETED | <0.01 s | 8 / 59 / 168 |
| L4d | ./lbdp 4 7 1 0 ; ./lbdp 4 7 0 1 | minimal X = 2 | COMPLETED | <0.1 s | 2950 / 98790 |
| **L5-H** | **./lbdp 5 7 0 1** (translations only, heuristic on), first code version | **no labelling of Q_5 has X<=7 (T<=87)**; layer 27 empty | COMPLETED | 3m01.5s | 18,696,829 |
| **L5-H'** | same command, FINAL code (SYM=0 path unchanged) | same, identical state count | COMPLETED | 2m40.3s | 18,696,829 |
| L5-S(v1) | ./lbdp 5 7 1 1, first canon (lex-min code vector over 3840 automorphisms) | same; layer 27 empty | COMPLETED | 15.9 s | 19,262 |
| L5-S(v2) | ./lbdp 5 7 1 1, intermediate canon (byte tables) | same; layer 27 empty | COMPLETED | 8.2 s | 19,510 |
| **L5-S** | ./lbdp 5 7 1 1, FINAL code (Gray-code canon, same representatives as v2) | same; layer 27 empty | COMPLETED | 1.3 s | 19,510 |
| L5-S0(v1) | ./lbdp 5 7 1 0, first canon | reached layer 10 (53,066 states) | PARTIAL (killed by me to switch to faster canon) | ~2.5 min | n/a |
| L5-S0(v2) | ./lbdp 5 7 1 0, byte-table canon | reached layer 11 (109,365 states) | PARTIAL (killed by me, cache-bound) | ~2.5 min | n/a |
| **L5-S0** | ./lbdp 5 7 1 0, FINAL code (heuristic OFF) | no labelling of Q_5 has X<=7 (T<=87); layer 30 empty | COMPLETED | 1m15.7s | 1,567,313 |
| L5-8 | ./lbdp 5 8 1 1 (sanity, final code) | minimal X = 8, U = 88: the DP itself finds the optimum | COMPLETED | 2.2 s | 38,006 |

Representative choice changes the greedy matching, hence slightly different state counts between v1 and
v2 with the heuristic on (19,262 vs 19,510); with the heuristic off the layer counts are representative-
independent, and v1/v2/final agree on every layer they reached (1,5,11,56,191,734,2468,7799,21755,53066,109365).
FINAL code = out/code/lbdp.c as saved; v1/v2 differ only in canon() (earlier revisions, not kept).
Small cases re-run with the final binary: ./lbdp 3 5 0 -> X=2 (504 states); ./lbdp 4 5 0 -> X=2 (32372);
./lbdp 4 4 0 -> X=2 (10362); ./lbdp 4 2 0 -> X=2 (2289). python3 check_identity.py: 1800 random
labellings d=1..6, 0 failures (0.2 s).

Headline lower-bound runs (two, with disjoint extra assumptions; the conclusion T >= 88 holds if
EITHER extra assumption is sound):
- L5-H rests on: the DP reduction (proof.md Lemmas 1-3, sequential form, state lemma) + translation
  reduction to f(00000)=1 + admissibility of the matching bound h (Lemma 4). No orbit-merging code.
- L5-S0 rests on: the DP reduction + orbit merging under the 3840 automorphisms (proof.md Symmetry (i),(ii)).
  No heuristic (Lemma 4 not used).
Both are exhaustive over all 32! labellings of Q_5 through the reduction; neither is time-limited.
Layer sizes L5-H: 1, 31, 485, 4995, 34035, 150616, 476062, 1080971, 1783317, 2252506, 2316439, 2134755,
1855895, 1583055, 1329070, 1084411, 856235, 648575, 464645, 307340, 182650, 94340, 40565, 13075, 2555,
205, 0 (layers 1..27).
Layer sizes L5-S(v1): 1, 5, 11, 53, 150, 433, 934, 1675, 2283, 2543, 2353, 2024, 1640, 1319, 1045, 825, 637,
479, 340, 227, 141, 80, 39, 16, 7, 2, 0.
Note: while L5-S0(v1) was running, two 7-second annealing re-runs (reproducibility check) ran concurrently.
