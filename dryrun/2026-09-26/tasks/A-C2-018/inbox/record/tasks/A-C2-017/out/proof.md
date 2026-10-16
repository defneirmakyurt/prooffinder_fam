For every integer m >= 2 and all unit vectors x_1, ..., x_m in R^(m-1) with <x_i, x_j> = 0 whenever |i - j| >= 2, we have sum_{i=1}^{m-1} theta(x_i, x_{i+1}) <= (m - 2) pi/2, where theta(x, y) = arccos|<x, y>|.

Status: cell A-C2 SOLVED. This is a complete proof for the full range m >= 2. It uses no computation and cites nothing.
Provenance: this is an analyst reproduction. The forward Gram–Schmidt route is the one used in A-C2-003 (literature) and
A-C2-015 (adversary). The board proof is A-C2-002, which uses a backward projection. This text was written here and checked line by line.

## Notation
c_i = <x_i, x_{i+1}> for 1 <= i <= m-1. By Cauchy–Schwarz (unit vectors), |c_i| <= 1. Put phi_i = arcsin|c_i| in [0, pi/2], so
sin phi_i = |c_i|. For 0 <= k <= m let V_k = span(x_1, ..., x_k), with V_0 = {0}, and let P_k be the orthogonal projection onto V_k.

## Step 1 (reformulation)
Let t in [0,1] and s = arcsin t in [0, pi/2]. Then pi/2 - s lies in [0, pi/2] and cos(pi/2 - s) = sin s = t. Since arccos is the
inverse of cos on [0, pi], arccos t = pi/2 - s. So theta(x_i, x_{i+1}) = arccos|c_i| = pi/2 - phi_i, and
  sum_{i=1}^{m-1} theta(x_i, x_{i+1}) = (m-1) pi/2 - Phi,  where Phi = phi_1 + ... + phi_{m-1}.
The target is therefore equivalent to Phi >= pi/2. Suppose, for contradiction, that
  (H)  Phi < pi/2.
Every phi_i >= 0, so under (H) every partial sum B_k := phi_1 + ... + phi_k (with B_0 = 0) satisfies 0 <= B_k <= Phi < pi/2. Hence cos B_k > 0.

## Step 2 (residuals)
For 1 <= k <= m put r_k = x_k - P_{k-1} x_k and t_k = |r_k| >= 0. We prove the following by induction on k = 1, ..., m:
  Q(k):  t_k >= cos B_{k-1}  (in particular t_k > 0 by Step 1).
Once Q(1), ..., Q(m) hold, x_1, ..., x_m are linearly independent. Indeed, t_k > 0 means x_k is not in V_{k-1}. If
sum a_j x_j = 0 with some a_j != 0, let k be the largest index with a_k != 0. Then x_k = -(1/a_k) sum_{j<k} a_j x_j lies in V_{k-1},
a contradiction. But m linearly independent vectors cannot lie in R^(m-1), which has dimension m-1. This contradiction refutes (H),
so Phi >= pi/2, and by Step 1 the sum of the theta's is <= (m-1)pi/2 - pi/2 = (m-2)pi/2. It remains to prove Q(k).

Base k = 1: V_0 = {0}, so r_1 = x_1, t_1 = 1 = cos 0 = cos B_0.

## Step 3 (the recursion; used for the step k -> k+1, 1 <= k <= m-1)
Assume Q(1), ..., Q(k), so t_1, ..., t_k > 0. Put e_j = r_j / t_j for j <= k.
(3a) e_1, ..., e_k is an orthonormal basis of V_k. Each r_j lies in V_j (x_j in V_j, P_{j-1}x_j in V_{j-1} ⊂ V_j), and r_j is orthogonal to
     V_{j-1}, by the defining property of the orthogonal projection P_{j-1}. So for i < j, e_i is in V_i ⊂ V_{j-1}, and <e_i, e_j> = 0.
     Also |e_j| = 1. These k orthonormal vectors lie in V_k, which is spanned by k vectors, so they form a basis of V_k.
