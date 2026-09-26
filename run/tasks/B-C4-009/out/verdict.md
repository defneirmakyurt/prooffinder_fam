```
VERDICT: ACCEPT
STATEMENT MATCH: yes (LOWER half: lambda^(k) = (k-2,k-2,k-3,...,3,2,2,1) is a partition of T_{k-1}+1 and d_B(lambda^(k)) = (k-1)(k-3) for every k >= 5, orbit tracked symbolically in k; hence D_B(T_{k-1}+1) >= (k-1)(k-3). The UPPER half is marked [GAP] by the proof itself and is gated separately.)
FIRST PROBLEM: none (for the lower-half target)
CHECKLIST:
  G1 PASS — proved statement (proof.md line 1, Step 8) is exactly the lower target: same lambda^(k), n = T_{k-1}+1, equality d_B = (k-1)(k-3), all k >= 5; no extra hypotheses.
  G2 PASS — every step on the lower-bound chain (Steps 0-4(a), 5, 6, 7-induction, 8) is written out; the one "standard" (0.1) comes with its short proof; no "clearly/similarly/by symmetry".
  G3 PASS — smallest case k = 5 covered by the symbolic argument (lambda = (3,3,2,2,1), t* = 7, gamma_3 exists since 3 <= k-1); the ellipsis is made unambiguous by the row-wise description in 8.1; checked by direct iteration.
  G4 PASS — invariant "diagram = closed S(h_t;x_t,y_t), energy E_min+1" preserved for t <= t* (offsets stay in {2..k-1}); strict drop E_min+1 -> E_min at t* (Lemma 2(c), integrality) gives non-cyclicity of B^{t*}.
  G5 PASS — construction and orbit symbolic in k; all residue computations (t* = k^2-4k+2, t* = -1 mod k-1, t*-1 = 1 mod k) verified; valid for all k >= 4, used for k >= 5.
  G6 PASS — no circularity; no external citation; Lemma 4(b) (uses only Lemmas 2,3) is not even needed for the lower bound.
  G7 PASS — computation not load-bearing; subject's code is stdlib, exact integers, reran in 7.61 s and 2.04 s.
  G8 PASS — no results cited; all lemmas (rotation, energy, cyclic set) proved from scratch.
  G9 PASS — Step 10 and claims.md state precisely: lower bound PROVED all k >= 5; upper bound GAP (only energy <= E_min+1, and exhaustive 5 <= k <= 12).
  S1 PASS (lower half) — explicit lambda^(k), d_B = F(k) = (k-1)(k-3) for every k >= 5; upper half/equality F = D_B N/A here (separate gate; exhaustive agreement k = 5..12).
  S2 PASS — referee's own exhaustive computation k = 5..12: D_B = 8,15,24,35,48,63,80,99 = F(k); lambda^(k) attains it every time; maximisers not unique (3,12,62,288,1310,5862,26399,119871), which the proof never claims.
  S3 PASS (lower half) — every k >= 5 incl. k = 5, witness proved symbolically; "every partition" part concerns the upper half: N/A here.
  S4 PASS — d_B is entry time (Cor. 3', d_B(cyclic) = 0); s = number of parts before removal (Step 1); new part sorted (Lemma 2); end state gamma_3 is one of the k cyclic partitions (not a fixed point); no finite-k reasoning in the proof.
  S5 PASS — Lemma 4 = gated C1 (gamma_j = delta_{k-1} + one cell of diagonal k, one k-cycle; independently confirmed k = 5..12); F(k) = k^2-4k+3 <= k^2-2k-1 for k >= 2 (C3(a)); C2 no constraint.
  S6 N/A — no values given by the statement; S2 table used instead.
EQUALITY CASES: d_B(lambda^(k)) = F(k) = exhaustive D_B(T_{k-1}+1) for k = 5..12; d_B(lambda^(k)) = (k-1)(k-3) by theory-free iteration k = 5..200.
CROSS-CELL: consistent with C1 (cyclic set, single k-cycle), C3(a) bound; C2 N/A.
CEX SEARCH: see section 4 below; no counterexample to any lower-bound step or lemma.
OTHER ISSUES: (1) UPPER bound for all partitions unproved for k >= 13 (Step 9, declared GAP) — outside this gate. (2) Cosmetic: file paths "out/code/..." in proof vs code/ in the subject; "stuck.md" referenced but not supplied. (3) Lemma 4(a) "period k" needs gamma_j pairwise distinct (true: distinct diagrams; unstated; not used).
RAN: see section 5 below.
```

