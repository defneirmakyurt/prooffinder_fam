# Run log: H-C5-003 (searcher, EXPLOIT of H-C5-002, UPPER route)

Machine: 4 shared cores; one heavy process at a time. Times are bash `time` (real) of the exact command
(`/usr/bin/time` is not installed). Paths relative to run/tasks/H-C5-003/out/.

Reading of the brief: the hand-in must be out/Q9.txt with at most 2399. Matching 2400 earns nothing.
My best labellings score 2400. They are saved as out/Q9.txt, out/best.txt (identical) and out/Q9_alt.txt,
as the brief's "save the best labelling" asks, and are NOT a solution.

## R1: checker sanity
| run | result | time |
|---|---|---|
| `python3 ../inbox/checker/verify.py ../inbox/subject/Q9.txt` | VERIFIED 2400 | 0.025 s |

## Multiway-cut repair annealer (code/mcut_sa.c), COMPLETED runs
Move: add random v not in F. For each tree of F holding >= 2 of v's F-neighbours, delete a minimum vertex
multiway cut separating them. delta = 1 - |cut|. With probability pnb the predecessor's move is used
instead (keep one random neighbour per tree). Metropolis acceptance, geometric T0 -> T1.
Seeds = xorshift seeds. Restarts: every run is one independent start from the empty forest, except s13.
"accepted" = number of accepted moves (the state count of the run).

| run | d | seed | iters | T0 -> T1 | pnb | init | accepted | best \|S\| | real time |
|---|---|---|---|---|---|---|---|---|---|
| R2-5 | 5 | 1 | 3e6 | 0.6->0.1 | 0 | empty | 651272 | 14 | 0.56 s |
| R2-6 | 6 | 1 | 3e6 | 0.6->0.1 | 0 | empty | 380837 | 28 | 0.73 s |
| R2-7 | 7 | 1 | 3e6 | 0.6->0.1 | 0 | empty | 209956 | 56 | 0.68 s |
| R2-8 | 8 | 1 | 3e6 | 0.6->0.1 | 0 | empty | 121175 | 112 | 0.60 s |
| s1 | 9 | 1 | 2e7 | 0.6->0.1 | 0 | empty | 1377038 | 236 | 10.8 s |
| s2 | 9 | 2 | 2e7 | 0.6->0.1 | 0 | empty | 1427316 | 236 | 11.8 s |
| s11 | 9 | 11 | 2e8 | 0.5->0.15 | 0 | empty | 13404228 | 236 | 87.5 s |
| s12 | 9 | 12 | 4e8 | 0.7->0.2 | 0.3 | empty | 40465163 | 236 | 286.5 s |
| s13 | 9 | 13 | 3e8 | 0.3 const | 0 | tmp/F9_s11.txt (276) | 17095859 | 236 | 127.4 s |
| s14 | 9 | 14 | 1.5e8 | 0.45->0.12 | 0.1 | empty | 7005592 | 236 | 72.5 s |
| s15 | 9 | 15 | 1.5e8 | 0.45->0.12 | 0.1 | empty | 7055364 | 236 | 66.5 s |

