For every integer N >= 0 and all lines l_1, ..., l_N through the origin of R^2 (repetitions allowed), S(l_1, ..., l_N) = sum_{1<=i<j<=N} theta(l_i, l_j) <= (pi/2) floor(N^2/4), where theta(l, l') = arccos|<x, x'>| for unit vectors x, x' spanning l, l'.

Status: **cell A-C1 solved** (two complete, independent written proofs, no [GAP]; no step rests on computation).

- Proof B (main, independent of the blind runs): perpendicular-pair invariance + a variational (rotation) argument on a maximiser + induction N -> N-2. Technique from Fodor-Vigh-Zarnocz, Arch. Math. 106 (2016), Theorem 2.1 (see sources.md); the write-up and the maximiser/induction organisation below are my own and fill steps that the published proof leaves as "clearly" / "by symmetry" / "obvious".
- Proof A (second proof): averaging over "quarter-turn cuts" (the L2 quadrant-discrepancy / Stolarsky identity for S^1 of Bilyk-Matzke, arXiv:1801.07837, Section 4.3), written out in full.

No citation is used as a proof: every step is proved here. Integrals are Riemann integrals of step functions.

---

## Part 0. Common preliminaries

**Step 0.1 (parametrisation).** Put u(a) = (cos a, sin a) for real a; |u(a)| = 1. Every line l in R^2 is spanned by u(a) for some real a (indeed for some a in [0, pi)). Proof: l is spanned by some v != 0; x = v/|v| is a unit vector spanning l, and by polar coordinates x = u(b) for some b in [0, 2 pi). If b < pi take a = b; otherwise -x = (cos(b - pi), sin(b - pi)) = u(b - pi) also spans l and b - pi is in [0, pi). Conversely every real a gives a line R u(a), and u(a + pi) = -u(a) spans the same line.

**Step 0.2 (theta well defined).** If unit vectors y, x span the same line then y = c x with |c| = 1, i.e. y = +-x. So |<x, x'>| does not depend on the choice of spanning unit vectors, and theta(l, l') is well defined. For l = R u(a), l' = R u(b): <u(a), u(b)> = cos a cos b + sin a sin b = cos(a - b) (cosine subtraction formula), so theta(l, l') = arccos|cos(a - b)|.

