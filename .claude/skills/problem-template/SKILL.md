---
name: problem-template
description: Template for a Proof Pursuit problem skill. The head copies this file to .claude/skills/problem-<slug>/SKILL.md and fills it in from the verbatim problem statement when a new problem is revealed (timebox ~10 minutes). Not loaded directly.
disable-model-invocation: true
---

<!--
HOW TO FILL THIS IN (head only; timebox ~10 minutes; delete this comment when done)
- Change the frontmatter: name: problem-<slug>, and a description of the form
  "Problem skill for <title> (<P>): statement, cells, hand-in format, cell typing, ladders,
  checker spec, angle bank, pitfalls. Load when opening problem <P> in a Proof Pursuit run."
  Remove disable-model-invocation.
- Copy text VERBATIM wherever the section says so. Don't paraphrase definitions.
- Don't solve anything. Every mathematical idea in the Ladders or the Angle bank is labelled
  (hypothesis) or (angle), never stated as a fact.
- Nothing about the literature goes in as fact. That is the Scout's job at run time.
  Scout references go in only as "unverified" until a human or a second scout has opened them.
- Workers never read this file. The head copies the relevant parts into briefs.
-->

# Problem <P>: <title>

Letter code: `<P>` (cell ids `<P>-C1` … `<P>-C6`). Ledger: `run/<P>/`.

## 1. Verbatim statement

<Setting text, verbatim, including every formula.>

### Cells

| Cell | Title | Points | Checking | Verbatim text |
|---|---|---|---|---|
| C1 | | | checked instantly / judged / open | |
| C2 | | | | |
| C3 | | | | |
| C4 | | | | |
| C5 | | | | |
| C6 | | | | |

(For long cell texts, give each cell its own subsection with the verbatim text.)

## 2. Definitions and notation (exactly as given)

- <term>: <definition, verbatim>
- Conventions stated in the problem: <e.g. repetitions allowed; angle range; bijection onto {1..n}>

## 3. Hand-in format

| Cell | What to hand in (verbatim or exact paraphrase) | Artefact files and format | Judges require |
|---|---|---|---|
| C1 | | | |

Global hand-in rules (verbatim): <e.g. computations only with code, < 10 min, exact/interval>.

## 4. Cell typing and exact targets

Types (head skill): scored construction / exact value with an instant check / prove a stated inequality or lemma / lower bound or optimality / open prove-or-disprove.

| Cell | Type | Tier guess (T0–T3) + reason | Exact target statement (all quantifiers, ranges, edge cases) |
|---|---|---|---|
| C1 | | | |

## 5. Decomposition ladders (hypotheses, not facts)

Lower cells are the way in: definitions, examples, obstacles. Say how each lower cell feeds the higher ones.

### C<k>
- R1 (hypothesis): <sub-claim>. Depends on: —
- R2 (hypothesis): <sub-claim>. Depends on: R1
- Feeds: <which higher cells reuse this, and how>

## 6. Checker spec (computational cells)

For each computational cell:
- **Input format:** <exact file format, e.g. one token per line, order, separators>
- **Validation:** <what makes an input malformed>
- **Output:** `VERIFIED <score>` or `FAILED: <reason>`; exit code 0/1.
- **Score:** <exact definition of the quantity>
- **Exactness:** <integers / fractions / interval with bound>
- **Runtime target:** <e.g. largest instance < 10 s; always < 10 min>
- **Random input generator for cross-testing:** <one-line description; the head writes it as a tiny script>
- **Hand-checkable cases:** <tiny instances the builders should hand-compute>

## 7. Angle bank (for FRESH / CONTRARIAN briefs; one per brief)

Use the axes from the head skill's angle generator. Each entry: idea tag, then the angle.
- `<tag>` (angle): representation / method family / structural assumption / scale / direction.

## 8. Pitfalls

Edge cases, ranges and conventions that are easy to get wrong:
- <e.g. repetitions allowed; d ≥ 1 vs d ≥ 2; bit-string order in the hand-in format; the degenerate case>

## 9. Problem-specific rules

- <e.g. "Citing a published result for the statement you are asked to prove does not count.">
- <e.g. "A value with no labelling behind it will not survive the later cells.">

## 10. Run notes (append during the run)

- <new pitfalls, clarifications, reasons for tier changes>
