---
name: problem-bulgarian-solitaire
description: Problem skill for "Bulgarian solitaire" (B), transient lengths d_B(λ) and their maximum D_B(n) under the Bulgarian solitaire shift on partitions of n. Holds the verbatim statement (official text), six cells, hand-in format, cell typing, ladders, checker spec, angle bank, pitfalls, Part S seeds and branch notes. Load when opening problem B in a Proof Pursuit run.
---

# Problem B: Bulgarian solitaire

Letter code: `B` (cell ids `B-C1` … `B-C6`). Ledger: `run/B/`. Official source: `sources/problem_description_bulgarian_solitaire.tex`.

> **Source note:** this skill follows the **official** text. The conventions the humans supplied earlier were cross-checked against it (§2 provenance table); where they differed, the official text wins. C1's verbatim text (below) was supplied 2026-09-26 from a screenshot the first transcription lacked; `sources/` now has it too.

## 1. Verbatim statement

Repeatedly take one card from every pile and form a new pile. How many moves can it take before the piles start to cycle?

**Definition (Partition).** A *partition* of a positive integer \(n\) is a weakly decreasing sequence
\[
\lambda=(\lambda_1,\ldots,\lambda_s)
\]
of positive integers with
\[
\lambda_1+\cdots+\lambda_s=n.
\]
Think of it as a division of \(n\) cards into \(s\) piles.

**Definition (Shift).** The *shift* \(B(\lambda)\) is the partition of \(n\) obtained as follows: remove one card from every pile, discard the piles that become empty, and add one new pile consisting of the \(s\) removed cards. Formally, \(B(\lambda)\) is the partition whose parts are the positive numbers among
\[
\lambda_1-1,\;\ldots,\;\lambda_s-1
\]
together with one extra part equal to \(s\).

Iterating \(B\) from any starting partition must eventually repeat, since there are finitely many partitions of \(n\).

**Definition (Cyclic partitions and time to cycle).** Call \(\lambda\) *cyclic* if
\[
B^i(\lambda)=\lambda\qquad\text{for some } i\ge 1,
\]
and let
\[
\begin{aligned}
d_B(\lambda)&=\min\{\,i\ge 0: B^i(\lambda)\text{ is cyclic}\,\},\\
D_B(n)&=\max\{\,d_B(\lambda):\lambda\text{ is a partition of } n\,\}.
\end{aligned}
\]
Thus \(D_B(n)\) is the largest number of shifts that can be needed before the process starts to cycle.

**Notation (Triangular numbers and rank).** Write
\[
T_k=\frac{k(k+1)}{2},\qquad \delta_k=(k,k-1,\ldots,2,1),
\]
the partition of \(T_k\) into distinct parts. Every \(n\ge 1\) satisfies
\[
T_{k-1}<n\le T_k
\]
for exactly one \(k\), which we call the *rank* of \(n\).

**Example.**
\[
\begin{aligned}
B\bigl((2,1,1,1,1)\bigr)&=(5,1),\\
B\bigl((5,1)\bigr)&=(4,2),\\
B\bigl((4,2)\bigr)&=(3,2,1),\\
B\bigl((3,2,1)\bigr)&=(3,2,1).
\end{aligned}
\]
Here \(d_B\bigl((2,1,1,1,1)\bigr)=3\).

### Cells

| Cell | Title | Points | Checking |
|---|---|---|---|
| C1 | Cyclic Partitions and Cycles | 1 | written proof |
| C2 | \(D_B\) at Triangular \(n\) | 2 | written proof |
| C3 | A General Upper Bound | 3 | written proof |
| C4 | One Above a Triangular Number | 5 | written proof |
| C5 | Two Above a Triangular Number | 8 | written proof |
| C6 | \(D_B(n)\) for Every \(n\) | 13 | **open question** |

**C1: Cyclic Partitions and Cycles (verbatim).** First, the long-run behaviour: which partitions repeat under the shift, and how they fall into cycles. Let \(n=T_k\). Prove that for every partition \(\lambda\) of \(n\) there is an \(i\) with \(B^i(\lambda)=\delta_k\), and that \(\delta_k\) is the only cyclic partition of \(n\). Then let \(n\) be arbitrary of rank \(k\), say \(n=T_{k-1}+r\) with \(1\le r\le k\): determine all cyclic partitions of \(n\), and determine the number of distinct cycles of \(B\) on the partitions of \(n\). Prove both.

