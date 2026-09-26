# Claims: B-C3-007 (literature, Phase 1L)

All "PROVED" items are proved in full in out/proof.md from the ASSUMPTIONS line (gated Cell 1) only. Method from Griggs-Ho 1998 (sources.md row 1), re-proved.

| claim | status | where proved |
|---|---|---|
| Cyclic partitions of rank k are closed under B (rotation of e); recognition criterion via conjugate counts | PROVED | proof.md 0.2-0.4 |
| Pile/row model: parts of B^i(lambda) <-> piles alive at row i+1; c_{r+1} <= c_r+1; z_r = c_r+1-c_{r+1} | PROVED | proof.md 1.1-1.2 |
| Sandwich lemma (GH Prop. 3.2(3)) | PROVED | proof.md 1.4 |
| Descent lemma (GH Lemmas 3.5+3.6): pattern (x;p,L), p>=x+1 gives pattern (y;p',L'), y<=x, p-x<=p'<=p-2, L'<=L-1; and L>=3 | PROVED | proof.md 2.1 |
| Counting corollary: pattern (x;p,L) with x<=X has p <= (L-1)X | PROVED | proof.md 2.2 |
| GH Lemma 3.4: pattern (k-1;p,k) gives p+k <= n+1, equality only for (1^n) | PROVED | proof.md 3.1 |
| Entry structure (GH Lemma 4.3): tau exists, d_B <= tau-1; if tau >= k+1 then case (i) or (ii) | PROVED | proof.md 4.1-4.2 |
| (a) For every k>=4, T_{k-1}<n<T_k, lambda |- n: d_B(lambda) <= tau-1 <= k^2-2k-1 (k=4 by hand, not by table) | PROVED | proof.md 5.1 |
| d_B(lambda*_k)=k^2-2k-1 for all k>=3, lambda*_k=(k-1,k-2,k-2,k-3,...,2,1,1); B^{k^2-2k-2}(lambda*_k)=nu_k=(k+1,k-1,...,3,1) | PROVED | proof.md 6.1-6.4 |
| (b) D_B(T_k-1)=k^2-2k-1 for every k>=4; D_B(2)=0 (k=2), D_B(5)=3 (k=3); k=1: T_1-1=0 not a positive integer | PROVED | proof.md 7.1-7.4 |
| B^{k^2-2k-2}(lambda)=nu_k implies d_B(lambda)=k^2-2k-1 (k>=4) | PROVED | proof.md 9.1 |
| d_B(lambda)=k^2-2k-1 implies B^{k^2-2k-2}(lambda)=nu_k (k>=4; k=4 by hand) | PROVED | proof.md 9.2 |
| (c) maximisers of T_k-1 are exactly E_k={lambda : B^{k^2-2k-2}(lambda)=nu_k}, every k>=4; k=2: {(2),(1,1)}; k=3: {(1^5)} | PROVED | proof.md 9.3, 7.3, 7.4 |
| E_4={(3,2,2,1,1)}; E_5 = the 6 partitions listed in 9.4 | COMPUTER-VERIFIED (code public: y, out/code/check.py) | proof.md 9.4; out/code/run.txt |
| |E_k| = 1,6,34,175,831,3911 for k=4..9; (a),(b),(c) and tau-1<=k^2-2k-1 hold for 4<=k<=9 | COMPUTER-VERIFIED (code public: y), sanity only, not used by any proof | out/code/check.py, out/code/run.txt |
| Closed-form list of E_k as explicit functions of k | OPEN here (not attempted beyond 9.6; not found in sources.md) | proof.md 9.6 |
