# Plan: B-C2-006 (EXPLOIT repair of B-C2-002, upper half: d_B(lambda) <= k^2-k for all lambda |- T_k, all k)

R1 PROVED  — B = rotation rho on tracks + compaction; energy non-increasing (proof.md Steps 1-4; subject, re-checked).
R2 PROVED  — delta_k unique cyclic partition of T_k; d_B = first hitting time of delta_k (Steps 5-9). Uses R1.
R3 PROVED  — two-track region R_k invariant; one hole/one cell annihilation dynamics (Steps 10-12). Uses R1.
R4 PROVED  — tau(h,i) <= k^2-k for Young-compatible pairs (Step 13).
R5 PROVED  — d_B <= k^2-k on R_k (Step 14). Uses R2-R4.
R6 PROVED  — conjugate formula (B l)'_j = l'_{j+1} + [j <= l'_1] (Step 19). New.
R7 PROVED  — monotonicity of B under diagram inclusion; persistence of delta_m-containment (Steps 20-21). Uses R6.
R8 PROVED  — queue form e_j(Bl) = e_{j+1}(l) + [j<=k+e_1] - [j<=k] around delta_k (Step 22). Uses R6.
R9 CHECKED — d_B <= k^2-k for all lambda |- T_k, 1 <= k <= 11 (Step 23b; exhaustive, 40.57 s).
R10 GAP    — d_B <= k^2-k for all lambda |- T_k, all k (target). Uses R2, R5, R7, R8 + missing multi-unit phase lemma.

Attempts on R10 (both failed, stopping rule reached):
  (a) last-pair phase argument generalised off R_k: arrival of the last hole/cell on tracks k,k+1 at time t1>0
      only yields t1 + tau <= t1 + k^2 - k (Young constraint gives nothing about t1).
  (b) gap-decrease argument in queue form (R8): gap between last -unit and +unit decreases by >= 1 per +lap
      only when the -unit visits the head once per +lap; short -laps (multiple -units) break it.
