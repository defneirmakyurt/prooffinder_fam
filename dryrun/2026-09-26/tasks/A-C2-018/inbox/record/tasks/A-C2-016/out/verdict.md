CROSS VERDICT: CONFIRMED
BRANCH: ALGEBRAIC
STATEMENT MATCH: yes
TRANSLATION: Gram matrix G of x_1..x_m is a unit-diagonal Jacobi (tridiagonal) matrix, PSD, rank <= m-1, so det G = 0. Diagonal +-1 conjugation makes all c_j >= 0 without changing theta. Step 4 is a sum-of-2x2-PSD-blocks certificate: G - cos^2(B_{k-1}) E_kk is PSD on the leading k x k block, i.e. the k-th LDL^T pivot p_k = D_k/D_{k-1} satisfies p_k >= cos^2(B_{k-1}). Step 5: if B_{m-1} < pi/2 every pivot is positive, so det G > 0, which contradicts rank <= m-1.
RED FLAGS: none
CHECKLIST:
  G1 PASS: proves exactly the chain sum over consecutive pairs, for all m >= 2, in R^(m-1), with theta = arccos|.|
  G2 PASS: every step is written out; the coefficient collection in (4c) was re-derived and holds
  G3 PASS: m = 2 (B_1 = pi/2 forced), |c| = 1, c = 0 and k = 1, 2 in Step 4 are all handled
  G4 PASS: no invariants; B_j is monotone because alpha_i >= 0
  G5 N/A: no construction is needed (the equality example is extra)
  G6 PASS: not circular; nothing is cited except the fact that m vectors in dimension m-1 are dependent
  G7 N/A: no computation is used; the float script is labelled exploratory
  G8 PASS: the only borrowed fact is standard linear algebra and is flagged as such
  G9 PASS: states SOLVED and what is established
  S1 PASS: exact statement
  S2 PASS: tight at (e1,e1,e2,..): B = pi/2 + 0 = pi/2, so every inequality is equality there
  S3 PASS: all listed cases covered
  S4 PASS: (a) arccos|.| is used; (b) consecutive pairs only; (c) the dimension is used in Step 6; (d) no distinctness assumed; (e),(f) N/A
  S5 PASS: agrees with A-C1 at m = 3
  S6 PASS: m = 2 gives 0 and m = 3 gives pi/2; no violations found
CEX SEARCH: out/cex/search.py: 85,820 exact-rational singular PSD Jacobi Gram matrices, m = 3..12. Tested the target and the Step-4 pivot bound. No violations beyond 1e-9 (min slack -1.3e-14, float noise at equality cases).
RAN: python3 out/cex/search.py, 200000 trials (85820 admissible), m=3..12, COMPLETED, 5.6 s wall (date-based timer)

---

## Full translation (algebraic lens)

Let G = (<x_i,x_j>) be the Gram matrix. By hypothesis G is tridiagonal with unit diagonal and off-diagonals
c_1..c_{m-1}. G is PSD with rank <= dim span <= m-1, so det G = 0. Conversely, any PSD matrix of rank <= m-1 is
the Gram matrix of vectors in R^(m-1). So the cell is equivalent to:

> For every unit-diagonal Jacobi matrix J with |c_j| <= 1 that is PSD and singular, sum arcsin|c_j| >= pi/2.

Signs: D = diag(+-1) gives DGD, the Gram matrix of the vectors +-x_i. Here c_j becomes |c_j| and theta does not change. The proof
uses only |c_j| (4a). This matches.

