For every integer d >= 1 and all lines l_1, ..., l_{d+1} through the origin of R^d (repetitions allowed), S(l_1, ..., l_{d+1}) = sum_{i<j} theta(l_i, l_j) <= (C(d+1, 2) - 1) * pi/2, where theta(l, l') = arccos |<x, x'>| for spanning unit vectors x, x'.

(This is exactly TARGET. No reading ambiguity was found. The gated claims A-C1 and A-C2 are not used; the proof below is self-contained. It uses only: the identity arcsin u + arccos u = pi/2, Bessel's inequality, the intermediate value theorem, the second-derivative test for concavity, closedness of concave functions under pointwise limits, the extreme value theorem on a compact set, and the rank of a Gram matrix.)

## Notation

Throughout, n = d + 1, [n] = {1, ..., n}, and <.,.> is the standard inner product on R^d. For unit vectors x = (x_1, ..., x_n) in R^d put

  F(x) = sum_{1 <= i < j <= n} arcsin |<x_i, x_j>|.

For such x and i in [n] put

  O_i(x) = { j in [n] \ {i} : <x_i, x_j> = 0 },   L_i(x) = { y in R^d : <y, x_j> = 0 for all j in O_i(x) },

and let N(x) = #{ {i,j} : i != j, <x_i, x_j> = 0 } be the number of orthogonal pairs. L_i(x) is a linear subspace containing x_i (by definition of O_i(x)), and L_i(x) is the orthogonal complement of span{x_j : j in O_i(x)}, so dim L_i(x) = d - dim span{x_j : j in O_i(x)}.

For d >= 1 let P(d) be the statement: for all unit vectors x_1, ..., x_{d+1} in R^d, F(x) >= pi/2.

## Step 1 (R1: reformulation)

Let l_1, ..., l_n be lines through the origin of R^d and choose unit vectors x_i spanning l_i. (theta(l_i, l_j) does not depend on the choice, since replacing x_i by -x_i does not change |<x_i, x_j>|; the unit spanning vectors of a line are exactly +-x_i.) By Cauchy–Schwarz, u_{ij} := |<x_i, x_j>| lies in [0, 1]. For every u in [-1, 1], arcsin u + arccos u = pi/2 (standard identity: if u = sin a with a in [-pi/2, pi/2], then u = cos(pi/2 - a) with pi/2 - a in [0, pi], so arccos u = pi/2 - a = pi/2 - arcsin u). Hence

  theta(l_i, l_j) = arccos u_{ij} = pi/2 - arcsin u_{ij},

and summing over the C(n,2) pairs i < j,

  S(l_1, ..., l_n) = C(n,2) pi/2 - F(x).

Therefore S <= (C(n,2) - 1) pi/2 holds iff F(x) >= pi/2. Every n-tuple of unit vectors arises from some n-tuple of lines (take l_i = R x_i), so TARGET for a given d is equivalent to P(d). Repetitions (l_i = l_j, i.e. x_i = +-x_j) and configurations spanning a proper subspace are included in P(d), since P(d) quantifies over all unit n-tuples.

## Step 2 (R2: concavity lemma)

Lemma 2. Let r in [0, 1], tau in R, and let I be an interval of R such that cos(t - tau) >= 0 for all t in I. Then h_r(t) = arcsin(r cos(t - tau)) is concave on I.

Proof. (a) Case r in [0, 1). Put c = cos(t - tau), s = sin(t - tau), w(t) = r c. Then |w| <= r < 1, and arcsin is infinitely differentiable on (-1, 1), so h_r is C^2 on R with

  h_r' = w' (1 - w^2)^{-1/2},
  h_r'' = w'' (1 - w^2)^{-1/2} + w (w')^2 (1 - w^2)^{-3/2} = [ w''(1 - w^2) + w (w')^2 ] (1 - w^2)^{-3/2}.

With w' = -r s and w'' = -r c the bracket equals

  -r c (1 - r^2 c^2) + r c r^2 s^2 = r c ( -1 + r^2 c^2 + r^2 s^2 ) = r c (r^2 - 1).

So h_r''(t) = r c (r^2 - 1) (1 - r^2 c^2)^{-3/2}. On I we have c >= 0, r >= 0 and r^2 - 1 < 0, hence h_r'' <= 0 on I. A C^2 function with non-positive second derivative on an interval is concave there (second-derivative test for concavity). So h_r is concave on I.

(b) Case r = 1. For t in I and 0 < r < 1, h_r(t) -> arcsin(cos(t - tau)) = h_1(t) as r -> 1^-, because arcsin is continuous on [-1, 1]. For a, b in I and lambda in [0, 1], part (a) gives h_r(lambda a + (1 - lambda) b) >= lambda h_r(a) + (1 - lambda) h_r(b) (note lambda a + (1 - lambda) b is in I since I is an interval); letting r -> 1^- gives the same inequality for h_1. So h_1 is concave on I. QED

## Step 3 (R3: facts about a vector moving on a great circle)

Lemma 3. Let u, v be orthonormal vectors in R^d and put y(t) = cos t u + sin t v (t in R). Then:
 (i) |y(t)| = 1 for all t.
 (ii) Let w be any unit vector of R^d, and write a = <u, w>, b = <v, w> and f(t) = <y(t), w> = a cos t + b sin t. Then r := sqrt(a^2 + b^2) <= 1.
 (iii) If a != 0, then f has a zero in (0, pi) and a zero in (-pi, 0); moreover r > 0.
 (iv) If a != 0 and I is an interval on which f does not take both a positive and a negative value, then there is tau in R with |f(t)| = r cos(t - tau) and cos(t - tau) >= 0 for all t in I; consequently (Lemma 2) t -> arcsin |f(t)| is concave on I.

Proof. (i) |y(t)|^2 = cos^2 t |u|^2 + 2 cos t sin t <u, v> + sin^2 t |v|^2 = cos^2 t + sin^2 t = 1.
(ii) By Bessel's inequality for the orthonormal pair u, v: <u, w>^2 + <v, w>^2 <= |w|^2 = 1.
(iii) r >= |a| > 0. f is continuous with f(0) = a and f(pi) = -a, which have opposite signs, so by the intermediate value theorem f vanishes at some point of (0, pi); also f(-pi) = -a and f(0) = a have opposite signs, so by the intermediate value theorem f vanishes at some point of (-pi, 0).
(iv) Since r > 0, (a/r, b/r) is a point of the unit circle, so there is tau_0 with a = r cos tau_0, b = r sin tau_0, and then f(t) = r (cos tau_0 cos t + sin tau_0 sin t) = r cos(t - tau_0). If f >= 0 on I, take tau = tau_0: then |f(t)| = f(t) = r cos(t - tau) and cos(t - tau) = f(t)/r >= 0 on I. If f <= 0 on I, take tau = tau_0 + pi: then cos(t - tau) = -cos(t - tau_0), so |f(t)| = -f(t) = r cos(t - tau) and cos(t - tau) = -f(t)/r >= 0 on I. By hypothesis one of the two cases holds. Since r in (0, 1] by (ii), (iii), Lemma 2 applies to arcsin |f(t)| = arcsin(r cos(t - tau)) on I. QED

## Step 4 (R4: sliding lemma)

Lemma 4. Let d >= 1, n = d + 1, and let x be a minimiser of F over all n-tuples of unit vectors in R^d. Let i in [n] satisfy O_i(x) != [n] \ {i} and dim L_i(x) >= 2. Then there is a minimiser x' of F with N(x') > N(x).

