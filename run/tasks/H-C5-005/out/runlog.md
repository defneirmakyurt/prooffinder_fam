# Run log: H-C5-005 (EXPLOIT of H-C5-002, UPPER route)

Machine: 4 cores shared; one heavy process at a time; every run under `timeout`. Times are wall-clock,
measured with bash `time` or `date +%s.%N` differences (`/usr/bin/time` is not installed).
PY = /home/user/bainsahackathon/.venv/bin/python3 (pysat) for the SAT tools; checker/builder are stdlib python3.

## Reading of the task (stated per the core rules)
Only the UPPER route (brief ROUTE line). Score = output of inbox/checker/verify.py on the handed-in file.
The subject's identity P = 512 + 8|S_f| + extra (proof.md, not refereed) is used ONLY as a search guide:
P <= 2399 needs a decycling set of size <= 235. All searches below therefore look for small decycling sets
(equivalently large induced forests) of Q_9 in various classes, and every candidate is turned into a
labelling by code/build_labelling.py and scored by the checker.

## Runs (chronological)
| # | what | parameters / seeds | status | wall time | result (smallest decycling set / checker) |
|---|---|---|---|---|---|
| 1 | checker on inbox/subject/Q9.txt | - | COMPLETED | 0.02 s | VERIFIED 2400 |
| 2 | sat_cegar.py (SAT + lazy cycle clauses, no symmetry) | d=3,4,5,6,7 with K=3,6,14,28,56 | COMPLETED | 0.06, 0.05, 0.06, 0.51, 75.2 s | FOUND |S| = K each (1,1,1,365,488 CEGAR iterations) |
| 3 | sat_group.py (orbit version) | d=6 K=28 trivial group; d=7 K=56 group C7 (cyclic shift) | COMPLETED | 0.83 s; 0.11 s | FOUND 28; FOUND 56 |
| 4 | sat_group.py on Q_9, class: sets invariant under cyclic coordinate shift C9 (60 orbits) | K=236 | TIMED OUT (6 CEGAR iterations) | 99.6 s | nothing found |
| 5 | same class | K=235 | PARTIAL (killed by me after < 2 min to free the core; no output) | < 120 s | nothing found |
| 6 | msa (SA over even part M, greedy Z; code/msa.c) | d=6,7,8; seed 1; 2e6 iters; T 3 -> 0.2 | COMPLETED | 0.47, 0.84, 1.89 s | |S| = 28, 56, 112 |
| 7 | msa on Q_9 | seeds 1, 2; 2e7 iters; T 4 -> 0.3; XW=1 | COMPLETED | 22.2 s, 22.5 s | P_est 2400, |M|=20, |Z|=0, |S|=236 (both) |
| 8 | msa on Q_9 | seed 3: 4e7 iters, T 8 -> 6, XW=0 | COMPLETED | 40.5 s | |S| = 241 |
| 9 | msa on Q_9 | seed 4: 4e7 iters, T 10 -> 1, XW=0 | COMPLETED | 37.5 s | |S| = 236 (|M|=20, Z empty) |
| 10 | msa on Q_9 | seed 5: 4e7 iters, T 6 -> 0.5, XW=1 | COMPLETED | 30.1 s | |S| = 236 (|M|=20, Z empty) |
| 11 | orbitsa (forest SA over group orbits; code/orbitsa.c) sanity | d=7 C7 3e5 iters; d=8 trivial 1e6 iters; T 2 -> 0.1 | COMPLETED | 1.18 s; 6.39 s | |S| = 56; 112 |
| 12 | orbitsa on Q_9, batch tmp/batch1.sh, 3e6 iters each, T 2 -> 0.15 (see table below) | seeds 11..20 | COMPLETED (all 10) | 25-63 s each, 8.5 min total | best 236 (trivial group only) |
| 13 | sat_lns.py from tmp/ob_triv.txt (|S|=236), regions = random 6-dim subcubes (64 vertices), ask |S cap R| <= current-1 | 40 rounds, seed 1, sub-time 10 s | COMPLETED | 0.8 s total | solver said UNSAT in all 40 regions (no DRAT; not a claim) |
| 14 | same, 7-dim subcubes (128 vertices) | 30 rounds, seed 2, sub-time 20 s | COMPLETED | 9.3 s total | UNSAT in all 30 regions (no DRAT; not a claim) |
| 15 | same, 8-dim subcubes (256 vertices) | 10 rounds requested, seed 3 | TIMED OUT inside round 0 (single SAT call did not return) | 280 s (outer timeout) | nothing found |
| 16 | build_labelling.py + checker on forests from runs 7 (seed 1), 9 (seed 4), 12 (trivial group) | - | COMPLETED | 0.02, 0.03, 0.77 s | VERIFIED 2400, VERIFIED 2400, VERIFIED 2406 |
| 17a | orbitsa unrestricted (tmp/batch2.sh) | seed 31, 6e6 iters, T 1.5 -> 0.2 | COMPLETED | 80.0 s | |S| = 236 |
| 17b | msa (tmp/batch2.sh) | seed 32, 8e7 iters, T 6 -> 0.5, XW=0 | COMPLETED | 61.1 s | |S| = 236 (|M|=20, Z empty), P_est 2400 |
| 17c | orbitsa unrestricted (tmp/batch2.sh) | seed 33, 5e6 iters, T 3 -> 0.3 | PARTIAL (killed by me after < 30 s to free the core; no result) | < 30 s | none |
| 18 | sat_cegar.py --oddmax 0 (near-parity class: S has no odd vertex) | d=9, K=236 | COMPLETED | 0.82 s | FOUND |S| = 236 (sanity: a 20-word code) |
| 19 | sat_cegar.py --oddmax 1 (class: |S cap O| <= 1, |S cap E| <= 234) | d=9, K=235 | TIMED OUT (first SAT call never returned) | 130 s (outer timeout) | nothing found |
| 20 | sat_cegar.py --oddmax 2 (class: |S cap O| <= 2, |S cap E| <= 233) | d=9, K=235 | TIMED OUT (first SAT call never returned) | 130 s (outer timeout) | nothing found |
| 21 | cluster_value.py (exact, stdlib) | smax = 4, then smax = 5 | COMPLETED | 0.36 s; 70.1 s | max value 1 at sizes 2..5 (1, 56, 2590, 111300 sets) -> lemma L2 |
| 22 | reproduction of the hand-in: msa seed 1 recompiled from code/msa.c, then build_labelling.py, then checker | as run 7 | COMPLETED | 14.4 s | forest and labelling byte-identical to out/forest_Q9.txt, out/Q9.txt; VERIFIED 2400 |

