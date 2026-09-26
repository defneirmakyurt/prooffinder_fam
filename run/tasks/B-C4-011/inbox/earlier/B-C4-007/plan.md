# Plan — B-C4-007 (BLIND prover)

Target: D_B(T_{k-1}+1) = F(k) for every k >= 5, both bounds.
Conjectured formula (from exhaustive computation k = 5..12, evidence only): **F(k) = (k-1)(k-3) = k^2 - 4k + 3**.
(For k = 3, 4 the values are 2, 4, so F fails there; the cell only asks k >= 5.)

Notation: n = T_{k-1}+1; <d,r> = cell (r, d+1-r) (diagonal d, row r); rho = rotation of cells;
E(lambda) = sum over cells (i,j) of i+j; gamma_j = delta_{k-1} + cell <k,j>;
Q(h;x,y) = delta_{k-1} - <k-1,h> + <k,x> + <k,y>.

## Ladder

- R1 (Rotation lemma) rho(Y(lambda)) = cells of rows (s, lambda_1-1, ..., lambda_s-1); rho keeps diagonals,
  shifts rows cyclically. B(lambda) = sorted nonzero row lengths. — **PROVED** (proof.md Step 1)
- R2 (Energy lemma) E(B lambda) <= E(lambda); equality iff lambda_1 <= l(lambda)+1 iff rho(Y(lambda)) is a
  Young diagram, and then Y(B lambda) = rho(Y(lambda)). Uses R1. — **PROVED** (Step 2)
- R3 cyclic mu => B mu cyclic and E(B mu) = E(mu). Uses R2. — **PROVED** (Step 3)
- R4 cyclic partitions of n are exactly gamma_1..gamma_k, and B(gamma_j) = gamma_{j+1 mod k}.
  Uses R1-R3, CRT. — **PROVED** (Step 4)
- R5 (Energy levels) E >= E_min := E(gamma_1) with equality iff lambda = gamma_j; E = E_min + 1 iff
  lambda = Q(h;x,y) for some h, x != y. Uses nothing but counting. — **PROVED** (Step 5)
- R6 (Family Q) Q(h;x,y) is a Young diagram iff x,y not in {h,h+1}; rho(Q(h;x,y)) = Q(h+;x+,y+);
  offsets (z-h) mod k constant except -1 at wrap steps (h = k-1). Uses R1. — **PROVED** (Step 6)
- R7 (Exact depth on level E_min+1) for valid Q(h0;x,y) with offsets o_x,o_y (in {2..k-1}),
  m = min: d_B(Q) = k - h0 + (m-2)(k-1) <= (k-1)(k-3), equality iff Q = lambda^(k) := Q(1;k-1,k).
  Uses R2-R6. — **PROVED** (Step 7)
- R8 (LOWER) lambda^(k) = (k-2,k-2,k-3,...,3,2,2,1) has d_B = (k-1)(k-3), orbit explicit:
  B^t = Q(1+(t mod (k-1)); b(t), b(t)+1) with b(t) = t-1 mod k, t <= k^2-4k+2;
  B^{k^2-4k+2} = (k,k-1,k-3,...,2), next = gamma_3. Uses R7. — **PROVED** (Step 8)
- R9 (UPPER) d_B(lambda) <= (k-1)(k-3) for every lambda |- n, every k >= 5.
  Proved only for E(lambda) <= E_min + 1 (R4, R7). General case — **GAP** (no argument for energy >= E_min+2).
- R10 (Target) D_B(T_{k-1}+1) = (k-1)(k-3) for all k >= 5. Uses R8, R9. — **GAP** (inherits R9);
  lower bound D_B >= (k-1)(k-3) PROVED for all k >= 5; equality CHECKED exhaustively for k = 5..12 only.

## Computations (evidence / sanity, not load-bearing)
- code/exhaustive_DB.py 5 12: D_B = (k-1)(k-3) and cyclic set = {gamma_j} for k=5..12.
- code/verify_lower_orbit.py 5 60: the symbolic orbit of R8 agrees with direct iteration.
