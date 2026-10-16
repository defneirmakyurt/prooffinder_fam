# Referee verdict — H-C1-007 (MODE VERIFY, SUBJECT H-C1-006)

```
VERDICT: ACCEPT
STATEMENT MATCH: yes
FIRST PROBLEM: none
```

Target (verbatim, from `inbox/target.md`): "The two smallest interesting cubes: Q_3 has 8
vertices and 12 edges, Q_4 has 16 vertices and 32 edges. Determine U(Q_3) and U(Q_4)."
Hand-in: "the values, and for each value an explicit labelling that attains it as a list of
the 2^d vertices in increasing label order, written as 0/1 strings."

Subject's answer: **U(Q_3) = 14, U(Q_4) = 34**, with `Q3.txt` and `Q4.txt`.
Re-scored by `inbox/checker/verify.py`: `VERIFIED 14`, `VERIFIED 34`.

---

## 1. Checklist pass

### Part G

| item | mark | reason |
|---|---|---|
| G1 | PASS | The first line of `proof.md` is exactly "U(Q_3) = 14 and U(Q_4) = 34"; all five definitions are restated verbatim from `statement.md`; both halves (attaining labelling + lower bound over all labellings) are supplied for both d. No extra hypothesis anywhere: Steps 1–5 are for an arbitrary finite simple graph, Step 6 adds only "no isolated vertex" (which Q_3, Q_4 satisfy), Step 7 is stated only for d ∈ {3,4}. "No result is claimed for any d outside {3,4}." |
| G2 | PASS | No unexplained "clearly / similarly / obviously / routine / by symmetry". The two combinatorial identities rest on maps whose well-definedness, injectivity and surjectivity are each written out (Step 2). Step 3 states its induction and its base case. Step 6 says which inequality in which chain becomes an equality and why each summand is non-negative. Step 7 does the two arithmetic cases separately rather than "similarly". (One compression, Step 4's "by exactly the argument of Step 2"; see §2, it is legitimate — the referenced argument is complete and the extra re-indexing is spelled out.) |
| G3 | PASS | k = 1 (lone valley) is the `[down(v)=0]` term of Step 2 and the `\|Val\|` term of Step 4. Step 3's induction base (the vertex with f = 1) is written out and uses no hypothesis. Step 6's hypothesis "no isolated vertex" is checked for Q_d in Step 7 (deg = d ≥ 3 ≥ 1). d = 3 and d = 4 are each treated. Step 6 handles v_0 ∈ M (ruled out in 6(a)) and down(v) = 0 for v ∈ R (ruled out by uniqueness of the valley). |
| G4 | PASS | Step 6 derives `\|E\|+1 = P ≥ \|Val\|+\|E\| ≥ 1+\|E\|` and correctly concludes both are equalities; `sum_v (N(v)−1)·up(v) = 0` with every term ≥ 0 (Step 3) gives N(v)=1 whenever up(v) ≥ 1. Strictness is used exactly where needed: in 6(d) the count t = down(v) is ≥ 1 strictly (v is not the unique valley), so "t integers each ≥ 1 summing to 1" forces t = 1. |
| G5 | PASS | No parametrised construction is claimed; two explicit labellings are handed in and both are re-scored exactly (checker, subject code, and my own literal enumerator). |
| G6 | PASS | No circularity: Steps 1–5 are proved from the definitions only; Steps 6–7 use only Steps 1–5; Step 8 is an exhibit. The only citation is the *general* inequality U(G) ≥ \|E\|+1 (IMO 2022 P6 lower-bound half, Bajnok arXiv:2509.19303) and it is **re-proved in full** as Steps 1–5. It is not the cell's statement (it gives 13 and 33, both short of the answer); the step that closes the gap, Steps 6–7, is the subject's own. |
| G7 | PASS | All code is stdlib-only and pure integer arithmetic (no float anywhere in `uphill.py`, `q3_exhaustive.py`, `identity_check.py`; `q4_upper.py` uses `random` only to pick moves, and its output is re-scored exactly). Longest subject run measured here: 1.12 s (`identity_check.py`) — far under 10 min. The only computer-assisted ingredient the *proof* depends on is the count of two single labellings, which is a finite check of exactly what is claimed, and Step 8 also hand-computes the Q_3 count (all eight N-values plus the neighbour lists). The Q_3 exhaustive run is over all 8! permutations with no symmetry reduction, so its "search space = all labellings" reduction is trivially sound; it is corroboration only, the Q_3 lower bound being proved by hand. `q4_upper.py` is explicitly flagged as upper-bound-only and nothing rests on its optimality. |
| G8 | PASS | Step 5 is explicitly parenthesised as the known IMO 2022 P6 lower-bound step with a precise reference (Bajnok, arXiv:2509.19303, Problem 6 solution), and `claims.md` marks it "PROVED here; also KNOWN". Step 6's "exactly one valley" half is likewise attributed, the down-degree count is claimed as new. New work (Steps 6–8) is cleanly separated. Caveat: the proof also points to `out/sources.md`, which is not in my inbox, so I could not open it; the inline arXiv reference is precise enough to stand on its own. |
| G9 | PASS | `proof.md` says "No result is claimed for any d outside {3,4}" and marks the closing Remark "NOT part of the cell … not used above". `claims.md` labels each row PROVED / COMPUTER-VERIFIED / NOT CLAIMED, including "Any value of U(Q_d) for d ≥ 5 — NOT CLAIMED". |

### Part S

| item | mark | reason |
|---|---|---|
| S1 | PASS | Both values given. (a) `inbox/checker/verify.py Q3.txt --d 3` → `VERIFIED 14`; `… Q4.txt --d 4` → `VERIFIED 34`; independently re-scored by my own literal path enumerator (§3) → 14 and 34. (b) Lower bounds U(Q_3) ≥ 14 and U(Q_4) ≥ 34 are proved for an arbitrary labelling in Steps 5+7. |
| S2 | N/A | The statement gives no value for U(Q_3) or U(Q_4), so there is no published extremal value to match. Tightness was instead tested on the instances where the *cited* bound is known to be attained (§4). |
| S3 | PASS | Lone valley counted (Step 2 `[down(v)=0]`, Step 4 `\|Val\|`); paths counted as *sequences*, so two routes to the same endpoint count twice — confirmed by my enumerator, which stores full vertex tuples and finds 14 / 34 distinct tuples; labels are a bijection onto 1..2^d (checker's parse rejects repeats/wrong counts, and my scorer asserts `sorted(order) == range(2^d)`); both d = 3 and d = 4 done; the lower half is quantified over **all** labellings — Steps 5–7 fix an arbitrary f and never restrict it. |
| S4 | PASS | Paths start at a valley and labels strictly increase — both re-validated per-path by my enumerator. Hand-in format: both files have exactly 2^d lines, each of exactly d characters from {0,1} with leading zeros, in increasing label order (`od -c` on Q3.txt shows `000\n001\n…`, no stray bytes). No "exhaustive search" is used as the lower bound: for Q_3 the exhaustive run is complete with *no* symmetry reduction (all 8! = 40320, so no soundness argument is needed), and the Q_3/Q_4 lower bounds are hand proofs. The local search `q4_upper.py` is labelled "proves nothing about optimality". No score is copied: I re-ran the checker myself. |
| S5 | PASS | Every handed-in value equals the accepted checker's count (14, 34). The general bound the proof states for all d, `U(Q_d) ≥ d·2^{d−1}+2 for d ≥ 3` (Remark), agrees with both values (12+2 = 14, 32+2 = 34) and correctly *excludes* d = 2, where I verified exhaustively that U(Q_2) = 5 = \|E\|+1 is attained — so the argument is neither over-strong nor vacuous. No lower cells exist. |
| S6 | PASS | Hand cases re-derived and reproduced: Q_1 (`0`,`1`) → the 2 uphill paths (0), (0,1) → 2 = \|E\|+1; Q_2 (`00`,`01`,`10`,`11`) → N = 1,1,1,2, total 5 = \|E\|+1. My exhaustive runs over all 2! and 4! labellings give minima 2 and 5, matching. |

No FAIL, no missing item.

---

## 2. Line-by-line re-derivation — why each step holds

**Notation block.** `up(v)+down(v) = deg(v)` holds because f is injective, so each neighbour
w of v satisfies exactly one of f(w) > f(v), f(w) < f(v). `v is a valley iff down(v) = 0` is
the definition verbatim. `P = sum_v N(v)` holds because every uphill path (v_1,…,v_k) has a
well-defined last entry v_k, so the paths are partitioned by their last vertex. Correct.

**Step 1 — `sum_v up(v) = |E| = sum_v down(v)`.** Holds. Each edge {u,v} with f(u) < f(v) is
counted in `up` only at u (up(w) counts edges incident with w whose other end is larger, and
the only incident endpoints are u and v; at v the other end u is smaller) and in `down` only
at v. Both sums are therefore edge-counts with multiplicity one. Injectivity of f is used and
is available. Verified computationally on 8000 random labellings and all 8! of Q_3.

**Step 2 — recurrence `N(v) = [down(v)=0] + sum_{w~v, f(w)<f(v)} N(w)`.** Holds. The k = 1
term is exactly the definition (the one-term sequence (v) is an uphill path iff v is a
valley). For k ≥ 2 the map φ(v_1,…,v_{k−1},v) = (v_{k−1},(v_1,…,v_{k−1})) is checked three
ways in the text and each check is valid:
*into B* — deleting the last entry of an uphill path leaves a sequence with the same first
vertex (still a valley), a subset of the adjacencies, and a sub-chain of the strict
inequalities, so it is an uphill path; and v_{k−1} ~ v with f(v_{k−1}) < f(v) from the
path's own data;
*injective* — v is fixed, so the pair determines the sequence;
*surjective* — appending v to an uphill path ending at w ~ v with f(w) < f(v) restores all
three defining conditions (v_1 unchanged, adjacency w ~ v, chain extended by f(w) < f(v)).
No hidden hypothesis. Note that the down-neighbours are counted with multiplicity one
because the graph is simple.

**Step 3 — `N(v) ≥ 1`.** Holds. Strong induction on f(v) is legitimate since f takes values in
a finite well-ordered set. Base: the vertex with f = 1 has every neighbour larger, so
down = 0 and the indicator term gives N ≥ 1 with no appeal to the hypothesis. Inductive step:
if down(v) ≥ 1 pick any down-neighbour w; all terms of Step 2 are cardinalities, hence ≥ 0,
so N(v) ≥ N(w) ≥ 1. No division, no extremum assumed.

**Step 4 — `P = |Val| + sum_v N(v)·up(v)`.** Holds. Length-1 paths ↔ valleys, giving |Val|.
For length ≥ 2: by Step 2 the paths of length ≥ 2 ending at a **fixed** v biject with
{(w,Q) : w ~ v, f(w) < f(v), Q uphill ending at w}. The set of *all* length-≥2 paths is the
disjoint union over v of these (unique last vertex), so its size is
`sum_v sum_{w~v, f(w)<f(v)} N(w)`. Re-indexing this double sum by the edge (w,v) read from
the *lower* end gives `sum_w N(w)·#{x ~ w : f(x) > f(w)} = sum_w N(w)·up(w)`. This is the
one place where the proof compresses ("by exactly the argument of Step 2"), but the
referenced argument is complete, the extra ingredient (unique last vertex) is stated, and the
re-indexing is a finite Fubini on a finite set — so this is a citation of proved work, not a
gap. Verified computationally on 8000 random labellings, all 8! of Q_3, and 4000 random
graphs.

**Step 5 — `P ≥ |E| + |Val| ≥ |E| + 1`.** Holds. `N(v) ≥ 1` (Step 3) and `up(v) ≥ 0` give
`N(v)·up(v) ≥ up(v)` (multiplying an inequality by a non-negative number — correct
direction). Summing and using Step 4, then Step 1, gives `P ≥ |Val| + |E|`. `|Val| ≥ 1`
because the vertex with f = 1 is a valley (1 is the least value and f is injective). This is
the cited IMO step, re-proved here from scratch; the citation is a general graph lemma, not
the cell's statement.

**Step 6 — structure at equality.** Holds. `P = |E|+1` squeezes the chain
`|E|+1 = P ≥ |Val|+|E| ≥ 1+|E|`, so both are equalities. Second equality ⇒ |Val| = 1. First
equality ⇒ `sum_v (N(v)−1)·up(v) = 0` with every summand ≥ 0 (Step 3 gives N(v)−1 ≥ 0,
up(v) ≥ 0) ⇒ each summand is 0 ⇒ N(v) = 1 whenever up(v) ≥ 1. (a) v_0 ∉ M because
up(v_0) = deg(v_0) − 0 = deg(v_0) ≥ 1, which is where "no isolated vertex" is used and is the
only place it is needed; so {v_0}, M, R is a genuine partition and |R| = n−1−m.
(b) down(v_0) = 0 by definition of valley. (c) v ∈ M ⇒ up(v) = 0 ⇒ down(v) = deg(v).
(d) v ∈ R ⇒ up(v) ≥ 1 ⇒ N(v) = 1, and v ≠ v_0 with v_0 the unique valley ⇒ down(v) ≥ 1 ⇒ the
indicator in Step 2 is 0 ⇒ 1 = sum of down(v) terms each ≥ 1 ⇒ down(v) = 1 (a sum of t ≥ 1
integers each ≥ 1 is ≥ t, so t = 1). Summing down over the three blocks and applying Step 1
gives `|E| = sum_{v∈M} deg(v) + (n−1−m)`. I tested all three conclusions on 1376 *actual*
equality instances found among 4000 random graphs — all held (§3E).

**Step 7 — no equality labelling for d = 3, 4.** Holds. Q_d is simple, finite, d-regular with
d ≥ 3 ≥ 1, so Step 6 applies. Substituting n = 2^d, |E| = d·2^{d−1}, deg ≡ d:
`d·2^{d−1} = m·d + 2^d − 1 − m`, i.e. `(d−1)m = d·2^{d−1} − 2^d + 1 = 2^{d−1}(d−2) + 1`
(since d·2^{d−1} − 2·2^{d−1} = 2^{d−1}(d−2)). d = 3: 2m = 5, impossible (parity). d = 4:
3m = 17, impossible (17 ≡ 2 mod 3). Both arithmetic identities check: 4·1+1 = 5, 8·2+1 = 17.
Hence P ≠ |E|+1; with Step 5's P ≥ |E|+1 and P ∈ Z this forces P ≥ |E|+2, i.e. 14 and 34. No
case is skipped — m ranges over all non-negative integers and the argument excludes every
one. Note the argument needs no bound m ≤ n, since the equation already has no solution in Z.

**Step 8 — matching labellings.** Holds, and I re-verified it three independent ways: the
accepted checker (`VERIFIED 14`, `VERIFIED 34`), the subject's own two counters, and my own
enumerator that materialises every uphill path as an explicit tuple and re-validates each
tuple against the raw definition. Both files are bijections onto {0,1}^d. The Q_3
hand-computation in the text is correct: with 000,001,010,011,101,110,100,111 ↦ 1..8 the
neighbour lists quoted are right and N = 1,1,1,2,1,1,3,4, total 14. (The coordinate
convention "leftmost = coordinate d−1" is immaterial: reversing coordinate order is a graph
automorphism of Q_d, and the checker's `int(r,2)` reading agrees with it anyway.)

**Conclusion.** Combining Step 7 (lower) and Step 8 (upper) gives equality. Sound.

**Closing Remark** (flagged as outside the cell, not used): also correct as far as it goes —
`d−2 ≡ −1 mod (d−1)` so the condition is `2^{d−1} ≡ 1 mod (d−1)`; and `n | 2^n − 1 ⇒ n = 1`
by the least-prime-factor/order argument given, which is valid (n | 2^n−1 forces n odd; for
the least prime p | n, ord_p(2) | gcd(n, p−1) = 1 since every prime factor of p−1 is < p).
I confirmed numerically that d = 2 is the only d in 2..40 passing the divisibility test.
Nothing in the cell's result depends on this.

**Unjustified / circular / false steps found: none.**

---

## 3. Numerical sanity, re-runs, and my own counterexample search

All code and logs are under `out/cex/`. PYTHON = `/Users/raducucu/bainsahackathon/.venv/bin/python3`.
All arithmetic is exact Python integers; no floating point occurs in any proof-bearing
computation. (`out/cex/hunt33.py` uses a float only for a simulated-annealing acceptance
coin; every reported objective value is an exact integer, and the hunt is evidence, not
proof.)

### Re-runs of the subject's code (`out/cex/log_subject_code.txt`, `log_checker.txt`)

| run | result | measured `real` |
|---|---|---|
| `checker/verify.py subject/Q3.txt --d 3` | `VERIFIED 14` | 0.05 s |
| `checker/verify.py subject/Q4.txt --d 4` | `VERIFIED 34` | 0.06 s |
| same two with plain stdlib `python3` | `VERIFIED 14`, `VERIFIED 34` | — |
| `uphill.py ../Q3.txt 3` | `uphill_paths=14 (recurrence) =14 (explicit enumeration) valleys=1` | 0.03 s |
| `uphill.py ../Q4.txt 4` | `uphill_paths=34 (recurrence) =34 (explicit enumeration) valleys=2` | 0.02 s |
| `q3_exhaustive.py` | 40320 labellings, min = 14, distribution (14,7104),(16,14112),… | 0.13 s |
| `identity_check.py` | I1, I2 hold on 2000 random labellings for each d = 2..5 and on all 8! of Q_3 | 1.12 s |
| `q4_upper.py 4 34` | best found 34, order = the submitted `Q4.txt` | 0.04 s |

Every claim in `claims.md` that names a run reproduces exactly, including the count 7104.

### My own checks (`out/cex/independent.py`, `log_independent.txt`, 0.75 s)

- **(A) Literal enumeration.** I built every uphill path of `Q3.txt` / `Q4.txt` as an explicit
  vertex tuple and re-validated each tuple against the raw definition (first vertex a valley,
  consecutive vertices adjacent, labels strictly increasing), plus no duplicates and closure
  under extension. Result: **14** paths for Q_3 (1 valley), **34** for Q_4 (2 valleys). This
  confirms the values without using the recurrence at all.
- **(C) Checklist S6 hand cases.** All 2! labellings of Q_1 → min 2 = |E|+1; all 4! of Q_2 →
  min 5 = |E|+1, distribution {5:16, 6:8}. Identity labellings reproduce the hand counts.
- **(B) Q_3 exhaustive, my own implementation.** All 8! = 40320 labellings, min = 14,
  distribution (14,7104),(16,14112),(17,6720),(18,4704),(19,576); **no labelling with ≤ 13**.
  15 does not occur at all. Cross-checked against the literal enumerator every 1009th
  permutation.
- **(D) Q_4 local search.** 400 random restarts with full best-improvement transposition
  descent: best 34, never below.
- **(E) Steps 1,3,4,5,6 on random graphs.** 4000 random simple graphs on 2..8 vertices with no
  isolated vertex, each with a random labelling, scored by the literal enumerator. Step 1,
  Step 3, Step 4 and Step 5 held in all 4000. Among them **1376 hit the equality case
  P = |E|+1**, and in every one of those all three Step-6 conclusions held: |Val| = 1;
  N(v) = 1 whenever up(v) ≥ 1; and |E| = (n−1−m) + sum_{v: up(v)=0} deg(v). Step 6 is the one
  new ingredient of the proof, and this is a direct stress test of it on non-vacuous data.

### Independent exhaustive lower bound (`out/cex/bnb_q4.py`, `log_bnb.txt`, 287.19 s total)

Branch and bound over **all** (2^d)! labellings (orderings), using only elementary bounds
derived from scratch (N(u) ≥ partial[u] + dT(u) and N(u) ≥ 1), with and without a stated
symmetry reduction. Scorer cross-checked against the literal enumerator on 300 random
labellings for each d = 2,3,4.

- Positive controls: d = 3 target 15 → **COMPLETED, found** a 14-labelling; d = 4 target 35 →
  **COMPLETED, found** a 34-labelling (a *different* one from the subject's:
  0000,0001,0010,0100,0111,1000,1111,1011,0011,1101,0101,1001,1110,0110,1010,1100). So the
  machinery does find witnesses when they exist, and U(Q_4) ≤ 34 is confirmed independently.
- d = 3 target 14, with symmetry reduction: **COMPLETED**, none found ⇒ U(Q_3) ≥ 14 (697 nodes).
- d = 3 target 14, **no** symmetry reduction at all: **COMPLETED**, none found ⇒ U(Q_3) ≥ 14
  (13601 nodes). Fully independent confirmation of the d = 3 lower bound.
- d = 4 target 34, both with and without reduction: **PARTIAL** — 60,000,000-node cap hit
  after 143.4 s and 141.8 s respectively. **These two runs prove nothing** and nothing in this
  verdict rests on them. The reason is instructive and corroborates the proof: my bound
  saturates at exactly |E| + 1 = 33 (it is an incremental form of Step 5), so a B&B that does
  not know Step 6 cannot cut at 34. This is precisely the +1 that Steps 6–7 supply, and it
  confirms that closing the gap is genuine new work rather than a restatement of the cited
  result.

### Stochastic counterexample hunt (`out/cex/hunt33.py`, `log_hunt33.txt`, 27.29 s)

Simulated annealing on transpositions, exact integer objective.
- Q_3, target ≤ 13: 200 restarts × 4000 steps, 700,133 exact evaluations. Best = **14**, not
  reached. Lowest values ever visited: 14, 16, 17, 18.
- Q_4, target ≤ 33: 400 restarts × 12000 steps, 4,499,578 exact evaluations. Best = **34**,
  not reached. Lowest values ever visited: 34, 37, 38, 39.
- Remark check: among d = 2..40, the only d for which Step 6's divisibility condition can hold
  is d = 2. Consistent with the Remark.

**No counterexample found to the statement or to any intermediate claim.**

---

## 4. Equality-case test

Part S records the extremal values as *unknown*, so there is no published extremal
configuration to match; I instead tested tightness where the argument predicts it.

- **Step 5 is tight and not over-strong.** For Q_2 the equality case is *not* excluded by
  Step 7's divisibility ((d−1)m = 2^{d−1}(d−2)+1 reads 1·m = 1, m = 1), and my exhaustive run
  over all 4! labellings gives U(Q_2) = 5 = |E|+1 exactly. Likewise Q_1: U = 2 = |E|+1. So the
  proof's machinery does *not* force |E|+2 everywhere.
- **Step 5's equality case occurs in bulk**: 1376 of 4000 random graph/labelling pairs attain
  P = |E|+1, and Step 6's conclusions hold in every one.
- **Step 6/7's conclusion is tight for the cube.** The submitted labellings attain exactly
  |E|+2 (14 and 34), i.e. one more than Step 5's bound — so the lower bound and the
  construction meet, and neither has slack. Note `Q4.txt` has **two** valleys, so it does not
  even try to be an equality configuration for Step 6; Step 5 already gives it
  P ≥ 32 + 2 = 34, consistent.
- For Q_3 the exhaustive distribution shows 14 is attained by 7104 of the 40320 labellings and
  that 13 and 15 never occur.

## 5. Cross-cell consistency

No lower cells exist for H-C1. Two external consistency checks instead
(`out/cex/grid_imo.py`, `log_grid.txt`, 0.74 s):

- The statement quotes IMO 2022 P6: U(n×n grid) = 2n²−2n+1. Exhaustively over all 4!
  labellings of the 2×2 grid → min **5** = 2·4−4+1; over all 9! = 362880 labellings of the
  3×3 grid → min **13** = 2·9−6+1. The subject's and the checker's reading of "uphill path"
  therefore reproduces the published value, so the counting semantics are right.
- Both grid values equal |E|+1, so the cited Step 5 is attained there — the proof's Steps 6–7
  correctly identify the cube (not the grid) as the case where the bound fails to be tight.
- The proof's own out-of-range Remark, U(Q_d) ≥ d·2^{d−1}+2 for d ≥ 3, agrees with both
  in-range values (14 = 12+2, 34 = 32+2) and correctly exempts d = 2, where U(Q_2) = 5 = |E|+1.

## 6. Other issues

- Presentational only: Step 4's "by exactly the argument of Step 2" compresses a re-indexing
  of a double sum. The referenced argument is complete and the compression is valid; no fix
  needed, but a single sentence ("summing the Step-2 bijection over all last vertices and
  re-indexing the resulting double sum by the lower endpoint of each edge") would remove the
  last trace of a "similarly".
- `proof.md` Step 5 points at `out/sources.md`, which is not in my inbox, so I could not open
  it. The inline reference (Bajnok, arXiv:2509.19303, Problem 6 solution) is precise on its
  own, and since Step 5 is re-proved in full nothing depends on the source file.
- `q4_upper.py` contains a stray dependence on the loop variable `seed` after the loop when
  the `break` never fires; cosmetic, it only affects a printed diagnostic, and nothing in the
  proof uses this script's output beyond a labelling that is then scored exactly.

---

```
RAN (PYTHON = /Users/raducucu/bainsahackathon/.venv/bin/python3, all /usr/bin/time -p):
  inbox/checker/verify.py on subject/Q3.txt --d 3       -> VERIFIED 14   COMPLETED  0.05 s
  inbox/checker/verify.py on subject/Q4.txt --d 4       -> VERIFIED 34   COMPLETED  0.06 s
  subject code/uphill.py ../Q3.txt 3                    -> 14 (both counters)  COMPLETED  0.03 s
  subject code/uphill.py ../Q4.txt 4                    -> 34 (both counters)  COMPLETED  0.02 s
  subject code/q3_exhaustive.py, all 8! = 40320         -> min 14, 7104 minimisers  COMPLETED  0.13 s
  subject code/identity_check.py, d = 2..5 x 2000 + all 8! of Q_3 -> I1,I2 hold  COMPLETED  1.12 s
  subject code/q4_upper.py 4 34                         -> best 34      COMPLETED  0.04 s
  out/cex/independent.py (literal enumeration of Q3/Q4; all 2!,4!,8! for d=1,2,3;
        400-restart descent on Q_4; Steps 1,3,4,5,6 on 4000 random graphs, 1376 equality cases)
                                                        -> 14 / 34; minima 2,5,14; all identities hold  COMPLETED  0.75 s
  out/cex/bnb_q4.py 60000000 : d=3 target 15 and d=4 target 35 controls -> witnesses FOUND  COMPLETED
                               d=3 target 14 reduced and unreduced      -> U(Q_3) >= 14     COMPLETED
                               d=4 target 34 reduced and unreduced      -> node cap 6e7 hit  PARTIAL (143.4 s, 141.8 s)
                                                        total wall time 287.19 s
  out/cex/hunt33.py : Q_3 target<=13 (200x4000, 700133 evals) and Q_4 target<=33
        (400x12000, 4499578 evals) simulated annealing; Remark divisibility d=2..40
                                                        -> best 14 and 34, no counterexample; only d=2 passes  COMPLETED  27.29 s
  out/cex/grid_imo.py : all 4! of the 2x2 grid and all 9! of the 3x3 grid
                                                        -> minima 5 and 13 = 2n^2-2n+1  COMPLETED  0.74 s
```
