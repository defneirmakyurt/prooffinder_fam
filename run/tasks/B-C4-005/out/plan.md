# Plan: B-C4-005 (BLIND, Phase 1)

Target: D_B(T_{k-1}+1) = F(k) for every k >= 5, both bounds.
Conjectured formula (from exhaustive data k = 5..11): F(k) = (k-1)(k-3) = k^2 - 4k + 3.
(Exceptions below the range: k = 3 gives 2, k = 4 gives 4; not part of the target.)

Notation: n = T_{k-1}+1; cells (i,j); diagonal d(i,j) = i+j-1; position pos(i,j) = i.
D(p,Q) = {d <= k-2} u {d = k-1, pos != p} u {d = k, pos in Q}  ("near state" when |Q| = 2).

## Ladder

- R1 (Lemma C) A partition of n is cyclic iff its diagram contains delta_{k-1}.
  Uses B-C1 (r = 1). Status: PROVED (proof.md Step 1).
- R2 (Lemma R) If s(lambda) >= lambda_1 - 1 then B(lambda) = (s, lambda_1-1, ..., lambda_s-1) and the map
  (i,j) -> (i+1,j-1) (j >= 2), (i,1) -> (1,i) is a bijection of diagrams preserving diagonals,
  rotating positions p -> p+1 (p < d), d -> 1 on diagonal d. Status: PROVED (Step 2).
- R3 (Lemma S) For a partition with diagram D(p,Q), k >= 4: (iii) p = k-1 forces Q n {k-1,k} = empty;
  (i) sorting (s <= lambda_1 - 2) happens iff p = k-1 and 1 in Q; (ii) otherwise B rotates p and Q.
  Uses R2. Status: PROVED (Step 3).
- R4 (Lemma F) If p = k-1, Q = {1,q}, then B(lambda) = lambda(e_{q+1}) is cyclic. Uses R3, B-C1.
  Status: PROVED (Step 4).
- R5 (LOWER, Theorem L) lambda^(k) = (k-2,k-2,k-3,...,3,2,2,1) has d_B = (k-1)(k-3), every k >= 5
  (orbit tracked symbolically via CRT). Uses R1-R4. Status: PROVED (Step 5).
- R6 (Lemma M) lambda subset mu implies B(lambda) subset B(mu). Status: PROVED (Step 6).
- R7 (Corollary U1) d_B(lambda) <= min_c d_B(lambda \ c) <= (k-1)(k-2) for all lambda |- n.
  Uses R6, R1, B-C1, B-C2 (at k-1). Status: PROVED (Step 7).  (Weaker than target by k-1.)
- R8 (Theorem N) Every near state (diagram D(p,Q), |Q| = 2) has d_B <= (k-1)(k-3), k >= 5.
  Uses R1-R4. Status: PROVED (Step 8).
- R9 (Reduction) Every partition lambda of n has d_B(lambda) <= (k-1)(k-3), all k >= 5
  (needs: transient time before reaching near states is compensated). Status: GAP.
  Finite evidence: exhaustive check k = 5..11 CHECKED (proves nothing for k >= 12).
- R10 (TARGET) D_B(T_{k-1}+1) = (k-1)(k-3) for all k >= 5. Uses R5, R9.
  Status: GAP (lower half PROVED for all k >= 5; upper half proved only as (k-1)(k-2), and exactly
  for near states; exact equality CHECKED for 5 <= k <= 11).
