# Board: problem B, updated 16:26, run time 1:12 of 7:00

| Cell | Pts | Tier | Phase | Cell status | Claim status | Robustness | Best so far | Live lineages | Next | Time used |
|------|-----|------|-------|-------------|--------------|------------|-------------|---------------|------|-----------|
| C1 | 1 | T1: 1 pt; classical-style classification, base case (i) then general (ii) | SUBMISSION done (LaTeX + PDF in run/B/C1/submission/); Phase 5 report pending | SOLVED | PROVED | – | B-C1-002 VALID (003, 004); B-C1-001 VALID (005, 006) | diagonal-energy (both provers) | Phase 5 report + audit; add Brandt 1982 context if humans want | 0:26 |
| C2 | 2 | T1: 2 pts; one exact-value family, both bounds | SUBMISSION done: run/B/C2/submission/ (LaTeX + PDF) | SOLVED | PROVED | – | D_B(T_k)=k^2-k, all k; witness (k-1,k-1,k-2,...,2,1,1) | diagonal-rotation-CRT | - | 0:23 |
| C3 | 3 | T2: 3 pts, three parts (bound for all non-triangular n; exact value; all maximisers) | 1 done: 3 blind PARTIAL (lower bound k^2-2k-1 proved x3, upper GAP; exhaustive k<=10); 1L literature running | PARTIAL | (b) LOWER half PROVED: D_B(T_k-1) >= k^2-2k-1, k>=3 (gate on B-C3-002 scoped to lower half, referees 008+009); (a), (b) upper, (c) pending | – | witness (k-1,k-2,k-2,...,2,1,1); exhaustive k<=10 |  | referees on 1L proof | 0:00 |
| C4 | 5 | T2: 5 pts, exact value both bounds for all k>=5 | 1 running: B-C4-005..007 (Defne's session, lean track) | NOT ATTEMPTED | OPEN | – |  |  | TAKEN by Defne's session: first proof -> VERIFY + GATE referees together -> gate -> Scribe; do not resume C4 here | 0:00 |
| C5 | 8 | T2/T3: 8 pts, four stated requirements incl. C3-extension analysis | PAUSED by humans (focus B2, B3); Phase 1 stopped | NOT ATTEMPTED | OPEN | – |  |  | resume after B3 | 0:00 |

## Partial cells: established / remaining gap
- [16:03] B-C2: established D_B(T_k) >= k^2-k for all k (gate on B-C2-002 = LOWER half only, both referees scoped their ACCEPT to it); gap: upper bound, under review in B-C2-003.
- [16:09] B-C3: established D_B(T_k-1) >= k^2-2k-1 for k>=3, witness (k-1,k-2,k-2,k-3,...,2,1,1); gaps: (a), upper (b) (1L running), (c) (conditional prover running).

## Awaiting gate

## Contested cells (tell the humans)

## Lessons (changes since last checkpoint; pending Referee/Checker-builder/Auditor lessons)

## Decisions for the team
- [15:58] Humans: B2 first then B3; fewer agents; no Space agent on easy cells; proofs over reports. B4/B5 workers stopped; B-C2-008/009 created, not dispatched (reserve).
- [16:00] TOOLING (for main): pp.py task --target FILE writes the path into brief TARGET and inbox/target.md stays the full-cell target, so carved half-targets never reach the worker. Workaround: copy the carved target over inbox/target.md before dispatch. B-C3-005/006 stopped for this reason.
- [16:26] [16:26] B-C4 resumed by Defne's session (humans' request), lean track: reuses Phase 0 checklist/target; new tasks B-C4-005..007 (001-004 were the paused ones). Alexandra's session: please don't resume C4.

## Obstacle notes (parked cells)
