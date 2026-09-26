VERDICT: ACCEPT
STATEMENT MATCH: yes
FIRST PROBLEM: none
CHECKLIST:
  G1 PASS — claims U(Q_7)=464 and U(Q_8)=1040, each with an explicit labelling (upper half) and a proof for every labelling (lower half); d in {7,8} exactly; no extra hypotheses.
  G2 PASS — A1–A7, C, B, D each written out; no bare "clearly/similarly/by symmetry"; the one-liners (induced subgraph of a forest is a forest; (k-1)(d-k) >= d-k) are immediate from the stated facts.
  G3 PASS — lone valleys enter through [v is a valley] in A2; d-1 >= 0 is used explicitly in A7; Lemma C is stated for d >= 2; m >= 3 in the cycle definition.
  G4 PASS — A3's descent strictly decreases labels, so it stops within n-1 moves; Lemma C's induction F_{5+j} <= 2^j F_5 is monotone; no other invariants are used.
  G5 PASS — the constructions are two explicit files, both valid bijections; the accepted checker gives 464 and 1040, and my own explicit enumeration of sequences gives the same.
  G6 PASS — no circularity; nothing is cited; the checker only scores the artefacts.
  G7 PASS — lb_forest.py is stdlib and exact (integer bitmasks), 0.44 s; section B gives the reduction to exactly the searched set (all Q_4 subsets; all ordered forest pairs with sizes summing to 20 or 19) and the soundness of the only filter (a forest on m vertices has at most m-1 edges).
  G8 PASS — no external results are used. F_5=18 (decycling number of Q_5 = 14) is known in the literature but is proved here by computation, so no citation is needed.
  G9 PASS — the claims table labels each item CHECKED/PROVED, and the one computational assumption (correctness of lb_forest.py) is named.
  S1 PASS — both integers are given; Q7.txt has 128 lines of 7 characters, Q8.txt has 256 lines of 8 characters; the lower bounds cover every labelling.
  S2 PASS — the optimum was unknown in advance; 464 >= 450 and 1040 >= 1026 agree with H-L1. Where |E|+2 is exceeded, a new argument (Lemma A + forests) is supplied rather than a BEST-FOUND value.
  S3 PASS — both values and both halves are present; the search space is defined; there is no symmetry reduction; the edge filter is sound; early stopping at m=18 only affects F_5 >= 18, which the bound does not use; nothing is time-limited.
  S4 PASS — lone valleys are counted, paths are counted as sequences starting at a valley, the labelling is a bijection, line 1 = label 1, leading zeros are kept; I re-scored with the accepted checker (sha256 2c0ba1a6…db6e) and independently.
  S5 PASS — checker counts equal the claimed values; the general bound 2^d+(d-1)(2^d-F_d) gives 14 at d=3 and 34 at d=4, and 2304 <= 2400 at d=9 via Lemma C; no value is below |E|+2.
  S6 PASS — accepted checker: Q7.txt VERIFIED 464 (0.026 s), Q8.txt VERIFIED 1040 (0.020 s).
  S7 PASS — the same argument gives exactly 88 (=32+4·14) and 204 (=64+5·28). My own labellings reach them (checker VERIFIED 88 and 204), and all four bounds lie between H-L1 and the checker-verified values.
