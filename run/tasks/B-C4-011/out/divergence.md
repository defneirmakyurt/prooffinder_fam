# Divergence: literature (B-C4-011) vs blind Phase 1 (B-C4-005, B-C4-006, B-C4-007)

Compared, not merged. No blind proof is copied into proof.md.

## Agreement (no contradictions found)

| item | blind runs | literature | this task |
|---|---|---|---|
| Value F(k) = (k-1)(k-3), k >= 5 | all three conjecture it, CHECKED k = 5..11 (005, 006) / 5..12 (007) | Griggs-Ho Thm 4.5 case (1) at r = 1 gives the lower bound (k-3-1)k+1+2 = (k-1)(k-3); Conj. 4.7 says it is the value; Figure 1 gives 8, 15, 24, 35 for k = 5..8 | check_r1.py: equality for k = 5..12, reproduces Figure 1 for n <= 36 |
| Extremal witness | lambda^(k) = (k-2,k-2,k-3,...,3,2,2,1), identical in 005/006/007 | identical to Griggs-Ho Thm 4.5 case (1) with r = 1 (lambda_1 = k-2, lambda_i = k-i for 2 <= i <= k-2, lambda_{k-1} = 2, lambda_k = 1) | confirmed a maximiser for k <= 12 |
| Exceptions k = 3, 4 | D_B(4) = 2, D_B(7) = 4 (005 Step 9.4; 007 stuck.md) | Figure 1: D_B(4) = 2, D_B(7) = 4; Thm 4.5 case (1) needs 1 < floor((k-1)/2), i.e. k >= 5 | reproduced |
| Number of maximisers | 3, 12, 62, 288 for k = 5..8 (007) | not in sources | 3, 12, 62, 288, 1310, 5862, 26399, 119871 (k = 5..12) |
| Weak upper bound (k-1)(k-2) | 005 Corollary U1 (monotonicity + B-C2) | monotonicity = Akin-Davis / Griggs-Ho Thm 4.1; Griggs-Ho use it only for the weaker k^2-k (Thm 4.2) | proof.md Step 5, with the triangular input CITED from Griggs-Ho Thm 3.7 instead of assumed |
| Upper bound status | all three: GAP above the two lowest energy levels | Griggs-Ho: CONJECTURED (Conj. 4.7); Hopkins 2012, Eriksson-Jonsson 2017: still conjectural | GAP; no proof found |

## Where the approaches differ

1. Mechanism. The blind runs use the diagonal-rotation picture (cells rotate along diagonals; a "sorting" step strictly lowers an energy). This is the same mechanism as Griggs-Ho Section 2 ("diagonally circular shifting" plus "left shifting", which moves a 1 to a lower diagonal) and as the 1981 proofs surveyed by Hopkins 2012. Griggs-Ho's UPPER bounds, however, use a different tool that no blind run used: the part-count sequence seq_B(lambda) and "sandwich" patterns (x-1, x, ..., x, x+1) (Prop. 3.2, Lemmas 3.3-3.6, 4.3).
2. Exact lifetime on the level E_min+1. The blind closed forms (006 Step 12: T = t_0 + (m-1)(k-1); 007 Lemma 7: (k-h_0) + (m-2)(k-1); 005 Theorem N: a + (k-1)(r-1) + 1) are not in any source I opened. Griggs-Ho state the lower-bound orbit only as "imitating the proof of Theorem 3.1". So the blind runs supply the symbolic orbit that the literature omits.
3. Energy function. The blind energy E = sum of diagonal indices (006, 007) and the excess decomposition (006 Step 5, 007 Lemma 5) do not appear in Griggs-Ho; Griggs-Ho track instead which diagonal each 1 of the array occupies. Same idea, different bookkeeping.
4. Part-count recursion. 006 stuck.md notes s(t) = #{j >= 1 : s(t-j) >= j} once the original piles are gone. This is Bojanov's 1981 recursion (quoted in Mestrovic 2026 as a problem) and is the basis of Griggs-Ho's diagram_B. Independently found by the blind run; the literature has it.
5. Corner removal. 005 found that one-cell removal alone fails (26 bad partitions at k = 6, 894 at k = 8). This task independently recomputed it (26, 146, 894, 4927, 27660 for k = 6..10) and adds that the corner-removal bound is exactly (k-1)(k-2) at its worst for k = 6..10, so it cannot save even one step. The blind proposal of a "time-shifted" removal (005 stuck.md) is not in the literature.

## Contradictions

None. Every numerical value in the blind runs that I could compare (D_B for k = 3..12 at r = 1, maximiser counts k = 5..8, the witness) agrees with Griggs-Ho and with out/code/check_r1.py.

## Provenance of ideas

- From the blind run only: level-1 exact lifetime formulas; energy excess decomposition; lap lemma (006 Step 11); time-shifted corner removal idea (005).
- From the literature only: identification of the target as Griggs-Ho Conj. 4.7 at r = 1; the sandwich-pattern machinery; the published bounds k^2-k and k^2-2k-1 and the observation that both are weaker than (k-1)(k-2) at r = 1; status reports (Hopkins 2012, Eriksson-Jonsson 2017).
- Both, found independently: the diagonal-rotation mechanism; monotonicity (005 Lemma M = Akin-Davis Thm 3(c)); the witness lambda^(k); the part-count recursion.
- New here: extended exhaustive check to k = 12 with maximiser counts to k = 12 (007 also reached k = 12 for the maximum); the quantitative statement that static corner removal is useless for 6 <= k <= 10 (max_lambda min_nu d_B(nu) = (k-1)(k-2)).
