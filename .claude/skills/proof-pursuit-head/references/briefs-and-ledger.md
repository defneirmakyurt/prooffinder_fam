# Briefs, reports and ledger templates

Contents:
1. Common brief header
2. Role-specific brief sections (with mode blocks)
3. Worker return report and worker output files
4. Referee verdict (VERIFY / GATE) and cross-verifier verdict (CROSS)
5. Dead-end entry
6. Board template
7. Angle generator and branch lenses
8. Lessons files
9. Cell checklist (Part G / Part S)
10. Phases index
11. Branch triage output
12. Agreement matrix
13. Gate report
14. Final report (Phase 5)
15. Audit report
16. Status table (after every phase)

`scripts/pp.py` parses this file. Keep the shapes it relies on:
- role blocks look like `**Role**` or `**Role: MODE**` followed by a fenced block;
- regime additions are lines of the form ``- REGIME: `text` ``.

## 1. Common brief header

Every brief starts with this block. `scripts/pp.py task` writes it for you.

```
TASK: <P>-<cell>-<nnn>      ROLE: <role>      REGIME: <BLIND | FRESH | CONTRARIAN | EXPLOIT | CLEAN-ROOM | LITERATURE | RECORD>
PHASE: <0 | 1 | 1L | 2 | 2A | 2B | 2B-XV | 2C | 3 | GATE | REPAIR | WAVE | 5 | AUDIT>   MODE: <mode or ->   BRANCH: <branch or ->
SUBJECT: <task id of the proof under review, or ->
TIME BOX: <minutes>
READ ONLY: run/tasks/<task-id>/ (this brief + inbox/). Do not open anything else under run/.
WRITE ONLY: run/tasks/<task-id>/out/
TARGET: <exact statement to prove / construct / check / refute, copied from target.md>
STATEMENT RULE: Work from the exact statement in TARGET. Preserve every definition, quantifier,
        parameter range and hand-in requirement. Never infer the question from a cell's title.
ASSUMPTIONS: <gated claims the worker may use, statements in inbox/; default "none beyond the statement">
STOPPING CONDITION: <when to stop>
LESSONS: <role-lessons.md v<n>[, problem-lessons.md v<m>] | none>
RULES: <hackathon rules + cell rules + non-structural pitfalls>
RETURN: only the report block from your agent instructions, at most 200 words plus LADDER / RAN
        (/ CHECKLIST) lines. Full work goes in out/.
INBOX: <files placed in inbox/>
PYTHON: <abs path>/.venv/bin/python3 (sympy, mpmath, networkx, python-flint, python-sat); plain python3 lacks them.
        Checkers and anything a judge reruns stay stdlib-only unless the brief says otherwise.
```

Inbox contents set by phase (`pp.py` enforces them):

