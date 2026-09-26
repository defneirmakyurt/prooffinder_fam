# Briefs, reports and ledger templates

Contents:
1. Common brief header
2. Role-specific brief sections
3. Worker return report
4. Referee verdict
5. Dead-end entry
6. Board template
7. Angle generator
8. Lessons files

## 1. Common brief header

Every brief starts with this block, filled in. `scripts/pp.py task` writes it for you.

```
TASK: <P>-<cell>-<nnn>      ROLE: <role>      REGIME: <EXPLOIT | FRESH | CONTRARIAN | CLEAN-ROOM>
TIME BOX: <minutes>
READ ONLY: tasks/<task-id>/ (this brief + inbox/). Do not open anything else under run/.
WRITE ONLY: tasks/<task-id>/out/
TARGET: <exact statement to prove / construct / check / refute, copied from target.md>
STATEMENT RULE: Work from the exact statement in TARGET. Preserve every definition, quantifier,
        parameter range and hand-in requirement. Never infer the question from a cell's title.
ASSUMPTIONS: <what the worker may take as given, e.g. "Lemma A-C1-L2 (accepted, statement in inbox/)";
        default "none beyond the statement">
STOPPING CONDITION: <when to stop, e.g. "stop and report as soon as you find a counterexample",
        "stop if the same rung fails twice", "stop when the checker score reaches X">
LESSONS: <role-lessons.md v<n>[, problem-lessons.md v<m>] | none>
RULES: <cell rules binding this worker, e.g. "citing a published proof of the target does not count";
        "any computation must be exact or interval arithmetic, code included, runtime < 10 min">
RETURN: only the report block from section 3, at most 200 words plus a LADDER of at most 10 lines.
        Full work goes in out/.
```

Inbox contents that every brief gets:
- `inbox/role-lessons.md`: a copy of `.claude/lessons/<role>.md` as it stands at dispatch (section 8).
- `inbox/problem-lessons.md`: a copy of `run/<P>/lessons.md`, when it exists. Referees and Checker-builders don't get it, because they are clean-room.

The version numbers in the LESSONS line are the ones the worker received. They let you attribute a later change in results to a lessons edit.

ASSUMPTIONS lists only claims that have passed the gate, or lemmas explicitly given as hypotheses for a conditional result. Put each one's exact statement in `inbox/`.

## 2. Role-specific brief sections

Add the matching block after the header.

**Scout**
```
Produce out/boundary.md with a table:
Statement/case | Status (PROVED / COMPUTER-VERIFIED (code public?) / CONJECTURED / OPEN / UNSURE)
| Reference (authors, title, year, theorem or table number, arXiv/DOI) | Method notes.
Also list known small-case values and the main techniques in the literature.
If you are not certain a reference exists, write UNSURE. Never merge "checked by computer" into "proved".
For anything you did not find, write "not found in <sources searched>", never "new" or "unknown".
```

**Prover**
```
First write out/plan.md: TARGET as a ladder of numbered rungs (lemmas, special cases, reductions)
with dependencies. Work through it in order, marking each rung
PROVED / CHECKED / GAP / REFUTED / NOT STARTED.
Write out/proof.md. First line: the exact statement you prove, no more.
Then numbered steps; each justified by a definition, an earlier step, or a named lemma with exact reference.
"Clearly", "routine", "obviously" and "similarly" may not replace an argument. Write the step out.
Mark anything you are not sure of [GAP].
Numerics may guide you; any step resting on computation must include code in out/,
exact or interval arithmetic, runtime < 10 min.
If you executed code, fill in RAN exactly: what ran, parameter range, COMPLETED / TIMED OUT / PARTIAL, measured runtime.
```
Regime additions:
- EXPLOIT: `Inbox holds the current best proof and the referee's critique. Repair the listed problems first. If the approach cannot be repaired, say so and why.`
- FRESH: `ANGLE: <angle>. Pursue this angle; if you abandon it, say why.`
- CONTRARIAN: `FORBIDDEN APPROACHES (already tried, do not use): <lines from deadends.md + live lineage tags>.`

For FRESH, write the angle as `<perspective>: <angle>` when a discipline perspective applies (section 7), e.g. `algebraic: Gram matrix, rank ≤ d`.

