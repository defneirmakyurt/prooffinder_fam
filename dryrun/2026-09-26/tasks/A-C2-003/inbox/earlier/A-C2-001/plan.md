# Plan: A-C2 (Orthogonality Lemma)

Notation: a_i = <x_i, x_{i+1}>, theta_i = arccos|a_i|, phi_i = pi/2 - theta_i in [0, pi/2],
so |a_i| = sin(phi_i). psi_0 = 0, psi_k = phi_1 + ... + phi_k.
G = Gram matrix (m x m), D_k = k-th leading principal minor of G, D_0 := 1.
Target <=> psi_{m-1} >= pi/2.

- R1 PROVED — G is symmetric tridiagonal, unit diagonal, off-diagonal a_i; det G = 0 (rank <= m-1).
- R2 PROVED — D_k = D_{k-1} - a_{k-1}^2 D_{k-2} for 2 <= k <= m (cofactor expansion). Uses R1.
- R3 PROVED — Trig lemma: psi, phi in [0, pi/2], psi+phi < pi/2  =>  cos^2 psi - sin^2 phi >= cos^2 psi * cos^2(psi+phi).
- R4 PROVED — If psi_{m-1} < pi/2 then for 1 <= k <= m: D_k >= cos^2(psi_{k-1}) D_{k-1} and D_k > 0. Uses R2, R3 (induction).
- R5 PROVED — Target: psi_{m-1} >= pi/2, hence sum theta_i <= (m-2) pi/2. Uses R1, R4 (contradiction det G > 0 vs = 0).
