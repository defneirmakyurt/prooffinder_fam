VERDICT: ACCEPT (overall). Per part: (a) ACCEPT; (b) upper half ACCEPT; (b) lower half ACCEPT; (c) ACCEPT
STATEMENT MATCH: yes for (a), (b) and (c), under the humans' reading of (c) relayed by the coordinator. That reading says an explicit criterion, proved in both directions, counts as determining the maximisers. The proof gives the criterion B^{k^2-2k-2}(lambda) = nu_k and proves both inclusions (9.1, 9.2) for every k>=4, with k=2,3 done by hand (7.3, 7.4).
FIRST PROBLEM: none.
Note: target.md itself still reads "as explicit functions of k". Under that literal wording (c) would stay MINOR, since the proof's 9.6 marks the closed list as [GAP]. This ACCEPT relies on the clarified reading, and the hand-in must state plainly that the (c) answer is a criterion.

Subject: B-C3-007 (proof.md, claims.md, code/check.py). Mode GATE. Referee B-C3-016, clean-room.

Re-issued under the corrected ASSUMPTIONS (head correction 16:38). Gated B-C1 may be used in both directions (brief.md, inbox/gated_B-C1.md). The proof's only external input is exactly that claim, so its C1 dependency is now inside ASSUMPTIONS. Nothing else in the review changed.

Re-issued again under the humans' clarification of (c), relayed by the coordinator: a characterisation by an explicit criterion, proved in both directions, counts as the answer. Only G1, the (c) verdict, the overall verdict and the (c)-related notes were changed. I also added per-step reasons for the non-mathematical steps (8, 9.4-9.6, 10), because an ACCEPT needs them.

## 1. Checklist

