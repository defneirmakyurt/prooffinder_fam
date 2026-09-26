# Verdict: B-C2-005 (GATE, subject B-C2-002, target = LOWER half of B-C2)

```
VERDICT: ACCEPT (LOWER half only)
STATEMENT MATCH: yes for the LOWER half. F(k)=k^2-k for every k>=1 with no exceptions; explicit witness lambda^(1)=(1), lambda^(k)=(k-1,k-1,k-2,...,2,1,1) for k>=2; d_B(lambda^(k))=k^2-k is proved symbolically in k for every k>=1. The UPPER half (Step 18) is an admitted GAP for k>=12 and is NOT covered by this verdict.
FIRST PROBLEM: none in Steps 1-13 and 15, which are all the lower half needs. (Step 18, upper half, k>=12: GAP, admitted by the author; out of scope for this gate.)
CHECKLIST:
  G1 PASS - the lower-half statement is proved exactly (explicit lambda^(k), equality d_B=k^2-k, all k>=1); the proof says openly that the upper half is only proved for k<=11
  G2 PASS - every step used by the lower half is written out (inductions in Steps 1 and 6 are explicit; CRT is cited in Step 8); no bare "clearly/by symmetry"
  G3 PASS - k=1 has its own witness (1)=delta_1 with d_B=0; k=2,3 follow from the general k>=2 argument (Step 13 needs k>=2, as stated); rerun gives d_B=2, 6
  G4 PASS - R_k closure under B and the hole/cell update rule are proved (Step 12); energy is non-increasing, and in Step 8 exact equality along a cycle is all that is needed
  G5 PASS - the witness is a valid partition of T_k for every k>=2 (sum (k-1)+T_{k-1}+1); orbit tracked symbolically in (h,i)=(1,k+1); simulation k<=150 agrees
  G6 PASS - no circularity; Step 8 (uniqueness) uses only Steps 4-6, and Step 15 uses Steps 9, 12, 13
  G7 PASS - the lower half uses no computation; the Step 17 code is exact, exhaustive, count checked against p(T_k), and a rerun gives ALL OK in 13.99 s; it claims only k<=11
  G8 PASS - no literature cited; only the Chinese remainder theorem
  G9 PASS - the first line and the Summary state exactly what is established; the gap is labeled
  S1 PASS (lower half) - F(k)=k^2-k with no small-k exceptions; explicit lambda^(k); d_B(lambda^(k))=F(k) proved for every k>=1
  S2 PASS - my own exact exhaustive enumeration for k=1..10 (T_k<=55): max d_B = k^2-k, witness attains it, and it is among the maximisers; the author's code (rerun) extends this to k=11
  S3 PASS - k=1,2,3 covered; cyclic start d_B=0 (k=1); the witness orbit is tracked symbolically in k (Steps 12, 13, 15); (n) and (1^n) give T_{k-1} and T_{k-1}+1 <= k^2-k (k<=10)
  S4 PASS - d_B is cycle-entry time (Step 9); s counts all parts, including 1-parts (Step 2, row 1 of R = (1,1..s)); sorted insertion is handled by column compaction; uniqueness of delta_k is proved in the submission (Steps 5-9); upper-for-all-k is not claimed
  S5 N/A for C5 (not gated); C1 consistent: the proof itself proves delta_k is the unique cyclic partition of T_k, confirmed exhaustively for k<=10
  S6 PASS - B orbit (2,1,1,1,1)->(5,1)->(4,2)->(3,2,1)->(3,2,1) reproduced; d_B=3 <= F(3)=6
EQUALITY CASES: witness d_B=k^2-k for k=1..150 (simulation); tau(h,i)=k^2-k iff (h,i)=(1,k+1) for k=2..60; maximiser counts for k=1..10 are 1,1,1,3,16,65,293,1267,5686,25475 (witness included each time)
CROSS-CELL: consistent with C1 (delta_k unique cyclic, proved in the submission and confirmed exhaustively for k<=10); C5 N/A
CEX SEARCH: out/cex/referee_check.py (log out/cex/referee_check_log.txt): exhaustive k<=10, witness k<=150, Step-12 rule on all of R_k for k<=10, tau formula k<=60 (with simulation k<=25). No counterexample found.
OTHER ISSUES: (1) Upper half is a GAP for k>=12 (Step 18), so the full target D_B(T_k)=F(k) for all k is NOT proved; the upper gate must not pass this proof. (2) Step 17/18 refer to out/code/..., out/stuck.md and tmp/explore2.py; stuck.md and tmp/ are not in the inbox, but nothing in the lower half relies on them. (3) The hand-in has to be LaTeX; this is Markdown with LaTeX math (a formatting issue only).
RAN: author's check_DB_triangular.py, k=1..11, COMPLETED, real 13.99 s (ALL OK)
RAN: out/cex/referee_check.py 10 150 60 (A: exhaustive k=1..10; B: witness k=1..150; C: R_k rule k=2..10; D: tau k=2..60, sim k<=25; E: example), COMPLETED, real 20.18 s (all True)
RAN: out/cex/referee_check.py 6 20 10 (smoke test, earlier version of the script), COMPLETED, real 0.10 s
```

