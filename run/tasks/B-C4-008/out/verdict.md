```
VERDICT: ACCEPT
STATEMENT MATCH: yes (LOWER half, as the brief asks): the proof shows, symbolically in k, that lambda^(k) = (k-2, k-2, k-3, ..., 3, 2, 2, 1) is a partition of T_{k-1}+1 with d_B(lambda^(k)) = (k-1)(k-3) exactly, for every k >= 5. Hence D_B(T_{k-1}+1) >= (k-1)(k-3). The proof's upper half is labelled [GAP] by the proof itself and is outside this gate.
FIRST PROBLEM: none (for the lower half)
CHECKLIST:
  G1 PASS — lower-half claim = TARGET verbatim: every k >= 5, explicit lambda^(k), exact value (k-1)(k-3) (equality, not just >=), cycle-entry time
  G2 PASS — every step is written out; "standard" in 0.1 is followed by the argument; no bare "clearly/similarly/by symmetry" in Steps 0-8
  G3 PASS — k = 5 gives (3,3,2,2,1) explicitly; ranges (rows 2..k-2, the lists in 8.2, gamma_3) are non-degenerate for k >= 5 (in fact k >= 4); t_* >= 7
  G4 PASS — energy is constant on closed rotations (Lemma 2) and drops by >= 1 at the wrap step, since E is integer-valued; the strict drop is what gives non-cyclicity of B^{t_*} (Lemma 3)
  G5 PASS — the orbit B^t = Q(h_t; b_t, b_t+), 0 <= t <= t_*, and the last two states are derived symbolically for every k >= 5 (Lemmas 6-7, Step 8.2), not from tested k
  G6 PASS — no circularity; the lower half uses Lemmas 1, 2, 3, 4(a), 5, 6, 7 only, all proved in-file; no citation of the target
  G7 PASS — no computation is load-bearing for the lower half; the code is stdlib, exact integers, and runs in < 11 s; the proof says the finite checks are sanity or evidence only
  G8 PASS — nothing is cited; every tool (Young diagrams, rotation, energy) is proved in-file. (Optional: credit the classical rotation/energy method, e.g. Brandt 1982 or Griggs-Ho 1998)
  G9 PASS — Step 10 separates PROVED (lower bound, cyclic set, levels <= E_min+1) from [GAP] (upper bound) and CHECKED (k = 5..12)
  S1 PASS — lower half matches S1 exactly; the upper half of S1 is N/A for this gate (the proof marks it [GAP], Step 9)
  S2 PASS — exhaustive, exact: D_B = 8, 15, 24, 35, 48, 63 (also 80, 99) = F(k) for k = 5..10 (11, 12); lambda^(k) is always a maximiser; maximiser counts 3, 12, 62, 288, 1310, 5862 (26399, 119871); lambda^(k) is not the unique global maximiser, and the proof does not claim it is
  S3 PASS — for the lower half: every k >= 5, symbolic, smallest k = 5 included. The "every partition" part (n), (1^n), ... is upper-half, N/A here
  S4 PASS — cycle ENTRY time (Cor. 3'); s = number of parts before subtraction (r_1 = s, Step 1); the new part is sorted in (8.2 last step); d_B(cyclic) = 0; the target is any gamma_j (gamma_3, period k), not a fixed point; finite k is not used as proof
  S5 PASS — Lemma 4 = gated C1 (delta_{k-1} + one cell of diagonal k, k partitions, one k-cycle); F(k) <= k^2-2k-1 (slack 2k-4 > 0), consistent with C3(a); C2: no constraint
  S6 PASS — the statement gives no values; the S2 table matches F(k) and lambda^(k)
EQUALITY CASES: d_B(lambda^(k)) = (k-1)(k-3) by theory-free cycle-entry iteration for all k = 5..150. The symbolic orbit formula and both final states were checked against direct iteration for k = 5..150. The exact d_B formula of Lemma 7 holds on every level-(E_min+1) partition, k = 4..30, and its unique maximiser there is Q(1;k-1,k) = lambda^(k).
CROSS-CELL: consistent with gated C1 (cyclic set and single k-cycle agree with the exhaustive runs, k = 5..12); F(k) = k^2-4k+3 < k^2-2k-1 (C3(a)).
CEX SEARCH: out/cex/ (exhaustive_check.py, maximisers_dump.py, orbit_check.py, lemma_checks.py, symbolic_arith.py). Searched: all partitions for k = 5..12 (Lemmas 2, 5(a), 5(b), 6(a), 7, D_B, maximisers), the level-(E_min+1) family for k = 4..30, 18000 random partitions for k = 5..40, and the orbit for k = 5..150. No counterexample and no lemma failure.
OTHER ISSUES: (1) The upper half (Step 9) is an acknowledged [GAP]; Cor. 7' (levels <= E_min+1) checks out. (2) Cosmetic: the paths "out/code/..." and "stuck.md" are not in the hand-in. The remark "k>=5 ensures 3<=k" should read 3<=k-1. The target's "..., 3, 2, 2, 1" pattern is degenerate at k=5; the row-wise definition in 8.1 fixes it as (3,3,2,2,1).
RAN: listed in section 5 below (all COMPLETED).
```

