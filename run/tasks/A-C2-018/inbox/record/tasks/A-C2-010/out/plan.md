# Plan (A-C2-010, BLIND, BRANCH ALGEBRAIC)

Notation: G = Gram matrix (G_ij = <x_i,x_j>), c_i = <x_i,x_{i+1}>, theta_i = arccos|c_i| in [0,pi/2],
D_k = det of leading k x k block of G (D_0 := 1), alpha_k = theta_1+...+theta_k - (k-1)pi/2.

- R1 (rank) G = X^T X with X the (m-1) x m matrix of columns x_i, so rank G <= m-1 and det G = D_m = 0. Deps: none. PROVED (proof.md Step 1)
- R2 (continuant recursion) G tridiagonal with unit diagonal; D_{k+1} = D_k - c_k^2 D_{k-1}, 1<=k<=m-1. Deps: none. PROVED (Step 2)
- R3 (partial sums) If sum_{i<=m-1} theta_i > (m-2)pi/2 then 0 < alpha_k <= pi/2 for all 1<=k<=m-1. Deps: none. PROVED (Step 3)
- R4 (trig lemma) For a in (0,pi/2], t in [0,pi/2] with b := a+t-pi/2 > 0: 0 <= cos t <= sin a sin(a+t) (= cos t + cos a sin b), and sin^2(a+t) = cos^2 b. Deps: none. PROVED (Step 4)
- R5 (invariant) Under R3's hypothesis, D_{k+1} >= sin^2(alpha_k) D_k > 0 for k = 1..m-1. Deps: R2, R3, R4. PROVED (Step 5)
- R6 (target) sum theta_i <= (m-2)pi/2. Deps: R1, R5 (contradiction D_m > 0 vs D_m = 0). PROVED (Step 6)
