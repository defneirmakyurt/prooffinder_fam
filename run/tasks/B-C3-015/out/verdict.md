```
VERDICT: ACCEPT   (per part: (a) ACCEPT, (b) upper ACCEPT, (b) lower ACCEPT, (c) ACCEPT)
                  [Re-issued 16:38+ under the corrected ASSUMPTIONS (gated B-C1, both directions). The previous
                  MINOR rested only on the ASSUMPTIONS line reading "none" at dispatch. No other change to the review.]
STATEMENT MATCH: yes. (a) every k>=4, every r=1..k-1, every lambda; (b) F(k)=k^2-2k-1 for k>=4, plus k=1 (n=0 is not
                 admissible), k=2 (0), k=3 (3); (c) maximisers E_k = {lambda |- T_k-1 : B^{k^2-2k-2}(lambda)=nu_k}, a structural
                 (preimage) description, and the proof itself flags that no closed list is given.
FIRST PROBLEM: none. Step 0 uses the Cell-1 classification in both directions, and the corrected ASSUMPTIONS now
               lists exactly that (brief.md, inbox/gated_B-C1.md). Each use applies it to n of rank k with 1<=r<=k
               (see "Uses of the ASSUMPTIONS" below).
```

## Checklist

### Part G
- G1 PASS. (a) is proved for every k>=4, every n with T_{k-1}<n<T_k (every r in 1..k-1, via 4.1 with 1<=r<=k-1) and every lambda. (b) gives the formula with its range stated and the small k separately. (c) gives the exact set with both inclusions. Nothing is weakened.
- G2 PASS. No step says "clearly" or "similarly". The steps Griggs-Ho leave as "similar" or "continue this process" are written out: 2.1(c) is a real induction, 6.2 is a coordinate computation, and k=4 is done by hand in 5.1 and 9.2.
- G3 PASS. tau<=k is handled in 5.1. k=4, including lambda=(1^9), is handled by an explicit chain. k=1,2,3 are in 7.2-7.4, with k=3 checked over all 7 partitions. The case L=2 comes from 2.1. (n), (1^n) and cyclic starts are covered by the general argument, and my run confirms them.
- G4 PASS. The strict drops L_{j+1}<=L_j-1 (2.1) make the chain in 2.2 terminate. Strict inequality in 5.1(ii) for L<=k-2 needs k>2, and for L=k it needs k>=5 (k^2-5k+2>0), with k=4 done separately. Invariant (S) is preserved (6.2(1)).
- G5 PASS. lambda*_k is tracked symbolically for every k>=3 by 6.2 plus the congruence computation in 6.4. I checked it numerically for k=3..40.
- G6 PASS. The proof does not assume its conclusion. tau's minimality is used in B3 by contradiction, which is legitimate. Griggs-Ho is cited only as the source of the method, and every lemma is re-proved. The Cell-1 dependency is not circular (it is a different cell), and it is now listed in ASSUMPTIONS.
- G7 PASS. No proof step depends on computation. 9.4 and check.py are labelled sanity checks. check.py is exact integer code, stdlib only, and ran in 19.03 s.
- G8 PASS. Griggs-Ho 1998 Sect. 3-4 is cited lemma by lemma, and the new work (k=4 by hand, (c)) is marked. The Cell-1 dependency is marked as ASSUMPTIONS, which matches the corrected brief.
- G9 PASS. Step 10 lists what is PROVED, what is sanity-only, and the open item (no closed-form list for E_k).

