# Plan: H-C5-004 (EXPLOIT of H-C5-002, UPPER route only)

Target: a labelling of Q_9 (file Q9.txt, 512 lines, line i = vertex with label i) with at most 2399 uphill
paths, as counted by inbox/checker/verify.py. Start time 13:35, time box 60 min (stop ~14:35).

Search guide (subject proof.md, not refereed; used only to steer the search, never as a score):
P(f) = 512 + 8|S_f| + sum_{u in S_f}(N(u)-2)up(u), S_f = {N >= 2}, V \ S_f an induced forest.
So a <= 2399 labelling needs an induced forest F of Q_9 with |F| >= 277 (|S| <= 235), and an order of S with
extra = sum (N-2)up <= 1887 - 8|S|.

Rungs
- R1 checker sanity: verify.py on subject Q9.txt gives 2400. [deps none]
- R2 structured idea: Q_9 = Q_8 x K_2 with a parity forest (perfect extended-Hamming code) in each half.
  Compute the best |F| this family can give. [deps none]
- R3 exact SAT-with-lazy-cycle-cuts (CEGAR) search for induced forests of size >= 277 invariant under a
  chosen cyclic subgroup <g> of Aut(Q_9); exhaustive over the class of <g>-invariant F for each g tried. [R1]
- R4 generic local search (improved max-induced-forest SA / tabu) on Q_9, several seeds; sanity on d=5..8. [R1]
- R5 if some |S| <= 235 is found: order S to make extra <= 1887 - 8|S|, write Q9.txt, run checker. [R3 or R4]
- R6 records: runlog, claims, stuck, README; checklist-G pass. [all]

Status (final)
- R1 CHECKED: verify.py on inbox/subject/Q9.txt -> VERIFIED 2400 (runlog 1).
- R2 PROVED (negative): two perfect-code halves of Q_8 x K_2 give at most 272 (claims.md A2).
- R3 PARTIAL: UNSAT (no DRAT) for 9-, 7-, 5-cycle-invariant forests of size >= 277; 3-cycle classes and
  (O\Z) u M with 3 <= |Z| <= 8 TIMED OUT (runlog 3-5, 18). SEARCH-FOUND-NOTHING, not a verification.
- R4 CHECKED (search only): SA reproduces 236 (9 seeds); balanced SA 240; LNS from both basins found no
  improvement (runlog 9-17). GAP: no forest with |F| >= 277.
- R5 NOT STARTED as intended (no |S| <= 235 found); the builder was validated on the 236 forests:
  VERIFIED 2400 (subject forest) and VERIFIED 2406 (SA forest type). out/Q9.txt = 2400.
- R6 CHECKED: runlog.md, claims.md, stuck.md, code/README.md written; checklist-G pass in runlog.md.