---

## 1. Checklist (full reasons)

Part G

- **G1 PASS.** TARGET (brief): for every k >= 5, lambda^(k) = (k-2,k-2,k-3,k-4,...,3,2,2,1) of n = T_{k-1}+1 has d_B = (k-1)(k-3), orbit tracked symbolically; hence D_B(T_{k-1}+1) >= (k-1)(k-3). Proof line 1 and Step 8.3 prove exactly this, for every k >= 5, with equality (not just >=) for d_B(lambda^(k)). The parts listed in 8.1 (row 1 = k-2, row i = k-i for 2 <= i <= k-2, row k-1 = 2, row k = 1) coincide with the target's partition (checked in code for k = 5..200 by comparing the diagram S(1;k-1,k) with the target list). Definitions used (shift with s = number of parts before removal, cyclic, d_B as first-cyclic time) are the statement's.
- **G2 PASS.** Word search for clearly/obviously/similarly/routine/by symmetry/WLOG: none. "This is standard" (0.1) is followed by an adequate argument. "By the induction in Lemma 7" (8.2) legitimately reuses a written proof whose hypotheses hold (h_0 = 1, offsets k-2, k-1 in {2..k-1}).
- **G3 PASS.** k = 5: lambda = (3,3,2,2,1), m = 3, t* = 7, B^7 = (5,4,2), B^8 = (4,3,3,1) = gamma_3; d_B = 8 = 4*2. Lemma 7 needs k >= 4, gamma_3 needs k-1 >= 3; both hold for k >= 5. Degenerate ellipsis in the target for k = 5 ("k-4,...,3" empty) is resolved by 8.1's row description and the k = 5 example.
- **G4 PASS.** See Step 7 notes: w(t) <= m-2 for t <= t* keeps both offsets in {2..k-1}, so closedness (Lemma 6(a)) and hence Y(B^{t+1}) = rho(Y(B^t)) (Lemma 2(c)) persist; energy constant E_min+1. At t* the step is a wrap step, an offset becomes 1, rho(Y) is not closed, energy drops by >= 1 (integer valued), which by Lemma 3 makes B^{t*} non-cyclic.
- **G5 PASS.** All k-dependence is symbolic: tau_j = (k-1-h_0)+(j-1)(k-1); t* = tau_{k-3} = k^2-4k+2; t* = k^2-4k+2 = 1-4+2 = -1 (mod k-1) so h_{t*} = k-1; t*-1 = k^2-4k+1 = 1 (mod k) so b_{t*} = 1. Re-derived by hand and confirmed at every t for k = 5..80.
- **G6 PASS.** Chain: Step 1 -> Lemma 2 -> Lemma 3/Cor 3' -> Lemma 4(a) -> Lemma 5 (energy count) -> Lemma 6 -> Lemma 7 induction -> Step 8. No step uses the target or the upper bound. Nothing cited.
- **G7 PASS.** Proof is symbolic; code is sanity only. Both subject scripts are stdlib, integer-only; reruns 7.61 s (orbit, k = 5..60) and 2.04 s (exhaustive, k = 5..11). No floating point anywhere.
- **G8 PASS.** No external results used; the rotation/energy machinery (known in the literature in similar form) is fully re-proved here.
- **G9 PASS.** Proof line 1, Step 9 and Step 10, and claims.md (R9, R10 = GAP) state exactly what is and is not proved.