### Part S
- S1 PASS. All three targets match (see STATEMENT MATCH). For (b), the upper half is 5.1 and the lower half is 6.4, each for every k>=4. For (c), both directions are proved: 9.1 (the set is contained in the maximisers) and 9.2 (the maximisers are contained in the set).
- S2 PASS. I enumerated exhaustively for every non-triangular n with rank 4..10 (n=7..54), deciding cyclicity from the definition. D_B(n)<=k^2-2k-1 held everywhere. D_B(T_k-1)=k^2-2k-1 for k=4..10. Each maximiser set equals {B^{k^2-2k-2}(lambda)=nu_k}.
- S3 PASS. Every r=1..k-1 is covered (4.1 uses only 1<=r<=k-1). The smallest k in range (k=4) is done by hand. Completeness of (c) is proved by hand (9.2), not by a table.
- S4 PASS. d_B is the cycle-entry time (0.3). s counts parts including 1-parts: c_{i+1} = number of parts of lambda^{(i)}. Partitions are treated as multisets. d_B(cyclic)=0. The (b) range is stated. The witness orbit is symbolic (6.4).
- S5 PASS. Every cyclicity test in the proof (0.1, 0.4, 6.3) agrees with the Cell-1 form. My definition-based cyclic sets equal the Cell-1 sets for every n tested. At k=3 (n=5) the proof gives D_B=3, consistent with C5 (N/A: C5 is not gated). F(k)=k^2-2k-1 is at most k^2-2k-1.
- S6 PASS. The statement's example does not bear on the cells. The 5.1 chain (1^9)->...->(3,3,2,1) is correct, and my code reproduces it.
- S7 PASS. The witness is the same partition as in the gated lower half B-C3-002, with d_B=k^2-2k-1. There is no conflict with D_B(T_k)=k^2-k.
- S8 PASS. Where k>=4 is used: tau<=k gives k-1 < k^2-2k-1, and 5.1(ii) L=k needs k>=5 plus the k=4 hand case. At k=3 the bound fails (D_B(5)=3 > 2), as 7.4 and Step 8 say. The k=4 step is by hand and covers n=7,8,9. My exhaustive check of n=7,8,9 agrees (D_B = 4, 5, 7).
- S9 PASS. In my table, bound attained only at n=T_k-1 for k=4..10. 9.2 derives c_{tau-2}=k+1 and c_{tau-1}=k-1: every maximiser has k+1 parts at step D-2 and equals nu_k (k-1 parts) at step D-1. I verified this for all maximisers, k=4..10. The argument is tight on both the one-drop and the several-drop orbits: it pins p=tau-k, L=k-2 in every maximiser.
- S10 N/A. The proof does not use containment comparison with T_k or T_{k-1}.
- S11 PASS. D_B(2)=0 and D_B(5)=3 (7.3, 7.4), and the formula is stated from k=4. My exhaustive check agrees.
- S12 PASS. The description is structural (preimage of nu_k). Sizes are 1, 6, 34, 175, 831, 3911 (k=4..9), plus 18163 at k=10 (my run), matching S12. For k=6..10 the maximiser set equals B^{-(k^2-4k-2)}(mu_k), and B^{2k}(mu_k)=nu_k, so the two descriptions coincide there.
- S13 PASS. Griggs-Ho Thm 4.4 is not used as a black box. Prop 3.2 and Lemmas 3.3-3.6 and 4.3 are re-proved (1.4, 2.1, 2.2, 3.1, 4.2).

## Uses of the ASSUMPTIONS (gated B-C1), hypothesis check
The gated statement requires n = T_{k-1}+r with 1<=r<=k, and k must be the rank of the partition being tested. Every use in the proof satisfies this:
- 0.1 and 4.1: n=T_{k-1}+r with 1<=r<=k-1 (Step 4 standing hypothesis).
- 5.1(i): lambda^{(tau-1)} |- n, same n.
- 5.1 k=4 chain: (4,3,2)=mu(1,1,1,0), n=9, r=3.
- 6.3: |Lambda(H,pi)|=T_{k-1}+(k-|H|)+1 with 1<=|H|<=k, so r in [1,k]. Lambda(H) has r=k-|H|>=1 for H not the full set, and 6.4 uses only |H|=1,2.
- 9.1: n=T_k-1, r=k-1.
- 7.3: k=2, r=1.
- 7.4: k=3, r=2.
The "if" direction is also re-derived in 0.2 and 0.4. My definition-based run confirms the gated classification for every n tested (S5).

