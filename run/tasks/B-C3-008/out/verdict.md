```
VERDICT: ACCEPT
STATEMENT MATCH: yes
FIRST PROBLEM: none
CHECKLIST:
  G1 PASS — proves exactly: for every k>=3, d_B(lambda*_k)=k^2-2k-1 and hence D_B(T_k-1)>=k^2-2k-1 (6.1, 8.4); no extra hypotheses beyond gated Cell 1, which the target allows.
  G2 PASS — every step of the witness chain (1.1-1.4, 2.1-2.6, 3.2, 3.5, 4.1-4.5, 5.4, 6.1) is written out; one trivial implicit converse (Phi(S(H,c))=1) noted below, a one-line computation.
  G3 PASS — smallest k=3 handled: row formula gives (2,1,1,1), admissible since k-1=2 not in {0,1}; d=2 by formula and by hand (8.3); k=2 excluded and treated separately (not in target range).
  G4 PASS — energy is preserved when lambda_1<=s+1 and drops by >=1 otherwise (1.3); Phi>=0 forces cyclicity at the first drop (2.6).
  G5 PASS — lambda*_k=Lambda({0,1},k) is admissible for every k>=3; the orbit B^t = Lambda({t,t+1} mod k,(k+t) mod (k+1)) and the CRT exit time are symbolic in k.
  G6 PASS — no circularity; Cell 1 is used only for the cyclic-set description (2.5), as TARGET permits.
  G7 PASS — the lower bound does not depend on computation; the included code is exact integer, stdlib, 38.7 s; finite checks are labelled CHECKED (finite range).
  G8 PASS — the only cited result is gated Cell 1, named explicitly in 2.5.
  G9 PASS — section 10 separates PROVED (lower bound, all k>=3) from CHECKED (k<=10) and GAP (upper bound k>=11).
  S1 PASS — for the (b) lower half: an explicit witness for every k>=3 with the k-range stated; (a), upper-(b) and (c) are outside this target (the proof marks them GAP for k>=11).
  S2 PASS — referee exhaustive run over all non-triangular n<=44 (ranks 2..9): (a) holds for k>=4; D_B(T_k-1)=k^2-2k-1 for k=4..9; d(lambda*_k)=F for k=3..9; maximiser counts 1,6,34,175,831,3911 match the proof.
  S3 PASS — the smallest k=3 is included and correct (d(lambda*_3)=2<=D_B(5)=3); completeness of (c) is not in this target.
  S4 PASS — d_B is taken as the cycle-entry time (4.2: min t with B^t cyclic); s counts all parts, 1-parts included (1.2); sorted insertion is handled via the order-ideal argument; the orbit is tracked symbolically in k.
  S5 PASS — the cyclicity test (Phi=0, 2.5) agrees with Cell 1, checked exhaustively for n<=44; the F(k)<=k^2-2k-1 comparison with (a) is N/A for the lower half; C5 at k=3 is N/A (not gated).
  S6 PASS — B((2,1,1,1,1)) -> (5,1) -> (4,2) -> (3,2,1) -> (3,2,1) reproduced; not used by the proof.
EQUALITY CASES: lambda*_k orbit simulated k=3..150: d_B=k^2-2k-1 exactly, orbit equals Lambda({t,t+1},(k+t) mod (k+1)), Phi=1 and non-cyclic for t<F, cyclic at t=F.
CROSS-CELL: consistent with gated C1 (cyclic set = Phi=0 = Cell 1 set, all n<=44).
CEX SEARCH: out/cex/witness_orbit.py (k=3..150) and out/cex/exhaustive.py (ranks 2..9) found no counterexample.
OTHER ISSUES: (1) 3.5/4.2 use Phi(S(H,c))=1 without stating it; it follows from 2.2, since D_{k-2} is full and the only extra cell is on diagonal k, so g_k=1 and every other g_d=0. (2) The target's pattern "(k-1,k-2,k-2,k-3,...,2,1,1)" is degenerate at k=3; the proof's row formula in 5.4 gives (2,1,1,1), the only sensible reading.
RAN: subject check_c3.py K=10 (ranks 2..10), COMPLETED, real 38.73 s
RAN: out/cex/witness_orbit.py 150 (k=3..150), COMPLETED, real 52.71 s
RAN: out/cex/exhaustive.py 9 (all non-triangular n, ranks 2..9, n<=44), COMPLETED, real 7.15 s
RAN: out/cex/s6.py (statement example), COMPLETED, real 0.02 s
```

## Per-step notes (lower-bound chain)

