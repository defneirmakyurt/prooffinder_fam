| claim | status | where proved |
|---|---|---|
| L1: t_k > 0 => t_{k+1}^2 = 1 - a_k^2/t_k^2 (Gram–Schmidt along chain) | PROVED | proof.md Step 1 |
| L2: some t_k = 0 (m vectors in R^(m-1)) | PROVED | proof.md Step 2 |
| L3: psi,phi >= 0, psi+phi < pi/2 => sin phi <= cos psi sin(psi+phi) | PROVED | proof.md Step 3 |
| L4: psi_{m-1} < pi/2 => t_k >= cos psi_{k-1} > 0 for all k | PROVED | proof.md Step 4 |
| Target A-C2: sum theta(x_k,x_{k+1}) <= (m-2)pi/2, all m >= 2 | PROVED | proof.md Step 5 |
| Bound is sharp for every m | PROVED (explicit examples, all m >= 2) | proof.md Sharpness |
| Floating sanity check (30000 random chains, m=2..11; trig grid 401x401) | numerical evidence only, NOT proof | code/sanity_gs.py |
| Exact lemma appears in the literature | UNSURE (not found; fetches blocked) | sources.md |
