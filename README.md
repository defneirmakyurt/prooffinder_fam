# Proof Pursuit: multi-agent research pipeline

A Claude Code setup for the *Proof Pursuit* hackathon track: 4 problems, each a column of cells from a warm-up up to an open question, in 7 hours. Lower cells are checked instantly on the answer; upper cells are judged on proofs, constructions and computational certificates.

The system is built around one idea: **nothing reaches the board as established until an independent check says so.** A *head* agent runs each problem. It never does the mathematics itself. It dispatches isolated *worker* subagents, controls exactly what each one may see, stores everything on disk, runs the tests and gates, and writes the reports. The humans read everything and decide what gets submitted.

> **Build status:** the design below is complete and documented. Part of the tooling is still being built: the phase commands of `pp.py`, and the `literature`, `triage` and `auditor` agents. See [BUILD_PLAN.md](BUILD_PLAN.md) for what's done and what's left.

---

## 1. The whole process at a glance

```
 sources/<problem>.md ──► HEAD (one per problem, on its own git branch)
                          never solves · controls information · runs gates · writes reports
                                   │  per cell, easiest first; Tiering sizes each phase
   ┌───────────────────────────────┼─────────────────────────────────────────────┐
   ▼                               ▼                                             ▼
 PHASE 0 Checklist        PHASE 1 Blind solvers ──► PHASE 1L Literature ──► PHASE 2 Verifiers
 Part G (all agents)      no web, no history,       web on; reads blind      clean-room, 7-step
 Part S (referees only)   2–3 per cell              results; divergence      protocol + own cex search
                                                                                 │
                     ┌───────────────────────────────────────────────────────────┘
                     ▼  (cells worth 3+ points, or when solvers disagree)
 PHASE 2A Branch triage ──► PHASE 2B Perspective solvers ──► cross-verifiers ──► agreement matrix
 rates ALGEBRAIC /          one per selected branch          one per other branch   ROBUST / CONTESTED /
 TOPOLOGICAL / ANALYSIS /   (BLIND + branch lens)            ("translate the key    UNSUPPORTED
 NUMBER-THEORY / DISCRETE                                     idea")
                     │  not ROBUST
                     ▼
 PHASE 2C Adversary: contrapositive · counterexample search · local analysis · minimal failing lemma
                     │  not SOLVED
                     ▼
 PHASE 3 Literature analyst (web): what's known / sub-problems / attempts / WHY it can't be solved now
                     │
 VALIDATION GATE on every proof from every phase: 2 independent referees + matrix (where run) + head check
                     │
                     ▼
 PHASE 4 Synthesis: run/<P>/report.md + SUMMARY.md       PHASE 5 final_report.md per cell + citation audit
```

**Information moves forward only.** Blind agents never see literature, other agents' proofs, or the specific checklist (Part S). Whoever finds a proof never validates it. Agreement between agents counts as evidence, never as proof.

---

## 2. How the team runs it

| Branch | Problem | Skill |
|---|---|---|
| `angles_between_lines` | A: Angles between lines | `problem-angles-lines` |
| `uphill_paths_on_the_hypercube` | H: Uphill paths on the hypercube | `problem-hypercube-uphill` |
| `Bulgarian_solitaire` | B: Bulgarian solitaire | `problem-bulgarian-solitaire` |
| `Disjoint_congruence_classes` | D: Disjoint congruence classes | `problem-disjoint-congruence-classes` (C1 text missing from the official source) |

**One teammate, one branch, one head.** The shared tooling (skills, agents, scripts) lives on `main` and is merged into every problem branch. Each teammate:

1. Checks out their problem branch and makes sure it contains the latest `main`.
2. Creates the environment once: `python3 -m venv .venv && .venv/bin/pip install -r requirements.txt`, then `.venv/bin/python3 scripts/envcheck.py`.
3. Starts Claude Code in the repo. **Restart Claude Code after any change to `.claude/agents/`**, because agent files are only read at startup.
4. Pastes the verbatim problem text into `sources/` if it isn't there, and tells Claude to run the board (skill `proof-pursuit-head`).
5. Answers the head at the checkpoints (about 1:30, 3:00 and 5:15), and reads everything before submitting.

