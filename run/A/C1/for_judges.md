# Cell 1: Lines in the Plane

**Statement.** Let l_1, ..., l_N be lines in R^2. Prove that S(l_1, ..., l_N) <= (pi/2) floor(N^2/4).

**Status.** Solved. Complete written proof for every N >= 0. No step relies on computation. No published result is cited; the argument is our own.

**Proof.**

For every integer N >= 0 and all lines l_1, ..., l_N through the origin of R^2 (repetitions allowed), S(l_1, ..., l_N) = sum_{1<=i<j<=N} theta(l_i, l_j) <= (pi/2) floor(N^2/4), where theta(l, l') = arccos|<x, x'>| for unit vectors x, x' spanning l, l'.

Conventions. "Line" means a line through the origin (a 1-dimensional linear subspace), as in the statement's definition. Integrals are Riemann integrals; every integrand below is, on each bounded interval, a finite linear combination of indicator functions of intervals, hence Riemann integrable, and linearity, monotonicity and the substitution t = s + c hold for them (standard calculus). For a statement P, 1[P] is 1 if P holds and 0 otherwise.

---

**Step 1 (parametrisation).** For a in R put u(a) = (cos a, sin a). Every line l in R^2 is spanned by u(a) for some a in [0, pi).

Proof. l is spanned by a nonzero vector v; x = v/|v| is a unit vector spanning l. By polar coordinates, x = (cos alpha, sin alpha) for some alpha in [0, 2 pi). If alpha < pi take a = alpha. If alpha >= pi, then -x = (cos(alpha - pi), sin(alpha - pi)) also spans l and alpha - pi is in [0, pi); take a = alpha - pi.

**Step 2 (theta is well defined; inner product).** If y is a unit vector spanning the same line as a unit vector x, then y = c x with |c| = |y|/|x| = 1, so y = x or y = -x. Hence for unit vectors x, x' spanning l, l', the number |<x, x'>| does not depend on the choice (|<±x, ±x'>| = |<x, x'>|), and theta(l, l') = arccos|<x, x'>| is well defined. For l, l' spanned by u(a), u(b) (unit vectors, since cos^2 + sin^2 = 1):
<u(a), u(b)> = cos a cos b + sin a sin b = cos(a - b) (cosine subtraction formula), so theta(l, l') = arccos|cos(a - b)|.

**Step 3 (the function rho).** For z in R define rho(z) = min_{k in Z} |z - k pi|.

(3a) The minimum exists and rho(z) is in [0, pi/2]. Let k0 = floor(z/pi + 1/2). Then k0 <= z/pi + 1/2 < k0 + 1, so |z/pi - k0| <= 1/2, i.e. |z - k0 pi| <= pi/2. For an integer k != k0, |z - k pi| >= |k - k0| pi - |z - k0 pi| >= pi - pi/2 = pi/2 >= |z - k0 pi| (triangle inequality). So the minimum is attained at k0 and rho(z) = |z - k0 pi| <= pi/2.

(3b) rho(z + pi) = rho(z): {|z + pi - k pi| : k in Z} = {|z - (k-1) pi| : k in Z}, the same set of numbers.

(3c) rho(-z) = rho(z): |-z - k pi| = |z - (-k) pi|, and k -> -k is a bijection of Z.

(3d) If |z| <= pi/2 then rho(z) = |z|: k = 0 gives |z|, and for k != 0, |z - k pi| >= |k| pi - |z| >= pi - pi/2 = pi/2 >= |z|.

(3e) If z in [-pi, -pi/2] then rho(z) = z + pi: indeed z + pi is in [0, pi/2], so by (3b) and (3d), rho(z) = rho(z + pi) = |z + pi| = z + pi.

**Step 4 (angle formula).** For real a, b: arccos|cos(a - b)| = rho(a - b). Consequently, if l, l' are spanned by u(a), u(b), then theta(l, l') = rho(a - b).

Proof. Put z = a - b, take k0 from (3a) and w = z - k0 pi, so |w| = rho(z) is in [0, pi/2]. Then cos z = cos(w + k0 pi) = (-1)^{k0} cos w, so |cos z| = |cos w| = |cos |w|| (cos is even) = cos |w| (cos >= 0 on [0, pi/2]). Since |w| is in [0, pi] and arccos is the inverse of cos restricted to [0, pi], arccos|cos z| = arccos(cos|w|) = |w| = rho(z). The second sentence follows from Step 2.

**Step 5 (the cut function g).** Define g : R -> {0, 1} by g(z) = 1[rho(z) < pi/4].

(5a) g(z + pi) = g(z) and g(-z) = g(z), by (3b), (3c).

