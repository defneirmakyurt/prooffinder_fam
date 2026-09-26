# Cell 2: An Orthogonality Lemma

**Statement.** Let m >= 2 and let x_1, ..., x_m be unit vectors in R^(m-1) with <x_i, x_j> = 0 whenever |i - j| >= 2. Prove that sum_{i=1}^{m-1} theta(x_i, x_{i+1}) <= (m - 2) pi/2, where theta(x, y) = arccos|<x, y>|.

**Status.** Solved. Complete written proof for every m >= 2. No step relies on computation. No published result is cited; the argument is our own.

**Proof.**

For every integer m >= 2 and all unit vectors x_1, ..., x_m in R^(m-1) with <x_i, x_j> = 0 whenever |i-j| >= 2, we have sum_{i=1}^{m-1} theta(x_i, x_{i+1}) <= (m-2) pi/2, where theta(x,y) = arccos|<x,y>|.

Only standard tools are used (Cauchy–Schwarz, elementary trigonometry, dimension counting, induction).

## Notation

For a chain x_1, ..., x_m as in the statement put c_i = <x_i, x_{i+1}> (1 <= i <= m-1). By Cauchy–Schwarz, |c_i| <= 1.
Put a_i = arcsin|c_i| in [0, pi/2]. Call a list of m unit vectors in an inner-product space of dimension m-1
satisfying <x_i,x_j> = 0 for |i-j| >= 2 an "m-chain". Write A(x) = sum_{i=1}^{m-1} a_i.

## Step 1 (reformulation)
For t in [0,1], arccos t + arcsin t = pi/2 (both sides are continuous; if s = arcsin t in [0,pi/2] then
cos(pi/2 - s) = sin s = t with pi/2 - s in [0, pi/2] = range of arccos on [0,1], so arccos t = pi/2 - s).
Hence theta(x_i,x_{i+1}) = arccos|c_i| = pi/2 - a_i, and
  sum_{i=1}^{m-1} theta(x_i,x_{i+1}) = (m-1) pi/2 - A(x).
So the target is equivalent to:  (*)  A(x) >= pi/2 for every m-chain, every m >= 2.

Note: an inner-product space of dimension k is isometric to R^k (choose an orthonormal basis, Gram–Schmidt),
and inner products are preserved by such an isometry; so (*) for chains in R^(m-1) is the same as (*) for
chains in any (m-1)-dimensional inner-product space. We use this in Step 4.

We prove (*) by induction on m.

## Step 2 (base case m = 2)
x_1, x_2 are unit vectors in R^1, so x_1, x_2 in {+1, -1} and |c_1| = |x_1 x_2| = 1. Thus a_1 = arcsin 1 = pi/2 and
A(x) = pi/2 >= pi/2. (Equivalently theta(x_1,x_2) = 0 = (2-2) pi/2.)

## Step 3 (inductive step, degenerate case)
Let m >= 3 and assume (*) for (m-1)-chains. Let x_1..x_m be an m-chain. If |c_{m-1}| = 1 then a_{m-1} = pi/2
and, as every a_i >= 0, A(x) >= a_{m-1} = pi/2. Done.

## Step 4 (inductive step, reduction; |c_{m-1}| < 1)
Write c = c_{m-1}, and let W = x_m^perp = {v in R^(m-1) : <v, x_m> = 0}; since x_m != 0, dim W = m-2 >= 1.
Define u = x_{m-1} - c x_m. Then
  <u, x_m> = c - c<x_m,x_m> = 0, so u in W;
  |u|^2 = 1 - 2c^2 + c^2 = 1 - c^2 > 0.