## Scope

The brief names the target as `run/B/C2/target_lower.md`. The inbox `target.md` is the combined target and says "the two halves are gated separately". This gate therefore judges only the LOWER bullet: "give an explicit partition lambda^(k) of T_k, as a function of k, and prove d_B(lambda^(k)) = F(k) for every k>=1". It also judges whatever that bullet depends on, in particular the proved description of the cyclic partitions of T_k. The upper half is an admitted GAP for k>=12 (Step 18) and falls outside this verdict.

## Checklist (Part G and Part S)

See the block above; each item has its one-line reason there.

## Per-step reasons (steps the lower half depends on)

- **N1-N4.** These are definitions. The Young-diagram characterisation and injectivity of lambda -> D(lambda) are standard facts.
- **Step 1.** Track of rho(i,j) is i+j-1 in both cases. Row r<d of track d is (r,d+1-r) with d+1-r>=2, so it maps to (r+1,d-r), which is row r+1. Row d, i.e. (d,1), maps to (1,d), which is row 1. So rho acts on each track as the cyclic shift sigma_d, and rho^t puts row r at row 1 iff r+t≡1 (mod d) and at row 2 iff r+t≡2 (mod d). I checked this by hand.
- **Step 2.** Row 1 of R=rho(D) is {(1,1..s)}, and row i+1 is {(i+1,1..lambda_i-1)}. Column j of R is {1 if j<=s} ∪ {2..c_j+1}, where c_j=#{i: lambda_i>=j+1} is an initial segment because lambda is weakly decreasing. Column j of D(B(lambda)) has length [s>=j]+c_j. So columns j<=s agree and columns j>s shift up by one. I re-derived this; the Step-12 rule was also checked by computer against the literal definition of B on all of R_k, k<=10.
- **Step 3.** A compacted cell moves from (i,j) to (i-1,j), which lowers its track by 1.
- **Step 4.** rho preserves tracks, so E(R)=E(lambda). Compaction then lowers E by sum_{j>s} c_j >= 0. Equality holds iff there is no compaction, iff D(B lambda)=rho(D lambda).
- **Step 5.** D(delta_k) is exactly the union of tracks 1..k, which holds T_k positions. If all these tracks are full, then D(lambda) contains D(delta_k) and has the same size, so lambda=delta_k. Otherwise some track d<=k has a hole, and by counting some cell lies on a track >k.
- **Step 6.** The Young property gives a left or upper neighbour one track lower (the j=1 case uses (i-1,1)). Induction then gives a cell on every lower track.
- **Step 7.** Direct: B(delta_k)=delta_k, including k=1.
- **Step 8.** On a cycle, E is constant, so there is no compaction and D(B^t lambda)=rho^t(D lambda). Choose a hole at row a of track d<=k and a cell at row b of track d+1; the cell exists by Steps 5 and 6, since a cell on track e>k>=d forces a cell on track d+1. Because gcd(d,d+1)=1, CRT gives t>=0 with the hole at (1,d) and the cell at (1,d+1). That contradicts the Young property. rho^t is a bijection preserving tracks, so holes stay holes. Valid.
- **Step 9.** Pigeonhole gives B^i=B^j with i<j, so B^i(lambda) is cyclic, and by Step 8 it equals delta_k. Hence d_B = the first hitting time of delta_k. This is the cycle-entry time, which is correct.
- **Step 10.** Counting cells gives |H|=|C|, and |H|=0 iff lambda=delta_k by Step 5. Valid.
- **Step 11.** A cell at row i of track k+1, i.e. (i,k+2-i), needs (i,k+1-i) (row i of track k, when i<=k) and (i-1,k+2-i) (row i-1 of track k, when i>=2). So i-h is not in {0,1}. Valid.
- **Step 12.** In R, only column k can compact: (1,j) missing forces j>=k, and (2,j) present forces j+1<=k+1. Column k compacts iff 1 ∈ sigma_k(H) and 2 ∈ sigma_{k+1}(C). Column k of R is then {2}, because (3,k) lies on track k+2, so the single cell (2,k) moves to (1,k). The closure of R_k and the update rule follow. I verified this exhaustively on R_k for k=2..10 (|R_k| = 3, 7, 16, 39, 95, 233, 577, 1436, 3590).
- **Step 13.** Take t=1-h+kx. Since k≡-1 (mod k+1), this gives x≡i-h-1 (mod k+1), and x_0 lies in [1,k-1] because D-1 is not in {-1,0}. The m=0 solution is >=1 and the m<=-1 solutions are <0. So tau=kx_0+1-h<=k^2-k, with equality iff x_0=k-1 and h=1, iff (h,i)=(1,k+1). I re-derived the algebra and brute-force checked every valid (h,i) for k=2..60. For k<=25 I also checked by simulating the actual partition with H={h}, C={i}.
- **Step 15.** For k=1 the witness is (1)=delta_1, so d_B=0=F(1). For k>=2 the witness is a partition of T_k, and its diagram is D(delta_k)\{(1,k)} ∪ {(k+1,1)}, so it lies in R_k with H={1}, C={k+1}, and k-1 is not in {0,1}. By Step 12 the state keeps |H|=|C|=1, and is therefore not delta_k, until the first annihilation. That happens at the least t>=1 with 1+t≡1 (mod k) and k+1+t≡2 (mod k+1), which is tau(1,k+1)=k^2-k (it satisfies t≡0 (mod k) and t≡2 (mod k+1)). After the annihilation H is empty, so the state is delta_k. By Step 9, d_B=k^2-k. Checked: k=2 gives (1,1,1)->(3)->(2,1); k=3 gives 6 steps; simulation for k=1..150 gives exactly k^2-k, and for k<=40 every intermediate state was confirmed to lie in R_k with |H|=|C|=1.

Not needed for the lower half: Step 14 (the upper bound on R_k; its logic is valid and its equality characterisation was checked), Steps 16-17 (upper bound for k<=11; the computation reproduces), and Step 18 (GAP).

## Numerical checks and counterexample search

- Author's code, rerun with `/usr/bin/time -p .venv/bin/python3 inbox/subject/code/check_DB_triangular.py 1 11`: ALL OK, real 13.99 s. It uses exact integer tuples and asserts the enumeration count against p(T_k). Log: out/cex/rerun_subject_code_log.txt.
- Mine: `/usr/bin/time -p python3 out/cex/referee_check.py 10 150 60` is stdlib-only and uses exact integers; it finished in real 20.18 s with all parts True. Log: out/cex/referee_check_log.txt. It uses its own recursive partition generator, with counts checked against Euler's pentagonal recurrence. It computes the cyclic set of the full functional graph of B, which is {delta_k} for k<=10, then D_B(T_k)=k^2-k for k=1..10, and lists the maximisers. The rest is as described above.
- No counterexample to the lower-half statement or to any intermediate claim was found. No floating point is used anywhere.
