# Plan: H-C5-005 (EXPLOIT of H-C5-002, UPPER route only)

Target: a labelling of Q_9 (file Q9.txt, 512 lines, line i = vertex with label i) with at most 2399 uphill
paths, scored by inbox/checker/verify.py. Time box 60 min (13:33-14:33).

Search guide (subject proof.md, NOT refereed; used only to steer search, never as a claim):
P(f) = |E| + c + sum over S-edges uw (u lower) of (N(u)-1), S = {N>=2}, c = #valleys = #forest components,
equivalently P = 512 + 8|S| + extra. P <= 2399 needs a decycling set S with |S| <= 235 and extra <= 1887-8|S|.

Ladder (status updated as work proceeds):
R1  checker reproduces 2400 on inbox/subject/Q9.txt                                   [deps: -]
R2  identity P = |E| + c + sum_{S-edges}(N(lower)-1) re-derived for "forest first, then S" labellings
    (used only as a search objective; final scores come from the checker)                [deps: -]
R3  SAT+CEGAR decycling-set solver (pysat, lazy cycle clauses) reproduces nabla(Q_d) upper values
    3,6,14,28,56,112 for d=3..8 (i.e. finds decycling sets of those sizes)               [deps: -]
R4  SAT+CEGAR on Q_9 finds a decycling set of size 236 (sanity)                            [deps: R3]
R5  SAT+CEGAR on Q_9 for size <= 235 (full, no symmetry assumption), time-limited          [deps: R4]
R6  structured sub-classes: symmetric (translation-invariant, |S|=234 / 232) SAT+CEGAR      [deps: R4]
R7  large-neighbourhood search (fix outside a subcube, SAT inside) from 236 solutions       [deps: R4]
R8  labelling builder: forest components BFS-first, S ordered to minimise extra; checker score [deps: R1]
R9  if |S|<=235 found with extra small: save out/Q9.txt, checker <= 2399 -> STOP             [deps: R5-R8]

## Status (end of time box, 14:15)
R1  CHECKED     checker on inbox/subject/Q9.txt -> VERIFIED 2400 (runlog run 1)
R2  CHECKED     (as a guide only) built labellings score 2400 / 2406 exactly as 512 + 8|S| + extra predicts (run 16)
R3  CHECKED     SAT-CEGAR finds decycling sets of size 3,6,14,28,56 for d=3..7 (run 2); d=8 via --oddmax 0 (112)
R4  CHECKED     Q_9 size 236 found by SAT in the near-parity class (run 18) and by SA (runs 7-12, 17)
R5  GAP         full SAT at d=9 infeasible in time; near-parity classes z=1,2 with K=235 TIMED OUT (runs 19-20)
R6  GAP         symmetric classes: SA over 9 nontrivial groups -> >= 237; C9 SAT timed out (runs 4, 5, 12)
R7  GAP         SAT-LNS: all 70 random 6/7-dim regions locally optimal (solver UNSAT, no DRAT); 8-dim timed out
R8  CHECKED     build_labelling.py + checker: out/Q9.txt, out/Q9_alt.txt VERIFIED 2400
R9  NOT REACHED no decycling set <= 235 found: SEARCH-FOUND-NOTHING; no <= 2399 labelling
R10 CHECKED     (added) L2: D-connected same-parity sets of size 2..5 have value <= 1 (exhaustive, code/cluster_value.py)
R11 PROVED      (added) L1, L3 (claims.md): |S| <= 235 forces a distance-2 cluster of size >= 6, value >= 2, on both
                parity sides (modulo the cited A(9,4) = 20)
