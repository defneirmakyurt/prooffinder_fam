---
name: problem-angles-lines
description: Problem skill for "Angles between lines" (A), Fejes Tóth's 1959 conjecture on the sum of pairwise angles between N lines through the origin. Holds the verbatim statement (official text), six cells, hand-in format, cell typing, ladders, checker spec, angle bank, pitfalls, Part S seeds and branch notes. Load when opening problem A in a Proof Pursuit run.
---

# Problem A: Angles between lines

Letter code: `A` (cell ids `A-C1` … `A-C6`). Ledger: `run/A/`. Official source: `sources/problem_description_angles_between_lines.tex`.

> **Source note:** this skill follows the **official** text. The earlier practice extract (`sources/practice-problems.md`) dropped Cell 1 and listed the cells in a different order. The official numbering and order are used everywhere here. The official text does not say which cells are checked instantly and which are judged; every cell asks for a written proof.

## 1. Verbatim statement

How large can the sum of pairwise angles between \(N\) lines through the origin be? Fejes Tóth conjectured in 1959 that orthogonal lines win.

**Definition (Lines and angles).** A *line* here always means a line through the origin of \(\mathbb{R}^d\). The *angle* between two lines \(\ell,\ell'\) is the acute (non-obtuse) angle \(\theta(\ell,\ell')\in[0,\pi/2]\) between them. If \(\ell,\ell'\) are spanned by unit vectors \(x,x'\), then
\[
\theta(\ell,\ell')=\arccos |\langle x,x'\rangle|.
\]

**Definition (Angle sum).** For lines \(\ell_1,\ldots,\ell_N\) in \(\mathbb{R}^d\) (repetitions allowed), write
\[
S(\ell_1,\ldots,\ell_N)=\sum_{1\le i<j\le N}\theta(\ell_i,\ell_j).
\]

The question is how large \(S\) can be.

**Conjecture (L. Fejes Tóth, 1959).** \(S\) is maximised by taking \(d\) mutually orthogonal lines, each used either \(\lfloor N/d\rfloor\) or \(\lceil N/d\rceil\) times.

**Example.** When \(N=d+k\) with \(0\le k\le d\), that configuration (the \(d\) coordinate axes, \(k\) of them used twice) has
\[
S=\left(\binom{N}{2}-k\right)\frac{\pi}{2},
\]
because exactly \(k\) pairs of lines coincide and every other pair is orthogonal.

Each cell below asks you to prove this bound, or a special case of it. Unless a cell says otherwise, you need a complete proof. Citing a published result for the statement you are asked to prove does not count.

### Cells

| Cell | Title | Points | Checking |
|---|---|---|---|
| C1 | Lines in the Plane | 1 | written proof (mode not stated) |
| C2 | An Orthogonality Lemma | 2 | written proof |
| C3 | \(d+1\) Lines in \(\mathbb{R}^d\) | 3 | written proof |
| C4 | Five Lines in \(\mathbb{R}^3\), Six in \(\mathbb{R}^4\) | 5 | written proof |
| C5 | \(d+2\) Lines in \(\mathbb{R}^d\) | 8 | written proof |
| C6 | \(N\) Lines in \(\mathbb{R}^d\) | 13 | **open question** |

**C1: Lines in the Plane (verbatim).** We begin in the plane (\(d=2\)), where the conjectured optimum splits the \(N\) lines as evenly as possible between two perpendicular directions. Let \(\ell_1,\ldots,\ell_N\) be lines in \(\mathbb{R}^2\). Prove that
\[
S(\ell_1,\ldots,\ell_N)\le\frac{\pi}{2}\left\lfloor\frac{N^2}{4}\right\rfloor.
\]

**C2: An Orthogonality Lemma (verbatim).** A statement about a chain of vectors, in which each vector may fail to be orthogonal only to its immediate neighbours in the list. Let \(m\ge 2\) and let \(x_1,\ldots,x_m\) be unit vectors in \(\mathbb{R}^{m-1}\) with \(\langle x_i,x_j\rangle=0\) whenever \(|i-j|\ge 2\). Prove that
\[
\sum_{i=1}^{m-1}\theta(x_i,x_{i+1})\le (m-2)\frac{\pi}{2},
\]
where \(\theta(x,y)=\arccos|\langle x,y\rangle|\).

**C3: \(d+1\) Lines in \(\mathbb{R}^d\) (verbatim).** The first case in every dimension: one line more than the dimension, \(N=d+1\), where the conjectured optimum repeats exactly one of the \(d\) coordinate axes. Let \(d\ge 1\). Prove that any \(d+1\) lines in \(\mathbb{R}^d\) satisfy
\[
S\le \left(\binom{d+1}{2}-1\right)\frac{\pi}{2}.
\]

**C4: Five Lines in \(\mathbb{R}^3\), Six in \(\mathbb{R}^4\) (verbatim).** Two concrete instances of the next case, \(N=d+2\): five lines in three dimensions and six lines in four. In each, the conjectured optimum repeats two of the coordinate axes. Prove that any \(5\) lines in \(\mathbb{R}^3\) satisfy \(S\le 4\pi\), and that any \(6\) lines in \(\mathbb{R}^4\) satisfy \(S\le \frac{13\pi}{2}\).

**C5: \(d+2\) Lines in \(\mathbb{R}^d\) (verbatim).** The case \(N=d+2\) in every dimension, with the same conjectured optimum: the \(d\) coordinate axes, two of them repeated. Prove that for every \(d\ge 2\), any \(d+2\) lines in \(\mathbb{R}^d\) satisfy
\[
S\le \left(\binom{d+2}{2}-2\right)\frac{\pi}{2}.
\]

**C6: \(N\) Lines in \(\mathbb{R}^d\) (verbatim).** **Open question.** Fejes Tóth's conjecture from the setting, for every \(N\) and every \(d\). For \(N\) lines in \(\mathbb{R}^d\), write \(N=qd+s\), \(0\le s<d\), and let
\[
M(N,d)=s\binom{q+1}{2}+(d-s)\binom{q}{2}.
\]
Prove or disprove: every \(N\) lines in \(\mathbb{R}^d\) satisfy
\[
S\le \left(\binom{N}{2}-M(N,d)\right)\frac{\pi}{2}.
\]
This is the value attained by splitting the lines as evenly as possible among \(d\) mutually orthogonal directions. Settling any infinite family not already covered above counts as partial progress.

## 2. Definitions and notation (exactly as given)

- *Line:* a line through the origin of \(\mathbb{R}^d\).
- *Angle between lines:* \(\theta(\ell,\ell')\in[0,\pi/2]\), the acute (non-obtuse) angle; \(\theta=\arccos|\langle x,x'\rangle|\) for spanning unit vectors.
- *For vectors (C2):* \(\theta(x,y)=\arccos|\langle x,y\rangle|\). This is the angle between the lines they span, not the vector angle.
- \(S(\ell_1,\ldots,\ell_N)=\sum_{i<j}\theta(\ell_i,\ell_j)\), with **repetitions allowed**.
- \(N=qd+s\), \(0\le s<d\); \(M(N,d)=s\binom{q+1}{2}+(d-s)\binom{q}{2}\): the number of coinciding pairs in the balanced orthogonal configuration.

## 3. Hand-in format

Official "What to Hand In" (verbatim): "For each cell you attempt, hand in a written proof. **Computation.** You may use a computer to explore. A proof may rely on a computation only if you include the code, it runs in under 10 minutes on a laptop, and it is rigorous: exact or interval arithmetic, or an argument that bounds the numerical error. **Status.** Say clearly which cells you consider solved and which are partial."

| Cell | Artefact files | Judges require |
|---|---|---|
| C1–C5 | `submission.md` (proof), plus code if any step rests on computation | a complete proof; cell declared solved or partial |
| C6 | a proof or disproof, or partial progress on an infinite family not already covered | a disproof needs a rigorously verified counterexample; partial progress must be a family outside C1–C5 |

## 4. Cell typing and exact targets

| Cell | Type | Tier guess + reason | Exact target |
|---|---|---|---|
| C1 | prove a stated inequality | T0/T1: 1 pt, fixed \(d=2\), all \(N\) | For every \(N\) and all lines \(\ell_1..\ell_N\) in \(\mathbb{R}^2\) (repetitions allowed): \(S\le\frac{\pi}{2}\lfloor N^2/4\rfloor\). |
| C2 | prove a stated lemma | T1: 2 pts, a genuine lemma | For all \(m\ge2\) and all unit \(x_1..x_m\in\mathbb{R}^{m-1}\) with \(\langle x_i,x_j\rangle=0\) for \(|i-j|\ge2\): \(\sum_{i=1}^{m-1}\arccos|\langle x_i,x_{i+1}\rangle|\le(m-2)\pi/2\). |
| C3 | prove a stated inequality | T1: 3 pts, "first case", likely uses C2 (hypothesis) | For all \(d\ge1\) and all lines \(\ell_1..\ell_{d+1}\) in \(\mathbb{R}^d\): \(S\le(\binom{d+1}{2}-1)\pi/2\). |
| C4 | prove two stated inequalities | T2: concrete but must be rigorous; a computer-assisted route may exist | (a) all 5 lines in \(\mathbb{R}^3\): \(S\le4\pi\); (b) all 6 lines in \(\mathbb{R}^4\): \(S\le13\pi/2\). Both are needed for SOLVED. |
| C5 | prove a stated inequality | T2: 8 pts, every \(d\) | For all \(d\ge2\) and all lines \(\ell_1..\ell_{d+2}\) in \(\mathbb{R}^d\): \(S\le(\binom{d+2}{2}-2)\pi/2\). |
| C6 | open prove-or-disprove | T3: marked open | For all \(N,d\): \(S\le(\binom N2-M(N,d))\pi/2\), or a counterexample. Partial: an infinite family not covered by C1–C5. |

## 5. Decomposition ladders (hypotheses, not facts)

Lower cells are the way in. C1 is the plane case for every \(N\). C2's lemma is placed as a tool. C3–C5 are the \(k=1,2\) cases of the \(N=d+k\) formula, and C6 is the general statement.

### C1
- R1 (hypothesis): small \(N\) (1–4) directly.
- R2 (hypothesis): in the plane a line is determined by one angle mod \(\pi\), which may allow a one-dimensional argument.
- R3 (hypothesis): an induction on \(N\), or a pairing argument, matches \(\lfloor N^2/4\rfloor\).
- Feeds: C6 for \(d=2\) (C1 is exactly that case, by the S5 note below).

### C2
- R1 (hypothesis): the case \(m=2\) (two unit vectors in \(\mathbb{R}^1\)).
- R2 (hypothesis): small \(m\) (3, 4) settled directly; the pattern suggests the general argument.
- R3 (hypothesis): the orthogonality pattern forces a tridiagonal Gram matrix, and the dimension bound \(m-1\) forces a singularity condition constraining the consecutive inner products.
- R4 (hypothesis): an induction on \(m\), or a direct estimate, turns R3 into the sum bound.
- Feeds: (hypothesis) C3 and possibly C5. Whether and how is for the workers to find.

### C3
- R1 (hypothesis): \(d=1\) and \(d=2\) directly (\(d=2\) is C1 with \(N=3\)).
- R2 (hypothesis): some structure among \(d+1\) lines in \(\mathbb{R}^d\) (a graph of non-orthogonal pairs, or a chain) reduces to C2's hypotheses.
- R3 (hypothesis): pairs outside that structure are bounded trivially by \(\pi/2\).
- Feeds: C4 and C5 (the \(k=2\) analogue).

### C4 / C5
- R1 (hypothesis): an analogue of the C3 reduction with two "excess" lines.
- R2 (hypothesis): C4's concrete dimensions may yield to a rigorous computer-assisted argument (interval branch-and-bound over a compact parameter space) if no uniform argument is found; check the parameter-space size against the 10-minute limit.
- Feeds: C4 is C5 at \(d=3,4\). A C5 proof settles C4, but not the reverse.

### C6
- R1 (hypothesis): natural infinite families not covered above: \(d=2\) with all \(N\) (already C1), \(N\le 2d\), \(N\) a multiple of \(d\). The Literature agent checks which are known.
- R2: a standing Breaker/adversary lineage on small \((N,d)\), looking for violations with interval-certified margins.

## 6. Checker spec (for Breakers and Referees; the cells themselves are proofs)

- **Input format:** a text file whose first line is `d N`, followed by \(N\) lines of \(d\) rationals (`p/q` or integers), the spanning vectors (not necessarily unit).
- **Validation:** exactly \(N\) nonzero vectors of length \(d\).
- **Output:** `S in [lo, hi]`, `BOUND = <exact multiple of π/2>`, and one of `VIOLATION CERTIFIED` / `NO VIOLATION` / `UNDECIDED (interval overlaps bound)`.
- **Score:** \(S\) as an interval, and the margin \(S-\text{bound}\) as an interval.
- **Exactness:** \(|\langle x,y\rangle|/(\|x\|\|y\|)\) from exact rationals, comparing squares to avoid square roots where possible; arccos by interval arithmetic (mpmath `iv` or python-flint `arb`). This checker may use mpmath/flint, an exception to the stdlib-only default; say so in the brief.
- **Runtime:** instant for \(N\le 50\).
- **Random input generator:** random rational vectors, plus perturbations of the orthogonal-with-repeats configuration.
- **Hand-checkable cases:** coordinate axes with repeats (exact multiples of \(\pi/2\)); two lines at \(\pi/3\) and \(\pi/4\).
- **C1 bound:** \(\frac{\pi}{2}\lfloor N^2/4\rfloor\).
- **C2 variant:** checks the chain hypotheses exactly (orthogonality for \(|i-j|\ge2\), dimension \(m-1\)) and evaluates the chain sum.

## 7. Angle bank (one per FRESH / CONTRARIAN brief)

- `gram-matrix` (angle): work with the Gram matrix; PSD + rank ≤ d constraints on the inner products.
- `induction-on-dim` (angle): induct on \(d\), \(m\) or \(N\); project onto a hyperplane or orthogonal complement.
- `extremal-perturb` (angle): take a maximiser and derive first/second-order conditions by rotating one line.
- `concavity-majorise` (angle): concavity or convexity of \(t\mapsto\arccos t\) on the relevant range, and majorisation of the inner products.
- `averaging` (angle): average over a group action or random rotations; a probabilistic or integral representation of the angle.
- `graph-structure` (angle): the graph of non-orthogonal pairs (chains, trees, cycles), related to C2.
- `planar-angle-param` (angle): for C1, parametrise lines by angles mod \(\pi\).
- `small-cases-exact` (angle): settle small \(m\) or \(N\) exactly and extract the pattern.
- `interval-bnb` (angle): rigorous interval branch-and-bound for fixed small \((N,d)\) (C4).
- `obstruction-first` (angle): find why the naive bound (every pair \(\le\pi/2\)) fails and what must be charged.
- `sdp-dual` (angle): an SDP/LP relaxation with an exact dual certificate for fixed small cases.

## 8. Pitfalls

- **Lines, not vectors:** θ uses \(|\langle x,y\rangle|\), so signs are irrelevant and \(\theta\le\pi/2\). A proof that treats vector angles in \([0,\pi]\) proves something else.
- **Repetitions allowed:** coincident lines (θ = 0) are legal and occur in the conjectured optimum. Proofs must not assume distinct lines.
- **Ranges:**
  - C1 is every \(N\) in the plane.
  - C2 has \(m\ge2\) and vectors in \(\mathbb{R}^{m-1}\) (**not** \(\mathbb{R}^m\)).
  - C3 has **\(d\ge1\)**.
  - C5 has **\(d\ge2\)**.
  - C4 needs **both** instances.
- **C2 sums only consecutive pairs** \(i,i+1\), not all pairs.
- **C2 is about unit vectors**, and non-consecutive vectors are exactly orthogonal. Check degenerate cases such as consecutive vectors being equal or orthogonal.
- **Equality cases exist:** near-optimal configurations make floating-point "violations" meaningless. Any claimed violation must be interval-certified.
- **\(M(N,d)\) and \(k\):** \(N=d+k\) with \(0\le k\le d\) matches \(M=k\) only in that range; recompute \(M\) for other \(N\).
- **Cell order:** C4 (the concrete instances) comes **before** C5 (general \(d+2\)) in the official numbering.
- **"Not already covered above"** in C6: partial progress must be a family outside C1–C5. The plane (\(d=2\)) is already C1.

## 9. Problem-specific rules

- **Citing a published result for the statement you are asked to prove does not count.** Literature findings inform methods only; provers may not cite a published proof of their target cell.
- Unless a cell says otherwise, a complete proof is required.
- Computation: code included, < 10 min, exact or interval arithmetic or a bounded numerical error.
- Say clearly which cells are solved and which are partial.

## 10. Run notes

This skill is frozen during the run; the head doesn't edit it. New pitfalls, clarifications and problem-specific lessons go to `run/A/lessons.md`, which is copied into briefs for problem A only.

## 11. Checklist Part S seeds and branch notes

Part S seeds (from the statement only; referees and gate only):
- **S2 equality configuration:**
  - C1: the lines split as evenly as possible between two perpendicular directions (stated in C1's text).
  - C3–C6: the Setting's conjectured optimum, \(d\) mutually orthogonal lines each used \(\lfloor N/d\rfloor\) or \(\lceil N/d\rceil\) times.
  - C2: none given, so "unknown" unless a gated result supplies one.
- **S3 cases to cover:**
  - C1: every \(N\), both parities.
  - C2: every \(m\ge2\), vectors in \(\mathbb{R}^{m-1}\).
  - C3: every \(d\ge1\).
  - C5: every \(d\ge2\).
  - C4: both instances.
  - Everywhere: repetitions allowed; lines, not vectors.
- **S5 consistency** (arithmetic from the definitions):
  - \(\binom N2-M(N,2)=\lfloor N^2/4\rfloor\), so C1 is C6 at \(d=2\).
  - For \(N=d+k\) with \(0\le k\le d\), \(M(N,d)=k\); so C3 and C5 are the \(k=1,2\) cases.
  - C4 is C5 at \(d=3,4\).
- **S6 checkable values:** the Setting's value \((\binom N2-k)\pi/2\) at the orthogonal-with-repeats configuration, and \(\frac{\pi}{2}\lfloor N^2/4\rfloor\) at the balanced perpendicular split in the plane.

Branch notes (angles, each only into its own 2B lens):
- ALGEBRAIC (angle): the Gram matrix of spanning unit vectors, which is PSD with rank ≤ d.
- TOPOLOGICAL (angle): lines through the origin are points of \(\mathbb{RP}^{d-1}\); the configuration space is compact.
- ANALYSIS (angle): behaviour of \(t\mapsto\arccos|t|\); perturbation at a maximiser.
- NUMBER-THEORY (angle): the rounding \(N=qd+s\) in \(M(N,d)\); the parity of \(N\) in \(\lfloor N^2/4\rfloor\).
- DISCRETE (angle): the orthogonality graph of the lines; C2's hypothesis is a chain.
