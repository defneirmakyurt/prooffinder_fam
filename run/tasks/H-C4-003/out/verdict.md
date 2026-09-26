```
VERDICT: ACCEPT
STATEMENT MATCH: yes
FIRST PROBLEM: none
CHECKLIST:
  G1 PASS — proves exactly U(Q_7)=464 and U(Q_8)=1040, both halves each (explicit labelling + lower bound for every labelling); no extra hypotheses.
  G2 PASS — every step of A1–A7, C, B, D is written out; no "clearly/obviously/routine/similarly/by symmetry/WLOG" (grep: none).
  G3 PASS — lone valleys (k=1) in A2; no isolated vertices for d>=1 (A1); k=d (up=0) case covered by ">=0" in A5; cycles need m>=3 distinct vertices (A7); m=20 and m=19 both searched.
  G4 PASS — only monotone invariant is A3's strictly decreasing descent (terminates in <= n-1 moves at a valley); A5 inequalities multiply only by nonnegative factors.
  G5 PASS — the constructions are the two explicit files; accepted checker gives VERIFIED 464 / 1040; my explicit-DFS recount agrees.
  G6 PASS — no circularity; nothing cited; the checker is used only for scoring.
  G7 PASS — lb_forest.py is stdlib, exact bitmask/integer arithmetic, 0.48 s; Section B gives the written reduction (every Q_5 forest splits into a pair of Q_4 forests; all pairs with sum 19, 20 examined; edge-count filter valid); float appears only in the elapsed-time print.
  G8 PASS — no external result cited; everything proved or computed in the file.
  G9 PASS — states the computer-assisted step and its single assumption (correctness of lb_forest.py); marks the SAT run as a non-headline cross-check and the SA search as not part of the proof.
  S1 PASS — both integers, both halves, Q7.txt (128 x 7 chars) and Q8.txt (256 x 8 chars) handed in.
  S2 PASS — 464 > 450 and 1040 > 1026, so H-L1 alone would not suffice; a new lower-bound argument (Lemma A + F_d bound) is supplied, and it meets the upper bound exactly.
  S3 PASS — search space defined (all 2^16 subsets of Q_4; all ordered pairs of Q_4-forests with |T0|+|T1| in {19,20}); soundness written for the split and the edge filter; no time-limited search used as a lower bound.
  S4 PASS — lone valleys counted; paths counted as sequences (A2 bijection); only valley-started paths; bijection onto 1..2^d; line 1 = label 1, leading zeros kept; re-scored with the accepted checker (sha256 2c0ba1a6...db6e, identical to the subject copy).
  S5 PASS — checker count = claimed value on both files; the general bound gives 8+2*3=14 at d=3 and 16+3*6=34 at d=4 (<= 34); values >= |E|+2.
  S6 PASS — accepted checker on Q7.txt -> VERIFIED 464 (0.030 s), on Q8.txt -> VERIFIED 1040 (0.022 s).
  S7 PASS — d=5: 32+4*14=88, d=6: 64+5*28=204, exactly the checker-verified values; within [82,88], [194,204], [450,464], [1026,1040]; at d=9 the method gives only 512+8*(512-288)=2304 <= 2400 (and <= 2368, no conflict).
EQUALITY CASES: Q7.txt / Q8.txt attain Lemma A with equality: |S| = 56 / 112 = 2^d - 4F_5 / 2^d - 8F_5; S independent, all S-vertices have down = d; T induces a forest (16 components). Q_3: 22080 of 40320 labellings have equality in (ii); min over all = 14.
CROSS-CELL: consistent with U(Q_3)=14, U(Q_4)<=34, H-L1 (450, 1026), the checker-verified 88/204 at d=5,6, and 2368 <= U(Q_9) <= 2400.
C10 (d=5,6): ACCEPT — U(Q_5) >= 32+4(32-18) = 88 and U(Q_6) >= 64+5(64-36) = 204 follow from Lemma A, Lemma C (F_6 <= 36) and F_5 <= 18 (independently re-derived). Both are tight: my SA labellings out/cex/Q5_ref.txt and Q6_ref.txt give VERIFIED 88 and 204 on the accepted checker.
CEX SEARCH: out/cex/: independent F_5 via a 4 x Q_3 split with component-count acyclicity (none on 19/20 vertices, one on 18); Lemma A steps A2–A7 on all 40320 Q_3 labellings and on 1320 random labellings for d=4..8 (0 violations); SA on d=4..8 minimising the count and the Lemma A slack (nothing below 34/88/204/464/1040; minimum slack 0).
OTHER ISSUES: none affecting the proof. Q7_alt1/Q8_alt1 (claim C3) and the runlogs are not in the inbox, so C3 is unchecked; it is not used.
RAN: accepted checker on Q7.txt, Q8.txt (also with --d 7/--d 8), COMPLETED, 0.021–0.030 s each
RAN: subject lb_forest.py (F_1..F_4 by all subsets; Q_5 pairs for m=20,19, and m=18 until the first hit), COMPLETED, 0.482 s
RAN: subject crosscheck_F5_sat.py (venv; m=19 UNSAT, m=18 SAT), COMPLETED, 0.287 s
RAN: subject lemmaA_sanity.py (1580 random labellings d=1..7 + Q7.txt, Q8.txt), COMPLETED, 0.092 s
RAN: out/cex/indep_count.py (explicit DFS enumeration of uphill paths on Q7.txt, Q8.txt), COMPLETED, 0.020 s
RAN: out/cex/indep_F5.py (F_1..F_4 over all subsets; Q_5 as 4 x Q_3, sums 20, 19 exhaustive, 18 until first hit), COMPLETED, 0.318 s
RAN: out/cex/lemmaA_check.py (all 40320 Q_3 labellings; 300/300/300/60/60 random for d=4..8), COMPLETED, 2.349 s
RAN: out/cex/sa_search.py (SA on d=4,5 x3, d=6 x2, d=7 x1, plus from Q7.txt/Q8.txt; fixed seeds and iterations), COMPLETED, 7.082 s
RAN: out/cex/equality_check.py (S/T structure of Q7.txt, Q8.txt; subject's F_5 witness), COMPLETED, 0.017 s
RAN: out/cex/dump_q5q6.py + accepted checker on Q5_ref.txt, Q6_ref.txt, COMPLETED, 1.011 s + 0.020 s + 0.030 s
```

