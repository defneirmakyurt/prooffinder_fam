VERDICT: ACCEPT
STATEMENT MATCH: yes
FIRST PROBLEM: none
CHECKLIST:
  G1 PASS — proves D_B(T_k) = k^2 - k for every k >= 1 (no exceptions; k=1 -> 0, k=2 -> 2), with the upper bound for every partition of T_k and an explicit witness for every k >= 1; no extra hypotheses.
  G2 PASS — every step is written out (0.1-0.3, A.0-A.4, B1-B9); no "clearly/similarly/by symmetry" steps carry weight. The only implicit bit is the one-line invariant p+m <= q-1 in B7(a), which is automatic from how I(m) is reached (see notes).
  G3 PASS — k=1 (A.0, B9), k=2 (A.1-A.4 general for k>=2; B9 by hand), k=3 (general k>=3 branch, B7 loop has 0 steps); d_B = 0 starts are in B9 "t <= k"; (1^n), (n) are covered by the general bound.
  G4 PASS — energy E is preserved without a slide and strictly drops with one (0.1(d): at least one cell moves down a diagonal); B7 gives a strict length drop q'-p' < q-p; x' <= x monotone as used in B9.
  G5 PASS — the witness orbit is tracked symbolically via S(a_t,b_t) and CRT for all k >= 2; A.2 (i)-(iii) are proved for general k >= 2 and (a,b).
  G6 PASS — no circularity. Uniqueness of the cyclic partition (0.3) is proved from 0.1/0.2 only; Griggs-Ho is cited as attribution, and every lemma used is re-derived.
  G7 PASS — no step of the proof depends on computation. The included scripts (stdlib, exact integers) are sanity checks only, and all reran well under 10 min.
  G8 PASS — Griggs-Ho 1998 (Thm 3.7, Prop 3.2, Lemmas 3.3-3.6), Igusa 1985 and Etienne 1991 are named as sources of the architecture only. Minor: sources.md, which holds the full bibliographic entries, is not in the subject.
  G9 PASS — the Conclusion states exactly what is established and that the computations prove nothing for all k.
  S1 PASS — F(k) = k^2 - k for all k >= 1; UPPER (Part B) for all lambda |- T_k; LOWER: explicit lambda^(k) = (k-1,k-1,k-2,...,2,1,1) (k>=2), (1) for k=1, with d_B = F(k) exactly (A.3-A.4).
  S2 PASS — own exact exhaustive enumeration for k = 1..11 (T_k <= 66): D_B(T_k) = k^2-k, the witness attains it, delta_k is the only cyclic partition, and no partition exceeds F(k).
  S3 PASS — every k >= 1, including k=1,2,3; cyclic start d=0; (1^n) and (n) covered by the general argument (k=3: d((6))=3, d((1^6))=4 <= 6); the witness orbit is tracked symbolically (A.3).
  S4 PASS — d_B is the cycle-entry time min{t : B^t = delta_k}, justified by 0.3. B counts s before subtraction, 1-parts included (0.1(b), B1). Sorted insertion is handled by 0.1(c)/(d). d_B(delta_k) = 0. The upper bound covers every partition. Uniqueness of the cyclic partition is proved in 0.3, not assumed from C1.
  S5 PASS — consistent with C1's statement (delta_k is the unique cyclic partition of T_k, proved in 0.3); C5 at k=2 is N/A (not gated). F(2) = 2 = D_B(3) exhaustively.
  S6 PASS — d_B((2,1,1,1,1)) = 3 (recomputed) <= F(3) = 6, and F(3) = 6 >= 3.