### Run 12 detail (orbitsa on Q_9; class = induced forests that are unions of orbits of the group generated)
Generator notation "p0,...,p8:t" = map x -> pi(x) XOR t, bit j of x goes to bit p_j. Output copied from tmp/batch1.log.
| name | generators | orbits | best |S| | time |
|---|---|---|---|---|
| triv | none (unrestricted) | 512 | 236 | 49.0 s |
| t511 | translation by 111111111 (swaps parity) | 256 | 240 | 54.3 s |
| c9 | cyclic shift of the 9 coordinates | 60 | 237 | 63.3 s |
| c3b | (012)(345)(678) | 176 | 237 | 63.4 s |
| t3 | translation by 000000011 | 256 | 256 | 49.8 s |
| t7 | translation by 000000111 | 256 | 256 | 56.3 s |
| t15 | translation by 000001111 | 256 | 238 | 55.3 s |
| tr01 | transposition of coords 0,1 | 384 | 240 | 48.7 s |
| tr01x | transposition (0 1) then XOR 000000100 | 256 | 256 | 25.4 s |
| c9x | cyclic shift then XOR 111111111 | 30 | 288 | 44.9 s |

The forest found by "triv" (tmp/ob_triv.txt) has |S| = 236 with 234 even + 2 odd vertices, e(S) = 13,
83 components (code/check_forest.py): the same non-parity shape the lineage reported. Its labelling scores 2406
(extra 6), worse than parity.

## Best checker score per run family
* parity-code labellings (runs 7, 9): 2400 (checker) -- matches the organisers' bound, earns nothing.
* non-parity 236 forest (run 12 triv): 2406 (checker).
* No run produced a decycling set of size <= 235 in any class searched: SEARCH-FOUND-NOTHING.

## Artefacts
* out/Q9.txt = out/best.txt: labelling from run 7 seed 1 (20-word even code M, F = O u M), checker VERIFIED 2400.
* out/Q9_alt.txt: labelling from run 9 seed 4 (a different 20-word code), checker VERIFIED 2400; differs from
  out/Q9.txt and from inbox/subject/Q9.txt (cmp).
* out/forest_Q9.txt, out/forest_Q9_alt.txt: the forests (indicator lines) they were built from.

## Exhaustiveness
No search here is exhaustive over any class of Q_9 objects. Runs 4, 5, 15, 19, 20 timed out; the SA runs are
heuristic; the LNS UNSAT answers (runs 13, 14) concern only the random regions tried, with the rest of the
solution fixed, and come without a DRAT proof. Outcome for the UPPER route: SEARCH-FOUND-NOTHING.