# Referee report H-C4-003 (GATE) on subject H-C4-001

All commands are run from `run/tasks/H-C4-003/`. Plain `python3` is stdlib-only; the venv python is used only for the subject's SAT cross-check. Every log is in `out/cex/*.log`.

## 1. Statement match

TARGET: determine the integers U(Q_7) and U(Q_8). For each, give (a) an explicit labelling with exactly V uphill paths and (b) a proof that every labelling has at least V. The hand-in is the two values plus Q7.txt and Q8.txt.

- **Claims:** U(Q_7) = 464 and U(Q_8) = 1040.
- **Upper halves:** Q7.txt and Q8.txt.
- **Lower halves:** Lemma A + Lemma C + the F_5 computation.
- **Definitions:** they match statement.md.
  - Valley: every neighbour has a larger label (A1).
  - Uphill path: a sequence starting at a valley, adjacent steps, labels strictly increasing, and k = 1 allowed (A2).
  - Q_d: {0,1}^d, adjacent when two vertices differ in exactly one coordinate.
- **Artefact format:** Q7.txt has 128 lines of length 7 and Q8.txt has 256 lines of length 8. All lines are distinct, the files are ASCII with one final newline, and line i is the vertex with label i. Leading zeros are kept (e.g. `0100010`).

## 2. Per-step re-derivation (reason each step holds)

**A1.** Q_d with d >= 1 is d-regular, so it has no isolated vertex. v is a valley ⟺ every neighbour has a larger label ⟺ down(v) = 0, because labels are distinct. So the valleys are exactly the down = 0 vertices, and they lie in T.

**A2.** N(v) = [v is a valley] + Σ_{w~v, f(w)<f(v)} N(w). Uphill paths ending at v split into two kinds:
- k = 1: the path is (v), which is uphill iff v is a valley.
- k >= 2: deleting v gives an uphill path ending at w = v_{k-1}, with w ~ v and f(w) < f(v). Conversely, appending v to such a path gives an uphill path ending at v.

These two maps are mutually inverse, and different w give disjoint sets of paths, so the count follows. Sequences are counted, so different routes to the same endpoint count separately. Numerically, the DP equals explicit enumeration on all 40320 Q_3 labellings and on the random d = 4..6 samples.

**A3.** From any v, repeatedly step to a lower neighbour. Labels strictly decrease, so the walk ends after at most n−1 steps at a vertex with no lower neighbour, which is a valley by A1. Read backwards, the walk is an uphill path ending at v, so N(v) >= 1. If down(v) = k >= 1, A2 gives N(v) >= Σ of k terms, each >= 1, so N(v) >= k. Checked numerically with no failures.

**A4.** Summing A2 over v gives Σ_v N(v) = V0 + Σ_v Σ_{w lower nbr of v} N(w). Each ordered pair (w lower, v upper) is one edge. Grouping by w gives Σ_w N(w)·up(w). Each edge has exactly one lower endpoint, so Σ up = E. The identity Σ N = V0 + E + Σ (N−1)·up was checked exactly on every tested instance.

**A5.**
- For w in T: N(w) − 1 >= 0 and up(w) >= 0, so the term is >= 0.
- For w in S with k = down(w) in [2, d]: N(w) − 1 >= k − 1 >= 1 by A3, and up(w) = d − k >= 0. So (N−1)·up >= (k−1)(d−k) >= d − k. The last step holds because k − 1 >= 1 and d − k >= 0.

The inequalities point the right way, and the only multipliers are nonnegative.

