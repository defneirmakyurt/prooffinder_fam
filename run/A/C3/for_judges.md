# Cell 3: d + 1 Lines in R^d

**Statement.** Let d >= 1. Prove that any d + 1 lines in R^d satisfy S <= (C(d+1, 2) - 1) pi/2.

**Status.** Solved. Complete written proof for every d >= 1. No step relies on computation. No published result is cited; the argument is our own.

**Proof.**

For every integer d >= 1 and all lines l_1, ..., l_{d+1} through the origin of R^d (repetitions allowed), S(l_1, ..., l_{d+1}) = sum_{i<j} theta(l_i, l_j) <= (C(d+1,2) - 1) * pi/2, where theta(l, l') = arccos|<x, x'>| for spanning unit vectors x, x'.

Tools used, all standard: the Cauchy–Schwarz inequality; the angle-addition
formulas for sin and cos; monotonicity of sin on [0, pi/2]; the identity arcsin t + arccos t = pi/2
on [0,1]; the fact that d+1 vectors in R^d are linearly dependent. No step rests on a computation.

Reading of the statement: none needed; the statement is used verbatim. "Repetitions allowed"
means some l_i may coincide and the lines may lie in a proper subspace; nothing below assumes
distinctness or that the lines span R^d.

---

## Step 0. Set-up

Fix d >= 1 and put n = d+1 (so n >= 2). Let l_1, ..., l_n be lines through the origin of R^d and
choose unit vectors x_i spanning l_i. (Replacing x_i by -x_i does not change |<x_i, x_j>|, so
theta(l_i, l_j) does not depend on the choice.) Put g_ij = <x_i, x_j>. Then g_ii = 1 and, by
Cauchy–Schwarz, |g_ij| <= |x_i||x_j| = 1, so arccos|g_ij| and arcsin|g_ij| are defined. Write
theta_ij = theta(l_i, l_j) = arccos|g_ij| for i != j.

## Step 1. Reformulation

For i != j put alpha_ij = arcsin|g_ij|, so alpha_ij = alpha_ji in [0, pi/2] and
sin(alpha_ij) = |g_ij|.

Claim: theta_ij = pi/2 - alpha_ij. Proof: let t = |g_ij| in [0,1] and u = arcsin t in [0, pi/2].
Then pi/2 - u lies in [0, pi/2], a subset of [0, pi], and cos(pi/2 - u) = sin u = t. Since arccos
is the inverse of cos restricted to [0, pi], arccos t = pi/2 - u.

Put T = sum_{1<=i<j<=n} alpha_ij. Summing the claim over the C(n,2) pairs,
  S(l_1, ..., l_n) = C(n,2) pi/2 - T.
Hence, for n = d+1,
  S <= (C(d+1,2) - 1) pi/2   if and only if   T >= pi/2.            (1)
It remains to prove T >= pi/2.

## Step 2. Lemma L

Lemma L. Let k >= 0 and a_1, ..., a_k >= 0 with D = a_1 + ... + a_k <= pi/2. Then
  sum_{j=1}^k sin(a_j) cos(D - a_j) <= sin D.

Proof, by induction on k. Throughout, each a_j is one of the non-negative summands of D, so
0 <= a_j <= D <= pi/2; hence sin(a_j) >= 0 and cos(a_j) >= 0.

k = 0: the sum is empty, and D = 0, so both sides are 0.

Step k-1 -> k (k >= 1): put D' = D - a_1 = a_2 + ... + a_k. Then 0 <= D' <= D <= pi/2, and
the numbers a_2, ..., a_k satisfy the hypothesis with sum D', so by the induction hypothesis
  sum_{j=2}^k sin(a_j) cos(D' - a_j) <= sin D'.                          (2)
By the angle-addition formula, sin D = sin(a_1 + D') = sin(a_1) cos(D') + cos(a_1) sin(D').
Since 0 <= a_1 <= D <= pi/2 we have cos(a_1) >= 0, so multiplying (2) by cos(a_1), and writing cos(D') = cos(D - a_1), gives
  sin D >= sin(a_1) cos(D - a_1) + sum_{j=2}^k cos(a_1) sin(a_j) cos(D' - a_j).     (3)
For each j >= 2, a_j is one of the non-negative summands of D', so 0 <= D' - a_j <= D' <= pi/2
and sin(D' - a_j) >= 0. By the angle-addition formula,
  cos(D - a_j) = cos(a_1 + (D' - a_j)) = cos(a_1) cos(D' - a_j) - sin(a_1) sin(D' - a_j)
               <= cos(a_1) cos(D' - a_j),
because sin(a_1) >= 0 (as 0 <= a_1 <= pi/2) and sin(D' - a_j) >= 0. Multiplying by
sin(a_j) >= 0 (as 0 <= a_j <= pi/2) gives cos(a_1) sin(a_j) cos(D' - a_j) >= sin(a_j) cos(D - a_j).
Substituting in (3):
  sin D >= sin(a_1) cos(D - a_1) + sum_{j=2}^k sin(a_j) cos(D - a_j) = sum_{j=1}^k sin(a_j) cos(D - a_j).
(For k = 1 the sum over j >= 2 is empty and (3) reads sin D >= sin(a_1), true with equality
since D' = 0.) This completes the induction. QED

## Step 3. Key Lemma

Key Lemma. Let n >= 2 and let alpha_ij = alpha_ji >= 0 (1 <= i != j <= n) be real numbers with
T = sum_{i<j} alpha_ij < pi/2. Put s = pi/2 - T > 0, D_i = sum_{j != i} alpha_ij, and
p_i = sin(D_i + s). Then for every i: p_i > 0 and
  sum_{j != i} sin(alpha_ij) p_j < p_i.                                  (4)

Proof.
(a) Bounds. D_i is the sum of alpha over the pairs {i,j} containing i, a sub-sum of the
non-negative terms making up T, so 0 <= D_i <= T. Hence 0 < s <= D_i + s <= T + s = pi/2 and
p_i = sin(D_i + s) > 0. Also every alpha_ij lies in [0, T], a subset of [0, pi/2), so
sin(alpha_ij) >= 0.

(b) Fix i. Let T_i' be the sum of alpha_kl over the pairs {k,l} with i not in {k,l}. The pairs
split into those containing i and those not containing i, so T = D_i + T_i'. For j != i,
  D_j = alpha_ij + sum_{k not in {i,j}} alpha_jk,
and the pairs {j,k} with k not in {i,j} are among the pairs counted in T_i'; all terms being
non-negative, sum_{k not in {i,j}} alpha_jk <= T_i'. Therefore
  D_j + s <= alpha_ij + T_i' + pi/2 - D_i - T_i' = pi/2 - (D_i - alpha_ij).
Here D_i - alpha_ij >= 0 (a sum of non-negative terms) and D_i - alpha_ij <= D_i <= T < pi/2.
So both D_j + s and pi/2 - (D_i - alpha_ij) lie in [0, pi/2], where sin is non-decreasing; thus
  p_j = sin(D_j + s) <= sin(pi/2 - (D_i - alpha_ij)) = cos(D_i - alpha_ij).

(c) Multiplying by sin(alpha_ij) >= 0 and summing over j != i,
  sum_{j != i} sin(alpha_ij) p_j <= sum_{j != i} sin(alpha_ij) cos(D_i - alpha_ij) <= sin(D_i),
the last step by Lemma L (Step 2) applied to the k = n-1 numbers a_j = alpha_ij (j != i), which are
non-negative with sum D_i <= T < pi/2.

(d) Finally 0 <= D_i < D_i + s <= pi/2 (by (a) and s > 0), and sin is strictly increasing on
[0, pi/2], so sin(D_i) < sin(D_i + s) = p_i. With (c) this gives (4). QED

## Step 4. Weighted diagonal dominance

Lemma W. Let G be a real n x n matrix with G_ii = 1 for all i, and suppose there are p_1, ..., p_n > 0
with sum_{j != i} |G_ij| p_j < p_i for every i. If c in R^n satisfies G c = 0, then c = 0.

Proof. Suppose G c = 0 with c != 0. Let r = max_i |c_i| / p_i; then r > 0 because some c_i != 0
and all p_i > 0. Choose i with |c_i| = r p_i. Row i of G c = 0 reads c_i = - sum_{j != i} G_ij c_j,
so, using |c_j| <= r p_j for all j,
  r p_i = |c_i| <= sum_{j != i} |G_ij| |c_j| <= r sum_{j != i} |G_ij| p_j < r p_i,
where the strict inequality uses r > 0 and the hypothesis. This is a contradiction. QED

## Step 5. A kernel vector of the Gram matrix

Let G = (g_ij) be the n x n Gram matrix of x_1, ..., x_n from Step 0. Since n = d+1 vectors in the
d-dimensional space R^d are linearly dependent, there is c = (c_1, ..., c_n) != 0 with
sum_j c_j x_j = 0. Taking the inner product with x_i gives sum_j g_ij c_j = 0 for each i, that is,
G c = 0 with c != 0.

## Step 6. Conclusion

Suppose, for contradiction, that T < pi/2, where T is as in Step 1. The numbers alpha_ij from
Step 1 satisfy alpha_ij = alpha_ji >= 0, and n = d+1 >= 2, so the Key Lemma (Step 3) gives
p_1, ..., p_n > 0 with sum_{j != i} sin(alpha_ij) p_j < p_i for all i. By Step 1,
|g_ij| = sin(alpha_ij) for i != j, and g_ii = 1. So the Gram matrix G satisfies the hypotheses of
Lemma W (Step 4), whence G c = 0 forces c = 0. This contradicts Step 5. Therefore T >= pi/2, and by
the equivalence (1) of Step 1,
  S(l_1, ..., l_{d+1}) <= (C(d+1,2) - 1) pi/2.
Since d >= 1 and the lines were arbitrary, this proves the statement.

Edge and degenerate cases, checked against the argument:
- d = 1: n = 2, both lines equal R^1, g_12 = +-1, alpha_12 = pi/2 = T, and S = 0 = (C(2,2) - 1) pi/2.
  The general argument also covers it (Steps 1–6 only need n >= 2).
- Repeated lines: if l_i = l_j then |g_ij| = 1, alpha_ij = pi/2; this is allowed in Step 1
  (alpha_ij in [0, pi/2]). Step 3 is only invoked under T < pi/2, where no alpha_ij equals pi/2;
  this is consistent, since the conclusion is that T < pi/2 is impossible.
- Lines spanning a proper subspace: Step 5 uses only linear dependence of d+1 vectors in R^d,
  which holds regardless.
- No step divides by a quantity that could vanish: the only division is by p_i > 0 (Step 4),
  with positivity from Step 3(a).

## Step 7. Sharpness (remark, not needed for the target)

Equality holds for x_k = e_k (k = 1..d) and x_{d+1} = e_1: the only non-orthogonal pair is {1, d+1},
with alpha = pi/2, so T = pi/2 and S = (C(d+1,2) - 1) pi/2. For d = 2, three lines at mutual angle
pi/3 also give equality (alpha = pi/6 for each of the 3 pairs, T = pi/2). So the bound cannot be
improved for any d >= 1 (for d = 1 both sides are 0).

## What is established

The statement on the first line is proved in full, for every d >= 1.
