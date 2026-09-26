# Where this search stalls (H-C5-004)

Blocked at the same place as the subject: no induced forest of Q_9 with more than 276 vertices (no decycling
set below 236) was found, so no labelling below 2400 exists among anything built here (a <= 2399 labelling
would need |S_f| <= 235 by the subject's identity, used only as a search guide).

What was tried and what it showed
* Unconstrained SA (subject's mif_sa, 9 new seeds, 2e7-5e7 moves): always 236, always the same type
  (2 vertices of one parity in S, 22 of that parity in F, e(S) = 13, 83 components). This type labels to 2406
  at best with the builder's order (extra 6), not 2400.
* SA constrained to parity-balanced forests (both classes >= 60): a second basin at |F| = 272 (135/137 split,
  16 components, e(S) = 112); LNS could not lift it.
* LNS with exact SAT re-solving of a subcube of dimension 7 or a ball of 130-170 vertices, from both basins:
  every region either proved non-improvable (UNSAT) or exhausted its conflict budget; plateau moves were
  possible (44-151 per run) but never led to an improvement. Regions of 200-256 vertices exhaust the budget.
* Exact SAT for symmetric forests: no 9-, 7- or 5-cycle-invariant forest of size >= 277 (UNSAT, no DRAT).
  Groups with more orbits (3-cycles: 176-192 orbits; involutions: >= 256 orbits) did not finish in 90-300 s.
* SAT for forests (O\Z) u M with 3 <= |Z| <= 8 did not finish in 240 s.
* Structured idea Q_8 x K_2 with two perfect-code halves: provably stuck at 272 (claims.md A2).

What might still work (not done)
* A certificate-producing SAT run (DRAT) for the symmetric classes, to turn the UNSAT answers into claims.
* Longer exact runs for order-3 and order-2 symmetric classes (each is a finite, well-defined class).
* Searching for 277 among forests far from both basins found here (neither near-parity nor 135/137 balanced).
* Honest assessment: two basins plateau at 276 and 272 under very different searches; if nabla(Q_9) = 236,
  the UPPER route is impossible and 2400 is optimal. That is not proved here.