**C2: \(D_B\) at Triangular \(n\) (verbatim).** Next, how long the process can take to reach a cycle, starting with the triangular numbers. Determine
\[
D_B(T_k)
\]
for every \(k\), with proof of both bounds.

**C3: A General Upper Bound (verbatim).** Now the numbers strictly between two consecutive triangular numbers.
- (a) Prove that for every \(k\ge 4\) and every non-triangular \(n\) with \(T_{k-1}<n<T_k\),
\[
D_B(n)\le k^2-2k-1.
\]
- (b) Determine \(D_B(T_k-1)\) exactly.
- (c) Determine also, for that \(n\), which partitions attain the maximum.

**C4: One Above a Triangular Number (verbatim).** The first family just above a triangular number:
\[
n=T_{k-1}+1,
\]
that is,
\[
n=11,16,22,29,\ldots\qquad\text{for } k=5,6,7,8,\ldots.
\]
Determine
\[
D_B(T_{k-1}+1)
\]
for every \(k\ge 5\), with proof of both bounds.

**C5: Two Above a Triangular Number (verbatim).** The next family:
\[
n=T_{k-1}+2,
\]
that is,
\[
n=3,5,8,12,17,23,\ldots\qquad\text{for } k=2,3,4,5,6,7,\ldots.
\]
Determine
\[
D_B(T_{k-1}+2)
\]
for every \(k\), with proof of both bounds.
- State exactly for which \(k\) your formula holds, and give the remaining values separately.
- Your upper bound must be a single argument valid for all \(k\) in that range, not a separate treatment of each \(k\).
- You must give the extremal partitions explicitly as a function of \(k\).
- Say also where the straightforward extension of the Cell 3 argument stops: give the bound it does yield, show it is strictly weaker than the truth, and identify precisely what your proof supplies in its place.

**C6: \(D_B(n)\) for Every \(n\) (verbatim).** **Open question.** Finally, the whole function
\[
n\longmapsto D_B(n).
\]
Determine \(D_B(n)\) for every \(n\).

## 2. Definitions and notation (exactly as given)

- *Partition* of \(n\ge1\): a weakly decreasing sequence of positive integers summing to \(n\); \(s\) is the number of parts ("piles").
- *Shift* \(B(\lambda)\): the parts are the positive numbers among \(\lambda_1-1,\ldots,\lambda_s-1\), together with one extra part equal to \(s\) (so \(B(\lambda)\) is again a partition of \(n\), written weakly decreasing).
- *Cyclic:* \(B^i(\lambda)=\lambda\) for some \(i\ge1\).
- \(d_B(\lambda)=\min\{i\ge0: B^i(\lambda)\text{ cyclic}\}\); \(D_B(n)=\max_{\lambda\vdash n} d_B(\lambda)\).
- \(T_k=k(k+1)/2\); \(\delta_k=(k,k-1,\ldots,1)\). The rank of \(n\ge1\) is the unique \(k\) with \(T_{k-1}<n\le T_k\) (the formula gives \(T_0=0\), so \(n=1\) has rank 1).

Provenance table (human-supplied conventions of 2026-09-26 vs. the official text):