Leading minors satisfy the continuant recursion D_k = D_{k-1} - c_{k-1}^2 D_{k-2}. The pivots satisfy p_k = D_k/D_{k-1} = 1 - c_{k-1}^2/p_{k-1}.
Step 4 says that for all t in R^k, t^T G_k t >= cos^2(B_{k-1}) t_k^2. Equivalently, the Schur complement of G_{k-1} in G_k
(= p_k when G_{k-1} > 0) is >= cos^2(B_{k-1}). The proof writes t^T G_k t - cos^2(B_{k-1}) t_k^2 as
sum_j [ (a_j,-|c_j|; -|c_j|, b_j) block on (t_j,t_{j+1}) ] + nonnegative remainder. Each 2x2 block is PSD because
a_j b_j >= c_j^2 (Step 3) and a_j, b_j >= 0. The diagonal telescopes, since cos^2(B_{i-1}) + sin^2(B_{i-1}) = 1. This is a valid
chordal (tree) PSD decomposition, the standard certificate for tridiagonal matrices.

Independent re-derivation through the pivot recursion: assume p_{k-1} >= cos^2 B > 0, with B = B_{k-2} < pi/2, alpha = alpha_{k-1} and
B + alpha <= pi/2. Then p_k = 1 - c_{k-1}^2/p_{k-1} >= 1 - sin^2(alpha)/cos^2(B). This is >= cos^2(B+alpha) iff
cos^2 B - sin^2 alpha >= cos^2(B) cos^2(B+alpha). The left side equals cos(B+alpha)cos(B-alpha). Since |B-alpha| <= B+alpha <= pi/2,
cos(B-alpha) >= cos(B+alpha) >= 0, so the left side is >= cos^2(B+alpha) >= cos^2(B)cos^2(B+alpha). Hence p_k >= cos^2(B_{k-1}),
which agrees with Step 4. Numerically, the minimum over all tested pivots of p_k - cos^2(B_{k-1}) is -2.2e-16, which is float noise.

Step 5/6 in algebraic terms: if B_{m-1} < pi/2, then all pivots are > 0, so G is positive definite and rank G = m, which is impossible in
R^(m-1). The proof's downward induction on t_k is the same argument, phrased on kernel vectors.

## Per-step re-derivation
- Step 1: arccos y + arcsin y = pi/2 on [0,1], so theta_i = pi/2 - alpha_i. The target is equivalent to B_{m-1} >= pi/2. Correct.
- Step 2: (sqrt a|t| - sqrt b|s|)^2 >= 0 and sqrt(ab) >= |c|. The degenerate a = 0 or b = 0 case is handled. Correct.
- Step 3: sin(v-u) = sin v cos u - cos v sin u <= sin v cos u, with both sides >= 0, so squaring is valid. Correct.
- Step 4: hypotheses u = B_{j-1} <= v = B_j <= B_{k-1} <= pi/2 hold. sin alpha_j = |c_j|. The coefficients are 1, 1, ..., sin^2(B_{k-1})
  (checked for k = 2, where the middle range is empty). (4d) follows. Correct.
- Step 5: downward induction. At each k, B_{k-1} <= B_{m-1} < pi/2 gives cos > 0, so t_k = 0. Correct.
- Step 6: m vectors in R^(m-1) are dependent, so B_{m-1} >= pi/2. Correct. The dimension hypothesis is used exactly here.

## Equality cases
(e1,e1,e2,...,e_{m-1}): c_1 = 1, all other c_j = 0, so B = pi/2 and there is equality. The m = 3 example (e1, (e1+e2)/sqrt2, e2) gives B = pi/4 + pi/4.
The search found many near-equality instances (slack |.| < 1e-9). These come from c = 1 or from zero entries that decouple the chain; there are no violations.

## Counterexample search
out/cex/search.py (stdlib) chooses rational c_1..c_{m-2} with all leading minors > 0, computed exactly with Fractions. It sets c_{m-1}^2 = D_{m-1}/D_{m-2},
so det = 0 holds exactly, and discards the instance if c_{m-1}^2 > 1. It then checks the target and the Step-4 pivot bound with float arcsin/cos at a margin of 1e-9.
The float error is about 1e-15 per term, so the margin is safe. Result: 0 violations. Log: out/cex/log.txt.
