# bainsahackathon: Proof Pursuit multi-agent build

A Claude Code setup for the Proof Pursuit hackathon. A **head** agent (skill `proof-pursuit-head`) runs the board. It dispatches isolated **worker** subagents, keeps a ledger in `run/`, and lets nothing reach the board as established until it passes an independent verification gate. The head doesn't do the mathematics itself.

## Layout

| Path | What it is | Who edits it |
|---|---|---|
| `.claude/skills/proof-pursuit-head/SKILL.md` | Head instructions: roles, regimes, loop, gate, budget, learning | humans |
| `.claude/skills/proof-pursuit-head/references/briefs-and-ledger.md` | Brief header, role brief blocks, report/verdict formats, board, angle generator, lessons format | humans (`pp.py` parses it) |
| `.claude/skills/problem-<slug>/SKILL.md` | One per problem: verbatim statement, cells, hand-in, ladders, checker spec, angle bank, pitfalls | humans; the head creates a missing one only from pasted verbatim text, then it's frozen |
| `.claude/skills/problem-template/SKILL.md` | Template for new problem skills | humans |
| `.claude/agents/<role>.md` | Worker **locked core** (7 roles) | **humans only** |
| `.claude/lessons/<role>.md` | Worker **lessons layer** | head, between waves |
| `.claude/lessons/pending/{referee,checker-builder}.md` | Lessons for the gate roles, awaiting human approval | head proposes, humans approve |
| `.claude/lessons/CHANGELOG.md` | Every lessons edit, with evidence and outcome | head |
| `scripts/pp.py` | Ledger helper: `open` (also creates `run/<P>/lessons.md` at version 0), `task` (brief + inbox), `deadend`, `board` (`--cell-status`, `--claim-status`), `pin`, `crosstest`, `report` (`run/<P>/report.md` per problem and `run/SUMMARY.md`: solved / partial / not attempted, established vs. gap, obstacles, pinned artefacts; generated from the gated board only). Scribe tasks require `--status` and `--cell-status`, and PARTIAL also requires `--established` (repeatable) and `--gap`. | humans |
| `scripts/guard.py` | PreToolUse isolation hook for workers | humans |
| `scripts/envcheck.py`, `requirements.txt` | Checks the `.venv` for sympy, mpmath, networkx, python-flint, python-sat | humans |
| `sources/practice-problems.md` | Verbatim source text of the practice problems (Angles, Hypercube); official competition texts go here too | humans |
| `run/` | The ledger: board, per-problem folders, `tasks/<id>/{brief.md, inbox/, out/}`, `<P>/lessons.md` | head |

## The board

| Problem | Skill | State |
|---|---|---|
| Angles between lines (A) | `problem-angles-lines` | ready |
| Uphill paths on the hypercube (H) | `problem-hypercube-uphill` | ready |
| Bulgarian solitaire (B) | `problem-bulgarian-solitaire` | **conventions only.** Cells and hand-in format wait for the official text. Every convention is in a provenance table to cross-check; if they differ, the official text wins. |
| Disjoint congruence classes | none | **not created, deliberately.** It will be built from the template only once the verbatim text is pasted, never from its title. |

## Worker roles and tools

| Role | Tools | Notes |
|---|---|---|
| Scout | Read, Write, Glob, WebSearch, WebFetch | the only role with web access; no Bash |
| Prover, Searcher, Breaker, Checker-builder | Read, Write, Edit, Glob, Grep, Bash | |
| Referee | Read, Write, Glob, Grep, Bash | the guard allows writing only `out/verdict.md`; Bash is limited to checks |
| Scribe | Read, Write, Edit, Glob, Bash | runs every verification command it documents |

All workers use `model: inherit` and `omitClaudeMd: true`. The global CLAUDE.md would otherwise tell them to "ask before starting", which subagents can't do, and would apply the human's git rules to them.

## Isolation design

Claude Code has no per-agent path scoping, and workers need Bash. Isolation is therefore enforced by a hook plus instructions, and it is **strong but not airtight**:

- `scripts/guard.py` runs as a PreToolUse hook declared in each agent's frontmatter. It binds a worker's agent id to the first `run/tasks/<id>/` it touches. From then on, it blocks reads anywhere else under `run/`, writes outside `out/`, and any access to `.claude/` or `dryrun/`.
- For Bash, it can only pattern-match the command text, so enforcement there is best effort. The dry run audits worker transcripts for leaks.
- Problem skills hold the whole angle bank and the pitfalls. A FRESH worker that saw the whole bank would break the regime design. So workers get no Skill tool and can't read `.claude/`. Each brief carries only its assigned angle and the relevant pitfalls.
- Lessons reach workers only as inbox copies (`role-lessons.md`, `problem-lessons.md`), so the guard needs no exception for `.claude/lessons/`.

## Verification rules (summary)