Cross-problem decisions (which problems get the most effort, which two to go deep on) are made by the humans, using the checkpoint statuses from each head. Four heads on four accounts also gives roughly four times the agent capacity. If heads share an account, agree a concurrency split.

**Day timeline:**

| Time | What happens |
|---|---|
| 0:00–5:15 | The pipeline runs, easiest cells first, breadth before depth. Checkpoints at about 1:30, 3:00 and 5:15. |
| 5:15 | **Freeze:** no new lineages or phases. |
| 5:15–6:15 | Gates, repairs of small gaps, final reports and audits. |
| 6:15–7:00 | Synthesis; the humans read, choose and submit. |

---

## 3. The pipeline per cell

| Phase | Who | Sees | Produces |
|---|---|---|---|
| **0 Checklist** | head (+2 checker-builders for computational cells) | the statement and problem skill | `checklist.md`: Part G (generic proof requirements, shown to everyone) and Part S (equality cases, required cases, traps, cross-cell consistency; referees only). Written without solving. |
| **1 Blind solvers** | 2 provers or searchers (3 for cells worth 3+ points) | statement, cell, Part G | `proof.md`, `claims.md`, `code/`, `stuck.md`. Standard textbook tools are allowed; results specific to this problem or its literature are not. |
| **1L Literature solver** | 1 literature agent | web + Phase 1 results | `sources.md`, its own attempt, and `divergence.md` (blind vs. literature, compared, never merged) |
| **2 Verifiers** | 1 referee per result | proof + claims + code + Parts G and S | `verdict.md` from the 7-step protocol, plus its own counterexample search |
| **2A Branch triage** | 1 triage agent | `stuck.md` and verdicts, not proofs | a relevance, entry point and risk for each of the 5 branches; `selected_branches.txt` |
| **2B Perspectives** | 1 solver per selected branch, then cross-verifiers from every other branch | BLIND + branch lens | proofs or `no_natural_route.md`; cross verdicts; the agreement matrix |
| **2C Adversary** | breaker in ADVERSARY mode | `stuck.md`, not proofs | contrapositive attempt, counterexample search with near misses, local optimality analysis, minimal failing sub-lemma |
| **3 Literature analyst** | literature agent | everything for the cell | what is known; sub-problems (known / hard to access / unknown); attempts; a precise note on why the cell can't be solved now |
| **Gate** | 2 referees + head + `pp.py gate` | — | `gate_report.md`: VALID / GAP / INVALID |
| **Repair** | new prover or searcher (EXPLOIT) | the proof + its gate report | a repaired proof, back to the gate |
| **4 Synthesis** | `pp.py report` | the gated board | `run/<P>/report.md` and `run/SUMMARY.md`: solved / partial / not attempted, established vs. gap, obstacles, top 3 cells for human attention |
| **5 Final report** | scribe (REPORT) + auditor | the cell's full record | `final_report.md`: 8 sections, every claim citing `tasks/<id>/out/<file>, step k`, final only after the audit passes. The scribe (SUBMISSION) packages the hand-in. |

**Which phases run where:**
- Phases 0, 1, 1L, 2 and the gate run on every cell.
- 2A–2C run on cells worth 3+ points, or where solvers disagree.
- Phase 3 runs on every cell that isn't solved.
- Phase 5 runs on every cell that reaches a terminal outcome.

**Tiering** (T0 direct → T3 open) sets how many agents each phase gets and how long it may run. It never changes the gate. **Computational cells** (constructions, exact values) keep checker-builders and searchers: two independent exact checkers, cross-tested, and every artefact re-scored and SHA-pinned. **Lineages, dead ends and repair waves** keep diversity going after the fixed phases: at most 3 live lines of attack per cell, with dead ends passed on to later workers so they avoid them.

---

## 4. Roles

