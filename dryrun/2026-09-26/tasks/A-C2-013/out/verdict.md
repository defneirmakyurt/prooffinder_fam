CROSS VERDICT: CONFIRMED
BRANCH: ANALYSIS
STATEMENT MATCH: yes
TRANSLATION: A(x)=sum arcsin|c_i| is a potential function. Eliminating x_m (projecting onto x_m^perp, i.e. the Schur complement of the tridiagonal Gram matrix at its last pivot) replaces the pair (a_{m-2}, a_{m-1}) by the single angle a' = arcsin(sin a_{m-2}/cos a_{m-1}). The key analytic fact is that this move never raises the potential when a_{m-2}+a_{m-1} < pi/2: phi(alpha,beta) = sin(alpha+beta)cos(beta) - sin(alpha) = sin(beta)cos(alpha+beta) >= 0, and arcsin is monotone. The dimension enters through the base case R^1 (potential = pi/2) and through dim W = m-2.
RED FLAGS: none. The degenerate pivot cos a_{m-1} = 0 is split off in Step 3, so the proof never divides by zero.

## Translation in full (analysis lens)

Take an admissible chain. Its Gram matrix G is tridiagonal, with 1 on the diagonal and c_i off the diagonal. G is PSD with rank <= m-1, so det G = 0. The leading minors satisfy D_k = D_{k-1} - c_{k-1}^2 D_{k-2}.

The proof's Step 4 is one Schur-complement step at the last pivot. Projecting x_{m-1} onto x_m^perp and normalising changes only the last surviving coupling, from c_{m-2} to c_{m-2}/sqrt(1-c_{m-1}^2). The result is again a singular PSD tridiagonal Gram matrix of size m-1, which I checked exactly on 11200 instances (R-check).

In angle coordinates a_i = arcsin|c_i| the map is (a_{m-2}, a_{m-1}) -> a' = arcsin(sin a_{m-2}/cos a_{m-1}). The potential A = sum a_i is non-increasing under this map:
- either a_{m-2}+a_{m-1} >= pi/2, and then A >= pi/2 directly;
- or the tangent-type inequality sin(a)/cos(b) <= sin(a+b) holds, which is Step 5 (the identity was verified symbolically).

Iterating the map down to a 2-chain in R^1 gives potential pi/2. Hence A >= pi/2, which is the target. So the key step translates cleanly into potential-function / monotone-smoothing language. No Lagrange or second-order analysis is needed, and none is used.

Behaviour near degenerate configurations:
- cos a_{m-1} -> 0 is handled by Step 3, where A >= a_{m-1} = pi/2.
- a' is well defined because |<z_{m-2}, z_{m-1}>| <= 1 by Cauchy–Schwarz.
- Orthogonal consecutive vectors (a_i = 0) need no special case.
- Every m=3 chain is an equality case: x_1 is orthogonal to x_3 in R^2, so theta_12 + theta_23 = pi/2 identically. The search confirms this: its minimum certified slack is ~ -2e-58, i.e. a ball containing 0.

Perturbation at a maximiser: not needed. The argument is a global monotone reduction, not a critical-point analysis.

## Per-step re-derivation
- Step 1: arccos t = pi/2 - arcsin t on [0,1]. The proof justifies this through the ranges. The reformulation to (*) A >= pi/2 is exact. The isometry remark (W is isometric to R^(m-2)) is correct.
- Step 2: R^1 unit vectors are +-1, so |c_1| = 1 and A = pi/2. Correct.
- Step 3: |c_{m-1}| = 1 gives a_{m-1} = pi/2, and every a_i >= 0. Correct.
- Step 4: u = x_{m-1} - c x_m lies in W, with |u|^2 = 1 - c^2 > 0.
  - (4a) holds: |j - m| >= 2 for j <= m-2.
  - (4c) holds: for i <= m-3, <x_i,x_{m-1}> = 0 and <x_i,x_m> = 0.
  - (4d) holds: <x_{m-2},x_m> = 0.
  - The z-chain has m-1 vectors in a space of dimension m-2, so the induction hypothesis applies (it needs m-1 >= 2, i.e. m >= 3). For m = 3 the prefix sum is empty.
