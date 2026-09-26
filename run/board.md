# Board: problem A, updated 14:54, run time 0:54 of 7:00

| Cell | Pts | Tier | Phase | Cell status | Claim status | Robustness | Best so far | Live lineages | Next | Time used |
|------|-----|------|-------|-------------|--------------|------------|-------------|---------------|------|-----------|
| C5 | 8 | T2 (8pts, every d) — cost-capped to 2 blind provers, no 2S/2A/2B/2C unless solvers disagree | 1 done (2 blind + 1 ad hoc); no 2/2A/2B/2C/5-audit run (cost-capped) | PARTIAL | PROVED (d=2 only) | – | T>=1 all d (Thm A); T>=pi proved only at d=2 |  | verification (referees), or a Schur-complement/variational push on Theorem A' | ~0:35 |
| C5-D2 | (lemma of C5) | n/a | GATE done | SOLVED | PROVED | – | S<=2pi, N=4 lines in R^2 |  | n/a — done | ~0:54 |

## Partial cells: established / remaining gap
- [14:40] A-C5: d=2 (N=4) fully proved (2 independent elementary arguments, unverified by referees); d>=3 open. New partial: T>=1 for all d (Theorem A), tight-at-extremal weighted version Theorem A' (=1 at conjectured minimizer). Second-moment/Jensen family proved incapable of closing the gap for any d (constant capped at ~1.38<pi). See run/A/C5/final_report.md.

## Awaiting gate
- [14:50] A-C5-001 gated against the FULL cell target: GAP/INVALID-adjacent MAJOR x2 (both referees: statement match no, since only d=2 of every d>=2 is proved) — correct, cell stays PARTIAL. Carved the d=2 sub-claim into its own lemma-cell A-C5-D2 (its own checklist scoped to N=4,d=2 only) and dispatched 2 fresh referees (A-C5-D2-002/003) to gate it on its own honest scope.
- [14:54] A-C5-D2 (the d=2 lemma of A-C5) gated VALID: both A-C5-D2-002 and A-C5-D2-003 ACCEPT, complete checklists, statement match yes. Now labelled PROVED on the board. A-C5 itself (the full d>=2 cell) remains PARTIAL: this VALID gate covers only d=2.

## Contested cells (tell the humans)

## Lessons (changes since last checkpoint; pending Referee/Checker-builder/Auditor lessons)

## Decisions for the team

## Obstacle notes (parked cells)
