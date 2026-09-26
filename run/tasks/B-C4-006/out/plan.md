# Plan: B-C4-006 (prover, BLIND, Phase 1)

Target: D_B(T_{k-1}+1) = F(k) for every k >= 5, both bounds.
Conjectured formula (from exhaustive data k = 5..11): F(k) = (k-1)(k-3) = (k-2)^2 - 1.

Notation: n = T_{k-1}+1. Diagonal D_d = {(i, d+1-i) : 1 <= i <= d}, 0-indexed position of (i, d+1-i) is i-1.
E(lambda) = sum over cells of (i+j-1). E_min = sum_{d<k} d^2 + k. eps = E - E_min.
rho = rigid rotation of cells: (i,j) -> (i+1,j-1) for j >= 2, (i,1) -> (1,i).

## Ladder

- R1 (Diagram criterion) A finite cell set S is the diagram of a partition iff it is closed under
  (i,j) -> (i-1,j) (i >= 2) and (i,j) -> (i,j-1) (j >= 2). Uses: none. **PROVED** (proof.md Step 1)
- R2 (Rotation) rho is a bijection diag(lambda) -> S_R := cells of the row sequence (s, lambda_1-1, ..., lambda_s-1);
  it preserves the diagonal index and shifts positions on D_d by +1 mod d. Uses: none. **PROVED** (Step 3)
- R3 (Rigid step / energy drop) If lambda_1 <= s+1 then S_R is a diagram and diag B(lambda) = rho(diag lambda);
  if lambda_1 >= s+2 then S_R is not a diagram and E(B(lambda)) <= E(lambda) - 1. Uses R1, R2. **PROVED** (Step 4)
- R4 (Energy decomposition) eps = [sum_{d>=k}(d-k+1)o_d - 1] + sum_{d<=k-1}(k-1-d)(d-o_d), both brackets >= 0.
  Uses: none. **PROVED** (Step 5)
- R5 (Level 0 = cyclic) eps(lambda) = 0 iff lambda = lambda(e_j) for some j iff lambda cyclic. Uses R4, B-C1 (r=1). **PROVED** (Step 6)
- R6 (Level 1 structure) eps = 1 iff D_1..D_{k-2} full, one hole on D_{k-1}, two cells on D_k, nothing higher;
  such diagrams <-> triples (Q; P < P') with P, P' not in {Q, Q+1}. Uses R1, R4. **PROVED** (Steps 7-8)
- R7 (Level-1 dynamics) For eps(lambda) = 1: d_B(lambda) = T := min{t >= 1 : rotated triple c_t violates}.
  Uses R2, R3, R5, R6. **PROVED** (Steps 9-10)
- R8 (Lap lemma) c_t violates iff pi_a or pi'_a lies in {0,1}, where t - t_0 = a(k-1) + r. Uses R7 set-up. **PROVED** (Step 11)
- R9 (Level-1 bound) T <= (k-1)(k-3), equality iff Q = 0 and {P,P'} = {k-2,k-1}. Uses R8. **PROVED** (Step 12)
- R10 (LOWER) lambda^(k) = (k-2,k-2,k-3,...,3,2,2,1) has d_B = (k-1)(k-3) for every k >= 5;
  explicit B^{F-1} = (k,k-1,k-3,...,2) and B^F = lambda(e_3). Uses R6, R7, R9, B-C1. **PROVED** (Step 13)
- R11 (UPPER, general) d_B(lambda) <= (k-1)(k-3) for EVERY partition lambda of T_{k-1}+1, k >= 5.
  Proved only for eps(lambda) <= 1 (R5, R9). For eps >= 2: **GAP** (see stuck.md). Exhaustively CHECKED for k = 5..11 only (evidence, not proof).
- R12 (Target) D_B(T_{k-1}+1) = (k-1)(k-3) for all k >= 5. Lower half PROVED (R10); upper half **GAP** (R11).

## Status summary
R1-R10 PROVED. R11 GAP (eps >= 2). R12 therefore PARTIAL: lower bound proved, upper bound proved only on levels eps <= 1.
