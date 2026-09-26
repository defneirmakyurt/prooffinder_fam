# Referee verdict — H-C1-005 (VERIFY, subject H-C1-004)

```
VERDICT: ACCEPT
STATEMENT MATCH: yes
FIRST PROBLEM: none
```

Subject's claim under review: `U(Q_3) = 14`, `U(Q_4) = 34`, with `inbox/subject/Q3.txt`
and `inbox/subject/Q4.txt` as the attaining labellings, and the lower halves
`U(Q_3) >= 14`, `U(Q_4) >= 34` established by exhaustive branch-and-bound.

Everything below was re-run by me. Interpreter
`/Users/raducucu/bainsahackathon/.venv/bin/python3` (CPython 3.14.0), Apple M1, macOS 26.6.2.

---

## 1. Checklist pass

### Part G

| item | result | reason |
|---|---|---|
| G1 | PASS | The settled statement is exactly the cell's: the two integers `U(Q_3)`, `U(Q_4)`, each with an explicit attaining labelling in the hand-in format (`2^d` lines, line `i` = vertex with label `i`, `0/1` strings of length `d`). Both halves (a) and (b) of "determine" are supplied for both `d`. No extra hypothesis; nothing is claimed for `d != 3, 4`. |
| G2 | PASS | Every step is written out: R2 proves the counting recursion by an explicit bijection with well-definedness, injectivity and surjectivity each argued; R2b is an induction; R5 is Facts 0–3 plus an assembly; R6 proves the memo invariant in all three child cases; R8 states the reduction. No "clearly/similarly/routine/obviously/by symmetry" stands in for an argument — in particular no symmetry argument occurs anywhere, because no symmetry reduction is used (I read `bnb.py` line by line: the branching loop is `for v in range(n): if (S >> v) & 1: continue`, i.e. every unplaced vertex, at every depth, including depth 0). |
| G3 | PASS | Degenerate cases are handled explicitly: isolated vertices (vacuous in `Q_d`, `d >= 1`, and correctly subsumed by `all()` over an empty neighbour list); `k = 1` paths (the `[v valley]` term — I confirmed `Q3.txt` has exactly one valley, `000`); `S` empty in `LB`; `T = 1`; recursion depth. |
| G4 | PASS | The only claimed invariant is the memo invariant `I(k,c)`, proved established at every write and used only where it applies (R6); it is in any case not load-bearing (the decisive runs use `--nomemo`). Strictness of `f(w) < f(v)` is justified: `f` is a bijection onto `{1..n}`, no ties. |
| G5 | PASS | The two constructions are checked at exactly the two claimed values `d = 3, 4`; there is no untested claimed value. |
| G6 | PASS | No circularity: the lower-bound search never reads the upper-bound labelling (`bnb.py d T` takes only `d` and `T`); the upper bound is an explicit object scored by the provided checker. No citation of the target. The provided checker is used as a scorer only, and its recursion is re-derived from the definitions in R2. |
| G7 | PASS | All arithmetic is exact Python integers; I read every file — the only floats are `math.exp` / the annealing temperature in `sa_q4.py`, a candidate generator that influences no claim. Code is supplied. The decisive runs measured 0.08 s and 0.84 s. The finite check covers exactly `d = 3, 4` and claims nothing else (`claims.md` says this explicitly). The written reduction from "every labelling" to "the set searched" is R8 plus the soundness proofs of each prune (R5 for `LB` and for the trivial prune) — not an assertion of exhaustiveness. |
| G8 | PASS | No external result is used or cited; everything is derived from `inbox/statement.md`. The one external artefact, `inbox/checker/verify.py`, is clearly separated and used only as a scorer. |
| G9 | PASS | "Established: `U(Q_3) = 14`, `U(Q_4) = 34`, both halves. Not established: anything for `d >= 5`, and any general formula." |

### Part S

