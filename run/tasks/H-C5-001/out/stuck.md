# Where the search stalls

By reduction.md (C), any labelling of Q_9 with <= 2399 uphill paths needs a feedback vertex set (FVS)
of Q_9 with <= 235 vertices (and, for equality-type constructions, few/cheap edges inside S).

- Independent FVS, one parity class: S = even class minus a set C whose members are pairwise at distance
  >= 4 (otherwise a 4-cycle survives); |S| <= 235 needs |C| >= 21. SA (runs 7, 8) always ends at rank 1
  (one surviving cycle) at |S| = 235, and at rank 0 only at |S| = 236 (2400). The even-only SAT (run 14)
  timed out.
- Independent FVS, both parity classes: SAT (run 13) says UNSAT for |S| <= 235 in 3.8 s (exploratory, no
  DRAT proof). Mixed independent sets also trap SA in small maximal independent sets (run 10).
- Non-independent FVS: plain-FVS SA (runs 18, 19) never goes below 236; plain-FVS SAT (runs 15, 17 for
  d=7) is slow (each lazy iteration ~ several seconds, ~200 cycles per model).
- Exact-count SA over arbitrary S (runs 11, 12) never leaves 2400: every single toggle costs >= 8.

What I could not reach: any FVS of Q_9 of size <= 235. If none exists then U(Q_9) = 2400 by (C) together
with the 2400 labelling; that is a lower-bound question (not this task's route) and would need a
complete, certified search (e.g. SAT with DRAT) that I did not produce.