**Step 0.3 (the function rho).** For real z put rho(z) = min_{k in Z} |z - k pi|.
(a) The minimum exists and lies in [0, pi/2]: let k0 = floor(z/pi + 1/2); then |z/pi - k0| <= 1/2, i.e. |z - k0 pi| <= pi/2, and for k != k0, |z - k pi| >= |k - k0| pi - |z - k0 pi| >= pi - pi/2 >= |z - k0 pi|. So rho(z) = |z - k0 pi| <= pi/2.
(b) rho(z + pi) = rho(z) and rho(-z) = rho(z): the sets {|z + pi - k pi|} and {|z - k pi|} (k in Z) coincide (reindex k -> k - 1), and |-z - k pi| = |z - (-k) pi|.
(c) If |z| <= pi/2 then rho(z) = |z|: k = 0 gives |z|, and for k != 0, |z - k pi| >= pi - |z| >= pi/2 >= |z|.
(d) rho is 1-Lipschitz, hence continuous: for real z, z' and every k, |z - k pi| <= |z - z'| + |z' - k pi|; minimising over k gives rho(z) <= |z - z'| + rho(z'), and symmetrically.

**Step 0.4 (angle formula).** For real a, b: theta(R u(a), R u(b)) = arccos|cos(a - b)| = rho(a - b).
Proof. Let z = a - b, k0 as in 0.3(a), w = z - k0 pi, so |w| = rho(z) is in [0, pi/2]. cos z = cos(w + k0 pi) = (-1)^{k0} cos w, so |cos z| = |cos w| = cos|w| (cos even, and cos >= 0 on [0, pi/2]). Since |w| is in [0, pi] and arccos inverts cos on [0, pi], arccos|cos z| = |w| = rho(z).

**Step 0.5 (integer bound).** For integers N >= 0 and k: k(N - k) <= floor(N^2/4). Proof: 4k(N - k) = N^2 - (N - 2k)^2. If N is even, 4k(N-k) <= N^2 and N^2/4 is an integer. If N = 2m + 1, N - 2k is odd so (N - 2k)^2 >= 1, hence 4k(N - k) <= N^2 - 1 = 4(m^2 + m) and k(N - k) <= m^2 + m = floor(N^2/4).

**Step 0.6 (reformulation).** For a = (a_1, ..., a_N) in R^N put F_N(a) = sum_{1<=i<j<=N} rho(a_i - a_j). By 0.1 and 0.4, the set of values S(l_1, ..., l_N) over all N-tuples of lines equals the set of values F_N(a) over a in R^N (each tuple of lines is R u(a_1), ..., R u(a_N) for some a, and each a gives a tuple of lines). Repetitions are allowed on both sides (a_i may coincide). So the target is: F_N(a) <= (pi/2) floor(N^2/4) for all a in R^N.

---

## Part B. Proof B (perpendicular pairs and a maximiser)

**Step B1 (a perpendicular pair splits every angle).** If theta(l, l') = pi/2, then for every line m: theta(l, m) + theta(l', m) = pi/2.
Proof. Let x, x', y be unit vectors spanning l, l', m. theta(l, l') = pi/2 means arccos|<x, x'>| = pi/2, i.e. <x, x'> = 0, so {x, x'} is an orthonormal basis of R^2 and 1 = |y|^2 = <x, y>^2 + <x', y>^2. Put t1 = theta(l, m) = arccos|<x, y>| in [0, pi/2]. Then |<x, y>| = cos t1 and |<x', y>| = sqrt(1 - cos^2 t1) = sin t1 (sin t1 >= 0 on [0, pi/2]) = cos(pi/2 - t1). As pi/2 - t1 is in [0, pi/2], a subset of [0, pi], theta(l', m) = arccos(cos(pi/2 - t1)) = pi/2 - t1.

**Step B2 (removing a perpendicular pair).** If among l_1, ..., l_N (N >= 2) there are indices p != q with theta(l_p, l_q) = pi/2, and R denotes the (N-2)-tuple of the other lines, then S(l_1, ..., l_N) = (N - 1) pi/2 + S(R).
Proof. Split the pairs {i, j} into: the pair {p, q} (contributes pi/2); pairs with exactly one index in {p, q}, grouped by the other index m (N - 2 groups, each contributing theta(l_p, l_m) + theta(l_q, l_m) = pi/2 by B1); pairs inside the complement (contribute S(R)). Total pi/2 + (N-2) pi/2 + S(R).

**Step B3 (a maximum exists).** Let M(N) = sup over a in R^N of F_N(a). F_N is continuous (by 0.3(d), finite sum) and pi-periodic in each coordinate (0.3(b)), so its values on R^N are its values on the compact cube [0, pi]^N, where a continuous function attains its maximum. Hence M(N) is finite and attained; call a in R^N with F_N(a) = M(N) a *maximiser*. M(0) = M(1) = 0 (empty sums).

**Step B4 (local structure of a maximiser without perpendicular pairs).** Let N >= 2 and let a be a maximiser with rho(a_i - a_j) != pi/2 for all i != j. Then for every index n: (i) no i != n has rho(a_n - a_i) = 0, and (ii) with z_i defined below, #{i != n : z_i > 0} = #{i != n : z_i < 0}.
Proof. Fix n. For i != n let z_i be the representative of a_n - a_i modulo pi that lies in (-pi/2, pi/2]: z_i = a_n - a_i - k pi with k = ceil((a_n - a_i)/pi - 1/2) (then z_i/pi is in (-1/2, 1/2]). By 0.3(b),(c), rho(a_n - a_i) = rho(z_i) = |z_i|; since this is != pi/2, z_i is in (-pi/2, pi/2). Let eta = min( {pi/2 - |z_i| : i != n} union {|z_i| : i != n, z_i != 0} ) > 0 (a finite set of positive numbers; nonempty since N >= 2). For real e with |e| < eta: for each i != n, |z_i + e| < |z_i| + (pi/2 - |z_i|) = pi/2, so rho(a_n + e - a_i) = rho(z_i + e) = |z_i + e| (0.3(b),(c)); moreover z_i + e has the sign of z_i when z_i != 0 (as |e| < |z_i|). Put P = #{i != n : z_i > 0}, Q = #{i != n : z_i < 0}, C = #{i != n : z_i = 0}. Then
  f(e) := sum_{i != n} rho(a_n + e - a_i) = sum_{z_i>0} (z_i + e) + sum_{z_i<0} (-z_i - e) + sum_{z_i=0} |e| = f(0) + (P - Q) e + C |e|.
Replacing a_n by a_n + e changes F_N only in the pairs containing n, so F_N(a with a_n -> a_n + e) = F_N(a) + f(e) - f(0) <= F_N(a) by maximality. Take e = d and e = -d with 0 < d < eta: (P - Q) d + C d <= 0 and -(P - Q) d + C d <= 0. Adding: 2 C d <= 0, so C = 0, which is (i) (z_i = 0 iff rho(a_n - a_i) = 0). Then (P - Q) d <= 0 and -(P - Q) d <= 0 give P = Q, which is (ii).

**Step B5 (some maximiser has a perpendicular pair).** For N >= 2 there is a maximiser a' with rho(a'_p - a'_q) = pi/2 for some p != q.
Proof. Let a be a maximiser (B3). If a has a perpendicular pair, take a' = a. Otherwise fix n = N and use the notation of B4: C = 0, P = Q, all z_i (i != N) are nonzero and lie in (-pi/2, pi/2). Put
  e* = min( {-z_i : z_i < 0} union {pi/2 - z_i : z_i > 0} ),
a minimum of a finite nonempty set (N >= 2) of numbers in (0, pi/2), so 0 < e* < pi/2. For 0 <= e <= e*: if z_i > 0 then z_i + e is in (0, pi/2] (as e <= pi/2 - z_i), so rho(z_i + e) = z_i + e by 0.3(c); if z_i < 0 then z_i + e is in (-pi/2, 0] (as e <= -z_i), so rho(z_i + e) = -(z_i + e). Hence f(e) = f(0) + (P - Q) e = f(0) on [0, e*], and a' := (a with a_N -> a_N + e*) satisfies F_N(a') = F_N(a) = M(N): a' is a maximiser. By the choice of e*, some i != N has z_i + e* = 0 or z_i + e* = pi/2, i.e. rho(a'_N - a'_i) = 0 or = pi/2.
 - If = pi/2: a' has a perpendicular pair.
 - If = 0: a' is a maximiser in which two lines coincide. If a' had no perpendicular pair, B4(i) applied to a' (with n = N) would forbid rho(a'_N - a'_i) = 0; contradiction. So a' has a perpendicular pair.

**Step B6 (induction).** Claim: M(N) <= (pi/2) floor(N^2/4) for all N >= 0. Induction on N in steps of 2. N = 0, 1: M = 0 = (pi/2) floor(N^2/4) (floor(0) = floor(1/4) = 0). Let N >= 2 and assume the claim for N - 2. Take a' from B5; by 0.6 it is a tuple of lines with a perpendicular pair, so by B2, M(N) = F_N(a') = (N - 1) pi/2 + F_{N-2}(rest) <= (N - 1) pi/2 + M(N - 2) <= (pi/2) (N - 1 + floor((N - 2)^2/4)). Since N - 1 is an integer, N - 1 + floor((N-2)^2/4) = floor((N-2)^2/4 + N - 1) = floor(N^2/4). Hence M(N) <= (pi/2) floor(N^2/4).