| item | result | reason |
|---|---|---|
| S1 | PASS | Both values given. (a) `verify.py Q3.txt --d 3` → `VERIFIED 14`; `verify.py Q4.txt --d 4` → `VERIFIED 34` (re-run by me). (b) Lower halves proved by exhaustive search with proved-sound prunes, and independently reproduced by me (§4, §6). |
| S2 | N/A → noted | Part S records the extremal values as *unknown*; the statement supplies none. So no external value can be compared. Tightness is instead established internally: lower bound = construction value, exactly, for both `d`. |
| S3 | PASS | A lone valley is counted (`[v valley]` term; `Q3.txt` has 1 valley contributing 1 of its 14 paths). Paths are counted as sequences, so distinct routes to the same endpoint count separately — this is exactly what the recursion's `sum over lower neighbours` does, and my independent counter enumerates the sequences literally and agrees on 900 random labellings and on both artefacts. Labels are a bijection onto `1..2^d` (enforced by `parse` and by `assert sorted(order) == list(range(n))`). Both `d = 3` and `d = 4` are done. Both halves are given, and the lower half is over ALL labellings (R8 + proved prunes). |
| S4 | PASS | Paths start at a valley (checked in both counters). Labels strictly increase. Hand-in order is "line `i` = vertex with label `i`", `d` characters with leading zeros — `Q3.txt` is 32 bytes / 8 lines of length 3, `Q4.txt` 80 bytes / 16 lines of length 4, all distinct, single trailing newline (`out/cex/hunt.py`). "Exhaustive" is *defined* (`(2^d)!` label sequences = leaves of the unpruned tree) and every prune has a written soundness proof; no symmetry reduction is used, so no symmetry reduction needs a soundness argument. No run is time-limited: `--maxnodes` was not used in any decisive run and, when used, prints `ABORTED ... search NOT complete` instead of a verdict. No score is copied from a report: I re-ran the checker myself. |
| S5 | PASS | Every handed-in value equals the accepted checker's count on the submitted labelling (re-run: 14 and 34). No general-`d` lower-bound statement is made, so nothing to compare. No lower cells exist. |
| S6 | PASS | Hand-computed `Q_1`: the only labellings give paths `(0)`, `(0,1)` → 2. Hand-computed `Q_2` with order `00,01,10,11`: valley `00`, paths `(00),(00,01),(00,10),(00,01,11),(00,10,11)` → 5. The provided checker, my literal enumerator and the subject's `uphill.count` all return 2 and 5 (`out/cex/small_cases.log`, `out/cex/q1q2_subject.log`). Full enumeration gives `U(Q_1)=2`, `U(Q_2)=5`. |

No FAIL, so nothing blocks ACCEPT.

---

## 2. Line-by-line re-derivation — why each step holds

**R2 (counting recursion).** Holds. `N(v)` = number of uphill paths whose last vertex is `v`;
every uphill path has exactly one last vertex, so the total is `sum_v N(v)` — a partition of the
set of uphill paths by last vertex, hence no double count and no omission. The `k = 1` term: the
only length-1 sequence ending at `v` is `(v)`, uphill iff `v` is a valley — this is the definition
verbatim. The `k >= 2` term: the map `phi(v_1,...,v_{k-1},v) = ((v_1,...,v_{k-1}), w = v_{k-1})` is
(i) well defined — the truncation inherits `v_1` a valley, adjacency for `i <= k-2`, and a
sub-chain of a strict chain is strict, and the index `w` satisfies `w ~ v` (consecutive on the
path) and `f(w) < f(v)` (last inequality of the chain); (ii) injective — the pair determines the
original by appending `v`; (iii) surjective — appending `v` to any uphill path ending at a lower
neighbour `w` of `v` yields an uphill path (valley start unchanged, adjacency `w ~ v`, chain
extended by `f(w) < f(v)`). So `|A(v)| = sum_{w ~ v, f(w) < f(v)} N(w)`. The "process in increasing
label order" remark is justified because the right-hand side mentions only strictly smaller labels.
*Independent confirmation:* my `out/cex/indep.py` counts uphill paths by literally enumerating the
sequences (no recursion identity at all) and agrees with the provided checker on both artefacts and
on 900 random labellings of `Q_3`, `Q_4`, `Q_5` — 0 mismatches.

**R2b (`N(x) >= 1`).** Holds. Induction on `f(x)`. If `x` is a valley, `N(x) >= 1` from the
`[valley]` term. Otherwise the definition of "not a valley" gives a neighbour `w` with
`f(w) < f(x)`; all terms of R2 are non-negative (they are cardinalities), so `N(x) >= N(w) >= 1`
by induction (`f(w) < f(x)` is a strict decrease, so the induction is well founded). The base is
genuinely covered: the label-1 vertex has no smaller-labelled neighbour, so it is a valley.

