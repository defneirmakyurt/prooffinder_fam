For every integer N >= 0 and all lines l_1, ..., l_N through the origin of R^2 (repetitions allowed), S(l_1, ..., l_N) = sum_{1<=i<j<=N} theta(l_i, l_j) <= (pi/2) floor(N^2/4), where theta(l, l') = arccos|<x, x'>| for spanning unit vectors x, x'.

Status: **cell solved** (full statement, no gaps). No step rests on computation. The cell writes N without a range;
the proof works for every integer N >= 0 (for N = 0, 1 both sides are 0), so no reading of the range is lost.

Tools used (all standard textbook facts, named): the cosine subtraction formula; arccos as the inverse of cos on
[0, pi]; the Riemann integral of step functions (linearity, monotonicity, additivity over intervals, translation
x -> x + c and reflection x -> c - x); the floor function.

---

## Notation

**Step 0 (distance to a lattice).** For c > 0 and real t put dist(t, cZ) := min_{k in Z} |t - ck|.

(a) *The minimum exists, is attained at k0 = floor(t/c) or k0 + 1, and is at most c/2.* Write t = c k0 + r with
r in [0, c). For k <= k0 - 1, t - ck = c(k0 - k) + r >= c; for k >= k0 + 2, ck - t = c(k - k0) - r >= 2c - r > c.
The two remaining values are |t - c k0| = r and |t - c(k0+1)| = c - r; both lie in (0, c] or [0, c), so both are
<= c, and min(r, c - r) <= c/2 because r + (c - r) = c. Every other k gives a value >= c >= min(r, c - r). Hence
the minimum over all k exists, equals min(r, c - r), is attained at k0 or k0 + 1, and is <= c/2.

(b) *dist(-t, cZ) = dist(t, cZ)*, because k -> -k is a bijection of Z and |-t - ck| = |t - c(-k)|.

(c) *dist(t + cm, cZ) = dist(t, cZ) for every integer m*, because k -> k - m is a bijection of Z and
|t + cm - ck| = |t - c(k - m)|.

(d) *dist(2t, 2cZ) = 2 dist(t, cZ)*, because |2t - 2ck| = 2|t - ck| for every k, so the two minima differ by the
factor 2.

Write delta(t) := dist(t, 2 pi Z). By (a) with c = 2 pi, delta(t) in [0, pi].

---

## Part I: the angle between two lines as half an arc distance

**Step 1 (parametrising lines).** A line l through the origin of R^2 is {lambda y : lambda in R} for some y != 0;
x = y/|y| is a unit vector spanning l. Every unit vector of R^2 has the form (cos a, sin a) for some real a (polar
coordinates). So for each i we fix a real a_i with l_i spanned by x_i := (cos a_i, sin a_i). (The definition of
theta uses any spanning unit vectors; the only choices are +-x_i, and |<x, x'>| does not depend on the signs.)

**Step 2 (inner product).** <x_i, x_j> = cos a_i cos a_j + sin a_i sin a_j = cos(a_i - a_j), by the cosine
subtraction formula.

**Step 3 (arccos|cos t| = dist(t, pi Z)).** Let t be real and r := dist(t, pi Z). By Step 0(a) with c = pi there is
an integer k with |t - k pi| = r and 0 <= r <= pi/2. By the cosine addition formula,
cos t = cos(k pi + (t - k pi)) = cos(k pi) cos(t - k pi) - sin(k pi) sin(t - k pi) = (-1)^k cos(t - k pi),
since cos(k pi) = (-1)^k and sin(k pi) = 0. Hence |cos t| = |cos(t - k pi)|. As t - k pi = +r or -r and cos is even,
|cos t| = |cos r| = cos r, the last equality because 0 <= r <= pi/2 gives cos r >= 0. Finally arccos is the inverse
of the restriction of cos to [0, pi] and r lies in [0, pi], so arccos|cos t| = arccos(cos r) = r.

Combining Steps 2 and 3: theta(l_i, l_j) = arccos|cos(a_i - a_j)| = dist(a_i - a_j, pi Z).

**Step 4 (doubling).** Put u_i := 2 a_i. By Step 0(d) with c = pi,
delta(u_i - u_j) = dist(2(a_i - a_j), 2 pi Z) = 2 dist(a_i - a_j, pi Z) = 2 theta(l_i, l_j). Therefore

    theta(l_i, l_j) = (1/2) delta(u_i - u_j)        for all i, j.                     (4.1)

---

## Part II: a semicircle identity for delta

**Step 5 (the half-period indicator g).** Define g : R -> {0, 1} by g(x) = 1 if x - 2 pi floor(x/(2 pi)) lies in
[0, pi), and g(x) = 0 otherwise.

(a) *Description.* g(x) = 1 if and only if x lies in U := union over m in Z of [2 pi m, 2 pi m + pi).
Proof: with m0 = floor(x/(2 pi)) we have x = 2 pi m0 + rho, rho in [0, 2 pi); if rho < pi then x is in
[2 pi m0, 2 pi m0 + pi) inside U. Conversely, if x is in [2 pi m, 2 pi m + pi) for some m, then
2 pi m <= x < 2 pi (m + 1), so floor(x/(2 pi)) = m and x - 2 pi m is in [0, pi), i.e. g(x) = 1.

(b) *Periodicity.* g(x + 2 pi) = g(x), since x is in [2 pi m, 2 pi m + pi) iff x + 2 pi is in
[2 pi (m+1), 2 pi (m+1) + pi), so x is in U iff x + 2 pi is in U.

(c) *Integrability.* On a bounded interval [A, B] only finitely many intervals [2 pi m, 2 pi m + pi) meet [A, B],
so by (a) the restriction of g to [A, B] is the indicator of a finite union of intervals, i.e. a step function,
hence Riemann integrable. For fixed reals u, v the functions psi -> g(u - psi), psi -> g(v - psi) and
psi -> |g(u - psi) - g(v - psi)| are likewise step functions on [0, 2 pi] (preimages of finitely many intervals
under psi -> u - psi are finitely many intervals), so all integrals below exist.

**Step 6 (integrals over one period).** If F : R -> R is 2 pi-periodic and Riemann integrable on bounded
intervals, then for every real a, integral_a^{a + 2 pi} F = integral_0^{2 pi} F.
Proof: write a = 2 pi n + b with n = floor(a/(2 pi)), b in [0, 2 pi). By additivity over intervals,
integral_a^{a+2pi} F = integral_{2pi n + b}^{2pi(n+1)} F + integral_{2pi(n+1)}^{2pi(n+1) + b} F.
By the translation x -> x - 2 pi n (resp. x -> x - 2 pi (n+1)) and periodicity, these equal
integral_b^{2pi} F and integral_0^{b} F, whose sum is integral_0^{2pi} F.

**Step 7 (reduction to one variable).** For real s put D(s) := integral_0^{2 pi} |g(x) - g(x + s)| dx.
Claim: for all real u, v,

    integral_0^{2 pi} |g(u - psi) - g(v - psi)| d psi = D(v - u).                     (7.1)

Proof: let s = v - u and F(x) := |g(x) - g(x + s)|; F is 2 pi-periodic by Step 5(b) and integrable on bounded
intervals by Step 5(c). Since v - psi = (u - psi) + s, the integrand in (7.1) is F(u - psi). The reflection
x = u - psi maps [0, 2 pi] onto [u - 2 pi, u], so the left side equals integral_{u - 2 pi}^{u} F(x) dx, which is
integral_0^{2 pi} F = D(s) by Step 6 (with a = u - 2 pi).

**Step 8 (symmetry and periodicity of D).**
(a) D(s + 2 pi) = D(s), because g(x + s + 2 pi) = g(x + s) by Step 5(b), so the integrands coincide.
(b) D(-s) = D(s): D(-s) = integral_0^{2 pi} |g(x) - g(x - s)| dx. The translation y = x - s turns this into
integral_{-s}^{2 pi - s} |g(y + s) - g(y)| dy, and the integrand y -> |g(y) - g(y + s)| is 2 pi-periodic and
integrable on bounded intervals (Step 5(b), (c)), so by Step 6 (with a = -s) this equals
integral_0^{2 pi} |g(y) - g(y + s)| dy = D(s).

**Step 9 (D on [0, pi]).** For 0 <= s <= pi, D(s) = 2s.
Proof: take x in [0, 2 pi). By Step 5(a), g(x) = 1 iff x is in U; the only interval of U meeting [0, 2 pi) is
[0, pi) (m = 0), so the set where g(x) = 1 is A := [0, pi).
Next, x + s lies in [s, 2 pi + s), a subset of [0, 3 pi). The intervals of U meeting [0, 3 pi) are [0, pi) and
[2 pi, 3 pi) (m = 0, 1). So g(x + s) = 1 iff x + s is in [0, pi) or in [2 pi, 3 pi), i.e. iff x is in
[-s, pi - s) or in [2 pi - s, 3 pi - s). Intersecting with [0, 2 pi) and using 0 <= s <= pi (so -s <= 0,
pi - s >= 0, 2 pi - s >= pi >= 0 and 3 pi - s >= 2 pi), the set where g(x + s) = 1 is
B := [0, pi - s) union [2 pi - s, 2 pi).
Since 2 pi - s >= pi, the interval [2 pi - s, 2 pi) is disjoint from A, and [0, pi - s) is contained in A. Hence
A \ B = [pi - s, pi) and B \ A = [2 pi - s, 2 pi). The integrand |g(x) - g(x + s)| equals 1 exactly on
(A \ B) union (B \ A) = [pi - s, pi) union [2 pi - s, 2 pi), two disjoint intervals (pi <= 2 pi - s) of length s
each, and 0 elsewhere on [0, 2 pi). The value of the integrand at the single point x = 2 pi does not affect the
Riemann integral. Therefore D(s) = s + s = 2s.

**Step 10 (the semicircle identity).** For all real u, v,

    integral_0^{2 pi} |g(u - psi) - g(v - psi)| d psi = 2 delta(u - v).               (10.1)

Proof: let s = v - u. By Step 0(a) with c = 2 pi there is an integer k with |s - 2 pi k| = delta(s) =: r, and
r is in [0, pi]. Applying Step 8(a) |k| times (in the appropriate direction), D(s) = D(s - 2 pi k). Now s - 2 pi k
is r or -r, and D(-r) = D(r) by Step 8(b); so D(s) = D(r) = 2r by Step 9. Thus D(v - u) = 2 delta(v - u), and
delta(v - u) = delta(u - v) by Step 0(b). Combine with (7.1).

---

## Part III: counting and conclusion

**Step 11 (counting separated pairs).** Fix psi in [0, 2 pi] and let K(psi) := {i in {1, ..., N} : g(u_i - psi) = 1},
k(psi) := |K(psi)|. For i < j the number |g(u_i - psi) - g(u_j - psi)| lies in {0, 1}, and it equals 1 exactly
when one of i, j lies in K(psi) and the other does not. A 2-element subset {i, j} of {1, ..., N} with exactly one
element in K(psi) is determined by choosing that element in K(psi) (k(psi) ways) and the other element in the
complement ((N - k(psi)) ways), and each such subset arises from exactly one such choice. Hence

    P(psi) := sum_{1<=i<j<=N} |g(u_i - psi) - g(u_j - psi)| = k(psi) (N - k(psi)).     (11.1)

**Step 12 (integer bound).** For integers 0 <= k <= N: 4k(N - k) = N^2 - (N - 2k)^2 <= N^2, so k(N - k) <= N^2/4;
since k(N - k) is an integer, k(N - k) <= floor(N^2/4).

**Step 13 (the target).** Using (4.1), then (10.1) for each pair, then linearity of the Riemann integral over the
finite sum (Step 5(c) gives integrability), then (11.1) and Step 12 with monotonicity of the integral:

    S(l_1, ..., l_N) = sum_{i<j} (1/2) delta(u_i - u_j)
                     = sum_{i<j} (1/4) integral_0^{2 pi} |g(u_i - psi) - g(u_j - psi)| d psi
                     = (1/4) integral_0^{2 pi} P(psi) d psi
                     = (1/4) integral_0^{2 pi} k(psi)(N - k(psi)) d psi
                     <= (1/4) integral_0^{2 pi} floor(N^2/4) d psi
                     = (1/4) (2 pi) floor(N^2/4) = (pi/2) floor(N^2/4).

This holds for every N >= 0 and every choice of lines, including repeated lines (if l_i = l_j then a_i - a_j is a
multiple of pi, delta(u_i - u_j) = 0, and nothing in Steps 1-13 assumed the lines distinct). For N = 0 and N = 1
the sum S is empty and both sides are 0. QED.

---

## Remark (sharpness; not needed for the target)

**Step 14.** The bound is attained: take floor(N/2) copies of the x-axis and ceil(N/2) copies of the y-axis. Two
copies of the same axis give theta = arccos 1 = 0, and an x-axis copy with a y-axis copy gives
theta = arccos 0 = pi/2, so S = (pi/2) floor(N/2) ceil(N/2). For N = 2m this is (pi/2) m^2 = (pi/2) N^2/4; for
N = 2m + 1 it is (pi/2) m(m + 1), and floor(N^2/4) = floor(m^2 + m + 1/4) = m^2 + m. So the inequality is an
equality there.

## What is established and what is not

Established: the full cell-1 statement, for all N >= 0 and all (possibly repeated) lines in R^2, by a written
argument using only standard facts about cos/arccos and the Riemann integral of step functions.
Not established / not claimed: anything about d >= 3; the characterisation of all equality cases (for odd N there
are other maximisers, e.g. N = 3 lines at mutual angles pi/3; this is not needed). The script
out/code/sanity_check.py is a floating-point spot-check only; no step of the proof depends on it.