**Step B7 (conclusion).** For any lines l_1, ..., l_N: S(l_1, ..., l_N) = F_N(a) for suitable a (0.6) <= M(N) <= (pi/2) floor(N^2/4). This is the target, for every N >= 0, repetitions allowed (nothing above assumed distinct lines; B4 even uses coincidences). QED (Proof B).

---

## Part A. Proof A (averaging over quarter-turn cuts)

**Step A1 (cut indicator).** For real u let chi(u) = 1 if u - pi floor(u/pi) is in [0, pi/2), and chi(u) = 0 otherwise. chi is pi-periodic (u -> u + pi shifts floor(u/pi) by 1 and leaves u - pi floor(u/pi) unchanged). On [0, pi), chi = indicator of [0, pi/2). On any bounded interval chi is a step function (the indicator of a finite union of intervals [k pi, k pi + pi/2)), so all integrals below exist. Integral over one period: for a pi-periodic function G integrable on bounded intervals and any real c, int_c^{c+pi} G = int_0^pi G (write c = m pi + r, 0 <= r < pi, split at (m+1) pi, translate each piece by an integer multiple of pi: int_{m pi + r}^{(m+1)pi} G = int_r^pi G and int_{(m+1)pi}^{(m+1)pi + r} G = int_0^r G).

