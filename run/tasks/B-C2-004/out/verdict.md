```
VERDICT: ACCEPT
STATEMENT MATCH: yes — for the LOWER half (brief TARGET = target_lower; inbox target.md: "the two halves are gated separately"). The explicit witness lambda^(k) (k=1: (1); k>=2: (k-1,k-1,k-2,...,2,1,1)) is proved to have d_B = k^2-k for every k >= 1, so D_B(T_k) >= F(k) = k^2-k, with no exceptions. Uniqueness of delta_k as the cyclic partition is proved in the proof itself (Step 8), as target.md requires.
FIRST PROBLEM: none (lower-half scope)
CHECKLIST:
  G1 PASS — the lower half is proved as stated: every k>=1, explicit witness, exact value d_B = k^2-k, no extra hypotheses
  G2 PASS — every step Step 15 relies on (1-10, 12, 13; 11 as a hypothesis check) is written out; no bare "clearly"/"similarly"
  G3 PASS — k=1 is handled separately (lambda=(1)=delta_1, d_B=0); k=2 witness (1,1,1) is covered by the general k>=2 argument (Step 13 needs k>=2)
  G4 PASS — energy identity E(B l)=E(l)-sum_{j>s}c_j is exact; closure of R_k under B is proved; strict decrease not needed
  G5 PASS — lambda^(k) is weakly decreasing with positive parts and sum T_k for every k>=2; its orbit is tracked symbolically in k
  G6 PASS — Step 8 (uniqueness) is proved from Steps 4-6 alone; the lower bound uses it without circularity
  G7 PASS — the lower half uses no computation; Step 17 is exact, exhaustive, stdlib-only, 13.92 s here, and scoped to k<=11
  G8 PASS — the only cited result is the Chinese remainder theorem (standard); everything else is new work
  G9 PASS — first line and Summary state exactly what is proved; upper bound for k>=12 marked GAP
  S1 PASS — lower half: explicit lambda^(k), d_B(lambda^(k)) = F(k) = k^2-k for every k>=1; (the upper half is NOT established for k>=12; out of scope here)
  S2 PASS — independent exhaustive enumeration k=1..11: D_B(T_k)=k^2-k, d_B(witness)=k^2-k, witness is a maximiser, delta_k the only cyclic partition
  S3 PASS — k=1,2,3 correct (0,2,6); witness orbit tracked symbolically via track rotation (Steps 1, 12, 13); (1^n)/(n)/cyclic starts are upper-half concerns, covered for k<=11 by exhaustion
  S4 PASS — d_B = cycle-entry time (Step 9); s counts all parts incl. 1s (Step 2 row 1 of R has s cells); sorted insertion handled by column argument; d_B(cyclic)=0; uniqueness proved
  S5 PASS — consistent with C1 claim (delta_k unique cyclic, proved in Step 8); C5 at k=2 N/A (not gated)
  S6 PASS — (2,1,1,1,1)->(5,1)->(4,2)->(3,2,1)->(3,2,1) reproduced; F(3)=6>=3
EQUALITY CASES: witness attains F(k) for k<=11 (exhaustive) and its orbit matches the Step-15 description at every t<=k^2-k for k<=120; maximisers are not unique for k>=4 (3,16,65,293,... of them); the proof does not claim uniqueness
CROSS-CELL: consistent with C1 (delta_k unique cyclic, verified k<=11); C5 N/A
CEX SEARCH: out/cex/{exhaustive,witness_orbit,lemmas}.py — no counterexample to any lower-half step
OTHER ISSUES: upper bound for arbitrary lambda, k>=12 is an admitted GAP (Step 18), so the full cell C2 is not complete; Step 17 cites a path out/code/ and tmp/ scripts not in the inbox (not relied upon)
RAN: see below
```

