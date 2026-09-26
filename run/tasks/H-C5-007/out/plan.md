# Plan: H-C5-007 (EXPLOIT of H-C5-002, LOWER route only)

Target: every labelling of Q_9 has >= 2369 uphill paths.
Notation: E / O = even / odd weight vertices of Q_9 (256 each). For an induced forest F: S = V \ F,
M = F n E, Z = O \ F = S n O, m = |M|, z = |Z|, so |F| = 256 + m - z.
G_2[M] = graph on M joining words at Hamming distance 2; tau = its vertex-cover number.

| rung | statement | uses | status |
|---|---|---|---|
| R1 | Lemma A (assumed, brief): S_f = {down >= 2}, V \ S_f induces a forest and P(f) >= 512 + 8 abs(S_f) | - | ASSUMED (gate: 1 ACCEPT) |
| R2 | Reduction: if every induced forest of Q_9 has <= 279 vertices then U(Q_9) >= 2376 >= 2369 | R1 | PROVED (proof.md Step 2) |
| R3 | Lemma 1: two words of M at distance 2 have a common neighbour in Z | def. | PROVED (Step 4) |
| R4 | Lemma 2: for o in Z with t_o = abs(N(o) n M) >= 1, Z contains >= (t_o-1)(t_o-2)/2 vertices o+e_i+e_j other than o | def. | PROVED (Step 5) |
| R5 | Lemma 3: an even-weight code of length 9, min distance >= 4, has <= 21 words (Delsarte k=1,2 inequalities + A_8 <= 1, elementary) | - | PROVED (Step 6) + CHECKED arithmetic (code/check_code_bound.py) |
| R6 | General inequality: abs(F) <= 277 + tau(G_2[M]) - z for every induced forest F | R3, R5 | PROVED (Step 7) |
| R7 | Theorem: if min(abs(S n E), abs(S n O)) <= 3 then abs(F) <= 279 | R3-R6 | PROVED (Steps 8-9) |
| R8 | Corollary: labellings with min(abs(S_f n E), abs(S_f n O)) <= 3 have P(f) >= 2376 | R1, R7 | PROVED (Step 10) |
| R9 | Missing lemma: tau(G_2[M]) <= z + 2 for EVERY induced forest (WLOG z <= abs(S n E)) | R3, R4 | GAP (attempt 1: clique-cover bound works only for z <= 3; fails for large z, where tau is global) |
| R10 | Every induced forest of Q_9 has <= 279 vertices (nabla(Q_9) >= 233) | R6 + R9 | GAP (depends on R9) |
| R11 | TARGET: U(Q_9) >= 2369 | R2 + R10 | GAP |

Dependencies: R11 <- R2, R10; R10 <- R6, R9; R8 <- R1, R7; R7 <- R3, R4, R5, R6.

Attempts on the failing rung (R9/R10):
1. Structural (clique cover of G_2[M] by the Z-cliques N(o) n M, with Lemma 2 to limit t_o): closes z <= 3
   only. For large z, sum_o (t_o - 1) is about 8z while tau can be about m - 20; a global argument is needed.
2. Not re-attempted computationally (SAT/CEGAR on 512 variables) within the 60-minute time box; see stuck.md.