**Step A2 (cut identity).** For all real a, b: int_0^pi |chi(a - t) - chi(b - t)| dt = 2 rho(a - b).
Proof. Substituting s = a - t (t in [0, pi] -> s in [a - pi, a]) and putting delta = b - a, the left side is int_{a-pi}^{a} |chi(s) - chi(s + delta)| ds = int_0^pi |chi(s) - chi(s + delta)| ds =: g(delta) (A1; the integrand is pi-periodic in s). g is pi-periodic in delta (chi is). Also g(-delta) = g(delta): substitute s = r + delta and use A1 again. Let k0 as in 0.3(a) for z = delta and delta' = delta - k0 pi, |delta'| = rho(delta) <= pi/2; then g(delta) = g(delta') = g(|delta'|). So it suffices to show g(d) = 2d for d in [0, pi/2]. For p, q in {0, 1}, |p - q| = p + q - 2pq (four cases). So g(d) = int_0^pi chi(s) ds + int_0^pi chi(s + d) ds - 2 int_0^pi chi(s) chi(s + d) ds = pi/2 + pi/2 - 2 I, using A1 (the second integral equals int_d^{d+pi} chi = int_0^pi chi = pi/2). For s in [0, pi): chi(s) = 1 iff s < pi/2; and for such s, s + d is in [0, pi) (d <= pi/2), so chi(s + d) = 1 iff s + d < pi/2. Hence chi(s) chi(s + d) = 1 exactly for s in [0, pi/2 - d), I = pi/2 - d, and g(d) = pi - 2(pi/2 - d) = 2d. Finally rho(a - b) = rho(-(b - a)) = rho(delta) = |delta'| (0.3(b)), giving 2 rho(a - b).

**Step A3 (counting cut pairs).** Fix reals a_1, ..., a_N and t; let K(t) = {i : chi(a_i - t) = 1}, k(t) = |K(t)|. Each term |chi(a_i - t) - chi(a_j - t)| is 1 iff exactly one of i, j is in K(t), else 0. A pair {i, j} (i < j) with exactly one element in K(t) is determined by its element in K(t) (k(t) choices) and its element outside (N - k(t) choices), each such pair arising once. So sum_{i<j} |chi(a_i - t) - chi(a_j - t)| = k(t)(N - k(t)).

**Step A4 (conclusion).** With a as in 0.6, by 0.4 and A2, then linearity of the integral over the finite sum, A3, 0.5 and monotonicity of the integral:
S = sum_{i<j} rho(a_i - a_j) = (1/2) int_0^pi sum_{i<j} |chi(a_i - t) - chi(a_j - t)| dt = (1/2) int_0^pi k(t)(N - k(t)) dt <= (1/2) pi floor(N^2/4) = (pi/2) floor(N^2/4). QED (Proof A). N = 0, 1 give empty sums (both sides 0); repeated lines are allowed (A3 counts indices).

---

## Remark (sharpness; not required)
floor(N/2) copies of R u(0) and ceil(N/2) copies of R u(pi/2): mixed pairs have theta = rho(pi/2) = pi/2, equal pairs theta = 0, so S = (pi/2) floor(N/2) ceil(N/2) = (pi/2) floor(N^2/4) (N = 2m: m^2; N = 2m+1: m(m+1) = floor(m^2 + m + 1/4)). The bound is attained for every N.

## What is established / not established
Established: the full cell statement, all N >= 0, all (possibly repeated) lines through the origin of R^2, twice, by independent written arguments. Not claimed: characterisation of all maximisers (for odd N there are others, e.g. three lines at mutual angles pi/3 give S = pi = (pi/2) floor(9/4)). The script out/code/sanity_exact.py is an exact but non-load-bearing sanity check.