C10 (d=5,6): ACCEPT — U(Q_5) >= 32+4(32-F_5) = 88 and U(Q_6) >= 64+5(64-2F_5) = 204 follow from Lemma A, Lemma C and F_5 <= 18. I confirmed F_5 <= 18 with two independent exhaustive computations. Both bounds are attained: out/cex/Q5_ref.txt gives 88 and out/cex/Q6_ref.txt gives 204 (accepted checker).
EQUALITY CASES: Q7.txt: count 464 = 2^7+6·56, |S|=56, S independent, T a forest. Q8.txt: 1040 = 2^8+7·112, |S|=112, same structure. So Lemma A is tight, and |S| = 2^d-2^{d-5}F_5 means Lemma C is tight too (F_7=72, F_8=144). All 40320 labellings of Q_3: minimum 14 = bound, minimum slack 0.
CROSS-CELL: Q_3=14 (exhaustive), Q_4 bound 34, Q_5 88, Q_6 204 (checker-verified labellings), Q_9 bound 2304 <= 2368 <= 2400. All consistent.
CEX SEARCH: out/cex/. Lemma A exhaustively on d=1..3 plus structured and adversarial labellings for d=4..9: 0 violations, minimum slack 0. F_5 <= 18 by C branch-and-bound over all subsets of Q_5, and by a Q_3×Q_2 split testing all 9,437,184 four-tuples with sum >= 19 (no filter): no forest with 19 or more vertices. Independent enumeration of paths in the artefacts: 464 and 1040.
OTHER ISSUES: none load-bearing. C3 (the *_alt1 files) is absent from the inbox, so unverified and unused. The SAT cross-check's find_cycle was not audited (it is unused). The direct F_6 branch-and-bound TIMED OUT; it is not needed, since Lemma C covers F_6.
RAN:
  checker verify.py inbox/subject/Q7.txt --d 7 — VERIFIED 464 — COMPLETED 0.026 s
  checker verify.py inbox/subject/Q8.txt --d 8 — VERIFIED 1040 — COMPLETED 0.020 s
  subject lb_forest.py (F_1..F_4 all subsets; Q_5 pairs m=20,19 full, m=18 to first hit) — COMPLETED 0.444 s, output = README
  subject crosscheck_F5_sat.py (venv; m=19 UNSAT, m=18 SAT) — COMPLETED 0.300 s
  subject lemmaA_sanity.py Q7.txt Q8.txt (1580 random, d=1..7) — COMPLETED 0.086 s
  out/cex/count_enum.py Q7 (d=7), Q8 (d=8) explicit DFS enumeration — 464, 1040 — COMPLETED 0.019 s
  out/cex/f5_bt d=1..4 (exhaustive B&B) — F=2,3,5,10 — COMPLETED 0.003–0.010 s each
  out/cex/f5_bt 5 / 5 18 / 5 17 (exhaustive B&B on Q_5) — F_5=18, none >18 — COMPLETED 0.143 / 0.142 / 0.154 s
  out/cex/f5_q3split.py (all Q_3-forest 4-tuples, sums 20 and 19) — 0 acyclic — COMPLETED 260.6 s
  out/cex/lemmaA_test.py (all labellings d=1..3; structured d=1..9; local search d=4..7) — 0 violations — COMPLETED 8.38 s
  out/cex/build_q5q6.py + checker on Q5_ref/Q6_ref — VERIFIED 88 / 204 — COMPLETED 0.661 s + 0.022 s + 0.021 s
  out/cex/f5_bt 6 36 (direct F_6 <= 36) — TIMED OUT at 300 s cap, no conclusion (not used)

---

# Full report (referee, H-C4-002, VERIFY of H-C4-001)

Reproduce: from `run/tasks/H-C4-002/`:
`gcc -O2 -o out/cex/f5_bt out/cex/f5_bt.c`;
`./out/cex/f5_bt 5 18`;
`python3 out/cex/f5_q3split.py`;
`python3 out/cex/lemmaA_test.py`;
`python3 out/cex/count_enum.py inbox/subject/Q7.txt 7 inbox/subject/Q8.txt 8`;
`python3 out/cex/build_q5q6.py && python3 inbox/checker/verify.py out/cex/Q5_ref.txt && python3 inbox/checker/verify.py out/cex/Q6_ref.txt`.
All logs are in `out/cex/*.log`, and the subject re-runs are in `out/cex/subject_reruns.log`.

## Statement match

The target is the pair of integers U(Q_7) and U(Q_8), each determined in two halves: (a) an explicit labelling attaining V and (b) a proof that every labelling has at least V uphill paths. The hand-in is the values plus the vertex lists in increasing label order.

- The subject claims 464 and 1040.
- Q7.txt and Q8.txt are in the inbox, in the right format (128 and 256 distinct lines of length 7 and 8, over the characters 0 and 1).
- The lower bounds quantify over every labelling f of Q_d.
- The definitions used (valley = down(v)=0; paths as sequences; a lone valley counts) match statement.md exactly.

## Per-step re-derivation (sections A, C, B, D)

**A1.**
- Q_d with d >= 1 is d-regular, so it has no isolated vertex. Then "valley" means every neighbour has a larger label, which is exactly down(v)=0.
- Every valley has down 0 <= 1, so it lies in T.
- **Holds.**

**A2.** N(v) = [v valley] + Σ_{w~v, f(w)<f(v)} N(w).
- A path with k=1 is (v), and it is uphill iff v is a valley.
- For k>=2, truncating the last vertex is a bijection onto the uphill paths ending at a lower neighbour: validity is preserved in both directions, and the last-but-one vertex determines the summand.
- **Holds.** The accepted checker uses the same recurrence, and I cross-checked it by explicit enumeration on all 40320 labellings of Q_3 and on both artefacts.

**A3.**
- The greedy descent strictly decreases labels, so it terminates at a vertex with no lower neighbour, which is a valley by A1. Reversing the walk gives an uphill path ending at v, so N(v) >= 1.
- By A2, if down(v) >= 1 then N(v) >= Σ over lower neighbours of N(w) >= down(v)·1.
- **Holds.** Asserted on every Q_3 labelling and on the random and adversarial ones.

