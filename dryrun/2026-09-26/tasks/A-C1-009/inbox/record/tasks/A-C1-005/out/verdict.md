```
VERDICT: ACCEPT
STATEMENT MATCH: yes
FIRST PROBLEM: none
CHECKLIST:
  G1 PASS — proves S <= (pi/2) floor(N^2/4) for every integer N >= 0 and all lines through 0 in R^2, repetitions allowed; no extra hypotheses; theta taken as arccos|<x,x'>| exactly as defined.
  G2 PASS — every step is written out; no "clearly/similarly/by symmetry"; the only compressed spots (iterating 2pi-periodicity n or |k| times, Steps 6 and 10) are one-line inductions stated in words.
  G3 PASS — N = 0, 1 (empty sums), N = 2, both parities (Step 12 is parity-free), coincident lines (delta = 0), endpoints s = 0 and s = pi in Step 9, the point x = 2pi in Step 9 all handled.
  G4 N/A — no invariant or descent argument.
  G5 PASS — the sharpness construction (Step 14, remark only) works for all N, both parities.
  G6 PASS — no circularity; no published result cited; the proof is self-contained (Crofton-type averaging written out).
  G7 PASS — no step rests on computation; the included float script is explicitly non-load-bearing; reran it (2.22 s).
  G8 PASS — only textbook facts used, each named (cos addition, arccos on [0,pi], polar form, Riemann integral of step functions).
  G9 PASS — states "cell solved", what is established (all N >= 0) and what is not (d >= 3, full equality characterisation).
  S1 PASS — statement proved is exactly S1's.
  S2 PASS — balanced perpendicular split gives equality (Step 14; exact check N = 0..40); the chain in Step 13 is tight there (k(psi)(N-k(psi)) = floor(N^2/4) on every open piece), so the proved bound is not smaller than the target.
  S3 PASS — N = 1 empty sum, N = 2, both parities, repeated lines, lines vs vectors (sign-independence in Step 1, theta = dist(., piZ) in [0, pi/2] in Step 3).
  S4 PASS — no trap hit: line angle in [0,pi/2] used, distinctness not assumed, parity-free, no floating point in the proof, no citation.
  S5 PASS — binom(N,2) - M(N,2) = floor(N^2/4) checked N <= 2000; Setting example N = 2,3,4 gives pi/2, pi, 2pi = bound.
  S6 PASS — N = 2,3,4,5 give pi/2, pi, 2pi, 3pi at the balanced split, equal to the proof's bound (exact).
EQUALITY CASES: balanced split floor(N/2) x-axis + ceil(N/2) y-axis, N = 0..40, exact rationals: S = bound and Step 13's inequality is an equality a.e.; N = 3 at pi/3 spacing (remark's extra maximiser) also equal.
CROSS-CELL: consistent with C6 at d = 2 and the Setting's example (S5); no verified cells yet.
CEX SEARCH: out/cex/check_exact.py (exact rationals: Step 0/3/4 identities, identity (10.1) by exact breakpoint integration, counting identity, whole chain S = (1/4) int k(N-k) as an exact identity, exhaustive grid search over 863163 multisets) and out/cex/hill_interval.py (hill-climbing N = 2..12, 66 climbs, certified with 200-bit arb ball arithmetic from the definition). No violation; no false intermediate claim.
OTHER ISSUES: cosmetic only: Step 6 uses F(x + 2pi n) = F(x) for integer (possibly negative) n, an unstated one-line induction from 5(b); "Tools used" lists the cosine subtraction formula while Step 3 uses the addition formula (the same fact).
RAN: subject sanity_check.py (python3, stdlib, seed 12345; N = 1..12 random, N = 2..9 hill-climb, 200 identity samples) COMPLETED, real 2.22 s
RAN: out/cex/check_exact.py (python3, stdlib, exact Fractions; E1 20000 rationals, E2 5000 pairs, E3/E4 1500 configs N = 0..11, E5 N <= 400, E6 grids m in {2..10,12,24,60} with N up to 12/11/10/9/9/8/8/7/7/7/5/4, E7 N <= 2000, E8 N = 0..40) COMPLETED, real 22.53 s
RAN: out/cex/hill_interval.py (.venv python3, python-flint arb 200 bits; N = 2..12, 6 climbs each x 6000 steps) COMPLETED, real 1.86 s
```

# Full report: referee A-C1-005, subject A-C1-002, mode VERIFY

## 1. Checklist pass

Reasons are in the block above. Two checks were done word for word against the statement:
- **Range of N.** The cell writes N with no range. The proof covers every integer N >= 0, and for N = 0 and N = 1 both sides are 0.
- **Lines vs vectors, repetitions.** The statement allows repetitions and uses the line angle arccos|<x,x'>| in [0, pi/2].
  - Step 1 notes that the value does not depend on the sign of the spanning vectors.
  - Step 3 proves theta = dist(a_i - a_j, pi Z), which lies in [0, pi/2].
  - Nothing assumes the lines are distinct: a repeated line gives delta = 0.

