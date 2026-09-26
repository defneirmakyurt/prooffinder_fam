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
| Improvement layer I1 (telemetry: `done`, `telemetry`; events from `task`, `gate`, `pin`) and I5 (technique library: `lib add/list/import`, `task --lib`, `lessons`), with tests (267 checks) | `scripts/pp.py`, `scripts/tests/test_pp.py`, README §8 |

## To build (in order)

### B0. Problem skills from the official texts (no solving)

- [x] `problem-bulgarian-solitaire`:
  - fill in §1 (verbatim), §3, §4 and §5 from `sources/problem_description_bulgarian_solitaire.tex`;
  - complete the provenance table in §2; where it differs, the official text wins, and list every difference for the humans;
  - remove the "conventions only" banner.
- [x] `problem-disjoint-congruence-classes`: create it from `problem-template` using `sources/problem_description_disjoint_congruence_classes.tex`, verbatim, with every idea labelled as a hypothesis or angle.
- [x] Update the README board table and the head skill's problem list.
- **Acceptance:** every cell is present with verbatim text, points and checking mode; Part S seeds come from the statement only.

### B1. `scripts/pp.py`: phase machinery

- [x] **`ROLES` and regimes**, matching the head skill:

  | Role | Regimes |
  |---|---|
  | prover, searcher | BLIND / FRESH / CONTRARIAN / EXPLOIT |
  | breaker | BLIND / FRESH / CONTRARIAN |
  | checker-builder, referee | CLEAN-ROOM |
  | literature | LITERATURE |
  | triage | BLIND |
  | scribe, auditor | RECORD |

  Remove `scout`, and add `auditor` to `ROLE_LESSONS_ONLY`.
- [x] **`task --phase {0,1,1L,2,2A,2B,2B-XV,2C,3,GATE,REPAIR,WAVE,5,AUDIT}`** sets the role, regime and mode from a table.
  - Also accepts `--mode` (VERIFY / GATE / CROSS / SOLVE / ANALYST / ADVERSARY / BRANCH / SUBMISSION / REPORT), `--branch`, `--subject TASK`, `--obstacles TASK…`, `--earlier TASK…` and `--record`.
  - The brief header gains the lines `PHASE / MODE / BRANCH` and `SUBJECT`.
- [x] **Brief blocks:**
  - `reference_block()` appends the `**Role: MODE**` block after `**Role**`;
  - regime additions include BLIND;
  - a BRANCH lens pulls its text from reference §7 plus `--branch-note`.
- [x] **Inbox rules** (reference §1 table):
  - `checklist.md` is split into `checklist-G.md` (everyone except checker-builder) and `checklist-S.md` (referee only);
  - BLIND inboxes reject everything except obstacles (`stuck.md`, `verdict.md`, `no_natural_route.md`) and `checker/`;
  - `--subject` copies only `proof.md`, `claims.md` and `code/`;
  - `--record` copies `run/tasks/<P>-<cell>-*/` into `inbox/record/tasks/…` with paths preserved.
- [x] **`phases.md`:** append a row per task (reference §10).
- [x] **`open`:** also writes the `checklist.md` template (reference §9) and `phases.md` header.
- [x] **Board:** new columns `Phase` and `Robustness`, the 5 cell statuses, and a `contested` note section. Regenerate `run/board.md`.
- [x] **`matrix P CELL`:** reads the selected branches from the latest 2A task's `out/selected_branches.txt`, proofs from the output folders, and verdicts from `out/verdict.md` (`VERDICT:` / `CROSS VERDICT:` lines). Writes `matrix.md` and classifies it per reference §12.
- [x] **`gate P CELL --subject TASK [--statement-checked]`:**
  - finds the VERIFY/GATE referees on that subject;
  - checks that each ACCEPT has a complete checklist (every G/S item answered, no FAIL);
  - reads the matrix class if 2B ran;
  - writes `gate/gate_report.md` (reference §13) and prints VALID / GAP / INVALID.
