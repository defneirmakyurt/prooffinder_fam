# Claims (A-C2-015, breaker, ADVERSARY) — each numbered against out/proof.md
C1 (step 2) Target <=> sum_i arcsin|<x_i,x_{i+1}>| >= pi/2. Uses only arccos t = pi/2 - arcsin t.
C2 (step 5) For alpha, phi >= 0 with alpha+phi <= pi/2: cos(alpha) sin(alpha+phi) - sin(phi) = sin(alpha) cos(alpha+phi) >= 0.
C3 (step 8a-8d) For a chain with <x_i,x_j>=0 when |i-j|>=2 and u_{k-1} != 0: the distance-complement satisfies
    |P_{V_{k-1}} x_k| = |<x_k,x_{k-1}>| / |u_{k-1}|, where u_{k-1} is the Gram-Schmidt residual of x_{k-1}.
C4 (steps 6-8) If sum phi_i < pi/2 then |P_{V_{k-1}} x_k| <= sin(phi_1+...+phi_{k-1}) < 1 for all k; hence x_1..x_m are linearly independent
    (in any ambient dimension).
C5 (step 9-10) Linear independence of m vectors contradicts ambient dimension m-1; so the target holds for all m >= 2.
C6 (remark) Bound is sharp; equality set contains a one-parameter family at m=3 (so the optimum is not strict).
No computation is used by the proof. The numerical search in out/cex_search/ is exploratory evidence only.