## Per-step notes (reason each step holds)
- 0.1 is read off from the form mu(e): entries are k-i+e_i, and the last entry is e_k. It depends on the Cell-1 "only if" direction, which ASSUMPTIONS allows (rank k, 1<=r<=k).
- 0.2: subtracting 1 turns entry k-i+e_i into k-(i+1)+e_i, and the new part is s=k-1+e_k. The result is the sequence of mu(e'). Verified term by term.
- 0.3 is induction on 0.2.
- 0.4 turns the conjugate bounds into k-i <= mu_i <= k-i+1 (h=k-i and h=k-i+2). With mu'_1<=k this gives mu=mu(e), and mu(e) is cyclic by 0.2 (rotation has order dividing k). Self-contained.
- 1.1: induction on i. A pile survives iff its part is >=2, and born pile i+1 gives the new part c_{i+1}. Correct.
- 1.2: z_r=c_r+1-c_{r+1} follows from 1.1. The alive rows of a pile form an interval.
- 1.3 follows from the definition via 1.2.
- 1.4: the max/min choice of p and q, together with c_{m+1}<=c_m+1, forces the pattern values. x>=2 because c_i>=1.
- 2.1(a): pigeonhole gives p' (x-1 slots, p-1>=x born piles).
- 2.1(b): pile p' is dead at row p and pile p'+1 survives row p because z_p=0. This forces c_{p'}=y-1 and c_{p'+1}=y.
- 2.1(c): the only piles ending in rows p..p+m are p'+1..p'+m, and none of them is j. So j is alive at row p+m+1 (1.2(3)), and c_j is y or y+1. H(L-1) contradicts z_{p+L-1}=0, which also gives L>=3.
- 2.2: the chain has L strictly decreasing, each step costs at most X in p, and the chain has f<=L-2 steps with final p_f<=X. So p<=(L-1)X.
- 3.1: R_{p+k} is identified via the k-1 born piles p+1..p+k-1 plus one extra pile X. Stepping back two rows puts pile p in and X stays. If X is born pile j>=2, then c_j>=c_{j-1}+2, contradicting 1.2(2). So X is an original pile (p+k<=n) or born pile 1 (s>=p+k-1). Equality s=n means lambda=(1^n). Needs k>=3, which is assumed.
- 4.1: the cycle rotates e, and r in 1..k-1 makes c take both values k-1 and k. So an index with c_i=k-1, c_{i+1}=k exists after d. Hence d<=tau-1.
- 4.2: i is chosen as in 2.1(b), using z_tau=0.
  - Case A: 1.4 with x=k-1 on (i, tau+1).
  - Case B1: 1.4 with x=k-1 on (j, tau+1).
  - Case B2: 1.4 with x=k on (tau-k, j).
  - Case B3: the telescoping sum of z gives mu'_h = c_{tau-k-1+h}+1-h, which lies in {k-h, k-h+1}. By 0.4, lambda^{(tau-k-1)} is cyclic, contradicting the minimality of tau. The boundary term -[h=k] (born pile tau-k, which ends at tau-1) is correct.
- 5.1(i): L=k-1 would give a part c_{tau-1}=k+1 in the cyclic lambda^{(tau-1)}, which is impossible. So L<=k-2 and p<=(k-3)k.
- 5.1(ii): L=k gives tau-1<=n-1<=T_k-2 by 3.1. That is below k^2-2k-1 for k>=5. For k=4 the equality case is (1^9), and that orbit has tau<=7. L=k-1 is impossible in both placements (c_tau=k, or z_tau>=1). L<=k-2 gives at most k^2-3k+1.
- 5.1 "moreover" follows from these case bounds.
- 6.1: the monotonicity differences are checked, and the only negative configurations are the ones excluded by (S).
- 6.2(1),(2): coordinate identities ell'_{i+1}=ell_i-1 and ell'_1=s. Verified, including the i=k boundary.
- 6.3: the pi-th part is too large, or there is a (k+1)-st part, so 0.1 is violated. Lambda(H) is mu(e).
- 6.4: the congruences pi_t=1 iff t=(k+1)v+1, and k in H_t iff v ≡ k-2 or k-3 (mod k), give t*=(k+1)(k-3)+1=k^2-2k-2. The rows at t* equal nu_k.
- 7.1-7.4: 7.1 combines 5.1 and 6.4. For k=2, both partitions of 2 are cyclic. For k=3, all 7 partitions of 5 were checked, and I verified them independently.
- 9.1: nu_k has first part k+1, so it is not cyclic. B(nu_k)=(k,...,2)=mu(1,...,1,0), which is cyclic.
- 9.2: tau=k^2-2k, and case (i) holds (for k=4, the alternative forces lambda in {(9),(2,1^7),(1^9)}, all with d_B<=6). Then p<=(L-1)k<=(k-3)k=tau-k<=p, which pins p=tau-k and L=k-2. So R_tau is born piles tau-k+1..tau-1. The sum condition gives lambda^{(tau-1)}=(k,...,2), and inverting one step, which is unique, gives nu_k.
- 9.3 combines 7.1, 9.1 and 9.2.

## Numerical checks and counterexample search (all exact, stdlib integer code; runs unchanged from the first issue)
- `out/cex/subject_check_K9.log`: the subject's check.py rerun with K=9, k=4..9. It printed ALL OK and is identical to the submitted run.txt; real 19.03 s.
- `out/cex/indep.py` decides cyclicity from the definition, i.e. whether lambda lies on its own B-cycle, not from the Cell-1 formula.
  - `indep_k2_9.log` covers k=2..9, every n in (T_{k-1}, T_k): ALL OK; real 14.44 s.
  - `indep_k10.log` covers k=10, n=46..54: ALL OK, |E_10|=18163; real 120.85 s.
  - What is checked: D_B<=k^2-2k-1; cyclic set = Cell-1 set; d_B<=tau-1<=k^2-2k-1; D_B(T_k-1)=k^2-2k-1; the maximiser set equals the preimage of nu_k; lambda*_k attains the maximum; parts at step D-2 = k+1; S12 comparison with mu_k.
- `out/cex/lemmas.py` (`lemmas_n32.log`) runs over every partition of every n=1..32 (43819 partitions, 149217 patterns found in their c-sequences). No failures. Real 18.01 s.
  - Checked there: the pile bijection 1.1; 2.1 (L>=3 and a descendant pattern in the stated window); 2.2; 3.1; 4.1; 4.2; the 5.1 bound and its "moreover".
  - Also: 6.1/6.2 on 11163 random (H,pi) with k=3..14, and lambda*_k for k=3..40. No failures.
- Counterexample to (a): none found for k=4..10. Equality in (a) occurs only at n=T_k-1.
