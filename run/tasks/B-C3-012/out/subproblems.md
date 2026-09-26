# Sub-problems for B-C3(a) (and the upper half of (b))

Setting: k >= 4, n = T_{k-1}+r, 1 <= r <= k-1, 0-based diagonals, C_k = {D_{k-2} subset C(lambda) subset D_k}.

| id | precise statement | label | status / where |
|---|---|---|---|
| SP1 | Cell 1: lambda cyclic iff D_{k-2} subset C(lambda) subset D_{k-1} | (a) known, assumed (gated B-C1) | proof.md 3.1 |
| SP2 | Diagonal monotonicity: N_{>=e}(B lambda) <= N_{>=e}(lambda) for all e; C_k forward invariant | (b) reproduced | PROVED proof.md 1-2 |
| SP3 | Entry decomposition d_B = t_C + d_B(B^{t_C} lambda); (a) <=> (EI) | (b) reproduced | PROVED proof.md 3-4 |
| SP4 | (EI) for t_C = 0: lambda in C_k => d_B(lambda) <= k^2-2k-1 (all k >= 3) | known in team work | PROVED in B-C3-004 Thm 6.1 (not gated) |
| SP5 | (EI) for t_C >= 1: for lambda outside C_k, d_B(B^{t_C}lambda) <= k^2-2k-1-t_C(lambda) | (c) unknown to the team; literature result claimed but inaccessible (Griggs-Ho 1998, UNSURE) | OPEN [GAP] |
| SP5a | Sharper form suggested by B-C3-004 5.1/6.1: at the entry time t_C, every particle on diagonal k (0-based) of mu = B^{t_C}lambda has death time (k+1)v_j - Q_j <= k^2-2k-2 - t_C in the hole-label frame of B-C3-004 Step 4 | (c) | OPEN; not tested by computer here |
| SP5b | Phase-A bound: t_A(lambda) <= (k-2)^2 - 1 for k >= 5 (data: 8,15,24,35 for k=5..8) | (c) | COMPUTER-VERIFIED k<=8 only (phase_stats.py); OPEN in general |
| SP5c | Phase-B bound: t_B(lambda) <= T_{k-1} - 1 (data: 5,9,14,20,27 for k=4..8) | (c) | COMPUTER-VERIFIED k<=8 only; OPEN in general |

SP5b and SP5c alone do not suffice: max t_C + max(d-t_C) exceeds k^2-2k-1 (why_not.md). SP5 needs coupling. SP5a is one candidate form of that coupling.