Proof. Write O = O_i(x), L = L_i(x) and J = [n] \ ({i} union O); J is non-empty by hypothesis, and <x_i, x_j> != 0 for every j in J (by definition of O).

(1) Choice of direction. x_i is in L and dim L >= 2, so L intersected with the orthogonal complement of x_i has dimension >= 1; pick a unit vector v in it. Then u := x_i and v are orthonormal, and <v, x_j> = 0 for all j in O (as v is in L). Put y(t) = cos t x_i + sin t v; by Lemma 3(i) each y(t) is a unit vector, and y(0) = x_i.

(2) Inner products along the circle. For j in O: <y(t), x_j> = cos t <x_i, x_j> + sin t <v, x_j> = 0 + 0 = 0 for all t. For j in J put f_j(t) = <y(t), x_j> = a_j cos t + b_j sin t, with a_j = <x_i, x_j> != 0.

(3) The interval. For j in J let Z_j = {t : f_j(t) = 0}, a closed set (f_j is continuous). By Lemma 3(iii), Z_j meets (0, pi) and (-pi, 0); 0 is not in Z_j since f_j(0) = a_j != 0. So Z_j intersected with [0, pi] is compact and non-empty, with minimum p_j in (0, pi), and Z_j intersected with [-pi, 0] is compact and non-empty, with maximum q_j in (-pi, 0). Put t_+ = min_{j in J} p_j > 0 and t_- = max_{j in J} q_j < 0 (J is finite and non-empty), and I = [t_-, t_+]. Then no f_j (j in J) vanishes on the open interval (t_-, t_+), and hence no f_j takes both a positive and a negative value on I: if f_j(p) > 0 > f_j(q) (or the reverse) with p, q in I, the intermediate value theorem gives a zero strictly between p and q, i.e. in (t_-, t_+), a contradiction. Also f_{j_0}(t_+) = 0 for an index j_0 in J attaining the minimum defining t_+.

