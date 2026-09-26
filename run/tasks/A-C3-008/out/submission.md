# Submission: Cell 3, "d + 1 Lines in R^d" (3 points)

# 1. Statement (verbatim from the cell)

> The first case in every dimension: one line more than the dimension, $N = d + 1$, where the conjectured optimum repeats exactly one of the $d$ coordinate axes.
>
> Let $d \geq 1$. Prove that any $d + 1$ lines in $\mathbb{R}^d$ satisfy
> $$S \leq \left( \binom{d+1}{2} - 1 \right) \frac{\pi}{2}.$$

Definitions, verbatim from the problem description: a *line* is a line through the origin of $\mathbb{R}^d$; the angle between lines $\ell, \ell'$ spanned by unit vectors $x, x'$ is the acute angle $\theta(\ell, \ell') = \arccos |\langle x, x' \rangle| \in [0, \pi/2]$; for lines $\ell_1, \ldots, \ell_N$ (repetitions allowed), $S(\ell_1, \ldots, \ell_N) = \sum_{1 \leq i < j \leq N} \theta(\ell_i, \ell_j)$.

Exact target: for every integer $d \geq 1$ and all lines $\ell_1, \ldots, \ell_{d+1}$ through the origin of $\mathbb{R}^d$ (repetitions allowed), $S(\ell_1, \ldots, \ell_{d+1}) \leq (\binom{d+1}{2} - 1)\,\pi/2$.

# 2. Status

- **Cell status: SOLVED**
- **Claim status: PROVED**

We consider Cell 3 **solved**: the inequality is proved for every $d \geq 1$ by a complete written proof (Section 4). No step rests on a computation (proof.md, line 6).

Claims in the accepted artefact `submission/claims.md` (all PROVED; locations are in `submission/proof.md`):

| claim | status | where |
|---|---|---|
| R1: $\theta_{ij} = \pi/2 - \arcsin\lvert g_{ij}\rvert$; $S = \binom{n}{2}\pi/2 - T$; target iff $T \geq \pi/2$ | PROVED | Step 1 |
| R2 (Lemma L): $a_j \geq 0$, $D = \sum a_j \leq \pi/2 \Rightarrow \sum \sin(a_j)\cos(D - a_j) \leq \sin D$ | PROVED | Step 2 |
| R3 (Key Lemma): $T < \pi/2$, $p_i = \sin(D_i + \pi/2 - T) \Rightarrow p_i > 0$ and $\sum_{j \neq i} \sin(\alpha_{ij}) p_j < p_i$ | PROVED | Step 3 |
| R4 (Lemma W): unit diagonal + positive weights with strict weighted row dominance $\Rightarrow$ trivial kernel | PROVED | Step 4 |
| R5: $d+1$ unit vectors in $\mathbb{R}^d$ give $c \neq 0$ with $Gc = 0$ | PROVED | Step 5 |
| R6 (TARGET): for all $d \geq 1$, any $d+1$ lines in $\mathbb{R}^d$ have $S \leq (\binom{d+1}{2} - 1)\pi/2$ | PROVED | Step 6 |
| R7: bound attained for every $d \geq 1$ (remark) | PROVED | Step 7 |

`claims.md` also lists one row with status "evidence" (floating-point sampling, `code/evidence.py`), marked there as "evidence only, not a proof step". See Limitations.

# 3. Cited vs. ours

**Cited.** The proof cites no published result, and in particular it does not cite a published result for the statement being proved. The only outside facts it uses are the standard tools listed in proof.md, lines 3-6: the Cauchy-Schwarz inequality; the angle-addition formulas for sin and cos; monotonicity of sin on $[0, \pi/2]$; the identity $\arcsin t + \arccos t = \pi/2$ on $[0,1]$; and the fact that $d+1$ vectors in $\mathbb{R}^d$ are linearly dependent.

**Ours.** The team wrote the whole argument, Steps 0-7 of `submission/proof.md` (claims R1-R7 above). It was produced in task A-C3-002 (header of `claims.md`) without literature access ("Regime: BLIND", proof.md, line 3). None of the artefacts shipped with this submission records a literature search, so we make no claim either way about whether these arguments already appear in the literature.

# 4. Proof

Below is the accepted artefact `submission/proof.md`, reproduced verbatim (sha256 `01ac84d122b60409e010d3272b3cd2b781c0a0db48f34e41be451eca47753ef6`). The scribe changed nothing. Some labels are internal to the team's records: "Regime: BLIND"; "gated assumptions A-C1 and A-C2", which the proof states it does not use; and "rung R1"-"rung R7", which refer to the rows of `claims.md`. The script mentioned in the final paragraph is not part of this submission (see Limitations).

---

For every integer d >= 1 and all lines l_1, ..., l_{d+1} through the origin of R^d (repetitions allowed), S(l_1, ..., l_{d+1}) = sum_{i<j} theta(l_i, l_j) <= (C(d+1,2) - 1) * pi/2, where theta(l, l') = arccos|<x, x'>| for spanning unit vectors x, x'.

Regime: BLIND. Tools used, all standard: the Cauchy–Schwarz inequality; the angle-addition
formulas for sin and cos; monotonicity of sin on [0, pi/2]; the identity arcsin t + arccos t = pi/2
on [0,1]; the fact that d+1 vectors in R^d are linearly dependent. The gated assumptions A-C1 and
A-C2 are NOT used. No step rests on a computation.

Reading of the statement: none needed; the statement is used verbatim. "Repetitions allowed"
means some l_i may coincide and the lines may lie in a proper subspace; nothing below assumes
distinctness or that the lines span R^d.

---

## Step 0. Set-up

Fix d >= 1 and put n = d+1 (so n >= 2). Let l_1, ..., l_n be lines through the origin of R^d and
choose unit vectors x_i spanning l_i. (Replacing x_i by -x_i does not change |<x_i, x_j>|, so
theta(l_i, l_j) does not depend on the choice.) Put g_ij = <x_i, x_j>. Then g_ii = 1 and, by
Cauchy–Schwarz, |g_ij| <= |x_i||x_j| = 1, so arccos|g_ij| and arcsin|g_ij| are defined. Write
theta_ij = theta(l_i, l_j) = arccos|g_ij| for i != j.

## Step 1. Reformulation (rung R1)

For i != j put alpha_ij = arcsin|g_ij|, so alpha_ij = alpha_ji in [0, pi/2] and
sin(alpha_ij) = |g_ij|.

Claim: theta_ij = pi/2 - alpha_ij. Proof: let t = |g_ij| in [0,1] and u = arcsin t in [0, pi/2].
Then pi/2 - u lies in [0, pi/2], a subset of [0, pi], and cos(pi/2 - u) = sin u = t. Since arccos
is the inverse of cos restricted to [0, pi], arccos t = pi/2 - u.

Put T = sum_{1<=i<j<=n} alpha_ij. Summing the claim over the C(n,2) pairs,
  S(l_1, ..., l_n) = C(n,2) pi/2 - T.
Hence, for n = d+1,
  S <= (C(d+1,2) - 1) pi/2   if and only if   T >= pi/2.            (1)
It remains to prove T >= pi/2.

## Step 2. Lemma L (rung R2)

Lemma L. Let k >= 0 and a_1, ..., a_k >= 0 with D = a_1 + ... + a_k <= pi/2. Then
  sum_{j=1}^k sin(a_j) cos(D - a_j) <= sin D.

Proof, by induction on k. Throughout, each a_j is one of the non-negative summands of D, so
0 <= a_j <= D <= pi/2; hence sin(a_j) >= 0 and cos(a_j) >= 0.

k = 0: the sum is empty, and D = 0, so both sides are 0.

Step k-1 -> k (k >= 1): put D' = D - a_1 = a_2 + ... + a_k. Then 0 <= D' <= D <= pi/2, and
the numbers a_2, ..., a_k satisfy the hypothesis with sum D', so by the induction hypothesis
  sum_{j=2}^k sin(a_j) cos(D' - a_j) <= sin D'.                          (2)
By the angle-addition formula, sin D = sin(a_1 + D') = sin(a_1) cos(D') + cos(a_1) sin(D').
Since 0 <= a_1 <= D <= pi/2 we have cos(a_1) >= 0, so multiplying (2) by cos(a_1), and writing cos(D') = cos(D - a_1), gives
  sin D >= sin(a_1) cos(D - a_1) + sum_{j=2}^k cos(a_1) sin(a_j) cos(D' - a_j).     (3)
For each j >= 2, a_j is one of the non-negative summands of D', so 0 <= D' - a_j <= D' <= pi/2
and sin(D' - a_j) >= 0. By the angle-addition formula,
  cos(D - a_j) = cos(a_1 + (D' - a_j)) = cos(a_1) cos(D' - a_j) - sin(a_1) sin(D' - a_j)
               <= cos(a_1) cos(D' - a_j),
because sin(a_1) >= 0 (as 0 <= a_1 <= pi/2) and sin(D' - a_j) >= 0. Multiplying by
sin(a_j) >= 0 (as 0 <= a_j <= pi/2) gives cos(a_1) sin(a_j) cos(D' - a_j) >= sin(a_j) cos(D - a_j).
Substituting in (3):
  sin D >= sin(a_1) cos(D - a_1) + sum_{j=2}^k sin(a_j) cos(D - a_j) = sum_{j=1}^k sin(a_j) cos(D - a_j).
(For k = 1 the sum over j >= 2 is empty and (3) reads sin D >= sin(a_1), true with equality
since D' = 0.) This completes the induction. QED

## Step 3. Key Lemma (rung R3)

Key Lemma. Let n >= 2 and let alpha_ij = alpha_ji >= 0 (1 <= i != j <= n) be real numbers with
T = sum_{i<j} alpha_ij < pi/2. Put s = pi/2 - T > 0, D_i = sum_{j != i} alpha_ij, and
p_i = sin(D_i + s). Then for every i: p_i > 0 and
  sum_{j != i} sin(alpha_ij) p_j < p_i.                                  (4)

Proof.
(a) Bounds. D_i is the sum of alpha over the pairs {i,j} containing i, a sub-sum of the
non-negative terms making up T, so 0 <= D_i <= T. Hence 0 < s <= D_i + s <= T + s = pi/2 and
p_i = sin(D_i + s) > 0. Also every alpha_ij lies in [0, T], a subset of [0, pi/2), so
sin(alpha_ij) >= 0.

(b) Fix i. Let T_i' be the sum of alpha_kl over the pairs {k,l} with i not in {k,l}. The pairs
split into those containing i and those not containing i, so T = D_i + T_i'. For j != i,
  D_j = alpha_ij + sum_{k not in {i,j}} alpha_jk,
and the pairs {j,k} with k not in {i,j} are among the pairs counted in T_i'; all terms being
non-negative, sum_{k not in {i,j}} alpha_jk <= T_i'. Therefore
  D_j + s <= alpha_ij + T_i' + pi/2 - D_i - T_i' = pi/2 - (D_i - alpha_ij).
Here D_i - alpha_ij >= 0 (a sum of non-negative terms) and D_i - alpha_ij <= D_i <= T < pi/2.
So both D_j + s and pi/2 - (D_i - alpha_ij) lie in [0, pi/2], where sin is non-decreasing; thus
  p_j = sin(D_j + s) <= sin(pi/2 - (D_i - alpha_ij)) = cos(D_i - alpha_ij).

(c) Multiplying by sin(alpha_ij) >= 0 and summing over j != i,
  sum_{j != i} sin(alpha_ij) p_j <= sum_{j != i} sin(alpha_ij) cos(D_i - alpha_ij) <= sin(D_i),
the last step by Lemma L (Step 2) applied to the k = n-1 numbers a_j = alpha_ij (j != i), which are
non-negative with sum D_i <= T < pi/2.

(d) Finally 0 <= D_i < D_i + s <= pi/2 (by (a) and s > 0), and sin is strictly increasing on
[0, pi/2], so sin(D_i) < sin(D_i + s) = p_i. With (c) this gives (4). QED

## Step 4. Weighted diagonal dominance (rung R4)

Lemma W. Let G be a real n x n matrix with G_ii = 1 for all i, and suppose there are p_1, ..., p_n > 0
with sum_{j != i} |G_ij| p_j < p_i for every i. If c in R^n satisfies G c = 0, then c = 0.

Proof. Suppose G c = 0 with c != 0. Let r = max_i |c_i| / p_i; then r > 0 because some c_i != 0
and all p_i > 0. Choose i with |c_i| = r p_i. Row i of G c = 0 reads c_i = - sum_{j != i} G_ij c_j,
so, using |c_j| <= r p_j for all j,
  r p_i = |c_i| <= sum_{j != i} |G_ij| |c_j| <= r sum_{j != i} |G_ij| p_j < r p_i,
where the strict inequality uses r > 0 and the hypothesis. This is a contradiction. QED

## Step 5. A kernel vector of the Gram matrix (rung R5)

Let G = (g_ij) be the n x n Gram matrix of x_1, ..., x_n from Step 0. Since n = d+1 vectors in the
d-dimensional space R^d are linearly dependent, there is c = (c_1, ..., c_n) != 0 with
sum_j c_j x_j = 0. Taking the inner product with x_i gives sum_j g_ij c_j = 0 for each i, that is,
G c = 0 with c != 0.

## Step 6. Conclusion (rung R6 = TARGET)

Suppose, for contradiction, that T < pi/2, where T is as in Step 1. The numbers alpha_ij from
Step 1 satisfy alpha_ij = alpha_ji >= 0, and n = d+1 >= 2, so the Key Lemma (Step 3) gives
p_1, ..., p_n > 0 with sum_{j != i} sin(alpha_ij) p_j < p_i for all i. By Step 1,
|g_ij| = sin(alpha_ij) for i != j, and g_ii = 1. So the Gram matrix G satisfies the hypotheses of
Lemma W (Step 4), whence G c = 0 forces c = 0. This contradicts Step 5. Therefore T >= pi/2, and by
the equivalence (1) of Step 1,
  S(l_1, ..., l_{d+1}) <= (C(d+1,2) - 1) pi/2.
Since d >= 1 and the lines were arbitrary, this proves the statement.

Edge and degenerate cases, checked against the argument:
- d = 1: n = 2, both lines equal R^1, g_12 = +-1, alpha_12 = pi/2 = T, and S = 0 = (C(2,2) - 1) pi/2.
  The general argument also covers it (Steps 1–6 only need n >= 2).
- Repeated lines: if l_i = l_j then |g_ij| = 1, alpha_ij = pi/2; this is allowed in Step 1
  (alpha_ij in [0, pi/2]). Step 3 is only invoked under T < pi/2, where no alpha_ij equals pi/2;
  this is consistent, since the conclusion is that T < pi/2 is impossible.
- Lines spanning a proper subspace: Step 5 uses only linear dependence of d+1 vectors in R^d,
  which holds regardless.
- No step divides by a quantity that could vanish: the only division is by p_i > 0 (Step 4),
  with positivity from Step 3(a).

## Step 7. Sharpness (remark, not needed for the target)

Equality holds for x_k = e_k (k = 1..d) and x_{d+1} = e_1: the only non-orthogonal pair is {1, d+1},
with alpha = pi/2, so T = pi/2 and S = (C(d+1,2) - 1) pi/2. For d = 2, three lines at mutual angle
pi/3 also give equality (alpha = pi/6 for each of the 3 pairs, T = pi/2). So the bound cannot be
improved for any d >= 1 (for d = 1 both sides are 0).

## What is established

The statement on the first line is proved in full, for every d >= 1, with no gaps known to me.
The gated claims A-C1 and A-C2 were not used. The floating-point script in out/code/ is evidence
only; no step rests on it.

---

# 5. How to verify

**The mathematics.** Read Section 4 (equivalently `submission/proof.md`). The proof is fully written out and no step rests on a computation (proof.md, line 6). So the hand-in rule on computer-assisted steps (code included, under 10 minutes, rigorous arithmetic) does not come into play.

**Integrity of the shipped files.** From the directory that contains this file, run:

```
cd submission && /usr/bin/time -p shasum -a 256 -c MANIFEST.sha256
```

Expected output:

```
proof.md: OK
claims.md: OK
```

Measured run (on a copy under `out/submission/`; macOS Darwin 24.3.0, shasum 6.02): output exactly as above, exit status 0, `real 0.01` seconds. Log: `verify/logs/manifest_check.txt`.

The scribe also checked with `cmp` that the three files in `submission/` (`proof.md`, `claims.md`, `MANIFEST.sha256`) are byte-identical to the accepted inbox copies. All three were reported identical, exit status 0, `real 0.00` seconds. Log: `verify/logs/cmp_inbox.txt`.

# 6. Limitations

- **Scope.** The result covers only the case $N = d+1$ (Cell 3), for every $d \geq 1$. Other cells are not addressed here. Step 7 (sharpness: equality for $x_k = e_k$, $k = 1..d$, with $x_{d+1} = e_1$, and for $d = 2$ three lines at mutual angle $\pi/3$) is a remark and is not needed for the target (proof.md, Step 7).
- **Evidence script not shipped.** `claims.md` (last row) refers to `code/evidence.py`, and proof.md (lines 145-146) refers to "the floating-point script in out/code/". That script is not among the accepted artefacts delivered for this submission, so it is not included and was not run. Both artefacts say it is evidence only and that no proof step rests on it (proof.md, lines 6 and 145-146; claims.md, last row).
- **Review.** The status PROVED comes from the team's acceptance of the artefact. Agent review is evidence, not proof, and the judges must check the written argument themselves. The scribe added no mathematics, changed no step, and found nothing in the text to flag. That is not a mathematical verification.
- **Literature.** No literature comparison appears in the shipped artefacts (see Section 3).
