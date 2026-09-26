# Board: problem B, updated 16:48, run time 3:03 of 7:00

| Cell | Pts | Tier | Phase | Cell status | Claim status | Robustness | Best so far | Live lineages | Next | Time used |
|------|-----|------|-------|-------------|--------------|------------|-------------|---------------|------|-----------|
| C1 | 1 | T1: 1 pt; classical-style classification, base case (i) then general (ii) | SUBMISSION done (LaTeX + PDF in run/B/C1/submission/); Phase 5 report pending | SOLVED | PROVED | – | B-C1-002 VALID (003, 004); B-C1-001 VALID (005, 006) | diagonal-energy (both provers) | Phase 5 report + audit; add Brandt 1982 context if humans want | 0:26 |
| C2 | 2 | T1: 2 pts; one exact-value family, both bounds | SUBMISSION done: run/B/C2/submission/ (LaTeX + PDF) | SOLVED | PROVED | – | D_B(T_k)=k^2-k, all k; witness (k-1,k-1,k-2,...,2,1,1) | diagonal-rotation-CRT | - | 0:23 |
| C3 | 3 | T2: 3 pts, three parts (bound for all non-triangular n; exact value; all maximisers) | SUBMISSION done: run/B/C3/submission/ (LaTeX + PDF, 10 pp) from gated B-C3-007 | SOLVED | PROVED | – | B-C3-007 VALID: (a) all k>=4; (b) D_B(T_k-1)=k^2-2k-1 (k>=4), D_B(2)=0, D_B(5)=3; (c) criterion B^{k^2-2k-2}(lambda)=nu_k |  | Phase 5 report + audit if time | 0:00 |
| C4 | 5 | T2: 5 pts, exact value both bounds for all k>=5 | LOWER half at gate (008 VERIFY + 009 GATE on B-C4-007); prover 006 running | NOT ATTEMPTED | CONJECTURED F(k)=(k-1)(k-3) (exhaustive k=5..12); LOWER proved by 005 and 007 (unrefereed); UPPER partial | – | witness (k-2,k-2,k-3,...,3,2,2,1), found independently by 005 and 007; weaker UPPER (k-1)(k-2) for all k (005) | diagonal energy + lap rotation (006, under repair 010); energy levels (007, lower half at gate); monotone coupling (005) | LOWER: referees 008/009; UPPER: repair 010 (EXPLOIT on 006) + literature 011 in parallel | 0:00 |
| C5 | 8 | T2/T3: 8 pts, four stated requirements incl. C3-extension analysis | PAUSED by humans (focus B2, B3); Phase 1 stopped | NOT ATTEMPTED | OPEN | – |  |  | resume after B3 | 0:00 |
| C6 | 13 | T3: open question, 13 pts; human-directed start at 16:40 | 1: 002, 004 PARTIAL (same lower bound F(n), D_B=F checked n<=60/62; head re-ran n<=55: 0 mismatches); 003 running; referees 006+007 on 004 lower bound; repair 008 on upper bound; 1L 009; FRESH 005; 2S 001 | PARTIAL | CONJECTURED D_B(n)=F(n) (checked n<=62); lower bound claimed x3, at gate |  |  |  | log each breakthrough in run/B/C6/progress.md; 1L after Phase 1; referees on any family result | 0:00 |

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
- [16:26] [16:26] B-C4 resumed by Defne's session (humans' request), lean track: reuses Phase 0 checklist/target; new tasks B-C4-005..007 (001-004 were the paused ones). Alexandra's session: please don't resume C4.
- [16:21] [16:20] Session lost ~16:13 (usage limit); B-C3-007/010/011/012/013 re-dispatched under the same task ids to continue from their own out/. 2S map B-C3-001 decided: no 2B branch (S1/S2 restate live diagonal and c-sequence lineages), so Robustness stays '-' for C3.
- [16:40] [16:42] Humans: C3(c) answered by the proved criterion {lambda: B^{k^2-2k-2}(lambda) = (k+1,k-1,...,3,1)} (both directions) counts as determined -> submit C3 as SOLVED if the gate passes; relayed to referee B-C3-016 as a target clarification. Humans: push the branch after each result.

## Obstacle notes (parked cells)