Now |c| = sin a_{m-1} with a_{m-1} in [0, pi/2), so sqrt(1-c^2) = cos a_{m-1} > 0. Let y = u / cos a_{m-1}, a unit vector in W.
Define z_j = x_j for 1 <= j <= m-2 and z_{m-1} = y.
 (4a) z_j in W for j <= m-2: <x_j, x_m> = 0 because |j - m| >= 2.
 (4b) All z_j are unit vectors (hypothesis, and construction of y).
 (4c) Orthogonality for |i-j| >= 2 within z: if i,j <= m-2 this is the hypothesis on x. If j = m-1 and i <= m-3, then
      <x_i, y> = (<x_i,x_{m-1}> - c<x_i,x_m>)/cos a_{m-1} = (0 - 0)/cos a_{m-1} = 0,
      since |i-(m-1)| >= 2 and |i-m| >= 3.
 (4d) Consecutive coefficients of z: for i <= m-3, <z_i,z_{i+1}> = c_i (unchanged). For i = m-2:
      <x_{m-2}, y> = (c_{m-2} - c<x_{m-2},x_m>)/cos a_{m-1} = c_{m-2}/cos a_{m-1},
      because |(m-2)-m| = 2. Hence |<z_{m-2},z_{m-1}>| = sin a_{m-2}/cos a_{m-1}.
So z_1..z_{m-1} is an (m-1)-chain in the (m-2)-dimensional space W. Its angles are a_1, ..., a_{m-3} and
  a' = arcsin( sin a_{m-2} / cos a_{m-1} )
(the argument lies in [0,1] by Cauchy–Schwarz applied to the unit vectors z_{m-2}, z_{m-1}).
By the induction hypothesis (and the isometry remark in Step 1):
  (4e)  a_1 + ... + a_{m-3} + a' >= pi/2.
(For m = 3 the sum a_1 + ... + a_{m-3} is empty, and (4e) reads a' >= pi/2.)

## Step 5 (trigonometric lemma)
Lemma. Let alpha in [0,pi/2], beta in [0,pi/2) with sin alpha <= cos beta. Then arcsin(sin alpha / cos beta) <= alpha + beta
whenever alpha + beta < pi/2; and arcsin(sin alpha / cos beta) <= pi/2 always.
Proof. The second claim is the range of arcsin. For the first, assume alpha + beta < pi/2. Then
  sin(alpha+beta) cos beta - sin alpha
    = sin alpha cos^2 beta + cos alpha sin beta cos beta - sin alpha
    = - sin alpha sin^2 beta + cos alpha sin beta cos beta
    = sin beta (cos alpha cos beta - sin alpha sin beta)
    = sin beta cos(alpha+beta) >= 0,
since sin beta >= 0 (beta in [0,pi/2)) and cos(alpha+beta) > 0 (alpha+beta in [0,pi/2)). Dividing by cos beta > 0:
sin alpha / cos beta <= sin(alpha+beta). Both sides lie in [0,1] and arcsin is increasing on [0,1], so
arcsin(sin alpha/cos beta) <= arcsin(sin(alpha+beta)) = alpha+beta, the last equality because alpha+beta in [0,pi/2]. QED.

## Step 6 (conclusion of the inductive step)
Apply Step 5 with alpha = a_{m-2}, beta = a_{m-1} (hypotheses: beta < pi/2 as |c_{m-1}| < 1; sin alpha <= cos beta by (4d)
and Cauchy–Schwarz).
 - If a_{m-2} + a_{m-1} >= pi/2, then A(x) >= a_{m-2} + a_{m-1} >= pi/2, as all a_i >= 0.
 - If a_{m-2} + a_{m-1} < pi/2, then a' <= a_{m-2} + a_{m-1} by Step 5, so by (4e)
      A(x) = a_1 + ... + a_{m-3} + a_{m-2} + a_{m-1} >= a_1 + ... + a_{m-3} + a' >= pi/2.
Together with Step 3, (*) holds for all m-chains. By induction (base Step 2), (*) holds for every m >= 2.

## Step 7 (target)
By Step 1, sum_{i=1}^{m-1} theta(x_i,x_{i+1}) = (m-1)pi/2 - A(x) <= (m-1)pi/2 - pi/2 = (m-2)pi/2. QED.

## Remarks
- Edge cases: m = 2 (Step 2); m = 3 (empty prefix sum in (4e)); parallel/antiparallel consecutive vectors
  (Step 3); orthogonal consecutive vectors (c_i = 0, a_i = 0) need no separate treatment.
- Sharpness (not required): m=3, x_1=e_1, x_2=(cos t, sin t), x_3=e_2 in R^2 gives theta sum = t + (pi/2 - t) = pi/2 = (m-2)pi/2.
- No computation is used in the proof.
