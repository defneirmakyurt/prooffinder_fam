# Proof Pursuit: multi-agent research pipeline

A Claude Code setup for the *Proof Pursuit* hackathon track: 4 problems, each a column of cells from a warm-up up to an open question, in 7 hours. Lower cells are checked instantly on the answer; upper cells are judged on proofs, constructions and computational certificates.

The system is built around one idea: **nothing reaches the board as established until an independent check says so.** A *head* agent runs each problem. It never does the mathematics itself. It dispatches isolated *worker* subagents, controls exactly what each one may see, stores everything on disk, runs the tests and gates, and writes the reports. The humans read everything and decide what gets submitted.

---

## 1. The whole process at a glance

```
 HUMANS   paste the verbatim problem into sources/ · start Claude Code on the problem branch · "run the board"
    │
    ▼
 HEAD     one per problem, on its own git branch · never solves · controls what each worker sees · runs the gates
    │     set-up: envcheck · problem skill · pp.py open · statement.md + target.md · tier every cell (T0–T3)
    │     then per cell, easiest first, breadth before depth
    ▼
 PHASE 0  Checklist: Part G (every agent) · Part S (referees only) · computational cells: 2 checker-builders + crosstest
    │
    ▼
 PHASE 1  Blind solvers, 2–3 per cell       ═══   PHASE 2S Space map (T2/T3 only, at the same time, web on)
    │     no web, no history                      4–8 space cards; the head decides every card (pp.py choose)
    ▼
 PHASE 1L Literature solver: web on, reads the Phase 1 results; divergence.md (compared, never merged)
    │
    ▼
 PHASE 2  Verifiers: one clean-room referee per result; 7-step protocol + its own counterexample search
    │     cells worth 3+ points, or solvers disagree
    ▼
 PHASE 2A Branch triage: rates ALGEBRAIC / TOPOLOGICAL / ANALYSIS / NUMBER-THEORY / DISCRETE
    │     (on T2/T3 the kept branches come from the space cards instead)
    ▼
 PHASE 2B Perspective solvers, one per kept branch (BLIND + branch lens) ──► cross-verifiers from every other branch
    │     ──► pp.py matrix: ROBUST / CONTESTED / UNSUPPORTED / INCOMPLETE
    │     not ROBUST
    ▼
 PHASE 2C Adversary: contrapositive · counterexample search · local analysis · minimal failing sub-lemma
    │     not SOLVED
    ▼
 PHASE 3  Literature analyst: what's known · sub-problems · attempts · WHY it can't be solved now
    │
    │     GATE, on every proof from any phase, the moment it appears
    │     ├ 2 clean-room referees ACCEPT the same version, and the proof is ROBUST itself where 2B ran
    │     ├ the head checks the statement word for word; pp.py gate → VALID / GAP / INVALID
    │     └ VALID → pp.py pin into accepted/ · GAP → REPAIR (a new EXPLOIT worker) + 2C · INVALID → downgrade
    │
    │     alongside: ≤ 3 live lineages per cell · FRESH / CONTRARIAN / EXPLOIT waves · dead ends passed on
    ▼
 PHASE 4  Synthesis: pp.py report → run/<P>/report.md + run/SUMMARY.md · pp.py summary merges the four branches
 PHASE 5  Final report per cell: Scribe REPORT → Auditor → pp.py finalize (only on AUDIT: PASS) · Scribe SUBMISSION
    │
    ▼
 HUMANS   read everything, choose what to submit, submit
```

**Information moves forward only.** Blind agents never see literature, other agents' proofs, space cards, or the specific checklist (Part S). Whoever finds a proof never validates it. Agreement between agents counts as evidence, never as proof. Numbers come from code the head re-runs, judgments from referees.

---

## 2. How the team runs it

| Branch | Problem | Skill |
|---|---|---|
| `angles_between_lines` | A: Angles between lines | `problem-angles-lines` |
| `uphill_paths_on_the_hypercube` | H: Uphill paths on the hypercube | `problem-hypercube-uphill` |
| `Bulgarian_solitaire` | B: Bulgarian solitaire | `problem-bulgarian-solitaire` |
| `Disjoint_congruence_classes` | D: Disjoint congruence classes | `problem-disjoint-congruence-classes` |

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

## 3. The pipeline, end to end

This section follows one problem from set-up to hand-in:
- 3.1 sets the problem up and sizes each cell;
- 3.2 and 3.3 list the phases and where each one runs;
- 3.4 follows one worker from creation to close;
- 3.5 walks one cell through every `pp.py` command;
- 3.6–3.8 cover the space map, the gate loop, and the lineages that keep going after the fixed phases;
- 3.9 says what each kind of problem emphasises.

The head skill (`.claude/skills/proof-pursuit-head/SKILL.md`) is the authoritative text. This section summarises it. `pp.py` below stands for `python3 scripts/pp.py`.

### 3.1 Set-up and tiering (once per problem)

