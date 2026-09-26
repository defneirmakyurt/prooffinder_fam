STATEMENT PROVED (with an honest gap, see Step 6): For d=2, and for every d>=2 in a weaker
form, any N=d+2 lines l_1,...,l_N through the origin of R^d satisfy S <= (C(d+2,2)-2)*pi/2,
where S = sum_{i<j} theta(l_i,l_j), theta(l,l') = arccos|<x,x'>| in [0,pi/2] for unit vectors
x,x' spanning l,l', and C(n,2)=n(n-1)/2. The full statement (every d>=2, the exact constant 2)
is PROVED for d=2. For d>=3 only a weaker true inequality is established; the exact target for
d>=3 is a GAP, stated precisely in Step 6.

Throughout, N=d+2, and for each line l_i we fix an arbitrary unit vector x_i spanning it (the
choice of sign of x_i is immaterial below, since only |<x_i,x_j>| ever appears).

## Step 1 (identity: arccos + arcsin = pi/2)

For x in [-1,1], define phi(x) = arccos(x) + arcsin(x). Both arccos and arcsin are differentiable
on (-1,1) with arccos'(x) = -1/sqrt(1-x^2) and arcsin'(x) = 1/sqrt(1-x^2) (standard calculus
facts, the defining property of these inverse trigonometric functions). Hence phi'(x) = 0 on
(-1,1), so phi is constant there; by continuity it is constant on all of [-1,1]. Evaluating at
x=0: phi(0) = arccos(0) + arcsin(0) = pi/2 + 0 = pi/2. Hence

    arccos(x) + arcsin(x) = pi/2  for all x in [-1,1].                      (1)

## Step 2 (reduction to a lower bound on T)

Write a_ij = <x_i,x_j> for i != j. By definition theta(l_i,l_j) = arccos|a_ij|. Applying (1) with
x = |a_ij| in [0,1]:

    theta(l_i,l_j) = pi/2 - arcsin|a_ij|.

Summing over the C(N,2) pairs i<j and setting T := sum_{i<j} arcsin|a_ij| (a sum of C(N,2)
nonnegative terms, each in [0,pi/2]):

    S = C(N,2)*(pi/2) - T.                                                   (2)

Hence the target inequality

    S <= (C(N,2)-2)*(pi/2)

is EXACTLY equivalent (by (2), a pure algebraic rearrangement) to

    T >= pi.                                                                 (3)

So from now on the whole task is to prove (3): T >= pi, i.e. Sum_{i<j} arcsin|a_ij| >= pi, for
every choice of N=d+2 unit vectors x_1,...,x_N in R^d.

## Step 3 (Gram matrix rank bound; holds for every d>=1 and every N>=1)

Let X be the d x N matrix whose columns are x_1,...,x_N, and let G = X^T X, an N x N matrix with
entries G_ii = <x_i,x_i> = 1 and G_ij = a_ij for i != j. Standard facts used here (linear
algebra):
  (i) G is symmetric.
  (ii) G is positive semidefinite: for any v in R^N, v^T G v = v^T X^T X v = |Xv|^2 >= 0.
  (iii) rank(G) = rank(X^T X) = rank(X) (a standard fact: X^T X and X have the same rank, since
        X v = 0 iff v^T X^T X v = |Xv|^2 = 0 iff (by PSD-ness and the spectral theorem, or simply
        since G is a Gram matrix) Gv=0; more directly, ker(X) subseteq ker(X^TX) always, and if
        X^TXv=0 then v^TX^TXv=|Xv|^2=0 so Xv=0, giving ker(X^TX) subseteq ker(X), hence
        ker(X)=ker(X^TX) and by rank-nullity rank(X)=rank(G)).
  (iv) Since X has only d rows, rank(X) <= d. Hence rank(G) <= d.

By the spectral theorem (G symmetric), G has N real eigenvalues lambda_1,...,lambda_N, each >=0
by (ii). By (iv) at most d of them are nonzero; let lambda_1,...,lambda_r (r = rank(G) <= d) be
the nonzero ones (r could be less than d, that only helps below), so lambda_{r+1}=...=lambda_N=0.

trace(G) = sum_k lambda_k = sum_{r+1..N} 0 + sum_{k=1}^r lambda_k = N, since trace(G) = sum_i
G_ii = N (using G_ii=1, N terms).                                            (4)

By the Cauchy-Schwarz inequality applied to the r-tuples (lambda_1,...,lambda_r) and (1,...,1):

    (sum_{k=1}^r lambda_k)^2 <= r * sum_{k=1}^r lambda_k^2 <= d * sum_{k=1}^r lambda_k^2,

the last step because r <= d and each lambda_k^2 >= 0 (so replacing the multiplier r by the
larger d only weakens/keeps valid the inequality: r*sum <= d*sum since sum>=0 and d>=r). Using
(4), sum_{k=1}^r lambda_k = N, so N^2 <= d * sum_{k=1}^r lambda_k^2, i.e.

    trace(G^2) = sum_k lambda_k^2 = sum_{k=1}^r lambda_k^2 >= N^2/d.          (5)

On the other hand, directly from the entries of G (trace of a product of symmetric matrices is
the sum of squared entries):

    trace(G^2) = sum_{i,j} G_ij^2 = sum_i G_ii^2 + sum_{i != j} G_ij^2 = N + 2*sum_{i<j} a_ij^2,

using G_ii=1 (N terms, each squared to 1) and symmetry (each unordered pair i<j contributes
G_ij^2 twice in the i!=j sum). Combining with (5):

    N + 2*sum_{i<j} a_ij^2 >= N^2/d,

so

    sum_{i<j} a_ij^2 >= (N^2/d - N)/2 = N(N-d)/(2d).                          (6)

Specializing to N=d+2:

    sum_{i<j} a_ij^2 >= (d+2)(d+2-d)/(2d) = (d+2)*2/(2d) = (d+2)/d.           (7)

This holds for every d>=1 (in particular every d>=2), and for every choice of N=d+2 unit vectors
in R^d. Step 3 uses only standard linear algebra (Gram matrices, spectral theorem, Cauchy-Schwarz)
and no citation specific to this problem.

## Step 4 (from squared cosines to T: a general but weak bound, all d>=2)

For x in [0,1]: arcsin(x) >= x. Proof: arcsin'(t) = 1/sqrt(1-t^2) >= 1 for all t in [0,1) (since
0 <= 1-t^2 <= 1 there), so arcsin(x) = integral_0^x arcsin'(t) dt >= integral_0^x 1 dt = x (this
also holds trivially at x=1 by continuity). Also x >= x^2 for x in [0,1], since x(1-x) >= 0.
Hence

    arcsin(x) >= x^2   for all x in [0,1].                                    (8)

