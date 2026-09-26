# Build plan (temporary; delete when the build is done)

**For the build session after the restart.** Read this file first, then `README.md`, `.claude/skills/proof-pursuit-head/SKILL.md` and `.claude/skills/proof-pursuit-head/references/briefs-and-ledger.md`. Those three documents are the **spec**: they already describe the merged design. The code and agent files below must be brought in line with them.

Working rules from the user's global instructions:
- Commit after each numbered step, staging files by name.
- Never push without an explicit OK.
- Never commit `.env`.
- Ask before deviating from this plan.

## Decisions already made (don't re-ask)

1. **Statuses:**
   - claim: `PROVED`, `COMPUTER-VERIFIED`, `EXHAUSTIVE-WITHIN-CLASS`, `BEST-FOUND`, `CONJECTURED`, `OPEN`, `SEARCH-FOUND-NOTHING`;
   - cell: `SOLVED`, `PARTIAL`, `COUNTEREXAMPLE`, `NOT SOLVED`, `NOT ATTEMPTED`;
   - robustness: `ROBUST` / `CONTESTED` / `UNSUPPORTED` / `–`.
2. **ROBUST is required only on cells where Phase 2B runs** (3+ points, or solvers disagree). Other cells need the gate only.
3. **Proof gate:** two distinct referees ACCEPT the same proof version, each running the 7-step protocol. The Phase 2 verifier counts as one of them.
4. **Workspace:** workers stay in `run/tasks/<id>/`, so the guard is unchanged in principle. Each cell folder has `checklist.md`, `phases.md`, `matrix.md`, `gate/gate_report.md` and `final_report.md`.
5. **One head per problem branch.** The branches are `angles_between_lines` (A), `uphill_paths_on_the_hypercube` (H), `Bulgarian_solitaire` (B) and `Disjoint_congruence_classes` (D), and each gets a `run/PROBLEM` file. The shared tooling lives on `main`. Branches are merged locally, and **pushing waits for the user's OK**.
6. **Blind means blind to literature, not to mathematics.** Standard textbook tools are allowed; results specific to the problem or its literature are not.
7. **Reports stay short:** 200 words plus at most 10 LADDER lines, plus RAN/CHECKLIST lines.

## Done

| Item | Where |
|---|---|
| Head skill installed and extended (decomposition, problem skills, tiering, learning, synthesis; now the merged pipeline) | `.claude/skills/proof-pursuit-head/` |
| Reference: briefs per role/mode, report/verdict formats, board, lenses, checklist, phases index, triage output, matrix, gate report, final report, audit, status table | `references/briefs-and-ledger.md` |
| 7 worker agents (old design) with the lessons-first read order, RAN, and the 7-item referee checklist | `.claude/agents/` |
| Isolation guard hook (tested on 15 cases) | `scripts/guard.py` |
| Ledger helper (old design): open, task, deadend, board, pin, crosstest, report | `scripts/pp.py` |
| Environment check, `requirements.txt`, `.venv` (all 5 packages OK) | `scripts/envcheck.py` |
| Problem skills: template, A, H (practice), B (conventions only), each with Part S seeds + branch notes | `.claude/skills/problem-*/` |
| Lessons layer (7 roles + pending referee/checker-builder + CHANGELOG) | `.claude/lessons/` |
| README describing the whole process | `README.md` |

## To build (in order)

### B1. `scripts/pp.py`: phase machinery

- [ ] **`ROLES` and regimes**, matching the head skill:

  | Role | Regimes |
  |---|---|
  | prover, searcher | BLIND / FRESH / CONTRARIAN / EXPLOIT |
  | breaker | BLIND / FRESH / CONTRARIAN |
  | checker-builder, referee | CLEAN-ROOM |
  | literature | LITERATURE |
  | triage | BLIND |
  | scribe, auditor | RECORD |

  Remove `scout`, and add `auditor` to `ROLE_LESSONS_ONLY`.
- [ ] **`task --phase {0,1,1L,2,2A,2B,2B-XV,2C,3,GATE,REPAIR,WAVE,5,AUDIT}`** sets the role, regime and mode from a table.
  - Also accepts `--mode` (VERIFY / GATE / CROSS / SOLVE / ANALYST / ADVERSARY / BRANCH / SUBMISSION / REPORT), `--branch`, `--subject TASK`, `--obstacles TASK…`, `--earlier TASK…` and `--record`.
  - The brief header gains the lines `PHASE / MODE / BRANCH` and `SUBJECT`.
- [ ] **Brief blocks:**
  - `reference_block()` appends the `**Role: MODE**` block after `**Role**`;
  - regime additions include BLIND;
  - a BRANCH lens pulls its text from reference §7 plus `--branch-note`.
- [ ] **Inbox rules** (reference §1 table):
  - `checklist.md` is split into `checklist-G.md` (everyone except checker-builder) and `checklist-S.md` (referee only);
  - BLIND inboxes reject everything except obstacles (`stuck.md`, `verdict.md`, `no_natural_route.md`) and `checker/`;
  - `--subject` copies only `proof.md`, `claims.md` and `code/`;
  - `--record` copies `run/tasks/<P>-<cell>-*/` into `inbox/record/tasks/…` with paths preserved.
- [ ] **`phases.md`:** append a row per task (reference §10).
- [ ] **`open`:** also writes the `checklist.md` template (reference §9) and `phases.md` header.
- [ ] **Board:** new columns `Phase` and `Robustness`, the 5 cell statuses, and a `contested` note section. Regenerate `run/board.md`.
- [ ] **`matrix P CELL`:** reads the selected branches from the latest 2A task's `out/selected_branches.txt`, proofs from the output folders, and verdicts from `out/verdict.md` (`VERDICT:` / `CROSS VERDICT:` lines). Writes `matrix.md` and classifies it per reference §12.
- [ ] **`gate P CELL --subject TASK [--statement-checked]`:**
  - finds the VERIFY/GATE referees on that subject;
  - checks that each ACCEPT has a complete checklist (every G/S item answered, no FAIL);
  - reads the matrix class if 2B ran;
  - writes `gate/gate_report.md` (reference §13) and prints VALID / GAP / INVALID.