(5b) {z : g(z) = 1} is the union over k in Z of the open intervals (k pi - pi/4, k pi + pi/4): by definition of rho as a minimum, rho(z) < pi/4 holds iff |z - k pi| < pi/4 for some k in Z. These intervals are pairwise disjoint and only finitely many meet any bounded interval, so g restricted to a bounded interval is a finite sum of indicator functions of intervals (Riemann integrable).

(5c) On [-pi/2, pi/2], g(z) = 1 iff |z| < pi/4: the interval (k pi - pi/4, k pi + pi/4) with k >= 1 lies in (3pi/4, infinity) and with k <= -1 lies in (-infinity, -3pi/4), so neither meets [-pi/2, pi/2]; only k = 0 contributes.

**Step 6 (integrals over a period).** Let F : R -> R be pi-periodic and Riemann integrable on bounded intervals. Then for every real c, int_c^{c+pi} F = int_0^pi F.

Proof. Write c = m pi + r with m in Z and r in [0, pi). Then int_c^{c+pi} F = int_{m pi + r}^{(m+1) pi} F + int_{(m+1) pi}^{(m+1) pi + r} F. Substituting t = s + m pi in the first integral and t = s + (m+1) pi in the second, and using F(s + j pi) = F(s) for all integers j (from F(s + pi) = F(s) for all s: induction on j >= 0, and for j < 0 apply the case -j >= 0 at the point s + j pi, giving F(s) = F((s + j pi) + (-j) pi) = F(s + j pi)), this equals int_r^pi F + int_0^r F = int_0^pi F.

In particular int_0^pi g = int_{-pi/2}^{pi/2} g = length of (-pi/4, pi/4) = pi/2, by Step 6 with c = -pi/2 and (5c).

**Step 7 (overlap lemma).** For theta in [0, pi/2]: int_{-pi/2}^{pi/2} g(s) g(s - theta) ds = pi/2 - theta.

Proof. By (5c), for s in [-pi/2, pi/2], g(s) = 1 iff s is in (-pi/4, pi/4). Fix s in (-pi/4, pi/4). Then s - theta is in (-pi/4 - theta, pi/4 - theta), a subset of (-3pi/4, pi/4) because 0 <= theta <= pi/2. Two cases.
- If s - theta is in [-pi/2, pi/4): by (3d), rho(s - theta) = |s - theta|, so g(s - theta) = 1 iff -pi/4 < s - theta < pi/4; the right inequality holds automatically (s < pi/4, theta >= 0), so g(s - theta) = 1 iff s - theta > -pi/4.
- If s - theta is in (-3pi/4, -pi/2): by (3e), rho(s - theta) = s - theta + pi, which lies in (pi/4, pi/2), so g(s - theta) = 0; and also s - theta > -pi/4 fails.
In both cases, for s in (-pi/4, pi/4): g(s - theta) = 1 iff s > theta - pi/4. Hence, for s in [-pi/2, pi/2], g(s) g(s - theta) = 1 iff s is in (-pi/4, pi/4) and s > theta - pi/4, i.e. iff s is in (theta - pi/4, pi/4) (using theta - pi/4 >= -pi/4); otherwise it is 0. This interval lies in [-pi/2, pi/2] and has length pi/2 - theta >= 0, which is the value of the integral.

**Step 8 (cut identity).** For all real x, y: int_0^pi |g(t - x) - g(t - y)| dt = 2 rho(x - y).

Proof. For p, q in {0, 1}, |p - q| = p + q - 2pq (check the four cases: (0,0) gives 0 = 0; (1,0) and (0,1) give 1 = 1; (1,1) gives 0 = 1 + 1 - 2). Hence
int_0^pi |g(t-x) - g(t-y)| dt = A_x + A_y - 2B, where A_x = int_0^pi g(t - x) dt, A_y likewise, B = int_0^pi g(t - x) g(t - y) dt.
- A_x: substituting s = t - x, A_x = int_{-x}^{pi - x} g(s) ds = int_0^pi g = pi/2 (Step 6 with c = -x, g pi-periodic by (5a); value from the end of Step 6). The same computation with y in place of x (substitute s = t - y, then Step 6 with c = -y) gives A_y = pi/2.
- B: substituting s = t - x and putting delta = y - x, B = int_{-x}^{pi-x} g(s) g(s - delta) ds. The function s -> g(s) g(s - delta) is pi-periodic by (5a), so by Step 6 (c = -x, then c = -pi/2) B = int_{-pi/2}^{pi/2} g(s) g(s - delta) ds. Let k0 be as in (3a) for z = delta and delta' = delta - k0 pi, so |delta'| = rho(delta) <= pi/2. By (5a) (applied |k0| times), g(s - delta) = g(s - delta' - k0 pi) = g(s - delta').
  - If delta' >= 0: Step 7 with theta = delta' = rho(delta) gives B = pi/2 - rho(delta).
  - If delta' < 0: substitute s = -r: B = int_{-pi/2}^{pi/2} g(-r) g(-r - delta') dr = int_{-pi/2}^{pi/2} g(r) g(r + delta') dr (g even, (5a)) = int_{-pi/2}^{pi/2} g(r) g(r - |delta'|) dr, and Step 7 with theta = |delta'| = rho(delta) gives B = pi/2 - rho(delta).
  Finally rho(delta) = rho(y - x) = rho(x - y) by (3c). So B = pi/2 - rho(x - y).