**Searcher**
```
First write out/plan.md: TARGET as a ladder of numbered rungs (checker sanity, small cases,
reductions, search stages) with dependencies. Work through it in order, marking each rung
PROVED / CHECKED / GAP / REFUTED / NOT STARTED.
Inbox holds checker/ (use it as your scoring function) and, if EXPLOIT, the lineage's best program and artefact.
Write a program that generates candidates; do not hand-craft objects.
Save: out/best.<ext> (artefact in the cell's required format), out/search/ (code),
out/runlog.md (method, seeds, restarts, measured runtime, best score per run).
State whether any search was exhaustive and over exactly which class;
give the soundness argument for every symmetry reduction, written out in full
("clearly", "routine", "obviously" and "similarly" may not replace an argument).
A search over finitely many parameter values never proves a statement for all parameters.
Fill in RAN exactly: what ran, parameter range, COMPLETED / TIMED OUT / PARTIAL, measured runtime.
```
Regime additions as for Prover.

**Breaker**
```
First write out/plan.md: the attack as a ladder of numbered rungs (sub-claims or families to test)
with dependencies. Work through it in order, marking each rung
PROVED / CHECKED (tested, no violation) / GAP / REFUTED / NOT STARTED.
Try to refute TARGET: random instances, optimisation of the violation, structured families.
Save the worst case with exact values in out/worst.<ext> and a script that reproduces it.
If nothing breaks it, list exactly what you tested (families, sizes, instance counts).
"Survived" is evidence, not proof.
Fill in RAN exactly: what ran, parameter range, COMPLETED / TIMED OUT / PARTIAL, measured runtime.
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
Inbox holds a statement and a proof. You do not know who wrote it or how confident anyone is. Assume it may be wrong.
1. Does the proved statement match TARGET exactly (ranges, quantifiers, edge cases)?
2. Read step by step; stop at the first step that is not justified.
3. You may test steps numerically.
4. Answer every item of the mandatory checklist in your instructions explicitly, in out/verdict.md and in CHECKLIST.
5. ACCEPT must give, for each step, the reason it holds. "Looks correct" is not a reason.
Return the verdict block in section 4 instead of the section 3 report.
```

**Scribe**
```
Inbox holds accepted artefacts and the cell's "what to hand in" text.
Produce out/submission.md in exactly that format: statement, cell status, claim status, cited vs. new,
proof or certificate, how to verify (command, expected output, measured runtime), limitations.
Cell status is SOLVED / PARTIAL / NOT ATTEMPTED as given in the brief; PARTIAL lists the claims
established and the exact remaining gap. Add no claim that is not in the accepted artefacts.
Fill in RAN exactly for every command you ran.
```

## 3. Worker return report

```
TASK: <id>   ROLE: <role>   REGIME: <regime>
OUTCOME: CLAIM | PARTIAL | NO-PROGRESS | REFUTED
CLAIM: <one precise sentence, or "none">
LADDER: <Prover/Searcher/Breaker only; one line per rung, ≤10 lines, ≤15 words each>
  R1 <PROVED | CHECKED | GAP | REFUTED | NOT STARTED> — <sub-claim>
  R2 ...
RAN: <required if any code executed: what ran, exact parameter range,
      COMPLETED / TIMED OUT / PARTIAL, measured runtime; one line per run; "none" only if nothing executed>
ARTEFACTS: <paths in out/>
IDEA-TAG: <2–4 words naming the approach>
KNOWN GAPS: <numbered list, or "none found">
DEAD ENDS: <approach — why it fails; one line each>
SCORE: <searchers: value from the provided checker; others: n/a>
```

The head uses IDEA-TAG to spot convergence and to name lineages. SCORE is always recomputed before it is trusted.
The 200-word limit excludes LADDER and RAN lines; the full ladder stays in out/plan.md.
LADDER statuses are the worker's claims: a PROVED rung is unrefereed and a CHECKED rung is unrerun
until the head says otherwise. GAP rungs become EXPLOIT repair targets.

**RAN is a factual record.** A worker never reports a run that did not happen or a runtime it did not measure. A run that was cut off is `TIMED OUT` or `PARTIAL`, with the range actually covered. The head re-runs every computation a claim depends on before trusting it. A RAN line that doesn't reproduce makes the report untrusted: log it, and don't use any of that report's computational claims.

## 4. Referee verdict

```
VERDICT: ACCEPT | MINOR | MAJOR | WRONG
STATEMENT MATCH: yes | no — <difference>
FIRST PROBLEM: step <k> — <what is unjustified; the fix, if known>
CHECKLIST: (each: OK — <one-line reason> | PROBLEM — <step> | N/A — <why>)
  base cases / exceptional parameter values:
  quantifiers and ranges vs. the cell statement:
  invariants preserved:
  decreases strict where needed:
  constructions valid for every claimed parameter:
  no circularity:
  "clearly / routine / similarly" treated as gaps:
OTHER ISSUES: <list>
CHECKS RUN: <numerical tests, small cases>
RAN: <what ran, parameter range, COMPLETED / TIMED OUT / PARTIAL, measured runtime; or "none">
```