- Step 5: I verified the identity by expanding it by hand and with sympy (residual 0). The sign argument uses sin beta >= 0 and cos(alpha+beta) > 0. Monotonicity of arcsin and arcsin(sin s) = s on [0, pi/2] are used correctly.
- Step 6: the hypotheses of the lemma hold: beta < pi/2 by the Step 3 split, and sin alpha <= cos beta by Cauchy–Schwarz on z. Both cases are correct.
- Step 7: an algebraic rearrangement. Correct.

## Checklist
- G1 PASS: proves exactly the cell's bound for all m >= 2, vectors in R^(m-1), consecutive-pair sum, with theta = arccos|.|.
- G2 PASS: every step is written out, including the trig identity. No "clearly" or "by symmetry" gaps.
- G3 PASS: covers m = 2 (base), m = 3 (empty prefix), |c_{m-1}| = 1 (Step 3) and c_i = 0 (a_i = 0, no division).
- G4 PASS: the invariant (the reduced list is an (m-1)-chain in dimension m-2) is verified in (4a)-(4d); the claimed decrease of A is non-strict, which suffices.
- G5 PASS: the construction of y, z works for every m >= 3 because |c_{m-1}| < 1 in that branch.
- G6 PASS: induction on m is well founded and nothing is circular. No citation.
- G7 PASS: no computation is load-bearing. The included float script is labelled non-load-bearing; I reran it (min 3.08e-12 > 0, 0.77 s).
- G8 PASS: only standard facts are used (Cauchy–Schwarz, Gram–Schmidt, trig).
- G9 PASS: states "SOLVED" and "KNOWN GAPS: none"; sharpness is marked as not required.
- S1 PASS: matches word for word, including the dimension m-1, the consecutive sum and the |.| in theta.
- S2 PASS: at (e1,e1,e2,...,e_{m-1}), a_1 = pi/2 and all other a_i = 0, so A = pi/2 exactly. The chained inequalities are A >= a_1 + ... + a' >= pi/2 with a' = a_{m-2} (since c_{m-1} = 0 gives y = x_{m-1}), so they are all tight. At m = 2 the sum is 0 = the bound.
- S3 PASS: all listed cases are covered. Signs are irrelevant because only |c_i| enters.
- S4 PASS: (a) theta in [0, pi/2] via |.|; (b) consecutive pairs only; (c) the dimension is used in the base case R^1 and in dim W = m-2; (d) no distinctness is assumed; (e) no float claims are made; (f) no citation.
- S5 PASS: at m = 3 the bound pi/2 agrees with A-C1 at N = 3 (pi - pi/2). The proof actually gives equality for every m = 3 chain, which is consistent.
- S6 PASS: m = 2 gives 0 and m = 3 gives pi/2. The S2 tuple gives (m-2)pi/2. Random exact instances show no violation (see below).

## Counterexample search (out/cex/)
- `out/cex/search.py` (seed 7):
  - Generates exact rational admissible chains for m = 2..9 through the tridiagonal Gram parametrisation (last coupling forced so det = 0), with denominators {2,3,5,7,12,50,1000} and 200 instances each: 11200 instances in total.
  - Checks the target with rigorous arb balls (python-flint, 200 bits), the Step-4 reduction exactly, the Step-5 lemma on each instance, and the dimension trap.
  - Result: 0 certified violations, 0 reduction failures, 0 lemma failures. The minimum slack lower bound is -2e-58 (m = 3, identically equal). Log: `out/cex/log_search.txt`.
- `out/cex/lemma_and_opt.py`:
  - sympy check of the Step-5 identity: residual 0.
  - An exploratory float hill-climb (non-load-bearing) over Gram–Schmidt-built chains, m = 2..7. Its best values never certifiably exceed the bound: the m = 3 gap of -2.6e-12 is float rounding at an identical equality. Log: `out/cex/log_lemma_opt.txt`.

## RAN
- `out/cex/search.py 7`: m = 2..9, 11200 exact instances, COMPLETED, real 1.98 s.
- `out/cex/lemma_and_opt.py`: sympy identity plus float hill-climb for m = 2..7 (30 restarts x 400 iterations), COMPLETED, real 3.00 s.
- `inbox/subject/code/sanity_lemma.py`: 1e6 float samples, COMPLETED, real 0.77 s (output in `out/cex/log_subject_sanity.txt`).