RAN lines (all with /Users/radu.cucu/Developer/bainsahackathon/.venv/bin/python3, timed with /usr/bin/time -p, cwd out/cex/):
- inbox/subject/code/check_DB_triangular.py 1 11 — k=1..11 — COMPLETED, ALL OK, real 13.92 s (log: out/cex/author_run_log.txt)
- out/cex/exhaustive.py 1 10 — k=1..10 — COMPLETED, ALL OK, real 2.49 s (log: exhaustive_log.txt)
- out/cex/exhaustive.py 11 11 — k=11 — COMPLETED, OK, real 63.74 s (log: exhaustive_k11_log.txt)
- out/cex/witness_orbit.py 1 120 — k=1..120, all t<=k^2-k — COMPLETED, OK, real 530.67 s (log: witness_orbit_log.txt)
- out/cex/witness_orbit.py 1 60 — k=1..60 — COMPLETED, OK, real 7.47 s (log: witness_orbit_1_60_log.txt; faster rerun option)
- out/cex/lemmas.py — Steps 2-4 on 31628 partitions (all n<=30 + 3000 seeded random n in [31,200]); Step 13 k=2..60; Steps 10-14 on all 2406 partitions of R_k, k=2..9 — COMPLETED, all OK, real 6.02 s (log: lemmas_log.txt). Two earlier runs of this script failed because of bugs in MY harness, not in the proof. The first (4.57 s) crashed with a KeyError in my diagram helper. The second (7.89 s) reported FAIL because my helper did not check weak decrease and so accepted non-partitions such as (1,2). Both bugs are fixed, and those logs were overwritten by the final run.

Scope note: the brief's TARGET is run/B/C2/target_lower.md, which is outside my read permission. I used the LOWER bullet of inbox/target.md, the "two halves gated separately" line, and checklist S1. This verdict covers the lower half only.

---

## 1. Checklist pass

See the block above (G1–G9, S1–S6, each with a reason). For the lower-half scope there is no FAIL.

If this proof were judged against the FULL cell, S1/G1 would FAIL, because the upper bound for k >= 12 is not proved (Step 18, which the proof admits openly).

## 2. Per-step re-derivation (reason each step holds)

