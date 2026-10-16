```
VERDICT: ACCEPT
STATEMENT MATCH: yes
FIRST PROBLEM: none
CHECKLIST:
  G1 PASS — proves S <= (pi/2) floor(N^2/4) for every N >= 0 and all lines through the origin of R^2, repetitions allowed; no extra hypotheses, same inequality direction and non-strictness.
  G2 PASS — no "clearly/obviously/routine/similarly/by symmetry" in any step (the only occurrence is a meta-remark about the published source); every step is written out (see per-step notes).
  G3 PASS — N = 0, 1 are induction bases (empty sums) in Proof B and trivial in Proof A; N = 2 goes through B2 with empty rest; coincident lines are handled explicitly (B4 treats C = #coincidences; A3 counts indices).
  G4 PASS — the invariant in B5 (F_N constant along the rotation a_N -> a_N + e, 0 <= e <= e*) is proved from C = 0 and P = Q; strictness is needed only for d > 0 in B4, which holds.
  G5 PASS — the rotation in B5 is defined for every N >= 2 (set nonempty, 0 < e* < pi/2); the sharpness configuration in the Remark works for every N.
  G6 PASS — induction uses only M(N-2) and B5 for N; FVZ 2016 and Bilyk-Matzke 2018 are cited as technique sources only, every step is proved in the text.
  G7 PASS — no step rests on computation; the included sanity script is exact (Fraction), non-load-bearing, labelled as proving nothing beyond its grid, reruns in 0.37 s.
  G8 PASS — citations separated from new work, with journal/volume/year/theorem (Arch. Math. 106 (2016) Thm 2.1) and arXiv id/section (1801.07837 Sec. 4.3).
  G9 PASS — status "cell A-C1 solved" stated; "not claimed: characterisation of all maximisers" stated.
  S1 PASS — exact statement matches, theta = arccos|<x,x'>| in [0, pi/2] via rho = dist(., pi Z) (Step 0.4).
  S2 PASS — Remark proves balanced split gives exactly (pi/2) floor(N^2/4); bound not smaller there; both proofs are tight there (checked exactly, E1-E3).
  S3 PASS — all N >= 0, both parities (Proof B: bases 0 and 1, step 2; Proof A parity-free via Step 0.5), N = 1, N = 2, coincident lines, sign-independence (Step 0.2).
  S4 PASS — line angles in [0, pi/2] used throughout; lines not assumed distinct; no parity restriction; no floating point in the proof; no citation used as proof.
  S5 PASS — bound equals binom(N,2) - M(N,2) (exact check N = 0..300); N = 2, 3, 4 values pi/2, pi, 2pi match the Setting's example.
  S6 PASS — balanced split gives pi/2, pi, 2pi, 3pi for N = 2..5 (exact check E5); proof's bound equals these values.
EQUALITY CASES: balanced split floor(N/2) x {0}, ceil(N/2) x {pi/2} attains the bound exactly for N = 0..40; Proof A integrand equals floor(N^2/4) on every piece there; Proof B's removal step maps it to the balanced split of N-2 with equality (N = 2..40). Regular odd-N configurations {k pi/N} also attain it (N odd 3..41), consistent with the proof's "not claimed" remark.
CROSS-CELL: consistent; C1 = C6 at d = 2 (binom(N,2) - M(N,2) = floor(N^2/4)); no verified cells listed yet.
CEX SEARCH: out/cex/cex.py (P1-P6) and out/cex/eq_cases.py: exact identities of Steps 0.3, 0.5, B1, B2, A2, A3/A4 on random rationals; exact grid maxima (D = 12, N <= 10; D = 7, N <= 12; D = 10, N <= 10; D = 24, N <= 6) never exceed the bound; every grid maximiser without a perpendicular pair satisfies B4 (C = 0, P = Q) and B5 (rotation keeps the max); float hill-climbing N <= 16 finds nothing above the bound (max excess 1.4e-14, rounding). No counterexample.
OTHER ISSUES: (non-blocking) B4 uses evenness of rho (0.3(b)) silently for pairs (i, n) with i < n; Remark's "for odd N there are others" fails for N = 1 (non-load-bearing, in the "not claimed" section); sources.md referenced but not in the inbox (the in-text references are precise enough).
RAN: subject sanity_exact.py defaults (D=48, NMAX=7, D2=8), COMPLETED, real 0.37 s (log out/cex/log_subject.txt)
RAN: cex.py P1-P4 (N 0..120 / 20000 rationals / 3000 configs N 2..9 / 1500 pairs + 1500 configs N 0..10), COMPLETED, real 0.99 s (log_P1-4.txt)
RAN: cex.py P5 (grids D=12 N<=10, D=7 N<=12, D=10 N<=10, D=24 N<=6), COMPLETED, real 1.27 s (log_P5.txt)
RAN: cex.py P6 float hill-climb N=2..16, 60 restarts each, COMPLETED, real 4.16 s (log_P6.txt)
RAN: cex.py all parts P1-P6 end to end, COMPLETED, real 6.12 s (log_all.txt)
RAN: eq_cases.py E1-E5 (N 0..40, odd N 3..41, N 0..300), COMPLETED, real 0.26 s (log_eq.txt)
```