(3b) x_{k+1} ⊥ V_{k-1}: V_{k-1} is spanned by x_1..x_{k-1}, and |(k+1) - j| >= 2 for j <= k-1, so <x_{k+1}, x_j> = 0 by hypothesis.
     (For k = 1, V_0 = {0} and there is nothing to prove.)
(3c) By (3a), P_k x_{k+1} = sum_{j<=k} <x_{k+1}, e_j> e_j. For j <= k-1, e_j is in V_{k-1}, so by (3b) that coefficient is 0.
     For j = k:
       <x_{k+1}, e_k> = (<x_{k+1}, x_k> - <x_{k+1}, P_{k-1} x_k>) / t_k = (c_k - 0) / t_k,
     because P_{k-1} x_k is in V_{k-1} and (3b) applies. So P_k x_{k+1} = (c_k / t_k) e_k.
(3d) Pythagoras: x_{k+1} = P_k x_{k+1} + r_{k+1} with r_{k+1} ⊥ V_k, so 1 = |x_{k+1}|^2 = c_k^2 / t_k^2 + t_{k+1}^2, i.e.
       t_{k+1}^2 = 1 - c_k^2 / t_k^2.

## Step 4 (trigonometric merge inequality)
Lemma. If B, p >= 0 and B + p < pi/2, then 0 <= sin p <= cos B · sin(B + p).
Proof. By the addition formula,
  cos B sin(B+p) - sin p = cos B (sin B cos p + cos B sin p) - sin p
                         = sin B cos B cos p + (cos^2 B - 1) sin p
                         = sin B cos B cos p - sin^2 B sin p
                         = sin B (cos B cos p - sin B sin p) = sin B cos(B + p).
This is >= 0: B is in [0, pi/2), so sin B >= 0, and B + p is in [0, pi/2), so cos(B+p) > 0. Also sin p >= 0 because p is in [0, pi/2). QED.

## Step 5 (induction step Q(k) -> Q(k+1))
Let B = B_{k-1} and p = phi_k, so that B + p = B_k < pi/2 by Step 1. By Q(k), t_k >= cos B > 0, so
  c_k^2 / t_k^2 <= sin^2 phi_k / cos^2 B <= sin^2(B + p),
where the last inequality comes from Step 4: dividing 0 <= sin p <= cos B sin(B+p) by cos B > 0 and squaring nonnegative numbers.
By (3d), t_{k+1}^2 >= 1 - sin^2(B_k) = cos^2(B_k). Since t_{k+1} >= 0 and cos B_k > 0, taking square roots gives t_{k+1} >= cos B_k. This is Q(k+1).

By induction Q(1), ..., Q(m) hold under (H), and Step 2 turns this into a contradiction. QED.

## Edge cases (G3)
- m = 2: there is a single step, k = 1 -> 2. Under (H), phi_1 < pi/2 would give t_2 > 0, i.e. x_1, x_2 independent in R^1, which is impossible.
  So phi_1 = pi/2, i.e. |c_1| = 1 and theta = 0 = (2-2)pi/2. This agrees with the direct check (x_1, x_2 = ±1).
- c_k = 0 (orthogonal neighbours): then t_{k+1} = 1, and nothing is divided by c_k or by sin phi_k.
- |c_k| = 1 (parallel or antiparallel neighbours): then phi_k = pi/2, so (H) already fails. The proof by contradiction needs no separate case.
- Repeated vectors are allowed. Independence is never assumed; it is derived under (H).
- Division by t_k only happens when t_k > 0 (Q(k)); division by cos B only when cos B > 0 (Step 1).

## Sharpness (remark, not needed)
m = 3, x_1 = e_1, x_2 = (cos s, sin s), x_3 = e_2 in R^2: theta sum = s + (pi/2 - s) = pi/2 = (m-2) pi/2, for every s in [0, pi/2].

## KNOWN GAPS
none.