1. `.venv/bin/python3 scripts/envcheck.py`.
2. The head loads the problem skill `problem-<slug>`. If it doesn't exist, the head copies `problem-template` and fills it in from the verbatim text in `sources/` in about 10 minutes, without solving anything. Every mathematical idea in it is labelled a hypothesis or an angle.
3. `pp.py open P C1 C2 …` creates `run/<P>/` (with `statement.md` and `lessons.md`) and, for each cell, `target.md`, a `checklist.md` template, `phases.md`, `deadends.md`, `checker/`, `lineages/`, `accepted/` and `gate/`.
4. The head copies the verbatim problem into `statement.md` and each cell's exact target into its `target.md`.
5. **Tiering.** The head spends at most about 5 minutes per cell, using only cheap signals:
   - points, and whether the cell is checked instantly, judged or open;
   - the cell type and ladder from the problem skill;
   - the size of the search space;
   - how much the cell depends on lower cells.

   The tier and a one-line reason go on the board (`pp.py board A-C2 --pts 2 --tier "T1: …"`).

| Tier | Typical signal | Phases and sizes | Time box |
|---|---|---|---|
| T0 direct | tiny finite computation or short standard argument | 0, 1 (2 solvers), 1L, 2, gate | 15–20 min |
| T1 routine | a known technique should suffice; moderate search | as T0; 2A–2C only if solvers disagree (2 branches) | 30–45 min |
| T2 hard | no obvious route; large search; 3+ points | full pipeline; 3 blind solvers; 2S alongside Phase 1, then 2B on the cards the head chooses | 60–75 min per attempt |
| T3 open | marked open | only after the lower cells are cleared; 2S first; a standing Breaker/adversary lineage; Phase 3 early | per budget |

Tiering sizes the phases; it never changes the gate.
- **Escalate** one tier when a phase returns no claim and no new rung, or when every proof comes back MAJOR/WRONG. Never de-escalate mid-cell.
- **Budget.** A 3+-point cell costs roughly 20–25 agent calls. Cross-verification is the part that grows: (proofs that passed Phase 2) × (kept branches − 1) calls.

### 3.2 The phases

| Phase | Who | Sees | Produces |
|---|---|---|---|
| **0 Checklist** | head (+2 checker-builders for computational cells) | the statement and problem skill | `checklist.md`: Part G (generic proof requirements, shown to everyone) and Part S (equality cases, required cases, traps, cross-cell consistency; referees only). Written without solving. |
| **1 Blind solvers** | 2 provers or searchers (3 for cells worth 3+ points) | statement, cell, Part G | `proof.md`, `claims.md`, `code/`, `stuck.md`. Standard textbook tools are allowed; results specific to this problem or its literature are not. |
| **1L Literature solver** | 1 literature agent | web + Phase 1 results | `sources.md`, its own attempt, and `divergence.md` (blind vs. literature, compared, never merged) |
| **2 Verifiers** | 1 referee per result | proof + claims + code + Parts G and S | `verdict.md` from the 7-step protocol, plus its own counterexample search |
| **2A Branch triage** | 1 triage agent | `stuck.md` and verdicts, not proofs | a relevance, entry point and risk for each of the 5 branches; `selected_branches.txt` |
| **2S Space map** (T2/T3 cells, in place of 2A) | 1 space agent, dispatched alongside Phase 1; then the head | statement, cell, Part G, optional checker and `stuck.md` (never proofs) | 4–8 space cards, found with web search: fidelity (EQUIVALENT / RELAXATION / RESTRICTION / LIMIT / ANALOGY / HEURISTIC), a translation check run on small cases, tightness, tools, what is known in the space, what no source has used, cost, payoff, an angle for FRESH workers. The head decides every card with `pp.py choose` (2B / VERIFIER / WAVE / DEADEND / HOLD / DROP), which writes `branches.txt` and `spaces.md` (§3.6) |
| **2B Perspectives** | 1 solver per selected branch, then cross-verifiers from every other branch (phase `2B-XV`) | BLIND + branch lens | proofs or `no_natural_route.md`; cross verdicts; the agreement matrix |
| **2C Adversary** | breaker in ADVERSARY mode | `stuck.md`, not proofs | contrapositive attempt, counterexample search with near misses, local optimality analysis, minimal failing sub-lemma |
| **3 Literature analyst** | literature agent | everything for the cell | what is known; sub-problems (known / hard to access / unknown); attempts; a precise note on why the cell can't be solved now |
| **Gate** | 2 referees + head + `pp.py gate` | — | `gate_report.md`: VALID / GAP / INVALID |
| **Repair** | new prover or searcher (EXPLOIT) | the proof + its gate report | a repaired proof, back to the gate |
| **Waves** | provers, searchers, breakers (FRESH, CONTRARIAN, EXPLOIT) | an assigned angle / the forbidden approaches / one lineage's best | as Phase 1, one lineage each (§3.8) |
| **4 Synthesis** | `pp.py report` | the gated board | `run/<P>/report.md` and `run/SUMMARY.md`: solved / partial / not attempted, established vs. gap, obstacles, top 3 cells for human attention |
| **5 Final report** | scribe (REPORT) + auditor | the cell's full record | `final_report.md`: 8 sections, every claim citing `tasks/<id>/out/<file>, step k`, final only after the audit passes. The scribe (SUBMISSION) packages the hand-in. |

