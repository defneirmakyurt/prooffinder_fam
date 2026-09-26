# code/
sanity.py — exploratory floating-point check only; the proof does NOT rest on it.
Run: python3 sanity.py (stdlib only, ~1 s).
Checks D_k - cos^2(psi_{k-1}) D_{k-1} >= 0 (the inequality of proof.md Step 4) on 200000 random
chains with m in [2,12] and sum phi_i < pi/2 (seed 1). Observed minimum -2.2e-16 (rounding at equality cases k=1,2).