**R5 / Fact 0.** Holds by construction of the node: `S` carries labels `1..m`, `R` carries
`m+1..n`, and the construction of the tree gives label `k+1` at depth `k`.

**R5 / Fact 1 (prefix determines cost so far).** Holds. For `i <= m`, the neighbours of `v_i` with
smaller label are exactly its neighbours among `v_1,...,v_{i-1}` (Fact 0 plus the labelling being
the identity on the prefix), so `N(v_1),...,N(v_m)` and `cost(S)` are functions of the sequence
alone. I checked this against the code: `Nv = (0 if low else 1) + sum(N[w] for w in low)` with
`low = [w in NB[v] if w in S]`, computed at the moment `v` is placed and restored on backtrack
(`N[v] = 0`), so `N[]` is exactly correct on `S` at every node.

**R5 / Fact 2 (expansion of the remaining cost).** Holds. Apply R2 to every `v in R` and split the
inner sum by `w in S` / `w in R`. By Fact 0 the whole `S`-part is `P(v)`. For the `R`-part, an
ordered pair `(v,w)` with `v,w in R`, `w ~ v`, `f(w) < f(v)` corresponds to an unordered `R`-edge,
and since labels are distinct exactly one of the two orientations qualifies, contributing `N` of
the lower end. So
`future = #valleys(R) + sum_{v in R} P(v) + sum_{R-edges {u,v}} N(lower end)`,
an identity, not an inequality. I re-derived it myself and got the same three terms, with no
double counting (the three terms come from disjoint parts of one expansion).

**R5 / Fact 3 (pointwise bounds).** Holds. `N(x) >= P(x)` because all placed neighbours of `x` are
lower (Fact 0) so they all occur in R2's sum, and the remaining terms are non-negative;
`N(x) >= 1` is R2b. Hence `N(x) >= max(1, P(x))`.

**R5 / assembly.** Holds. `#valleys(R) >= 0` always; when `S` is empty the vertex taking label 1
has all neighbours higher, hence is a valley and lies in `R`, giving `>= 1`. For an `R`-edge
`{u,v}` the lower end is `u` or `v`, so `N(lower) >= min(max(1,P(u)), max(1,P(v)))`. Substituting
into the Fact-2 identity gives `future >= LB(S)` for **every** completion. Therefore
`cost(S) + LB(S) >= T` implies every extension has total `>= T`, so the cut removes no labelling
with fewer than `T` uphill paths. `LB(S)` reads only `S` and `N` on `S`, so it is computable at the
node. I checked `lower_bound()` in `bnb.py` term by term against this formula: `tot += p` over
`v in R` is `sum P(v)`; the `EDGES` loop (each edge once, `u < v`) adds
`min(max(1,P[u]), max(1,P[v]))` for edges with both ends unplaced; `if S == 0: tot += 1`. It
matches exactly, including the `S`-empty special case.

**R5 / trivial prune.** Holds. At the child that gives label `m+1` to `v`, `N(v)` is already exact
(Fact 1), and every not-yet-placed vertex has `N >= 1 > 0` (R2b), so the total of any labelling
through this child is `>= cost(S) + N(v)`; if that is `>= T` the child contains nothing below `T`.
Code: `if cost + Nv >= T: continue`.

**R6 (state memo).** Holds, and is explicitly *not* load-bearing. The equivalence claim is correct:
running R2 forward along a completion, a vertex `u in R` needs `N(w)` only for `w` a lower
neighbour, i.e. `w in S` adjacent to `u` (hence `w in B(S)`, since `u` is unplaced) or `w in R`
placed earlier in the same pass; and "`u` is a valley" is decided by `S` and the completion order.
So `future` — and hence `minfuture` — is a function of `(S, N|_{B(S)})`. The invariant
`I(k,c): c + minfuture(k) >= T` is checked at both write sites and in all three ways a child can be
disposed of; the `min(prev, cost)` write is covered because the smaller value already satisfies the
invariant. The decisive Q_4 run uses `--nomemo` and the decisive Q_3 run uses `--nomemo --nolb`, so
no reported bound depends on R6.