The inequality is non-strict (<=), in the same direction as the target, with the same constant (pi/2) floor(N^2/4). Nothing depends on citing a published result.

## 2. Line-by-line re-derivation (the reason each step holds)

- **Step 0(a).** Write t = c k0 + r with k0 = floor(t/c) and r in [0, c).
  - For k <= k0 - 1: |t - ck| = c(k0 - k) + r >= c.
  - For k >= k0 + 2: |t - ck| = c(k - k0) - r > c.
  - The two remaining values are r and c - r, both <= c, and their minimum is <= c/2.

  So the minimum exists, is attained, and is <= c/2. Checked exactly against a brute-force minimum over 101 values of k (E1).
- **Step 0(b), (c), (d).** Each follows from a bijection of Z (k -> -k, k -> k - m), or from scaling every term by 2. All correct; checked exactly in E1.
- **Step 1.** Polar form of unit vectors. Only the spanning vectors ±x_i are possible, and |<.,.>| ignores the sign. Correct.
- **Step 2.** The cosine subtraction formula. Correct.
- **Step 3.** Take k attaining r = dist(t, pi Z) <= pi/2 (Step 0(a) with c = pi).
  - cos t = (-1)^k cos(t - k pi), from the addition formula with sin(k pi) = 0.
  - So |cos t| = cos r >= 0, and arccos(cos r) = r because r is in [0, pi].

  Correct. Float cross-check E1b: max difference 6.6e-12, which is the known sensitivity of arccos near 1, not an error.
- **Step 4.** By Step 0(d) with c = pi, dist(2t, 2pi Z) = 2 dist(t, pi Z). This gives (4.1). Correct; checked exactly in E1.
- **Step 5(a)–(c).**
  - (a) m0 = floor(x/2pi) identifies the interval of U that contains x. The converse direction is also proved.
  - (b) Shifting x by 2pi maps each interval of U to the next one.
  - (c) On a bounded interval g is the indicator of finitely many intervals, and the affine preimages under psi -> u - psi are still finitely many intervals.

  So every integrand is a step function and Riemann integrable. Correct.
- **Step 6.** Write a = 2pi n + b. Split the integral at 2pi(n+1) (additivity), translate each piece, and use periodicity. The pieces give int_b^{2pi} + int_0^b = int_0^{2pi}. Correct.
  - Periodicity is applied for an integer n that may be negative. This is an obvious induction from 5(b); cosmetic only.
- **Step 7.** v - psi = (u - psi) + s, so the integrand is F(u - psi). The substitution x = u - psi maps [0, 2pi] onto [u - 2pi, u] with orientation reversed, which is accounted for. Then Step 6 with a = u - 2pi gives D(s). Correct.
- **Step 8.**
  - (a) Holds pointwise by 5(b).
  - (b) Translate by y = x - s, then apply Step 6 with a = -s.

  Correct.
- **Step 9.** For 0 <= s <= pi and x in [0, 2pi), the only intervals of U involved are:
  - [0, pi) for g(x);
  - [0, pi) and [2pi, 3pi) for g(x + s), since x + s lies in [s, 2pi + s), a subset of [0, 3pi).

  Then:
  - The intersection B = [0, pi - s) ∪ [2pi - s, 2pi) uses -s <= 0 and 3pi - s >= 2pi.
  - The symmetric difference is [pi - s, pi) ∪ [2pi - s, 2pi). The two pieces are disjoint because 2pi - s >= pi, and each has length s.

  So D(s) = 2s, including s = 0 and s = pi. Verified by exact integration (E2: D endpoints and 5000 random pairs).
- **Step 10.** Take k with |s - 2pi k| = delta(s) = r in [0, pi] (Step 0(a)).
  - Periodicity (8a, iterated) gives D(s) = D(±r).
  - Evenness (8b) and Step 9 give D(r) = 2r.
  - Step 0(b) gives delta(v - u) = delta(u - v).
  - Combining with (7.1) gives (10.1).

  Correct. Verified exactly in E2.
- **Step 11.** |g - g'| is in {0, 1}, and it is 1 exactly when the pair is split by K(psi). The number of split pairs is k(N - k), by a stated bijection. Correct; checked exactly in E3.
- **Step 12.** 4k(N - k) = N^2 - (N - 2k)^2 <= N^2, and integrality then gives the floor. Correct.
  - Exact check E5: holds for all k <= N <= 400, with equality iff k = floor(N/2) or ceil(N/2).
