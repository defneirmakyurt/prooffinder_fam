---
name: problem-bulgarian-solitaire
description: Problem skill for "Bulgarian solitaire" (B), transient lengths d_B(λ) and their maximum D_B(n) under the Bulgarian solitaire map on partitions of n. Holds the human-supplied conventions (pending cross-check against the official text), rules, pitfalls, checker spec and angle bank; cells and hand-in format are pending the official text. Load when opening problem B in a Proof Pursuit run.
---

# Problem B: Bulgarian solitaire

Letter code: `B` (cell ids `B-C1` … `B-C<m>`). Ledger: `run/B/`.

> **STATUS: CONVENTIONS ONLY.** The official problem text hasn't been pasted yet. Everything in §2 and §9 was supplied by the humans on 2026-09-26 and is **pending cross-check**. When the official text arrives:
> 1. put it verbatim in §1;
> 2. compare it against every row of the provenance table in §2;
> 3. where they differ, **the official text wins**. Update this skill and tell the humans exactly what differed.
>
> Until then, don't open problem B, don't dispatch workers on it, and don't guess cells from the problem's title.

## 1. Verbatim statement

**PENDING: official text not yet provided.**

### Cells

**PENDING.** The number of cells, titles, points, checking mode and verbatim cell texts all come from the official text.

## 2. Definitions and notation (human-supplied; pending cross-check)

- **State:** a partition \(\lambda=(\lambda_1\ge\cdots\ge\lambda_s>0)\) of \(n\). \(s\) is the number of parts.
- **The map \(B\):** subtract 1 from every part, remove the zeros, add a part of size \(s\) (the number of parts of \(\lambda\) *before* subtraction), then sort in decreasing order.
- **Transient length:** \(d_B(\lambda)=\min\{\,i\ge 0 : B^i(\lambda)\text{ is cyclic}\,\}\). A state is *cyclic* when it lies on a cycle of \(B\), i.e. \(B^j(\mu)=\mu\) for some \(j\ge1\).
- **Maximum transient:** \(D_B(n)=\max_{\lambda\vdash n} d_B(\lambda)\), over **all** partitions of \(n\).
- **Triangular numbers and staircase:** \(T_k=k(k+1)/2\), with \(T_0=0\); \(\delta_k=(k,k-1,\ldots,1)\).
- **Rank of \(n\):** the unique \(k\) with \(T_{k-1}<n\le T_k\).

Provenance table (fill in the "Official text" column when it arrives):