EQUALITY CASES: The witness lambda^(k) attains k^2-k: symbolically in the proof (A.3), by exhaustive search for k<=11, and by orbit simulation for k<=60. The maximisers for k<=4 match the proof's list: k=3 only (2,2,1,1); k=4 (3,3,2,1,1), (3,2,2,2,1), (3,2,2,1,1,1).
CROSS-CELL: consistent with C1's statement (unique cyclic delta_k); C5 N/A.
CEX SEARCH: out/cex/exhaustive.py, lemmas.py, diagrams.py found 0 violations of any claim; details below.
OTHER ISSUES: (1) The hand-in must be LaTeX, but proof.md is plain text; convert before submission. (2) Line 48 mentions "the B-C1 assumption"; drop it, since 0.3 proves it and ASSUMPTIONS is none. (3) B7(a) should state the invariant p+m <= q-1 explicitly. (4) Paths out/tmp/ and sources.md in the proof do not match the subject (the code is in subject/tmp/); fix the references.
RAN:
  out/cex/exhaustive.py 10 — all partitions of T_k, k=1..10 — COMPLETED, real 2.82 s
  out/cex/exhaustive.py 11 — all partitions of T_k, k=1..11 (2,323,520 at k=11) — COMPLETED, real 106.31 s
  out/cex/lemmas.py 22 — (*), B2/flip form, B4-B9 on all partitions of n<=22 — COMPLETED, real 1.81 s
  out/cex/lemmas.py 36 22 — B4-B9 on all partitions of n<=36 ((*)/B2 for n<=22) — COMPLETED, real 14.21 s
  out/cex/diagrams.py 30 8 40 — 0.1 for n<=30, 0.3 for T_k with k<=8, A.2 for k=2..40 — COMPLETED, real 4.55 s
  inbox/subject/tmp/witness.py 40 — k=1..40 — COMPLETED, real 1.73 s (0 failures)
  inbox/subject/tmp/witness.py 60 — k=1..60 — COMPLETED, real 17.85 s (0 failures)
  inbox/subject/tmp/dbt.py 8 — k=1..8 — COMPLETED, real 0.62 s (values 0,2,6,12,20,30,42,56)
  inbox/subject/tmp/gh_lemmas.py 30 80 — n<=30, c_1..c_80 — COMPLETED, real 3.16 s (0 violations; 4411 B5 cases)