(4) Concavity. Define g(t) = sum_{j in [n] \ {i}} arcsin |<y(t), x_j>|. By (2) the terms with j in O vanish identically, so g(t) = sum_{j in J} arcsin |f_j(t)|. By step (3) and Lemma 3(iv) (applied with u = x_i, v, w = x_j, a = a_j != 0), each term is concave on I; a finite sum of concave functions is concave, so g is concave on I.

(5) g is constant on I. Let x^(t) be the n-tuple obtained from x by replacing x_i with y(t); it consists of unit vectors. The pairs not containing i contribute the same to F(x^(t)) and to F(x), so F(x^(t)) = F(x) - g(0) + g(t). As x minimises F, g(t) >= g(0) for all t. Now 0 lies strictly between t_- and t_+; with lambda = t_+ / (t_+ - t_-) in (0, 1) we have 0 = lambda t_- + (1 - lambda) t_+, and concavity of g on I gives

  g(0) >= lambda g(t_-) + (1 - lambda) g(t_+).

Hence 0 >= lambda (g(t_-) - g(0)) + (1 - lambda)(g(t_+) - g(0)), where both brackets are >= 0 and lambda, 1 - lambda > 0; so both brackets are 0, in particular g(t_+) = g(0). Therefore F(x^(t_+)) = F(x), i.e. x' := x^(t_+) is also a minimiser of F.