# Referee report A-C1-007 (VERIFY), subject A-C1-003

Target (from brief/target.md, statement.md Cell 1): for every N and all lines l_1..l_N through the origin of R^2, repetitions
allowed, S = sum_{i<j} theta(l_i, l_j) <= (pi/2) floor(N^2/4), theta = arccos|<x,x'>| in [0, pi/2]. Assumptions: none.
Rules: exact/interval computation only, citing a published proof of the statement does not count.

The subject's first line states exactly this for all N >= 0 (N = 0 is a harmless extension). Status declared: solved.

## 1. Checklist (full)

See block above; every item G1-G9, S1-S6 is PASS with its reason.

## 2. Line-by-line re-derivation (per-step reasons)

**0.1** Every unit vector is (cos b, sin b), b in [0, 2 pi) (polar coordinates); if b >= pi, -x = u(b - pi) spans the same line. Holds.

**0.2** y in R x with |y| = |x| = 1 forces y = +-x, so |<x,x'>| is independent of the choice of spanning vectors; <u(a),u(b)> = cos(a-b) by the subtraction formula. Holds.

**0.3** (a) k0 = floor(z/pi + 1/2) gives z/pi - k0 in [-1/2, 1/2); for k != k0 the reverse triangle inequality gives |z - k pi| >= pi - pi/2 >= |z - k0 pi|, so the min over the infinite set is attained and is <= pi/2. (b) reindexing k. (c) for k != 0, |z - k pi| >= pi - |z| >= pi/2 >= |z|. (d) triangle inequality then min over k. All hold.

**0.4** w = z - k0 pi, cos z = (-1)^{k0} cos w, |cos w| = cos|w| since |w| <= pi/2; arccos inverts cos on [0, pi]. Holds.

**0.5** 4k(N-k) = N^2 - (N-2k)^2 (verified algebraically); even N gives k(N-k) <= N^2/4 in Z; odd N gives (N-2k)^2 >= 1 so k(N-k) <= m^2 + m = floor(N^2/4). Valid for all integers k. Holds (checked exactly N <= 120, |k| <= 60).

**0.6** By 0.1 every tuple of lines is (R u(a_i)); by 0.4 S = F_N(a). Only the direction "every S-value is an F-value" is needed, and it is proved. Holds.

