# Claims: B-C3-010 (k >= 4, n = T_k - 1, M = k^2-2k-1)

| claim | status | where proved (file, step) |
|---|---|---|
| Cyclic partitions of n are exactly c_1..c_k (delta_k minus the last cell of row j) | PROVED (from Cell 1) | proof.md 1.1 |
| First part >= k+1 implies non-cyclic | PROVED | proof.md 1.2 |
| d_B(B lambda) = max(d_B(lambda)-1, 0); d_B(B^j lambda)=m (m>=1) iff d_B(lambda)=m+j | PROVED | proof.md 1.5, 1.6 |
| Preimage rule B^{-1}(mu) = {pi_s(mu) : s part value, s >= l(mu)-1}; Garden-of-Eden iff mu_1 <= l(mu)-2 | PROVED | proof.md Lemma 2.1, Cor 2.2 |
| D_1 = {d_B = 1} = {mu^(v) : 2<=v<=k-1} u {omega_k}, k-1 elements, mu^(2) = nu_k | PROVED (also CHECKED 4<=k<=60) | proof.md Prop 3.6; code/check_families.py |
| E_k = disjoint union over mu in D_1 of {lambda : B^{M-1} lambda = mu} (no hypothesis) | PROVED | proof.md Prop 4.1 |
| R_k subset of E_k, i.e. every lambda with B^{M-1} lambda = nu_k has d_B = M (target item 2 for R_k; no hypothesis) | PROVED | proof.md Prop 4.1 |
| lambda*_k = (k-1,k-2,k-2,k-3,...,2,1,1) in R_k | PROVED (subject B-C3-004 Prop 7.2; CHECKED 4<=k<=60) | proof.md 4.2 |
| alpha_k = H_k u (2,2,1,1,1), beta_k = H_k u (2,2,2,1) in R_k, k >= 5 | PROVED (also CHECKED 5<=k<=60) | proof.md 4.3 |
| Under (H): E_k = {lambda : B^{M-1} lambda non-cyclic} | PROVED [uses (H)] | proof.md 5.1 |
| Under (H): every member of E_k is Garden-of-Eden (lambda_1 <= l(lambda)-2) | PROVED [uses (H)] | proof.md 5.2 |
| Under (H): no mu in D_1 has a preimage chain of length M | PROVED [uses (H)] | proof.md 5.3 |
| Target item 3: under (H), E_k subset of R_k (no mu in D_1 \ {nu_k} has a chain of length M-1) | GAP for k >= 12 (CHECKED 4<=k<=11, unconditionally) | proof.md 6.1, 6.2; code/check_E.py |
| Target item 1: closed-form description of E_k as a function of k | GAP (partial explicit content only; explicit lists CHECKED k<=11) | proof.md 7.1-7.3 |
| E_4 = {(3,2,2,1,1)}, E_5 = six listed partitions; |E_k| = 1,6,34,175,831,3911,18163,84654 (k=4..11) | CHECKED | proof.md 7.3; code/check_E.py, code/print_R.py |
