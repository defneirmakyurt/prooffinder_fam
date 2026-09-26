# Board: problem B, updated 16:00, run time 2:15 of 7:00

| Cell | Pts | Tier | Phase | Cell status | Claim status | Robustness | Best so far | Live lineages | Next | Time used |
|------|-----|------|-------|-------------|--------------|------------|-------------|---------------|------|-----------|
| C1 | 1 | T1: 1 pt; classical-style classification, base case (i) then general (ii) | SUBMISSION done (LaTeX + PDF in run/B/C1/submission/); Phase 5 report pending | SOLVED | PROVED | – | B-C1-002 VALID (003, 004); B-C1-001 VALID (005, 006) | diagonal-energy (both provers) | Phase 5 report + audit; add Brandt 1982 context if humans want | 0:26 |
| C2 | 2 | T1: 2 pts; one exact-value family, both bounds | 1: 002 PARTIAL (lower proved, upper GAP k>=12); lower-half referees + upper REPAIR running | NOT ATTEMPTED | lower: pending gate; upper: COMPUTER-VERIFIED k<=11 only | – | k^2-k (witness (k-1,k-1,k-2,...,1,1)); exhaustive k<=11 | diagonal-rotation-CRT | gate lower half; repair upper; await 001 and 1L | 0:23 |
| C3 | 3 | T2: 3 pts, three parts (bound for all non-triangular n; exact value; all maximisers) | 0 done, 1 + 2S running | NOT ATTEMPTED | OPEN | – |  |  | 3 blind provers + space map | 0:00 |
| C4 | 5 | T2: 5 pts, exact value both bounds for all k>=5 | PAUSED by humans (focus B2, B3); Phase 1 stopped | NOT ATTEMPTED | OPEN | – |  |  | resume after B3 | 0:00 |
| C5 | 8 | T2/T3: 8 pts, four stated requirements incl. C3-extension analysis | PAUSED by humans (focus B2, B3); Phase 1 stopped | NOT ATTEMPTED | OPEN | – |  |  | resume after B3 | 0:00 |

## Partial cells: established / remaining gap

## Awaiting gate

## Contested cells (tell the humans)

## Lessons (changes since last checkpoint; pending Referee/Checker-builder/Auditor lessons)

## Decisions for the team
- [15:58] Humans: B2 first then B3; fewer agents; no Space agent on easy cells; proofs over reports. B4/B5 workers stopped; B-C2-008/009 created, not dispatched (reserve).
- [16:00] TOOLING (for main): pp.py task --target FILE writes the path into brief TARGET and inbox/target.md stays the full-cell target, so carved half-targets never reach the worker. Workaround: copy the carved target over inbox/target.md before dispatch. B-C3-005/006 stopped for this reason.

## Obstacle notes (parked cells)