- **Step 13.** The chain is:
  1. (4.1): theta = (1/2) delta.
  2. (10.1): delta(u_i - u_j) = (1/2) int |g - g|, so theta = (1/4) int.
  3. Linearity over the finite sum; each summand is a step function.
  4. (11.1) pointwise for every psi.
  5. Monotonicity against the constant floor(N^2/4) (Step 12).
  6. int_0^{2pi} 1 = 2pi.

  Every equality in the chain was checked as an exact identity, S = (1/4) int k(N - k), on 1500 random rational configurations (E4). Correct.
- **Step 14 (remark, not load-bearing).** floor(N/2) ceil(N/2) = floor(N^2/4) for both parities. Correct; checked exactly in E8.
  - The extra odd-N maximiser (N = 3 at mutual angle pi/3) is correct: S = pi = bound.

No step is unjustified, circular or false. I found no first problem.

## 3. Numerical sanity

- **Subject script.** Reran it with plain python3 (stdlib), seed 12345. Output: no bound violation, identity error 6.0e-4 within the Riemann-sum resolution 6.28e-4. Measured real 2.22 s; the author's README reports 3.62 s. The script is floating point and explicitly non-load-bearing, and no proof step depends on it.
  - Its hill-climb gaps of about -3e-11 for odd N are float noise at equality. For odd N the maximum is attained on an open set; for example, three points in doubled angle not contained in any open semicircle give S = pi. So these gaps are not violations.
- **Floating point.** None is used inside the proof.

## 4. Equality-case test

Tested the configuration in Part S (S2) with exact rationals for N = 0..40:
- S equals (pi/2) floor(N^2/4) exactly.
- On every open piece between breakpoints, k(psi)(N - k(psi)) = floor(N^2/4). So the only inequality in Step 13 is an equality at this configuration, and the argument is tight exactly where S2 requires.

Whether other configurations also attain equality is "unknown" per Part S. The proof's remark gives one for N = 3 (pi/3 spacing), which I confirmed exactly.

## 5. Cross-cell consistency

There are no verified cells yet. The S5 arithmetic checks out:
- binom(N,2) - M(N,2) = floor(N^2/4) for N = 0..2000.
- The Setting example at d = 2 gives pi/2, pi, 2pi for N = 2, 3, 4, which equals the bound.
- The S6 values pi/2, pi, 2pi, 3pi hold.

## 6. Own counterexample search (out/cex/)

- `out/cex/check_exact.py` (stdlib, exact `Fraction` arithmetic, angles in units of pi; log `out/cex/check_exact_log.txt`):
  - **E1.** Step 0(a)–(d) and the Step 3/4 identity: 20000 random rationals × 4 moduli.
  - **E2.** Identity (10.1) by exact breakpoint integration: 5000 random rational pairs, plus D at the endpoints.
  - **E3/E4.** Counting identity (11.1), and the whole chain S = (1/4) int k(N - k) as an exact identity: 1500 configurations, N = 0..11.
  - **E5.** Step 12, all 0 <= k <= N <= 400.
  - **E6.** Exhaustive grid search: all multisets of N directions in {0, pi/m, ..., (m-1)pi/m}, 863163 multisets, exact integer comparison with the bound. Grids and ranges of N:

    | m | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 12 | 24 | 60 |
    |---|---|---|---|---|---|---|---|---|---|---|---|---|
    | N up to | 12 | 11 | 10 | 9 | 9 | 8 | 8 | 7 | 7 | 7 | 5 | 4 |

    - No violation.
    - For even m the grid contains a perpendicular pair, and the grid maximum equals the bound exactly.
  - **E7.** S5/S6 arithmetic.
  - **E8.** Equality configurations.

  COMPLETED, real 22.53 s.
- `out/cex/hill_interval.py` (.venv python, python-flint arb, 200 bits; log `out/cex/hill_interval_log.txt`):
  - Float hill-climbing for N = 2..12: 6 random starts × 6000 steps each, 66 final configurations.
  - Each final configuration was re-evaluated rigorously from the definition, sum of arccos|cos(a_i - a_j)|, in ball arithmetic.
  - Results:
    - 36 configurations certified strictly below the bound.
    - 30 overlap the bound to within about 1e-55. These are all odd N, consistent with the open set of maximisers.
    - 0 certified above the bound.

  COMPLETED, real 1.86 s.

This search is evidence only. It supports, and does not replace, the written proof, which I checked step by step above.

## 7. Verdict

**ACCEPT.** The statement matches word for word, every Part G and Part S item is PASS or N/A, and every step has the reason it holds in §2. The only remarks are cosmetic: the unstated integer-n periodicity induction in Step 6, and the "subtraction" vs "addition" wording of the cosine formula. Neither needs a fix for correctness.