| # | Convention (human-supplied) | Official text | Match? |
|---|---|---|---|
| 1 | state = partition in decreasing order, positive parts | "weakly decreasing sequence of positive integers" | yes |
| 2 | \(B\): −1 from every part, drop zeros, add a part \(s\), sort decreasing | positive numbers among \(\lambda_i-1\), plus one extra part \(s\); result is a partition | yes (sorting is implicit in "partition") |
| 3 | \(d_B\) = min \(i\ge0\) with \(B^i(\lambda)\) cyclic | same | yes |
| 4 | \(D_B(n)=\max_{\lambda\vdash n}d_B(\lambda)\) | same | yes |
| 5 | \(T_k=k(k+1)/2\) with \(T_0=0\); \(\delta_k=(k,\ldots,1)\) | same formula; \(T_0\) not stated, but the rank definition for \(n=1\) needs \(T_0=0\), which the formula gives | yes |
| 6 | rank: unique \(k\) with \(T_{k-1}<n\le T_k\) | same | yes |
| 7 | formula-in-\(k\) cells: exact formula, both bounds, witnesses explicit in \(k\) | "give the exact value as a formula in \(k\) and prove both bounds; state any partitions you use explicitly as functions of \(k\)" | yes |
| 8 | rules: citing doesn't count; full proof **with attribution**; < 10 min | citing doesn't count; "a proof written out in full does, whatever its source". Computation: code included, < 10 min, **and exhaustive over a finite set that your argument has reduced the problem to** | **differs** (see below) |

**Differences for the humans** (the official text wins):
1. Rule 8: the official computation rule is stricter than the supplied one. A computation counts only if it is exhaustive over a finite set the argument has reduced the problem to. The supplied rule only mentioned the 10-minute limit.
2. Rule 8: the official text does not itself require attribution of a written-out proof's source (the general hackathon rule to separate cited results from our own still applies).
3. The official text adds a **Status** rule: say clearly which cells are solved and which are partial.
4. The official text has six cells. C1's statement was missing from the first transcription; it was supplied from a screenshot on 2026-09-26 and is now in §1 and in `sources/`.

## 3. Hand-in format

Official "What to Hand In" (verbatim): "For each cell you attempt, hand in a written proof. **Computation.** You may use a computer to explore. A proof may rely on a computation only if you include the code, it runs in under 10 minutes on a laptop, and the computation is exhaustive over a finite set that your argument has reduced the problem to. **Exact values.** Where a cell asks you to determine a quantity, give the exact value as a formula in \(k\) and prove both bounds; state any partitions you use explicitly as functions of \(k\). **Status.** Say clearly which cells you consider solved and which are partial. **Citations.** Citing a published result for the statement you are asked to prove does not count as a solution; a proof written out in full does, whatever its source."

| Cell | Artefact files | Judges require |
|---|---|---|
| C1 | `submission.md` | for \(n=T_k\): proof every \(\lambda\vdash n\) reaches \(\delta_k\) under iteration, and that \(\delta_k\) is the unique cyclic partition of \(n\); for general \(n=T_{k-1}+r\) (\(1\le r\le k\)): the complete, explicit list of cyclic partitions of \(n\) and the exact count of distinct \(B\)-cycles on partitions of \(n\), both proved |
| C2 | `submission.md` | formula for \(D_B(T_k)\) for every \(k\); both bounds proved; witnesses explicit in \(k\) |
| C3 | `submission.md` | (a) proof of the bound for all \(k\ge4\) and all non-triangular \(n\) in range; (b) exact \(D_B(T_k-1)\), both bounds; (c) the full set of maximisers at \(n=T_k-1\), with proof that there are no others |
| C4 | `submission.md` | formula for every \(k\ge5\); both bounds; witnesses explicit in \(k\) |
| C5 | `submission.md` | formula with its exact \(k\)-range and remaining values separately; **one** upper-bound argument for the whole range; extremal partitions explicit in \(k\); the Cell 3 extension analysis (its bound, strictly weaker, what replaces it) |
| C6 | `submission.md` | \(D_B(n)\) for every \(n\); partial progress per the hackathon rules |

Code, where a step rests on computation, ships in `submission/` with its run command and measured runtime.

## 4. Cell typing and exact targets

Every "determine" cell is an **exact extremal value** in the head's gate: an upper bound over every \(\lambda\vdash n\) and an explicit witness family with \(d_B\) equal to the value **proved for every \(k\)**. The two halves go through the gate separately.