(6) Counting orthogonal pairs. Pairs {k, l} with i not in {k, l} have the same vectors in x and in x', so they are orthogonal in x' iff in x. The pairs {i, j} orthogonal in x are exactly those with j in O, and by (2) they remain orthogonal in x'. In addition {i, j_0} with j_0 in J is orthogonal in x' (f_{j_0}(t_+) = 0) but not in x (j_0 not in O). So N(x') >= N(x) + 1. QED

## Step 5 (R5: matching lemma)

Lemma 5. Let d >= 1, n = d + 1, and let x_1, ..., x_n be unit vectors in R^d such that for every i there is at most one j != i with <x_i, x_j> != 0. Then there are i != j with |<x_i, x_j>| = 1; consequently F(x) >= arcsin 1 = pi/2.

Proof. Let G be the n x n Gram matrix, G_{kl} = <x_k, x_l>, so G = X^T X where X is the d x n matrix with columns x_1, ..., x_n. Then rank G <= rank X <= d < n, so there is c in R^n, c != 0, with G c = 0. Suppose, for contradiction, that |<x_k, x_l>| < 1 for all k != l. Fix k. If x_k is orthogonal to all x_l (l != k), then (Gc)_k = G_{kk} c_k = c_k (G_{kk} = |x_k|^2 = 1), so c_k = 0. Otherwise there is exactly one l != k with gamma := <x_k, x_l> != 0; by hypothesis applied to l, the only index m != l with <x_l, x_m> != 0 is m = k. Then (Gc)_k = c_k + gamma c_l = 0 and (Gc)_l = gamma c_k + c_l = 0. Substituting c_k = -gamma c_l into the second equation gives (1 - gamma^2) c_l = 0; as gamma^2 < 1, c_l = 0 and then c_k = 0. So c_k = 0 for every k, contradicting c != 0. Hence some pair i != j has |<x_i, x_j>| = 1, and as every term of F is >= 0 (arcsin is >= 0 on [0, 1]), F(x) >= arcsin 1 = pi/2. QED

## Step 6 (R6: base case P(1))

The unit vectors of R^1 are +1 and -1, so for x_1, x_2 in R^1 we have |<x_1, x_2>| = 1 and F(x) = arcsin 1 = pi/2 >= pi/2.

## Step 7 (R7: induction step)

Let d >= 2 and assume P(d - 1). Let n = d + 1 and let M be the set of n-tuples of unit vectors in R^d, i.e. the product of n copies of the unit sphere of R^d; M is compact (a product of closed bounded sets in R^{dn}). F is continuous on M (inner products, absolute value and arcsin on [0, 1] are continuous; Cauchy–Schwarz keeps |<x_i, x_j>| in [0, 1]). By the extreme value theorem F attains its minimum on M. N takes integer values in [0, C(n,2)], so among the minimisers there is one, call it x*, with N(x*) maximal among minimisers.

Claim: for every i in [n], either (alpha) O_i(x*) = [n] \ {i}, or (beta) dim L_i(x*) = 1.
Indeed, x*_i is a non-zero vector of L_i(x*), so dim L_i(x*) >= 1. If neither (alpha) nor (beta) held, then O_i(x*) != [n] \ {i} and dim L_i(x*) >= 2, and Lemma 4 would give a minimiser x' with N(x') > N(x*), contradicting the choice of x*.

Case A: some i satisfies (alpha). Then every x*_j (j != i) lies in the (d - 1)-dimensional subspace W = x*_i^perp, d - 1 >= 1. Choose an orthonormal basis of W and let Q : W -> R^{d-1} be the coordinate map; Q is linear and preserves inner products. The d vectors Q x*_j (j != i) are unit vectors in R^{d-1} with <Q x*_j, Q x*_k> = <x*_j, x*_k>. By P(d - 1) (applied to these d = (d - 1) + 1 vectors),
  sum_{j<k, j,k != i} arcsin |<x*_j, x*_k>| >= pi/2.
The remaining terms of F(x*), those containing i, are arcsin 0 = 0. So F(x*) >= pi/2.

Case B: every i satisfies (beta). Then dim span{x*_j : j in O_i(x*)} = d - dim L_i(x*) = d - 1, so |O_i(x*)| >= d - 1. As there are only d indices j != i, at most one j != i has <x*_i, x*_j> != 0. Lemma 5 gives F(x*) >= pi/2.

In both cases F(x*) >= pi/2, and for every x in M, F(x) >= F(x*) >= pi/2. This is P(d).

## Step 8 (R8: conclusion)

By Step 6 and Step 7, induction on d gives P(d) for every integer d >= 1. By Step 1, P(d) is equivalent to TARGET for that d: for all lines l_1, ..., l_{d+1} through the origin of R^d (repetitions allowed), S(l_1, ..., l_{d+1}) = C(d+1, 2) pi/2 - F(x) <= (C(d+1, 2) - 1) pi/2. QED

## Edge cases and remarks

- d = 1: two lines in R^1 coincide, S = 0 = (C(2,2) - 1) pi/2 (equality); covered by Step 6.
- Repeated lines (x_i = +-x_j) and lines spanning a proper subspace are allowed everywhere: no step assumes distinctness or spanning. Lemma 5 in fact produces a repeated line in the extremal minimiser in Case B.
- The bound is attained (e.g. the d coordinate axes with one repeated; for d = 2 also three lines at mutual angles pi/3, or lines at directions 0, alpha, pi/2 with 0 <= alpha <= pi/2). The proof establishes only the inequality; it does not classify equality cases.
- No step rests on computation. out/code/sanity.py is floating-point evidence only.

## What is established

TARGET (Cell 3) in full: for every d >= 1, any d + 1 lines in R^d satisfy S <= (C(d+1,2) - 1) pi/2. Nothing about Cells 4-6 is claimed.
