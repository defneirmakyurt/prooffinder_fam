# Runlog: H-C4-001 (searcher, BLIND, phase 1)

Reading of the brief: "out/best.<ext>" is realised as the two files TARGET requires, out/Q7.txt and
out/Q8.txt (one artefact per d); alternates Q7_alt1.txt, Q8_alt1.txt as the brief's HAND-IN FILES
line asks. Wall times measured with `date +%s.%N` before/after each command (/usr/bin/time is
not installed on this machine). Machine shared (load average up to ~6 on 4 cores during runs).

## Method
1. Written reduction (claims.md, Lemma A): #uphill >= 2^d + (d-1)|S| where S = {down >= 2} and
   V \ S induces a forest. So the search targets small vertex sets S whose complement induces a
   forest, preferably with S independent (then the decoded labelling has exactly 2^d + (d-1)|S|).
2. code/fvs_sa.c: simulated annealing (geometric temperature 2.0 -> 0.05) over subsets S, moves =
   flip one vertex or swap a vertex with a neighbour of the other status, objective
   (d-1)|S| + d*cyc(T) + mu*e(S); best acyclic state decoded (T trees in BFS order, then S greedy)
   and polished by random order-moves on the exact count (accept if not worse).
3. Lower bound: code/lb_forest.py (exhaustive F_1..F_5), cross-check code/crosscheck_F5_sat.py.

## Runs (fvs_sa arguments: d seed SA-iters mu out polish-iters [init]; init 0 = start S = even
## vertices (default), 2 = random start). "states" = SA iterations; "polish" = order-moves.
| run | d | seed | mu | init | states | polish | runtime | |S| | score (checker) |
|---|---|---|---|---|---|---|---|---|---|
| R0-2 | 2 | 1 | 0.3 | 0 | 3e5 | 5e4 | 0.02 s | 1 | VERIFIED 5 |
| R0-3 | 3 | 1 | 0.3 | 0 | 3e5 | 5e4 | 0.04 s | 3 | VERIFIED 14 |
| R0-4 | 4 | 1 | 0.3 | 0 | 3e5 | 5e4 | 0.07 s | 6 | VERIFIED 34 |
| R0-5 | 5 | 1 | 0.3 | 0 | 3e5 | 5e4 | 0.17 s | 14 | VERIFIED 88 |
| R0-6 | 6 | 1 | 0.3 | 0 | 3e5 | 5e4 | 0.26 s | 28 | VERIFIED 204 |
| R0b | 5, 6 | 2,3,4 | 0 and 0.3 | 0 | 3e6 | 1e5 | not timed individually (whole batch < 120 s) | 14 / 28 | internal 88 / 204 (not re-checked; by-product only) |
| R4-d7a | 7 | 11 | 0.3 | 0 | 1e7 | 2e5 | 18.0 s | 56 | VERIFIED 464 |
| R4-d7b | 7 | 12 | 0.3 | 0 | 1e7 | 2e5 | 18.4 s | 56 | VERIFIED 464 |
| R4-d7c | 7 | 13 | 0.3 | 0 | 1e7 | 2e5 | 19.3 s | 56 | VERIFIED 464 |
| R4-d7d (-> Q7.txt) | 7 | 11 | 0 | 0 | 1e7 | 2e5 | 19.3 s | 56 | VERIFIED 464 |
| R4-d7e | 7 | 12 | 0 | 0 | 1e7 | 2e5 | 21.1 s | 56 | VERIFIED 464 |
| R4-d7f | 7 | 13 | 0 | 0 | 1e7 | 2e5 | 23.7 s | 56 | VERIFIED 464 |
| R4-d7g | 7 | 11 | 0.3 | 2 | 1e7 | 2e5 | 25.9 s | 56 | VERIFIED 464 |
| R4-d7h (-> Q7_alt1.txt) | 7 | 31 | 0.3 | 2 | 1e7 | 2e5 | 27.8 s | 56 | VERIFIED 464 |
| R4-d8a (-> Q8.txt) | 8 | 21 | 0.3 | 0 | 2e7 | 2e5 | 118.7 s | 112 | VERIFIED 1040 |
| R4-d8b | 8 | 21 | 0 | 0 | 2e7 | 2e5 | 133.9 s | 112 | VERIFIED 1040 |
| R4-d8c (-> Q8_alt1.txt) | 8 | 22 | 0.3 | 0 | 2e7 | 2e5 | 106.2 s | 112 | VERIFIED 1040 |
| repro-Q7 | 7 | 11 | 0 | 0 | 1e7 | 2e5 | 20.9 s | 56 | byte-identical to Q7.txt |
| repro-Q7alt | 7 | 31 | 0.3 | 2 | 1e7 | 2e5 | 19.9 s | 56 | byte-identical to Q7_alt1.txt |
| repro-Q8 | 8 | 21 | 0.3 | 0 | 2e7 | 2e5 | 86.4 s | 112 | byte-identical to Q8.txt |

Note: runs R4-d7g/h were made with an intermediate build in which init 0/1 polarity was swapped;
init 2 (random) code path was identical, and the final build reproduces them (repro-Q7alt).

Structure of the artefacts (code/lemmaA_sanity.py and an inline check): in all four hand-in files S
is an independent set (Q7: |S| = 56, Q8: |S| = 112) and count = 2^d + (d-1)|S| exactly.
Q7.txt: S inside even-weight vertices, weight profile {0:1, 2:18, 4:31, 6:6}; Q7_alt1.txt: S inside
odd-weight vertices {1:6, 3:31, 5:18, 7:1}, disjoint from Q7.txt's S. Q8.txt: {0:1, 2:24, 4:62, 6:24, 8:1};
Q8_alt1.txt: {2:28, 4:56, 6:28} (different profiles; 96 common S-vertices).

## Lower-bound runs
| run | what | class | status | runtime | counts |
|---|---|---|---|---|---|
| LB1 | python3 code/lb_forest.py | all subsets of V(Q_1..Q_4); all pairs of Q_4-forests with sizes summing to 20, 19 (and 18 until first hit) | COMPLETED, exhaustive | 0.73 s (first version), 0.51 s (final version with F_1..F_3 added) | 65536 subsets, 25015 forests of Q_4, 16928 pairs, 1100 passed edge filter; F_4 = 10, F_5 = 18 |
| LB2 | venv python3 code/crosscheck_F5_sat.py | Q_5, m = 19 and 18, CEGAR/CaDiCaL | COMPLETED | 0.71 s | m=19 UNSAT after 707 iterations / 786 cycle clauses; m=18 SAT |
| LS | python3 code/lemmaA_sanity.py Q7 Q8 (sanity, not proof) | 1580 seeded labellings d = 1..7 | COMPLETED | 0.32 s | 0 violations |

## Best score per d
d = 7: 464 (all 8 runs), matches lower bound 464. d = 8: 1040 (all 3 runs), matches lower bound 1040.
Stopping condition: for d = 7, 8 the score did not change over >= 3 independent runs, and it equals
the proven lower bound, so no further search can improve it.