| # | Convention | Source | Official text | Match? |
|---|---|---|---|---|
| 1 | state = partition in decreasing order, positive parts | human, 2026-09-26 | pending | pending |
| 2 | \(B\): −1 from every part, drop zeros, add part \(s\), sort decreasing | human, 2026-09-26 | pending | pending |
| 3 | \(d_B\) = cycle-entry time, min \(i\ge0\) with \(B^i(\lambda)\) cyclic | human, 2026-09-26 | pending | pending |
| 4 | \(D_B(n)=\max_{\lambda\vdash n}d_B(\lambda)\) | human, 2026-09-26 | pending | pending |
| 5 | \(T_k=k(k+1)/2\), \(\delta_k=(k,\ldots,1)\) | human, 2026-09-26 | pending | pending |
| 6 | rank of \(n\): unique \(k\) with \(T_{k-1}<n\le T_k\) | human, 2026-09-26 | pending | pending |
| 7 | formula-in-\(k\) cells: exact formula, both bounds proved, every witness explicit in \(k\) | human, 2026-09-26 | pending | pending |
| 8 | rules in §9 (citing doesn't count; full proof with attribution; < 10 min) | human, 2026-09-26 | pending | pending |

## 3. Hand-in format

**PENDING.** Known so far (human-supplied): when a cell asks for a formula in \(k\), the hand-in gives the exact formula, a proof of both bounds, and every witness partition explicitly as a function of \(k\).

## 4. Cell typing and exact targets

**PENDING.** When the cells arrive, note that a "formula in \(k\)" cell is an **exact extremal value** in the head's gate. The target has two halves, and each goes through the gate separately:
- **(upper)** for every \(n\) in the cell's range and every \(\lambda\vdash n\): \(d_B(\lambda)\le F\);
- **(lower)** an explicit witness \(\lambda^{(k)}\) (or one per \(n\), as the cell requires), given as a function of \(k\), with \(d_B(\lambda^{(k)})=F\) **proved for every \(k\)**, not only computed for small \(k\).

## 5. Decomposition ladders (hypotheses, not facts)

Generic ladder for a "formula in \(k\)" cell, to be adapted to the actual cells:
- R1 (hypothesis): exact values of \(D_B(n)\) and all maximising \(\lambda\) for small \(n\), by exhaustive computation with the cross-tested checker. This makes those \(n\) only `COMPUTER-VERIFIED`.
- R2 (hypothesis): a candidate formula in \(k\) and a candidate witness family, read off R1. This is `CONJECTURED` until R3 and R4 are proved.
- R3 (hypothesis): the upper bound for all \(\lambda\vdash n\), for every \(n\) in range. This needs a proof; computation covers finitely many \(n\) only.
- R4 (hypothesis): the witness family attains the formula for every \(k\). This needs a proof that tracks the orbit symbolically in \(k\).
- Feeds: lower cells (small \(n\), specific ranks) should validate the checker and suggest R2 before higher cells are attempted.

## 6. Checker spec

The artefact format is **provisional** until the official hand-in format arrives.

- **Input format (provisional):** a text file with one partition per line: positive integers separated by single spaces, in weakly decreasing order. Mode `d` prints \(d_B\) for each line. Mode `D n` enumerates every \(\lambda\vdash n\) and prints \(D_B(n)\) with all maximisers.
- **Validation:** positive integers only, weakly decreasing, non-empty lines; in mode `D`, \(n\ge1\).
- **Output:** `VERIFIED <value>` (exit 0) or `FAILED: <reason>` (exit 1).
- **Score:** \(d_B\) **by cycle-entry time**. Iterate \(B\), recording the first time \(t\) each state is seen. At the first repeat, at time \(t\), of a state first seen at time \(s<t\): the transient length is \(s\) and the cycle length is \(t-s\). A cyclic start returns 0.
- **Exactness:** Python integers; states as sorted tuples.
- **Runtime target:** each mode under 10 minutes on a laptop for the largest \(n\) any cell needs (range pending).
- **Required tests:**
  - cyclic starts return **0**;
  - small \(n\) computed **by hand**, with the hand computation written out in a comment (values deliberately not given here);
  - a start where the first-repeat time and the cycle-entry time differ, to show the checker returns the cycle-entry time;
  - the sum of parts is preserved by \(B\) (assert it on every step);
  - a naive second implementation (store the full orbit list, find the first index of the repeated state) cross-checked on all \(\lambda\vdash n\) for small \(n\).
- **Random input generator for cross-testing:** random partitions of \(n\) for \(n=1..60\) (random compositions, sorted), plus the structured starts \((n)\), \((1^n)\), \(\delta_k\), and \(\delta_k\) with parts added or removed.

## 7. Angle bank (one per FRESH / CONTRARIAN brief)

- `young-diagram` (geometric angle): track how \(B\) moves the cells of the Young diagram of \(\lambda\).
- `potential-function` (analytic angle): look for a quantity that changes monotonically along \(B\)-orbits outside the cycles and bounds the transient.
- `orbit-invariants` (algebraic angle): invariants and symmetries of \(B\); the structure of the cyclic states at a given rank.
- `small-n-exact` (computational angle): exact \(d_B\), \(D_B\) and maximisers for small \(n\); extract the pattern in \(k\).
- `witness-family` (combinatorial angle): construct explicit families \(\lambda^{(k)}\) and follow their orbits symbolically.
- `obstruction-first` (angle): find what forces a long transient, and what a start must look like to be far from every cycle.

## 8. Pitfalls

- **Cycle-entry time ≠ first-repeat detection time.** If the first repeat occurs at time \(t\) and that state first appeared at time \(s<t\), the transient length is \(s\) and the cycle length is \(t-s\). Reporting \(t\) is wrong.
- **A cyclic start has transient 0.**
- **\(s\) is the number of parts *before* subtraction**, parts equal to 1 included, even though they vanish.
- **Sort after adding the new part.** The new part \(s\) goes into its sorted position, not at the front.
- **\(D_B(n)\) is a maximum over *all* \(\lambda\vdash n\).** A lower bound needs one explicit witness; the upper bound must cover every partition.
- **Rank boundaries:** \(n=T_k\) has rank \(k\); \(n=T_{k-1}+1\) also has rank \(k\); \(n=1\) has rank 1, since \(T_0=0\).
- **Formula in \(k\):** "exact" means an exact expression, with both bounds proved and the witness given explicitly as a function of \(k\). A pattern checked for \(k\le K\) is `CONJECTURED`, not proved.
- **The formula may depend on where \(n\) lies within its rank.** Check whether the cell asks for a formula in \(k\) alone, or in \(n\) and \(k\).

## 9. Problem-specific rules (human-supplied; pending cross-check)

- Citing a published result that answers a cell does not count. Write out the full proof, and attribute its source.
- Computations must run in under 10 minutes on a laptop.
- For a formula in \(k\): give the exact formula, prove both bounds, and give every witness partition explicitly as a function of \(k\).

## 10. Run notes

This skill is frozen during the run; the head doesn't edit it. The exception is the one-time update from the official text described at the top, which is done with the humans. New pitfalls, clarifications and problem-specific lessons go to `run/B/lessons.md`, which is copied into briefs for problem B only.
