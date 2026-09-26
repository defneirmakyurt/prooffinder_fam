VERDICT: ACCEPT
STATEMENT MATCH: yes. The target is the LOWER half of C3(b): d_B(lambda*_k) = k^2-2k-1 for every k >= 3, hence D_B(T_k-1) >= k^2-2k-1. The proof proves exactly this (6.1, via 4.2-4.5, 5.4), for all k >= 3, symbolically. Upper bound (a) and (c) are out of scope. The proof labels them honestly: GAP for k >= 11, CHECKED for k <= 10.
FIRST PROBLEM: none. Cosmetic only: 4.2 applies 2.6 to Lambda(H,c), which needs Phi(Lambda(H,c)) = 1. The proof derives case B from Phi = 1 (3.2) but does not write the converse. It is a one-line computation: D_{k-2} is full, so g_d = 0 for d <= k-1; g_k = N_{>=k} = 1; g_d = 0 for d > k.

## Checklist

- G1 PASS: the claimed statement is "for every k >= 3, d_B(lambda*_k) = k^2-2k-1, so D_B(T_k-1) >= k^2-2k-1". This matches the target word for word, with no extra hypotheses.
- G2 PASS: every step is written out (see the per-step notes). No "clearly" or "by symmetry" gaps. "Immediate from 3.2 and 3.3" in 3.4 really is immediate (case A needs r <= k-3 < k-1).
- G3 PASS: smallest case k = 3. lambda*_3 = (2,1,1,1) (row formula of 3.5 with H = {0,1}, c = 3). Admissibility needs k-1 not in {0,1}, i.e. k >= 3. m_1 = k-2 >= 1. d = 2 = 3^2-6-1. This agrees with 8.3 (B(2,1,1,1) = (4,1) -> (3,2), which is cyclic). For k = 3, 3.3's "d* <= k-2" branch is d* = 1: diagonal 1 would need 3 cells, impossible. So it is handled.
- G4 PASS: energy is non-increasing (1.4). For the witness, the "invariant" is Phi = 1 with C(B lambda) = R(C(lambda)). It is preserved exactly while (H+t, c+t) is admissible (4.2, using the iff in 3.5 and 1.4). At failure the drop is strict (1.3(ii)), which forces Phi = 0.
- G5 PASS: the construction H = {0,1}, c = k is admissible for every k >= 3. The row lengths and sum (k-1)+(k-2)+T_{k-2}+1 = T_k - 1 hold for all k >= 3 (I checked the algebra: T_k - T_{k-2} = 2k-1).
- G6 PASS: no circularity. R2 uses gated Cell 1, which the target explicitly allows. Nothing cites C3(b).
- G7 PASS: the lower-bound proof uses no computation. The included code is stdlib, exact integers, and runs in 39 s. Finite checks are labelled as finite (8.2).
- G8 PASS: the cited items are Cell 1 (marked "assumed"; allowed by the target), the rearrangement inequality and the CRT (standard). All new work is proved in place.
- G9 PASS: section 10 separates PROVED, CHECKED (finite) and NOT PROVED (GAP for (a), equality in (b) and completeness in (c) for k >= 11).
- S1 PASS (for this half): the explicit witness is valid for every k in the stated range k >= 3. The upper half of (b) is gated separately and is not claimed as proved for k >= 11.
- S2 PASS: my exhaustive exact enumeration covered all partitions of every n <= 55 (ranks <= 10), with out/cex/referee_check.py.
  - (a) holds for every non-triangular n of rank 4..10.
  - D_B(T_k-1) = k^2-2k-1 for k = 4..10, and D_B(5) = 3.
  - The maximiser counts are 1, 6, 34, 175, 831, 3911, 18163, which match the proof's 9.x.
  - d_B(lambda*_k) = k^2-2k-1 for k = 3..10.
- S3 PASS (for this half): the range k >= 3 is stated, and the smallest k = 3 is treated (G3). Completeness for (c) is out of scope.
- S4 PASS:
  - d_B is the entry time (4.2: min t with B^t cyclic; lambda itself has Phi = 1, so it is not cyclic).
  - s counts all parts (1.2: row 0 of R(C) has length s = number of rows).
  - Sorted insertion is handled via the order-ideal / rearrangement argument.
  - The orbit is tracked symbolically in k (4.1-4.4).
- S5 PASS: R2's cyclic set (D_{k-2} plus r cells of diagonal k-1) is exactly gated Cell 1's (delta_{k-1} + k-1 of the k cells of the k-th diagonal, for r = k-1). My code checks this cyclic set against brute-force cycle detection for every n <= 55: no mismatch. For k >= 4 the value k^2-2k-1 agrees with the (a) bound. C5 at k = 3 is N/A (not gated), but the proof's D_B(5) = 3 is consistent with my table.
- S6 PASS: B(2,1,1,1,1) = (5,1) -> (4,2) -> (3,2,1) -> (3,2,1) is consistent with the B definition used (1.2). My B implementation reproduces it implicitly through the exhaustive table (n = 6 is in the enumeration).

## Per-step notes (lower-bound chain)