Forest statistics (predecessor's stdlib checker `../inbox/subject/code/check_forest.py`):
- tmp/F9_s1.txt: forest=True |S|=236 e(S)=7 S_even=1 S_odd=235 components=89
- tmp/F9_s2.txt: forest=True |S|=236 e(S)=13 S_even=234 S_odd=2 components=83
- tmp/F9_s11.txt: forest=True |S|=236 e(S)=7 S_even=1 S_odd=235 components=89
- tmp/F9_s12.txt: forest=True |S|=236 e(S)=13 S_even=2 S_odd=234 components=83
- tmp/F9_s14.txt: forest=True |S|=236 e(S)=13 S_even=234 S_odd=2 components=83
- tmp/F9_s15.txt: forest=True |S|=236 e(S)=13 S_even=2 S_odd=234 components=83

Smallest decycling set reached in any d = 9 run: 236. Never <= 235: SEARCH-FOUND-NOTHING (heuristic, not
exhaustive).

## Symmetric penalty annealer (code/sym_pen_sa.c), COMPLETED runs
Energy -|F| + lambda * (cycle rank of G[F]), exact union-find recomputation per proposal. Move: flip one
sigma-orbit. F is forced to be invariant under the coordinate permutation sigma (a restricted class).
| run | d | seed | sigma (i -> p_i) | orbits | iters | T0 -> T1 | lambda | best \|S\| | real time |
|---|---|---|---|---|---|---|---|---|---|
| p8 | 8 | 1 | identity | 256 | 5e6 | 1.0->0.1 | 1.5 | 112 | 12.8 s |
| c3 | 9 | 21 | 1 2 0 4 5 3 7 8 6 (three 3-cycles) | 176 | 2e7 | 1.0->0.1 | 1.5 | 237 | 131.1 s |
| c2 | 9 | 22 | 1 0 3 2 5 4 7 6 8 (four transpositions) | 272 | 2e7 | 1.0->0.1 | 1.5 | 236 | 91.3 s |
check_forest.py: tmp/P9_c3.txt forest=True |S|=237 e(S)=21; tmp/P9_c2.txt forest=True |S|=236 e(S)=7.

## Labellings from forests (code/forest_to_labelling.py), then scored by the provided checker
| forest | labelling | builder's own count | checker output |
|---|---|---|---|
| tmp/F9_s1.txt | tmp/L9_s1.txt = out/Q9.txt = out/best.txt | 2400 | VERIFIED 2400 |
| tmp/F9_s11.txt | tmp/L9_s11.txt = out/Q9_alt.txt | 2400 | VERIFIED 2400 |
| tmp/F9_s2.txt | tmp/L9_s2.txt | 2406 | VERIFIED 2406 |
sha256: Q9.txt 335c9b99..., Q9_alt.txt 7cab0612..., subject Q9.txt 79ad1691... (all three differ).
Q9.txt / Q9_alt.txt use a forest whose deleted set is 235 odd + 1 even word (e(S) = 7), not the
predecessor's 236 even words.

## Lazy SAT (code/sat_forest.py, cadical153, seqcounter cardinality), calibration
| run | result | time |
|---|---|---|
| d=5 K=18 | FOUND (1 iteration) | 0.16 s |
| d=6 K=36 | FOUND (749 iterations, 6189 cycle clauses) | 1.5 s |
| d=7 K=72 | TIMED OUT (timeout 120 s), no result | 120.0 s |
| d=5 K=19 | solver UNSAT after 147 iterations (no DRAT proof, not claimed) | 0.17 s |
Conclusion: too weak for d = 9 (K = 277). Not run at d = 9.

## Cluster sub-search (R6)
| run | result | time |
|---|---|---|
| `python3 code/clusters.py 6` | clusters (G2-connected sets of even words) up to symmetry: sizes 1..6: 1, 1, 2, 8, 31, 268 classes; max net = 1 at every size; no cluster with net >= 2 | 32.2 s |
| delta sanity (inline python calling clusters.delta) | Q_4-even cluster: delta = 6 of 8 witnesses (net 2); Q_3-even: delta = 3 (net 1); pair: delta = 1 (net 1) | < 1 s |
| `PYTHON code/region_code.py 3 K`, K = 12, 14, 16 | SAT (code of that size exists in {wt(last 5 coords) >= 3}) | <= 0.1 s each |
| same, K = 17, 18, 19 | solver UNSAT (no certificate; not claimed as proof) | 4.7 s, 1.7 s, 0.8 s |
| `python3 code/clusters_q5.py 4 5` | all G2-connected sets of 4 / 5 even words of one Q_5 subcube containing 0: 405 / 1340 sets, none with net >= 2 | 0.15 s |
| `python3 code/clusters_q5.py 6 7 8` | 2997 / 5005 / 6435 sets; net >= 2 only for 5 sets of size 8, all the even words of a Q_4 subcube (delta 6, 8 witnesses of degree 4) | 1.0 s |
| `python3 code/clusters_q5.py 9 ... 16` | net >= 2 for 45 (size 9), 25 (size 10), 0 (sizes 11, 12, 13), 105, 15, 1 (sizes 14, 15, 16) sets; types of the size-9/10 ones not analysed | 296.5 s |

## Checklist G pass (against claims.md)
- G1: no claim of the cell's statement. The target U(Q_9) <= 2399 is SEARCH-FOUND-NOTHING. The hand-in
  files score 2400, which matches the organisers' bound and earns nothing.
- G2: the cluster reduction (C4) and the symmetry-reduction soundness (C5) are written out step by step.
- G3: n/a (single parameter value d = 9; the d = 5..8 runs are calibration only).
- G4: the annealers keep F a forest. mcut_sa re-checks the final best F with edges = vertices - components;
  sym_pen_sa recomputes the cycle rank. Every forest was re-checked by check_forest.py.
- G5: artefacts claimed only for d = 9, each checked by the provided checker.
- G6: no circularity.
- G7: all counts are exact integers. Checker and cluster enumerations are stdlib. SAT UNSAT verdicts
  (region code 17..19, d = 5 K = 19) have no DRAT certificates and are NOT claimed as proofs.
- G8: the only cited result is A(9,4) = 20 (classical code tables), used in C4 step 5 only.
- G9: claims.md lists what is and is not established.
