# Board: problem A, updated 15:32, run time 0:19 of 7:00

| Cell | Pts | Tier | Phase | Cell status | Claim status | Robustness | Best so far | Live lineages | Next | Time used |
|------|-----|------|-------|-------------|--------------|------------|-------------|---------------|------|-----------|
| A-C1 | 1 | T0/T1: d=2 fixed, all N, short argument likely | GATE | SOLVED | PROVED | – | A-C1-001 proof, gate VALID (004 VERIFY + 006 GATE) | cut-averaging | done: final_report.md filed after AUDIT PASS | 0:00 |
| A-C2 | 2 | T1 (drill: full pipeline forced): 2 pts, a genuine lemma, all m | 5 | SOLVED | PROVED | ROBUST | A-C2-002 proof, gate VALID pre-2B and re-gated VALID with matrix ROBUST (005+006; XV 012 ALG + 013 ANA CONFIRMED) | tridiagonal-minors (001, 010 ALG); project-out-induction (002); gram-schmidt residuals (003 1L, 015 2C); trig AM-GM weights (011 ANA) | done: final_report.md (audit PASS); submission.md packaged (020) for the humans to read and submit | 0:00 |
| A-C3 | 3 | T1 (skill guess: first case in every dimension; 3 pts so 2A-2C run) | GATE | SOLVED | PROVED | – | A-C3-002 proof, gate VALID (006 VERIFY + 007 GATE ACCEPT), pinned in accepted/ | arcsin-sum Gram nonsingularity (002, VALID); extremal minimiser sliding (001, unrefereed reserve) | Scribe SUBMISSION (008) packaging; humans read before submitting | 0 |

## Partial cells: established / remaining gap

## Awaiting gate

## Contested cells (tell the humans)

## Lessons (changes since last checkpoint; pending Referee/Checker-builder/Auditor lessons)

## Decisions for the team
- [12:27] [A-C2] Isolation near-miss (caught before dispatch): pp.py task --obstacles copies referee verdict.md into BLIND 2A/2C inboxes, and an ACCEPT verdict carries every Part S line plus a per-step reconstruction of the proof. A-C2-007 was created with it and never dispatched; A-C2-008 re-created with stuck.md-only obstacles. Needs a tooling decision: filter verdict.md to the VERDICT/FIRST PROBLEM lines, or copy verdicts only for non-ACCEPT outcomes.
- [15:13] [15:13] Angles branch now carries Radu's A-C1/A-C2 (both gate VALID, audited). Humans: next cell is A-C3 only. H-C1 dry-run row removed from this branch's board (H lives on its own branch).
- [15:18] [15:18] Humans: maximum speed. Fast track (gate unchanged): phases that don't depend on each other run in parallel; T1 cells keep exactly 2 branches; on the first proof: VERIFY + GATE referees + cross-verifiers dispatched together; 2B branch solvers only as fallback if Phase 1 proofs fail.
- [15:26] [15:26] Humans: finish A-C3 asap, time and cost efficient (not an open question). Cut: literature 1L stopped (A-C3-005); 2B cross-verifiers and branch solvers skipped (T1: only if solvers disagree), so robustness is '–'; final report/audit deferred. Kept: gate = two clean-room referees ACCEPT the same proof version + head's word-for-word statement check; Scribe SUBMISSION. C4-C6 not started.

## Obstacle notes (parked cells)
- [15:24] [15:24] A-C3: A-C3-001/002/003 (provers) and A-C3-005 (literature) died on an API session limit (HTTP 429); re-dispatched on the same task ids to keep their partial out/.
