# Board: problem A, updated 15:13, run time 0:00 of 7:00

| Cell | Pts | Tier | Phase | Cell status | Claim status | Robustness | Best so far | Live lineages | Next | Time used |
|------|-----|------|-------|-------------|--------------|------------|-------------|---------------|------|-----------|
| A-C1 | 1 | T0/T1: d=2 fixed, all N, short argument likely | GATE | SOLVED | PROVED | – | A-C1-001 proof, gate VALID (004 VERIFY + 006 GATE) | cut-averaging | done: final_report.md filed after AUDIT PASS | 0:00 |
| A-C2 | 2 | T1 (drill: full pipeline forced): 2 pts, a genuine lemma, all m | 5 | SOLVED | PROVED | ROBUST | A-C2-002 proof, gate VALID pre-2B and re-gated VALID with matrix ROBUST (005+006; XV 012 ALG + 013 ANA CONFIRMED) | tridiagonal-minors (001, 010 ALG); project-out-induction (002); gram-schmidt residuals (003 1L, 015 2C); trig AM-GM weights (011 ANA) | done: final_report.md (audit PASS); submission.md packaged (020) for the humans to read and submit | 0:00 |
| A-C3 | 3 | T1 (skill guess: first case in every dimension; 3 pts so 2A-2C run) | 0 done; 1 next | NOT ATTEMPTED | OPEN | – | – | – | Phase 0 checklist, then Phase 1: 3 blind provers | 0 |

## Partial cells: established / remaining gap

## Awaiting gate

## Contested cells (tell the humans)

## Lessons (changes since last checkpoint; pending Referee/Checker-builder/Auditor lessons)

## Decisions for the team
- [12:27] [A-C2] Isolation near-miss (caught before dispatch): pp.py task --obstacles copies referee verdict.md into BLIND 2A/2C inboxes, and an ACCEPT verdict carries every Part S line plus a per-step reconstruction of the proof. A-C2-007 was created with it and never dispatched; A-C2-008 re-created with stuck.md-only obstacles. Needs a tooling decision: filter verdict.md to the VERDICT/FIRST PROBLEM lines, or copy verdicts only for non-ACCEPT outcomes.
- [15:13] [15:13] Angles branch now carries Radu's A-C1/A-C2 (both gate VALID, audited). Humans: next cell is A-C3 only. H-C1 dry-run row removed from this branch's board (H lives on its own branch).

## Obstacle notes (parked cells)