| Cell | Type | Tier guess + reason | Exact target |
|---|---|---|---|
| C1 | classification + count, two parts | T1: 1 pt; base case then general case | (i) For \(n=T_k\): every \(\lambda\vdash T_k\) has \(B^i(\lambda)=\delta_k\) for some \(i\), and \(\delta_k\) is the unique cyclic partition of \(T_k\). (ii) For \(n=T_{k-1}+r\), \(1\le r\le k\): the explicit set of cyclic partitions of \(n\), and the exact number of distinct \(B\)-cycles on partitions of \(n\) — both proved for every \(k\) and every \(r\) in range. |
| C2 | exact extremal value | T1: 2 pts; one family | For every \(k\ge1\): a formula \(F_2(k)\) with (upper) \(d_B(\lambda)\le F_2(k)\) for all \(\lambda\vdash T_k\), and (lower) an explicit \(\lambda^{(k)}\vdash T_k\) with \(d_B(\lambda^{(k)})=F_2(k)\). |
| C3 | (a) prove a stated bound; (b) exact extremal value; (c) classification | T2: 3 pts, three parts | (a) For all \(k\ge4\), all \(n\) with \(T_{k-1}<n<T_k\), all \(\lambda\vdash n\): \(d_B(\lambda)\le k^2-2k-1\). (b) A formula for \(D_B(T_k-1)\) with both halves; the \(k\)-range is **not stated** in the cell (see Pitfalls). (c) The exact set \(\{\lambda\vdash T_k-1: d_B(\lambda)=D_B(T_k-1)\}\), as explicit functions of \(k\), with proof that it is complete. |
| C4 | exact extremal value | T2: 5 pts | For every \(k\ge5\): a formula for \(D_B(T_{k-1}+1)\) with both halves; witnesses explicit in \(k\). |
| C5 | exact extremal value + method analysis | T2/T3: 8 pts, four stated requirements | For every \(k\ge2\): \(D_B(T_{k-1}+2)\), as a formula on a stated \(k\)-range plus the remaining values separately; one uniform upper-bound argument; explicit extremal partitions; the Cell 3 extension analysis. |
| C6 | open | T3: marked open | \(D_B(n)\) for every \(n\ge1\). Partial progress: further families, as the hackathon rules allow. |

## 5. Decomposition ladders (hypotheses, not facts)

Lower cells feed higher ones: C2 fixes the triangular case, C3 gives a general bound and one boundary family, C4 and C5 are the first two families above a triangular number, C6 is everything.

### Generic ladder for a "determine" cell
- R1 (hypothesis): exact \(D_B(n)\) and all maximisers for small \(n\) in the family, by exhaustive computation with the cross-tested checker. This is `COMPUTER-VERIFIED` for those \(n\) only.
- R2 (hypothesis): a candidate formula in \(k\) and a candidate witness family, read off R1. `CONJECTURED` until R3 and R4 are proved.
- R3 (hypothesis): the upper bound for all \(\lambda\vdash n\), for every \(k\) in range. Needs a proof; computation covers finitely many \(k\) only.
- R4 (hypothesis): the witness family attains the formula for every \(k\), by tracking its orbit symbolically in \(k\).

### C3
- R1 (hypothesis): (a) may come from comparing \(\lambda\) with a structure at the nearby triangular numbers; how is for the workers.
- R2 (hypothesis): (b) and (c) follow the generic ladder at \(n=T_k-1\); (c) additionally needs a proof that no other partition attains the maximum.
- Feeds: C5 requires the "straightforward extension of the Cell 3 argument", so C3(a)'s argument must be on the record before C5's last requirement can be met.

### C4 / C5
- R1 (hypothesis): generic ladder on the family \(n=T_{k-1}+1\) (C4) or \(T_{k-1}+2\) (C5).
- R2 (hypothesis): for C5, the small-\(k\) exceptions the cell expects ("give the remaining values separately") show up in R1's data.
- R3 (hypothesis): for C5, apply the C3(a) argument to \(n=T_{k-1}+2\), record the bound it yields, and compare with R2.

### C6
- R1 (hypothesis): families \(n=T_{k-1}+j\) for further fixed \(j\), and \(n=T_k-j\), extend the C3–C5 pattern.
- R2 (hypothesis): exhaustive small-\(n\) tables expose how \(D_B\) depends on the position of \(n\) within its rank.

## 6. Checker spec (for exploration, Breakers and Referees; the cells themselves are proofs)