**A6.** Σ_all down = E. On T, down is in {0, 1}: it is 0 exactly on the V0 valleys, which all lie in T, and 1 on the rest. So Σ_T down = |T| − V0 and Σ_S down = E − |T| + V0. Substituting gives Σ N >= d|S| + |T| = 2^d + (d−1)|S|. I checked the algebra by hand and the identity numerically.

**A7.** Take a cycle in Q_d[T] (at least 3 distinct vertices). Its highest-labelled vertex has two distinct cycle-neighbours, both lower, so down >= 2 and the vertex is in S, a contradiction. So T induces a forest and |T| <= F_d. Because d − 1 >= 0, the bound 2^d + (d−1)|S| is nondecreasing in |S|, so replacing |S| by its lower bound 2^d − F_d is valid.

**Lemma C.** H_b = {x_d = b} induces a copy of Q_{d−1} under deletion of the last coordinate, since two vertices of H_b differ exactly in one of the first d−1 coordinates. T ∩ H_b induces a subgraph of the forest Q_d[T], so it is acyclic and |T ∩ H_b| <= F_{d−1}. H_0 and H_1 partition V, which gives F_d <= 2F_{d−1}. Iterating gives F_6 <= 36, F_7 <= 72 and F_8 <= 144. The induction is one line, but its step is exactly the lemma.

**B (the F_5 computation).**
- Reduction: T is recovered from its pair of sides (T0, T1) as the mask T0 | T1<<16. Each side is a Q_4 forest by Lemma C's argument, and each side has at most F_4 = 10 vertices, which is computed over all 2^16 subsets. So a forest on 19 or 20 vertices would have to appear among the pairs with sizes (9,10), (10,9) or (10,10). There are 16192 such pairs, and the code examines all of them.
- Filter: a forest on m vertices has at most m − 1 edges, and e(Q_5[T]) = e(T0) + e(T1) + |T0 ∩ T1|, where the last term counts the direction-5 matching edges. The filter is valid.
- Full test: union-find over the induced edges, each edge processed once (w < v), and a cycle is flagged when an edge joins two vertices already in one component. I reviewed the code and it is correct.
- Hereditary step: removing a vertex from a forest leaves a forest, and m = 20 is checked explicitly anyway.
- Output: m = 20 and m = 19 are rejected, and an 18-vertex witness is found. My equality_check.py confirms the witness is an induced forest. Only F_5 <= 18 is needed for the bound.
- Runtime 0.48 s, exact arithmetic, no floating point in the logic.

**D.**
- d = 7: 128 + 6·(128 − 72) = 464.
- d = 8: 256 + 7·(256 − 144) = 1040.

Together with the checker-verified files (464 and 1040), this gives U(Q_7) = 464 and U(Q_8) = 1040. The arithmetic is re-checked.

**C10, d = 5 and 6.**
- d = 5: 32 + 4·(32 − 18) = 88.
- d = 6: 64 + 5·(64 − 36) = 204, using F_6 <= 2F_5 = 36.

The same steps apply, so this is ACCEPT. Both bounds are tight: labellings from my own search give VERIFIED 88 and 204 on the accepted checker.

## 3. Numerical sanity

- The subject's code reproduces exactly: lb_forest.py, the SAT cross-check (m = 19 UNSAT after 707 iterations, m = 18 SAT) and lemmaA_sanity.py (1580 trials, 0 violations; count = bound = 464 and 1040).
- The accepted checker is byte-identical to the subject's copy (same sha256).
- My explicit enumeration of uphill paths, with no DP, gives 464 on Q7.txt and 1040 on Q8.txt (16 valleys each, longest path 4 vertices).

## 4. Equality cases

Part S lists no extremal configurations (the optima are unknown). The artefacts attain Lemma A with equality:
- S is independent, every S-vertex has down = d, and |S| = 56 / 112.
- |T| = 72 / 144, so the Lemma C bound on F_7 and F_8 is attained by these T.

## 5. Cross-cell

- d = 3: 14 = U(Q_3).
- d = 4: 34 <= 34.
- d = 5 and 6: 88 and 204, matching the checker-verified labellings.
- The values are >= H-L1.
- d = 9: the method gives >= 2304, which is consistent with 2368 <= U(Q_9) <= 2400 (a weaker bound, not a contradiction).

## 6. Counterexample search (out/cex/)

- **indep_F5.py:** a different split of Q_5 (four Q_3 copies along the two lowest bits), a different acyclicity test (#edges = #vertices − #components), and pruning on pairs of adjacent copies, whose soundness is written in the header. It finds no induced forest on 20 or 19 vertices and one on 18. This independently confirms F_4 = 10 and F_5 = 18.
- **lemmaA_check.py:** A2 through (ii) on all 8! labellings of Q_3 and on random labellings for d = 4..8. 0 violations; min over Q_3 is 14.
- **sa_search.py:** annealing to minimise the count and to make the Lemma A slack negative. Best counts: 34 / 88 / 204 at d = 4 / 5 / 6, 622 at d = 7 from a weight-sorted start, and 464 / 1040 when started from the artefacts. Nothing goes below the claimed bounds, and the minimum slack is 0. This is heuristic evidence only; the proof does not rely on it.