Part S

- **S1 PASS (lower half); upper half N/A.** Explicit lambda^(k) with d_B = F(k) for every k >= 5. That F(k) = D_B needs the upper half (separate gate); my exhaustive table agrees for k = 5..12.
- **S2 PASS.** Referee's independent exhaustive computation (Kahn peeling for the cyclic set, reverse BFS for d_B; no theory assumed):

  | k | n | #partitions | D_B | F(k) | d_B(lambda^(k)) | #maximisers | cycles |
  |---|---|---|---|---|---|---|---|
  | 5 | 11 | 56 | 8 | 8 | 8 | 3 | 1 of length 5 |
  | 6 | 16 | 231 | 15 | 15 | 15 | 12 | 1 of length 6 |
  | 7 | 22 | 1002 | 24 | 24 | 24 | 62 | 1 of length 7 |
  | 8 | 29 | 4565 | 35 | 35 | 35 | 288 | 1 of length 8 |
  | 9 | 37 | 21637 | 48 | 48 | 48 | 1310 | 1 of length 9 |
  | 10 | 46 | 105558 | 63 | 63 | 63 | 5862 | 1 of length 10 |
  | 11 | 56 | 526823 | 80 | 80 | 80 | 26399 | 1 of length 11 |
  | 12 | 67 | 2679689 | 99 | 99 | 99 | 119871 | 1 of length 12 |

  k = 5 maximisers: (3,3,2,2,1), (3,3,2,1,1,1), (3,2,2,2,1,1). lambda^(k) is a maximiser in every case; it is not the unique global maximiser, and the proof only claims uniqueness on the level E_min+1 (confirmed for k = 4..25).
- **S3 PASS (lower half).** Witness proved symbolically for every k >= 5 including k = 5. The "every partition / (n) / (1^n) / cyclic starts" requirement belongs to the upper half: N/A here.
- **S4 PASS.** Entry time: Cor. 3' shows d_B = t iff B^t cyclic and B^{t-1} not, and B^{t*} is shown non-cyclic by the strict energy drop, B^{t*+1} = gamma_3 cyclic. s: Step 1 uses s = number of parts of lambda. Sorting: Lemma 2 handles the unsorted case (energy drop). Cycle of length k: end state gamma_3 is on the unique k-cycle; no fixed point assumed. No finite-k inference.
- **S5 PASS.** Lemma 4 matches gated C1 exactly; my code confirms cyclic set = {gamma_j}, one cycle of length k, k = 5..12. C3(a): (k-1)(k-3) = k^2-4k+3 <= k^2-2k-1 iff k >= 2. C2: no constraint.
- **S6 N/A.** No values in the statement for this family; S2 table used.

## 2. Per-step notes (reason each step holds)