**B1** theta(l,l') = pi/2 gives <x,x'> = 0, so {x, x'} is an orthonormal basis and <x,y>^2 + <x',y>^2 = 1; |<x',y>| = sin t1 = cos(pi/2 - t1) with pi/2 - t1 in [0, pi/2], so arccos gives pi/2 - t1. Holds for every line m, including m = l or l'.

**B2** Partition of pairs into {p,q}, the N-2 groups {p,m},{q,m} (each summing to pi/2 by B1), and pairs inside the rest. Holds (exact check P3).

**B3** F_N is continuous (composition of 1-Lipschitz rho with linear maps, finite sum), pi-periodic in each coordinate (0.3(b)), so sup over R^N = max over the compact cube [0, pi]^N, which is attained. Holds; M(0) = M(1) = 0.

**B4** z_i is the representative of a_n - a_i in (-pi/2, pi/2] (k = ceil(y - 1/2) gives y - k in (-1/2, 1/2], verified); rho(a_n - a_i) = |z_i| by 0.3(b),(c), and != pi/2 gives |z_i| < pi/2. eta > 0 since the set is finite, nonempty (N >= 2), and consists of positive numbers. For |e| < eta, |z_i + e| < pi/2 and signs of nonzero z_i are kept, so f(e) = f(0) + (P-Q)e + C|e|. Moving a_n changes only the pairs containing n; for i < n the pair term is rho(a_i - a_n - e) = rho(a_n + e - a_i) by evenness (0.3(b)). This use is silent but the lemma is proved. Maximality at e = +-d, 0 < d < eta, gives (P-Q)d + Cd <= 0 and -(P-Q)d + Cd <= 0, so C = 0 and then P = Q. Holds.

**B5** If the maximiser a has no perpendicular pair, B4 at n = N gives C = 0, P = Q, all z_i in (-pi/2, 0) or (0, pi/2). e* is the min of a finite nonempty set in (0, pi/2). On [0, e*], z_i + e stays in (0, pi/2] (z_i > 0) or (-pi/2, 0] (z_i < 0), so f(e) = f(0) + (P-Q)e = f(0), and a' is again a maximiser. The minimising index gives z_i + e* = 0 or pi/2, i.e. rho(a'_N - a'_i) = 0 or pi/2. In the 0 case, B4(i) applied to the maximiser a' rules out "no perpendicular pair". Holds. (Side remark: for even N, P + Q = N - 1 is odd, so P = Q is impossible and every maximiser already has a perpendicular pair; not needed.)

**B6** Strong induction with bases N = 0, 1 and step N-2 -> N, which covers all N >= 0 and both parities. M(N) = F_N(a') = (N-1) pi/2 + F_{N-2}(rest) by B2 applied to the lines R u(a'_i). This is <= (N-1) pi/2 + M(N-2) <= (pi/2)(N - 1 + floor((N-2)^2/4)), and (N-2)^2/4 + N - 1 = N^2/4 with floor(x + n) = floor(x) + n for integer n. Holds.

**B7** S = F_N(a) <= M(N) <= bound. Nothing assumes distinct lines. Holds.

**A1** chi(u) = 1 iff u mod pi is in [0, pi/2); it is pi-periodic and a step function on bounded intervals, so its Riemann integrals exist. The shift invariance of a period integral is proved by splitting at (m+1) pi. Holds.

**A2** Affine substitution s = a - t (valid for step functions), then A1, give g(delta). g is pi-periodic and even: g(-delta) = g(delta) via s = r + delta and A1. Reducing to d = |delta'| in [0, pi/2]: |p - q| = p + q - 2pq on {0,1}; both single integrals are pi/2; the product is 1 exactly on [0, pi/2 - d) because s + d < pi for s < pi/2. So g(d) = 2d, and rho(a - b) = rho(delta) = |delta'|. Holds; it includes the endpoint d = pi/2 (I = 0, g = pi). Exact check P4: 1500 random rational pairs.

**A3** A pair is cut iff exactly one index is in K(t); there are k(N-k) such pairs, and repeated angles are counted by index. Holds.

**A4** Linearity of the integral over a finite sum, A2, A3, pointwise bound 0.5, monotonicity: S = (1/2) int_0^pi k(t)(N-k(t)) dt <= (pi/2) floor(N^2/4). Holds. The identity S = (1/2) int k(N-k) was checked exactly for 1500 random rational configurations, N <= 10.

**Remark / What is established.** Sharpness is proved for every N (floor(N/2) ceil(N/2) = floor(N^2/4) for both parities). "For odd N there are others" is true for odd N >= 3 (regular N-configuration verified exactly for N = 3..41) but not for N = 1. It is non-load-bearing and sits in the "not claimed" section.

Unjustified, circular or false load-bearing steps: none. Two independent complete proofs, each sufficient on its own.

## 3. Numerical sanity

- Subject code `inbox/subject/code/sanity_exact.py` rerun with defaults: ALL OK, real 0.37 s. It uses exact Fractions and is non-load-bearing, as it says.
- There is no floating point inside either proof. My only float run (P6) is exploratory. Its excesses of order 1e-14 are rounding at exact maximisers, not violations.

## 4. Equality cases (Part S2)

- Balanced split: S equals the bound exactly for N = 0..40 (E1).
- Proof A is tight there: k(t)(N-k(t)) = floor(N^2/4) on every piece (E2).
- Proof B is tight there: B2 removal leaves the balanced split of N-2 at its bound (E3).
- Other equality configurations exist for odd N (regular configurations; grid maximisers without perpendicular pairs in P5). This is consistent with S2's "unknown" and with the proof's "not claimed".

## 5. Cross-cell consistency (S5)

- binom(N,2) - M(N,2) = floor(N^2/4) for N = 0..300 (exact).
- N = 2, 3, 4 give pi/2, pi, 2pi, matching the Setting's example.
- No verified cells are listed yet.

## 6. Counterexample search (out/cex/)

- `cex.py` P1-P4: the exact identities and inequalities of Steps 0.3, 0.5, B1, B2, A2, A3/A4 on random rationals (denominators up to 1000, negative and large values). 0 failures.
- `cex.py` P5: exact maximum over all multisets on grids {k pi/D}:
  - grids covered: D = 12 (N <= 10), D = 7 (N <= 12; odd grid, so no perpendicular pairs), D = 10 (N <= 10), D = 24 (N <= 6);
  - never above the bound;
  - every grid configuration attaining the bound without a perpendicular pair satisfies B4 (C = 0, P = Q at every line) and B5 (the rotation by e* keeps the value);
  - no even-N maximiser lacks a perpendicular pair.
- `cex.py` P6: float coordinate hill-climbing for N = 2..16 with 60 restarts each. The best values sit at the bound (max excess 1.4e-14).
- `eq_cases.py` E1-E5: equality and cross-cell arithmetic (see §4-5).

Result: no counterexample to the statement or to any intermediate claim.

## 7. Verdict

**ACCEPT.** Statement match is exact and every checklist item is PASS. Every numbered step of both Proof B and Proof A is justified as shown in §2. The non-blocking presentational notes are in OTHER ISSUES.
