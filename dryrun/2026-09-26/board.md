# Board: problem ?, updated 14:26, run time 1:52 of 7:00

| Cell | Pts | Tier | Phase | Cell status | Claim status | Robustness | Best so far | Live lineages | Next | Time used |
|------|-----|------|-------|-------------|--------------|------------|-------------|---------------|------|-----------|
| A-C1 | 1 | T0/T1: d=2 fixed, all N, short argument likely | GATE | SOLVED | PROVED | – | A-C1-001 proof, gate VALID (004 VERIFY + 006 GATE) | cut-averaging | done: final_report.md filed after AUDIT PASS | 0:00 |
| H-C1 | 1 | T0: Q3 brute force (8!) feasible; Q4 needs search, may rise | 2 | PARTIAL | BEST-FOUND (values); lower bounds GAP at the gate | – | U(Q3)=14, U(Q4)=34 (head re-scored VERIFIED); 1L proves both lower bounds by hand (no search) | prefix branch-and-bound (003+004, byte-identical artefacts = one lineage); equality-case counting (006, literature) | each proof has one ACCEPT; a second referee on H-C1-006 would close the gate (1 call) | 0:00 |

## Partial cells: established / remaining gap

## Awaiting gate

## Contested cells (tell the humans)
- [14:01] H-C1: the two blind searchers are one lineage, not two (byte-identical Q3.txt/Q4.txt, node counts 135168 vs 135169). Their agreement is weaker corroboration than it looks.

## Lessons (changes since last checkpoint; pending Referee/Checker-builder/Auditor lessons)

## Decisions for the team

## Obstacle notes (parked cells)