The official text fixes no artefact file format; this one is internal.

- **Input format:** a text file with one partition per line: positive integers separated by single spaces, weakly decreasing. Mode `d FILE` prints \(d_B\) for each line. Mode `D n` enumerates every \(\lambda\vdash n\) and prints \(D_B(n)\) with all maximisers.
- **Validation:** positive integers only, weakly decreasing, non-empty lines; in mode `D`, \(n\ge1\).
- **Output:** `VERIFIED <value>` (exit 0) or `FAILED: <reason>` (exit 1).
- **Score:** \(d_B\) **by cycle-entry time**. Iterate \(B\), recording the first time each state is seen. At the first repeat, at time \(t\), of a state first seen at time \(s<t\): the transient length is \(s\) and the cycle length is \(t-s\). A cyclic start returns 0.
- **Exactness:** Python integers; states as tuples in weakly decreasing order.
- **Runtime target:** mode `D` under 10 minutes on a laptop for the largest \(n\) any exploration needs; state the largest \(n\) reached.
- **Required tests:**
  - the official example: \(B\) maps \((2,1,1,1,1)\to(5,1)\to(4,2)\to(3,2,1)\to(3,2,1)\), and \(d_B((2,1,1,1,1))=3\);
  - a cyclic start returns **0**;
  - small \(n\) computed **by hand**, with the hand computation in a comment;
  - a start where the first-repeat time and the cycle-entry time differ;
  - \(B\) preserves the sum of parts (assert on every step);
  - a naive second implementation (store the orbit list, find the first index of the repeated state), cross-checked on all \(\lambda\vdash n\) for small \(n\).
- **Random input generator for cross-testing:** random partitions of \(n\) for \(n=1..60\) (random compositions, sorted), plus the structured starts \((n)\), \((1^n)\), \(\delta_k\), and \(\delta_k\) with parts added or removed.

## 7. Angle bank (one per FRESH / CONTRARIAN brief)

- `young-diagram` (angle): track how \(B\) moves the cells of the Young diagram of \(\lambda\).
- `potential-function` (angle): a quantity that changes monotonically along orbits outside the cycles and bounds the transient.
- `orbit-invariants` (angle): invariants and symmetries of \(B\); the structure of the cyclic states at a given rank.
- `small-n-exact` (angle): exact \(d_B\), \(D_B\) and maximisers for small \(n\); extract the pattern in \(k\).
- `witness-family` (angle): explicit families \(\lambda^{(k)}\), with their orbits followed symbolically.
- `obstruction-first` (angle): what forces a long transient; what a start must look like to be far from every cycle.
- `rank-position` (angle): parametrise \(n=T_{k-1}+j\) and study the dependence on \(j\) and \(k\) separately.

## 8. Pitfalls

- **Cycle-entry time ≠ first-repeat detection time.** If the first repeat occurs at time \(t\) and that state first appeared at time \(s<t\), the transient length is \(s\). Reporting \(t\) is wrong.
- **A cyclic start has \(d_B=0\).**
- **\(s\) is the number of parts before subtraction**, parts equal to 1 included, even though they vanish.
- **The new part \(s\) goes into its sorted position**, not at the front.
- **\(D_B(n)\) is a maximum over all \(\lambda\vdash n\).** The upper bound must cover every partition; the lower bound needs an explicit witness.
- **Rank boundaries:** \(n=T_k\) has rank \(k\); \(n=T_{k-1}+1\) also has rank \(k\); \(n=1\) has rank 1.
- **"Exact" means a formula in \(k\) with both bounds proved for every \(k\).** A pattern checked for \(k\le K\) is `CONJECTURED`.
- **Ranges differ by cell:** C2 "every \(k\)"; C3(a) \(k\ge4\) and \(n\) strictly between \(T_{k-1}\) and \(T_k\); C3(b) states **no** \(k\)-range (flag the range you prove); C4 \(k\ge5\); C5 every \(k\ge2\), with the formula's range stated and the remaining values given separately.
- **C5 at \(k=2\) is \(n=3=T_2\)**, a triangular number (arithmetic from the definitions). C3(a) covers only non-triangular \(n\).
- **C3(c) asks for all maximisers**, not one.
- **C5's upper bound must be one argument** for the whole range, not a case-by-case treatment of each \(k\).
- **Computation counts only if exhaustive over a finite set the argument has reduced the problem to.** Small-\(n\) tables alone prove nothing for all \(k\).