**R8 (what "exhaustive" means).** Holds. Two things are needed and both are supplied:
(i) the unpruned leaf set is all `(2^d)!` bijections — I verified in the source that at every node
the branching is over *every* unplaced vertex, with no canonical-form filter, no symmetry
reduction, and no restriction on the label-1 vertex, so label sequences are built freely and the
leaves are exactly the bijections `V(Q_d) -> {1..n}`; (ii) every prune is proved above to remove
only subtrees containing no labelling with total `< T`. Hence `NONE BELOW T` is exactly "every
labelling of `Q_d` has at least `T` uphill paths". This is a written reduction, not an assertion.

**Upper halves.** `Q3.txt` and `Q4.txt` are valid labellings in the required format, and the
accepted checker scores them 14 and 34. Hence `U(Q_3) <= 14`, `U(Q_4) <= 34`.

**Conclusion.** `U(Q_3) = 14` and `U(Q_4) = 34`.

### Unjustified, circular or false steps found

None.

---

## 3. Numerical sanity and re-runs of the supplied code

All runs below are mine, timed with `/usr/bin/time -p`.

| command | output | runtime | status |
|---|---|---|---|
| `verify.py inbox/subject/Q3.txt --d 3` | `VERIFIED 14` | 0.02 s | COMPLETED |
| `verify.py inbox/subject/Q4.txt --d 4` | `VERIFIED 34` | 0.02 s | COMPLETED |
| `bnb.py 3 14 --nomemo --nolb` | `nodes=59681`, `NONE BELOW 14` | 0.08 s | COMPLETED |
| `bnb.py 4 34 --nomemo` | `nodes=135169`, `NONE BELOW 34` | 0.84 s | COMPLETED |
| `bnb.py 3 15` | `FOUND 14` + labelling identical to `Q3.txt` | 0.01 s | COMPLETED |
| `bnb.py 4 35` | `FOUND 34` + labelling identical to `Q4.txt` | 0.01 s | COMPLETED |
| `brute_q3.py` | 40320 labellings, `min = 14`, 7104 minimisers, histogram `[(14,7104),(16,14112),(17,6720),(18,4704),(19,576)]` | 0.23 s | COMPLETED |
| `crosscheck.py sweep 3 16` | `NONE BELOW T` for `T = 1..14`, `FOUND 14` for `T = 15,16` | 0.48 s | COMPLETED |
| `crosscheck.py counter 3 300 verify.py` | `mismatches=0` | 10.20 s | COMPLETED |
| `crosscheck.py counter 4 300 verify.py` | `mismatches=0` | 12.50 s | COMPLETED |
| `bnb.py 4 34 --nolb` (memo only — **my own probe, never claimed**) | no output | > 600 s | TIMED OUT |

Every run the subject claims reproduces, with runtimes matching the claimed 0.09 s / 0.85 s to
within noise. The memo-only configuration `--nolb` for `d = 4` does not finish in 10 minutes; this
is not a defect, because no claim rests on it (the README lists only `--nomemo`).

Floating point: `grep`-level reading of all five source files shows the only floating-point
operations are `T0 * (T1/T0) ** (it/iters)`, `math.exp`, `rng.random()` in `sa_q4.py`, a candidate
generator whose output is re-scored by `verify.py`. No bound and no count uses a float. Everything
else is Python `int`.

---

## 4. Equality-case test

Part S lists the extremal values as **unknown**, so there is no externally supplied extremal
configuration to test against. I tested tightness internally instead:

* `d = 3`: exhaustive enumeration of all `8! = 40320` labellings with my *literal* path counter
  gives minimum 14, attained by 7104 labellings (identical histogram to `brute_q3.py`), and
  `Q3.txt` is one of them. So the bound `>= 14` is attained, i.e. tight, and the value is exact.
* `d = 4`: my independent level-DP over all `16!` label sequences returns exact minimum 34 (run
  with cutoff 35, `out/cex/dp2.py 4 35`), and `Q4.txt` scores exactly 34. Tight.
* Lower cubes: `U(Q_1) = 2`, `U(Q_2) = 5`, attained.

No slack anywhere: lower bound = construction value for both `d`.

---

## 5. Cross-cell consistency

There are no lower verified cells (S5: "No lower cells exist"). The subject makes no general-`d`
statement, so there is nothing that could disagree with a future cell. As an extra consistency
probe I computed `U(Q_1) = 2`, `U(Q_2) = 5`, `U(Q_3) = 14`, `U(Q_4) = 34` — the subject's two
values sit in this sequence and its counter reproduces the hand-computed `Q_1` and `Q_2` values.