Therefore the integral equals pi/2 + pi/2 - 2(pi/2 - rho(x - y)) = 2 rho(x - y).

**Step 9 (integer bound).** For integers N >= 0 and k: k(N - k) <= floor(N^2/4).

Proof. 4k(N - k) = N^2 - (N - 2k)^2. If N is even, then 4k(N - k) <= N^2, so k(N - k) <= N^2/4 = floor(N^2/4) (N^2/4 is an integer). If N = 2m + 1 is odd, N - 2k is odd, so (N - 2k)^2 >= 1 and 4k(N - k) <= N^2 - 1 = 4(m^2 + m), so k(N - k) <= m^2 + m = floor((4m^2 + 4m + 1)/4) = floor(N^2/4).

**Step 10 (pair count).** Let a_1, ..., a_N be real, fix t in R, let I(t) = {i : g(t - a_i) = 1} and k(t) = |I(t)|, an integer in {0, ..., N}. Then sum_{1<=i<j<=N} |g(t - a_i) - g(t - a_j)| = k(t)(N - k(t)).

Proof. Each term is 1 if exactly one of i, j lies in I(t) and 0 otherwise (the values are in {0,1}). An unordered pair {i, j} of distinct indices with exactly one element in I(t) is determined by choosing its element in I(t) (k(t) ways) and its element outside I(t) (N - k(t) ways), and distinct choices give distinct pairs; so there are exactly k(t)(N - k(t)) such pairs, and each appears exactly once in the sum over i < j.

**Step 11 (main inequality).** Let l_1, ..., l_N be lines in R^2 (repetitions allowed). By Step 1 choose a_i in [0, pi) with l_i spanned by u(a_i). By Step 4 and Step 8,
theta(l_i, l_j) = rho(a_i - a_j) = (1/2) int_0^pi |g(t - a_i) - g(t - a_j)| dt   for all i < j.
Summing this finite family and using linearity of the integral and Step 10,
S(l_1, ..., l_N) = (1/2) int_0^pi sum_{i<j} |g(t - a_i) - g(t - a_j)| dt = (1/2) int_0^pi k(t)(N - k(t)) dt.
By Step 9 applied with k = k(t) for each t, the integrand is at most floor(N^2/4) at every t, so by monotonicity of the integral
S(l_1, ..., l_N) <= (1/2) * pi * floor(N^2/4) = (pi/2) floor(N^2/4).

**Step 12 (degenerate cases).** For N = 0 and N = 1 the sum S is empty, S = 0, and (pi/2) floor(N^2/4) = 0 since floor(0) = floor(1/4) = 0; this is also what Step 11 gives (k(N - k) = 0 for k in {0,...,N} when N <= 1). Repeated lines are allowed in Steps 1-11: nothing there assumes the a_i distinct (a repeated line contributes rho(0) = 0 to its pair, and Step 10 counts indices, not distinct values).

**Step 13 (sharpness; not required by the cell).** Let m = floor(N/2). Take m copies of the line spanned by u(0) and N - m copies of the line spanned by u(pi/2). By Step 4, a pair of equal lines has theta = rho(0) = 0 and a mixed pair has theta = rho(pi/2) = pi/2 (by (3d)); there are m(N - m) mixed pairs. So S = (pi/2) m(N - m), and m(N - m) = m^2 = N^2/4 for N = 2m, m(N - m) = m(m + 1) = floor(N^2/4) for N = 2m + 1 (Step 9 computation). Hence the bound is attained for every N, and the inequality of Step 11 is the best possible.

---

What is established: the full target for every N >= 0 (N = 0, 1 trivially), all lines through the origin of R^2, with repetitions. What is not claimed: characterisation of all equality cases (not asked). No computation is used in the proof.