(All runs: `/usr/bin/time -p python3 ...` with system python3, stdlib only, run from run/tasks/B-C2-012/. Logs are in out/cex/*_log.txt and times in out/cex/*_time.txt.)

---

# Full checklist

Given above in the verdict block. Each item has been checked against target.md verbatim: F(k) for EVERY k >= 1; UPPER for every lambda |- T_k; LOWER with an explicit lambda^(k) as a function of k; cyclicity facts proved in the submission; computation only as sanity. Hand-in format (LaTeX) is a presentation requirement still to be met (OTHER ISSUES 1). It does not affect the mathematics being gated.

# Per-step notes (why each step holds)

Conventions: the diagram has column j of height lambda_j, and diagonal w(i,j) = i+j-1.

**0.1 (shift on diagrams).**
- (a) (i-1)+(j+1)-1 = i+j-1, and (1,j) -> (j,1) stays on diagonal j. The position "column j of diag w" is (w+1-j, j), sent to (w-j, j+1) for j<w and (1,w) -> (w,1). So rot is a cyclic permutation of each diagonal, and hence a bijection of the quadrant.
- (b) The row-1 cells fill column 1 to height s, and column j minus its bottom cell becomes column j+1. These are exactly the parts of B.
- (c) Column heights s, lambda_1-1, ..., lambda_s-1 are weakly decreasing iff s >= lambda_1-1.
- (d) Row i of the sorted diagram has length r_i = #{columns with height >= i}. For i <= s, column 1 counts and the other columns >= i form the initial segment 2..m (their heights are decreasing), so row i is unchanged. For i > s, column 1 does not count, so row i is {2..r_i+1}, which shifts to {1..r_i}. (s+1,2) exists because lambda_1-1 >= s+1, so at least one cell moves.

**0.2.** The parts k-1..1 and 0 give back the parts k-1..1; the new part is s = k.

**0.3 (convergence and uniqueness).**
- Hole and cell. S != D_k with |S| = T_k forces both a cell on a diagonal > k and a hole on a diagonal <= k. So W0 >= k+1, w0 <= k, and w (the largest diagonal < W0 with a hole) exists. Diagonal w+1 is either W0 or full, so it carries a cell.
- Tracking without slides. With no slide, the diagram is rot^tau(S) by 0.1(c). The hole and the cell move cyclically by 0.1(a) with moduli w and w+1, which are coprime. CRT gives tau < w(w+1) with the hole at (1,w) and a cell at (w+1,1).
- A slide occurs. Then s <= w-1 (row 1 is an initial segment) and mu_1 >= w+1 > s+1, so 0.1(d) applies.
- Termination. E is a positive integer. It is preserved by the pure rotation 0.1(c) and drops by at least 1 under 0.1(d). So slides cannot happen infinitely often, and the orbit hits delta_k, which is fixed by 0.2.
- Uniqueness. A cyclic mu equals B^{mp}(mu) = delta_k for large m.
- Checks. Exhaustive for T_k with k<=8: a slide occurs within w(w+1) steps from every non-delta start. The energy rule holds on every checked step.

**A.0.** For k=1 the only partition is (1) = delta_1, and d=0.

**A.1.** The witness is weakly decreasing and positive, and its sum is (k-1)+(T_k-k)+1 = T_k. Its diagram is D_k minus (k,1) plus (1,k+1), checked column by column.

**A.2.**
- (i) Row 1 = s and column 1 = mu_1. The removed cell (k+1-a,a) is in row 1 iff a=k and in column 1 iff a=1. The added cell (k+2-b,b) is in row 1 iff b=k+1 and in column 1 iff b=1.
- (ii) s >= k-1 and mu_1 <= k+1, so a slide needs s=k-1 and mu_1=k+1, i.e. a=k and b=1 (for k>=2, a=k already excludes a=1). Otherwise 0.1(c) gives rot. rot fixes D_k setwise (it permutes each diagonal) and moves the hole and the extra cell one column cyclically.
- (iii) rot(S(k,1)) has the hole at (k,1) and the extra cell at (k,2). The cells in rows > s = k-1 are only (k,2), because (k,1) is the hole. By 0.1(d) that cell slides to (k,1), giving D_k.
- Checks: all admissible (a,b) for k=2..40 (21320 cases, exactly sum(k^2-k), since only b in {a, a+1} is inadmissible) show 0 violations.

**A.3.**
- Start and step. lambda^(k) = S(1,k+1), i.e. a_0=1 and b_0=k+1. Both indices advance by +1 cyclically.
- Induction. Up to t* the hypothesis of (ii) holds, and "S(a_t,b_t) is a diagram" holds because it equals diagram(B^t(lambda)).
- CRT. a_t = k iff t ≡ -1 (mod k), and b_t = 1 iff t ≡ 1 (mod k+1). t0 = k^2-k-1 satisfies both (mod k: -1; mod k+1: 1+1-1 = 1), and 0 <= t0 < k(k+1) for k >= 2, so t* = t0.
- Not delta before k^2-k. Each S(a_t,b_t) has a cell on diagonal k+1, so it is not D_k.

**A.4.** A cyclic mu = B^t(lambda) with t < k^2-k would equal B^{mp}(mu) = delta_k, which contradicts A.3. So d_B = k^2-k exactly. Only 0.2 is used, not uniqueness.

**B1.**
- Induction on t. Subtracting 1 and dropping non-positive entries commutes with keeping only the positive ones. The new pile is c_{t+1}, entered as c_{t+1} - 0.
- Formula (*). Count the entries >= t+1 in that list.
- Row entries. e_{i,i-1} = [c_{i-1} >= 1] = 1, since every partition has at least one part.
- Checks: (*) verified for every t < L on all partitions of n<=22.

**B2.** Row i+1 consists of the entries of row i, each weakly smaller (0/1 entries, monotone in i), plus the new entry e_{i+1,i} = 1. A flip of a c-column u at row i means e_{i,u}=1 and e_{i+1,u}=0, i.e. c_u = i-u. This gives c_{i+1} = c_i + 1 - L_i. Checked on n<=22.

**B3.**
- Choosing p. p = the largest index in [i,j) with c_p <= x-1. Then c_{p+1} >= x (by maximality, or because p+1 = j and c_j > x). Also c_{p+1} <= c_p + 1 <= x by B2. So c_p = x-1 and c_{p+1} = x. Since c_{p+1} = x < c_j, j >= p+2.
- Choosing q. q = the first index > p+1 with c_q != x, so q <= j. Then c_q >= x (every index in (p,j) has c >= x, and c_j > x) and c_q <= x+1 (B2), so c_q = x+1.

**B4.**
- c_u = k for u > t. B^u(lambda) = delta_k for u >= t, and delta_k has k parts.
- Bounds on c_t. c_t is a part of delta_k, so c_t <= k. B2 gives c_t >= k-1.
- c_t = k is impossible. It would make mu's k parts minus 1 equal {k-1..1, 0}, so mu = delta_k. That contradicts the minimality of t (via 0.3 and 0.2).

**B5.**
- The maximal zero i. The k entries e_{t,t-k..t-1} exist because t >= k+1, and they sum to <= k-1. Since e_{t,t-1} = 1, a maximal zero i lies in [t-k, t-2]. L_t = 0 gives e_{t+1,i+1} = 1, so c_{i+1} >= t-i. e_{t,i} = 0 gives c_i <= t-i-1. B2 then forces equality in both.
- Case i >= t-k+1. c_i <= k-2 < k-1 < c_{t+1} = k. B3 then gives (ii) with p >= t-k+1.
- Case i = t-k: subcases c_j <= k-2 and c_j >= k+1. B3 applies on [j,t+1] or on [t-k,j], and gives (ii) or (i) with the stated ranges.
- Case i = t-k: remaining subcase. All c_u <= k on [t-k+1,t-1], and exactly those k-1 columns are 1 in row t. So mu's parts are c_{t-1-v} - v <= k-v for v=0..k-2. Their sum is <= T_k - 1 < T_k, a contradiction.
- Checks: 21955 cases with t >= k+1 over T_k <= 36 show 0 violations.

**B6.**
- Setup. c_p = m-2 >= 1, so m >= 3. Column p ends at row p+m-2. Columns p+1..p+m-1 (each c = m-1) are 1 at row p+m. So exactly one more 1 at row p+m, in a column Z, which is a lambda-column or u0 <= p-1.
- Z a lambda-column. lambda_j >= p+m and lambda_j <= n.
- Z = u0 >= 2. L_{p+m-1} = 0, so rows p+m-1 and p+m agree. L_{p+m-2} = 1 with column p as the unique flip, so rows p+m-2 and p+m-1 agree off column p. This gives e_{p+m-2,u0-1} = 0 and e_{p+m,u0} = 1, hence c_{u0} >= c_{u0-1} + 2, contradicting B2.
- Z = u0 = 1. Then c_1 = s >= p+m-1 and s <= n.
- Checks: 5812 instances, 0 violations.

**B7.**
- Finding p'. p >= x+1, and the x entries e_{p,p-x..p-1} sum to <= x-1; also x >= 2 since c_p >= 1. With the maximal zero p' in [p-x,p-2], L_p = 0 gives the base relations, and B2 forces c_{p'} = y-1, c_{p'+1} = y with y = p-p' in [2,x].
- Step (a). Column p'+m (c = y) ends at row p+m. So p+m = q-1 would need L_{q-1} = 0, which is impossible. Hence L_{p+m} = 1 with the unique flip at p'+m, and the rows agree elsewhere.
- Step (b). e_{p+m+1,p'+m+1} = 1 gives c >= y, and B2 gives c <= y+1.
- Termination. Only finitely many I(m) are possible. That needs p+m <= q-1 whenever I(m) holds: true for m=1 since q >= p+3, and inherited because the step to I(m+1) is taken only when p+m <= q-2 (implicit in the text, see OTHER ISSUES 3).
- The bound q' <= p+1. Otherwise c_p = c_{p+1} = y, while x-1 != x.
- Checks: the constructive p', q' were recomputed on 199838 instances (n<=36), 0 violations.

**B8.** Suppose p > x. Then among e_{p,1..p-1} at most x-1 < p-1 are 1. The maximal zero i <= p-2 has e_{p,i+1} = 1. Two equality steps of B2 carry this to e_{p+2,i+1} = 1, so c_{i+1} >= p-i+1 while c_i <= p-i-1, contradicting B2. Checks: 151310 instances, 0 violations.

**B9.**
- Cases k=1,2 and t <= k. k=1,2 were checked by hand, correctly (partitions of 3: (3)->(2,1), (1,1,1)->(3)->(2,1)). For t <= k, k < k^2-k when k >= 3.
- (ii) with q-p = k. The ranges force p = t-k+1. B6 with m=k gives t <= T_k <= k^2-k for k >= 3.
- All other patterns. q-p <= k-1 and p >= t-k (checked for both (i) and (ii)). Each B7 step lowers the length by at least 1 and keeps it >= 2, so there are at most k-3 steps.
- Stopping. The loop ends with p_m <= x_m <= k, either directly or when the length is 2 (B8).
- Final bound. p_0 <= p_m + mk <= k^2-2k, so t <= k^2-k.
- Checks: the whole chain was re-executed on all 21955 cases (T_k <= 36), 0 violations.

# Numerical checks and counterexample search (all exact integer arithmetic, stdlib)

- out/cex/exhaustive.py computes the transient length from the functional graph, detecting cycles by path revisits and not assuming delta_k is the only cycle.
  - k = 1..11: the only cyclic partition is delta_k, D_B(T_k) = 0,2,6,12,20,30,42,56,72,90,110 = k^2-k, and the witness attains it.
  - Maximiser counts: 1,1,1,3,16,65,293,1267,5686,25475,115838.
- out/cex/lemmas.py checks (*), B2 (flip form), B4, B5, B6, B7 (the proof's explicit construction), B8, and the B9 chain on all partitions of n <= 36 ((*)/B2 for n <= 22). There were 0 violations.
- out/cex/diagrams.py checks:
  - 0.1(c)/(d) exactly on all partitions of n <= 30;
  - the 0.3 slide-within-w(w+1) claim and the energy rule on all non-delta partitions of T_k, k <= 8;
  - A.2 on all admissible (a,b), k = 2..40.

  There were 0 violations.
- The subject's own scripts reproduce their stated outputs (see RAN). dbt.py and gh_lemmas.py loop with `while x != delta`, which presumes the uniqueness proved in 0.3. That is harmless for sanity code; my exhaustive.py does not presume it.
- Floating point: none is used anywhere, in the proof or in the code.
