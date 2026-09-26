# Plan: B-C3-010 (EXPLOIT / REPAIR of B-C3-004, target C3(c) under (H))

Notation: k >= 4, n = T_k - 1, M = M_k = k^2-2k-1, nu_k = (k+1,k-1,k-2,...,3,1), R_k = {lambda |- n : B^{M-1}(lambda) = nu_k},
D_1 = {mu |- n : d_B(mu) = 1}.

Subject's listed problems (its own 9.2 / claims): (c) was stated only as the dynamical set R_k (not explicit, excluded by
TARGET item 1), and "no other partition" was GAP. No separate gate report in inbox. Repair attempted below.

| rung | statement | depends on | status |
|---|---|---|---|
| R1 | Cyclic partitions of n are c_1..c_k (delta_k minus last cell of row j); B maps cyclic to cyclic; d(B lambda) = max(d(lambda)-1,0) | Cell 1 (ASSUMPTION) | PROVED (proof.md Step 1) |
| R2 | Preimage rule B^{-1}(mu) = {pi_s(mu): s part value, s >= l(mu)-1}; Garden-of-Eden iff mu_1 <= l(mu)-2 | def of B | PROVED (Step 2) |
| R3 | D_1 explicit: {mu^(v): 2<=v<=k-1} u {omega_k}, k-1 elements, mu^(2) = nu_k | R1, R2 | PROVED (Step 3) |
| R4 | No hypothesis: E_k = disjoint union over mu in D_1 of B^{-(M-1)}(mu); R_k subset of E_k | R1, R3 | PROVED (Prop 4.1) |
| R5 | Explicit members: lambda*_k in R_k (subject Prop 7.2), alpha_k, beta_k in R_k for k>=5 (B^3 agreement) | R4, subject Step 7 | PROVED (4.2, 4.3) |
| R6 | Under (H): E_k = {B^{M-1}lambda non-cyclic}; members are Garden-of-Eden; trees over D_1 have height <= M-1 | R1, R2 | PROVED (Step 5) |
| R7 | (R6 of proof) B^{-(M-1)}(mu) empty for mu in D_1 minus nu_k, i.e. E_k = R_k (target item 3) | R4 + ??? | GAP for k>=12 (CHECKED 4<=k<=11) |
| R8 | Closed-form description of E_k as a function of k (target item 1) | R7 + structure of backward tree | GAP (only partial explicit content R3-R5; lists CHECKED k<=11) |
| R9 | Target items 1-3 | R4, R5, R7, R8 | GAP (item 2 PROVED for R_k; items 1, 3 open for k>=12) |

Stopping: R7 attempted twice (direct use of (H); C_k particle analysis from subject) - both fail (see stuck.md). R8 fails
for the reason in proof.md 7.2. Stop and report PARTIAL.

Numerical: out/code/check_E.py 11 (exhaustive, exact, unconditional): E_k = R_k, max d = M, all E_k Garden-of-Eden,
sizes 1,6,34,175,831,3911,18163,84654 for k=4..11 (CHECKED only for these k). out/code/check_families.py 60: cross-check
of Steps 3-4 for 4<=k<=60.
