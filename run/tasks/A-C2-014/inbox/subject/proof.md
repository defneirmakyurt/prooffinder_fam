For every integer m >= 2 and all unit vectors x_1, ..., x_m in R^(m-1) with <x_i, x_j> = 0 whenever |i-j| >= 2, we have sum_{i=1}^{m-1} theta(x_i, x_{i+1}) <= (m-2) pi/2, where theta(x,y) = arccos|<x,y>|.

Status: cell A-C2 SOLVED (complete proof, no computation used). Branch: ANALYSIS (weighted AM-GM with trigonometric weights = a "potential" splitting of the quadratic form); the final step borrows one fact from linear algebra (m vectors in R^(m-1) are linearly dependent).

## Notation

For 1 <= i <= m-1 put c_i = <x_i, x_{i+1}>. Since x_i, x_{i+1} are unit vectors, Cauchy–Schwarz gives |c_i| <= 1. Put
alpha_i = arcsin|c_i| in [0, pi/2],   B_0 = 0,   B_j = alpha_1 + ... + alpha_j (1 <= j <= m-1).
So sin(alpha_i) = |c_i|, and 0 = B_0 <= B_1 <= ... <= B_{m-1} because every alpha_i >= 0.

## Step 1 (R1: reformulation)
For y in [0,1], arccos y + arcsin y = pi/2 (both sides are continuous on [0,1]; if arcsin y = s in [0, pi/2], then cos(pi/2 - s) = sin s = y with pi/2 - s in [0, pi/2], the range of arccos, so arccos y = pi/2 - s). With y = |c_i|:
theta(x_i, x_{i+1}) = pi/2 - alpha_i.
Hence sum_{i=1}^{m-1} theta(x_i,x_{i+1}) = (m-1) pi/2 - B_{m-1}, and the target inequality is equivalent to
(*)  B_{m-1} >= pi/2.

## Step 2 (R2: weighted AM-GM)
Claim: if a, b >= 0, c real and ab >= c^2, then for all real t, s: 2|c||t s| <= a t^2 + b s^2.
Proof. If a = 0 or b = 0 then c^2 <= ab = 0, so c = 0 and the right side is >= 0. If a, b > 0, then a t^2 + b s^2 - 2 sqrt(ab)|t||s| = (sqrt(a)|t| - sqrt(b)|s|)^2 >= 0, and sqrt(ab) >= |c|, so a t^2 + b s^2 >= 2 sqrt(ab)|ts| >= 2|c||ts|.

## Step 3 (R3: angle inequality)
Claim: if 0 <= u <= v <= pi/2 then cos(u) sin(v) >= sin(v - u) >= 0, hence cos^2(u) sin^2(v) >= sin^2(v - u).
Proof. By the subtraction formula, sin(v-u) = sin v cos u - cos v sin u. Since u, v in [0, pi/2], cos v >= 0 and sin u >= 0, so cos v sin u >= 0 and sin(v - u) <= sin v cos u. Also v - u in [0, pi/2], so sin(v-u) >= 0. Squaring the inequality 0 <= sin(v-u) <= cos u sin v between nonnegative numbers preserves it.

## Step 4 (R4: key lemma)
Claim: let 1 <= k <= m and suppose B_{k-1} <= pi/2. Then for every (t_1, ..., t_k) in R^k,
  || sum_{i=1}^k t_i x_i ||^2 >= cos^2(B_{k-1}) t_k^2.
Proof. If k = 1: ||t_1 x_1||^2 = t_1^2 = cos^2(B_0) t_1^2. Now let k >= 2.
(4a) Expand the norm using ||x_i|| = 1 and <x_i, x_j> = 0 for |i-j| >= 2 (the hypothesis; for |i-j| = 1 the inner product is c_{min(i,j)}):
  || sum_{i=1}^k t_i x_i ||^2 = sum_{i=1}^k t_i^2 + 2 sum_{j=1}^{k-1} c_j t_j t_{j+1}
                              >= sum_{i=1}^k t_i^2 - 2 sum_{j=1}^{k-1} |c_j| |t_j t_{j+1}|.
(4b) For each 1 <= j <= k-1 set a_j = cos^2(B_{j-1}) >= 0 and b_j = sin^2(B_j) >= 0. Since 0 <= B_{j-1} <= B_j <= B_{k-1} <= pi/2 and B_j - B_{j-1} = alpha_j, Step 3 with u = B_{j-1}, v = B_j gives a_j b_j >= sin^2(alpha_j) = c_j^2. By Step 2,
  2 |c_j| |t_j t_{j+1}| <= cos^2(B_{j-1}) t_j^2 + sin^2(B_j) t_{j+1}^2.
(4c) Summing over j = 1..k-1 and collecting the coefficient of each t_i^2:
  - i = 1: only the j = 1 term contributes, coefficient cos^2(B_0) = 1;
  - 2 <= i <= k-1: j = i contributes cos^2(B_{i-1}) and j = i-1 contributes sin^2(B_{i-1}); total 1;
  - i = k: only j = k-1 contributes, coefficient sin^2(B_{k-1}).
  So 2 sum_{j=1}^{k-1} |c_j||t_j t_{j+1}| <= sum_{i=1}^{k-1} t_i^2 + sin^2(B_{k-1}) t_k^2.
(4d) Combining with (4a): || sum_{i=1}^k t_i x_i ||^2 >= t_k^2 - sin^2(B_{k-1}) t_k^2 = cos^2(B_{k-1}) t_k^2.

## Step 5 (R5: independence when the angle budget is small)
Claim: if B_{m-1} < pi/2 then x_1, ..., x_m are linearly independent.
Proof. Suppose sum_{i=1}^m t_i x_i = 0. We show t_k = 0 for k = m, m-1, ..., 1 by downward induction. Assume t_{k+1} = ... = t_m = 0 (vacuous for k = m). Then sum_{i=1}^k t_i x_i = 0. Because B_{k-1} <= B_{m-1} < pi/2 (monotonicity of B), Step 4 applies and gives 0 >= cos^2(B_{k-1}) t_k^2; as 0 <= B_{k-1} < pi/2 we have cos(B_{k-1}) > 0, so t_k = 0. After k = 1 all t_i = 0.

## Step 6 (R6: conclusion)
The m vectors x_1, ..., x_m lie in R^(m-1), a space of dimension m-1, so they are linearly dependent (standard linear algebra). By Step 5 (contrapositive), B_{m-1} >= pi/2, which is (*). By Step 1, sum_{i=1}^{m-1} theta(x_i,x_{i+1}) = (m-1) pi/2 - B_{m-1} <= (m-2) pi/2. QED.

## Edge cases
- m = 2: vectors in R^1, so x_2 = +-x_1, theta = 0 = (m-2) pi/2; the proof covers this (Step 5 with k = 2, 1; B_1 = alpha_1 = pi/2 forced).
- Repeated or antipodal vectors (|c_i| = 1, alpha_i = pi/2): allowed; all steps hold with B_j possibly reaching pi/2 only in Step 4, whose hypothesis is B_{k-1} <= pi/2; Step 5 only invokes it when B_{m-1} < pi/2.
- Signs of c_i play no role (only |c_i| is used).
- Equality is attained, e.g. m = 3 with x_1 = e_1, x_2 = (e_1+e_2)/sqrt2, x_3 = e_2 in R^2 (check: <x_1,x_3> = 0, angles pi/4 + pi/4 = pi/2 = (m-2) pi/2). Not needed for the proof.

## What is established / not
Established: the full target for every m >= 2. Nothing is assumed beyond the statement; no computation is used. The float script out/tmp/sanity.py is an exploratory sanity check only and nothing rests on it.
