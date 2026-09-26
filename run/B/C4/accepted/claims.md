# Claims — B-C4-007

| claim | status | where proved (file, step) |
|---|---|---|
| R1 rotation lemma: rho(Y(lambda)) = rows (s, lambda_1-1, ..., lambda_s-1); B = sort | PROVED | proof.md Step 1 |
| R2 energy lemma: E(B lambda) <= E(lambda), equality iff lambda_1 <= l(lambda)+1 iff rho(Y) closed; then Y(B lambda)=rho(Y(lambda)) | PROVED | proof.md Step 2 (Lemma 2) |
| R3 cyclic => energy constant along orbit; strict drop => not cyclic; d_B = first cyclic time criterion | PROVED | proof.md Step 3 (Lemma 3, Cor. 3') |
| R4 cyclic partitions of T_{k-1}+1 are exactly gamma_1..gamma_k, B(gamma_j)=gamma_{j+1 mod k} (k>=2) | PROVED | proof.md Step 4 (Lemma 4) |
| R5 E >= E_min with equality iff gamma_j; level E_min+1 = {closed S(h;x,y)} | PROVED | proof.md Step 5 (Lemma 5) |
| R6 S(h;x,y) closed iff x,y not in {h,h+1}; rho(S(h;x,y)) = S(h+;x+,y+); offsets drop by 1 only at wrap steps | PROVED | proof.md Step 6 (Lemma 6) |
| R7 d_B(Q(h0;x,y)) = (k-h0)+(m-2)(k-1) <= (k-1)(k-3), unique maximiser Q(1;k-1,k) | PROVED | proof.md Step 7 (Lemma 7, Cor. 7') |
| R8 LOWER: d_B(lambda^(k)) = (k-1)(k-3), lambda^(k)=(k-2,k-2,k-3,...,3,2,2,1), orbit explicit, all k>=5 | PROVED | proof.md Step 8 |
| R9 UPPER: d_B(lambda) <= (k-1)(k-3) for all lambda |- T_{k-1}+1, all k>=5 | GAP | proof.md Step 9 (proved only for E <= E_min+1) |
| R9-finite: D_B(T_{k-1}+1) = (k-1)(k-3) and cyclic set = {gamma_j}, for 5 <= k <= 12 only | CHECKED | code/exhaustive_DB.py |
| R8-sanity: symbolic orbit of Step 8 agrees with iteration, 5 <= k <= 60 (not load-bearing) | CHECKED | code/verify_lower_orbit.py |
| R10 TARGET D_B(T_{k-1}+1) = (k-1)(k-3) for all k >= 5 | GAP | inherits R9 |
