Statement. For every integer m >= 2 and all unit vectors x_1,...,x_m in R^(m-1) with <x_i,x_j> = 0 whenever |i-j| >= 2, we have sum_{i=1}^{m-1} theta(x_i,x_{i+1}) <= (m-2) pi/2, where theta(x,y) = arccos|<x,y>|.

Status: complete proof (BLIND; only textbook linear algebra and trigonometry). No computation is used.

1. Notation. For 1 <= i <= m-1 put a_i = |<x_i,x_{i+1}>|. By Cauchy-Schwarz and |x_i| = 1, a_i in [0,1]. Put theta_i = arccos a_i in [0, pi/2] and phi_i = arcsin a_i in [0, pi/2]. Since arcsin t + arccos t = pi/2 for t in [-1,1], theta_i = pi/2 - phi_i.

2. Reduction. sum_{i=1}^{m-1} theta_i = (m-1) pi/2 - sum_i phi_i. Hence the claim is equivalent to sum_{i=1}^{m-1} phi_i >= pi/2.

3. Assume for contradiction that sum_{i=1}^{m-1} phi_i < pi/2. Put Phi_0 = 0 and Phi_k = phi_1 + ... + phi_k for 1 <= k <= m-1. Since every phi_i >= 0, 0 <= Phi_k <= Phi_{m-1} < pi/2 for all 0 <= k <= m-1.

4. Subspaces. Let V_0 = {0} and V_k = span(x_1,...,x_k) for 1 <= k <= m. Let P_k denote the orthogonal projection onto V_k, and u_k = x_k - P_{k-1} x_k (1 <= k <= m). Then u_k is orthogonal to V_{k-1}, and by Pythagoras |u_k|^2 = |x_k|^2 - |P_{k-1} x_k|^2 = 1 - |P_{k-1} x_k|^2.

5. Trigonometric lemma. If alpha, phi >= 0 and alpha + phi <= pi/2, then sin(phi) <= cos(alpha) sin(alpha+phi).
   Proof: cos(alpha) sin(alpha+phi) - sin(phi) = cos(alpha)(sin(alpha)cos(phi) + cos(alpha)sin(phi)) - sin(phi)
   = sin(alpha)cos(alpha)cos(phi) - (1 - cos^2(alpha)) sin(phi) = sin(alpha)cos(alpha)cos(phi) - sin^2(alpha) sin(phi)
   = sin(alpha) (cos(alpha)cos(phi) - sin(alpha)sin(phi)) = sin(alpha) cos(alpha+phi).
   Here sin(alpha) >= 0 because alpha in [0, pi/2], and cos(alpha+phi) >= 0 because alpha+phi in [0, pi/2]. So the difference is >= 0.

6. Inductive claim C(k), for k = 1,...,m: |P_{k-1} x_k| <= sin(Phi_{k-1}), and consequently |u_k| >= cos(Phi_{k-1}) > 0.
   (The "consequently": by step 4, |u_k|^2 = 1 - |P_{k-1}x_k|^2 >= 1 - sin^2(Phi_{k-1}) = cos^2(Phi_{k-1}); cos(Phi_{k-1}) > 0 because Phi_{k-1} in [0, pi/2) by step 3.)

7. Base k = 1: P_0 x_1 = 0 and sin(Phi_0) = 0, so C(1) holds.

8. Step. Let 2 <= k <= m and assume C(k-1); in particular u_{k-1} != 0 and |u_{k-1}| >= cos(Phi_{k-2}) > 0.
   8a. x_{k-1} = P_{k-2} x_{k-1} + u_{k-1} with P_{k-2}x_{k-1} in V_{k-2}. Hence V_{k-1} = V_{k-2} + span(u_{k-1}), and u_{k-1} is orthogonal to V_{k-2}. Therefore, for every y, P_{k-1} y = P_{k-2} y + (<y,u_{k-1}>/|u_{k-1}|^2) u_{k-1}, and the two summands are orthogonal.
   8b. x_k is orthogonal to V_{k-2}: for k = 2, V_0 = {0}; for k >= 3, V_{k-2} is spanned by x_1,...,x_{k-2}, each of index differing from k by at least 2, so each is orthogonal to x_k by hypothesis. Hence P_{k-2} x_k = 0.
   8c. <x_k, u_{k-1}> = <x_k, x_{k-1}> - <x_k, P_{k-2}x_{k-1}> = <x_k, x_{k-1}>, since P_{k-2}x_{k-1} lies in V_{k-2}, which is orthogonal to x_k by 8b.
   8d. By 8a-8c, P_{k-1} x_k = (<x_k,x_{k-1}>/|u_{k-1}|^2) u_{k-1}, so |P_{k-1}x_k| = a_{k-1}/|u_{k-1}| <= sin(phi_{k-1}) / cos(Phi_{k-2}), using a_{k-1} = sin(phi_{k-1}) and C(k-1).
   8e. Apply step 5 with alpha = Phi_{k-2}, phi = phi_{k-1}: both are >= 0 and alpha + phi = Phi_{k-1} < pi/2 (step 3). So sin(phi_{k-1}) <= cos(Phi_{k-2}) sin(Phi_{k-1}), and dividing by cos(Phi_{k-2}) > 0 gives sin(phi_{k-1})/cos(Phi_{k-2}) <= sin(Phi_{k-1}).
   8f. By 8d and 8e, |P_{k-1}x_k| <= sin(Phi_{k-1}), which is C(k).

9. By steps 6-8, u_k != 0 for every k = 1,...,m, i.e. x_k is not in V_{k-1}. Hence dim V_k = dim V_{k-1} + 1 for each k, so dim V_m = m. But V_m is a subspace of R^(m-1), so dim V_m <= m-1. Contradiction.

10. Therefore sum_i phi_i >= pi/2, and by step 2, sum_{i=1}^{m-1} theta(x_i,x_{i+1}) <= (m-2) pi/2. This holds for every m >= 2 (for m = 2 the argument reads: phi_1 < pi/2 would make x_1, x_2 independent in R^1). QED.

Remark (equality, not needed for the proof): equality holds e.g. for m = 2 (x_2 = +-x_1) and for m = 3 with x_1 = (1,0), x_2 = (c,s), x_3 = (0,1), c,s >= 0, c^2+s^2 = 1 (a whole one-parameter family), and for configurations obtained from these by adjoining further vectors orthogonal to everything (a_i = 0 elsewhere).