- [ ] **`status P`:** the per-phase table (reference §16).
- [ ] **`blindcheck TASK`:** grep the blind outputs for arXiv, doi, http, "et al.", author-year patterns and "conjecture of"; print the hits.
- [ ] **`finalize P CELL --report TASK --audit TASK`:** copy `final_report.md` only if the audit says `AUDIT: PASS`.
- [ ] **`summary --branches b1 b2 …`:** merge the SUMMARY rows from each branch via `git show <branch>:run/SUMMARY.md`.
- [ ] **`report`:** add the Robustness column, the new statuses, and the top 3 cells for human attention (CONTESTED or counterexample first, then PARTIAL by points).
- **Acceptance:**
  - scratch-copy tests for every phase: a brief is generated, the inbox rules are enforced, and forbidden inputs are rejected;
  - matrix and gate tested on synthetic verdict files covering ROBUST / CONTESTED / UNSUPPORTED and VALID / GAP / INVALID.

### B2. `scripts/guard.py`

- [ ] The referee may write `out/verdict.md` **and** `out/cex/**`; its Bash redirects into `out/cex/` are allowed.
- [ ] The new agent types need no special case. Literature, triage and auditor write only under `out/`.
- **Acceptance:** re-run the 15 original cases plus the new cex cases.

### B3. Agents (locked cores; humans have authorised this build)

- [ ] `prover.md`, `searcher.md`: BLIND regime, BRANCH mode (with `no_natural_route.md`), and outputs `claims.md`, `stuck.md`, `code/README.md`.
- [ ] `breaker.md`: ADVERSARY mode with its four files (contrapositive, cex search, local analysis, minimal failing) and the verdict labels.
- [ ] `referee.md`:
  - VERIFY / GATE modes run the 7-step protocol (Parts G + S, equality cases, cross-cell consistency, own cex search in `out/cex/`);
  - CROSS mode (branch lens, translate the key idea, CROSS verdict);
  - verdict blocks per reference §4.
- [ ] `scribe.md`: SUBMISSION mode (current) and REPORT mode (`final_report.md`, reference §14, citations by path and step; uncited claims deleted).
- [ ] New `literature.md`, replacing `scout.md`, which gets deleted:
  - tools Read, Write, Glob, Grep, Bash, WebSearch, WebFetch;
  - modes SOLVE (1L) and ANALYST (3).
- [ ] New `triage.md`: tools Read, Write, Glob; never solves; output per reference §11.
- [ ] New `auditor.md`: tools Read, Write, Glob, Grep; output per reference §15.
- [ ] Every agent keeps: the lessons-first read order, the guard hook, `omitClaudeMd: true`, `model: inherit`, honest-run rules, and the report block (reference §3).

### B4. Lessons

- [ ] Rename `.claude/lessons/scout.md` to `literature.md`.
- [ ] Add `triage.md` and `auditor.md` (at `version: 0`) and `pending/auditor.md`.

### B5. Remove build notes

- [ ] Delete the "Build status" note in the head skill and in the README, and mark the Literature / Triage / Auditor rows in the README as built.

### B6. Problem branches (after B1–B5 are committed on `main`)

- [ ] For each of the 4 branches: create a local tracking branch, merge `main`, add `run/PROBLEM` (letter + skill slug, e.g. `A problem-angles-lines`; `D` has no skill yet), and commit.
- [ ] Show the user the result. **Push only after their OK** (`main` is also 1+ commits ahead of origin).

### B7. Restart Claude Code

This is needed because the agent files changed; agent edits aren't picked up by a running session.

### B8. Dry run (≤ 16 subagent calls)

- [ ] **Hypercube C1 (`uphill_paths_on_the_hypercube`)** (6 calls):
  1. Phase 0 checklist + 2 checker-builders;
  2. `crosstest`;
  3. Phase 1: 2 blind searchers;
  4. re-score;
  5. 1L literature;
  6. gate on computational claims;
  7. scribe SUBMISSION.
- [ ] **Angles C1 (`angles_between_lines`)** (9 calls):
  1. Phase 0 checklist;
  2. Phase 1: 2 blind provers;
  3. 1L literature;
  4. Phase 2: one verifier per result (≤ 3);
  5. one GATE referee;
  6. scribe REPORT + auditor.
- [ ] **Audit afterwards:**
  - isolation leaks (guard denials, `blindcheck`, transcripts);
  - report length;
  - unclear briefs;
  - gate and matrix behaviour;
  - whether Part S stayed out of blind inboxes.
- [ ] Fix the skills and agents, then move the dry-run ledgers to `dryrun/2026-09-26/`, reset `run/`, and commit.
- Dry-run results are **not** submission-verified unless they pass the gate.
- Phases 2A–2C and 3 aren't covered at this size. Propose a second mini dry run (a small 2A/2B/2C/3 chain on Angles C2) if the budget allows.

### B9. Clean up

- [ ] Delete `BUILD_PLAN.md` and remove its row from the README layout table.

## Open questions for the humans

1. The extracted Angles column has **5 cells**, not 6. Check the original.
2. **Disjoint congruence classes:** paste the verbatim text so its skill can be built.
3. **Bulgarian solitaire:** paste the official text; the conventions need cross-checking.
4. Does each head run on **its own account**? If heads share one, the concurrency split and tiering must be tighter.
5. The push to origin (`main` + 4 branches) is waiting for an OK.
