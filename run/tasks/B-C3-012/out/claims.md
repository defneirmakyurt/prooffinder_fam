| claim | status | where proved |
|---|---|---|
| Lemma 1: N_{>=e}(B lambda) <= N_{>=e}(lambda) for all e (cells never rise in diagonal) | PROVED; also COMPUTER-VERIFIED (code public: y) on every orbit step, all partitions of rank-k non-triangular n, 4<=k<=8 | proof.md sec. 1; code/phase_stats.py |
| Corollary 2: "D_m subset C" and "N_{>=e}=0" forward invariant; C_k forward invariant; t_C = max(t_A,t_B) | PROVED | proof.md sec. 2 |
| Lemma 3: cyclic subset C_k (uses Cell 1); d_B(lambda) = t_C + d_B(B^{t_C} lambda) | PROVED | proof.md sec. 3 |
| (a) <=> entry inequality (EI) | PROVED | proof.md 4.1 |
| (EI) for t_C = 0, i.e. (a) on C_k | PROVED by B-C3-004 Thm 6.1 (team, not gated); not reproduced here | inbox/earlier/B-C3-004/proof.md Step 6 |
| (EI) for t_C >= 1, i.e. (a) in general, k >= 11 | OPEN here [GAP] | stuck.md, why_not.md |
| (a) and D_B(T_k-1) = k^2-2k-1 for 4<=k<=8 | COMPUTER-VERIFIED (code public: y) | code/phase_stats.py, run_phase_stats_8.txt |
| max t_A = 4,8,15,24,35 ; max t_B = 5,9,14,20,27 ; max t_C = 5,9,15,24,35 ; max(d_B - t_C) = 7,14,23,34,47 (k=4..8) | COMPUTER-VERIFIED (code public: y) | code/run_phase_stats_8.txt |
| Literature: D_B(n) <= k^2-2k-1 for T_{k-1}<n<T_k, k>=4 (Griggs-Ho 1998) | UNSURE (primary source not opened) | sources.md |