## 9. Problem-specific rules

- Citing a published result for the statement you are asked to prove does not count; a proof written out in full does, whatever its source. Separate cited results from our own, as the hackathon rules require.
- Computation: code included, < 10 minutes on a laptop, exhaustive over a finite set the argument has reduced the problem to.
- Exact values: a formula in \(k\), both bounds proved, partitions given explicitly as functions of \(k\).
- Say clearly which cells are solved and which are partial.

## 10. Run notes

This skill is frozen during the run; the head doesn't edit it. The one exception: when the humans supply C1's verbatim text, it is added to §1, §3, §4 and §11 with them. New pitfalls, clarifications and problem-specific lessons go to `run/B/lessons.md`, which is copied into briefs for problem B only.

## 11. Checklist Part S seeds and branch notes

Part S seeds (from the statement only; referees and gate only):
- **S2 extremal configurations:** C1 is the exception — it names \(\delta_k\) explicitly as the unique cyclic partition at \(n=T_k\). Unknown for every other cell (the statement names no maximiser).
- **S3 cases to cover:**
  - C1(i): every \(k\ge1\), \(n=T_k\). C1(ii): every \(k\ge1\) and every \(r\) with \(1\le r\le k\).
  - C2: every \(k\ge1\).
  - C3(a): every \(k\ge4\) and every non-triangular \(n\) with \(T_{k-1}<n<T_k\); every \(\lambda\vdash n\).
  - C3(b)/(c): the \(k\)-range the proof claims, stated explicitly; (c) completeness of the maximiser list.
  - C4: every \(k\ge5\).
  - C5: every \(k\ge2\): the formula's range plus the remaining values.
  - Everywhere: cyclic starts (\(d_B=0\)); partitions with many parts equal to 1.
- **S5 consistency** (arithmetic from the definitions):
  - C1(ii) at \(r=k\) is \(n=T_k\), so it must reduce to C1(i): exactly one cyclic partition (\(\delta_k\)), one cycle.
  - C1's classification of cyclic partitions is a prerequisite for every cyclicity check in C2–C6's ladders (R1's brute force and R3/R4's proofs both need it).
  - C5 at \(k=2\) is \(n=3=T_2\), so it must agree with C2 at \(k=2\).
  - \(T_k-1=T_{k-1}+(k-1)\): C3(b) at \(k=3\) is \(n=5=T_2+2\), so it must agree with C5 at \(k=3\).
  - For \(k\ge4\), C4's and C5's values are at non-triangular \(n\) of rank \(k\), so they must satisfy C3(a)'s bound \(k^2-2k-1\).
  - C6 must agree with every gated lower cell.
- **S6 checkable values:** the official example: \(B((2,1,1,1,1))=(5,1)\), \(B((5,1))=(4,2)\), \(B((4,2))=(3,2,1)\), \(B((3,2,1))=(3,2,1)\), so \((3,2,1)\) is cyclic and \(d_B((2,1,1,1,1))=3\); hence \(D_B(6)\ge3\).
- **C5 meta-requirement:** the referee checks that the submission states the formula's \(k\)-range, gives the remaining values, uses one uniform upper-bound argument, and contains the Cell 3 extension analysis.

Branch notes (angles, each only into its own 2B lens):
- ALGEBRAIC (angle): invariants of \(B\) and the structure of the cyclic states at a given rank.
- TOPOLOGICAL (angle): the functional graph of \(B\) on partitions of \(n\): trees hanging off cycles; depth of the deepest tree.
- ANALYSIS (angle): a potential or energy function on partitions that decreases along transient orbits.
- NUMBER-THEORY (angle): the position \(j\) of \(n=T_{k-1}+j\) within its rank; divisibility and parity in \(k\) and \(j\).
- DISCRETE (angle): Young diagrams and the movement of their cells under \(B\); explicit witness families.
