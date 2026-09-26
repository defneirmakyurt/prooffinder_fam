# Claims: B-C4-011 (literature, Phase 1L, upper half of B-C4)

| claim | status | where proved |
|---|---|---|
| Monotonicity: lambda <= mu implies B^t(lambda) <= B^t(mu) (Akin-Davis; Griggs-Ho Thm 4.1) | PROVED (re-derived in full) | proof.md Step 2 |
| For k >= 2, a partition of T_{k-1}+1 containing delta_{k-1} is some gamma_j, and B(gamma_j) = gamma_{j+1 mod k}; hence it is cyclic | PROVED (full) | proof.md Step 3 |
| For every nu of T_m: B^{m^2-m}(nu) = delta_m | CITED: Griggs-Ho 1998 Thm 3.7 + Cor 2.2 (Igusa 1985, Etienne 1991, Brandt 1982); argument contained in Griggs-Ho (opened) | proof.md Step 4 |
| d_B(lambda) <= min over removable cells c of d_B(lambda minus c), lambda of T_{k-1}+1 | PROVED modulo the cited theorem | proof.md Step 5(a) |
| D_B(T_{k-1}+1) <= (k-1)(k-2) for all k >= 3 | PROVED modulo the cited theorem | proof.md Step 5(b) |
| Published general bound k^2-2k-1 (Griggs-Ho Thm 4.4) is weaker than (k-1)(k-2) at r = 1 for k >= 4 | PROVED (arithmetic) | proof.md Step 6.1 |
| TARGET: d_B(lambda) <= (k-1)(k-3) for all lambda of T_{k-1}+1, all k >= 5 | GAP (not proved); = r = 1 case of Griggs-Ho Conjecture 4.7, CONJECTURED in the literature | proof.md Step 7; sources.md |
| Lower-bound witness and value (k-1)(k-3) at r = 1 appear in Griggs-Ho Thm 4.5 case (1) | PROVED in source as a claim, argument NOT written there ("imitating the proof of Theorem 3.1") | sources.md row 1 |
| max d_B over partitions of T_{k-1}+1 equals (k-1)(k-3), cyclic set = {gamma_j}, lambda^(k) attains it, for 5 <= k <= 12 | COMPUTER-VERIFIED (exact, code public: out/code/check_r1.py) | proof.md Step 7.3 |
| Griggs-Ho Figure 1 (D_B(n), n <= 36) reproduced | COMPUTER-VERIFIED (out/code/check_r1.py) | proof.md Step 7.3 |
| Corner-removal (static monotonicity) cannot give any improvement over (k-1)(k-2) for 6 <= k <= 10 (max_lambda min_nu d_B(nu) = (k-1)(k-2)) | COMPUTER-VERIFIED (exact, out/code/corner_obstruction.py), evidence only | proof.md Step 7.2 |
