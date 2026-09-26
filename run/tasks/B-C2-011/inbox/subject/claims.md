| claim | status | where proved |
|---|---|---|
| F(k) = k^2 - k for all k >= 1, no exceptions (D_B(T_k) = k^2 - k) | PROVED here (both bounds, written out); also PROVED in literature (Griggs-Ho 1998 Thm 3.7; Igusa 1985; Etienne 1991) | proof.md Parts A, B; sources.md |
| Shift on diagrams = diagonal rotation, plus left-slide of rows > s when s < lambda_1 - 1 | PROVED | proof.md 0.1 |
| delta_k is fixed by B | PROVED | proof.md 0.2 |
| Every orbit of T_k reaches delta_k; delta_k is the only cyclic partition of T_k (so B-C1 not needed) | PROVED (energy + CRT, Griggs-Ho Thm 2.1 idea) | proof.md 0.3 |
| lambda^(k) = (k-1,k-1,k-2,...,2,1,1) (k>=2; (1) for k=1) has d_B = k^2 - k exactly | PROVED (self-contained) | proof.md A.1-A.4 |
| c-sequence formula (*), row comparison / flip form c_{i+1} = c_i + 1 - L_i | PROVED | proof.md B1, B2 |
| Sandwich property | PROVED | proof.md B3 |
| Last step before delta_k has c_t = k-1 | PROVED | proof.md B4 |
| Griggs-Ho Lemma 3.3(2), 3.4, 3.5, 3.6 | PROVED (re-derived; 3.5's "continue this process" written as induction I(m)) | proof.md B5-B8 |
| d_B(lambda) <= k^2 - k for all lambda |- T_k | PROVED | proof.md B9 |
| D_B(T_k) = k^2 - k for k <= 8; witness orbit for k <= 40; lemma statements for n <= 30 | COMPUTER-VERIFIED (code public: y) — sanity only | out/tmp/dbt.py, witness.py, gh_lemmas.py |
