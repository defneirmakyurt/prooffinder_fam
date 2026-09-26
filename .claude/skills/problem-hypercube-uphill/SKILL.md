---
name: problem-hypercube-uphill
description: Problem skill for "Uphill paths on the hypercube" (H), minimising U(Q_d), the number of uphill paths over labellings of the d-cube, for d = 3..9. Holds the verbatim statement, cells, hand-in format, cell typing, ladders, checker spec, angle bank and pitfalls. Load when opening problem H in a Proof Pursuit run.
---

# Problem H: Uphill paths on the hypercube

Letter code: `H` (cell ids `H-C1` … `H-C6`). Ledger: `run/H/`.

## 1. Verbatim statement

Label the vertices of the hypercube to make as few uphill paths as possible. IMO 2022 settled the grid; the cube is still open.

Let \(G\) be a finite simple graph on \(n\) vertices. A *labelling* of \(G\) is a bijection \(f\) from \(V(G)\) to \(\{1,2,\ldots,n\}\). Fix a labelling.

- A vertex \(v\) is a *valley* if every neighbour \(w\) of \(v\) has \(f(w)>f(v)\). An isolated vertex counts as a valley.
- An *uphill path* is a sequence \((v_1,v_2,\ldots,v_k)\) with \(k\ge 1\) in which \(v_1\) is a valley, \(v_i\) and \(v_{i+1}\) are adjacent for each \(i\), and \(f(v_1)<f(v_2)<\cdots<f(v_k)\). A valley on its own (\(k=1\)) counts as an uphill path.

Let \(U(G)\) be the smallest possible number of uphill paths, taken over all labellings of \(G\).

IMO 2022 Problem 6 asks for \(U\) of the \(n\times n\) grid graph. The answer is \(2n^2-2n+1\).

This column asks about the \(d\)-dimensional hypercube \(Q_d\). Its vertex set is \(\{0,1\}^d\), and two vertices are adjacent when they differ in exactly one coordinate. \(Q_d\) has \(2^d\) vertices and \(d\cdot 2^{d-1}\) edges.

### Cells

| Cell | Title | Points | Checking | Verbatim text |
|---|---|---|---|---|
| C1 | \(U(Q_3)\) and \(U(Q_4)\) | 1 | checked instantly | The two smallest interesting cubes: \(Q_3\) has 8 vertices and 12 edges, \(Q_4\) has 16 vertices and 32 edges. Determine \(U(Q_3)\) and \(U(Q_4)\). |
| C2 | \(U(Q_5)\) | 2 | checked instantly | \(Q_5\) has 32 vertices and 80 edges. Determine \(U(Q_5)\). |
| C3 | \(U(Q_6)\) | 3 | checked instantly | \(Q_6\) has 64 vertices and 192 edges. Determine \(U(Q_6)\). |
| C4 | \(U(Q_7)\) and \(U(Q_8)\) | 5 | checked instantly | Two larger cubes: \(Q_7\) has 128 vertices and 448 edges, \(Q_8\) has 256 vertices and 1024 edges. Determine \(U(Q_7)\) and \(U(Q_8)\). |
| C5 | Bounds for \(U(Q_9)\) | 8 | judged | \(Q_9\) has 512 vertices and 2304 edges. The best bounds known to the organisers are \(2368\le U(Q_9)\le 2400\); the lower bound is unpublished. Improve either one: prove that \(U(Q_9)\ge 2369\), or exhibit a labelling of \(Q_9\) with at most 2399 uphill paths. |
| C6 | \(U(Q_9)\) | 13 | judged, **open question** | The same cube, settled completely. Determine \(U(Q_9)\) exactly, with proof of both bounds. |

## 2. Definitions and notation (exactly as given)

- *Labelling:* a bijection \(f:V(G)\to\{1,\ldots,n\}\).
- *Valley:* \(v\) with \(f(w)>f(v)\) for every neighbour \(w\). An isolated vertex counts as a valley.
- *Uphill path:* a sequence \((v_1,\ldots,v_k)\), \(k\ge1\), with \(v_1\) a valley, consecutive vertices adjacent, and labels strictly increasing. A lone valley counts.
- \(U(G)\): the minimum number of uphill paths over all labellings.
- \(Q_d\): vertices \(\{0,1\}^d\); adjacent iff the strings differ in exactly one coordinate. \(2^d\) vertices, \(d2^{d-1}\) edges.

## 3. Hand-in format

| Cell | What to hand in | Artefact files | Judges require |
|---|---|---|---|
| C1–C4 | "the values, and for each value an explicit labelling that attains it as a list of the \(2^d\) vertices in increasing label order, written as 0/1 strings" | `Q<d>.txt` per value: \(2^d\) lines, line \(i\) = the vertex with label \(i\) | "marked correct on the values alone, but a value with no labelling behind it will not survive the later cells, which build on the construction" |
| C5 | "either a labelling of \(Q_9\) in the same format, whose uphill paths will be counted mechanically, or a proof of the lower bound" | `Q9.txt` with ≤ 2399 uphill paths, or a lower-bound proof ≥ 2369 (+ code) | mechanical count, or a judged proof |
| C6 | "1. the value; 2. an explicit labelling that attains it, in the same format; 3. a proof that no labelling gives fewer uphill paths" | value, `Q9.txt`, proof (+ code) | all three |