- **Step 0.1.** Closed finite sets = Young diagrams: closedness under "left" makes each row an initial segment; closedness under "up" applied to (i+1, r_{i+1}) gives r_i >= r_{i+1} (and no empty row above a nonempty one). Converse immediate. Correct.
- **Step 0.2.** <d,r> = (r, d+1-r); left neighbour (r, d-r) = <d-1,r> exists iff r <= d-1; upper neighbour (r-1, d+1-r) = <d-1,r-1> exists iff r >= 2. Verified.
- **Step 0.3.** Y(delta_{k-1}) = {i+j <= k} = diagonals 1..k-1, T_{k-1} cells. Correct.
- **Step 0.4.** rho(i,j) = (i+1,j-1) or (1,i); preserves i+j; on diagonal d it is r -> r+1 (r < d), d -> 1. Verified; hence a bijection fixing each diagonal and Y(delta_{k-1}).
- **Step 1 (R1).** Column-1 cells (i,1), i <= s, go to row 1 columns 1..s; cell (i,j), j >= 2, goes to (i+1, j-1). So rows of rho(Y) have lengths (s, lambda_1-1, ..., lambda_s-1) = r(lambda); B(lambda) = sorted nonzero entries by definition of the shift. Correct (also random-tested, part (d)).
- **Step 2 (Lemma 2).** E(r) = E(lambda) since rho is an i+j-preserving bijection. E(B lambda) = E(r-sorted) (trailing zeros contribute 0). Sum a_i(a_i+1)/2 is rearrangement-invariant; adjacent swap of a_i < a_{i+1} changes sum i*a_i by a_i - a_{i+1} < 0; bubble sort terminates at the sorted sequence. Hence (a) and (i) iff r weakly decreasing iff r_1 >= r_2 (rest already decreasing) iff lambda_1 <= s+1 (ii); (iii) iff same, by 0.1 (zeros only at the end). (c): if sorted, B(lambda) = r minus trailing zeros, so Y(B lambda) = rho(Y lambda); otherwise integer drop >= 1. All correct; 20000 random tests pass.
- **Step 3 (Lemma 3, Cor. 3').** Energy chain around a cycle forces equalities; B of cyclic is cyclic. Cor. 3': cyclicity propagates forward, so d_B = t iff B^t cyclic and B^{t-1} not. Correct.
- **Step 4 (Lemma 4).** gamma_j closed: neighbours of <k,j> lie on diagonal k-1. (a) rho(Y(gamma_j)) = Y(delta_{k-1}) + <k,j+1>, closed, so B(gamma_j) = gamma_{j+1} (Lemma 2(c)); B^k(gamma_j) = gamma_j, so cyclic. (b) (not needed for the lower bound) CRT argument: if <d,a> absent and <d+1,c> present, some rho^t places (1,d) absent and (1,d+1) present in the closed set Y(B^t mu); contradiction. Then n in [T_{d-1}, T_d - 1] forces d = k, c = 1. Correct.
- **Step 5 (Lemma 5).** E = sum (d+1)c_d; identity E - E_min = M + sum_{d>=k}(d-k)c_d + sum_{d<=k-1}(k-1-d)m_d re-derived by substitution (uses sum_{d>=k} c_d = 1+M). (a) equality forces M = 0, c_d = 0 for d > k, c_k = 1. (b) the three cases are exhaustive; the M = 0, c_{k+1} = 1, c_k = 0 case contradicts closedness. Correct (identity random-tested). Used in Step 8 only for E(Q(k-1;1,2)) = E_min+1 and E(gamma_3) = E_min, both direct from the identity.
- **Step 6 (Lemma 6).** (a) Removing <k-1,h> keeps delta_{k-1} closed (its right/lower neighbours are on diagonal k, absent); adding <k,z> needs <k-1,z> (if z <= k-1) and <k-1,z-1> (if z >= 2), the only absent one being <k-1,h>: condition z not in {h,h+1}. (b) rho acts diagonal-wise. (c) z+ = z+1 (mod k) always; h+ = h+1 unless h = k-1 where h+ = 1 = h+1-(k-1), giving offset drop by 1 mod k. Offset in {2..k-1} iff z not in {h,h+1} (both in 1..k). Correct; closedness criterion checked exhaustively for k = 4..25.
- **Step 7 (Lemma 7).** tau_j are exactly the t with h_t = k-1; w(t) = #{tau_j <= t-1} <= m-2 for t <= t* = tau_{m-1}; offsets o - w(t) stay in {2..k-1} (no mod reduction since o >= m >= w+2 and o <= k-1). Induction: rho(S(h_t;..)) = S(h_{t+1};..) closed, so Y(B^{t+1}Q) = rho(Y(B^tQ)). At t* the (m-1)-th wrap step turns the offset m into 1: not closed, energy drops to <= E_min, hence = E_min, so B^{t*+1}Q = gamma_j (cyclic), B^{t*}Q non-cyclic (Lemma 3), d_B = t*+1 = (k-h_0)+(m-2)(k-1). Maximisation: m <= k-2, h_0 >= 1. Correct; formula verified on every closed S(h;x,y), k = 4..25, with unique maximiser Q(1;k-1,k). Cor. 7' follows (outside the lower target).
- **Step 8.1.** <k-1,1> = (1,k-1), <k,k-1> = (k-1,2), <k,k> = (k,1): rows (k-2, k-2, k-3, ..., 2, 2, 1), k parts, weakly decreasing, sum T_{k-1}-1+2 = T_{k-1}+1. Matches the target. Correct.
- **Step 8.2.** h_0 = 1, offsets o(k-1,1) = k-2, o(k,1) = k-1, m = k-2, t* = (k-2)+(k-4)(k-1) = k^2-4k+2. x_t = t-1, y_t = t (mod k), so y_t = x_t+. h_{t*} = k-1, b_{t*} = 1 (residues re-derived). Q(k-1;1,2) = delta_{k-1} minus (k-1,1) plus (1,k),(2,k-1) = (k, k-1, k-3, ..., 2), k-2 parts. B of it: s = k-2 < k-1 = lambda_1 - 1; parts minus 1 are k-1, k-2, k-4, ..., 1, plus new part k-2: (k-1,k-2,k-2,k-4,...,1) = gamma_3 (third part of delta_{k-1} raised). Energy E_min+1 > E_min: B^{t*} not cyclic. All correct; verified at every t for k = 5..80.
- **Step 8.3.** Cor. 3' with t = t*+1 gives d_B = k^2-4k+3 = (k-1)(k-3); D_B >= d_B(lambda^(k)) by definition of max. Correct.
- **Step 9.** Declared GAP (upper bound for E >= E_min+2). Outside this target; not counted.
- **Step 10.** Summary accurate.

## 3. Numerical sanity

- Subject's `verify_lower_orbit.py 5 60`: rerun, passes (7.61 s).
- Subject's `exhaustive_DB.py 5 11`: rerun, ALL MATCH (2.04 s).
- Floating point: none in proof or code.

## 4. Counterexample search (out/cex/)

- `out/cex/exhaustive_referee.py` (independent algorithm): all partitions of T_{k-1}+1, k = 5..12; D_B, all maximisers, cyclic set, cycle structure. Result: D_B = (k-1)(k-3), lambda^(k) a maximiser, cyclic set = {gamma_j} forming one k-cycle. No counterexample. Logs: `exhaustive_referee_5_11.log`, `exhaustive_referee_12.log`.
- `out/cex/orbit_and_lemmas.py 200 80 25 20000`: (a) theory-free first-repeat d_B(lambda^(k)) = (k-1)(k-3), k = 5..200; (b) Step 8.2 orbit formula at every t, B^{t*}, B^{t*+1} = gamma_3, gamma_3 cyclic, d_B(B^{t*}) = 1, k = 5..80; (c) Lemma 6(a) and Lemma 7 on all S(h;x,y), k = 4..25, unique max; (d) Lemma 2 on 20000 random partitions (n <= 300), Lemma 5 identity on 2000 random partitions of T_{k-1}+1 (4 <= k <= 30). ALL OK. Log: `orbit_and_lemmas.log`.

## 5. RAN

- subject verify_lower_orbit.py, k = 5..60, COMPLETED, real 7.61 s (`out/cex/rerun_verify_lower_orbit_5_60.log`)
- subject exhaustive_DB.py, k = 5..11, COMPLETED, real 2.04 s (`out/cex/rerun_exhaustive_DB_5_11.log`)
- referee exhaustive_referee.py, k = 5..11, COMPLETED, real 0.94 s
- referee exhaustive_referee.py, k = 12, COMPLETED, real 4.96 s, 1.15 GB RSS
- referee orbit_and_lemmas.py 200 80 25 20000, COMPLETED, real 71.29 s
(Python: /Users/defneirmakyurt/bainsahackathon/.venv/bin/python3; all scripts stdlib-only, exact integers.)