---

## 6. My own counterexample search (`out/cex/`)

| file | what it does | result |
|---|---|---|
| `indep.py` | uphill-path counter by **literal enumeration of the sequences** from the definition (DFS from each valley along strictly increasing labels); uses no counting recursion, so it is logically independent of R2 and of the provided checker | — |
| `small_cases.py` / `small_cases.log` | hand-computed `Q_1` and `Q_2` asserted; full enumeration of all labellings of `Q_1, Q_2, Q_3` | `U(Q_1)=2`, `U(Q_2)=5`, `U(Q_3)=14` (7104 minimisers). **Independently confirms `U(Q_3) = 14` over all 40320 labellings.** 0.48 s |
| `xcheck.py` / `xcheck.log` | literal counter vs provided checker on both artefacts and on 400+400+100 random labellings of `Q_3, Q_4, Q_5` | both artefacts AGREE (14, 34); 0 mismatches in 900 random trials. 27.72 s |
| `dp_exact.py` / `dp3.log` | my own exhaustive level-DP over all `(2^d)!` label sequences, merging only prefixes with the same `(S, N on the boundary of S)`, run with **no pruning at all** on `d = 3` | exact minimum 14 — agrees with the literal `8!` enumeration, which validates the state-merging step of my DP. 0.02 s |
| `dp2.py` / `dp2_d3.log`, `dp2_d4_both.log`, `dp2_d4_more.log`, `dp2_d4_b1.log` | same DP with two lower bounds on the remaining cost: `B1 = sum_{v in R} max(1,P(v))` (uses only `N >= 1` and `N(x) >= P(x)` — **it does not use the subject's edge term at all**) and `B2` (my re-derivation of the subject's `LB`) | `d = 3`, cutoff 14: no labelling below 14 (0.02 s). `d = 4`, cutoff 34, **`B1` only**: no labelling below 34, 738908 states, **61.35 s** — an independent proof of `U(Q_4) >= 34` that does not rely on R5's edge term. `d = 4`, cutoff 34, both bounds: same verdict, 0.10 s. `d = 4`, cutoff 35: exact minimum over all `16!` labellings = **34**, 0.69 s |
| `hunt.py` / `hunt.log` | byte-level format check of both artefacts, then random-restart best-improvement swap hill climbing scored by the literal counter: 4000 restarts on `Q_3`, 1200 on `Q_4` | format OK (32 / 80 bytes, correct line counts and lengths, all vertices distinct, single trailing newline); best found 14 and 34; **no labelling below 14 or below 34 found**. 22.47 s |
| `dp4.log` | first attempt at `d = 4` with no bound beyond `N >= 1` | PARTIAL — reached level 8 (822106 states) then **TIMED OUT** at 600 s. Superseded by `dp2_d4_b1.log`, which completes. |

**No counterexample exists**: the search in `dp2.py 4 34 b1` is exhaustive over all `16!` label
sequences (merging only provably equivalent prefixes, pruning only prefixes that cannot reach a
total below 34), so `U(Q_4) >= 34` is confirmed by code I wrote, using a bound I derived and the
subject does not use.

---

## 7. Other issues (none blocking)

1. **Wording, R8.** "the unpruned run visits the full tree (59681 nodes with only the trivial
   prune)" — the full `d = 3` tree has `sum_{k=0}^{8} 8!/(8-k)! = 109601` nodes, so 59681 is *not*
   the full tree; the trivial prune is active (there is no flag to disable it). The parenthesis
   already says so, and nothing logical rests on the number: the reduction in R8 needs only
   (i) branching over every unplaced vertex and (ii) soundness of each prune, both of which are
   proved. Suggested fix: "visits 59681 nodes, the full tree minus what the (proved) trivial prune
   removes".
2. `claims.md` refers to `out/stuck.md` and `../runlog.md`, which are not in my inbox. Nothing
   load-bearing depends on them; every claim in the summary table is supported by material I could
   read and re-run.
3. `claims.md` reports 0.09 s and 0.92 s for the two decisive runs; I measured 0.08 s and 0.84 s on
   this machine. Consistent.