- **N1–N4.** These are definitions. The Young-diagram characterisation is standard and follows directly from weak decrease.
- **Step 1.** For j >= 2: track(i+1, j-1) = i+j-1. For j = 1: track(1, i) = i = track(i, 1). Row r of track d is (r, d+1-r). For r <= d-1 we have d+1-r >= 2, so its image is (r+1, d-r), which is row r+1. Row d is (d, 1) and maps to (1, d), which is row 1. The formula for rho^t follows by induction. Verified numerically inside lemmas.py (C) and witness_orbit.py.
- **Step 2.** Row 1 of R consists of the images of (i, 1) for i <= s, namely (1, 1..s). Row i+1 of R consists of the images of (i, j) with j >= 2, namely (i+1, 1..lambda_i - 1). So the row lengths are s, lambda_1 - 1, ..., which are the parts of B(lambda). For column j: (1, j) is in R iff j <= s, and (i+1, j) is in R iff lambda_i >= j+1 iff i <= c_j. The height of column j in D(B lambda) is [s >= j] + c_j, because parts >= j >= 1 are automatically positive. So columns with j <= s are unchanged and columns with j > s shift up by one. Checked exhaustively for n <= 30 and on 3000 random larger partitions.
- **Step 3.** A cell moving from (i, j) to (i-1, j) lowers its track by exactly 1.
- **Step 4.** rho preserves tracks, so E(R) = E(lambda). Each compacted cell lowers E by 1, and there are sum_{j>s} c_j of them. Equality holds iff every c_j = 0 for j > s, iff D(B lambda) = R. Checked numerically, same sets as Step 2.
- **Step 5.** D(delta_k) is exactly tracks 1..k, which hold T_k positions. If all of these are full, a partition of T_k must equal delta_k. Otherwise fewer than T_k cells lie on tracks <= k, so some cell lies on a track > k.
- **Step 6.** A cell at (i, j) on track e >= 2 has a left neighbour (if j >= 2) or an upper neighbour (if j = 1, so i = e >= 2) in D, and that neighbour is on track e-1. Induction gives a cell on every track 1..e.
- **Step 7.** Direct computation gives B(delta_k) = delta_k.
- **Step 8.** Energy is non-increasing and B^p lambda = lambda, so energy is constant along the orbit. Then Step 4 gives D(B^t lambda) = rho^t(D(lambda)). Take a hole on track d <= k at row a, and a cell on track d+1 at row b; the cell exists because Step 6 applies to a cell on track > k >= d. Since gcd(d, d+1) = 1, the CRT gives a time t at which (1, d) is a hole and (1, d+1) is a cell. That violates the Young property. The bijectivity of rho^t is what guarantees that holes map to holes. The case d = 1 is vacuous. The argument is correct, and exhaustion confirms uniqueness of the cyclic partition for k <= 11.
- **Step 9.** The orbit is finite, so it reaches a cyclic partition, which by Step 8 is delta_k. So d_B = the first hitting time of delta_k, which is the cycle-entry time as the definition requires.
- **Step 10.** Counting gives T_{k-1} + (k - |H|) + |C| = T_k, so |H| = |C|. Also |H| = 0 iff lambda = delta_k, by Step 5.
- **Step 11.** Take the cell (i, k+2-i). The Young property forces (i, k+1-i) to be a cell when i <= k, and (i-1, k+2-i) (row i-1 of track k) to be a cell when i >= 2. Hence i - h is not in {0, 1}. The boundary cases i = k+1 and i = 1 are handled correctly. Checked on all of R_k for k <= 9.
- **Step 12.** Compaction of column j requires (1, j) not in R, which gives track j >= k, and (2, j) in R, which gives j+1 <= k+1. So j = k. Position (3, k) lies on track k+2 and is empty, so exactly one cell moves, from (2, k) to (1, k). Tracks 1..k-1 are untouched and no cell reaches track k+2, so R_k is closed under B. The update rule for H and C follows. Checked by labelled tracking on all 2406 partitions in R_k, k = 2..9.
- **Step 13.** Write t = 1 - h + kx. Since k ≡ -1 (mod k+1), the second congruence reduces to x ≡ i-h-1. With D = i-h, the case analysis gives x_0 in [1, k-1]. For m = 0 we get t >= 1; for m <= -1 we get t <= -2k < 0. So tau = kx_0 + 1 - h <= k^2 - k, with equality iff x_0 = k-1 and h = 1, iff (h, i) = (1, k+1). Brute force for k = 2..60 agrees on the formula, the bound and the equality case.
- **Step 14 (upper half on R_k only; not needed for the lower bound).** The last annihilation removes a pair tracked back to (h_0, i_0). Minimality holds because an earlier common solution would force an earlier annihilation of the unique row-1 hole. Steps 11 and 13 then give T <= k^2 - k. Checked for k <= 9 (d_B equals tau of the last pair).
- **Step 15 (the lower bound).** For k >= 2 the witness is weakly decreasing, since lambda_1 = lambda_2 = k-1 and lambda_k = lambda_{k+1} = 1, and its sum is (k-1) + T_{k-1} + 1 = T_k. Its diagram is delta_k minus (1, k) plus (k+1, 1). So it lies in R_k with H = {1} and C = {k+1}. By Step 12, the single hole and single cell rotate until the first t >= 1 with t ≡ 0 (mod k) and t ≡ 2 (mod k+1). That time is tau(1, k+1) = k^2 - k, by Step 13, where the hypothesis i - h = k is not in {0, 1} because k >= 2. Before that time |H| = 1, so the state is not delta_k (Step 10); after it H is empty, so the state is delta_k. By Steps 8 and 9, d_B = k^2 - k. For k = 1, lambda = (1) = delta_1 and d_B = 0. This is verified at every t <= k^2 - k for k <= 120, and by exhaustion for k <= 11.
- **Steps 16–17.** Correct for their stated ranges, and not needed for the lower half. I reproduced the run (13.92 s against the quoted 14.85 s).
- **Step 18.** The GAP is honestly declared and lies outside the lower-half target.

## 3. Numerical sanity
All arithmetic is exact integer arithmetic in stdlib Python, with no floating point anywhere. The author's code runs in 13.92 s. Step 17 has a written reduction ("all partitions of T_k") to exactly the set that is enumerated, and completeness is asserted against p(n).

## 4. Equality cases
For k = 1..11:

| k | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| D_B(T_k) | 0 | 2 | 6 | 12 | 20 | 30 | 42 | 56 | 72 | 90 | 110 |
| number of maximisers | 1 | 1 | 1 | 3 | 16 | 65 | 293 | 1267 | 5686 | 25475 | 115838 |

The witness is a maximiser for every k in this range.

## 5. Cross-cell
C1: delta_k is the unique cyclic partition of T_k. This is proved in Step 8 and confirmed for k <= 11. C5 is not gated (N/A).

## 6. Counterexample search
- **exhaustive.py.** Independent enumeration, B computed by sorted insertion, and the full functional graph with cycle detection. It does not assume delta_k is unique, and it measures cycle-entry distance. Covers k = 1..11. No counterexample.
- **witness_orbit.py.** Checks the Step-15 orbit description at every t for k = 1..120. No mismatch.
- **lemmas.py.** Covers Steps 2–4, Step 13, and Steps 10–14. No failures.