- **Claim statuses:** `PROVED`, `COMPUTER-VERIFIED`, `EXHAUSTIVE-WITHIN-CLASS`, `BEST-FOUND`, `CONJECTURED`, `OPEN`.
- **Cell statuses** (board and submissions): `SOLVED`, `PARTIAL` or `NOT ATTEMPTED`. `SOLVED` means every claim the hand-in requires has passed the gate. `PARTIAL` always lists the claims established and the exact remaining gap. A `BEST-FOUND` value in an instant-check cell makes the cell `PARTIAL`.
- **Proofs** need two clean-room referee ACCEPTs. Each must give its own reason for every step and answer the 7-item checklist. Agreement between referees is not proof.
- **Exact extremal values** need a universal bound plus a matching explicit construction, as functions of the parameters. The two halves go through the gate separately.
- **Computer-assisted proofs** need a refereed reduction to exactly the finite set searched, plus an exhaustive search over it. Finitely many parameter values never prove "for all".
- **`RAN` field:** every worker that executed code reports what ran, the range, COMPLETED / TIMED OUT / PARTIAL, and the measured runtime. The head re-runs every computation a claim depends on.
- **Novelty:** results are "not found in <sources searched>", never "new".

## Learning (lessons layer)

- Each role has a **locked core** (`.claude/agents/<role>.md`, humans only) and a **lessons layer** (`.claude/lessons/<role>.md`, head-editable).
- `pp.py task` copies the lessons into each new inbox and records the version in the brief's `LESSONS:` line. The core tells workers to read the lessons first, and says the core wins any conflict.
- Problem-specific lessons go to `run/<P>/lessons.md` and are copied only into that problem's briefs, never into Referee or Checker-builder briefs.
- A lesson may sharpen formats, habits, stopping conditions and tool use. It may **never** weaken the gate, the referee checklist, exactness or runtime requirements, isolation, status labels or `RAN`.
- Referee and Checker-builder lessons wait in `pending/` until humans approve them at a checkpoint.
- Edits happen between waves only, and each cites the task ids that justify it. If the next wave doesn't improve, the edit is reverted. Every edit is logged in `CHANGELOG.md` and committed to git.

**Reload behaviour (tested 2026-09-26):** edits to an existing `.claude/agents/*.md` file do **not** take effect in a running Claude Code session. A subagent dispatched after the edit still received the old core. Skills, in contrast, were picked up live. Consequences:
- A human edit to a locked core needs a **restart of Claude Code** before it applies.
- The lessons mechanism doesn't depend on reloading: lessons travel in the inbox, so they apply to the next dispatched task immediately.

## Setup and dry run

1. **Restart Claude Code** before any dispatch. New agent directories and edits to agent files are only picked up at startup.
2. **Environment:** each person creates their own `.venv` with `python3 -m venv .venv && .venv/bin/pip install -r requirements.txt`. All five packages install on Python 3.14. Check with `.venv/bin/python3 scripts/envcheck.py`, which should print "All required tools present". Every brief carries a `PYTHON:` line pointing workers at `.venv/bin/python3`; plain `python3` lacks the packages. Checkers and anything a judge re-runs stay stdlib-only. A standalone DRAT/LRAT proof checker (e.g. `drat-trim`) is optional, needed only if a hypercube lower bound rests on a SAT UNSAT proof.
3. **Planned dry run** (practice problems, 11 subagent calls, leaving 5 for a repair round or a tie-break referee; no Scouts):
   - Hypercube: 2 checker-builders, 2 searchers and 1 scribe. Cross-test and re-scoring are head scripts (`pp.py crosstest` with a random-permutation generator).
   - Angles: 1 breaker, 2 provers, 2 referees and 1 scribe. Both referees read the stronger proof, because the gate needs two ACCEPTs on the same proof.
   - "Determine U(Q4)" needs lower-bound evidence to be more than `BEST-FOUND`; the dry run checks that the gate labels it correctly.
4. **After the dry run:** move the dry-run ledger to `dryrun/2026-09-26/`, commit it for the record, and reset `run/` to the empty skeleton. `run/tasks/*/out/tmp/` is git-ignored.

**Report length:** 200 words, plus at most 10 LADDER lines of ≤ 15 words each and the RAN lines (and the CHECKLIST lines for referees). The full ladder stays in `out/plan.md`.

## Changelog of this build

- **2026-09-26, initial build:** head skill; seven worker agents with the isolation guard; `pp.py`, envcheck and the `run/` skeleton; problem template and the two practice problem skills.
- **2026-09-26, update:**
  - Brief header gains STATEMENT RULE, ASSUMPTIONS, STOPPING CONDITION and LESSONS.
  - Proofs may not use "clearly / routine / obviously / similarly" in place of an argument.
  - `RAN` field for every code-running worker, and honest-run rules.
  - Cell statuses SOLVED / PARTIAL / NOT ATTEMPTED.
  - Mandatory 7-item referee checklist; ACCEPT must give reasons.
  - Gate rules for exact extremal values, computer-assisted proofs and novelty.
  - Discipline perspectives in the angle generator.
  - Head working style.
  - Real four-problem board and the Bulgarian solitaire skill (conventions only).
  - Lessons layer with locked cores, pending approval for the gate roles, and a changelog.
  - Problem skills are frozen during a run; run notes move to `run/<P>/lessons.md`.