| Inbox item | Who gets it |
|---|---|
| `role-lessons.md` | everyone |
| `statement.md` (verbatim problem text), `target.md` (the cell's target) | everyone |
| `problem-lessons.md` | everyone except Referee, Checker-builder, Auditor |
| `checklist-G.md` | everyone except Checker-builder |
| `checklist-S.md` | Referee only (VERIFY, GATE, CROSS) |
| `subject/` (`proof.md`, `claims.md`, `code/` of SUBJECT only) | Referee; REPAIR (plus the gate report) |
| `obstacles/` (`stuck.md`, `verdict.md`, `no_natural_route.md` of named tasks, never proofs) | Triage (2A), Breaker ADVERSARY (2C) |
| `checker/` | Searchers, Breakers where relevant |
| earlier results the phase allows | Literature (1L: Phase 1 outputs; 3: everything for the cell) |
| `record/tasks/<id>/…` (paths preserved so citations resolve) | Scribe REPORT, Auditor |
| accepted artefacts + hand-in text | Scribe SUBMISSION |
| `library/<entry>/` (`ENTRY.md`, `MANIFEST.sha256`, `files/`), chosen with `--lib` | Prover, Searcher, Breaker. Under BLIND: `code` entries with no literature markers only. Never clean-room roles, Triage, Literature, Scribe or Auditor |

BLIND inboxes accept nothing else. ASSUMPTIONS lists only claims that have passed the gate, with each exact statement in `inbox/`. A brief with `--lib` ends with a LIBRARY paragraph telling the worker to copy any library file its code needs into `out/code/`, and to name the entry in `claims.md` for every claim that depends on it. That way referees see the code and auditors can trace the entry.

## 2. Role-specific brief sections

Add the matching block after the header (role block, then mode block if any).

**Prover**
```
First write out/plan.md: TARGET as a ladder of numbered rungs (lemmas, special cases, reductions)
with dependencies. Work through it in order, marking each rung
PROVED / CHECKED / GAP / REFUTED / NOT STARTED.
Write out/proof.md. First line: the exact statement you prove, no more.
Then numbered steps; each justified by a definition, an earlier step, or a named lemma with exact reference.
"Clearly", "routine", "obviously", "similarly" and "by symmetry" may not replace an argument. Write the step out.
Mark anything you are not sure of [GAP].
Also write out/claims.md (claim | status | where proved), out/stuck.md (exact point of failure, or "none"),
and out/code/README.md (how to run any code) if you wrote code.
Check inbox/checklist-G.md item by item before you finish.
Numerics may guide you; any step resting on computation must include code in out/code/,
exact or interval arithmetic, runtime < 10 min.
If you executed code, fill in RAN exactly: what ran, parameter range, COMPLETED / TIMED OUT / PARTIAL, measured runtime.
```
Regime additions:
- BLIND: `Derive everything from first principles. Standard textbook tools are fine; results specific to this problem or its literature are not: if you recognise a known theorem about this problem, do not use it, work the argument out yourself. Cite no papers or authors.`
- FRESH: `ANGLE: <angle>. Pursue this angle; if you abandon it, say why.`
- CONTRARIAN: `FORBIDDEN APPROACHES (already tried, do not use): <lines from deadends.md + live lineage tags>.`
- EXPLOIT: `Inbox holds the current best proof and its gate report or critique. Repair the listed problems first. If the approach cannot be repaired, say so and why.`

**Prover: BRANCH**
```
BRANCH LENS: <branch> — <lens text from section 7, plus the problem skill's branch note if any>.
Attack TARGET mainly with this branch's tools. You may borrow from other branches briefly; say where.
If the branch gives no natural route, write out/no_natural_route.md with the reason and stop.
Do not force an argument.
```

**Searcher**
```
First write out/plan.md: TARGET as a ladder of numbered rungs (checker sanity, small cases,
reductions, search stages) with dependencies. Work through it in order, marking each rung
PROVED / CHECKED / GAP / REFUTED / NOT STARTED.
Inbox holds checker/ (use it as your scoring function) and, if EXPLOIT, the lineage's best program and artefact.
Write a program that generates candidates; do not hand-craft objects.
Save: out/best.<ext> (artefact in the cell's required format), out/code/ (code + README.md),
out/runlog.md (method, seeds, restarts, measured runtime, best score per run),
out/claims.md (claim | status | where shown), out/stuck.md.
State whether any search was exhaustive and over exactly which class;
give the soundness argument for every symmetry reduction, written out in full.
A search over finitely many parameter values never proves a statement for all parameters.
A search that found nothing is SEARCH-FOUND-NOTHING, not a verification.
Fill in RAN exactly: what ran, parameter range, COMPLETED / TIMED OUT / PARTIAL, measured runtime.
```
Regime additions as for Prover (BLIND, FRESH, CONTRARIAN, EXPLOIT). A BRANCH lens on a Searcher is a search angle.

**Breaker**
```
First write out/plan.md: the attack as a ladder of numbered rungs (sub-claims or families to test)
with dependencies. Work through it in order, marking each rung
PROVED / CHECKED (tested, no violation) / GAP / REFUTED / NOT STARTED.
Try to refute TARGET: structured candidates first (symmetric, perturbations of the conjectured optimum,
repetitions, equal values, smallest cases), then randomised and optimisation-based search with many restarts.
Save the worst case with exact values in out/worst.<ext> and a script that reproduces it.
If nothing breaks it, list exactly what you tested (families, sizes, instance counts, seeds).
"Survived" is evidence, not proof. A small positive gap is not a counterexample.
Fill in RAN exactly: what ran, parameter range, COMPLETED / TIMED OUT / PARTIAL, measured runtime.
```

**Breaker: ADVERSARY**
```
Phase 2C. Inbox/obstacles/ holds stuck.md / verdict.md files of failed attempts (never their proofs).
Four separate tasks, each with its own output file:
1. out/contrapositive.md — write the claim as P => Q; try to prove not-Q => not-P directly
   (assume the bound fails and derive forced structure). A complete argument here is a proof: write it
   also as out/proof.md + out/claims.md so it can be verified.
2. out/cex_search/ — counterexample search assuming the claim is false (code, seeds, logs, near misses with gaps).
   Confirm any violation in exact or interval arithmetic.
3. out/local_analysis.md — is the conjectured optimum a strict local optimum (second-order perturbation)?
   A perturbation that beats it is a disproof; otherwise this is evidence only.
4. out/minimal_failing.md — the smallest sub-case where the known arguments fail, as a precise sub-lemma.
out/verdict.md: PROOF-ROUTE-FOUND | COUNTEREXAMPLE-CANDIDATE | LOCALLY-OPTIMAL-EVIDENCE | STUCK.
```

**Checker-builder**
```
From the statement alone, write out/verify.py: Python standard library only (fractions allowed),
exact arithmetic, reads the artefact format given in TARGET, prints VERIFIED + score,
or the exact reason for failure. Keep it short enough to read line by line.
Also write out/tests.py: hand-computed small cases plus a brute-force cross-check where feasible.
Fill in RAN exactly: what ran, parameter range, COMPLETED / TIMED OUT / PARTIAL, measured runtime.
```

**Referee**
```
Inbox holds TARGET, inbox/subject/ (proof.md, claims.md, code/), inbox/checklist-G.md and inbox/checklist-S.md.
You do not know who wrote the proof or how confident anyone is. Assume it may be wrong.
Run the 7-step protocol and write out/verdict.md:
1. Checklist pass: every item of Part G and Part S, PASS / FAIL / N/A with one line each.
   A FAIL on tightness, cases covered or statement match blocks ACCEPT.
2. Line-by-line re-derivation; list every unjustified, circular or false step.
   "Clearly / routine / obviously / similarly / by symmetry" are gaps unless written out.
3. Numerical sanity on random and extremal instances; run the code, record runtime; flag floating point inside a proof.
4. Equality-case test at the extremal configurations in Part S.
5. Cross-cell consistency with the verified cells listed in Part S.
6. Your own counterexample search, code in out/cex/.
7. Verdict ACCEPT / MINOR / MAJOR / WRONG. ACCEPT gives, for each step, the reason it holds.
You may write only out/verdict.md and out/cex/. Return the verdict block in section 4.
```

**Referee: CROSS**
```
Phase 2B cross-verification. BRANCH LENS: <branch> — <lens text>.
Re-check inbox/subject/ from this branch's viewpoint. Try to TRANSLATE the key idea into your branch;
a key step that cannot be translated, or contradicts the translation, is a red flag — name it.
Hunt for counterexamples with your branch's tools (code in out/cex/).
Verdict: CONFIRMED | CONFIRMED-WITH-CAVEATS | GAP | REFUTED, in the CROSS block of section 4.
```

**Literature**
```
You have web search and fetch. Tag every result PROVED / COMPUTER-VERIFIED / CONJECTURED, and say whether the
source contains the argument or only cites it. Flag computations whose code is unavailable and steps called
"routine" but not written down. Every claim carries a source link or a pointer to an artefact, plus a status tag.
Never present a citation as a proof of the cell itself. Never call anything new: write "not found in <sources searched>".
Your output never reaches blind agents.
```

**Literature: SOLVE**
```
Phase 1L. Inbox/earlier/ holds the Phase 1 blind results for this cell.
1. Find the literature for this cell and its neighbours, with links (out/sources.md: link, what was used, status).
2. Attempt the cell using known techniques (out/proof.md, out/claims.md).
3. Compare with the blind solvers: where do approaches differ or contradict? (out/divergence.md).
   Record which ideas came from the blind run, which from literature, and which are new here.
Blind and literature results are compared, never merged.
```

**Literature: ANALYST**
```
Phase 3. Inbox/earlier/ holds everything for this cell (proofs, verdicts, matrix, no_natural_route, adversary).
1. Map what is known: PROVED vs COMPUTER-VERIFIED vs CONJECTURED, with links; flag inaccessible results.
2. Reduce the cell to critical sub-problems: (a) known and citable, (b) known but hard to access, so reproduce it,
   (c) unknown (out/subproblems.md).
3. Attempt (b) and (c), crediting earlier work (out/proof.md, out/claims.md).
4. If the cell cannot be solved: out/why_not.md — where the obstruction is, which approaches fail and why
   (with counterexamples if any), why each failing branch fails, and what the next person needs to start.
```

**Triage**
```
Phase 2A. Do not solve the cell. Inbox/obstacles/ holds stuck.md and verdict.md files (not proofs).
For each branch ALGEBRAIC, TOPOLOGICAL, ANALYSIS, NUMBER-THEORY, DISCRETE write in out/triage.md:
RELEVANCE (HIGH / MEDIUM / LOW / NONE), REASON (a paragraph tied to the cell's actual structure),
ENTRY POINT (a concrete first step; none nameable => at most LOW), RISK (likely failure + early warning sign).
Rate relevance to the problem's structure, not to a guessed answer.
Selection: HIGH and MEDIUM run as solvers; NONE is dropped; keep the best LOW only to reach two solver branches;
a dropped branch may be tagged verifier-only. Log every elimination with its reason.
Write out/selected_branches.txt (section 11).
```

**Scribe**
```
Reports introduce no new mathematics. Never upgrade a status given in the brief.
Fill in RAN exactly for every command you ran.
```

**Scribe: SUBMISSION**
```
Inbox holds accepted artefacts and the cell's "what to hand in" text.
Produce out/submission.md in exactly that format: statement, cell status, claim status, cited vs. new,
proof or certificate, how to verify (command, expected output, measured runtime), limitations.
PARTIAL lists the claims established and the exact remaining gap. Add no claim that is not in the accepted artefacts.
```

**Scribe: REPORT**
```
Phase 5. Inbox/record/ holds the cell's full record, paths preserved (record/tasks/<id>/out/...).
Write out/final_report.md in the section 14 format. Every statement cites its artefact by relative path and
step number (e.g. "tasks/A-C1-003/out/proof.md, step 4"); a claim with no artefact is deleted.
State in Limitations: "agent agreement is evidence, not proof".
```

**Auditor**
```
Phase 5 audit. Inbox holds final_report.md and inbox/record/ (the artefacts it cites).
For every citation: does the file exist, and does the cited step say what the report claims?
List every unsupported or mis-cited statement. Write out/audit.md (section 15). Verdict PASS only if none remain.
```

## 3. Worker return report and worker output files

```
TASK: <id>   ROLE: <role>   REGIME: <regime>   PHASE: <phase>
OUTCOME: CLAIM | PARTIAL | NO-PROGRESS | REFUTED | NO-NATURAL-ROUTE
CLAIM: <one precise sentence, or "none">
LADDER: <Prover/Searcher/Breaker only; one line per rung, ≤10 lines, ≤15 words each>
  R1 <PROVED | CHECKED | GAP | REFUTED | NOT STARTED> — <sub-claim>
RAN: <required if any code executed: what ran, exact parameter range,
      COMPLETED / TIMED OUT / PARTIAL, measured runtime; one line per run; "none" only if nothing executed>
ARTEFACTS: <paths in out/>
IDEA-TAG: <2–4 words naming the approach>
KNOWN GAPS: <numbered list, or "none found">
DEAD ENDS: <approach — why it fails; one line each>
SCORE: <searchers: value from the provided checker; others: n/a>
```

Triage, Literature, Scribe and Auditor use the same block with IDEA-TAG set to their phase and LADDER omitted.

The head uses IDEA-TAG to spot convergence and to name lineages. SCORE is always recomputed before it is trusted. The 200-word limit excludes LADDER and RAN lines; the full ladder stays in `out/plan.md`. LADDER statuses are the worker's claims: a PROVED rung is unrefereed and a CHECKED rung is unrerun until the head says otherwise.

**RAN is a factual record.** A worker never reports a run that did not happen or a runtime it did not measure. A run that was cut off is `TIMED OUT` or `PARTIAL`, with the range actually covered. The head re-runs every computation a claim depends on before trusting it. A RAN line that doesn't reproduce makes the report untrusted: log it, and don't use any of that report's computational claims.

Worker output files (solvers):

| File | Contents |
|---|---|
| `out/plan.md` | the ladder |
| `out/proof.md` | first line = exact statement proved; numbered steps |
| `out/claims.md` | table: claim \| status \| where proved (file, step) |
| `out/code/` + `README.md` | runnable code and how to run it |
| `out/stuck.md` | the exact point of failure, or "none" |
| `out/no_natural_route.md` | 2B only, when the branch gives no route |

## 4. Referee verdict (VERIFY / GATE) and cross-verifier verdict (CROSS)

```
VERDICT: ACCEPT | MINOR | MAJOR | WRONG
STATEMENT MATCH: yes | no — <difference>
FIRST PROBLEM: step <k> — <what is unjustified; the fix, if known>   (or "none")
CHECKLIST: <one line per Part G and Part S item: G1 PASS — reason | S3 FAIL — step k | ...>
EQUALITY CASES: <tested configurations and result>
CROSS-CELL: <consistency with verified cells, or N/A>
CEX SEARCH: <what was searched, out/cex/ path, result>
OTHER ISSUES: <list>
RAN: <what ran, parameter range, COMPLETED / TIMED OUT / PARTIAL, measured runtime; or "none">
```

`out/verdict.md` holds the full reasoning. For ACCEPT, it states for each numbered step of the proof why that step holds. An ACCEPT with any FAIL item, a missing item, or no per-step reasons is incomplete and doesn't count.

```
CROSS VERDICT: CONFIRMED | CONFIRMED-WITH-CAVEATS | GAP | REFUTED
BRANCH: <branch>
TRANSLATION: <the key idea in this branch's terms, or "does not translate: <why>">
RED FLAGS: <steps that resist translation or contradict it, or "none">
CEX SEARCH: <what was searched, out/cex/ path, result>
RAN: <...>
```

## 5. Dead-end entry

```
- [<idea-tag>] <approach> — <why it fails / where it stalls> (<task id>)
```

Keep each entry to one line. CONTRARIAN briefs receive these lines verbatim.

## 6. Board template (one problem per branch)

```
# Board: problem <P>, updated <time>, run time <h:mm> of 7:00

| Cell | Pts | Tier | Phase | Cell status | Claim status | Robustness | Best so far | Live lineages | Next | Time used |
|------|-----|------|-------|-------------|--------------|------------|-------------|---------------|------|-----------|
| A-C1 | 2 | T1: <reason> | 2 | PARTIAL | ... | – | ... | ... | ... | 0:00 |

## Partial cells: established / remaining gap
- <cell>: ESTABLISHED: <claim — status; ...>  GAP: <exact statement still missing>

## Awaiting gate
## Contested cells (tell the humans)
## Lessons (changes since last checkpoint; pending Referee/Checker-builder/Auditor lessons)
## Decisions for the team
## Obstacle notes (parked cells)
- <cell>: TRIED: <idea tags> STALLS AT: <exact step or lemma> NEEDS: <what would unlock it> KNOWN: <literature status, or "not found in <sources>">
```

- **Cell status:** `SOLVED`, `PARTIAL`, `COUNTEREXAMPLE`, `NOT SOLVED` or `NOT ATTEMPTED`.
  - `SOLVED` only when every claim the hand-in requires has passed the gate at an established status: `PROVED`, `COMPUTER-VERIFIED`, or `EXHAUSTIVE-WITHIN-CLASS` where the class is the whole space the statement quantifies over.
  - Everything short of that is `PARTIAL`, including a `BEST-FOUND` value in an instant-check cell. Every `PARTIAL` cell has an entry under "Partial cells".
- **Claim status:** the strongest claim for the cell.
- **Robustness:** `ROBUST` / `CONTESTED` / `UNSUPPORTED` / `INCOMPLETE`, or `–` where 2B didn't run.

## 7. Angle generator and branch lenses

**Branch lenses (Phase 2A/2B).** These are generic. Problem-specific branch notes live in the problem skill and go only into the matching lens.
- **ALGEBRAIC:** matrices, rank, eigenvalues, trace and norm inequalities, determinants, positive semidefinite cones, polynomial identities, symmetry groups and invariants.
- **TOPOLOGICAL:** configuration spaces, compactness, continuity and degree arguments, critical point structure, connectedness of the extremiser set.
- **ANALYSIS:** convexity, Jensen, tangent-line bounds, Lagrange multipliers, second-order conditions, behaviour near degenerate configurations, smoothing and variational arguments, potential functions.
- **NUMBER-THEORY:** divisibility and rounding of counts, parity, integrality constraints, congruences.
- **DISCRETE:** graph, hypergraph and poset formulations, induction, double counting, extremal (Turán-type) arguments, pigeonhole, majorisation, bijections.

For searches, **COMPUTATIONAL** is an extra lens: exhaustive search, SAT/ILP, constructions, local search.

**Angles for FRESH/CONTRARIAN waves.** Change at least one axis relative to every live lineage:
- **Branch lens:** as above.
- **Representation:** vectors vs. Gram matrix vs. projections; graph vs. poset vs. matrix; labelling vs. ordering vs. orientation.
- **Method family:** induction or reduction; extremal (perturb at an optimum); averaging or probabilistic; convexity or majorisation; LP/SDP duality; explicit construction; exhaustive or SAT search; local search or annealing; recursive product construction.
- **Structural assumption:** symmetric or equivariant objects; small support; near the conjectured optimum; far from it.
- **Scale:** solve many small cases exactly, find the pattern, then generalise.
- **Direction:** start from the obstruction (why the naive argument fails) rather than from the target.

Write the chosen angle in the brief as `<branch>: <angle>`, or just `<angle>`. If the worker opens a lineage, the angle becomes that lineage's idea tag.

## 8. Lessons files

```
version: <n>
# Lessons: <role>
<!-- Head-editable lessons layer. Refines the locked core in .claude/agents/<role>.md, never overrides it. ≤ ~30 lines. -->

- <lesson> (evidence: <task ids>; added <hh:mm>; version <n>)
```

- `version:` must be the first line. `pp.py` reads it into the brief's LESSONS line.
- Problem lessons (`run/<P>/lessons.md`) use the same format with `# Lessons: problem <P>`.
- Pending Referee/Checker-builder/Auditor lessons wait in `.claude/lessons/pending/<role>.md` in the same format, which is never copied into an inbox.

CHANGELOG entry (`.claude/lessons/CHANGELOG.md`):

```
## <hh:mm> <role or problem P> v<old> → v<new>
- Change: <added / sharpened / merged / reverted: text>
- Evidence: <task ids>
- Result after next wave: <pending | improved: ... | no change → reverted | worse → reverted: why>
```

## 9. Cell checklist (`run/<P>/<cell>/checklist.md`)

Written by the head in Phase 0, **without solving the cell**. `pp.py` splits it into `checklist-G.md` (everyone) and `checklist-S.md` (referees only).

```
# Checklist: <P>-<cell>

## Part G (generic; shared with every agent, blind ones included)
- G1 The statement proved is exactly the cell's: no extra hypotheses, no weaker inequality, the full parameter range.
- G2 Every step justified. No unexplained "clearly", "similarly", "routine", "obviously", "by symmetry".
- G3 Base cases, edge and degenerate cases, exceptional parameter values handled.
- G4 Every claimed invariant is preserved; every claimed decrease is strict where strictness is needed.
- G5 Every construction works for every claimed parameter value, not only the tested ones.
- G6 No circularity, and no citation that is the statement itself.
- G7 Any computation is exact or interval-based, code included, under 10 minutes; a finite check proves
     nothing beyond its range; a computer-assisted step has a written reduction to exactly the set searched.
- G8 Cited results separated from new work, with precise references.
- G9 The proof says what is established and what is not.

## Part S (specific; referees and the gate only, NEVER shown to blind agents)
- S1 Exact statement and the quantities to be bounded: <from target.md>
- S2 Equality / extremal configurations where any valid proof must be tight: <from the statement or gated cells; else "unknown">
- S3 Cases the proof must cover: <parities, whole parameter ranges, degenerate inputs>
- S4 Known traps: <problem-skill pitfalls; failure modes seen in lower cells; each labelled source>
- S5 Consistency with other cells: <verified cells this must agree with, exact statements>
- S6 Small explicit instances with known optimum, and numerical checks any proof must pass: <from statement or gated results only>
```

## 10. Phases index (`run/<P>/<cell>/phases.md`, appended by `pp.py task`)

```
| Task | Phase | Role | Regime | Mode | Branch | Subject | Created |
|------|-------|------|--------|------|--------|---------|---------|
```

## 11. Branch triage output (`out/selected_branches.txt`)

```
ALGEBRAIC	solver
DISCRETE	solver
ANALYSIS	verifier-only
```

One line per kept branch, tab-separated: branch, then `solver` or `verifier-only`. Dropped branches are absent; their reasons are in `triage.md`.

## 12. Agreement matrix (`run/<P>/<cell>/matrix.md`, written by `pp.py matrix`)

Rows are proofs (task ids), and columns are the Phase 2 verifier and each cross-verifying branch. Cells hold verdicts.

Classification:
- **ROBUST:** some proof passed the Phase 2 verifier (ACCEPT) and is CONFIRMED (or CONFIRMED-WITH-CAVEATS) by at least three other branches. With fewer than four selected branches, it must be confirmed by every other selected branch. No GAP or REFUTED on that proof.
- **CONTESTED:** verdicts disagree. List the disputed steps for the humans.
- **UNSUPPORTED:** every verdict is in, nothing is contested, and no proof has the confirmations ROBUST needs.
- **INCOMPLETE** (transient): no disagreement so far, and some proof with no negative verdict still has verdicts pending (its Phase 2 verifier or a kept branch), so it could still become ROBUST. It is not ROBUST, so the gate treats it as a GAP.

Kept branches are those in the latest triage's `selected_branches.txt`, plus any branch re-admitted in 2B-D (from its first 2B task). The gate needs the proof under the gate to be ROBUST itself; a ROBUST cell reached through another proof doesn't count.

## 13. Gate report (`run/<P>/<cell>/gate/gate_report.md`, written by `pp.py gate`)

```
# Gate: <P>-<cell>, proof <task id>, <time>
Referees: <task id> VERIFY ACCEPT (checklist complete: yes) | <task id> GATE ACCEPT (complete: yes)
Matrix: ROBUST | CONTESTED | UNSUPPORTED | INCOMPLETE | not run; this proof: robust | not robust | not in matrix | n/a
Statement checked word for word by head: yes | no
Checklist scores: <G/S items with PASS/FAIL/N/A per referee>
DECISION: VALID | GAP | INVALID — <rule that decided it>
Next: <PROVED on board | repair + Phase 2C with this report | tell the humans>
```

## 14. Final report (`final_report.md`, Scribe REPORT mode)

1. **OUTCOME:** PROVED / PARTIAL / COUNTEREXAMPLE / NOT SOLVED, with status tags.
2. **STATEMENT:** the exact statement, and the checklist hash (sha256 of `checklist.md`).
3. **RESULT:** one of:
   - the final proof, or a pointer to it;
   - the explicit counterexample, with its exact verification and reproduction command;
   - the best partial result and the smallest open lemma.
4. **HOW IT WAS REACHED:** a timeline over Phases 0–3 and the gate, with citations:
   - agents run, approaches taken, outcomes, stuck points;
   - triage decisions (branches kept, dropped, re-admitted);
   - literature vs. blind divergence;
   - the agreement matrix;
   - adversary searches (seeds, trials, near misses);
   - dead ends, and why they failed.
5. **LITERATURE VS OURS:** two separate lists.
   - Existing results: full references, links and status, noting whether the source contains the argument or only cites it.
   - Our contribution: artefact and status.
6. **REPRODUCIBILITY:** commands, runtimes, software versions, any floating point use with its error bound, and confirmation of the 10-minute limit.
7. **LIMITATIONS:** what was not established, unresolved disagreements, what the humans must still check. Always include: "agent agreement is evidence, not proof".
8. **NEXT STEPS.**

Every statement cites an artefact as `tasks/<id>/out/<file>, step <k>`.

## 15. Audit report (`out/audit.md`)

```
AUDIT: PASS | FAIL
CITATIONS CHECKED: <n>
UNSUPPORTED: <statement — why (missing file / step says otherwise / no citation)>, one per line, or "none"
```

## 16. Status table (printed by the head after every phase; `pp.py status`)

```
| Cell | Agents run (by phase) | Verdicts | Robustness | Next |
```