- G1 PASS. (a) is proved for every k>=4, every r in 1..k-1 and every lambda. (b) gives F(k)=k^2-2k-1 for k>=4, D_B(2)=0 and D_B(5)=3, and notes that k=1 is vacuous. (c) is an explicit criterion proved in both directions for every k>=4 (with k=2,3 by hand), which is what the clarified reading asks for.
- G2 PASS. The one "as in 2.1(b)" (in 4.2) is followed by the explicit inequalities c_i<=tau-1-i and c_{i+1}>=tau-i, and I re-derived both. No other unexplained "clearly", "similarly" or "by symmetry".
- G3 PASS. tau<=k is handled separately (5.1). In 5.1(ii), L=k at k=4 is done by hand through the (1^9) chain. For (b), k=1,2,3 are done by hand in 7.2-7.4. L=2 is covered in 2.1 and 2.2.
- G4 PASS. In 2.1, L'<=L-1 strictly, so the chain in 2.2 terminates. Condition (S) is preserved by 6.2(1), which I re-derived. tau is well defined (4.1).
- G5 PASS. lambda*_k is tracked symbolically through (H_t, pi_t) for all k>=3, and the first exceptional time is t*=(k+1)(k-3)+1. I checked the orbit numerically for k=3..40.
- G6 PASS. No circularity. The Griggs-Ho results are re-proved rather than cited as the target.
- G7 PASS. No computation is used by any proof step; code/check.py is sanity only. It is stdlib, uses exact integers, and reran in 19.13 s with output identical to run.txt.
- G8 PASS. Griggs-Ho 1998 is named as the source of the method and every lemma is re-proved. The one external input is gated B-C1, which is allowed by ASSUMPTIONS and stated explicitly.
- G9 PASS. Step 10 lists what is proved, what is open (a closed-form E_k) and what is sanity only.
- S1 PASS. (a) is exact. (b) has its range stated, with both halves (5.1 and 6.4) valid for every k>=4. (c) proves both inclusions (9.1 and 9.2) for every k>=4, with k=2,3 done by hand.
- S2 PASS. My exhaustive exact run covered every n<=45 (ranks 1..9), with cyclicity computed independently of C1 from the functional graph. (a) holds for all non-triangular n of rank 4..9. D_B(T_k-1)=7,14,23,34,47,62 for k=4..9 equals k^2-2k-1. For each k=4..9 the maximiser set equals B^{-m}(nu_k), with sizes 1,6,34,175,831,3911.
- S3 PASS. 4.1-5.1 treat general 1<=r<=k-1 and every lambda: (n), (1^n) and cyclic starts (d=0) need no special case, and tau still exists. The smallest k in (b)/(c), k=4, is done by hand. Completeness in (c) is proved (9.2), not tabled.
- S4 PASS. d_B is the entry time (0.3, 4.1). s counts parts before subtraction (1.1: c_{i+1}=#parts of lambda^(i)). B is taken as a multiset, so sorting is handled. d_B(cyclic)=0. The range is stated. The witness orbit is symbolic (6.4).
- S5 PASS. My independent cyclic sets equal the C1 list for every n<=45. D_B(5)=3 (C5 is N/A). F(k)<=k^2-2k-1.
- S6 PASS. The example chain (2,1,1,1,1)->(5,1)->(4,2)->(3,2,1)->(3,2,1) is re-derived by hand and consistent with the proof's B. Not in scope of (a).
- S7 PASS. My table gives D_B(T_k)=0,2,6,12,20,30,42,56,72 for k=1..9, which is k^2-k. 6.4 gives d_B(lambda*_k)=k^2-2k-1 for all k>=3, matching B-C3-002.
- S8 PASS. k>=4 is used in 5.1 (the tau<=k bound; T_k-2<k^2-2k-1 for k>=5). k=4 is done by hand, not by computer. The argument breaks at k=3 exactly in case (ii) with L=k, consistent with D_B(5)=3>2.
- S9 PASS. In my run, within each block k=4..9 the bound is attained only at n=T_k-1. The equality analysis 9.2 forces c_{tau-k}=k-1, c_{tau-k+1..tau-3}=k, c_{tau-2}=k+1, lambda^(tau-2)=nu_k and lambda^(tau-1)=(k,...,2). I verified this for every maximiser, k=4..9.
- S10 PASS. The proof does not use containment comparison; it uses the pattern-descent machinery (2.1, 2.2, 3.1).
- S11 PASS. D_B(2)=0 and D_B(5)=3 (only (1^5) attains it); the formula holds from k=4. My run agrees.
- S12 PASS. The sizes match for k=4..9 (k=10 not run). I verified that the proof's set equals S12's {lambda : B^{k^2-4k-2}(lambda)=mu_k} for k=6..9, and that B^{2k}(mu_k)=nu_k. The description is structural (dynamical), which the clarified reading of (c) accepts.
- S13 PASS. Griggs-Ho Thm 4.4 is not used as the proof; Lemmas 3.3-3.6, 4.3 and Prop 3.2 are re-proved.

## 2. Per-step re-derivation (why each step holds)

- 0.1: mu(e) has rows k-i+e_i, which is weakly decreasing because 1+e_i-e_{i+1}>=0. The last row is e_k. So the i-th part is <=k+1-i and there is no (k+1)-st part. Applying it to a cyclic partition uses the C1 "only if" direction, which ASSUMPTIONS allows.
- 0.2: re-derived. Subtracting 1 gives k-(i+1)+e_i, and the new part is s=k-1+e_k, so the result is the rotation e'. This also proves the "if" direction of C1: B^k(mu(e))=mu(e).
- 0.3: follows from 0.2 and the definition of min.
- 0.4: the conjugate bounds give k-i<=mu_i<=k+1-i, so e_i is in {0,1} and the sum is r. Then mu=mu(e) is cyclic by 0.2.
- 1.1: re-derived by induction. A born pile j has size j+c_j-i in lambda^(i). Only born pile i+1 enters row i+2.
- 1.2: (1) follows from 1.1. (2) holds because z_r>=0. (3) holds because alive rows form an interval.
- 1.3: substituting c into z_r=c_r+1-c_{r+1} gives the z-form.
- 1.4: re-derived. The max/min choices give c_p=x-1, c_{p+1}=x, a run of x, then c_q=x+1 because c_q<=c_{q-1}+1. x>=2 because c_i>=1.
- 2.1: re-derived in full. (a) There are p-1>=x born piles but |R_p|=x-1, and born pile p-1 is in R_p, so p' exists and y=p-p' lies in [2,x]. (b) Pile p' ends before row p. Pile p'+1 survives row p because z_p=0. With 1.2(2) this gives c_{p'}=y-1 and c_{p'+1}=y. (c) The induction H(m) is correct. Pile j=p'+m+1 is alive at some row in [p,p+m], and the only piles ending in rows p..p+m are p'+1..p'+m, so j survives to row p+m+1 and c_j is in {y,y+1}. H(L-1) contradicts z_{p+L-1}=0. The case L=2 gives L>=3.
- 2.2: in the chain, p_j<=p_{j+1}+X and L drops strictly. It ends at p_f<=x_f<=X with f<=L-2, so p<=(f+1)X<=(L-1)X.
- 3.1: re-derived. The k-1 born piles p+1..p+k-1 are in R_{p+k}, leaving one further pile X. Stepping back two rows via z=0 and z=1 gives R_{p+k-2}={p..p+k-3} together with X. If X is a born pile j>=2, then c_j>=c_{j-1}+2, contradicting 1.2(2). So X is original (p+k<=n) or born pile 1 (s>=p+k-1, with equality only for (1^n)).
- 4.1: the c-values on the cycle are periodic and, because 1<=r<=k-1, take both values k-1 and k. So an index with c_i=k-1 and c_{i+1}=k exists beyond d. This uses C1 "only if" (lambda^(d)=mu(e)), which ASSUMPTIONS allows.
- 4.2: re-derived. The choice of i gives c_i=tau-i-1 and c_{i+1}=tau-i. In Case A, 1.4 with x=k-1 gives (ii) with p>=i>=tau-k+1. B1 and B2 follow from 1.4 with the stated bounds. In B3 the part count a_h=z_{tau-k-1+h}-[h=k] is correct: born pile tau-k is the only pile ending in [tau-k,tau-1] that is born after row tau-k. The telescoping gives mu'_h=c_{tau-k-1+h}+1-h, which lies in {k-h,k-h+1}. By 0.4, lambda^(tau-k-1) is cyclic, which contradicts the minimality of tau (tau-k>=1).
- 5.1: in (i), L=k-1 forces c_{tau-1}=k+1, which is a part of the cyclic lambda^(tau-1) and contradicts 0.1. So L<=k-2, p<=(k-3)k and tau-1<=k^2-2k-1. In (ii): for L=k, 3.1 gives tau-1<=n-1<=T_k-2, which is <k^2-2k-1 for k>=5 (k^2-5k+2>0). For k=4, the only equality case is (1^9), and I re-derived by hand its chain (1^9)->...->(4,3,2), which is cyclic with c_7=3 and c_8=4, so tau<=7. L=k-1 is impossible: c_tau would be k, or z_tau>=1. L<=k-2 gives <=k^2-3k+1. The "moreover" follows.
- 6.1: I re-derived that (S) makes ell weakly decreasing; the only negative difference is exactly the configuration (S) excludes.
- 6.2: I re-derived ell'_1=s and ell'_{i+1}=ell_i-1. For the i=k boundary, (S) forces [pi=k]=0 when k is in H. (S) is preserved in (1). In (2) the multiset matches Lambda((H+1)\{1}).
- 6.3: the size T_{k-1}+k-|H|+1 has rank k. Row pi has k-pi+2>k+1-pi, or there is a (k+1)-st part (ell_k=1 by (S)). This uses 0.1, hence C1 "only if", which ASSUMPTIONS allows.
- 6.4: re-derived. The exceptional times are t=(k+1)v+1 with v in {k-2,k-3} mod k, so t*=k^2-2k-2. At t*, H={k-1,k} and pi=1, giving nu_k. The next partition is Lambda({k}), which is cyclic.
- 7.1-7.4: 7.1 combines 5.1 and 6.4. I re-derived the k=2 and k=3 tables by hand; there are 7 partitions of 5.
- 9.1: nu_k is not cyclic (first part k+1). B(nu_k)=(k,...,2)=mu(1,..,1,0), which is cyclic.
- 9.2: at equality, tau=k^2-2k>=k+1. Case (i) is forced: for k>=5 by 5.1; for k=4, case (ii) would force X to be original or born pile 1, giving lambda in {(9),(2,1^7),(1^9)}, all with d_B<=6<7. Then p=tau-k and L=k-2. The k-1 born piles form R_tau. Summing parts gives c_{tau-1}=k-1, so lambda^(tau-1)=(k,...,2). Undoing one B step gives nu_k.
- 9.3: follows from 7.1, 9.1 and 9.2. It is the (c) answer as an explicit criterion; nu_k and m=k^2-2k-2 are explicit in k.
- Step 8 (remark, not used): correct. 5.1 fails at k=3 because D_B(5)=3>2 (7.4, and my run).
- 9.4 (illustration, not used): E_4 and E_5 as listed agree with my independent exhaustive run.
- 9.5: restates 7.3 and 7.4.
- 9.6 (scope statement): correct. No closed list is claimed, and the sizes 1,6,34,175,831,3911 match my run. Under the clarified reading the [GAP] label is a statement about scope, not a missing step; the hand-in should drop it.
- Step 10: an accurate summary of what is established and what is sanity only.

## 3. Numerical sanity

I reran the subject's code/check.py (K=9). It completed in 19.13 s, and its output is byte-identical to run.txt apart from the timing lines. It uses exact integer arithmetic and no floating point. Note that it identifies cyclic partitions from the C1 list, so I did not treat it as independent.

## 4. Equality cases

- For n=T_k-1, k=4..9, every maximiser satisfies tau=k^2-2k, the 9.2 row pattern, lambda^(D-1)=nu_k and lambda^(D)=(k,...,2). All passed.
- lambda*_k attains the maximum for k=3..40.
- No other n in any block (k=4..9) attains k^2-2k-1.

## 5. Cross-cell

- C1: the cyclic sets match for every n<=45.
- C2: D_B(T_k)=k^2-k for k=1..9.
- C3 lower half (B-C3-002): consistent.
- C3 at k=3: D_B(5)=3.

## 6. Counterexample search (out/cex/)

- exhaust.py (log exhaust_k1-9.txt): all partitions of n=1..45, with cyclicity computed independently from the functional graph. It checked (a), (b), (c), tau-1<=bound, the 9.2 rows and the S12 alternative description. Result: ALL OK.
- lemmas.py (log lemmas_log.txt):
  - Lemmas 2.1, 2.2 and 3.1 on every pattern in the c-sequences of all partitions of n<=32 (43819 partitions, 149217 patterns): 0 violations.
  - 6.2 on all 28664 (H,pi) configurations satisfying (S), k=3..12: 0 violations.
  - 6.4 for k=3..40: 0 failures.

No counterexample found.

## OTHER ISSUES

1. (Withdrawn after the head correction.) The use of gated B-C1 in 0.1, 4.1, 5.1(i), 6.3 and 9.1 is inside the corrected ASSUMPTIONS, so it is no longer an issue. For reference, C1 also agrees with my independent computation for n<=45.
2. Minor wording: 4.2 B3 has a self-corrected sentence ("those are born after row tau-k... precisely"), and 4.2 says "as in 2.1(b)". Both are correct as written, but they should be tidied in the LaTeX.
3. |E_10|=18163 (S12) was not checked; my run stopped at k=9. This is not needed by any proof step.
4. Under the literal wording of target.md ("explicit functions of k"), (c) would be MINOR. The ACCEPT relies on the humans' clarified reading, relayed by the coordinator. The hand-in must say plainly that the (c) answer is a criterion and must drop the [GAP] label in 9.6.

RAN:
- out/cex/exhaust.py 1 9: exhaustive for all n=1..45 (ranks 1..9). COMPLETED, real 16.36 s.
- out/cex/lemmas.py 32 12 40: patterns for n<=32, 6.2 for k=3..12, lambda*_k for k=3..40. COMPLETED, real 1.95 s.
- inbox/subject/code/check.py 9 (subject rerun, plain python3), k=4..9. COMPLETED, real 19.13 s; output identical to run.txt.
