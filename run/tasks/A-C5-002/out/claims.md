| Claim | Status | Where proved |
|---|---|---|
| G is a symmetric PSD matrix, rank ≤ d, diagonal 1 | PROVED | proof.md Step 1 |
| Target ⟺ Σ arcsin\|G_ij\| ≥ π (★) | PROVED | proof.md Step 2 |
| Σ_{i<j} G_ij² ≥ N(N-r)/(2r), r=rank(G) ≤ d, decreasing in r | PROVED | proof.md Step 3 |
| Approach A (Jensen on arcsin from moment bound) closes (★) for general d | REFUTED (as a proof strategy) | proof.md Steps 4-8; exact numeric gap in code/approach_A_check.py |
| Veronese embedding P_x lies on sphere radius √((d-1)/d) in Sym_0(R^d) | PROVED | proof.md Step 9 |
| cos(ang_P(x,x')) = (d cos²θ - 1)/(d-1) | PROVED | proof.md Step 10; verified symbolically in code/approach_B_check.py |
| d=2: ang_P = 2θ exactly | PROVED | proof.md Step 11 |
| d≥3: ang_P < 2θ (reversal, both at θ=π/2 exactly and asymptotically as θ→0) | PROVED (as a counterexample to the needed inequality) | proof.md Steps 12-13; code/approach_B_check.py |
| Approach B closes (★) for general d≥3 | REFUTED (as a proof strategy) | proof.md Step 14 |
| Un-embedded hyperplane bound S ≤ π⌊N/2⌋⌈N/2⌉ is never strong enough (any d) | PROVED | proof.md Step 15 |
| Doubling map ang(y,y') = 2θ(ℓ,ℓ') exactly, all Δ | PROVED | proof.md Step 17; code/approach_d2_check.py |
| Random-line separation probability = β/π | PROVED | proof.md Step 18; code/approach_d2_check.py |
| a(N-a) ≤ ⌊N/2⌋⌈N/2⌉ for integers a∈{0,...,N} | PROVED | proof.md Step 20 |
| S ≤ 2π = (C(4,2)-2)π/2 for every 4 lines in R² (d=2 case of target) | PROVED | proof.md Steps 16-21 |
| Target statement for general d≥3 | GAP | proof.md, "Summary"; stuck.md |
| Full converse/equality characterization for d=2 | GAP | proof.md Step 22 |