The phase ids are the `--phase` values of `pp.py task`: `0 1 1L 2 2A 2S 2B 2B-XV 2C 3 GATE REPAIR WAVE 5 AUDIT`. The role, regime and mode follow from the phase.

### 3.3 Which phases run where

- Phases 0, 1, 1L, 2 and the gate run on every cell.
- 2A–2C run on cells worth 3+ points, or where solvers disagree. Easy cells get only two branches.
- 2S runs on T2/T3 cells and replaces 2A there: the head, not the agent, chooses the branches from the space cards.
- Phase 3 runs on every cell that isn't solved.
- Phase 5 runs on every cell that reaches a terminal outcome (SOLVED, COUNTEREXAMPLE, NOT SOLVED).
- **Computational cells** (constructions, exact values, searches) keep the checker machinery:
  - two checker-builders write independent exact checkers, which are cross-tested; every artefact is re-scored and SHA-pinned;
  - Phase 1 solvers are Searchers with the checker;
  - in 2B, branch lenses act as search angles (COMPUTATIONAL is a searcher-only lens), and a construction is verified by re-scoring, not by the matrix;
  - lower-bound *arguments* still go through the full proof pipeline.

### 3.4 One worker, start to finish

1. **Create.** `pp.py task P CELL --phase PH --stop "…"`:
   - picks the task id `<P>-<cell>-<nnn>`, and the role, regime and mode for the phase;
   - writes `run/tasks/<id>/brief.md`: the header (target, statement rule, assumptions, stopping condition, lesson versions, rules, return format), then the role block and mode block;
   - fills `inbox/` under the regime's rules and refuses anything the regime forbids;
   - appends a row to the cell's `phases.md` and a `task` event to `run/telemetry.jsonl`;
   - prints the dispatch line.
2. **Dispatch.** The head uses the Agent tool with `subagent_type` = the role, passes exactly the printed one-line prompt and nothing else, and puts several dispatches in one message so they run in parallel.
3. **Work.** The worker reads `inbox/role-lessons.md`, then `inbox/problem-lessons.md` if it exists, then `brief.md` and the inbox.
   - Provers, searchers and breakers first write `out/plan.md`, a ladder of numbered rungs, and work through it.
   - `scripts/guard.py` keeps the worker inside its task folder and lets it write only to `out/`.