Global rule (verbatim): "A lower-bound proof may be computer-assisted. If it is, include the code; it must run in under 10 minutes on a laptop, and you must explain why the computation proves the bound. Say clearly which cells you consider solved and which are partial."

## 4. Cell typing and exact targets

| Cell | Type | Tier guess + reason | Exact target |
|---|---|---|---|
| C1 | exact value with an instant check | T0: \(Q_3\) has 8! labellings (brute force plainly feasible); \(Q_4\) has 16!, so it needs symmetry/search, and the tier may rise | the integers \(U(Q_3)\), \(U(Q_4)\), each with an attaining labelling and lower-bound evidence |
| C2 | exact value with an instant check | T1 | \(U(Q_5)\) + labelling + lower-bound evidence |
| C3 | exact value with an instant check | T1–T2 | \(U(Q_6)\) + labelling + lower-bound evidence |
| C4 | exact value with an instant check | T2: both values needed | \(U(Q_7)\), \(U(Q_8)\) + labellings + lower-bound evidence |
| C5 | scored construction **or** lower bound | T2 | a labelling of \(Q_9\) with ≤ 2399 uphill paths, **or** a proof that \(U(Q_9)\ge2369\) |
| C6 | exact value + optimality | T3: open | \(U(Q_9)\) exactly: a value, a labelling, and a proof of the lower bound |

Instant-check cells are judged on the value alone. A wrong value costs the cell, so the head's rule applies: without a proved lower bound, submit a value only when at least three independent lineages plateau at it. Record the status as `BEST-FOUND` in that case, or `EXHAUSTIVE-WITHIN-CLASS` / `COMPUTER-VERIFIED` where earned.

## 5. Decomposition ladders (hypotheses, not facts)

Lower cells are the way in: they validate the checker, the search methods and any lower-bound technique at sizes where exhaustive checking is possible, before \(Q_9\).

### C1
- R1: the checker agrees with hand counts on \(Q_1\), \(Q_2\) and random labellings (cross-tested).
- R2 (hypothesis): \(U(Q_3)\) by exhaustive search over all 8! labellings, with no symmetry reduction needed. This makes the lower bound COMPUTER-VERIFIED.
- R3 (hypothesis): an upper bound for \(Q_4\) by local search / structured labellings.
- R4 (hypothesis): a lower bound for \(Q_4\) by exhaustive search with *proved* symmetry breaking (the automorphism group of \(Q_d\) has order \(2^d d!\)), or by SAT/ILP with a checkable certificate, or by a proof.
- Feeds: constructions and lower-bound methods reused for C2–C6.

### C2–C4
- R1 (hypothesis): structured labellings of \(Q_d\) built from labellings of \(Q_{d-1}\) (product \(Q_d=Q_{d-1}\times K_2\)) give good upper bounds; test against search.
- R2 (hypothesis): local search (swap moves, fast incremental DP recount) finds the plateau values.
- R3 (hypothesis): lower-bound evidence gets weaker with \(d\): exhaustive is hopeless beyond small \(d\), so rely on SAT/ILP with certificates, a proof, or ≥ 3 independent plateaus (BEST-FOUND).
- Feeds: the sequence \(U(Q_3..Q_8)\) suggests the structure for \(Q_9\) (hypothesis).

### C5 / C6
- R1: upper route: search or construction for ≤ 2399; any artefact is scored by the checker only.
- R2: lower route: a lower-bound argument for ≥ 2369, possibly computer-assisted; the soundness argument must be written.
- Split the budget between both routes; don't give the whole cell to one side.

## 6. Checker spec

- **Input format:** a text file with exactly \(2^d\) non-empty lines. Each line is a 0/1 string of length \(d\). Line \(i\) (1-based) is the vertex with label \(i\). \(d\) is inferred from the line length and must match an optional `--d` argument.
- **Validation:** every line has the same length \(d\ge1\) and only the characters `0`/`1`; there are exactly \(2^d\) lines; all are distinct. Trailing whitespace and a final newline are tolerated; anything else is FAILED.
- **Output:** `VERIFIED <count>` (exit 0) or `FAILED: <reason>` (exit 1).
- **Score:** the number of uphill paths, from the definitions: valleys, then all strictly increasing adjacent sequences starting at a valley, the single-vertex path included.
- **Exactness:** Python integers.
- **Runtime:** \(Q_9\) well under 10 s.
- **Random input generator for cross-testing:** uniform random permutations of \(\{0,1\}^d\) for \(d=1..9\), plus structured orders (lexicographic, reverse, by Hamming weight, Gray code).
- **Hand-checkable cases:** all labellings of \(Q_1\) and \(Q_2\), which builders compute by hand; the results are not given here.
- **Brute-force cross-check:** explicit path enumeration by DFS (for small \(d\)) against the DP count.