`out/verdict.md` holds the full reasoning. For ACCEPT, it states for each numbered step of the proof why that step holds.

## 5. Dead-end entry

```
- [<idea-tag>] <approach> — <why it fails / where it stalls> (<task id>)
```

Keep each entry to one line. CONTRARIAN briefs receive these lines verbatim.

## 6. Board template

```
# Board: updated <time>, run time <h:mm> of 7:00

| Cell | Pts | Tier | Cell status | Claim status | Best so far | Live lineages | Next wave | Time used |
|------|-----|------|-------------|--------------|-------------|---------------|-----------|-----------|
| H-C1 | 1 | T0: <reason> | NOT ATTEMPTED | ... | ... | ... | ... | 0:00 |
| A-C1 | 2 | T1: <reason> | PARTIAL | ... | ... | ... | ... | 0:00 |

## Partial cells: established / remaining gap
- <cell>: ESTABLISHED: <claim — status; ...>  GAP: <exact statement still missing>

## Awaiting gate
## Lessons (changes since last checkpoint; pending Referee/Checker-builder lessons)
## Decisions for the team
## Obstacle notes (parked cells)
```

- **Cell status** is `SOLVED`, `PARTIAL` or `NOT ATTEMPTED`. A cell is `SOLVED` only when every claim its hand-in requires has passed the gate at an established status (`PROVED`, `COMPUTER-VERIFIED`, or `EXHAUSTIVE-WITHIN-CLASS` where the class is the whole space the statement quantifies over). Everything short of that is `PARTIAL`, including a value submitted as `BEST-FOUND` in an instant-check cell. Every `PARTIAL` cell has an entry under "Partial cells".
- **Claim status** is the strongest claim for the cell: `PROVED`, `COMPUTER-VERIFIED`, `EXHAUSTIVE-WITHIN-CLASS`, `BEST-FOUND`, `CONJECTURED` or `OPEN`.

## 7. Angle generator

When a FRESH or CONTRARIAN worker needs an angle, change at least one axis relative to every live lineage:

- **Discipline perspective:** within one wave, give each FRESH worker a different perspective when it fits the problem, and skip any that don't fit. Adversarial work is already covered by the Breaker and the Referee.
  - combinatorial: counting, extremal arguments, bijections;
  - algebraic: symmetries, invariants, representations;
  - geometric/topological: configurations, obstructions;
  - analytic: inequalities, potential functions, monotonicity;
  - computational: exhaustive search, constructions, counterexamples.
- **Representation:** vectors vs. Gram matrix vs. projections; graph vs. poset vs. matrix; labelling vs. ordering vs. orientation.
- **Method family:** induction or reduction; extremal (perturb at an optimum); averaging or probabilistic; convexity or majorisation; LP/SDP duality; explicit construction; exhaustive or SAT search; local search or annealing; recursive product construction.
- **Structural assumption:** symmetric or equivariant objects; small support; near the conjectured optimum; far from it.
- **Scale:** solve many small cases exactly, find the pattern, then generalise.
- **Direction:** start from the obstruction (why the naive argument fails) rather than from the target.

Write the chosen angle in the brief as `<perspective>: <angle>`, or just `<angle>` when no perspective fits. If the worker opens a lineage, the angle becomes that lineage's idea tag.

## 8. Lessons files

```
version: <n>
# Lessons: <role>
<!-- Head-editable lessons layer. Refines the locked core in .claude/agents/<role>.md, never overrides it. ≤ ~30 lines. -->

- <lesson> (evidence: <task ids>; added <hh:mm>; version <n>)
```

- `version:` must be the first line. `pp.py` reads it into the brief's LESSONS line.
- Problem lessons (`run/<P>/lessons.md`) use the same format with `# Lessons: problem <P>`.
- Pending Referee/Checker-builder lessons wait in `.claude/lessons/pending/<role>.md` in the same format, which is never copied into an inbox.

CHANGELOG entry (`.claude/lessons/CHANGELOG.md`):

```
## <hh:mm> <role or problem P> v<old> → v<new>
- Change: <added / sharpened / merged / reverted: text>
- Evidence: <task ids>
- Result after next wave: <pending | improved: ... | no change → reverted | worse → reverted: why>
```