- [x] **`status P`:** the per-phase table (reference §16).
- [x] **`blindcheck TASK`:** grep the blind outputs for arXiv, doi, http, "et al.", author-year patterns and "conjecture of"; print the hits.
- [x] **`finalize P CELL --report TASK --audit TASK`:** copy `final_report.md` only if the audit says `AUDIT: PASS`.
- [x] **`summary --branches b1 b2 …`:** merge the SUMMARY rows from each branch via `git show <branch>:run/SUMMARY.md`.
- [x] **`report`:** add the Robustness column, the new statuses, and the top 3 cells for human attention (CONTESTED or counterexample first, then PARTIAL by points).
- **Acceptance:**
  - scratch-copy tests for every phase: a brief is generated, the inbox rules are enforced, and forbidden inputs are rejected;
  - matrix and gate tested on synthetic verdict files covering ROBUST / CONTESTED / UNSUPPORTED and VALID / GAP / INVALID.

### B2. `scripts/guard.py`

- [x] The referee may write `out/verdict.md` **and** `out/cex/**`; its Bash redirects into `out/cex/` are allowed.
- [x] The new agent types need no special case. Literature, triage and auditor write only under `out/`.
- **Acceptance:** re-run the 15 original cases plus the new cex cases. (The original 15 were never saved; a rebuilt 15-case baseline plus 19 cex/Bash-write cases pass.)

### B3. Agents (locked cores; humans have authorised this build)

- [x] `prover.md`, `searcher.md`: BLIND regime, BRANCH mode (with `no_natural_route.md`), and outputs `claims.md`, `stuck.md`, `code/README.md`.
- [x] `breaker.md`: ADVERSARY mode with its four files (contrapositive, cex search, local analysis, minimal failing) and the verdict labels.
- [x] `referee.md`:
  - VERIFY / GATE modes run the 7-step protocol (Parts G + S, equality cases, cross-cell consistency, own cex search in `out/cex/`);
  - CROSS mode (branch lens, translate the key idea, CROSS verdict);
  - verdict blocks per reference §4.
- [x] `scribe.md`: SUBMISSION mode (current) and REPORT mode (`final_report.md`, reference §14, citations by path and step; uncited claims deleted).
- [x] New `literature.md`, replacing `scout.md`, which gets deleted:
  - tools Read, Write, Glob, Grep, Bash, WebSearch, WebFetch;
  - modes SOLVE (1L) and ANALYST (3).
- [x] New `triage.md`: tools Read, Write, Glob; never solves; output per reference §11.
- [x] New `auditor.md`: tools Read, Write, Glob, Grep; output per reference §15.
  **Amended 2026-09-26 after the dry run, with the humans' approval:** Bash added, so the Auditor re-runs the report's `RAN` lines instead of taking them on trust; the guard confines its Bash writes to `out/`.
- [x] Every agent keeps: the lessons-first read order, the guard hook, `omitClaudeMd: true`, `model: inherit`, honest-run rules, and the report block (reference §3).

### B4. Lessons

- [x] Rename `.claude/lessons/scout.md` to `literature.md`.
- [x] Add `triage.md` and `auditor.md` (at `version: 0`) and `pending/auditor.md`.

### B5. Remove build notes

- [x] Delete the "Build status" note in the head skill and in the README, and mark the Literature / Triage / Auditor rows in the README as built.

### B6. Problem branches (after B1–B5 are committed on `main`)

- [x] **Done 2026-09-26, pre-build:**
  - `main` merged into all 4 branches;
  - each branch's `.tex` moved to `sources/`;
  - `run/PROBLEM` added;
  - pushed with the user's OK.
- [x] **After the build:** merge `main` into all 4 branches again, and push. The user has authorised pushes for syncing. (Done 2026-09-26 after merging a teammate's push to `main`; D's `run/PROBLEM` updated.)

### B7. Restart Claude Code

This is needed because the agent files changed; agent edits aren't picked up by a running session.

### B8. Dry run (≤ 16 subagent calls)

**Run on 2026-09-26. Findings and fixes: `dryrun/2026-09-26-findings.md`.** 16 fresh subagent calls
used (A-C1 nine, H-C1 seven); interrupted workers were resumed in their own task folders, which
costs no extra slot.