| Role | Job | Tools |
|---|---|---|
| Prover | Line-by-line proof (blind, branch lens, repair, angle waves) | Read, Write, Edit, Glob, Grep, Bash |
| Searcher | Programs that produce constructions, exhaustive/SAT searches, certificates | same |
| Breaker | Refute targets early; ADVERSARY mode in Phase 2C | same |
| Checker-builder | Exact stdlib-only checker from the statement alone | same |
| Referee | VERIFY / GATE (7-step protocol) and CROSS (branch lens) | Read, Write (`verdict.md`, `cex/` only), Glob, Grep, Bash |
| Literature *(to build)* | SOLVE (Phase 1L) and ANALYST (Phase 3); the only role with web access | Read, Write, Glob, Bash, WebSearch, WebFetch |
| Triage *(to build)* | Branch relevance for Phase 2A; never solves | Read, Write, Glob |
| Scribe | SUBMISSION (hand-in) and REPORT (`final_report.md`) | Read, Write, Edit, Glob, Bash |
| Auditor *(to build)* | Checks every citation in a final report | Read, Write, Glob, Grep |

Every worker is a Claude Code subagent (`.claude/agents/<role>.md`) with `omitClaudeMd: true`, so personal CLAUDE.md rules don't leak in.

---

## 5. Information control and isolation

| Regime | Sees | Used for |
|---|---|---|
| BLIND | statement, cell, Part G, optional branch lens, checker; triage/adversary also get `stuck.md`/verdicts (never proofs) | Phase 1, 2A, 2B, 2C |
| FRESH / CONTRARIAN | statement + an assigned angle / a list of forbidden approaches | extra waves |
| EXPLOIT | one lineage's best + its critique or gate report | repair |
| CLEAN-ROOM | only the object under evaluation (+ Parts G/S for referees) | referees, checker-builders |
| LITERATURE | web + earlier results the phase allows | 1L, 3 |
| RECORD | accepted artefacts or the full cell record | scribe, auditor |

How it's enforced:
- Each worker gets a task folder `run/tasks/<id>/` holding `brief.md`, `inbox/` (copies the head places there) and `out/`. `pp.py task --phase` builds the inbox. It enforces the regime: Part S goes only to referees, and blind inboxes accept only obstacle files, never proofs.
- `scripts/guard.py`, a PreToolUse hook in every agent, binds a worker to its own task folder. It blocks reads of other tasks, the ledger and `.claude/`, and blocks writes outside `out/`. For Bash commands it can only pattern-match, so enforcement there is best effort. `pp.py blindcheck` flags literature markers in blind outputs, and any breach is reported to the humans at once.
- The head passes each worker a one-line prompt pointing at its task folder, and nothing else: no hints, no theorem or author names.

---

## 6. Verification and statuses

**Proofs** need two distinct clean-room referees to ACCEPT the same proof version. The Phase 2 verifier counts as one of them; the author never does. Each referee runs the 7-step protocol:
1. Checklist Parts G and S, item by item.
2. Line-by-line re-derivation.
3. Numerical sanity checks, with the code run and timed.
4. Equality-case test.
5. Cross-cell consistency.
6. Its own counterexample search.
7. A verdict with a reason for every step.

Where Phase 2B ran, the cell must also be **ROBUST**: confirmed by at least 3 other branches, or all of them when fewer than 4 are selected, with no GAP or REFUTED. The head checks the statement word for word, and `pp.py gate` computes VALID / GAP / INVALID from the verdict files.

**Computations and constructions:**
- Two independent checkers must agree, using exact or interval arithmetic.
- A judge must be able to rerun the checker in under 10 minutes on a laptop.
- Artefacts are SHA-pinned.
- The head re-runs every computation a claim depends on.
- "Exhaustive" needs a defined search space and a written soundness argument for each symmetry reduction.

**Exact extremal values** need a universal bound and a matching construction, and the two halves pass the gate separately. **Computer-assisted proofs** need a refereed reduction plus an exhaustive search. A finite check never proves "for all n". **Counterexamples** are re-verified exactly by a separate agent before the humans are told.

| Kind | Values |
|---|---|
| Claim | `PROVED`, `COMPUTER-VERIFIED`, `EXHAUSTIVE-WITHIN-CLASS`, `BEST-FOUND`, `CONJECTURED`, `OPEN`, `SEARCH-FOUND-NOTHING` |
| Cell | `SOLVED`, `PARTIAL` (always with established claims + the exact gap), `COUNTEREXAMPLE`, `NOT SOLVED`, `NOT ATTEMPTED` |
| Robustness | `ROBUST`, `CONTESTED`, `UNSUPPORTED`, or `–` where 2B didn't run |

