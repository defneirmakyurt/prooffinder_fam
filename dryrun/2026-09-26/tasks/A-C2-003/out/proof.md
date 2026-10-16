For every integer m >= 2 and all unit vectors x_1, ..., x_m in R^(m-1) with <x_i, x_j> = 0 whenever |i - j| >= 2, we have sum_{i=1}^{m-1} theta(x_i, x_{i+1}) <= (m - 2) pi/2, where theta(x, y) = arccos|<x, y>| in [0, pi/2].

Status: cell A-C2 SOLVED by this write-up (complete proof, every m >= 2, no computation used).
Technique: Gram–Schmidt orthogonalisation along the chain. This is the continued-fraction / chain-sequence recursion for tridiagonal (Jacobi) Gram matrices, a classical tool (Wall; Chihara; Szwarc, see sources.md, references NOT opened). No result is cited; every step is proved below.

## Notation

Fix m >= 2 and x_1, ..., x_m as in the statement. For 1 <= k <= m-1 put
- a_k = <x_k, x_{k+1}>. Then |a_k| <= 1 by Cauchy–Schwarz, since |x_k| = |x_{k+1}| = 1.
- theta_k = theta(x_k, x_{k+1}) = arccos|a_k| in [0, pi/2], and phi_k = pi/2 - theta_k in [0, pi/2].

Since cos theta_k = |a_k|, we get sin phi_k = sin(pi/2 - theta_k) = cos theta_k = |a_k|, so
  (N1) a_k^2 = sin^2 phi_k.
Put psi_0 = 0 and psi_k = phi_1 + ... + phi_k for 1 <= k <= m-1. Since all phi_k >= 0,
  (N2) 0 = psi_0 <= psi_1 <= ... <= psi_{m-1}.
We have sum_{k=1}^{m-1} theta_k = (m-1) pi/2 - psi_{m-1}. So the target is equivalent to
  (T) psi_{m-1} >= pi/2.

For 0 <= k <= m let V_k = span(x_1, ..., x_k), a subspace of R^(m-1) (V_0 = {0}).
For 1 <= k <= m let h_k = x_k - P_{k-1} x_k, where P_j is the orthogonal projection of R^(m-1) onto V_j (P_0 = 0),
and let t_k = |h_k| >= 0. So h_1 = x_1 and t_1 = 1.

## Step 1 (the Gram–Schmidt recursion)

Claim: let 1 <= k <= m-1 with t_k > 0. Then t_{k+1}^2 = 1 - a_k^2 / t_k^2.

Proof.
(1a) V_k = V_{k-1} + span(h_k), and h_k is orthogonal to V_{k-1}. Indeed, h_k = x_k - P_{k-1}x_k is orthogonal to V_{k-1} by the definition of orthogonal projection, and x_k = P_{k-1}x_k + h_k with P_{k-1}x_k in V_{k-1}, so V_{k-1} + span(x_k) = V_{k-1} + span(h_k).
(1b) Hence, since h_k != 0 and h_k is orthogonal to V_{k-1}, for every vector v:
     P_k v = P_{k-1} v + (<v, h_k> / t_k^2) h_k.
     (The right side lies in V_k, and v minus it is orthogonal to V_{k-1} (because v - P_{k-1}v is, and h_k is) and to h_k (because <v - P_{k-1}v, h_k> = <v, h_k> as P_{k-1}v is in V_{k-1}, which is orthogonal to h_k). So it is the orthogonal projection.)
(1c) Take v = x_{k+1}. For 1 <= j <= k-1 we have |(k+1) - j| >= 2, so <x_{k+1}, x_j> = 0 by hypothesis. Hence x_{k+1} is orthogonal to V_{k-1}, so P_{k-1} x_{k+1} = 0. Also
     <x_{k+1}, h_k> = <x_{k+1}, x_k> - <x_{k+1}, P_{k-1}x_k> = a_k - 0 = a_k,
     because P_{k-1}x_k is in V_{k-1}, which is orthogonal to x_{k+1}.
     So P_k x_{k+1} = (a_k / t_k^2) h_k, with |P_k x_{k+1}|^2 = a_k^2 / t_k^2.
(1d) x_{k+1} = P_k x_{k+1} + h_{k+1} with the two summands orthogonal. By Pythagoras,
     1 = |x_{k+1}|^2 = a_k^2 / t_k^2 + t_{k+1}^2.   QED.

## Step 2 (dimension forces some t_k = 0)