4. **Return.** The worker returns only its report block: OUTCOME, CLAIM, LADDER, RAN, ARTEFACTS, IDEA-TAG, KNOWN GAPS, DEAD ENDS and SCORE, in at most 200 words plus the LADDER and RAN lines. Everything else stays in `out/`.
5. **Close.** The head:
   - runs `pp.py done TASK --tokens N --ms N [--score S]`;
   - runs `pp.py blindcheck TASK` on every blind output;
   - re-runs every `RAN` line a claim depends on (if one doesn't reproduce, the whole report is untrusted);
   - re-scores any artefact with the cell's checker;
   - updates the board.
6. **Interrupted?** The head re-dispatches the *same* task id, adding one sentence that says `out/` holds the worker's own interrupted work. A report sent back after an audit FAIL is re-dispatched the same way, with the failing citations verbatim and nothing else.

### 3.5 One cell, command by command

In the block below:
- the example is cell A-C2;
- `<task>` is an id printed by `pp.py task`;
- every `--stop "…"` is a stopping condition suited to the task.

Each `task` line is followed by a dispatch and, on return, the closing steps of §3.4.

```bash
# Set-up (once per problem)
.venv/bin/python3 scripts/envcheck.py
pp.py open A C1 C2 C3 C4 C5 C6                  # then fill statement.md and each target.md
pp.py board A-C2 --pts 2 --tier "T1: <reason>"

# Phase 0: the head writes run/A/C2/checklist.md (Part G + Part S) without solving
pp.py task A C2 --phase 0 --stop "…"            # computational cells: two checker-builders
pp.py crosstest <task1>/out/verify.py <task2>/out/verify.py --gen "<command printing one artefact for {seed}>" \
    --log run/A/C2/checker/crosstest.log        # once they agree, the checkers go into run/A/C2/checker/

# Phase 1 (and, on T2/T3, the 2S map in the same message)
pp.py task A C2 --phase 1 --role prover --stop "…"                               # 2 blind solvers, 3 on 3+-point cells
pp.py task A C2 --phase 1 --role searcher --checker run/A/C2/checker --stop "…"  # computational cells
pp.py task A C2 --phase 2S --checker run/A/C2/checker --stop "…"                 # T2/T3 only

# Phase 1L and Phase 2
pp.py task A C2 --phase 1L --earlier <phase-1 tasks> --stop "…"
pp.py task A C2 --phase 2 --subject <proof task> --stop "…"         # one verifier per result
#   a computational claim adds --checker run/A/C2/checker --subject-file best.txt

# Gate, as soon as a proof has one ACCEPT
pp.py task A C2 --phase GATE --subject <proof task> --stop "…"      # the second referee
pp.py gate A C2 --subject <proof task> --statement-checked          # VALID / GAP / INVALID
pp.py pin A C2 run/tasks/<proof task>/out/proof.md …                # VALID only: accepted/ + sha256

# 3+ points, or solvers disagree: choose branches, then 2B
pp.py task A C2 --phase 2A --obstacles <tasks> --stop "…"           # → selected_branches.txt
pp.py choose A C2 --map <2S task> --take "S1=2B: <reason>" --take "S2=VERIFIER: <reason>" …   # T2/T3 → branches.txt
pp.py task A C2 --phase 2B --role prover --branch ALGEBRAIC --stop "…"         # one per solver branch
pp.py task A C2 --phase 2 --subject <2B proof> --stop "…"                      # its Phase 2 verifier
pp.py task A C2 --phase 2B-XV --branch DISCRETE --subject <2B proof> --stop "…" # one per other kept branch
pp.py matrix A C2                                                   # ROBUST / CONTESTED / UNSUPPORTED / INCOMPLETE

# Not ROBUST → 2C · not SOLVED → 3 · a GAP at the gate → repair
pp.py task A C2 --phase 2C --obstacles <tasks> --stop "…"
pp.py task A C2 --phase 3 --earlier <tasks> --stop "…"
pp.py task A C2 --phase REPAIR --role prover --subject <gapped proof> --stop "…"   # inbox gets its gate report

# Lineages, dead ends and extra waves (§3.8)
pp.py deadend A C2 --tag <idea-tag> --task <task> "approach — why it fails"
pp.py task A C2 --phase WAVE --role prover --regime FRESH --angle "<angle>" --stop "…"
pp.py task A C2 --phase WAVE --role prover --regime CONTRARIAN --forbid-file run/A/C2/deadends.md --stop "…"

# Terminal outcome: Phase 5
pp.py task A C2 --phase 5 --mode REPORT --status PROVED --cell-status SOLVED --stop "…"   # copies the full record
pp.py task A C2 --phase AUDIT --subject <report task> --stop "…"
pp.py finalize A C2 --report <report task> --audit <audit task>     # only on AUDIT: PASS
pp.py task A C2 --phase 5 --mode SUBMISSION --status PROVED --cell-status SOLVED --stop "…"

# Synthesis, and at every checkpoint (about 1:30, 3:00, 5:15)
pp.py report                                    # run/A/report.md + run/SUMMARY.md
pp.py status A                                  # per-phase table + tasks with no 'done' event
pp.py telemetry --by role regime                # tokens and yield
pp.py lib list --branches <other problem branches>
pp.py lessons --branches <all problem branches>
pp.py summary --branches angles_between_lines uphill_paths_on_the_hypercube Bulgarian_solitaire Disjoint_congruence_classes
```

At each checkpoint the head also reads `run/guard.log` (every isolation denial) and commits the ledger, staging `run/` paths by name. A PARTIAL cell's Scribe task also takes `--established "…"` (repeatable) and `--gap "…"`.

### 3.6 Choosing spaces (Phase 2S)

On T2 and T3 cells, a Space agent maps the cell before the head chooses branches.
- **Dispatch.** It runs under LITERATURE (web on), alongside Phase 1, with `--checker` where the cell has one and `--inbox` for any human-provided material.
- **Second map.** If Phases 1–2 leave stuck points that the map doesn't address, the head dispatches a second map at 2A time with `--obstacles`.
- **Output.** 4–8 cards in `out/spaces.md`, plus `graph.md` (links between spaces and neighbouring problems), `spec.md` (properties any valid proof must have) and `proposals.md`.
- **Card fields:** BRANCH, FIDELITY, FEEDS, CHECK, TIGHT, TOOLS, KNOWN, UNEXPLORED, COST, PAYOFF, ANGLE, FIRST TASK.

The agent never chooses. The head evaluates every card from its fields and from reruns, not from mathematics of its own:
1. **Reproduce:** rerun the card's check from its RAN line; a card that doesn't reproduce is dropped.
2. **Direction:** a bound needs RELAXATION or EQUIVALENT; a construction or counterexample needs RESTRICTION or EQUIVALENT; LIMIT, ANALOGY and HEURISTIC are at most angles for a FRESH wave.
3. **Known vs. unexplored:** a route already run to its end is at most a DEADEND or a pointer for Literature; a concrete UNEXPLORED item that passes its check is a strong WAVE candidate.
4. **Tightness:** on a cell with equality cases, a relaxation with TIGHT NO cannot carry the proof.
5. **Specification ledger:** drop or downgrade a card that breaks an item in `spec.md`.
6. **Diversity:** prefer cards whose tag differs from every live lineage.
7. **Cost and payoff** against the time box and the remaining budget.
8. **Pairing:** on exact-value and prove-or-disprove cells, keep at least one card on each side.

Then it decides every card with `pp.py choose P CELL --map TASK --take "S<n>=ACTION: reason" …`:

| Action | Use it for | What follows |
|---|---|---|
| `2B` | CHECK PASSED, EQUIVALENT / RELAXATION / RESTRICTION, not TIGHT NO; the strongest card on its branch | a blind 2B solver on that branch, with the generic branch lens only (never card text) |
| `VERIFIER` | a branch whose viewpoint gives an independent check | that branch cross-verifies the 2B proofs |
| `WAVE` | UNEXPLORED items, LIMIT / ANALOGY / HEURISTIC or unchecked cards, a second card on a taken branch, search-only or bound-only tasks | a FRESH wave with the card's ANGLE, when a wave is due |
| `DEADEND` | TIGHT NO or CHECK FAILED | the obstruction goes to `deadends.md`, and CONTRARIAN briefs inherit it |
| `HOLD` | plausible but not affordable now | re-admitted first if every chosen branch fails |
| `DROP` | irreproducible, irrelevant, or dominated | nothing |

`choose` refuses a decision that breaks the table's preconditions, and a reason is required for every card. It then:
- writes `branches.txt`, which the matrix reads in place of the triage;
- appends the decision record to `run/<P>/<cell>/spaces.md`;
- prints the `pp.py task` lines to run next.

The rest of the map is routed like this:
- `spec.md` items go into Part S as labelled hypotheses;
- `NEIGHBOUR QUESTION` lines and cited sources go to the Phase 3 literature agent;
- a card's ANGLE is the only card text that ever reaches a worker, and only a FRESH one;
- nothing from a map ever reaches a blind agent or `run/<P>/lessons.md`.

Every task dispatched from a card carries the card's tag as `--angle`, so `pp.py telemetry --by angle` shows which spaces fed gated claims. When every kept card has failed:
1. re-admit the HOLD cards;
2. then dispatch a fresh map with the obstacles;
3. only then escalate the tier.

### 3.7 The gate, repair and escalation

The gate runs on any proof or partial proof from any phase, the moment it appears. The Phase 2 verifier is the first referee, a GATE-mode referee the second, and the author never counts. `pp.py gate` decides:
- **VALID** when both referees ACCEPT the same version with complete checklists, the proof is ROBUST itself where 2B ran on the cell, and the head has checked the statement word for word (`--statement-checked`);
- **INVALID** on any `WRONG`;
- **GAP** otherwise.

It writes `gate/gate_report.md` and keeps a copy per proof in `gate/<task>.md`. What follows:

| Outcome | Next |
|---|---|
| VALID | pin the artefacts into `accepted/` (`pp.py pin`), mark `PROVED` on the board, and add any reusable tool to the library (§8) |
| GAP | a REPAIR worker (a new prover or searcher, EXPLOIT) gets the proof and its gate report; the cell also goes to 2C. The repaired version goes back through Phase 2, the cross-verifiers where 2B ran, and the gate |
| INVALID | the claim is downgraded, never deleted; the humans are told |
| referees disagree | the disputed step alone goes to a third referee |

Two special cases:
- **Counterexamples** are re-verified in exact or interval arithmetic by a separate agent, and by two agreeing checkers where a checker exists, before the humans are told.
- **Exact values and computer-assisted proofs** go through the gate in two halves (§6).

When a time box expires with no checkable artefact, the head writes a status note and moves the workers. The tier escalates as in §3.1.

### 3.8 Lineages, extra waves and decomposition

Once the fixed phases have run, diversity is kept going on purpose. A **lineage** is one line of attack on one cell. It has:
- an idea tag of 2–4 words;
- a current best;
- its latest critique, gate report or score;
- its dead ends.

The rules:
- **At most three live lineages per cell.** Repair workers are spread across them rather than stacked on the leader.
- **Open** a lineage when a result is structurally different from the existing ones and either scores near the best or gets `MINOR`.
- **Retire** it after two waves without improvement. Its dead ends move to the cell's `deadends.md`, so CONTRARIAN workers inherit them.
- **Merge** two lineages only when they turn out to be the same idea under different tags.

Extra waves follow this mix:

| Cell state | Exploit | Fresh | Contrarian | Also |
|---|---|---|---|---|
| Improving (best improved last wave) | ~60% | ~25% | ~15% | referees on each new best |
| Stagnant (2 waves, no gain) | ~20% | ~40% | ~40% | retire the weakest lineage |
| Converged (half or more of reports share an idea tag) | ≤20% | re-angle everyone | the rest | tell the team |
| Endgame (claims freeze near) | repair only | – | – | referees, scribe, auditor |

Every FRESH or CONTRARIAN brief changes at least one axis relative to every live lineage: branch lens, representation, method family, structural assumption, scale, or direction. Each such brief gets exactly **one** angle, from the problem skill's angle bank or a chosen space card.

**Decomposition** happens mostly inside a worker's task:
- The worker writes its target as a ladder in `out/plan.md` and marks each rung `PROVED` / `CHECKED` / `GAP` / `REFUTED` / `NOT STARTED`.
- A `GAP` rung becomes the target of the lineage's next repair worker.
- A rung becomes its own task only when:
  - the same lemma blocks several lineages;
  - it is doubtful enough to send a Breaker first;
  - it should be attacked from several angles in parallel;
  - it needs its own referee or checker.
- A ladder of `PROVED` rungs is still a claim: referees check the assembled proof, and the head re-runs every `CHECKED` rung.

### 3.9 Problem types

| Type | Emphasis |
|---|---|
| Scored construction | checkers first, then mostly searchers; diversity from representations and method families; only re-scored artefacts count |
| Exact value with an instant check | a construction plus lower-bound evidence. Without a proved lower bound, the value is submitted only when three independent lineages plateau at it, as `BEST-FOUND`, with the cell `PARTIAL` |
| Prove a stated inequality or lemma | the full proof pipeline, with breakers first on doubtful intermediate lemmas |
| Lower bound / optimality | provers write the reduction, searchers run the exhaustive, SAT or LP computation; the referee reads the reduction, the checker verifies the certificate |
| Open prove-or-disprove | the budget is split between a standing breaker/adversary lineage and provers on infinite special families; never all on one side |

How the four problems map onto these types:
- **A, Angles between lines:** proofs of stated inequalities; the last cell is open prove-or-disprove.
- **H, Uphill paths on the hypercube:** C1–C4 are exact values with an instant check; C5 is a scored construction or a lower bound; C6 is an exact value plus optimality.
- **B, Bulgarian solitaire:** C1 proves the cycle structure; C2–C5 are exact extremal values (both bounds); C6 is open.
- **D, Disjoint congruence classes:** C1–C5 prove the statement over growing ranges, with an exhaustiveness certificate for any computation; C6 is open.

---

## 4. Roles

| Role | Job | Tools |
|---|---|---|
| Prover | Line-by-line proof (blind, branch lens, repair, angle waves) | Read, Write, Edit, Glob, Grep, Bash |
| Searcher | Programs that produce constructions, exhaustive/SAT searches, certificates | same |
| Breaker | Refute targets early; ADVERSARY mode in Phase 2C | same |
| Checker-builder | Exact stdlib-only checker from the statement alone | same |
| Referee | VERIFY / GATE (7-step protocol) and CROSS (branch lens) | Read, Write (`verdict.md`, `cex/` only), Glob, Grep, Bash |
| Literature | SOLVE (Phase 1L) and ANALYST (Phase 3); the only role with web access | Read, Write, Glob, Grep, Bash, WebSearch, WebFetch |
| Triage | Branch relevance for Phase 2A; never solves | Read, Write, Glob |
| Space | Phase 2S: carries the cell into several mathematical spaces, learns from the web which spaces and tools exist and what has and hasn't been used, checks each translation by code, reports what each space's tools can deliver; never solves, never chooses | Read, Write, Edit, Glob, Grep, Bash, WebSearch, WebFetch |
| Scribe | SUBMISSION (hand-in) and REPORT (`final_report.md`) | Read, Write, Edit, Glob, Bash |
| Auditor | Checks every citation in a final report, and re-runs its `RAN` lines | Read, Write, Glob, Grep, Bash |

Every worker is a Claude Code subagent (`.claude/agents/<role>.md`) with `omitClaudeMd: true`, so personal CLAUDE.md rules don't leak in.

---

## 5. Information control and isolation

| Regime | Sees | Used for |
|---|---|---|
| BLIND | statement, cell, Part G, optional branch lens, checker, library code the head picks (§8); triage/adversary also get `stuck.md`/verdicts (never proofs); never space cards | Phase 1, 2A, 2B, 2C |
| FRESH / CONTRARIAN | statement + an assigned angle / a list of forbidden approaches | extra waves |
| EXPLOIT | one lineage's best + its critique or gate report | repair |
| CLEAN-ROOM | only the object under evaluation (+ Parts G/S for referees) | referees, checker-builders |
| LITERATURE | web + earlier results the phase allows (space map: obstacles and checker, never proofs) | 1L, 2S, 3 |
| RECORD | accepted artefacts or the full cell record | scribe, auditor |

How it's enforced:
- Each worker gets a task folder `run/tasks/<id>/` holding `brief.md`, `inbox/` (copies the head places there) and `out/`. `pp.py task --phase` builds the inbox. It enforces the regime: Part S goes only to referees, and blind inboxes accept only obstacle files and library code, never proofs.
- `scripts/guard.py`, a PreToolUse hook in every agent, binds a worker to its own task folder. It blocks reads of other tasks, the ledger and `.claude/`, and blocks writes outside `out/`. For Bash commands it can only pattern-match, so enforcement there is best effort. Every denial is appended to `run/guard.log` (task, agent type, tool, target, reason): the head cannot read worker transcripts, so this is its only isolation audit trail. `pp.py blindcheck` flags literature markers in blind outputs, and any breach is reported to the humans at once.
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

Where Phase 2B ran, the proof must also be **ROBUST** itself (not just some other proof in the cell): confirmed by at least 3 other branches, or all of them when fewer than 4 are selected, with no GAP or REFUTED. The head checks the statement word for word, and `pp.py gate` computes VALID / GAP / INVALID from the verdict files.

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
| Robustness | `ROBUST`, `CONTESTED`, `UNSUPPORTED`, `INCOMPLETE` (verdicts still pending), or `–` where 2B didn't run |

A result is never called "new". The wording is always "not found in <sources searched>".

---

## 7. Learning during the run

- **Two layers per role.** Each role has a **locked core** (`.claude/agents/<role>.md`, edited by humans only) and a **lessons layer** (`.claude/lessons/<role>.md`, which the head may edit between phases).
- **Lessons travel in the inbox.** They reach every new task immediately, with no restart needed.
- **Problem lessons** go to `run/<P>/lessons.md`.
- **Evidence and rollback.** Every lesson cites the task ids that justify it. It is reverted if the next wave doesn't improve, logged in `CHANGELOG.md`, and committed.
- **No lesson may weaken verification.** That covers the gate, the checklist, exactness, isolation or blindness, status labels, and `RAN` records.
- **Gate-role lessons need approval.** Lessons for Referee, Checker-builder and Auditor wait in `pending/` until the humans approve them.

§8 adds measurement (telemetry) and a shared technique library, and lists the proposals that were deferred.

---

## 8. Self-improvement layer

§7 lets lessons change between phases. This layer adds two things: every task is measured, and verified tools are shared across cells and problems. Of the seven proposals, **two are built (I1, I5)**. The other five are deferred, because they pay off only over many runs or need more subagent calls than a 7-hour event has. The limits in §6–7 still apply: nothing here may weaken the gate, isolation or blindness.

```
 pp.py task / done / gate / pin ──► run/telemetry.jsonl ──► pp.py telemetry ──► §7 lesson rollback, checkpoint status
 accepted/ + checker/ ──► pp.py lib add ──► run/library/ ◄── pp.py lib import (other problem branches)
                                                 └──► pp.py task --lib ──► worker inbox/library/
```

### Built

**I1. Telemetry.** `run/telemetry.jsonl` holds one JSON event per line and is append-only.
- `pp.py task` records the task: phase, role, regime, mode, branch, angle, subject, role and problem lesson versions, library entries and time box.
- `pp.py done TASK --tokens N --ms N [--score S]` records a returned worker. The head runs it with the numbers from the subagent result. It also records the `out/` files and the verdict (referee, cross-verifier, auditor or adversary label).
- `pp.py gate` and `pp.py pin` record their decisions, so every task knows whether it **fed a gated claim**. A task fed one if it was the subject or an accepting referee of a VALID gate, or the source of a pinned artefact.
- `pp.py telemetry --by <role regime angle lessons lib cell phase branch>` prints, per group: tasks, returned, proofs, fed, verdicts, tokens and mean minutes. `--tasks` prints one row per task.
- **What it's for:** the §7 rollback rule (`--by lessons` compares lesson versions), and tokens and yield by role and regime at each checkpoint. With a handful of tasks per group, the numbers are a hint, not a verdict.

**I5. Technique library.** Each entry lives in `run/library/<P>-<name>/` and holds `ENTRY.md` (kind, what, from, evidence), `MANIFEST.sha256` and `files/`.
- **Verified material only.** Sources must come from `accepted/` (gated or pinned) or `checker/` (cross-tested). There are two kinds: `code`, and `lemma` (from `accepted/` only).
- **Add:** `pp.py lib add NAME SRC… --kind code|lemma --what … --evidence …`.
- **Share across problems:** `pp.py lib list --branches …` shows the entries here and on other problem branches. `pp.py lib import BRANCH ENTRY` copies one over and checks its sha256. As with `pp.py summary`, the branches must have been pushed and fetched, which is a human step.
- **Use:** `pp.py task … --lib ENTRY` copies an entry into `inbox/library/`.
  - Only Provers, Searchers and Breakers get it; clean-room roles never do.
  - BLIND inboxes take only `code` entries with no literature markers, so a blind solver never sees a proof or literature.
  - The brief tells the worker to copy any library file its code needs into `out/code/` and to name the entry in `claims.md`.
- **Lessons across problems:** `pp.py lessons --branches …` lists every problem's lessons across branches. A lesson that appears for two or more problems is a candidate role lesson.

### Deferred

| # | Idea | Why not now |
|---|---|---|
| I2 | EVOLVE searcher regime (AlphaEvolve / FunSearch style): a scored program pool per cell; an EVOLVE searcher changes the top-k programs | Evolution pays off after many generations. A 7-hour call budget can't get there, and building it takes time away from solving. |
| I3 | Regression set for gate lessons: past proofs with seeded flaws that a pending Referee lesson must catch | Needs a set of past proofs that doesn't exist yet, and costs referee calls. |
| I4 | Adaptive angle × regime allocation (Thompson sampling on telemetry rewards) | A bandit needs many trials per option. A cell gets a handful of workers, so a sensible fixed mix does as well. |
| I6 | Head retrospective (`pending/head.md` at checkpoints) | Pays off between runs, not within one. The checkpoint status already covers what matters on the day. |
| I7 | Lean 4 for small lemmas | Setup (Mathlib, toolchain, workers that can write Lean) takes days, not hours. |

If this system runs again, start with I4 and I6: the telemetry log from this run is the data they need.

---

## 9. Repository layout

| Path | What it is | Who edits it |
|---|---|---|
| `.claude/skills/proof-pursuit-head/SKILL.md` | Head instructions: rules, roles, regimes, phases, tiering, gate, budget, learning | humans |
| `.claude/skills/proof-pursuit-head/references/briefs-and-ledger.md` | Brief blocks per role/mode, report and verdict formats, checklist, matrix, gate report, final report, audit, board | humans (`pp.py` parses it) |
| `.claude/skills/problem-<slug>/SKILL.md` | One per problem: verbatim statement, cells, hand-in, typing, ladders, checker spec, angle bank, pitfalls, Part S seeds, branch notes | humans; frozen during a run |
| `.claude/skills/problem-template/SKILL.md` | Template for new problem skills | humans |
| `.claude/agents/<role>.md` | Worker locked cores | humans only |
| `.claude/lessons/` | Lessons layer, `pending/`, `CHANGELOG.md` | head, between phases |
| `scripts/pp.py` | Ledger helper: tasks and inboxes, board, dead ends, pinning, cross-tests, matrix, gate, status, blind check, reports, finalize, summary, telemetry, technique library, cross-branch lessons | humans |
| `scripts/guard.py` | Isolation hook for workers | humans |
| `scripts/tests/` | Scratch-copy tests: `test_pp.py` (phases, inbox rules, matrix, gate, reports, telemetry, library) and `test_guard.py` (isolation cases); run with `python3 scripts/tests/<file>` | humans |
| `scripts/envcheck.py`, `requirements.txt` | Environment check (`.venv`: sympy, mpmath, networkx, python-flint, python-sat) | humans |
| `sources/` | Verbatim problem texts | humans |
| `run/` | The ledger for one problem per branch (layout in the head skill) | head |
| `BUILD_PLAN.md` | Temporary: what's still to be built | build session |
| `dryrun/` | Dry-run findings and archived dry-run ledgers | build session |

---

## 10. Output the humans get

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
- **2026-09-26, merged phase pipeline:**
  - Phases 0–5 from the team's pipeline spec merged into the existing design: checklist Part G/S, blind solvers, literature solver, branch triage, perspective solvers with an agreement matrix, adversary, literature analyst, final report with audit.
  - One head per problem branch.
  - `SEARCH-FOUND-NOTHING` and the extra cell statuses.
  - A two-referee gate with a 7-step protocol.
- **2026-09-26, pipeline build:** skills for Bulgarian solitaire (official text) and Disjoint congruence classes; `pp.py` phase machinery (`task --phase`, inbox rules, `matrix`, `gate`, `status`, `blindcheck`, `finalize`, `summary`); referee `out/cex/` in the guard; agents updated, `literature`, `triage` and `auditor` added, `scout` removed.
- **2026-09-26, cross-verification fixes:** the gate needs the gated proof itself to be ROBUST, not just the cell; `INCOMPLETE` while verdicts are pending (UNSUPPORTED only once every verdict is in); branches re-admitted in 2B-D count in the matrix; `pp.py task` refuses a cross-verifier on a proof whose Phase 2 verdict is negative, or a second one from the same branch; triage core additions.
- **2026-09-26, self-improvement layer documented (proposed; not approved):** ideas I1–I7 copied from `BUILD_PLAN.md` into §8, so they survive when the plan is deleted.
- **2026-09-26, B8 dry run (A-C1 and H-C1) and the fixes it forced:**
  - `run/guard.log`: every isolation denial is now recorded, because the head cannot read worker transcripts;
  - `pp.py status` lists tasks with no `done` event, so lost telemetry is visible;
  - an AUDIT task gets the Scribe's own record snapshot, not a later one that contradicts the report;
  - `task --subject-file` and `--checker` for referees, so a referee judging a computational claim gets the artefact and can re-score it;
  - the Auditor gets Bash and re-runs the report's `RAN` lines, confined to `out/` by the guard (human-approved change to a locked core);
  - scribe and searcher lessons v1;
  - full write-up in `dryrun/2026-09-26-findings.md`.
- **2026-09-26, self-improvement layer, I1 + I5 built:**
  - telemetry: `run/telemetry.jsonl`, `pp.py done`, `pp.py telemetry`; `task`, `gate` and `pin` record events;
  - technique library: `pp.py lib add | list | import`, `task --lib`, `pp.py lessons`;
  - I2, I3, I4, I6 and I7 deferred, with reasons in §8.
- **2026-09-26, Phase 2S space map (proposed):**
  - a `space` agent maps a hard cell into 4–8 spaces and reports cards with fidelity, a checked translation, tightness, tools, cost and payoff;
  - the head evaluates each card and decides with `pp.py choose`, which writes `branches.txt`, which the matrix reads in place of the triage;
  - only a card's LENS reaches workers;
  - tests in `test_pp.py`.
- **2026-09-26, space agent gets web access:** the map runs under LITERATURE, adds KNOWN / UNEXPLORED fields and the LIMIT / ANALOGY fidelities, and replaces the blind LENS with an ANGLE for FRESH workers only; a 2B choice passes the branch and its generic lens, never card text.
- **2026-09-26, README: the whole pipeline:**
  - §1's diagram now runs from the humans' set-up to their hand-in, with 2S beside Phase 1 and the gate, repair and lineage loops;
  - §3 now covers set-up and tiering, a worker's life from `pp.py task` to `pp.py done`, one cell command by command, choosing spaces, the gate and repair loop, lineages and waves, and problem types.
