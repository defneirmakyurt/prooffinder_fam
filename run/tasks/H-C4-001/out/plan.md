# Plan: H-C4-001 (U(Q_7), U(Q_8)), searcher, BLIND, phase 1

Target: integers U(Q_7), U(Q_8); for each: (a) labelling attaining V, (b) proof every labelling has >= V.

## Ladder
- R1 checker sanity: inbox checker (sha256 = library H-uphill-checker) reproduces hand-computed small cases (Q_2 cycle labelling). deps: none.
- R2 Lemma A (forest bound, written proof in claims.md): for every labelling of Q_d,
  #uphill >= 2^d + (d-1)|S|, where S = {v : v has >= 2 lower neighbours}, and T = V\S induces a forest.
  Hence U(Q_d) >= 2^d + (d-1) * nabla_d, nabla_d = min size of a vertex set whose complement induces a forest. deps: none.
- R3 Lemma B (construction): if T induces a forest and S = V\T, labelling "T in rooted-tree order, then S" has
  count 2^d + (d-1)|S| + sum over S-edges w->v (lower w) of (N(w)-2). deps: none.
- R4 search (upper half): SA over vertex subsets S of Q_7 / Q_8, min (d-1)|S| + penalty(cycles in T); decode by R3; polish; score with checker. deps R1, R3.
- R5 stopping for upper half: best score not improved over >= 3 independent restarts/methods, for each d. deps R4.
- R6 lower half: prove nabla_7 >= s7*, nabla_8 >= s8* (exact, e.g. SAT with cycle clauses + DRAT, or counting). deps R2.
- R7 match: upper (R4) = 2^d + (d-1)s* = lower (R2+R6)? deps R4, R6.

## Status
(see bottom; updated as work proceeds)

- R1 CHECKED — hand case tmp/hand_q2.txt (00,01,11,10 get labels 1..4): only valley 00; uphill paths
  (00), (00,01), (00,01,11), (00,01,11,10), (00,10) = 5 by hand; checker prints VERIFIED 5.
- R2 PROVED — Lemma A, claims.md section A (steps A1-A7).
- R3 PROVED (independent-S case) — claims.md "Construction principle"; not needed for the claim (checker scores used).
- R4 CHECKED — Q7.txt VERIFIED 464, Q8.txt VERIFIED 1040 (+ alternates).
- R5 CHECKED — d=7: 8 runs all 464; d=8: 3 runs all 1040; equal to lower bound.
- R6 PROVED/CHECKED — Lemma C (doubling, PROVED) + F_5 = 18 (lb_forest.py, exhaustive, CHECKED; SAT cross-check).
- R7 PROVED — 464 = 2^7 + 6*(128-72), 1040 = 2^8 + 7*(256-144); upper = lower for d = 7, 8.