Claim: there is k in {1, ..., m} with t_k = 0.
Proof. Suppose t_k > 0 for all 1 <= k <= m. Then h_k != 0, so x_k is not in V_{k-1} (if x_k were in V_{k-1}, then P_{k-1}x_k = x_k and h_k = 0). So dim V_k = dim V_{k-1} + 1 for each k, and dim V_m = m. But V_m is a subspace of R^(m-1), so dim V_m <= m - 1. Contradiction. QED.

## Step 3 (trigonometric lemma)

Lemma. Let psi >= 0 and phi >= 0 with psi + phi < pi/2. Then sin phi <= cos psi * sin(psi + phi).
Proof. By the subtraction formula, sin phi = sin((psi + phi) - psi) = sin(psi+phi) cos psi - cos(psi+phi) sin psi. Hence
  cos psi * sin(psi+phi) - sin phi = cos(psi+phi) sin psi.
Here psi + phi is in [0, pi/2), so cos(psi+phi) > 0; and psi is in [0, pi/2), so sin psi >= 0. Therefore the difference is >= 0. QED.

## Step 4 (lower bound on t_k if (T) fails)

Assume, for contradiction, (H) psi_{m-1} < pi/2. By (N2), 0 <= psi_j < pi/2, hence cos psi_j > 0, for all 0 <= j <= m-1.

Claim Q(k), for 1 <= k <= m: t_k >= cos psi_{k-1} (> 0).
Base k = 1: t_1 = |x_1| = 1 = cos 0 = cos psi_0.
Step: let 1 <= k <= m-1 and assume Q(k). Then t_k >= cos psi_{k-1} > 0, so Step 1 applies:
  t_{k+1}^2 = 1 - a_k^2 / t_k^2 = 1 - sin^2 phi_k / t_k^2        (by (N1))
            >= 1 - sin^2 phi_k / cos^2 psi_{k-1}                   (since 0 < cos psi_{k-1} <= t_k and sin^2 phi_k >= 0).
Apply the Lemma (Step 3) with psi = psi_{k-1} >= 0 and phi = phi_k >= 0; their sum is psi_k < pi/2 by (H), (N2). It gives
  0 <= sin phi_k <= cos psi_{k-1} sin psi_k, so sin^2 phi_k / cos^2 psi_{k-1} <= sin^2 psi_k (squaring two nonnegative numbers, then dividing by cos^2 psi_{k-1} > 0).
Therefore t_{k+1}^2 >= 1 - sin^2 psi_k = cos^2 psi_k, and since t_{k+1} >= 0 and cos psi_k > 0, t_{k+1} >= cos psi_k. This is Q(k+1).

By induction Q(k) holds for all 1 <= k <= m, so t_k > 0 for all k, contradicting Step 2.

## Step 5 (conclusion)

(H) is false, so psi_{m-1} >= pi/2, i.e. (T). Therefore
  sum_{k=1}^{m-1} theta(x_k, x_{k+1}) = (m-1) pi/2 - psi_{m-1} <= (m-2) pi/2.   QED.

## Edge cases (G3)

- m = 2: hypothesis on |i-j| >= 2 is vacuous; the proof uses only Q(1), Q(2): (H) would give t_2^2 = 1 - a_1^2 >= cos^2 phi_1 > 0, contradicting Step 2 (two vectors in R^1). Directly: x_2 = ±x_1, theta = 0 = (2-2) pi/2.
- a_k = 0 (phi_k = 0) or |a_k| = 1 (phi_k = pi/2) are allowed; the only divisions are by t_k and by cos psi_{k-1}, both shown > 0 under (H) at the point of use. Step 1 is only invoked with t_k > 0.
- Signs of the a_k never matter (only a_k^2 enters).
- Repeated / antiparallel vectors are allowed; nothing assumes linear independence (Step 2 derives dependence).

## Sharpness (not required)

m = 3, x_1 = e_1, x_2 = (cos t, sin t), x_3 = e_2 in R^2, t in [0, pi/2]: theta sum = t + (pi/2 - t) = pi/2 = (m-2) pi/2. For every m >= 2: x_k = e_k (1 <= k <= m-1), x_m = e_{m-1} satisfies the hypotheses (<e_i,e_j> = 0 for i != j) and gives m-2 right angles plus theta(e_{m-1},e_{m-1}) = 0, total (m-2) pi/2. So the bound is attained for every m.

## What is established

The full statement of cell A-C2, all m >= 2, no extra hypotheses. Tools: Cauchy–Schwarz, orthogonal projection / Pythagoras, dimension counting, the sine subtraction formula. No computation is used; out/code/sanity_gs.py is a floating-point sanity check only and is not part of the proof.

KNOWN GAPS: none found in the proof. Literature provenance of this exact lemma not located (all fetches blocked); see sources.md.