# Referee report B-C4-008 (VERIFY, lower half of B-C4; subject B-C4-007)

## 1. Statement match

TARGET (lower half): for EVERY k >= 5, lambda^(k) = (k-2, k-2, k-3, k-4, ..., 3, 2, 2, 1) is a partition of n = T_{k-1}+1 with d_B(lambda^(k)) = (k-1)(k-3), and its orbit is tracked symbolically in k. Hence D_B(T_{k-1}+1) >= (k-1)(k-3).

What the proof proves (Steps 8.1-8.3):
- lambda^(k) := Q(1;k-1,k) has row lengths: row 1 = k-2; row i = k-i for 2 <= i <= k-2; row k-1 = 2; row k = 1. That is (k-2, k-2, k-3, ..., 2, 2, 1), the TARGET partition.
- The sum is (k-2) + (T_{k-2} - 1) + 3 = T_{k-2} + k = T_{k-1} + 1. Checked with sympy in symbolic_arith.log.
- d_B(lambda^(k)) = t_* + 1 = k^2 - 4k + 3 = (k-1)(k-3), for every k >= 5.
- d_B is the cycle-entry time, as the statement defines it (min{i >= 0 : B^i cyclic}; Cor. 3').

Reading note: for k = 5 the literal list "k-2, k-2, k-3, k-4, ..., 3, 2, 2, 1" is degenerate, since k-4 = 1 < 3. The row-wise definition in 8.1 gives (3,3,2,2,1). This has sum 11 and is the only sensible reading. For k >= 6 the two readings coincide; orbit_check.py builds both and asserts they are equal for k = 5..150.

## 2. Checklist (full, with reasons)

- **G1 PASS.** The lower-half claim is the TARGET word for word: all k >= 5 (none omitted), an explicit lambda^(k) as a function of k, and an exact value (the proof shows the equality d_B = (k-1)(k-3), not just >=). No extra hypotheses.
- **G2 PASS.** Every step of Steps 0-8 is argued. The one "This is standard" in 0.1 is followed by the full argument (rows are initial segments; r_i >= r_{i+1}; the converse). "By the induction in Lemma 7" in 8.2 points to a written induction. There is no bare "clearly", "similarly" or "by symmetry".
- **G3 PASS.** Smallest case k = 5: lambda = (3,3,2,2,1), B^{t_*} = (5,4,2), B^{t_*+1} = (4,3,3,1) = gamma_3, and t_* = 7. All index ranges are non-empty for k >= 5: rows 2..k-2 in 8.1, "k-3, ..., 2" and "k-4, ..., 1" in 8.2. Lemma 6(a) needs {k-1,k} and {1,2} disjoint, i.e. k >= 4. Lemma 7 needs two distinct offsets in {2..k-1}, i.e. k >= 4. The edge case t_* = 0 in Lemma 7 (h_0 = k-1, m = 2) is also covered by the induction.
- **G4 PASS.** Invariant: while the rotated diagram is closed, energy is preserved and Y(B(lambda)) = rho(Y(lambda)) (Lemma 2(b)(c)). The level-(E_min+1) shape S(h;x,y) is preserved up to t_* (Lemma 6(a)(b) with offsets in {2..k-1}). Strictness where needed: at the wrap step the rotated set is not closed. So E drops, by at least 1 because E is an integer (Lemma 2(c)). The drop gives non-cyclicity of B^{t_*}(lambda) (Lemma 3).
- **G5 PASS.** The orbit formula h_t = 1 + (t mod (k-1)), b_t ≡ t-1 (mod k) is derived for all k from Lemma 6(b)(c). So are the identities t_* ≡ -1 (mod k-1) and t_* - 1 ≡ 1 (mod k): t_* = (k-1)(k-3) - 1 and t_* - 1 = k(k-4) + 1, polynomial identities I verified with sympy. The final state and gamma_3 are computed symbolically.
- **G6 PASS.** No circularity. The lower half uses Lemmas 1, 2, 3, 4(a), 5(a)/(b), 6 and 7. None of them assumes the conclusion, and none is the statement itself. Lemma 4(b) (classification of cyclic partitions) is not needed for the lower half; it is proved independently anyway.
- **G7 PASS.** The lower half is purely symbolic. The code is sanity or evidence only and the proof says so. It is stdlib Python with exact integers and no floating point. Runtimes I measured: 7.61 s (orbit, k = 5..60), 2.06 s (exhaustive, k = 5..11), 10.45 s (exhaustive, k = 12). The proof states that the finite checks prove nothing beyond their range.
- **G8 PASS.** No external result is cited; every tool is proved in-file. Optional: credit the classical rotation/energy technique (Brandt 1982; Akin-Davis 1985; Griggs-Ho 1998). Correctness does not depend on it.
- **G9 PASS.** Step 10 and claims.md clearly separate PROVED, [GAP] (upper bound for E >= E_min+2) and CHECKED (5 <= k <= 12).
- **S1 PASS (lower half).** Explicit lambda^(k) with d_B = F(k) for every k >= 5. The UPPER half of S1 is N/A for this gate: the proof marks it [GAP] (Step 9), and the brief gates it separately.
- **S2 PASS.** Exhaustive exact computation (my own code, which uses no theory: cyclic points are found as the points on cycles of the functional graph):

  | k | n | #partitions | D_B | F(k) | #maximisers | lambda^(k) a maximiser |
  |---|---|---|---|---|---|---|
  | 5 | 11 | 56 | 8 | 8 | 3 | yes |
  | 6 | 16 | 231 | 15 | 15 | 12 | yes |
  | 7 | 22 | 1002 | 24 | 24 | 62 | yes |
  | 8 | 29 | 4565 | 35 | 35 | 288 | yes |
  | 9 | 37 | 21637 | 48 | 48 | 1310 | yes |
  | 10 | 46 | 105558 | 63 | 63 | 5862 | yes |
  | 11 | 56 | 526823 | 80 | 80 | 26399 | yes |
  | 12 | 67 | 2679689 | 99 | 99 | 119871 | yes |

  Full maximiser lists for k = 5..10 are in out/cex/maximisers_k5_10.txt. For k = 5 they are (3,3,2,2,1), (3,3,2,1,1,1) and (3,2,2,2,1,1). lambda^(k) is not the unique global maximiser. The proof claims uniqueness only on the level E_min+1, which is correct: checked for k = 4..30.
- **S3 PASS (lower half).** The witness is proved symbolically for every k >= 5, and the smallest k = 5 is covered by the general argument (and checked explicitly). The "every partition (n), (1^n), many 1-parts, cyclic starts" part concerns the upper bound: N/A for this gate.
- **S4 PASS.**
  - Cycle-ENTRY time: Cor. 3' gives d_B = t exactly when B^t is cyclic and B^{t-1} is not.
  - s counts parts before subtraction: r_1 = s in Step 1, and 8.2 uses s = k-2 for (k, k-1, k-3, ..., 2).
  - The new part is sorted in (8.2: "sorting occurs").
  - d_B(cyclic) = 0 (Cor. 7' and the definition).
  - "Reaching a cycle" means reaching gamma_3, which lies on the k-cycle of Lemma 4(a); no fixed point is assumed.
  - No finite-k argument is used for the claim.
- **S5 PASS.** Lemma 4 agrees exactly with gated C1: the cyclic partitions are delta_{k-1} plus one cell ⟨k,j⟩ of diagonal k, there are k of them, forming one cycle of length k. The exhaustive runs confirm this for k = 5..12. For C3(a): F(k) = k^2-4k+3 <= k^2-2k-1, with slack 2k-4 > 0 for k >= 5. C2: no constraint.
- **S6 PASS.** The statement gives no values for this family. The S2 table agrees with F(k) and contains lambda^(k).

## 3. Per-step notes (reason each step holds)

- **0.1** Closed finite sets are exactly Young diagrams. Left-closure makes each row an initial segment. Up-closure applied to (i+1, r_{i+1}) gives r_i >= r_{i+1}, which also makes the non-empty rows consecutive from row 1. Conversely, left-justified rows of weakly decreasing lengths are closed.
- **0.2** ⟨d,r⟩ = (r, d+1-r). Its left neighbour (r, d-r) = ⟨d-1,r⟩ exists iff r <= d-1. Its upper neighbour (r-1, d+1-r) = ⟨d-1,r-1⟩ exists iff r >= 2. Direct computation.
- **0.3** {i+j <= k} is exactly the set of diagonals 1..k-1, with T_{k-1} cells.
- **0.4** rho⟨d,r⟩ = ⟨d,r+1⟩ for r < d (since d+1-r >= 2), and rho⟨d,d⟩ = ⟨d,1⟩. So rho acts as a d-cycle on each diagonal: it is a bijection, it preserves i+j, and it fixes Y(delta_{k-1}) setwise.
- **Step 1 (R1)** Column-1 cells (i,1) go to (1,i), forming row 1 of length s. The cell (i,j) with j >= 2 goes to (i+1, j-1), forming row i+1 of length lambda_i - 1. B is the sorted list of non-zero entries, by the definition of the shift.
- **Step 2 (R2)** E(r) = E(lambda) because rho preserves i+j. E(B lambda) = E(r↓), since the zeros are trailing. An adjacent swap of an ascent changes Σ i·a_i by a_i - a_{i+1} < 0, and bubble sort terminates at r↓. So E(r↓) < E(r) iff r is not weakly decreasing. Since r_2 >= ... >= r_{s+1}, r is weakly decreasing iff s >= lambda_1 - 1. By 0.1, closedness of rho(Y) is the same condition. When it holds, Y(B lambda) = rho(Y lambda). E is integer-valued, so a failure means a drop of at least 1.
- **Step 3 (R3)** The chain E(mu) = E(B^i mu) <= ... <= E(B mu) <= E(mu) forces equalities. Cor. 3': the set {i : B^i cyclic} is upward closed, so its minimum is characterised by "B^t cyclic and B^{t-1} not".
- **Step 4 (R4)** gamma_j is closed because the neighbours of ⟨k,j⟩ lie on the full diagonal k-1. 4(a): rho(Y gamma_j) = Y gamma_{j+1} is closed, so Lemma 2(c) gives B gamma_j = gamma_{j+1}, hence period k. 4(b) (not needed for the lower half) is correct:
  - CRT with gcd(d, d+1) = 1 rotates a missing cell ⟨d,a⟩ to ⟨d,1⟩ = (1,d) and a present cell ⟨d+1,c⟩ to ⟨d+1,1⟩ = (1,d+1) at the same time. This contradicts closedness of rho^t(Y) = Y(B^t mu).
  - An empty diagonal d+1 propagates emptiness to all later diagonals.
  - The interval count then forces d = k and c = 1.
- **Step 5 (R5)** The identity E - E_min = M + Σ_{d>=k}(d-k)c_d + Σ_{d<=k-1}(k-1-d)m_d is re-derived. It uses Σ_{d>=k} c_d = 1+M, Σ(d+1)c_d = Σ(d-k)c_d + (k+1)(1+M) and Σ(d+1)m_d = kM - Σ(k-1-d)m_d. It was also verified on every partition for k = 5..12.
  - (a) Equality forces M = 0, no cells beyond diagonal k and c_k = 1, so the partition is some gamma_j.
  - (b) Value 1: the case analysis is complete. The case "c_{k+1} = 1, c_k = 0" is killed by closedness (the upper or left neighbour lies on diagonal k). The case "third sum = 1" needs M >= 1, which makes the total at least 2.
- **Step 6 (R6)**
  - (a) Removing ⟨k-1,h⟩ keeps Y(delta_{k-1}) closed, because its right and lower neighbours lie on diagonal k, which is absent. The added cells ⟨k,z⟩ need ⟨k-1,z⟩ (when z <= k-1) and ⟨k-1,z-1⟩ (when z >= 2). The only absent cell is ⟨k-1,h⟩, so the condition is z ∉ {h, h+1}. The side conditions are automatic because 1 <= h <= k-1.
  - (b) rho is a bijection that is diagonal-wise cyclic.
  - (c) If h < k-1, the offset z - h is unchanged. If h = k-1, then h⁺ = 1 and z⁺ - 1 ≡ z ≡ (z - (k-1)) - 1 (mod k), so the offset drops by 1.
  - The offsets are distinct because x ≠ y are distinct residues in {1..k}. Closedness is equivalent to "offsets ∉ {0,1}", since h and h+1 both lie in {1..k}.
- **Step 7 (R7)**
  - Wrap times: τ_j = (k-1-h_0) + (j-1)(k-1), since h_t = k-1 iff t ≡ -h_0 (mod k-1).
  - For t <= t_* = τ_{m-1}, at most m-2 wraps have occurred, so both offsets lie in [m-(m-2), k-1] = [2, k-1], with no reduction mod k.
  - Induction: 6(b) gives the rotated set, 6(a) shows it is closed, and Lemma 2(c) identifies it with Y(B^{t+1}Q).
  - At t_* the (m-1)-th wrap brings the minimum offset to 1. The rotated set is not closed, so E drops to <= E_min. Lemma 5(a) then forces a gamma_j, which is cyclic by 4(a). Lemma 3 gives B^{t_*}Q non-cyclic, and Cor. 3' gives d_B = t_* + 1 = (k-h_0) + (m-2)(k-1).
  - Maximisation: h_0 >= 1, and m <= k-2 for two distinct offsets in {2..k-1}. Equality holds iff h_0 = 1 and the offsets are {k-2, k-1}, i.e. x, y = k-1, k.
- **8.1** ⟨k-1,1⟩ = (1,k-1), ⟨k,k-1⟩ = (k-1,2) and ⟨k,k⟩ = (k,1) give exactly the listed row lengths. The sequence is weakly decreasing and has k parts. S(1;k-1,k) is closed by 6(a) (k >= 4).
- **8.2**
  - Setup: h_0 = 1, offsets k-2 and k-1, m = k-2, t_* = τ_{k-3} = (k-2) + (k-4)(k-1) = k^2-4k+2.
  - Orbit: x_t ≡ t-1 and y_t ≡ t (mod k), so y_t = x_t⁺.
  - At t_*: t_* = (k-1)(k-3) - 1 gives h = k-1, and t_* - 1 = k(k-4) + 1 gives b = 1. The state is Q(k-1;1,2), with offsets 2 and 3, consistent with m - (m-2) = 2.
  - Rows of Q(k-1;1,2): row 1 = k, row 2 = k-1, rows 3..k-2 have length k-i, and row k-1 = 0. So the state is (k, k-1, k-3, ..., 2) with s = k-2 parts.
  - Last step: s = k-2 < k-1 = lambda_1 - 1, so sorting occurs. The parts minus 1 are k-1, k-2, k-4, ..., 1; adding the new part k-2 gives (k-1, k-2, k-2, k-4, ..., 1) = gamma_3 (third part of delta_{k-1} raised; 3 <= k-1).
  - Non-cyclicity: E(Q(k-1;1,2)) = E_min + 1 > E_min = E(gamma_3), so Lemma 3 shows B^{t_*} is not cyclic.
- **8.3** Cor. 3' gives d_B(lambda^(k)) = t_* + 1 = (k-1)(k-3). Since D_B is a maximum over all partitions of n, D_B(T_{k-1}+1) >= (k-1)(k-3).

Unjustified, circular or false steps in Steps 0-8: none found.

## 4. Numerical sanity, equality cases, counterexample search

All my code is in /Users/defneirmakyurt/bainsahackathon/run/tasks/B-C4-008/out/cex/. It is stdlib Python with exact integer arithmetic; symbolic_arith.py uses sympy (exact).

- `exhaustive_check.py` enumerates ALL partitions of T_{k-1}+1. It finds cyclic points without theory, computes d_B as the cycle-entry time, D_B and all maximisers. It checks on every partition: Lemma 2(a)(b), Lemma 5(a) (E >= E_min, with equality iff cyclic), cyclic set = {gamma_j}, level E_min+1 = {closed S(h;x,y)} (Lemmas 5(b), 6(a), with closedness tested directly on cells), and the Lemma 7 formula on the whole level. Result for k = 5..11 and k = 12: ALL OK, D_B = F(k), and lambda^(k) is a maximiser.
- `maximisers_dump.py` lists all maximisers for k = 5..10; see maximisers_k5_10.txt.
- `orbit_check.py` builds lambda^(k) in two ways (8.1 rows and the target pattern) and asserts they are equal with sum T_{k-1}+1. It computes d_B by theory-free cycle-entry iteration, and asserts the symbolic orbit formula for every t <= t_*, the state (k, k-1, k-3, ..., 2) and B^{t_*+1} = gamma_3. It also checks that the cycle length is k. Result for k = 5..150: ALL MATCH.
- `lemma_checks.py`:
  - (A) For every closed S(h;x,y), k = 4..30, the theory-free d_B equals (k-h) + (m-2)(k-1). The maximum over the level is (k-1)(k-3), attained only at (h,x,y) = (1,k-1,k).
  - (B) 18000 seeded random partitions, k = 5..40, check: the rho(Y) row list (Lemma 1), E(r) = E(lambda), Lemma 2(a)(b), and Y(B lambda) = rho(Y lambda) in the equality case.
  - Result: ALL OK.
- `symbolic_arith.py` (sympy) checks: τ_{m-1} = t_*; t_* = (k-1)(k-3) - 1; t_* - 1 = k(k-4) + 1; the Lemma 7 value at h_0 = 1, m = k-2 equals (k-1)(k-3); sum(lambda^(k)) = T_{k-1}+1; C3(a) slack = 2k-4. All identities hold.
- The subject's code was re-run. exhaustive_DB.py matches for k = 5..11 and k = 12. verify_lower_orbit.py passes for k = 5..60.

Floating point: none is used anywhere in the proof or the code.
Counterexamples found: none (to the statement, to lambda^(k), or to any intermediate lemma).

## 5. RAN (this session, measured with /usr/bin/time -p, Python = /Users/defneirmakyurt/bainsahackathon/.venv/bin/python3)

- subject code/exhaustive_DB.py 5 11 — k = 5..11 — COMPLETED — real 2.06 s (log: out/cex/subject_exhaustive_5_11.log)
- subject code/exhaustive_DB.py 12 12 — k = 12 — COMPLETED — real 10.45 s (out/cex/subject_exhaustive_12.log)
- subject code/verify_lower_orbit.py 5 60 — k = 5..60 — COMPLETED — real 7.61 s (out/cex/subject_verify_lower_orbit_5_60.log)
- out/cex/exhaustive_check.py 5 11 — k = 5..11, all partitions — COMPLETED — real 3.30 s (exhaustive_check_5_11.log)
- out/cex/exhaustive_check.py 12 12 — k = 12, all 2679689 partitions — COMPLETED — real 16.55 s (exhaustive_check_12.log)
- out/cex/maximisers_dump.py 5 10 — k = 5..10 — COMPLETED — real 0.21 s (maximisers_k5_10.txt / .time)
- out/cex/orbit_check.py 5 150 — k = 5..150 — COMPLETED — real 14.53 s (orbit_check_5_150.log)
- out/cex/lemma_checks.py 30 40 500 — Lemma 7 for k = 4..30; Lemmas 1-2 on 18000 random partitions, k = 5..40 — COMPLETED — real 28.73 s (lemma_checks_30_40_500.log)
- out/cex/symbolic_arith.py — symbolic in k — COMPLETED — real 0.30 s (symbolic_arith.log)
