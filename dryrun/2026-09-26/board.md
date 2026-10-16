# Board: problem ?, updated 14:26, run time 1:52 of 7:00

| Cell | Pts | Tier | Phase | Cell status | Claim status | Robustness | Best so far | Live lineages | Next | Time used |
|------|-----|------|-------|-------------|--------------|------------|-------------|---------------|------|-----------|
| A-C1 | 1 | T0/T1: d=2 fixed, all N, short argument likely | GATE | SOLVED | PROVED | – | A-C1-001 proof, gate VALID (004 VERIFY + 006 GATE) | cut-averaging | done: final_report.md filed after AUDIT PASS | 0:00 |
| A-C2 | 2 | T1 (drill: full pipeline forced): 2 pts, a genuine lemma, all m | 5 | SOLVED | PROVED | ROBUST | A-C2-002 proof, gate VALID pre-2B and re-gated VALID with matrix ROBUST (005+006; XV 012 ALG + 013 ANA CONFIRMED) | tridiagonal-minors (001, 010 ALG); project-out-induction (002); gram-schmidt residuals (003 1L, 015 2C); trig AM-GM weights (011 ANA) | done: final_report.md (audit PASS); submission.md packaged (020) for the humans to read and submit | 0:00 |
| H-C1 | 1 | T0: Q3 brute force (8!) feasible; Q4 needs search, may rise | 2 | PARTIAL | BEST-FOUND (values); lower bounds GAP at the gate | – | U(Q3)=14, U(Q4)=34 (head re-scored VERIFIED); 1L proves both lower bounds by hand (no search) | prefix branch-and-bound (003+004, byte-identical artefacts = one lineage); equality-case counting (006, literature) | each proof has one ACCEPT; a second referee on H-C1-006 would close the gate (1 call) | 0:00 |

## Partial cells: established / remaining gap

## Awaiting gate

## Contested cells (tell the humans)
- [14:01] H-C1: the two blind searchers are one lineage, not two (byte-identical Q3.txt/Q4.txt, node counts 135168 vs 135169). Their agreement is weaker corroboration than it looks.

## Lessons (changes since last checkpoint; pending Referee/Checker-builder/Auditor lessons)

## Decisions for the team
- [12:27] [A-C2] Isolation near-miss (caught before dispatch): pp.py task --obstacles copies referee verdict.md into BLIND 2A/2C inboxes, and an ACCEPT verdict carries every Part S line plus a per-step reconstruction of the proof. A-C2-007 was created with it and never dispatched; A-C2-008 re-created with stuck.md-only obstacles. Needs a tooling decision: filter verdict.md to the VERDICT/FIRST PROBLEM lines, or copy verdicts only for non-ACCEPT outcomes. (A-C2 timestamps on this board and in telemetry.jsonl are UTC; the first run's are local, +02:00.)

## Obstacle notes (parked cells)