A result is never called "new". The wording is always "not found in <sources searched>".

---

## 7. Learning during the run

- **Two layers per role.** Each role has a **locked core** (`.claude/agents/<role>.md`, edited by humans only) and a **lessons layer** (`.claude/lessons/<role>.md`, which the head may edit between phases).
- **Lessons travel in the inbox.** They reach every new task immediately, with no restart needed.
- **Problem lessons** go to `run/<P>/lessons.md`.
- **Evidence and rollback.** Every lesson cites the task ids that justify it. It is reverted if the next wave doesn't improve, logged in `CHANGELOG.md`, and committed.
- **No lesson may weaken verification.** That covers the gate, the checklist, exactness, isolation or blindness, status labels, and `RAN` records.
- **Gate-role lessons need approval.** Lessons for Referee, Checker-builder and Auditor wait in `pending/` until the humans approve them.

---

## 8. Repository layout

| Path | What it is | Who edits it |
|---|---|---|
| `.claude/skills/proof-pursuit-head/SKILL.md` | Head instructions: rules, roles, regimes, phases, tiering, gate, budget, learning | humans |
| `.claude/skills/proof-pursuit-head/references/briefs-and-ledger.md` | Brief blocks per role/mode, report and verdict formats, checklist, matrix, gate report, final report, audit, board | humans (`pp.py` parses it) |
| `.claude/skills/problem-<slug>/SKILL.md` | One per problem: verbatim statement, cells, hand-in, typing, ladders, checker spec, angle bank, pitfalls, Part S seeds, branch notes | humans; frozen during a run |
| `.claude/skills/problem-template/SKILL.md` | Template for new problem skills | humans |
| `.claude/agents/<role>.md` | Worker locked cores | humans only |
| `.claude/lessons/` | Lessons layer, `pending/`, `CHANGELOG.md` | head, between phases |
| `scripts/pp.py` | Ledger helper: tasks and inboxes, board, dead ends, pinning, cross-tests, matrix, gate, status, blind check, reports, finalize, summary | humans |
| `scripts/guard.py` | Isolation hook for workers | humans |
| `scripts/envcheck.py`, `requirements.txt` | Environment check (`.venv`: sympy, mpmath, networkx, python-flint, python-sat) | humans |
| `sources/` | Verbatim problem texts | humans |
| `run/` | The ledger for one problem per branch (layout in the head skill) | head |
| `BUILD_PLAN.md` | Temporary: what's still to be built | build session |

---

## 9. Output the humans get

- **`run/SUMMARY.md` and `run/<P>/report.md`:** each cell's outcome, claim status, robustness, established claims vs. remaining gap, obstacles, and the top 3 cells to look at now. `pp.py summary` merges the four branches.
- **`run/<P>/<cell>/final_report.md`:**
  - the outcome and exact statement;
  - the result;
  - how it was reached;
  - literature vs. ours;
  - reproducibility;
  - limitations ("agent agreement is evidence, not proof");
  - next steps.

  Every claim is cited to an artefact and step, and the report is audited.
- **Scribe submissions:** in each cell's exact hand-in format, with verification commands actually run and timed.

---

## Changelog of this build

- **2026-09-26, initial build:** head skill; seven worker agents with the isolation guard; `pp.py`, envcheck and the `run/` skeleton; problem template and the two practice problem skills.
- **2026-09-26, verification hardening:** statement rule, assumptions and stopping condition in briefs; `RAN` field; cell statuses; 7-item referee checklist; gate rules for extremal values, computer-assisted proofs and novelty; lessons layer; Bulgarian solitaire skill (conventions only).
- **2026-09-26, synthesis:** `pp.py report` (per-problem report and SUMMARY), obstacle note format, problem lessons file.
- **2026-09-26, merged phase pipeline (documented; build in progress):**
  - Phases 0–5 from the team's pipeline spec merged into the existing design: checklist Part G/S, blind solvers, literature solver, branch triage, perspective solvers with an agreement matrix, adversary, literature analyst, final report with audit.
  - One head per problem branch.
  - `SEARCH-FOUND-NOTHING` and the extra cell statuses.
  - A two-referee gate with a 7-step protocol.
