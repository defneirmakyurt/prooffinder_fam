# Plan: B-C2-002 (D_B(T_k), BLIND)

Conjectured formula (from exact small-k data, then the rungs below): F(k) = k^2 - k for every k >= 1, no exceptions.
Witness: lambda^(1) = (1); lambda^(k) = (k-1, k-1, k-2, ..., 2, 1, 1) for k >= 2.

Notation: cell (i,j) of the Young diagram D(lambda); its track (diagonal) is i+j-1; track d has the d positions
(r, d+1-r), r = 1..d ("row r of track d"). rho(i,j) = (i+1,j-1) (j>=2), rho(i,1) = (1,i).

| Rung | Statement | Depends on | Status |
|---|---|---|---|
| R1 | D(B(lambda)) = rho(D(lambda)) with every column j > s shifted up one row (s = #parts); rho keeps tracks and rotates rows of track d cyclically (r -> r+1, d -> 1); a shift moves each moved cell down exactly one track | defs | PROVED (proof.md Step 1-3) |
| R2 | Energy E = sum of tracks is non-increasing; E(B(l)) = E(l) iff D(B(l)) = rho(D(l)) | R1 | PROVED (Step 4) |
| R3 | For l of T_k, l != delta_k: some track <= k has a hole, some track > k has a cell; cells on track e imply cells on every track <= e | defs | PROVED (Step 5-6) |
| R4 | delta_k is fixed by B and is the ONLY cyclic partition of T_k; hence d_B(l) = min{ i : B^i(l) = delta_k } | R1-R3, CRT | PROVED (Step 7-9) |
| R5 | Two-track region Rg = { delta_{k-1} <= l <= delta_{k+1} } is B-closed; inside it holes (track k) and cells (track k+1) rotate and the only interaction is annihilation of (hole at row 1, cell at row 2) after rotation | R1 | PROVED (Step 10-12) |
| R6 | Single-pair collision time tau(h,i) = k*x0 + 1 - h <= k^2 - k for i-h not in {0,1}; equality iff (h,i) = (1,k+1) | CRT arithmetic | PROVED (Step 13) |
| R7 | Upper bound on Rg: d_B(l) <= k^2 - k for every l in Rg (every k >= 1) | R4-R6 | PROVED (Step 14) |
| R8 | Lower bound: d_B(lambda^(k)) = k^2 - k exactly, every k >= 1 | R4-R6 | PROVED (Step 15) |
| R9 | Upper bound d_B(l) <= k^2 - k for EVERY partition l of T_k, every k | R1-R7 + ??? | GAP for k >= 12 (PROVED by hand k = 1,2; CHECKED exhaustively, exact, 1 <= k <= 11) |
| R10 | Target: D_B(T_k) = k^2 - k for every k >= 1 | R8, R9 | GAP (holds for 1 <= k <= 11; lower bound for all k) |

Dead ends on R9 (two failed attempts, stopping condition reached):
- A1 "final pair" invariant: t + max_{pairs at time t} tau(pair) <= k^2-k along every orbit. REFUTED numerically
  (out/tmp/explore2.py: violations for every k >= 3); pairs formed late can have large nominal collision time
  and are broken by other annihilations, so the invariant is not inductive.
- A2 additive two-phase bound (time to enter Rg) + (time inside Rg): entry time reaches T_{k-1} and time inside Rg
  reaches k^2-k, so the sum is not bounded by k^2-k; needs an interaction argument not found.
