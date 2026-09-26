# Claims H-C2-001

Library dependency: inbox/library/H-uphill-checker (verify.py, copied unmodified to out/code/verify.py)
is used only to SCORE artefacts (upper half). The library "lemma" it embodies is: verify.py prints
the exact number of uphill paths of the given labelling (per its docstring: N(v) recursion, Lemma 1 of
proof.md). The lower-bound DP does not call it.

| claim | status | where shown |
|---|---|---|
| C1 checker reproduces hand count on Q_2 lex order (T=5) | CHECKED | runlog.md "Checker sanity" |
| C2 out/Q5.txt (= out/best.txt) is a labelling of Q_5 with exactly 88 uphill paths | CHECKED (provided checker: VERIFIED 88) | runlog.md A5-1; library H-uphill-checker |
| C3 out/Q5_alt1.txt is a structurally different labelling with 88 uphill paths (5 vs 8 valleys) | CHECKED (VERIFIED 88) | runlog.md A5-2 |
| C4 T = E + sum_v ([valley] + (N(v)-1) up(v)), each term >= 0 | PROVED | proof.md Lemmas 1-3 |
| C5 non-valley with N>=2, up>=1 in Q_5 has cost >= 3; matching bound h admissible | PROVED | proof.md Lemma 4, "Heuristic h" |
| C6 translation / full automorphism reductions sound | PROVED | proof.md "Symmetry" |
| C7 layered DP decides "min X <= LIMIT" exactly (empty layer => no labelling with X <= LIMIT) | PROVED | proof.md "Correctness of the layered DP" |
| C8 DP sanity: U(Q_3) = 14 matches independent brute force over all 8! labellings; U(Q_4) DP = 34 matches annealing | CHECKED | runlog.md L3*, B3, L4* |
| C9 no labelling of Q_5 has T <= 87 (exhaustive over all 32! labellings via the reduction). Rests on C4+C7 plus EITHER (C5 + translations) [run L5-H'] OR (full orbit merging, C6) [run L5-S0] | CHECKED (computer-assisted) | runlog.md L5-H' (2m40s, 18,696,829 states), L5-S0 (1m16s, 1,567,313 states), L5-S (1.3 s, 19,510) |
| C9b DP at LIMIT 8 itself finds minimal X = 8 (consistent with C2) | CHECKED | runlog.md L5-8 |
| C10 U(Q_5) = 88 | PROVED (C2 + C9) | proof.md Conclusion |

Scope: only d = 5 (and d = 3, 4 as sanity) is covered; nothing is claimed for other d.

## Checklist G pass
- G1 claim is exactly "U(Q_5) = 88": labelling with 88 (checker) + every labelling >= 88 (C9). Definitions
  as in the statement (valley: all neighbours larger; lone valley counts; sequences counted).
- G2 proof.md writes out every step (recursion, identity, state lemma, heuristic, symmetry, DP invariant).
- G3 base case: layer 1 / label-1 vertex is a valley (proof.md); N-value encoding bound (c) covers the
  4-bit edge case; empty-layer termination covers early exit.
- G4 invariant of the DP stated and proved step by step (proof.md "Correctness").
- G5 construction claimed only for d = 5; checked by the provided checker.
- G6 no circularity; no citations.
- G7 exact integer arithmetic throughout; runs < 3 min; finite check covers exactly d = 5 (all 32!
  labellings through the written reduction); d = 3,4 only as sanity.
- G8 no cited results; library entry H-uphill-checker used only for scoring (stated above).
- G9 established: U(Q_5) = 88 (computer-assisted lower bound). Not established: anything for d != 5.
