# Plan: B-C1 (prover, BLIND, Phase 1)

Conventions: rows/columns 0-based. A partition lambda of n is identified with its sequence
(lambda_0 >= ... >= lambda_{s-1} >= 1) and with its cell set Y(lambda) = {(a,b): 0<=a<s, 0<=b<lambda_a}.
D_d = {(a,b) in N^2 : a+b = d} (|D_d| = d+1). C(k,r) = partitions with rows (k-1-a+eps_a)_{a=0..k-1},
eps in {0,1}^k, sum eps = r (trailing zero row dropped). W(k,r) = binary words of length k with r ones.

Ladder:
- R1 (Energy invariance) For every partition lambda with s parts, mu := (s, lambda_0-1, ..., lambda_{s-1}-1)
  satisfies E(mu) = E(lambda), E(x) := sum_a (a x_a + x_a(x_a-1)/2).          deps: none.   PROVED
- R2 (Sorting lemma) For a finite sequence x of nonnegative integers with weakly decreasing rearrangement x*,
  E(x*) <= E(x), with equality only if x is weakly decreasing.                 deps: none.   PROVED
- R3 (Monotonicity) E(B(lambda)) <= E(lambda), equality only if s >= lambda_0 - 1, and then
  B(lambda) = mu with trailing zeros removed.                                 deps: R1, R2. PROVED
- R4 (Cycle => sort-free) If lambda is cyclic, every B^t(lambda), t>=0, satisfies s >= lambda_0 - 1, and
  Y(B^t lambda) = phi^t(Y(lambda)) where phi(a,b)=(a+1,b-1) (b>=1), phi(a,0)=(0,a).  deps: R3. PROVED
- R5 (phi rotates diagonals) phi maps D_d bijectively to itself; phi^t(a, d-a) = ((a+t) mod (d+1), ...). PROVED
- R6 (No hole below a cell) If lambda is cyclic there is no d < d' with a hole on D_d and a cell on D_d'.
                                                                                deps: R4, R5. PROVED
- R7 (Cyclic => in C(k,r)) If lambda is a cyclic partition of n = T_{k-1}+r (1<=r<=k) then lambda in C(k,r).
                                                                                deps: R6.     PROVED
- R8 (C(k,r) closed, B = rotation) eps -> lambda(eps) is a bijection W(k,r) -> C(k,r), and
  B(lambda(eps)) = lambda(rho eps), rho = cyclic right shift. Hence every element of C(k,r) is cyclic.
                                                                                deps: none.   PROVED
- R9 (ii)(a): cyclic partitions of n = T_{k-1}+r are exactly C(k,r).          deps: R7, R8. PROVED
- R10 (ii)(b): number of cycles = (1/k) sum_{d | gcd(k,r)} phi(d) binom(k/d, r/d) (necklace count via
  orbit-counting lemma, proved inline).                                        deps: R8, R9. PROVED
- R11 (i): n = T_k: C(k,k) = {delta_k}; every orbit reaches delta_k.          deps: R9 + pigeonhole. PROVED

Sanity (not load-bearing): brute-force check of R9/R10 for 1 <= n <= 45, out/code/check_c1.py.  CHECKED (guide only)

## Checklist-G pass (against proof.md)
- G1: statement proved for every k >= 1, 1 <= r <= k; (i) is the case r = k. OK.
- G2: grep finds no clearly/obviously/similarly/by symmetry/routine; every step is written out. OK.
- G3: k = 1, r = k, r' = 0 (triangular n) and d < d' are handled explicitly (proof.md Section 8). OK.
- G4: E is nonincreasing (Lemma 3a); equality forces the sort-free step (strict inequality in Lemma 2). OK.
- G5: C(k,r) is a partition family closed under B for all k >= 1 (Thm 9, including k = 1). OK.
- G6: no circularity; (i) is derived from (ii)(a) plus pigeonhole. OK.
- G7: the computation is a sanity check only, stdlib, exact, 4.3 s. OK.
- G8: no citations; Burnside's lemma is proved inline (Step 6.3). OK.
- G9: proof.md Section 9 states what is established. OK.