Applying (8) with x = |a_ij| in [0,1] and summing over all pairs i<j, using (7):

    T = sum_{i<j} arcsin|a_ij| >= sum_{i<j} a_ij^2 >= (d+2)/d.                (9)

Inequality (9) is a fully proved, unconditional statement: for every d>=2 and every N=d+2 unit
vectors in R^d, T >= (d+2)/d = 1 + 2/d. Equivalently, by Step 2,

    S <= (C(d+2,2) - 1 - 2/d) * (pi/2)   for every d>=2.                     (9')

This is a TRUE, general (all d) inequality, but it is WEAKER than the target: since 1+2/d <= 2 <
pi for every d>=2 (as 2/d <= 1), the bound (9) never reaches the needed T >= pi (3). So Step 4
alone does not establish the target inequality for any d. It is recorded as an honest partial
result.

## Step 5 (exact proof of the target for d=2)

Here we prove (3), T >= pi, directly for d=2 (equivalently S <= 2*pi for N=4 lines in R^2), by a
different, self-contained argument (not using Steps 3-4).

A line in R^2 through the origin is uniquely determined by an angle phi in the circle group
R/(pi*Z) (circumference pi): the line is spanned by (cos phi, sin phi), and phi, phi' represent
the same line iff phi - phi' is a multiple of pi. For two lines with angles phi, phi', the acute
angle between them is theta = arccos|cos(phi-phi')|. Writing alpha = phi - phi' mod pi, taken in
[0,pi), we have |cos(alpha)| = cos(alpha) if alpha <= pi/2, and |cos(alpha)| = cos(pi-alpha) =
-cos(alpha) if alpha > pi/2 -- wait, more directly: arccos|cos(alpha)| is, for alpha in [0,pi),
exactly min(alpha, pi - alpha) (this is the standard fact that arccos(cos(alpha)) = alpha for
alpha in [0,pi], and arccos|cos(alpha)| = min(arccos(cos(alpha)), arccos(cos(pi-alpha))) =
min(alpha, pi-alpha), since cos(pi-alpha) = -cos(alpha) has the same absolute value). Define
h(x) := min(x, pi-x) for x in [0,pi]; so theta(l,l') = h(alpha) where alpha in [0,pi) is a
representative of phi - phi' mod pi (h is well-defined on this representative since h(alpha) =
h(pi-alpha), so any choice of representative alpha or pi-alpha of the same class gives the same
value).

Let the 4 lines l_1,l_2,l_3,l_4 have angles phi_1,phi_2,phi_3,phi_4 in R/(pi*Z) (with repetitions
allowed, i.e. some phi_i may coincide). Relabel the 4 indices (a relabeling does not change S,
which is a sum over unordered pairs of all 4 lines) so that, listing representatives of
phi_1,...,phi_4 in [0,pi) in cyclic (non-decreasing, then wrapping) order, they become
p_1 <= p_2 <= p_3 <= p_4 in [0,pi), now indexed 1,2,3,4 in this cyclic order. Define the 4
consecutive gaps

    g_1 = p_2-p_1,  g_2 = p_3-p_2,  g_3 = p_4-p_3,  g_4 = pi-p_4+p_1  (wrap-around gap).

Each g_i >= 0 (by the sorted order and since p_1 in [0,pi)), and g_1+g_2+g_3+g_4 = pi (telescoping
sum, the four gaps partition the full circle of circumference pi).

Now compute all 6 pairwise theta's in terms of the g_i. For the 4 "adjacent" pairs (in the cyclic
order 1-2,2-3,3-4,4-1): the two arcs between p_1,p_2 around the circle have lengths g_1 and
pi-g_1 (the rest of the circle), so theta(l_1,l_2) = h(g_1); similarly theta(l_2,l_3)=h(g_2),
theta(l_3,l_4)=h(g_3), theta(l_4,l_1)=h(g_4). For the 2 "opposite" pairs: the two arcs between
p_1,p_3 have lengths g_1+g_2 and g_3+g_4 = pi-(g_1+g_2), so theta(l_1,l_3) = h(g_1+g_2); and the
two arcs between p_2,p_4 have lengths g_2+g_3 and g_4+g_1 = pi-(g_2+g_3), so
theta(l_2,l_4) = h(g_2+g_3). Hence

    S = h(g_1)+h(g_2)+h(g_3)+h(g_4) + h(g_1+g_2) + h(g_2+g_3) =: F(g_1,g_2,g_3,g_4).      (10)

We claim F <= 2*pi whenever g_i >= 0 and sum g_i = pi. Note first the elementary bound

    h(x) <= pi/2 for all x in [0,pi],                                        (11)

since h(x)=min(x,pi-x) <= (x+(pi-x))/2 = pi/2 (AM of the two arguments of the min is an upper
bound for the min).

Claim: at most one of g_1,...,g_4 exceeds pi/2. Indeed if g_j>pi/2 and g_k>pi/2 for j!=k, then
g_j+g_k>pi, but g_j+g_k <= g_1+g_2+g_3+g_4 = pi (as the other two gaps are >=0), a contradiction.

Case A: all g_i <= pi/2. Then h(g_i)=min(g_i,pi-g_i)=g_i for each i (since g_i <= pi-g_i
holds because g_i<=pi/2<=pi-g_i is equivalent to g_i<=pi/2). So
    h(g_1)+h(g_2)+h(g_3)+h(g_4) = g_1+g_2+g_3+g_4 = pi.
By (11), h(g_1+g_2) <= pi/2 and h(g_2+g_3) <= pi/2. Hence
    F <= pi + pi/2 + pi/2 = 2*pi.

Case B: exactly one g_k > pi/2 (k in {1,2,3,4}; by the Claim, exactly one, not more). Then for
i != k, g_i <= (sum_{i!=k} g_i) = pi-g_k < pi-pi/2 = pi/2 (using g_i>=0 for the other two terms
in the sum, so g_i <= pi - g_k for each such i), so h(g_i)=g_i as in Case A. Also h(g_k)=pi-g_k
(since g_k>pi/2 means g_k>pi-g_k). Hence
    h(g_1)+h(g_2)+h(g_3)+h(g_4) = (pi-g_k) + sum_{i!=k} g_i = (pi-g_k)+(pi-g_k) = 2*pi-2*g_k.
By (11) again, h(g_1+g_2)+h(g_2+g_3) <= pi. So
    F <= (2*pi - 2*g_k) + pi = 3*pi - 2*g_k < 3*pi - 2*(pi/2) = 2*pi,
using g_k > pi/2 strictly.

In both cases F <= 2*pi. By (10), S = F <= 2*pi = (C(4,2)-2)*(pi/2) (since C(4,2)=6,
(6-2)*pi/2 = 2*pi). This proves the target inequality exactly for d=2, for every choice of 4
lines in R^2 (including all degenerate/repeated cases, which correspond to some g_i=0, handled
within Case A since 0<=pi/2).

Equality is attained, e.g., by g=(0,pi/2,0,pi/2) (two coincident pairs of orthogonal lines: the
conjectured optimum) and by g=(pi/4,pi/4,pi/4,pi/4) (4 evenly spaced lines), both verified to give
F = 2*pi exactly (checked exactly in out/code/check_d2.py, and directly: in the first, adjacent
sum = 0+pi/2+0+pi/2=pi, opposite sum = h(pi/2)+h(pi/2)=pi, total 2*pi; in the second, all g_i=pi/4
so h(g_i)=pi/4, adjacent sum=pi, and g_1+g_2=g_2+g_3=pi/2 so opposite sum=pi, total 2*pi).

This completes a full, exact proof of the target statement for d=2.

## Step 6 (status for d>=3: GAP)

For d>=3, only the weaker inequality (9')/(9) from Step 4 is established
(T >= (d+2)/d, strictly less than the needed pi). Two attempts to close the gap were made and
both fall short (recorded for completeness, not resting any claim on them):

(a) *Averaging attempt.* If one had, for every (d+1)-subset of the N=d+2 lines (necessarily
linearly dependent, being d+1 vectors in R^d), a bound T_subset >= pi/2 (a "one smaller" version
of (3) for corank exactly 1), then summing this bound over all N choices of which single line to
delete and double counting (each pair i<j is inside exactly N-2 of the N subsets of size N-1)
gives (N-2)*T >= N*(pi/2), i.e. T >= N/(N-2)*(pi/2) = (d+2)/d * (pi/2). This equals pi exactly
when d=2 (matching Step 5) but is strictly less than pi for every d>=3 (e.g. d=3 gives
5/3*pi/2 = 5pi/6 < pi). So even granting the (unproved here) corank-1 lemma, this averaging route
does not reach the target for d>=3. [GAP - this sub-lemma for corank 1 was also not proved here,
and even if proved, the averaging is insufficiently sharp.]

(b) *Vertex/extremal-principle attempt.* Steps 3-4's bound sum a_ij^2 >= (d+2)/d, applied through
the function g(t)=arcsin(sqrt(t)) (t=a_ij^2) instead of the cruder linear bound (8), suggests
that the minimum of sum g(t_ij) given sum t_ij = (d+2)/d and each t_ij in [0,1] should be attained
at an extreme point of that polytope, giving a candidate improved bound
T >= pi/2 + arcsin(sqrt(2/d)) (matching pi exactly at d=2, but only ~2.53 < pi at d=3, and still
short of pi as d -> infinity, where it tends to pi/2). Even setting aside that this is still
insufficient for d>=3, making it rigorous would require proving that this "bang-bang" extremal
point is indeed the true minimizer of a sum of the function g (which is concave on [0,1/2] and
convex on [1/2,1], i.e. not globally convex or concave) over the relevant polytope -- a nontrivial
extremal-principle lemma that was not established here. [GAP - both the extra lemma and, even
granting it, the resulting bound do not reach pi for d>=3.]

No further approach was completed within the time available. The exact target inequality for
d>=3 is therefore an open GAP in this proof; only the weaker inequality (9') is established for
all d>=2, and the exact target is fully proved only for d=2.
