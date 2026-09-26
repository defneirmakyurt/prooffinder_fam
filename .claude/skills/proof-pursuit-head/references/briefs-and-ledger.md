# Briefs, reports and ledger templates

Contents:
1. Common brief header
2. Role-specific brief sections
3. Worker return report
4. Referee verdict
5. Dead-end entry
6. Board template
7. Angle generator

## 1. Common brief header

Every brief starts with this block, filled in.

```
TASK: <P>-<cell>-<nnn>      ROLE: <role>      REGIME: <EXPLOIT | FRESH | CONTRARIAN | CLEAN-ROOM>
TIME BOX: <minutes>
READ ONLY: tasks/<task-id>/ (this brief + inbox/). Do not open anything else under run/.
WRITE ONLY: tasks/<task-id>/out/
TARGET: <exact statement to prove / construct / check / refute>
RULES: <cell rules binding this worker, e.g. "citing a published proof of the target does not count";
        "any computation must be exact or interval arithmetic, code included, runtime < 10 min">
RETURN: only the report block from section 3, at most 200 words plus a LADDER of at most 10 lines.
        Full work goes in out/.
```

## 2. Role-specific brief sections

Add the matching block after the header.

**Scout**
```
Produce out/boundary.md with a table:
Statement/case | Status (PROVED / COMPUTER-VERIFIED (code public?) / CONJECTURED / OPEN / UNSURE)
| Reference (authors, title, year, theorem or table number, arXiv/DOI) | Method notes.
Also list known small-case values and the main techniques in the literature.
If you are not certain a reference exists, write UNSURE. Never merge "checked by computer" into "proved".
```

**Prover**
```
First write out/plan.md: TARGET as a ladder of numbered rungs (lemmas, special cases, reductions)
with dependencies. Work through it in order, marking each rung
PROVED / CHECKED / GAP / REFUTED / NOT STARTED.
Write out/proof.md. First line: the exact statement you prove, no more.
Then numbered steps; each justified by a definition, an earlier step, or a named lemma with exact reference.
Mark anything you are not sure of [GAP].
Numerics may guide you; any step resting on computation must include code in out/,
exact or interval arithmetic, runtime < 10 min.
```
Regime additions:
- EXPLOIT: `Inbox holds the current best proof and the referee's critique. Repair the listed problems first. If the approach cannot be repaired, say so and why.`
- FRESH: `ANGLE: <angle>. Pursue this angle; if you abandon it, say why.`
- CONTRARIAN: `FORBIDDEN APPROACHES (already tried, do not use): <lines from deadends.md + live lineage tags>.`

**Searcher**
```
First write out/plan.md: TARGET as a ladder of numbered rungs (checker sanity, small cases,
reductions, search stages) with dependencies. Work through it in order, marking each rung
PROVED / CHECKED / GAP / REFUTED / NOT STARTED.
Inbox holds checker/ (use it as your scoring function) and, if EXPLOIT, the lineage's best program and artefact.
Write a program that generates candidates; do not hand-craft objects.
Save: out/best.<ext> (artefact in the cell's required format), out/search/ (code),
out/runlog.md (method, seeds, restarts, runtime, best score per run).
State whether any search was exhaustive and over exactly which class;
give the soundness argument for every symmetry reduction.
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
```

**Checker-builder**
```
From the statement alone, write out/verify.py: Python standard library only (fractions allowed),
exact arithmetic, reads the artefact format given in TARGET, prints VERIFIED + score,
or the exact reason for failure. Keep it short enough to read line by line.
Also write out/tests.py: hand-computed small cases plus a brute-force cross-check where feasible.
```

**Referee**
```
Inbox holds a statement and a proof. You do not know who wrote it or how confident anyone is. Assume it may be wrong.
1. Does the proved statement match TARGET exactly (ranges, quantifiers, edge cases)?
2. Read step by step; stop at the first step that is not justified.
3. You may test steps numerically.
Return the verdict block in section 4 instead of the section 3 report.
```

**Scribe**
```
Inbox holds accepted artefacts and the cell's "what to hand in" text.
Produce out/submission.md in exactly that format: statement, status, cited vs. new,
proof or certificate, how to verify (command, expected output, runtime), limitations.
Add no claim that is not in the accepted artefacts.
```

## 3. Worker return report

```
TASK: <id>   ROLE: <role>   REGIME: <regime>
OUTCOME: CLAIM | PARTIAL | NO-PROGRESS | REFUTED
CLAIM: <one precise sentence, or "none">
LADDER: <Prover/Searcher/Breaker only; one line per rung, ≤10 lines, ≤15 words each>
  R1 <PROVED | CHECKED | GAP | REFUTED | NOT STARTED> — <sub-claim>
  R2 ...
ARTEFACTS: <paths in out/>
IDEA-TAG: <2–4 words naming the approach>
KNOWN GAPS: <numbered list, or "none found">
DEAD ENDS: <approach — why it fails; one line each>
SCORE: <searchers: value from the provided checker; others: n/a>
```

The head uses IDEA-TAG to spot convergence and to name lineages. SCORE is always recomputed before it is trusted.
The 200-word limit excludes LADDER lines; the full ladder stays in out/plan.md.
LADDER statuses are the worker's claims: a PROVED rung is unrefereed and a CHECKED rung is unrerun
until the head says otherwise. GAP rungs become EXPLOIT repair targets.

## 4. Referee verdict

```
VERDICT: ACCEPT | MINOR | MAJOR | WRONG
STATEMENT MATCH: yes | no — <difference>
FIRST PROBLEM: step <k> — <what is unjustified; the fix, if known>
OTHER ISSUES: <list>
CHECKS RUN: <numerical tests, small cases>
```

## 5. Dead-end entry

```
- [<idea-tag>] <approach> — <why it fails / where it stalls> (<task id>)
```

Keep each entry to one line. CONTRARIAN briefs receive these lines verbatim.

## 6. Board template

```
# Board: updated <time>, run time <h:mm> of 7:00

| Cell | Pts | Tier | Status | Best so far | Live lineages | Next wave | Time used |
|------|-----|------|--------|-------------|---------------|-----------|-----------|
| H-C1 | 1 | T0: <reason> | ... | ... | ... | ... | 0:00 |
| A-C1 | 2 | T1: <reason> | ... | ... | ... | ... | 0:00 |

## Awaiting gate
## Decisions for the team
## Obstacle notes (parked cells)
```

## 7. Angle generator

When a FRESH or CONTRARIAN worker needs an angle, change at least one axis relative to every live lineage:

- **Representation:** vectors vs. Gram matrix vs. projections; graph vs. poset vs. matrix; labelling vs. ordering vs. orientation.
- **Method family:** induction or reduction; extremal (perturb at an optimum); averaging or probabilistic; convexity or majorisation; LP/SDP duality; explicit construction; exhaustive or SAT search; local search or annealing; recursive product construction.
- **Structural assumption:** symmetric or equivariant objects; small support; near the conjectured optimum; far from it.
- **Scale:** solve many small cases exactly, find the pattern, then generalise.
- **Direction:** start from the obstruction (why the naive argument fails) rather than from the target.

Write the chosen angle in the brief. If the worker opens a lineage, the angle becomes that lineage's idea tag.
