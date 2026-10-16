**Statement proved.** For every integer m >= 2 and all unit vectors x_1, ..., x_m in R^(m-1) with <x_i, x_j> = 0 whenever |i-j| >= 2, we have sum_{i=1}^{m-1} theta(x_i, x_{i+1}) <= (m-2) pi/2, where theta(x,y) = arccos|<x,y>| in [0, pi/2].

Status: **cell solved** (complete proof, no computation relied on). Route: Gram matrix, rank, determinant recursion (algebraic branch); one elementary trigonometric identity is borrowed from analysis/trigonometry (Step 4).

## Notation
G is the m x m Gram matrix, G_ij = <x_i, x_j>. For 1 <= i <= m-1 put c_i = <x_i, x_{i+1}> and theta_i = theta(x_i, x_{i+1}) = arccos|c_i| in [0, pi/2], so c_i^2 = cos^2 theta_i. For 0 <= k <= m let D_k be the determinant of the leading principal k x k submatrix G^(k) of G (rows and columns 1..k), with D_0 := 1. For 1 <= k <= m-1 put alpha_k = theta_1 + ... + theta_k - (k-1) pi/2.

## Step 1 (rank). D_m = det G = 0.
Let X be the (m-1) x m real matrix whose j-th column is x_j. Then G = X^T X. Hence rank G <= rank X <= m-1 < m, so the m x m matrix G is singular and det G = 0. Since G^(m) = G, D_m = 0.

## Step 2 (structure and recursion).
Since each x_i is a unit vector, G_ii = 1. By hypothesis G_ij = 0 when |i-j| >= 2; G_{i,i+1} = G_{i+1,i} = c_i. So G is symmetric tridiagonal with unit diagonal, and so is every G^(k). D_1 = det[1] = 1.
Claim: for 1 <= k <= m-1, D_{k+1} = D_k - c_k^2 D_{k-1}.
Proof. Expand det G^(k+1) along its last row (row k+1). Its only nonzero-possible entries are (k+1,k) = c_k and (k+1,k+1) = 1 (entries (k+1,j), j <= k-1, vanish since |k+1-j| >= 2). The (k+1,k+1) cofactor is (+1) det G^(k) = D_k. The (k+1,k) cofactor is (-1)^{(k+1)+k} det M = -det M, where M is G^(k+1) with row k+1 and column k deleted. M is k x k; its columns are columns 1..k-1 of G^(k) followed by the column (G_{1,k+1}, ..., G_{k,k+1})^T = (0, ..., 0, c_k)^T (entries i <= k-1 vanish because |i-(k+1)| >= 2). Expanding det M along this last column: the only nonzero-possible entry is at position (k,k) of M, with sign (-1)^{2k} = +1, and deleting row k and column k of M leaves exactly G^(k-1) (rows and columns 1..k-1). So det M = c_k D_{k-1} (for k = 1, M = [c_1] and D_0 = 1, consistent). Therefore D_{k+1} = 1*D_k + c_k * (-(c_k D_{k-1})) = D_k - c_k^2 D_{k-1}. QED.
Using c_k^2 = cos^2 theta_k: D_{k+1} = D_k - cos^2(theta_k) D_{k-1}.   (*)

## Step 3 (proof by contradiction; partial sums).
Suppose, for contradiction, that T := theta_1 + ... + theta_{m-1} > (m-2) pi/2. Fix 1 <= k <= m-1.
- Lower bound: theta_1 + ... + theta_k = T - (theta_{k+1} + ... + theta_{m-1}) > (m-2) pi/2 - (m-1-k) pi/2 = (k-1) pi/2, using theta_i <= pi/2 for the m-1-k removed terms (the sum is empty, value 0, when k = m-1). Hence alpha_k > 0.
- Upper bound: theta_1 + ... + theta_k <= k pi/2, so alpha_k <= pi/2.
Thus alpha_k in (0, pi/2] and sin alpha_k > 0 for every 1 <= k <= m-1.
Also alpha_{k+1} = alpha_k + theta_{k+1} - pi/2 for 1 <= k <= m-2 (from the definition).