- **0.1-0.2.** Partitions correspond to order ideals, and diagonal d has d+1 cells. These are standard and correct.
- **1.1.** R(i,j)=(i+1,j-1) for j>=1, and R(i,0)=(0,i). On diagonal d this is row i -> i+1 for i<d and row d -> 0, so R is a bijection of each diagonal and preserves energy.
- **1.2.** Cells in column 0, (i,0) with i<s, go to row 0, which gets length s. Row i of C loses its column-0 cell and moves to row i+1 with length lambda_{i+1}-1. Verified.
- **1.3(i).** Assume lambda_1<=s+1. Then s>=lambda_1-1>=...>=lambda_s-1>=0, so the rows are weakly decreasing initial segments, R(C) is an order ideal, and R(C)=C(B lambda).
- **1.3(ii).** Assume lambda_1>=s+2. Then (1,s) is in R(C) but (0,s) is not. Energy of a left-justified row arrangement is sum(i*l_i+l_i(l_i-1)/2). Swapping the entries in positions 0 and 1 lowers sum(i*l_i) by lambda_1-1-s>=1. The decreasing rearrangement minimises sum(i*l_i) by the rearrangement inequality. So E(B)<=E-1. Correct.
- **1.4.** The two cases in 1.3 are exhaustive. Verified on every partition with n<=44: equality holds iff lambda_1<=s+1.
- **2.1-2.3.** E=sum_{d>=1} N_{>=d}. There are T_d positions with diagonal <=d-1, so N_{>=d}>=n-T_d. The values of nu_d follow from T_{k-1}<n<=T_k. Phi is a sum of non-negative integers.
- **2.4.** Phi=0 forces g_d=0 for every d. Taking d=k-1 gives D_{k-2} ⊆ S, and d=k gives no cell on diagonal k or beyond. The converse also holds.
- **2.5.** The Cell 1 set λ(e) has diagram D_{k-2} ∪ {(i,k-1-i): e_{i+1}=1}, which is the same as Phi=0. Checked exhaustively for n<=44 against brute-force cycle detection.
- **2.6.** Phi=1 means non-cyclic. The energy either stays the same (so C(Bλ)=R(C)) or drops to Phi=0, which is cyclic.
- **3.2 (case B).** The g_d argument is correct: N_{>=d}=g_d for d>=k, and monotonicity forces d*=k. The converse is Phi(S(H,c))=1 for every admissible (H,c) (see OTHER ISSUES (1)).
- **3.3/3.4.** Case A requires r<=k-3, so it cannot occur at r=k-1. This is correct, but the lower bound does not need it.
- **3.5.** The admissibility criterion is correct: the neighbours of diagonal k-1 cells lie on the full diagonal k-2. The cell (c,k-c) needs (c-1,k-c) when c>=1 and (c,k-1-c) when c<=k-1. The row-length formula is correct.
- **4.1.** R(S(H,c))=S(H+1 mod k, c+1 mod (k+1)), because R cycles diagonals k-1 and k with periods k and k+1.
- **4.2.** R(C) is an order ideal iff the shifted pair is admissible (3.5), and 1.4 gives the dichotomy. The induction gives d_B=tau, with B^t non-cyclic (Phi=1) for t<tau.
- **4.3.** Admissibility fails iff alpha in {gamma-1, gamma}; the side conditions hold automatically because 0<=alpha<=k-1. So tau(H,c)=min_a tau_a.
- **4.4.** All four wrap cases were re-derived. Case 2 gives w_t=w_{t-1}-k, which equals -1 iff gamma_{t-1}=0. Case 3 gives w_t>=1. Case 4 is impossible from a non-failing state. So the first failure is exactly the first t with (alpha_t,gamma_t)=(0,1). The CRT solution is t=1-c+(k+1)m with m ≡ c-1-a (mod k). The bounds 1<=t_0<=k^2<k(k+1)+1 are checked in the proof, and the m_a=0 case is excluded by admissibility when c>=1.
- **5.4/6.1.** H={0,1}, c=k is admissible because k-1 is not in {0,1} for k>=3. The rows are (k-1,k-2,k-2,...,1,1): weakly decreasing, all positive, with sum 2k-2+T_{k-2}+1... = (k^2+k-2)/2 = T_k-1. m_0=k-1 and m_1=k-2, so d=1-k+(k+1)(k-2)=k^2-2k-1. This is symbolic for every k>=3. The d_B definition then gives D_B(T_k-1)>=d_B(lambda*_k).
- Sections 7-9 are outside this target. I spot-checked 7.3 (B^{k^2-4k-2} λ* = μ_k): it is consistent with the orbit formula, and the orbit formula was verified up to k=150.

## Numerical checks / counterexample search
- `out/cex/witness_orbit.py` computes d_B(lambda*_k) with no Cell 1 input (first-repeat index), for k=3..150. For every t<=F it also checks the proof's orbit formula, Phi, and the Cell 1 cyclicity test. Log: `out/cex/witness_orbit_3_150_log.txt`, ALL OK.
- `out/cex/exhaustive.py 9` covers every partition of every non-triangular n with rank 2..9. It compares the brute-force cyclic set with the Cell 1 set and with Phi=0, checks Lemma 1.4, checks (a) for k>=4, and reports D_B(T_k-1) with its maximisers. Log: `out/cex/exhaustive_rank2_9_log.txt`, ALL OK. For k=3, D_B(5)=3>2=d(lambda*_3), which is consistent with a lower bound. For k>=4, lambda*_k is the unique Phi=1 maximiser.
- The subject's code was rerun: `out/cex/subject_check_c3_K10_log.txt`, ALL OK.
