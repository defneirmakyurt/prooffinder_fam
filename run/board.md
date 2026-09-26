# Board: problem B, updated 16:33, run time 2:48 of 7:00

| Cell | Pts | Tier | Phase | Cell status | Claim status | Robustness | Best so far | Live lineages | Next | Time used |
|------|-----|------|-------|-------------|--------------|------------|-------------|---------------|------|-----------|
| C1 | 1 | T1: 1 pt; classical-style classification, base case (i) then general (ii) | SUBMISSION done (LaTeX + PDF in run/B/C1/submission/); Phase 5 report pending | SOLVED | PROVED | – | B-C1-002 VALID (003, 004); B-C1-001 VALID (005, 006) | diagonal-energy (both provers) | Phase 5 report + audit; add Brandt 1982 context if humans want | 0:26 |
| C2 | 2 | T1: 2 pts; one exact-value family, both bounds | SUBMISSION done: run/B/C2/submission/ (LaTeX + PDF) | SOLVED | PROVED | – | D_B(T_k)=k^2-k, all k; witness (k-1,k-1,k-2,...,2,1,1) | diagonal-rotation-CRT | - | 0:23 |
| C3 | 3 | T2: 3 pts, three parts (bound for all non-triangular n; exact value; all maximisers) | 1 done: 3 blind PARTIAL (lower bound k^2-2k-1 proved x3, upper GAP; exhaustive k<=10); 1L literature running | PARTIAL | (b) LOWER half PROVED: D_B(T_k-1) >= k^2-2k-1, k>=3 (gate on B-C3-002 scoped to lower half, referees 008+009); (a), (b) upper, (c) pending | – | witness (k-1,k-2,k-2,...,2,1,1); exhaustive k<=10 |  | referees on 1L proof | 0:00 |
| C4 | 5 | T2: 5 pts, exact value both bounds for all k>=5 | PAUSED by humans (focus B2, B3); Phase 1 stopped | NOT ATTEMPTED | OPEN | – |  |  | resume after B3 | 0:00 |
| C5 | 8 | T2/T3: 8 pts, four stated requirements incl. C3-extension analysis | PAUSED by humans (focus B2, B3); Phase 1 stopped | NOT ATTEMPTED | OPEN | – |  |  | resume after B3 | 0:00 |
| C6 | 13 | T3: open question, 13 pts; human-directed start at 16:40 | 0 done; 1 dispatched (3 blind provers 002-004, incremental proof.md); 2S map 001 running | NOT ATTEMPTED | OPEN |  |  |  | log each breakthrough in run/B/C6/progress.md; 1L after Phase 1; referees on any family result | 0:00 |

## Partial cells: established / remaining gap
- [16:03] B-C2: established D_B(T_k) >= k^2-k for all k (gate on B-C2-002 = LOWER half only, both referees scoped their ACCEPT to it); gap: upper bound, under review in B-C2-003.
- [16:09] B-C3: established D_B(T_k-1) >= k^2-2k-1 for k>=3, witness (k-1,k-2,k-2,k-3,...,2,1,1); gaps: (a), upper (b) (1L running), (c) (conditional prover running).

## Awaiting gate
- [16:29] [16:28] B-C3-007 (1L): full proof of (a), (b) both halves, (c) as {lambda: B^{k^2-2k-2}(lambda)=(k+1,k-1,...,3,1)}; RAN check.py 9 reproduced by head (ALL OK, 18 s); referees B-C3-015, B-C3-016 dispatched in parallel.

## Contested cells (tell the humans)

## Lessons (changes since last checkpoint; pending Referee/Checker-builder/Auditor lessons)

## Decisions for the team
- [15:58] Humans: B2 first then B3; fewer agents; no Space agent on easy cells; proofs over reports. B4/B5 workers stopped; B-C2-008/009 created, not dispatched (reserve).
- [16:00] TOOLING (for main): pp.py task --target FILE writes the path into brief TARGET and inbox/target.md stays the full-cell target, so carved half-targets never reach the worker. Workaround: copy the carved target over inbox/target.md before dispatch. B-C3-005/006 stopped for this reason.
- [16:21] [16:20] Session lost ~16:13 (usage limit); B-C3-007/010/011/012/013 re-dispatched under the same task ids to continue from their own out/. 2S map B-C3-001 decided: no 2B branch (S1/S2 restate live diagonal and c-sequence lineages), so Robustness stays '-' for C3.

## Obstacle notes (parked cells)