## 7. Angle bank (one per FRESH / CONTRARIAN brief)

- `weight-order` (angle): labellings ordered by Hamming weight, with a tie-break rule to optimise.
- `recursive-product` (angle): build a \(Q_d\) labelling from two \(Q_{d-1}\) labellings via \(Q_d=Q_{d-1}\times K_2\).
- `anneal-swaps` (angle): simulated annealing on permutations with swap moves and an incremental DP recount.
- `few-valleys` (angle): a structural assumption: fix the number and position of valleys first, then order the rest.
- `symmetric-labelling` (angle): labellings invariant or near-invariant under a subgroup of \(\mathrm{Aut}(Q_d)\).
- `sat-ilp-lower` (angle): encode "≤ T uphill paths" as SAT/ILP for small \(d\); UNSAT with a DRAT proof gives a lower bound.
- `exhaustive-symbreak` (angle): exhaustive search over canonical labellings with proved symmetry breaking.
- `grid-lower-bound-style` (angle): adapt the *style* of lower-bound argument used for the grid (IMO 2022 P6). The Literature agent must find that argument; don't assume it transfers.
- `small-cases-pattern` (angle): exact values for small \(d\), then guess the structure and generalise.
- `obstruction-first` (angle): what forces uphill paths (per valley, per edge) and how to count them.

## 8. Pitfalls

- **A lone valley counts** (\(k=1\)); the count is over *sequences*, so different routes to the same endpoint count separately.
- **Paths must start at a valley.** Increasing paths from non-valleys don't count.
- **Strict increase** in labels; labels are a bijection onto \(1..n\) (no ties, no zero).
- **Hand-in order:** vertices listed in **increasing label order** (line 1 = label 1), not a list of labels by vertex. Strings are exactly \(d\) characters with leading zeros.
- **Bit order inside a string** is a relabelling of coordinates, so the count is invariant, but keep one convention everywhere.
- **Two values in C1 and C4:** both must be right.
- **C5 thresholds:** a labelling with **≤ 2399**, or a proof of **≥ 2369**. Matching 2400 or 2368 earns nothing.
- **"Exhaustive"** needs a defined search space and a written soundness argument for every symmetry reduction; a time-limited search is not a lower bound.
- **Scores:** never copy a score from a report; re-score with the accepted checker.

## 9. Problem-specific rules

- C1–C4 are marked on values alone, but each value must have an explicit attaining labelling.
- A computer-assisted lower bound must include code, run in < 10 min, and explain why the computation proves the bound.
- The organisers' bounds \(2368\le U(Q_9)\le2400\) are given in the statement; the lower bound is unpublished.
- Say clearly which cells are solved and which are partial.

## 10. Run notes

This skill is frozen during the run; the head doesn't edit it. New pitfalls, clarifications and problem-specific lessons go to `run/H/lessons.md`, which is copied into briefs for problem H only.

## 11. Checklist Part S seeds and branch notes

Part S seeds (from the statement only; referees and gate only):
- **S2 extremal values.**
  - C1–C4, C6: the statement gives no values, so the optimum is "unknown".
  - C5: the organisers' bounds are \(2368\le U(Q_9)\le 2400\), with the lower bound unpublished.
- **S3 cases to cover.**
  - Lone valleys count as paths.
  - Paths are counted as sequences.
  - Labels are a bijection onto \(1..2^d\).
  - C1 and C4 each need both values.
  - An exact value needs both halves: an attaining labelling and a lower bound over **all** labellings.
- **S5 consistency.**
  - Every value handed in must equal the checker's count on the submitted labelling.
  - A lower-bound argument claimed for general \(d\) must agree with every verified small value.
- **S6 checkable instances:** the checker's hand-computed \(Q_1\), \(Q_2\) cases, once the checker-builders have produced them.

Branch notes (angles, each only into its own 2B lens):
- ALGEBRAIC (angle): the automorphism group of \(Q_d\) (order \(2^d d!\)), for symmetry breaking or symmetric labellings.
- TOPOLOGICAL (angle): the labelling as a discrete Morse-like function; valleys as local minima.
- ANALYSIS (angle): averaging or probabilistic bounds over random labellings.
- NUMBER-THEORY (angle): Hamming weight and parity classes of \(\{0,1\}^d\).
- DISCRETE (angle): a labelling as an acyclic orientation or linear extension; the recursion \(Q_d=Q_{d-1}\times K_2\).
- COMPUTATIONAL (angle, searchers): SAT/ILP for small \(d\), annealing, exhaustive search with proved symmetry breaking.
