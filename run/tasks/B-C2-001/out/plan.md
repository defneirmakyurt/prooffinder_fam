# Plan: B-C2-001 (D_B(T_k), BLIND)

Conjectured formula (from exact small-k data, then proved as far as stated below):
F(k) = k^2 - k for every k >= 1 (no exceptions: F(1)=0, F(2)=2, F(3)=6, ...).
Witness: lambda^(1) = (1); for k >= 2, lambda^(k) = (k-1, k-1, k-2, ..., 2, 1, 1)
(i.e. lambda_1 = k-1, lambda_i = k+1-i for 2 <= i <= k, lambda_{k+1} = 1).

Ladder (model: Young diagram cells (i,j), diagonal index i+j-1):

- R1 PROVED (proof.md Steps 0-1). Down-closed sets = diagrams; rotation rho of the diagram:
  weight-preserving, injective, cyclic on each diagonal; B(lambda) = sorted rows of rho(Y);
  if rho(Y) is down-closed then Y(B(lambda)) = rho(Y).
- R2 PROVED (Step 2). Energy E = sum of diagonal indices satisfies E(B(lambda)) <= E(lambda),
  with equality only if Y(B(lambda)) = rho(Y(lambda)). Uses R1.
- R3 PROVED (Step 3). For lambda |- T_k: E(lambda) >= sum_{d<=k} d^2 with equality iff lambda = delta_k;
  lambda != delta_k implies a cell on a diagonal > k and a hole on a diagonal <= k. B(delta_k)=delta_k.
- R4 PROVED (Step 4). If every step from lambda |- T_k is a pure rotation, then lambda = delta_k
  (gcd / residue-class argument). Uses R1, R3.
- R5 PROVED (Steps 5-6). Every lambda |- T_k reaches delta_k; delta_k is the unique cyclic partition
  of T_k; hence d_B(lambda) = min{t : B^t(lambda) = delta_k}. Uses R2, R3, R4.
- R6 PROVED (Step 7). Explicit orbit of lambda^(k): B^t(lambda^(k)) = Z(q_t, r_t) != delta_k for
  0 <= t <= k^2-k-1 and B^{k^2-k}(lambda^(k)) = delta_k; so d_B(lambda^(k)) = k^2-k for all k >= 1.
  Uses R1, R5.
- R7 CHECKED (Step 8, code/check_triangular.py). Upper bound d_B(lambda) <= k^2-k for all
  lambda |- T_k, for each k in 1..11 (exhaustive, exact integers). Uses R5 (reduction to hitting time).
- R8 GAP (Step 9, stuck.md). Upper bound d_B(lambda) <= k^2-k for every k >= 12.
  Attempted twice: (a) energy + time-between-sorts; (b) conjugate "charge/queue" model with
  lap-counting potential. Both fail on the general (far-from-delta_k) regime.
- R9 GAP. Target: D_B(T_k) = k^2-k for every k >= 1. Lower half PROVED for all k (R6);
  upper half PROVED only for k <= 11 (R7), GAP for k >= 12 (R8).