## Step 4 (trigonometric lemma).
Let a in (0, pi/2], t in [0, pi/2], and b := a + t - pi/2 with b in (0, pi/2]. Then
 (i) sin a sin(a+t) - cos t = cos a sin b >= 0;
 (ii) cos^2(a+t) = sin^2 b and sin^2(a+t) = cos^2 b.
Proof. a + t = pi/2 + b, so sin(a+t) = cos b and cos(a+t) = -sin b, giving (ii). Also t = pi/2 + b - a, so cos t = cos(pi/2 + (b-a)) = -sin(b-a) = sin(a-b) = sin a cos b - cos a sin b (angle-subtraction formula). Hence sin a sin(a+t) - cos t = sin a cos b - sin a cos b + cos a sin b = cos a sin b, which is >= 0 since a, b in [0, pi/2]. QED.
Consequence: since cos t >= 0 (t in [0,pi/2]) and 0 <= cos t <= sin a sin(a+t) by (i), squaring gives cos^2 t <= sin^2 a * sin^2(a+t) = sin^2 a * cos^2 b.   (**)

## Step 5 (invariant). Under the assumption of Step 3, for every 1 <= k <= m-1:
  P(k):  D_k > 0 and D_{k+1} >= sin^2(alpha_k) * D_k > 0.
Proof by induction on k.
- k = 1: D_1 = 1 > 0 and by (*), D_2 = D_1 - cos^2(theta_1) D_0 = 1 - cos^2 theta_1 = sin^2 theta_1 = sin^2(alpha_1) D_1, and sin^2 alpha_1 > 0 by Step 3, so D_2 > 0.
- Step k -> k+1 (1 <= k <= m-2): assume P(k), so D_k > 0, D_{k+1} > 0 and D_k <= D_{k+1} / sin^2(alpha_k) (division legitimate as sin alpha_k > 0). Apply Step 4 with a = alpha_k in (0,pi/2], t = theta_{k+1} in [0,pi/2]; then b = alpha_k + theta_{k+1} - pi/2 = alpha_{k+1}, which lies in (0,pi/2] by Step 3. Then, using (*) for the equality, D_k <= D_{k+1}/sin^2(alpha_k) together with cos^2 theta_{k+1} >= 0 for the first inequality, and (**) (with cos^2 b = cos^2 alpha_{k+1}) together with D_{k+1} > 0 for the second:
  D_{k+2} = D_{k+1} - cos^2(theta_{k+1}) D_k
          >= D_{k+1} - cos^2(theta_{k+1}) D_{k+1} / sin^2(alpha_k)
          >= D_{k+1} - sin^2(alpha_k) cos^2(alpha_{k+1}) D_{k+1} / sin^2(alpha_k)
          = (1 - cos^2 alpha_{k+1}) D_{k+1} = sin^2(alpha_{k+1}) D_{k+1} > 0,
  the last inequality because D_{k+1} > 0 and sin alpha_{k+1} > 0 (Step 3). Together with D_{k+1} > 0 this is P(k+1). QED.

## Step 6 (conclusion).
P(m-1) gives D_m >= sin^2(alpha_{m-1}) D_{m-1} > 0, contradicting D_m = 0 (Step 1). Hence the assumption of Step 3 is false: sum_{i=1}^{m-1} theta(x_i, x_{i+1}) = T <= (m-2) pi/2. This holds for every m >= 2.

## Edge cases
- m = 2: the hypothesis on |i-j| >= 2 is vacuous; the induction of Step 5 consists only of the base case k = 1 = m-1, which gives D_2 = sin^2 theta_1 > 0 if theta_1 > 0, contradicting D_2 = 0; hence theta_1 = 0 = (m-2) pi/2. (Directly: x_2 = +-x_1 in R^1.)
- Repeated vectors / theta_i = 0 or pi/2 are allowed throughout: only theta_i in [0,pi/2] was used.
- No sign normalisation of the c_i is needed: only c_i^2 enters (Step 2).
- Sharpness (not required): equality is attained, e.g. m = 3, x_1 = x_2 = e_1, x_3 = e_2 in R^2 gives theta_1 + theta_2 = 0 + pi/2 = pi/2.

## What is established
The full cell statement, for all m >= 2, with no extra hypotheses. No computation is used in the proof (a floating-point sanity script in out/tmp/ was guidance only).
