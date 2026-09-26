# Plan: B-C3-011 (EXPLOIT / REPAIR of B-C3-004)

Target: for every k >= 4, every n with T_{k-1} < n < T_k (n = T_{k-1}+r, 1 <= r <= k-1), every lambda |- n:
d_B(lambda) <= k^2-2k-1; hence D_B(T_k-1) <= k^2-2k-1 (k >= 4).

Gap in subject (B-C3-004): (a) was proved only on the class C_k. Repair: abandon the C_k route for the
upper bound and use the c-sequence route (as suggested in the brief), with a new end-of-orbit lemma for
non-triangular n (the cyclic set is a rotation class) and two new length lemmas.

Rungs (all for arbitrary lambda |- n >= 1 unless stated):
- R1 Column model: parts of B^{i-1}(lambda) = remaining lengths of the columns covering row i; c_{i+1} = c_i + 1 - L_i. [PROVED, proof.md §1]
- R2 Sandwich lemma: i<j, c_i < x < c_j => pattern (x-1,x,...,x,x+1) inside [i,j], length >= 2. Uses R1. [PROVED, proof.md §2]
- R3 Triple lemma: (x-1,x,x+1) at p => p <= x. Uses R1. [PROVED, proof.md §3]
- R4 Shortening lemma: pattern of length >= 3 and p > x => shorter pattern (p',q',x'), x'<=x, p' >= p-x. Uses R1. [PROVED, proof.md §4]
- R5 Descent: pattern (p,q,x) => p <= (q-p-1) x. Uses R3, R4. [PROVED, proof.md §5]
- R6 Length lemma: pattern (p,q,x) => q-p != x and q-p <= x+1. Uses R1. [PROVED, proof.md §6]
- R7 Long-pattern lemma: pattern of length m = x+1 => p+m <= T_{m-1}+2. Uses R1. [PROVED, proof.md §7]
- R8 Cycle lemma (non-triangular n, uses B-C1): after t = d_B, c_{t+i} = k-1+e_{k+1-i} (1<=i<=k), all c_u in {k-1,k} for u>t. [PROVED, proof.md §8]
- R9 End lemma: t>=1 => c_t in {k-2,k-1}; if c_t = k-1 then row t has exactly one part k+1, all others <= k-1, and c_{t+k-1} = k. Uses R8, B-C1. [PROVED, proof.md §9]
- R10 Case c_t = k-2 => t <= k^2-2k-1. Uses R2, R5, R6, R7, R8. [PROVED, proof.md §10]
- R11 Case c_t = k-1 => t <= k^2-2k-1 (sub-cases A1, A2, B). Uses R1, R2, R5, R6, R7, R9. [PROVED, proof.md §11]
- R12 Target (a) and (b-upper). Uses R9-R11. [PROVED, proof.md §12]

Sanity (not proof): out/code/check_c3a.py checks R6, R7, R9 and the case certificates of R10/R11 exhaustively for 4<=k<=9, and D_B(n) <= k^2-2k-1. [CHECKED 4<=k<=9, sanity only; ran 46.78 s]