**A4.**
- The double sum Σ_v Σ_{lower w} N(w) regroups as Σ_w N(w)·up(w), because each ordered pair (w lower, v upper) is exactly one edge, counted once.
- Σ_w up(w) = E, since each edge has exactly one lower endpoint (labels are distinct).
- **Holds.** The identity is asserted exactly in lemmaA_test.py on all tested labellings.

**A5.**
- For w in T, (N-1)·up >= 0 by A3.
- For w in S, with k = down(w) in [2,d]: N-1 >= k-1 >= 1 and up = d-k >= 0, so (N-1)·up >= (k-1)(d-k) >= d-k.
- Direction and signs are correct.
- **Holds.**

**A6.**
- Σ_all down = E (each edge counted once, at its upper endpoint).
- The down values in T are 0 (exactly the V0 valleys) or 1, so Σ_T down = |T| - V0 and Σ_S down = E - |T| + V0.
- Substituting gives d|S| + |T| = 2^d + (d-1)|S|. I rechecked the algebra.
- **Holds.**

**A7.**
- In a cycle of Q_d[T] with m >= 3 distinct vertices, the vertex with the maximum label has two distinct lower neighbours on the cycle, so down >= 2, which contradicts membership in T.
- Hence Q_d[T] is acyclic, |T| <= F_d by the definition of F_d, and |S| >= 2^d - F_d. Since d-1 >= 0 the bound is monotone in |S|.
- **Holds.** T was a forest in every tested labelling.

**C (Lemma C).**
- Fixing the last coordinate b gives H_b ≅ Q_{d-1}: vertices sharing x_d are adjacent iff they differ in exactly one of the first d-1 coordinates.
- T ∩ H_b induces a subgraph of the forest Q_d[T], so it is acyclic and has at most F_{d-1} vertices.
- H_0 and H_1 partition V, so F_d <= 2F_{d-1} for d >= 2, and by induction F_{5+j} <= 2^j F_5.
- **Holds.**

**B (F_5 = 18 computation).** The reduction is sound:
- T ∩ H_b maps to Q_4-forests T0, T1 with |T0|+|T1| = |T|, and T = T0 | (T1<<16) under the stated encoding (vertex x+16b; direction-5 edge = bit 4).
- Every subset of Q_4 is tested, so all forest pairs are enumerated. The s0 range [m-F4, F4] is complete because every forest has at most F4 vertices.
- The edge count e0+e1+|T0∩T1| is correct, and the filter e <= m-1 is necessary for acyclicity.
- Union-find processes each Q_5 edge once (w<v) and flags a cycle when the endpoints share a root, which is correct.
- Closure under vertex deletion turns "none with 19" into "none with >= 19".
- Only F_5 <= 18 is used; the m=18 witness is not needed.
- **Holds.** Reproduced: 0.444 s, output identical to the README.
- I confirmed F_5 <= 18 with two independent programs. The first is an exhaustive include/exclude branch-and-bound on Q_5 in C with union-find cycle detection; it finds no forest with more than 18 vertices (11.2M nodes). The second uses a different decomposition (Q_3 × Q_2, all 1,048,576 + 8,388,608 four-tuples, direct acyclicity test, no filter) and finds 0 acyclic.
- Both programs reproduce F_1..F_4 = 2, 3, 5, 10.

**D.**
- F_7 <= 4·18 = 72 and F_8 <= 8·18 = 144.
- 128 + 6·56 = 464 and 256 + 7·112 = 1040. The arithmetic checks.
- The upper halves come from C1 and C2, re-scored by me with the accepted checker and by explicit enumeration.
- **Holds.**

**C1/C2.** VERIFIED 464 and 1040 by the accepted checker; my explicit DFS enumeration gives the same counts, with 16 valleys in each file. The files are valid bijections.

**C3.** The alternative files are not in the inbox. This item is unverified, but it is not used.

**Construction principle (Lemma B)** is not load-bearing. It is still consistent: both artefacts have S independent and T a forest, and the count equals |T| + d|S|.

## Numerical sanity

- **Exhaustive, d = 1..3:** Lemma A holds on every labelling, all intermediate claims (A3, A4, A7) hold, and min U(Q_3) = 14.
- **Structured labellings, d = 1..9:** lex, reverse-lex, weight and Gray-code orders give no violation.
- **Adversarial local search:** minimising (count − bound) found minimum slack 0 at d = 4, 5 and positive slack at d = 6, 7, with no negative slack.
- **Arithmetic:** every computation in the proof is exact integer arithmetic, with no floating point.

## Counterexample search

I found no counterexample to the statement or to any intermediate claim.

- Lemma A: no violation in any test.
- The F_5 bound: confirmed by two independent exhaustive methods.
- The artefact counts: confirmed by explicit enumeration.

The only run that did not finish was the direct F_6 branch-and-bound, which TIMED OUT at the 300 s cap. It is only a redundant sanity check: F_6 <= 36 follows from Lemma C.
