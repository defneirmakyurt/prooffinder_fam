# Plan: A-C5 — d+2 lines in R^d

Target: for every d≥2, any N=d+2 lines ℓ_1,...,ℓ_N through the origin of R^d satisfy
S = Σ_{i<j} θ(ℓ_i,ℓ_j) ≤ (C(d+2,2) - 2)·π/2,
θ(ℓ,ℓ') = arccos|⟨x,x'⟩| for unit vectors x,x' spanning ℓ,ℓ'.

Equivalent reformulation used throughout: with G_ij = ⟨x_i,x_j⟩ (Gram matrix of any chosen
unit-vector representatives), θ_ij = arccos|G_ij|, and π/2 - θ_ij = arcsin|G_ij|, so the target
is equivalent to
    Σ_{i<j} arcsin|G_ij| ≥ π.               (★)

## Ladder

R1. Gram-matrix setup: G is symmetric PSD, rank(G) ≤ d, G_ii = 1. — PROVED (definitional).

R2. Eigenvalue moment bound: with r = rank(G) ≤ d and N = d+2,
    Σ_{i<j} G_ij^2 ≥ N(N-r)/(2r), a decreasing function of r, so r=d is the extremal
    (hardest) case among r ≤ d. — PROVED (Cauchy–Schwarz on eigenvalues).

R3 (Approach A, general d). Try to close (★) via R2 plus convexity of arcsin on [0,1].
    Tested at d=2: the resulting lower bound on Σ arcsin|G_ij| is only ≈2.04, short of the
    required π. — GAP: aggregate second-moment + Jensen is structurally too weak; named
    obstruction recorded in stuck.md.

R4 (Approach B, general d). Veronese/projector embedding x ↦ P_x = xx^T - (1/d)I into the
    sphere of radius √((d-1)/d) in Sym_0(R^d); derive the exact identity
    cos(ang_P(x,x')) = (d·cos²θ - 1)/(d-1). For d=2 this gives ang_P = 2θ exactly (used in
    R5–R8). For d≥3, checked exactly at θ=π/2 (d=3): ang_P = 2π/3 < π = 2θ, and by a small-θ
    expansion ang_P ≈ √3·θ < 2θ near 0 — the inequality needed (ang_P ≥ 2θ) fails, so a
    hyperplane-separation bound on Σ ang_P cannot bound Σ θ_ij from above. — GAP for d≥3, with
    the reversal exhibited explicitly.

R5. Doubling map for lines in R^2: ℓ with angle α ↦ y = (cos2α, sin2α) ∈ S^1. Exact identity
    ang(y,y') = 2θ(ℓ,ℓ') for all α (both sub-cases Δ≤π/2, Δ>π/2 checked). — PROVED.

R6. Random-line separation identity: for two points on S^1 at circular distance β∈[0,π], the
    probability that a uniformly random line through the origin (angle mod π) separates them is
    β/π. — PROVED from scratch by a crossing-count argument.

R7. Combinatorial bound: for a(θ) = #points strictly in one open half-plane determined by
    angle θ, a(θ)(N-a(θ)) ≤ ⌊N/2⌋⌈N/2⌉ for all integers a(θ)∈{0,...,N}. — PROVED (elementary).

R8 (d=2 case, N=4). Combine R5–R7: Σ_{i<j} ang(y_i,y_j) = π·E_θ[a(θ)(N-a(θ))] ≤ π·⌊N/2⌋⌈N/2⌉
    = 4π (N=4), hence S = (1/2)Σ ang(y_i,y_j) ≤ 2π = (C(4,2)-2)·π/2. — PROVED. This is the
    full target statement for d=2.

R9 (general d≥3). NOT PROVED. Both approaches A and B block with the named obstructions above;
    no third approach was found in the time box. — GAP, stated as such in proof.md/stuck.md.

Dependencies: R8 uses R5,R6,R7. R3 uses R1,R2. R4 is independent. R9 records the state after
R3, R4 both fail to close the general case.
