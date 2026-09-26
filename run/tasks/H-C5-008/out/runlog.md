# Runlog: H-C5-008 (searcher, CONTRARIAN, UPPER route)

Reading of the brief (stated per the core rules): UPPER route only; a labelling with <= 2399 paths
needs (gated Lemma A) an induced forest of Q_9 with >= 277 vertices. Contrarian angle chosen:
**forests invariant under a free group action, searched in the covering quotient Q_9/G**
(translation groups = binary linear codes, and free affine involutions sigma(v)+a). None of the
forbidden approaches is a covering-quotient search: they searched Q_9 itself, forests invariant
under coordinate-cycle groups, parity/code sets S, cluster products. The inner optimiser on each
quotient is SA or SAT-CEGAR on the (much smaller) quotient graph; I read this as allowed because the
object searched (a forest in Q_9/G, 64-256 vertices, with a written lifting lemma) and the symmetry
classes (translations, twisted involutions) are new. This reading is listed under KNOWN GAPS.

Machine: 4 shared cores; one heavy process at a time. Python = /home/user/bainsahackathon/.venv/bin/python3
for the pysat parts; stdlib python3 for checker/decoder. Runtimes are wall-clock from `time` (bash
builtin; /usr/bin/time is not installed) or the per-run seconds printed by the scripts.

| run | what | parameters | result | status | runtime |
|---|---|---|---|---|---|
| R1 | checker sanity: verify.py on q1.txt (0,1) and q2.txt (00,01,10,11) | hand values 2 and 5 | `VERIFIED 2`, `VERIFIED 5` | COMPLETED | <1 s |
| R2 | quotients.py: code classes r = 1,2,3 | all column multisets | 8 / 35 / 99 classes | COMPLETED | 2.05 s |
| R3 | qsat.py r=3 m=35, all 99 classes, 60 s cap each | CaDiCaL 1.5.3 CEGAR, 4-cycle clauses up front | 99 UNSAT (solver answers, no DRAT) | COMPLETED | 15.8 s |
| R4 | qsat.py r=3 m=34, 33, 32 all classes | same | m=34: 9 SAT, 90 UNSAT; m=33: 12 SAT; m=32: 81 SAT; every SAT forest lifted and re-checked in Q_9 (272-vertex forests) | COMPLETED | 14.5 + 24.0 + 4.8 s |
| R5 | qsat.py r=2 m=70, all 35 classes, 12 s cap | same | 24 UNSAT, 11 TIMEOUT (classes 10,21,22,23,24,29,30,31,32,33,34), 0 SAT | PARTIAL (timeouts) | 156.6 s |
| R6 | runqls.py r=2 SA (qls.c), 1e7 iters seed 1 all 35 classes; then 6e7 iters seed 2 on the 11 timed-out classes | T 0.6 -> 0.05 geometric | best 68 (=272 lifted) in 9 classes, never 70 | COMPLETED (heuristic) | 39.7 s + 113.8 s |
| R7 | runqls.py r=1 SA 5e7 iters seed 1, all 8 classes | same | best 137 (274, class weight 4); 136 (weights 5,6,8,9); 132 (7); 128 (2,3) | COMPLETED (heuristic) | 63.1 s |
| R8 | runqls.py r=1 SA 3e8 iters seed 2, classes 2,3,4,6,7 | same | 137, 136, 136, 136, 136 | COMPLETED (heuristic) | 232.8 s |
| R8b | SA calibration on Q_8 itself (qls2, 1e8 iters, seeds 1, 2) | same | 144 both seeds (= F_8, the known optimum by Lemma A/C + U(Q_8) = 1040) | COMPLETED | 14.0 s, 13.6 s |
| R9 | decode.py + verify.py on lifted forests | T in BFS order per tree, then S by #S-neighbours | 274-forest (r=1, weight 4, e(S)=58): `VERIFIED 2764`; 276-forests (involutions t=1,f=4 and t=2,f=4, S independent): `VERIFIED 2400` each | COMPLETED | <1 s each |
| R10 | affquot.py involutions, SA 1e8 iters seed 1, all 12 classes (t,f) | qls2.c | 138 (=276) for (1,4) and (2,4); 137 for (1,6),(2,2),(3,2); 136 for (1,2),(2,3),(2,5); 134 for (1,5),(1,7),(3,3); 132 for (1,3) | COMPLETED (heuristic) | 12 runs, 9.3-17.3 s each |
| R11 | affquot.py one 1 4, 4e8 iters, seeds 11..16 | qls2.c | see below | see below | see below |
