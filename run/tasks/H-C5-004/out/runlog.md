# Runlog: H-C5-004 (EXPLOIT of H-C5-002, UPPER route), 13:35-14:30

Reading of the brief: the target is a Q_9 labelling that the checker scores at most 2399. The subject's
identity P = 512 + 8|S_f| + sum_{S_f}(N-2)up (not refereed) is used only as a search guide: a labelling scoring
<= 2399 needs an induced forest F with |F| >= 277 (|S| <= 235). So every search below looks for a large induced
forest. Scores are always inbox/checker/verify.py output. Runtimes are bash `time` real seconds
(/usr/bin/time is not installed) or the program's own wall clock, as marked.
Python = /home/user/bainsahackathon/.venv/bin/python3, SAT solver cadical153 (python-sat).

Headline: no induced forest with |F| >= 277 was found. Smallest decycling set found: 236 (in every run that
reached it). Best checker score: VERIFIED 2400 (out/Q9.txt, rebuilt from the subject's parity forest; it
matches the known bound and earns nothing).

| # | run | params / seed | result | status | runtime |
|---|---|---|---|---|---|
| 1 | checker on inbox/subject/Q9.txt | - | VERIFIED 2400 | COMPLETED | 0.02 s |
| 2 | sym_forest_sat.py sanity, trivial group | d=5 K=18 / K=19; d=6 K=36 / K=37 | SAT 18 / UNSAT 19; SAT 36 / UNSAT 37 (matches known 14, 28) | COMPLETED | 0.0, 0.1, 0.9, 1.3 s (internal) |
| 3 | sym_forest_sat.py, g = 9-cycle of coords, t=0 (60 orbits) | K=276, K=277 | UNSAT (13 it, 340 cuts); UNSAT (7 it, 163 cuts) | COMPLETED | 24.6 s, 15.3 s |
| 4 | run_classes.sh 277 90 4: 7-cycle (80 orbits), 5-cycle (128), three 3-cycles (176), two 3-cycles (192) | K=277 | 7cyc UNSAT (9 it, 137 cuts); 5cyc UNSAT (0 cuts); 3cyc3 TIMED OUT; 3cyc2 TIMED OUT | 2 COMPLETED, 2 TIMED OUT | 2.1, 1.7, 90, 90 s |
| 5 | sym_forest_sat.py, three 3-cycles (176 orbits) | K=277, timeout 300 s | ~45 iterations, 2271+ cuts, undecided | TIMED OUT | 300 s |
| 6 | lns_forest.py from subject forest | seed 1, 30 steps, subcube dim 7 | 276, 30 regions UNSAT, 0 plateau moves | COMPLETED | 7.2 s |
| 7 | lns_forest.py from subject forest | seed 2, 6 steps, subcube dim 8, budget 2e5 conflicts | 276, all 6 steps budget-exhausted | COMPLETED | 70.3 s |
| 8 | lns_forest.py from subject forest | seed 3, 10 steps, balls of 200, budget 1e5 | 276, all budget-exhausted | COMPLETED | 49.3 s |
| 9 | mif_sa (subject SA, unchanged) | seed 101, 2e7 moves, T 2.0->0.05 | |S| = 236 (e(S)=13, 2 minority vertices, 83 comps) | COMPLETED | 11.3 s |
| 10 | build_labelling.py on run 9's forest + checker | seed 0 | extra 6; VERIFIED 2406 | COMPLETED | < 1 s |
| 11 | mif_sa, seeds 201..208 | 5e7 moves each, T 2.0->0.05 | |S| = 236 in all 8 (all of type e(S)=13, 234+2 parity split, 83 comps) | COMPLETED | 31.3, 30.3, 31.9, 36.5, 36.3, 31.2, 36.8, 44.7 s |
| 12 | lns_forest.py from run-11 forest (seed 201 file) | seed 11, 400 steps, mixed regions (subcube 7 / balls 130-170), plateau 0.7, budget 3e4 | 276; 204 UNSAT, 196 budget, 44 plateau moves, 0 improvements | COMPLETED | 254.4 s |
| 13 | build_labelling.py on subject forest (2 seeds) + checker | seeds 1, 2 | VERIFIED 2400, VERIFIED 2400 (files differ from the subject's Q9.txt) | COMPLETED | < 1 s |
| 14 | mif_sa_bal, both parity classes >= L | 3e7 moves, L = 60, 100, 130 (seeds 360, 3100, 3130) | L=60: |S| = 240 (F 135 even / 137 odd); L=100, 130: no feasible best recorded | COMPLETED | 16.8, 1.8, 1.8 s |
| 15 | mif_sa_bal L=60 | seeds 401, 402, 403, 1e8 moves | |S| = 240, 248, 240 | COMPLETED | 54.2, 59.7, 55.2 s |
| 16 | lns_forest.py from run-15 forest (seed 401 file; e(S)=112, 16 comps) | seed 21, 300 steps, subcube 7, plateau 0.7 | 272; 299 UNSAT, 151 plateau moves, 0 improvements | COMPLETED | 193.2 s |
| 17 | lns_forest.py from run-11 forest (seed 205 file) | seed 31, balls of 140, plateau 0.8, budget 6e4 | 276 at step 150 (35 UNSAT, 116 budget, 11 plateau), 0 improvements | TIMED OUT (300 s cap) | 300 s |
| 18 | zsat.py: F = (O\Z) u M, 3 <= |Z| <= 8, |F| >= 277 | - | first solve calls did not finish, undecided | TIMED OUT (240 s cap) | 240 s |
| 18b | lns_forest.py from run-11 forest (seed 203 file) | seed 41, subcube dim 7, plateau 0.9, budget 3e4 | 276 at step 1300: 1301 regions UNSAT, 463 plateau moves, 0 improvements | TIMED OUT (270 s cap) | 270 s |
| 19 | checker on out/Q9.txt (= out/best.txt), tmp/lab_subject_seed2.txt, tmp/lab_s101.txt | - | VERIFIED 2400, VERIFIED 2400, VERIFIED 2406 | COMPLETED | 0.05 s each |

Node/state counts (role lesson v1): SAT runs report iterations and lazy cuts above; SA runs report moves
(2e7..1e8 proposals); LNS runs report the number of region solves (steps) and their outcomes.

Not exhaustive anywhere except the three symmetric classes of runs 3-4 (see claims.md for their exact class,
and the caveat that the UNSAT answers carry no DRAT certificate).

## Checklist G pass (against claims.md)
- G1: no claim of the cell is made; the only artefact claim is "2400 labelling", which matches the known
  bound and is labelled as earning nothing. Search claims name their exact class.
- G2: the symmetry-class argument (claims.md A1) and the Q_8 x K_2 argument (A2) are written step by step.
- G3: sanity cases d = 5, 6 reproduce 14 and 28 (runlog 2); the symmetric classes list their orbit counts.
- G4: no invariant/decrease argument is used for the claims.
- G5: no construction claimed beyond the one file checked.
- G6: the subject's identity is used only to steer the search (P <= 2399 needs |F| >= 277); no score rests on it.
- G7: every score is the checker's; SAT UNSATs have no DRAT certificate and are therefore reported as
  SEARCH-FOUND-NOTHING, not verification; all timed-out runs are marked TIMED OUT.
- G8: no literature used beyond the subject's files.
- G9: established: 2400 file (checker). Not established: anything below 2400, any lower bound.
