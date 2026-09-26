# Plan: H-C5-001 (UPPER route: labelling of Q_9 with <= 2399 uphill paths)

Start 13:10 UTC, time box 75 min (stop ~14:25).

Notation: N(v) = number of uphill paths ending at v; total = sum_v N(v); |E(Q_9)| = 2304.

## Ladder

R1  Checker sanity: provided verify.py reproduces hand-computable small cases (Q_1, Q_2, Q_3 lex). -- deps: none
R2  Reduction lemma (written proof in out/reduction.md):
    (a) for any labelling, F := {v : N(v) = 1} induces a forest, each tree has exactly one valley,
        S := V \ F, and total = |E| + c(F) + sum over S-edges w<v of (N(w) - 1);
    (b) conversely, if S is an independent set of Q_d whose complement F induces a forest with c trees,
        the labelling "F first, parents before children, then S" has total = |E| + c = 2^d + (d-1)|S|.
    For d = 9: total = 512 + 8|S|, so total <= 2399  <=>  |S| <= 235.  -- deps: none
R3  Checked instance of R2(b): build labelling from an independent feedback set, compare checker vs formula. -- deps R1,R2
R4  Search engine for independent feedback vertex sets (IFVS) validated on small d (exact SAT optimum for d <= 6). -- deps R2
R5  Search Q_9 for IFVS with |S| <= 235 (SAT on orbit variables under symmetry groups + lazy cycle cuts; local search). -- deps R4
R6  If found: write Q9.txt, run provided checker, stop. -- deps R3,R5
R7  (only if R5 fails) generalise beyond independent S (non-independent S with cheap S-edges). -- deps R2

## Status (final, ~14:10 UTC)
R1 CHECKED  -- verify.py: Q_2 lex = 5 (hand count 1+1+1+2); d=3,4,5 builder outputs 14, 34, 88 = formula.
R2 PROVED   -- reduction.md Steps 0-6 and part (b).
R3 CHECKED  -- d=3,4,5 (runlog run 1) and d=9 (run 9): checker count = 2^d + (d-1)|S|.
R4 CHECKED (engine behaviour only) -- SAT reproduces one-class values d<=8; SA reaches them d=6,7,8.
            The SAT UNSAT answers are exploratory (no DRAT) and are not claimed.
R5 GAP      -- no FVS (independent or not) of Q_9 with |S| <= 235 found: SEARCH-FOUND-NOTHING, not exhaustive.
R6 NOT REACHED -- best hand-in Q9.txt = 2400 (matches known bound, earns nothing).
R7 GAP      -- plain-FVS SA and exact-count SA tried (runs 11,12,18,19); best 2400.

## Checklist-G pass
G1 target statement unchanged; claim is only "2400 labelling" + proved necessary condition. G2 reduction.md
written step by step, no "clearly". G3 d>=1 handled; Step 3 uses a cycle (>=4 vertices in Q_d, bipartite).
G4 N>=1 and N(w)>=2 on S shown. G5 part (b) valid for every d>=1 and every IFVS. G6 no citations. G7 all
reported scores from provided checker; no computation used as proof. G8 no cited results. G9 stuck.md,
claims.md say what is not established.