- 0.1-0.4: definitions. For n = T_k - 1 with k >= 2, the rank is k and r = k-1.
- 1.1: R maps diagonal d to itself by row i -> (i+1) mod (d+1). So it is injective and preserves diagonals, hence E(R(S)) = E(S).
- 1.2: row 0 of R(C) is the image of column 0, which has length s. Row i+1 has length lambda_{i+1} - 1. Verified.
- 1.3(i): lambda_1 <= s+1 makes ell weakly decreasing. Then R(C) is the diagram of the sorted positive entries, which is B(lambda).
- 1.3(ii): with lambda_1 >= s+2, the cells (1,s) are in R(C) and (0,s) is not. Swapping rows 0 and 1 changes sum i*ell_i by s-(lambda_1-1) <= -1. Sorting decreasingly does not increase sum i*ell_i (rearrangement), and the ell(ell-1)/2 terms are order-free. So E(B lambda) <= E(lambda) - 1. Verified.
- 1.4: the two cases are exhaustive, so the iff holds.
- 2.1: E = sum over d of N_{>=d}. This is the standard layer-cake identity.
- 2.2: #positions with diagonal <= d-1 is T_d. nu_d = n - T_d for d <= k-1 (T_d <= T_{k-1} < n) and 0 for d >= k (T_d >= T_k >= n).
- 2.3-2.4: Phi = sum g_d with g_d >= 0. Phi = 0 iff diagonals 0..k-2 are full and nothing lies on diagonal >= k. Both directions are checked.
- 2.5: e-parametrisation. Row i of lambda(e) is (k-1-i) + e_{i+1}, i.e. D_{k-2} row i plus the cell (i, k-1-i). The rows of D_{k-2} ∪ Q are all < k, so the bijection with Cell 1's list is correct.
- 2.6: Phi = 1 means not cyclic by R2. After one B, E is equal (then C(B) = R(C) by 1.4, and Phi stays 1) or drops (then Phi = 0, which is cyclic).
- 3.1-3.2: case B. d* > k contradicts g_k = 0 because N_{>=d} is monotone. So there is one cell on diagonal k, and diagonal k-1 has r-1 cells.
- 3.3: case A. If d* <= k-2, diagonal d* would need d*+2 cells, which is impossible. If d* = k-1, one hole on diagonal k-2 blocks two distinct positions on diagonal k-1, so r+1 <= k-2.
- 3.4: for r = k-1 case A is impossible, so every Phi = 1 partition is case B.
- 3.5: the order-ideal iff admissibility check is written out. The neighbours of diagonal-(k-1) cells lie on the full diagonal k-2. The cell (c, k-c) needs (c-1, k-c) if c >= 1 and (c, k-1-c) if c <= k-1. Row-length formula verified.
- 4.1: R permutes diagonal k-1 with period k and diagonal k with period k+1, and fixes D_{k-2} setwise. So R(S(H,c)) = S(H+1, c+1).
- 4.2: combine 3.5 (iff), 1.4 and 2.6. Induction on t gives d_B = tau, with the non-cyclicity before tau from R2.
- 4.3: the side conditions c >= 1 and c <= k-1 are automatic when alpha = gamma-1 or alpha = gamma (because 0 <= alpha <= k-1). So admissibility factorises over a in H.
- 4.4: I re-derived all four transition cases.
  - Case (2): w_t = w_{t-1} - k, which equals -1 iff gamma_t = 1.
  - Case (3): w_t = alpha_t >= 1.
  - Case (4): impossible from an admissible state.

  So the first failure has (alpha, gamma) = (0, 1), and every such time is a failure. The CRT solution is t_0 = 1 - c + (k+1)m_a, with t_0 in [1, k^2]. The case m_a = 0 forces c = 0 by admissibility. Verified.
- 4.5: the formula follows. Brute-force checks: the proof's code (k <= 10) and mine (every case-B partition for 3 <= k <= 16, 588311 partitions, d_B by definition) agree.
- 5.4 / 6.1: H = {0,1}, c = k is admissible for k >= 3. m_0 = k-1 and m_1 = k-2, so d = 1 - k + (k+1)(k-2) = k^2-2k-1. The row lengths give lambda*_k with sum T_k - 1. Hence D_B(T_k-1) >= k^2-2k-1. (Uniqueness among Phi = 1 is not needed for this target, but 5.1-5.3 are also correct.)
- 7.x (not needed for this target): 7.2 is correct, and 7.3's congruences (t ≡ -2 mod k; k+t ≡ 2 mod k+1) check out.

## Numerical checks and counterexample search (out/cex/)

- Subject code, `python3 inbox/subject/code/check_c3.py 10`: ALL OK, real 39.05 s. Log: out/cex/subject_check_c3_K10_log.txt.
- Referee code, `python3 out/cex/referee_check.py 10 150 16 20000`: ALL OK, real 86.53 s. Log: out/cex/referee_check_log.txt. It has four parts:
  1. Exhaustive: every partition of every n = 1..55. It checks d_B via the functional graph, the cyclic set against the Cell 1 characterisation, (a) for ranks 4..10, D_B(T_k-1), and the maximiser counts.
  2. Witness orbit by the definition of d_B, for k = 3..150. d_B(lambda*_k) = k^2-2k-1, and each iterate before entry equals Lambda({t, t+1} mod k, (k+t) mod (k+1)), which is non-cyclic. The iterate at F is cyclic.
  3. Lemma R4 against d_B by definition, for every case-B partition with 3 <= k <= 16 and 2 <= r <= k-1.
  4. Lemma R1 / Corollary 1.4 on 20000 random partitions with n <= 300.
- Result: no counterexample. There is no floating point anywhere.
