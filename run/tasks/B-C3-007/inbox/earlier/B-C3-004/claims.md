# Claims: B-C3-004

| claim | status | where proved (file, step) |
|---|---|---|
| For n=T_{k-1}+r, 1<=r<=k-1: lambda cyclic iff delta_{k-1} <= lambda <= delta_k (from Cell 1) | PROVED | proof.md, Step 1 (1.1) |
| Cyclic set closed under B; d_B(lambda)<=t iff B^t(lambda) cyclic | PROVED | proof.md, 1.2-1.3 |
| Bijection C_k <-> pairs (A,P) with support rule (S); size T_{k-1}+|A|+|P| | PROVED | proof.md, Step 2 |
| B on C_k = rotation of A (mod k), P (mod k+1), plus absorption when A_{k-1}=0, P_0=1 | PROVED (also CHECKED k=3..10) | proof.md, Lemma 3.1; code/check_classC.py |
| Hole labels only shrink, one per absorption; particle Q's v-th check at time (k+1)v-Q inspects label Q-1-v | PROVED | proof.md, Step 4 |
| Counting lemma: |H_0|>=p+1 => death by check k-3 (Q<=k-1) or k-2 (Q in {k,k+1}) | PROVED | proof.md, Lemma 5.1 |
| (a) restricted to C_k: d_B(lambda)<=k^2-2k-1, all k>=3 | PROVED | proof.md, Theorem 6.1 |
| (a) in full (lambda outside C_k) | GAP (CHECKED 4<=k<=10 only) | proof.md, 6.2; code/check_small.py |
| d_B(lambda*_k)=k^2-2k-1, lambda*_k=(k-1,k-2,k-2,k-3,...,2,1,1), all k>=3 | PROVED | proof.md, Prop. 7.2 |
| B^{k^2-2k-2}(lambda*_k)=nu_k=(k+1,k-1,...,3,1) | PROVED | proof.md, Prop. 7.2 |
| (b) lower bound D_B(T_k-1)>=k^2-2k-1, k>=4 | PROVED | proof.md, Cor. 7.3 |
| (b) upper bound D_B(T_k-1)<=k^2-2k-1, k>=4 | GAP (CHECKED 4<=k<=10) | proof.md, 8.1 |
| D_B(2)=0 (k=2), D_B(5)=3 (k=3), with extremal sets {(2),(1,1)}, {(1^5)} | PROVED | proof.md, 8.2, 8.3 |
| B^{k^2-2k-2}(lambda)=nu_k => d_B(lambda)=k^2-2k-1 | PROVED | proof.md, Prop. 9.1 |
| (c) extremal set of T_k-1 = {lambda : B^{k^2-2k-2}(lambda)=nu_k}, k>=4 | GAP (CHECKED 4<=k<=10; sizes 1,6,34,175,831,3911,18163) | proof.md, 9.2 |
