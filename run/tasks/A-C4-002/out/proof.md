Statement proved: (a) any 5 lines through the origin of R^3 (repetitions allowed) satisfy S <= 4*pi; (b) any 6 lines through the origin of R^4 (repetitions allowed) satisfy S <= 13*pi/2, where S = sum_{i<j} theta(l_i, l_j) and theta(l, l') = arccos|<x, x'>| for spanning unit vectors x, x'.

Status: both (a) and (b) are proved below in full. No step rests on a computer calculation. The scripts in `out/code/` are numerical sanity checks only (evidence, not part of the proof).

Assumptions used (gated, from the brief): **A-C1** (only for N = 4 lines in R^2) and **A-C2** (the chain lemma). A-C3 is not used. Everything else is proved here from textbook facts, each named where it is used: extreme value theorem, intermediate value theorem (IVT), mean value theorem (MVT), Bessel's inequality, the cross product in R^3 with Lagrange's identity, and elementary calculus.

Reading of the statement (no ambiguity found): "lines" are lines through the origin; a line is given by a unit vector x, and x and -x give the same line; lines may coincide and may span a proper subspace.

---

## S0. Notation and reformulation

**0.1.** For unit vectors x, y write c(x,y) = |<x,y>| in [0,1],
theta(x,y) = arccos c(x,y), and phi(x,y) = arcsin c(x,y).
Because arccos t + arcsin t = pi/2 for t in [-1,1], we have theta(x,y) = pi/2 - phi(x,y). Also phi(x,y) = 0 iff <x,y> = 0, and phi(x,y) = pi/2 iff x = +-y. Replacing x by -x changes neither theta nor phi.

**0.2.** A *configuration* is X = (x_1, ..., x_N) in (S^{d-1})^N (S^{d-1} is the unit sphere of R^d), with x_i spanning the i-th line. Put

  S(X) = sum_{i<j} theta(x_i, x_j),   Phi(X) = sum_{i<j} phi(x_i, x_j).

By 0.1, S(X) = C(N,2) pi/2 - Phi(X).

**0.3.** For N = d+2 the claimed bound is (C(d+2,2) - 2) pi/2. For d = 3 this is (10 - 2) pi/2 = 4 pi. For d = 4 it is (15 - 2) pi/2 = 13 pi/2. By 0.2, **S(X) <= (C(d+2,2)-2) pi/2 is equivalent to Phi(X) >= pi.**

**0.4 (isometry invariance).** If U is a linear subspace of R^d of dimension m and Q : U -> R^m is a linear isometry (send an orthonormal basis of U to the standard basis), then Q preserves inner products. So c, theta, phi, S, Phi and all orthogonality relations are unchanged when vectors of U are replaced by their images under Q. The same holds for an orthogonal map of R^d applied to all vectors, and for replacing some x_i by -x_i.

---

## L1. Lemma 1 (concavity)

**Lemma 1.** Let 0 < R <= 1, t_0 in R, and let I be an interval with R cos(t - t_0) >= 0 for all t in I. Then f(t) = arcsin(R cos(t - t_0)) is concave on I.

*Proof.* Put u = t - t_0 and w = 1 - R^2 cos^2 u.

*Case R < 1.* Then |R cos u| <= R < 1, so f is twice differentiable on R with f'(t) = -R sin u * w^{-1/2}. Since dw/du = 2R^2 cos u sin u,
f''(t) = -R cos u * w^{-1/2} + R sin u * (1/2) w^{-3/2} * 2R^2 cos u sin u = -R cos u * w^{-3/2} * (w - R^2 sin^2 u) = -R cos u (1 - R^2) w^{-3/2}.
On I we have cos u >= 0, so f'' <= 0 on I. A twice differentiable function with f'' <= 0 on an interval is concave there (MVT).

*Case R = 1.* The set {u : cos u >= 0} is the union of the disjoint closed intervals [2 pi m - pi/2, 2 pi m + pi/2], m in Z, and consecutive ones are separated by open intervals on which cos u < 0. Since I is connected, {t - t_0 : t in I} lies in one of them, say the one with index m. For |u - 2 pi m| <= pi/2 we have cos u = sin(pi/2 - |u - 2 pi m|), and pi/2 - |u - 2 pi m| is in [0, pi/2]. Hence f(t) = pi/2 - |t - t_0 - 2 pi m| on I, which is concave because it is a constant minus a convex function. ∎

---

## L2. Lemma 2 (independence along a path)

**Lemma 2.** Let m >= 2 and y_1, ..., y_m be vectors of an inner product space with <y_i, y_j> = 0 whenever |i - j| >= 2, and <y_i, y_{i+1}> != 0 for 1 <= i <= m-1. Then y_2, ..., y_m are linearly independent.

*Proof.* Let sum_{i=2}^m lambda_i y_i = 0. We show lambda_l = 0 for l = 2, ..., m by induction on l. Take the inner product of the relation with y_{l-1}. By hypothesis <y_i, y_{l-1}> = 0 unless i is in {l-2, l-1, l}. By the induction hypothesis lambda_i = 0 for every such i with 2 <= i <= l-1. So the relation reduces to lambda_l <y_l, y_{l-1}> = 0, and since <y_l, y_{l-1}> != 0 we get lambda_l = 0. ∎

**Corollary 2'.**
(a) (path) If y_1, ..., y_n (n >= 2) satisfy the hypotheses of Lemma 2, then dim span(y_1, ..., y_n) >= n - 1.
(b) (cycle) Let n >= 3 and y_1, ..., y_n with <y_i, y_j> = 0 unless i - j is congruent to 0, 1 or -1 mod n, and <y_i, y_{i+1}> != 0 for all i (indices mod n). Then dim span(y_1, ..., y_n) >= n - 2.

*Proof.* (a) The n - 1 vectors y_2, ..., y_n are independent by Lemma 2. (b) Apply Lemma 2 to y_1, ..., y_{n-1} (m = n-1 >= 2). The consecutive products are nonzero by hypothesis. If 1 <= i < j <= n-1 and j - i >= 2, then 2 <= j - i <= n - 2, so j - i is not congruent to 0, 1 or -1 mod n, and <y_i, y_j> = 0. Hence y_2, ..., y_{n-1} (n - 2 vectors) are independent. ∎

---

## L3. Lemma 3 (graphs of maximum degree 2)

**Lemma 3.** Let H be a finite connected simple graph with n >= 2 vertices, every vertex of degree <= 2. Then the vertices can be listed u_1, ..., u_n so that either E(H) = {u_i u_{i+1} : 1 <= i < n} (a *path*), or n >= 3 and E(H) = {u_i u_{i+1} : 1 <= i < n} together with u_n u_1 (a *cycle*).

*Proof.* Let P = (u_1, ..., u_m) be a path in H (distinct vertices, consecutive ones adjacent) of maximal length m. Such a path exists since H is finite, and m >= 2 since H is connected with n >= 2. Every neighbour of u_1 lies on P, since otherwise P could be extended; the same holds for u_m. Suppose some vertex z is not on P. Since H is connected, there is a walk from z to u_1. The first vertex of this walk that lies on P, say u_i, is preceded by a vertex w not on P, so w u_i is an edge with w not on P. Then i is not in {1, m} by the previous remark. For 1 < i < m, u_i already has two neighbours u_{i-1}, u_{i+1} on P, and w would be a third, which is impossible. Hence m = n and P contains every vertex. Any edge of H that is not an edge of P joins two vertices of P. An interior vertex u_i (1 < i < n) already has degree 2, so such an edge must be u_1 u_n. If n = 2 that is the edge u_1 u_2 of P, and H is simple. So H is P (a path), or P plus the edge u_n u_1 with n >= 3 (a cycle). ∎

---

## L4. Lemma 4 (structure of a suitable maximiser)

**Lemma 4.** Let d >= 2 and N >= 2. There is a configuration X* = (x_1, ..., x_N) in (S^{d-1})^N with S(X*) = max S such that for every k one of the following holds:
(i) <x_k, x_j> = 0 for every j != k;
(ii) span{x_j : j != k, <x_j, x_k> = 0} = x_k^perp.

*Proof.*
**4.1.** theta is continuous on S^{d-1} x S^{d-1}, since it is a composition of continuous maps. So S is continuous on the compact set (S^{d-1})^N and attains its maximum (extreme value theorem). Let M be the nonempty set of maximisers. For a configuration X let omega(X) be the number of pairs i < j with <x_i, x_j> = 0, an integer in [0, C(N,2)]. Choose X* in M with omega(X*) = max{omega(X) : X in M}, the maximum of a nonempty finite set of integers.

**4.2.** Suppose, for contradiction, that some k satisfies neither (i) nor (ii). Let J = {j != k : <x_j, x_k> = 0} and K = {j != k : <x_j, x_k> != 0}. Then K is nonempty because (i) fails. Let V = {y in R^d : <y, x_j> = 0 for all j in J}, the orthogonal complement of span{x_j : j in J}. Then x_k is in V. Also span{x_j : j in J} is contained in x_k^perp (dimension d-1) and is not equal to it because (ii) fails, so its dimension is <= d-2 and dim V >= 2. Choose a unit vector v in V with <v, x_k> = 0, and set x(t) = cos t * x_k + sin t * v. This is a unit vector, and x(t) is in V for all t.

**4.3.** For j in K let g_j(t) = <x(t), x_j> = <x_k, x_j> cos t + <v, x_j> sin t. Let R_j = (<x_k,x_j>^2 + <v,x_j>^2)^{1/2}. Then R_j > 0 because g_j(0) != 0, and R_j <= |x_j| = 1 by Bessel's inequality, since x_k, v are orthonormal. Also g_j(t) = R_j cos(t - t_j) for some t_j, so its zeros form the discrete set t_j + pi/2 + pi Z. Since g_j(pi) = g_j(-pi) = -g_j(0), the IVT gives a zero of g_j in (0, pi) and one in (-pi, 0). Let t_+ be the smallest zero in (0, pi) of the finite product prod_{j in K} g_j, and t_- the largest zero in (-pi, 0). On the open interval (t_-, t_+) no g_j (j in K) vanishes, so by the IVT each g_j has the constant sign eps_j := sign g_j(0) there. By continuity eps_j g_j >= 0 on [t_-, t_+].

**4.4.** Let F(t) = sum_{j != k} phi(x(t), x_j). For j in J, phi(x(t), x_j) = 0 because x(t) is in V. For j in K and t in [t_-, t_+], phi(x(t), x_j) = arcsin(eps_j g_j(t)), and eps_j g_j(t) = R_j cos(t - t_j') with t_j' = t_j or t_j + pi. By Lemma 1 (with I = [t_-, t_+]) each of these terms is concave on [t_-, t_+], so F is concave on [t_-, t_+].

**4.5.** Let X(t) be X* with x_k replaced by x(t), so X(0) = X*. By 0.1,
S(X(t)) = sum_{i<j; i,j != k} theta(x_i, x_j) + (N-1) pi/2 - F(t).
Since X* maximises S, we get F(0) <= F(t) for all t. Since t_- < 0 < t_+, write 0 = lambda t_- + (1 - lambda) t_+ with lambda = t_+/(t_+ - t_-) in (0,1). Concavity gives F(0) >= lambda F(t_-) + (1-lambda) F(t_+) >= min(F(t_-), F(t_+)). Pick t* in {t_-, t_+} with F(t*) = min(F(t_-), F(t_+)). Then F(t*) <= F(0) <= F(t*), so F(t*) = F(0), hence S(X(t*)) = S(X*) and X(t*) is in M.

**4.6.** Compare omega(X(t*)) with omega(X*). Pairs not containing k are unchanged. For j in J the pair {k, j} stays orthogonal, because x(t*) is in V. By the choice of t*, some j_0 in K has g_{j_0}(t*) = 0. So the pair {k, j_0}, which was not orthogonal in X*, is orthogonal in X(t*). The remaining pairs {k, j} with j in K were not orthogonal in X*, so none of them is lost. Hence omega(X(t*)) >= omega(X*) + 1, contradicting the choice of X* in 4.1. ∎

---

## L5. Lemma 5 (paths; uses A-C2)

**Lemma 5.** Let n >= 2, let U be a subspace of some R^D with dim U = n - 1, and let y_1, ..., y_n be unit vectors in U with <y_i, y_j> = 0 whenever |i - j| >= 2. Then sum_{i=1}^{n-1} phi(y_i, y_{i+1}) >= pi/2.

*Proof.* Let Q : U -> R^{n-1} be a linear isometry and z_i = Q y_i. These are unit vectors in R^{n-1} with <z_i, z_j> = <y_i, y_j> (0.4). So they satisfy the hypotheses of A-C2 exactly, with m = n >= 2: unit vectors in R^{m-1}, and <z_i, z_j> = 0 whenever |i - j| >= 2. A-C2 gives sum_{i=1}^{n-1} theta(z_i, z_{i+1}) <= (n-2) pi/2. By 0.1, sum_{i=1}^{n-1} phi(y_i, y_{i+1}) = (n-1) pi/2 - sum theta(z_i, z_{i+1}) >= (n-1) pi/2 - (n-2) pi/2 = pi/2. ∎

---

## L6. Lemma 6 (cycles of length 3 and 4)

**Lemma 6.** Let n be 3 or 4. Let y_1, ..., y_n be unit vectors lying in a subspace U with dim U = n - 2, such that <y_i, y_j> = 0 whenever i - j is not congruent to 0, 1 or -1 mod n. Then sum_{i in Z/n} phi(y_i, y_{i+1}) >= pi.

*Proof.* *n = 3.* Here dim U = 1, so every y_i is +-y_1. Hence |<y_i, y_j>| = 1 and phi(y_i, y_j) = pi/2 for all i, j. The sum is 3 pi/2 >= pi.

*n = 4.* Here dim U = 2. Fix r in Z/4. The three vectors y_{r+1}, y_{r+2}, y_{r+3} lie in U, and <y_{r+1}, y_{r+3}> = 0 because the index difference is 2, which is not congruent to 0, 1 or -1 mod 4. Lemma 5 (with n = 3 and the 2-dimensional U) gives phi(y_{r+1}, y_{r+2}) + phi(y_{r+2}, y_{r+3}) >= pi/2. Add these four inequalities over r in Z/4. The term phi(y_i, y_{i+1}) occurs in the r-th inequality iff {i, i+1} is a subset of Z/4 \ {r}, i.e. iff r is not i or i+1. That happens for exactly 2 values of r. Hence 2 sum_i phi(y_i, y_{i+1}) >= 4 * pi/2, and the sum is >= pi. ∎

---

## L7. Lemma 7 (the 5-cycle)

**Lemma 7.** Let y_1, ..., y_5 be unit vectors in a 3-dimensional subspace U, with indices mod 5, such that
(H0) <y_i, y_{i+2}> = 0 for every i, and
(H1) <y_i, y_{i+1}> != 0 for every i.
Then D := sum_{i in Z/5} phi(y_i, y_{i+1}) >= pi.

(In Z/5 the pairs with index difference +-2 are exactly the non-adjacent pairs of the 5-cycle.)

*Proof.*
**7.1.** By 0.4 we may take U = R^3, apply an orthogonal map of R^3 to all vectors, and replace individual y_i by -y_i. None of these changes (H0), (H1) or D.

**7.2.** By (H0) with i = 1, y_1 is orthogonal to y_3. Apply an orthogonal map with y_1 -> e_1, y_3 -> e_2 (extend {y_1, y_3} to an orthonormal basis). Write y_2 = (p, q, r). Replace y_2 by -y_2 if needed so that p >= 0. Then apply T = diag(1, eps, eps'), with eps, eps' in {1, -1} chosen so that the 2nd and 3rd coordinates of T y_2 are >= 0, to all five vectors. Finally replace T y_3 = eps e_2 by eps T y_3 = e_2. Now y_1 = e_1, y_3 = e_2, y_2 = (p, q, r) with p, q, r >= 0 and p^2 + q^2 + r^2 = 1.

**7.3.** By (H1), p = <y_1, y_2> != 0 and q = <y_2, y_3> != 0, so p, q > 0. Hence p < 1 and q < 1, so y_1, y_2 are linearly independent and y_2, y_3 are linearly independent.

**7.4.** By (H0) with i = 4 (<y_4, y_6> = <y_4, y_1>) and i = 2, y_4 is orthogonal to y_1 and y_2. The orthogonal complement of span(y_1, y_2) in R^3 is one-dimensional and spanned by the cross product y_1 x y_2 = (0, -r, q), whose norm is (q^2 + r^2)^{1/2} = (1 - p^2)^{1/2} > 0 (Lagrange's identity). So y_4 = +-(0, -r, q)/(q^2+r^2)^{1/2}. Next, by (H0) with i = 5 (<y_5, y_7> = <y_5, y_2>) and i = 3, y_5 is orthogonal to y_2 and y_3. These two are linearly independent (7.3), so the orthogonal complement of span(y_2, y_3) is one-dimensional and spanned by y_2 x y_3 = (p,q,r) x (0,1,0) = (-r, 0, p), whose norm is (p^2 + r^2)^{1/2} = (1 - q^2)^{1/2} > 0. So y_5 = +-(-r, 0, p)/(p^2+r^2)^{1/2}.

**7.5.** The five edge values are
|<y_1,y_2>| = p,  |<y_2,y_3>| = q,  |<y_3,y_4>| = r/(q^2+r^2)^{1/2},
|<y_4,y_5>| = pq / ((q^2+r^2)^{1/2} (p^2+r^2)^{1/2}),  |<y_5,y_1>| = r/(p^2+r^2)^{1/2}.
(For the 4th: (0,-r,q).(-r,0,p) = qp.) By (H1) with i = 3, r > 0.

**7.6.** Since 0 < p < 1, let b = arccos p, in (0, pi/2). Then q^2 + r^2 = sin^2 b and (q, r)/sin b is a unit vector with both coordinates > 0, so (q, r) = (sin b cos A_0, sin b sin A_0) for a unique A_0 in (0, pi/2). With M(A) := (cos^2 b + sin^2 b sin^2 A)^{1/2} we have (p^2 + r^2)^{1/2} = M(A_0). Substituting into 7.5, and using arcsin(cos b) = pi/2 - b and arcsin(sin A_0) = A_0:
D = Dbar(A_0), where for A in [0, pi/2]
  Dbar(A) = (pi/2 - b) + arcsin(sin b cos A) + A + arcsin(sin b sin A / M(A)) + arcsin(cos b cos A / M(A)).
(Term by term: phi_12 = arcsin(cos b); phi_23 = arcsin(sin b cos A_0); phi_34 = arcsin(sin b sin A_0/sin b); phi_51 = arcsin(sin b sin A_0/M); phi_45 = arcsin(cos b sin b cos A_0/(sin b M)).)

**7.7 (Dbar is continuous on [0, pi/2]).** M(A) >= cos b > 0. The arguments of the arcsines lie in [0,1]: (sin b sin A)^2 <= M^2 and (cos b cos A)^2 <= cos^2 b <= M^2. Hence Dbar is continuous on [0, pi/2].

**7.8 (endpoint values).** M(0) = cos b, so Dbar(0) = (pi/2 - b) + arcsin(sin b) + 0 + 0 + arcsin(1) = pi/2 - b + b + pi/2 = pi. M(pi/2) = 1, so Dbar(pi/2) = (pi/2 - b) + 0 + pi/2 + arcsin(sin b) + 0 = pi.

**7.9 (concavity).** The term arcsin(sin b cos A) is concave on [0, pi/2] by Lemma 1 (R = sin b in (0,1), t_0 = 0, cos A >= 0). The term A is linear. Let g(A) be the sum of the last two terms. For A in (0, pi/2):
M^2 - sin^2 b sin^2 A = cos^2 b > 0 and M^2 - cos^2 b cos^2 A = cos^2 b sin^2 A + sin^2 b sin^2 A = sin^2 A > 0.
So both arguments lie in [0,1). Using arcsin y = arctan(y/(1-y^2)^{1/2}) for y in [0,1),
  g(A) = arctan(tan b sin A) + arctan(cos b cot A).
Differentiating,
  d/dA arctan(tan b sin A) = tan b cos A/(1 + tan^2 b sin^2 A) = sin b cos b cos A/(cos^2 b + sin^2 b sin^2 A),
  d/dA arctan(cos b cot A) = -cos b/(sin^2 A (1 + cos^2 b cot^2 A)) = -cos b/(sin^2 A + cos^2 b cos^2 A).
Both denominators equal 1 - sin^2 b cos^2 A, since cos^2 b + sin^2 b sin^2 A = 1 - sin^2 b cos^2 A and sin^2 A + cos^2 b cos^2 A = 1 - sin^2 b cos^2 A. Hence
  g'(A) = cos b (sin b cos A - 1)/((1 - sin b cos A)(1 + sin b cos A)) = -cos b/(1 + sin b cos A),
  g''(A) = -sin b cos b sin A/(1 + sin b cos A)^2 <= 0.
So g is concave on (0, pi/2), and therefore Dbar is concave on (0, pi/2). A function that is continuous on [0, pi/2] (7.7) and concave on (0, pi/2) is concave on [0, pi/2] (pass to the limit in the concavity inequality).

**7.10.** A_0 is a convex combination of 0 and pi/2, so by concavity and 7.8, D = Dbar(A_0) >= min(Dbar(0), Dbar(pi/2)) = pi. ∎

---

## L8. Lemma 8 (the 6-cycle)

**Lemma 8.** Let y_1, ..., y_6 be unit vectors in a 4-dimensional subspace U, with indices mod 6, such that
(H0) <y_i, y_j> = 0 whenever i - j is congruent to 2, 3 or 4 mod 6 (the non-adjacent pairs of the 6-cycle), and
(H1) <y_i, y_{i+1}> != 0 for every i.
Then D := sum_{i in Z/6} phi(y_i, y_{i+1}) >= pi.

*Proof.*
**8.1.** By 0.4 take U = R^4. We may replace individual y_i by -y_i.

**8.2.** y_1 and y_2 are not parallel. If y_2 = +-y_1, then <y_2, y_3> = +-<y_1, y_3> = 0 by (H0), contradicting (H1). Also y_4 and y_5 are not parallel. If y_5 = +-y_4, then <y_5, y_6> = +-<y_4, y_6> = 0 by (H0) (difference 2), contradicting (H1). So P_12 := span(y_1, y_2) and P_45 := span(y_4, y_5) are 2-dimensional. By (H0), y_1 and y_2 are each orthogonal to y_4 and y_5 (index differences 3, 4, 2, 3). So P_12 is orthogonal to P_45 and R^4 = P_12 (+) P_45.

**8.3 (frames).** Replacing y_2 by -y_2 if needed, c_12 := <y_1, y_2> > 0 (it is != 0 by (H1)). Put f_1 = y_1 and f_2 = (y_2 - c_12 y_1)/|y_2 - c_12 y_1|; the denominator is nonzero by 8.2. Then y_2 = cos alpha f_1 + sin alpha f_2 with cos alpha = c_12 in (0,1) and sin alpha > 0, so alpha is in (0, pi/2). Next, replacing y_5 by -y_5 if needed, c_45 := <y_4, y_5> > 0 (it is != 0 by (H1)). Put f_3 = y_4 and f_4 = (y_5 - c_45 y_4)/|y_5 - c_45 y_4|; the denominator is nonzero by 8.2. Then y_5 = cos beta f_3 + sin beta f_4 with cos beta = c_45 in (0,1) and sin beta > 0, so beta is in (0, pi/2). Since f_1, f_2 lie in P_12 and f_3, f_4 lie in P_45, which are orthogonal (8.2), (f_1, f_2, f_3, f_4) is an orthonormal basis of R^4. Write a = sin alpha, A = cos alpha, b = sin beta, B = cos beta (all in (0,1)). Put f_2' = -a f_1 + A f_2 (orthogonal to y_2 in P_12) and f_5' = -b f_3 + B f_4 (orthogonal to y_5 in P_45).

**8.4 (y_3 and y_6).** By (H0), y_3 is orthogonal to y_1 and y_5. Write y_3 = sum lambda_i f_i. Then lambda_1 = <y_3, y_1> = 0 and <y_3, y_5> = B lambda_3 + b lambda_4 = 0, so (lambda_3, lambda_4) is a multiple of (-b, B). Hence y_3 is in span(f_2, f_5'), and since f_2, f_5' are orthonormal, y_3 = cos sigma f_2 + sin sigma f_5' for some sigma. By (H0), y_6 is orthogonal to y_4 and y_2. Write y_6 = sum nu_i f_i. Then nu_3 = 0 and A nu_1 + a nu_2 = 0, so y_6 = cos tau f_2' + sin tau f_4 for some tau. Finally <y_3, y_6> = 0 by (H0) (difference 3). Since <f_2, f_2'> = A, <f_2, f_4> = 0, <f_5', f_2'> = 0 and <f_5', f_4> = B, this reads
  A cos sigma cos tau + B sin sigma sin tau = 0.   (*)

**8.5 (edge values).**
|<y_1,y_2>| = A,  |<y_2,y_3>| = a|cos sigma|,  |<y_3,y_4>| = |sin sigma| |<f_5', f_3>| = b|sin sigma|,
|<y_4,y_5>| = B,  |<y_5,y_6>| = |sin tau| |<y_5, f_4>| = b|sin tau|,  |<y_6,y_1>| = |cos tau| |<f_2', f_1>| = a|cos tau|.
By (H1), c := |cos sigma|, s := |sin sigma|, |cos tau| and |sin tau| are all > 0. Taking absolute values in (*) gives A c |cos tau| = B s |sin tau|. Together with |cos tau|^2 + |sin tau|^2 = 1 this yields
  |cos tau| = B s/N,  |sin tau| = A c/N,  where N = (A^2 c^2 + B^2 s^2)^{1/2}.
Let sigma_0 in (0, pi/2) be the angle with cos sigma_0 = c and sin sigma_0 = s. Using arcsin A = pi/2 - alpha and arcsin B = pi/2 - beta, we get D = Delta(sigma_0), where for sigma in [0, pi/2]
  Delta(sigma) = pi - alpha - beta + arcsin(a cos sigma) + arcsin(b sin sigma) + arcsin(bA cos sigma/N(sigma)) + arcsin(aB sin sigma/N(sigma)),
  N(sigma) = (A^2 cos^2 sigma + B^2 sin^2 sigma)^{1/2} >= min(A, B) > 0.

**8.6 (continuity, endpoints).** The arcsine arguments lie in [0,1]: a cos sigma <= a < 1, b sin sigma <= b < 1, (bA cos sigma)^2 <= A^2 cos^2 sigma <= N^2, and (aB sin sigma)^2 <= B^2 sin^2 sigma <= N^2. So Delta is continuous on [0, pi/2]. With N(0) = A and N(pi/2) = B:
Delta(0) = pi - alpha - beta + arcsin a + 0 + arcsin b + 0 = pi, and Delta(pi/2) = pi - alpha - beta + 0 + arcsin b + 0 + arcsin a = pi.

**8.7 (derivative).** From now on sigma is in (0, pi/2), with c = cos sigma, s = sin sigma (both > 0), R_1 = (1 - a^2 c^2)^{1/2} and R_2 = (1 - b^2 s^2)^{1/2}. Note R_1^2 = s^2 + A^2 c^2 and R_2^2 = c^2 + B^2 s^2. Also
N^2 - b^2 A^2 c^2 = A^2 B^2 c^2 + B^2 s^2 = B^2 R_1^2 > 0 and N^2 - a^2 B^2 s^2 = A^2 c^2 + A^2 B^2 s^2 = A^2 R_2^2 > 0.
So all four arguments lie in [0,1) and Delta is differentiable. Using (N^2)' = 2sc(B^2 - A^2), i.e. N' = sc(B^2 - A^2)/N:
- (arcsin(a c))' = -a s/R_1;
- (arcsin(b s))' = b c/R_2;
- (bA c/N)' = bA(-s N^2 - c^2 s (B^2 - A^2))/N^3 = -bA s B^2/N^3, and (1 - (bAc/N)^2)^{1/2} = B R_1/N, so (arcsin(bAc/N))' = -bAB s/(N^2 R_1);
- (aB s/N)' = aB(c N^2 - s^2 c (B^2 - A^2))/N^3 = aB c A^2/N^3, and (1 - (aBs/N)^2)^{1/2} = A R_2/N, so (arcsin(aBs/N))' = aAB c/(N^2 R_2).
Therefore
  Delta'(sigma) = (Qf(sigma) - Pf(sigma))/N^2, with Pf = (s/R_1)(a N^2 + bAB) > 0 and Qf = (c/R_2)(b N^2 + aAB) > 0.

**8.8 (sign pattern of Delta').** Let h = Qf/Pf = c R_1 (b N^2 + aAB) / (s R_2 (a N^2 + bAB)) > 0. Then sign Delta' = sign(h - 1). Now
log h = log c - log s + log R_1 - log R_2 + log(b N^2 + aAB) - log(a N^2 + bAB).
Differentiate term by term, using (R_1^2)' = 2a^2 cs and (R_2^2)' = -2b^2 sc:
- (log c - log s)' = -s/c - c/s = -1/(sc);
- (log R_1)' = a^2 sc/R_1^2 and (-log R_2)' = b^2 sc/R_2^2;
- (log(bN^2 + aAB) - log(aN^2 + bAB))' = (N^2)' * [b(aN^2 + bAB) - a(bN^2 + aAB)] / [(bN^2+aAB)(aN^2+bAB)] = 2sc(B^2 - A^2) * AB(b^2 - a^2) / [(bN^2+aAB)(aN^2+bAB)] = -2sc AB (A^2 - B^2)^2 / [(bN^2+aAB)(aN^2+bAB)] <= 0, because b^2 - a^2 = A^2 - B^2.
Since a^2 <= 1 we have R_1^2 = 1 - a^2 c^2 >= 1 - c^2 = s^2, and since b^2 <= 1, R_2^2 = 1 - b^2 s^2 >= 1 - s^2 = c^2. Hence
(log h)' <= -1/(sc) + a^2 sc/s^2 + b^2 sc/c^2 = (-1 + a^2 c^2 + b^2 s^2)/(sc) = -(A^2 c^2 + B^2 s^2)/(sc) = -N^2/(sc) < 0.
So h is strictly decreasing on (0, pi/2). As sigma -> 0+: Qf -> A(bA + aB) > 0 and Pf -> 0+ (s -> 0, R_1 -> A), so h -> +infinity. As sigma -> pi/2-: Qf -> 0 (c -> 0, R_2 -> B > 0) and Pf -> aB^2 + bAB > 0, so h -> 0. By the IVT and strict monotonicity there is a unique sigma* in (0, pi/2) with h(sigma*) = 1, and h > 1 on (0, sigma*), h < 1 on (sigma*, pi/2). Hence Delta' > 0 on (0, sigma*) and Delta' < 0 on (sigma*, pi/2).

**8.9.** By the MVT and 8.6, Delta is strictly increasing on [0, sigma*] and strictly decreasing on [sigma*, pi/2]. So Delta(sigma) > Delta(0) = pi for sigma in (0, sigma*], and Delta(sigma) > Delta(pi/2) = pi for sigma in [sigma*, pi/2). In particular D = Delta(sigma_0) > pi. ∎

---

## S9. Proof of the theorem

Let d be 3 or 4 and N = d + 2. We prove d = 3 first (part (a)) and then d = 4 (part (b)). Part (b) uses part (a) in Case A below. Part (a) does not use part (b).

**9.1.** Let X* = (x_1, ..., x_N) be the maximiser given by Lemma 4. Every configuration X satisfies S(X) <= S(X*), so it suffices to show S(X*) <= (C(N,2) - 2) pi/2. By 0.3 this means Phi(X*) >= pi, or directly the bounds 4 pi (d = 3) and 13 pi/2 (d = 4).

**9.2 (Case A: some x_k is orthogonal to all the others).** Then the other N - 1 = d + 1 vectors lie in U = x_k^perp, which has dimension d - 1, and
S(X*) = sum_{j != k} theta(x_k, x_j) + sum_{i<j; i,j != k} theta(x_i, x_j) = (N-1) pi/2 + S',
where S' is the angle sum of the other d + 1 lines. By 0.4, S' is the angle sum of d + 1 lines in R^{d-1}.
- d = 3: S' is the angle sum of 4 lines in R^2. By A-C1 with N = 4, S' <= (pi/2) floor(16/4) = 2 pi. So S(X*) <= 4 pi/2 + 2 pi = 4 pi.
- d = 4: S' is the angle sum of 5 lines in R^3. By part (a), already proved, S' <= 4 pi. So S(X*) <= 5 pi/2 + 4 pi = 13 pi/2.

**9.3 (Case B: no x_k is orthogonal to all the others).** Then by Lemma 4, (ii) holds for every k: with J_k = {j != k : <x_j, x_k> = 0}, we have span{x_j : j in J_k} = x_k^perp.

**9.3.1.** X* spans R^d: for any k, span{x_j : j in J_k} + R x_k = x_k^perp + R x_k = R^d.

**9.3.2.** Let G be the graph on {1, ..., N} with an edge ij iff <x_i, x_j> != 0 (i != j). Then |J_k| >= dim x_k^perp = d - 1, so deg_G(k) = (N - 1) - |J_k| <= (d + 1) - (d - 1) = 2.

**9.3.3.** Let C_1, ..., C_q be the vertex sets of the connected components of G. By Lemma 3, each component is an isolated vertex, a path with >= 2 vertices, or a cycle with >= 3 vertices. Let W_l = span{x_u : u in C_l}. For l != l', every u in C_l and u' in C_{l'} are non-adjacent, so <x_u, x_{u'}> = 0. So the W_l are mutually orthogonal, and their sum is direct. By 9.3.1 their sum is R^d, so sum_l dim W_l = d. Let delta_l = |C_l| - dim W_l, which is >= 0 because W_l is spanned by |C_l| vectors. Then
  sum_l delta_l = N - d = 2.

**9.3.4.** A pair ij that is not an edge of G has phi(x_i, x_j) = 0, and every edge lies inside one component. Hence Phi(X*) = sum_l Phi_l, where Phi_l = sum over edges uv of G inside C_l of phi(x_u, x_v). We show Phi_l >= delta_l pi/2 for every l.

**9.3.5 (isolated vertex).** dim W_l = 1 = |C_l|, so delta_l = 0 and Phi_l = 0.

**9.3.6 (path).** List C_l as v_1, ..., v_n (n >= 2) as in Lemma 3. Non-adjacent vertices of C_l are orthogonal (definition of G) and consecutive ones are not. So y_i = x_{v_i} satisfies the hypotheses of Lemma 2, and Corollary 2'(a) gives dim W_l >= n - 1, i.e. delta_l <= 1. If delta_l = 0, then Phi_l >= 0. If delta_l = 1, then dim W_l = n - 1, and Lemma 5 (with U = W_l) gives Phi_l = sum_{i=1}^{n-1} phi(x_{v_i}, x_{v_{i+1}}) >= pi/2.

**9.3.7 (cycle).** List C_l as v_1, ..., v_n (n >= 3, edges v_i v_{i+1} with indices mod n). Non-adjacent vertices are orthogonal and adjacent ones are not, so Corollary 2'(b) gives dim W_l >= n - 2. Conversely, apply 9.3 at k = v_1. The vertices orthogonal to x_{v_1} are J_{v_1} = (vertices outside C_l) together with {v_3, ..., v_{n-1}} (empty if n = 3). Put U_1 = span{x_{v_3}, ..., x_{v_{n-1}}}, which is contained in W_l, and U_2 = span{x_j : j not in C_l}, which is contained in W_l^perp. Then U_1 + U_2 = x_{v_1}^perp. Let w be in W_l with w orthogonal to x_{v_1}, and write w = u_1 + u_2 with u_1 in U_1 and u_2 in U_2. Then u_2 = w - u_1 lies in W_l and in W_l^perp, so u_2 = 0 and w is in U_1. Now W_l ∩ x_{v_1}^perp is the kernel of the nonzero functional w -> <w, x_{v_1}> on W_l (nonzero since x_{v_1} is in W_l), so it has dimension dim W_l - 1. Hence dim W_l - 1 <= dim U_1 <= n - 3. Together: dim W_l = n - 2, i.e. **delta_l = 2**. Since W_l is contained in R^d, n - 2 <= d, so n <= d + 2 (also n <= N = d + 2). Apply to y_i = x_{v_i}, which lie in the (n-2)-dimensional W_l, with non-adjacent pairs orthogonal and adjacent pairs non-orthogonal:
- n = 3 or 4: Lemma 6 gives Phi_l >= pi;
- n = 5 (dim W_l = 3; possible for d = 3 and d = 4): Lemma 7, whose (H0) and (H1) are exactly these conditions, gives Phi_l >= pi;
- n = 6 (dim W_l = 4; possible only for d = 4, where W_l = R^4): Lemma 8 gives Phi_l >= pi.
For d = 3 the possible cycle lengths are n in {3,4,5}, and for d = 4 they are n in {3,4,5,6}, so every case is covered. So Phi_l >= pi = delta_l pi/2.

**9.3.8.** By 9.3.4 to 9.3.7 and 9.3.3, Phi(X*) = sum_l Phi_l >= (sum_l delta_l) pi/2 = pi. By 0.3, S(X*) <= (C(N,2) - 2) pi/2, which is 4 pi for d = 3 and 13 pi/2 for d = 4.

**9.4.** In both cases S(X*) is at most the claimed bound, and S(X) <= S(X*) for every configuration X of N = d+2 lines in R^d. This proves (a) (d = 3, via A-C1, A-C2 and Lemmas 1 to 7) and then (b) (d = 4, via A-C2, part (a) and Lemmas 1 to 8). ∎

**9.5 (sharpness, not needed for the proof).** The configuration e_1, e_1, e_2, e_2, e_3 in R^3 has S = 8 * pi/2 = 4 pi. The configuration e_1, e_1, e_2, e_2, e_3, e_4 in R^4 has S = 13 pi/2. So both bounds are attained.

---

## S10. Edge and degenerate cases (checklist G3)

- Coincident lines (x_i = +-x_j) and configurations spanning a proper subspace are included, since X ranges over all of (S^{d-1})^N and the bound is proved for a global maximiser.
- A line orthogonal to all the others is Case A (9.2), which is where Lemma 4 (i) can occur.
- In Case B, degenerate components are covered: isolated vertices (delta = 0), paths of length 2 with coincident vectors (delta = 1, phi = pi/2, consistent with Lemma 5 at n = 2), and 3-cycles of three coincident lines (Lemma 6, n = 3).
- In Lemmas 7 and 8 the degenerate positions (some edge orthogonal, some adjacent pair parallel) are excluded by (H1). In the application they cannot occur, because edges of G are non-orthogonal by definition, and 7.3 and 8.2 show that (H1) and (H0) already force adjacent vectors to be non-parallel.

## S11. What is established

Both instances of Cell 4 are proved, conditional only on the gated claims A-C1 (instance N = 4) and A-C2. No computer calculation is used. KNOWN GAPS: none found.