- [x] **Hypercube C1** — 2 checker-builders, `crosstest` (208 cases, 0 disagreements), 2 blind
  searchers, head re-scoring, 1L literature, 2 referees on the lower-bound arguments.
  Values U(Q_3)=14, U(Q_4)=34, re-scored by the head; the literature route proves both bounds by
  hand. Cell PARTIAL until the gate closes.
- [x] **Angles C1** — checklist, 2 blind provers, 1L literature, 3 verifiers, 1 GATE referee,
  scribe REPORT, auditor. Gate VALID, cell SOLVED / PROVED, `final_report.md` filed after an
  audit PASS (the first audit returned FAIL on three citations; the repair loop was exercised).
- [x] **Audit afterwards:** isolation (`blindcheck` clean on every blind task; the guard had no
  audit trail, now fixed); report length; brief clarity; gate behaviour; Part S never left a
  referee inbox; telemetry gaps. All written up in the findings file.
- [x] Hypercube C1's checker passed the cross-test and is in the library as `H-uphill-checker`.
  The `--lib` dispatch path is covered by `test_pp.py`; a 16th call to hand an Angles prover a
  hypercube checker would have exercised nothing further and was spent on a referee instead.
- [x] Fixes implemented and tested (see the findings file's change table).
- [ ] Move the dry-run ledgers to `dryrun/2026-09-26/`, reset `run/`, and commit.
- Dry-run results are **not** submission-verified unless they pass the gate.
- [ ] Phases 2A–2C and 3 were not reached at this size. A second mini dry run (a small 2A/2B/2C/3
  chain on Angles C2) is still worth doing if the budget allows.

### B9. Clean up

- [ ] Delete `BUILD_PLAN.md` and remove its row from the README layout table.

## Open questions for the humans

1. ~~Angles cell count~~ **Resolved:** the official text has 6 cells; the extract had dropped Cell 1 and changed the order. `problem-angles-lines` has been rewritten from the official text.
2. ~~Disjoint congruence classes skill~~ **Built in B0.**
3. ~~Bulgarian solitaire cross-check~~ **Done in B0;** the differences are listed in the skill's §2.
6. ~~Cell 1 missing for B and D~~ **Resolved 2026-09-26:** both C1 texts were supplied from screenshots and are now in the skills and in `sources/` (B-C1 1 pt; D-C1 "Three classes", 1 pt, judged).
7. **D source says "all four" but lists five certificate items.** The skill keeps all five.
4. Does each head run on **its own account**? If heads share one, the concurrency split and tiering must be tighter.
5. The push to origin (`main` + 4 branches) is waiting for an OK.

## Improvement layer

**Decision (2026-09-26):** build only what pays off within one 7-hour run: I1 (it's free) and I5 (same-day sharing across the four problems). The rest either needs many runs of data or more subagent calls than the event has. Full description in README §8.

- [x] **I1. Per-task telemetry.** `run/telemetry.jsonl`:
  - `pp.py task` records role, regime, phase, angle, branch, subject, lesson versions and library entries;
  - `pp.py done TASK --tokens --ms [--score]` records the returned outputs and verdict;
  - `pp.py gate` and `pp.py pin` record what fed a gated claim;
  - `pp.py telemetry --by …` prints the yield table.
- [x] **I5. Technique library across problems.**
  - `run/library/<P>-<name>/` holds verified sources only (from `accepted/` or `checker/`), with a sha256 manifest;
  - `pp.py lib add | list --branches | import`;
  - `pp.py task --lib` (Prover / Searcher / Breaker; BLIND takes only code entries without literature markers);
  - `pp.py lessons --branches` for candidate role lessons.
- **Deferred**:
  - **I2 EVOLVE regime:** needs many generations;
  - **I3 regression set for gate lessons:** no past proofs yet;
  - **I4 adaptive allocation:** a bandit needs many trials per option;
  - **I6 head retrospective:** pays off between runs;
  - **I7 Lean 4:** days of setup.
  
  Revisit I4 and I6 first if the system runs again, using this run's telemetry.
