STATEMENT PROVED HERE (exact, and no more): for **d = 2**, N = d+2 = 4, any 4 lines
ℓ_1,ℓ_2,ℓ_3,ℓ_4 through the origin of R^2 (repetitions allowed) satisfy
    S(ℓ_1,...,ℓ_4) ≤ (C(4,2) - 2)·π/2 = 2π,
where S = Σ_{i<j} θ(ℓ_i,ℓ_j), θ(ℓ,ℓ') = arccos|⟨x,x'⟩| ∈ [0,π/2] for unit vectors x,x' spanning
ℓ,ℓ'.

For general d≥3 the target statement is **not proved** here. Two distinct approaches were
carried out and both stop at a named obstruction (Steps 9–15 below record exactly where and
why). This is reported as a PARTIAL result: complete proof for d=2 (a genuine instance of the
family, not merely a numerical check), plus two blocked general-d approaches with precise gaps.

Throughout, for a line ℓ_i fix any unit vector representative x_i (the choice of sign does not
affect θ or S, since θ uses |⟨·,·⟩|).

## Part I — general-d setup and reformulation (used by both approaches)

1. **Gram matrix.** Let G = (G_ij)_{i,j=1}^N, G_ij = ⟨x_i,x_j⟩, N = d+2. G is symmetric,
   positive semidefinite (it is a Gram matrix), G_ii = 1, and rank(G) ≤ d because the x_i lie in
   R^d. Write θ_ij = θ(ℓ_i,ℓ_j) = arccos|G_ij| for i≠j.

2. **Reformulation.** Since arccos(x) + arcsin(x) = π/2 for x∈[0,1] (standard identity: both
   sides differentiate to 0 and agree at x=0), π/2 - θ_ij = arcsin|G_ij|. Summing over the
   C(N,2) pairs,
       (C(N,2))·π/2 - S = Σ_{i<j} arcsin|G_ij|.
   Hence the target S ≤ (C(N,2)-2)·π/2 is **equivalent** to
       Σ_{i<j} arcsin|G_ij| ≥ π.                                             (★)

3. **Eigenvalue moment bound.** Let λ_1≥...≥λ_N≥0 be the eigenvalues of G and r = rank(G) ≤ d,
   so exactly N-r of the λ_k are 0. Then Σλ_k = trace(G) = N (diagonal entries are 1), and
       trace(G²) = Σ_k λ_k² = Σ_{i,j} G_ij² = N + Σ_{i≠j} G_ij² = N + 2Σ_{i<j} G_ij².
   By the Cauchy–Schwarz inequality applied to the r nonzero eigenvalues,
   (Σ_{k: λ_k>0} λ_k)² ≤ r·Σ_{k:λ_k>0} λ_k², i.e. N² ≤ r·Σλ_k², so Σλ_k² ≥ N²/r. Combining,
       Σ_{i<j} G_ij² ≥ (N²/r - N)/2 = N(N-r)/(2r).                            (1)
   The right side, as a function of r on (0,N], equals N²/(2r) - N/2, which is strictly
   decreasing in r. Since r ≤ d, the bound (1) is weakest exactly when r=d; i.e. the hardest
   case for proving (★) is when the x_i span all of R^d (r=d), and any r<d configuration
   satisfies a *stronger* instance of (1). [This is a genuine general-d fact but, as Approach A
   below shows, (1) alone is not strong enough to force (★).]

## Part II — Approach A (aggregate moments + convexity): blocked

4. arcsin is convex on [0,1]: arcsin''(x) = x/(1-x²)^{3/2} ≥ 0 for x∈[0,1). By Jensen's
   inequality for the convex function arcsin, with m = C(N,2) terms,
       (1/m)Σ_{i<j} arcsin|G_ij| ≥ arcsin( (1/m)Σ_{i<j}|G_ij| ).                (2)

5. Since |G_ij|∈[0,1], |G_ij| ≥ G_ij², so Σ_{i<j}|G_ij| ≥ Σ_{i<j}G_ij² ≥ N(N-d)/(2d) by (1) with
   r=d (the worst case identified in Step 3).

6. Combining (2) and Step 5: Σ arcsin|G_ij| ≥ m·arcsin( N(N-d)/(2dm) ), m=C(N,2).

7. **This bound is too weak, checked exactly at d=2 (N=4, m=6):** N(N-d)/(2dm) = 4·2/(2·2·6) =
   1/3, and m·arcsin(1/3) = 6·arcsin(1/3). Exact value: arcsin(1/3) is irrational (not a
   rational multiple of π; standard fact, e.g. since sin of a rational multiple of π other than
   the well-known list is never a "nice" rational unless in the finite Niven's-theorem list, and
   1/3 is not in that list) but numerically arcsin(1/3) = 0.339837 rad, so 6·0.339837 = 2.0390,
   which is **less than π = 3.14159**, i.e. strictly short of the target lower bound (★) needs.
   This is an *exact* function evaluation (arcsin, arcsin(1/3) computed to any desired precision
   is not in dispute; the comparison 2.039 < π is unambiguous since the gap 1.10 rad exceeds any
   plausible numerical error). See out/code/approach_A_check.py.

8. **Obstruction (Approach A).** The loss has two independent sources: (i) Step 5 replaces
   Σ G_ij² by the smaller Σ|G_ij| bound only in the direction |G_ij|≥G_ij² which discards
   information whenever some |G_ij| is itself small; (ii) more fundamentally, Jensen's
   inequality (2) is tight only when all |G_ij| are *equal*, whereas the actual extremal
   configuration (d axes, 2 repeated) has |G_ij| concentrated at the two extreme values 0 and 1,
   the opposite of "equal spread." Jensen from a single aggregate moment can never certify a
   bound whose extremizer is a maximally *concentrated* (non-equal) distribution: any config
   with the same Σ|G_ij| but spread more evenly gives a strictly larger value of the Jensen
   lower bound while the true Σ arcsin|G_ij| can be smaller for concentrated configurations
   satisfying additional (PSD/rank) structure not captured by the two moments used. Hence (★)
   cannot be closed this way from (1) alone; a genuinely finer invariant of the rank-d PSD
   constraint (beyond one moment) is needed for general d. — **GAP for d≥3.**

## Part III — Approach B (Veronese/projector embedding): blocked

9. For a unit vector x∈R^d define P_x = xx^T - (1/d)I, a traceless symmetric d×d matrix, i.e. a
   point of the Euclidean space Sym_0(R^d) (dimension D=d(d+1)/2-1) with inner product
   ⟨A,B⟩=trace(AB). Direct computation: ⟨P_x,P_x⟩ = trace(xx^Txx^T) - (2/d)trace(xx^T) +
   (1/d²)trace(I) = 1 - 2/d + 1/d = 1 - 1/d = (d-1)/d (using trace(xx^T)=|x|²=1,
   trace(xx^Txx^T)=(x·x)²=1, trace(I)=d). So every P_x lies on the sphere of radius
   r_0=√((d-1)/d) in Sym_0(R^d): the map x↦P_x is well-defined on lines (P_x=P_{-x}) and sends
   lines in R^d to points on a genuine round sphere, generalizing the doubling map of Part IV
   below (which is the case d=2).

10. For two unit vectors x,x' with c=⟨x,x'⟩ (so |c|=cosθ, θ=θ(ℓ,ℓ')): trace(xx^Tx'x'^T) =
    (x·x')² = c² (using trace(ABAB)-type identity trace((xx^T)(x'x'^T)) = (x^Tx')(x'^Tx) = c²),
    so ⟨P_x,P_{x'}⟩ = trace((xx^T-(1/d)I)(x'x'^T-(1/d)I)) = c² - (1/d)trace(x'x'^T) -
    (1/d)trace(xx^T) + (1/d²)trace(I) = c² - 1/d - 1/d + 1/d = c² - 1/d. Let ang_P(x,x')∈[0,π]
    be the angle
    between P_x,P_{x'} on the sphere (arccos of their normalized inner product). Then
        cos(ang_P) = (c² - 1/d)/((d-1)/d) = (d·c² - 1)/(d-1) = (d·cos²θ - 1)/(d-1).           (3)

11. **d=2 check.** For d=2, (3) gives cos(ang_P) = 2cos²θ - 1 = cos(2θ), and since 2θ∈[0,π],
    ang_P = 2θ exactly — this recovers the doubling-map identity of Part IV (Step 16) as the
    d=2 instance of the general Veronese embedding. This is a genuine coincidence special to
    d=2: for d=2, Sym_0(R^2) is 2-dimensional, so the sphere in Step 9 literally *is* a circle,
    the same circle as the doubling map.

12. **d≥3 reversal, checked exactly at θ=π/2.** For d=3, θ=π/2 gives c=0, so by (3)
    cos(ang_P) = (d·0-1)/(d-1) = -1/(d-1); for d=3 this is -1/2, so
    ang_P = arccos(-1/2) = 2π/3 exactly. Compare to 2θ = π. Since 2π/3 < π, we have
        ang_P(x,x') < 2θ(ℓ,ℓ')   at θ=π/2, d=3.                                (4)
    This is an exact computation (arccos(-1/2)=2π/3 is a standard exact value), not a numerical
    approximation.

13. **Small-θ confirmation.** Near θ=0, c=cosθ≈1-θ²/2, so c²≈1-θ², and by (3)
    cos(ang_P) ≈ (d(1-θ²)-1)/(d-1) = 1 - dθ²/(d-1). For small x, arccos(1-x) ≈ √(2x), so
    ang_P ≈ √(2·dθ²/(d-1)) = θ·√(2d/(d-1)). For d=3, √(2d/(d-1)) = √3 ≈ 1.732 < 2. So again
    ang_P < 2θ for small θ>0 when d=3 (and in general √(2d/(d-1)) < 2 ⟺ 2d/(d-1) < 4 ⟺
    2d < 4d-4 ⟺ d>2, true for all d≥3). So the reversal ang_P < 2θ holds both at θ=π/2 exactly
    and asymptotically as θ→0, for every d≥3.

14. **Why this blocks Approach B.** The strategy that worked for d=2 (Part IV) needed
    Σ_{i<j} ang_P(x_i,x_j) ≥ 2·Σ θ_ij, so that an *upper* bound on Σ ang_P (obtainable, for any
    d, from the same random-hyperplane-separation argument applied to the sphere in Sym_0(R^d),
    since that argument only used that the points lie on a Euclidean sphere, which holds for
    every d by Step 9) would yield an upper bound on Σθ_ij = S. But Steps 12–13 show the
    pointwise inequality needed (ang_P ≥ 2θ) is **false** for d≥3 — it holds with equality only
    at d=2 and reverses strictly for d≥3. So bounding Σang_P from above gives no valid bound on
    S in this direction. — **GAP for d≥3.**

15. A direct (non-embedded) hyperplane-separation bound on the x_i themselves (using the full,
    sign-dependent angle ang(x_i,x_j)∈[0,π] and the elementary pointwise fact θ_ij ≤
    ang(x_i,x_j), proved because θ_ij=min(ang,π-ang)≤ang) gives, by the same argument as Part IV,
    S ≤ Σang(x_i,x_j) ≤ π·⌊N/2⌋⌈N/2⌉. Checked against the target: this requires
    2⌊N/2⌋⌈N/2⌉ ≤ C(N,2)-2. For N=4: 2·4=8 > C(4,2)-2=4 — fails. For N=5: 2·6=12 > 8 — fails.
    In general 2⌊N/2⌋⌈N/2⌉ ≥ (N²-1)/2 > N(N-1)/2 - 2 = C(N,2)-2 for all N≥2 (since
    (N²-1)/2 - (N(N-1)/2-2) = (N²-1-N²+N)/2+2 = (N-1)/2+2 > 0). So the un-embedded bound is
    *never* strong enough, for any d — confirming that some doubling/embedding refinement
    (halving the effective angle) is essential, and that the only place we could complete it
    (d=2) relied on the sphere Sym_0(R^2) coinciding with a circle. — recorded as part of the
    same obstruction.

## Part IV — Complete proof for d=2 (N=4)

16. **Doubling map.** Represent a line ℓ in R^2 by its angle α∈[0,π) (mod π; α and α+π give the
    same line). Define y(ℓ) = (cos2α, sin2α) ∈ S^1 ⊂ R^2. This is well-defined on lines (adding
    π to α adds 2π to 2α, same point).

17. **Exact identity ang(y,y') = 2θ(ℓ,ℓ').** Let α,α' be the angles of ℓ,ℓ', Δ = |α-α'| mod π ∈
    [0,π), so θ(ℓ,ℓ') = min(Δ,π-Δ) ∈[0,π/2] by definition of the acute angle between lines.
    - If Δ≤π/2: θ=Δ, and 2Δ∈[0,π]. The standard angle between y,y' (i.e. arccos(y·y')∈[0,π]) is
      arccos(cos2Δ) = 2Δ (arccos∘cos is the identity on [0,π]). So ang(y,y')=2Δ=2θ.
    - If Δ>π/2 (so Δ∈(π/2,π)): θ=π-Δ, and 2Δ∈(π,2π). Since cos is 2π-periodic and even,
      cos(2Δ)=cos(2π-2Δ), and 2π-2Δ∈(0,π), so arccos(cos2Δ)=2π-2Δ=2(π-Δ)=2θ.
    In both cases ang(y,y')=2θ(ℓ,ℓ'), exactly, with no residual error. (Degenerate case Δ=0 or
    Δ=π/2 checked directly: Δ=0 gives ang=0=2θ; Δ=π/2 gives 2Δ=π, ang=π=2θ.) This holds for
    coincident lines too (θ=0 ⟹ ang=0), so repetitions among the ℓ_i are handled with no special
    case.

18. **Random-line separation identity.** Fix two points y,y' on S^1 at angles φ,φ' (mod 2π), and
    let β=ang(y,y')∈[0,π] be their circular distance (shorter arc). Let θ_line be uniform on
    [0,π) (a "random line" through the origin, i.e. a random unordered pair of antipodal
    directions {θ_line,θ_line+π}); it determines two open half-planes H_1=(θ_line,θ_line+π),
    H_2=(θ_line+π,θ_line+2π) (mod 2π). Say the line *separates* y,y' if exactly one of them lies
    in H_1. **Claim:** P(separates) = β/π.
    Proof: the event "separates" changes only when θ_line crosses φ or φ' (mod π); since
    Lebesgue measure on the circle {θ_line} of circumference π is translation invariant, and
    whether y,y' are separated depends only on θ_line-φ and θ_line-φ' i.e. only on
    θ_line - φ mod π and the fixed difference φ'-φ mod π, we may translate coordinates so φ=0,
    φ'=β (this uses only that translating θ_line, φ, φ' simultaneously by a constant preserves
    both the separation relation and the uniform measure). With φ=0, φ'=β, β∈[0,π]: 0 lies in
    H_1=(θ_line,θ_line+π) mod 2π iff θ_line∈(-π,0) mod 2π iff θ_line∈(0,π) is false and
    θ_line=0 boundary — concretely, checking directly: for θ_line∈(0,β), one has β∈(θ_line,
    θ_line+π) [since θ_line<β<θ_line+π as β≤π<θ_line+π] while 0∉(θ_line,θ_line+π) mod 2π
    [since (θ_line,θ_line+π)⊂(0,2π) does not contain 0 for θ_line∈(0,β)⊂(0,π)] — so exactly one
    of {0,β} is in H_1: separated. For θ_line∈(β,π), both 0 and β fail to lie in
    (θ_line,θ_line+π) mod 2π [0 excluded as before since θ_line>0; β excluded because
    β<θ_line]: not separated. Hence separated exactly for θ_line∈(0,β), a set of measure β out
    of total measure π, giving P(separates)=β/π. (Verified by direct substitution for sample
    values β=π/2, π/3 in out/code/approach_d2_check.py, matching this derivation exactly.)

19. **Combinatorial identity.** Let y_1,...,y_N (N=4) be the doubled images of ℓ_1,...,ℓ_4.
    For a fixed θ_line, let a(θ_line) = #{i : y_i ∈ H_1(θ_line)} (a.e.-defined, ties measure
    zero in θ_line since there are finitely many points). The number of pairs {i,j} separated by
    this θ_line is exactly a(θ_line)·(N-a(θ_line)) (each of the a points pairs with each of the
    N-a others). By Step 18 and linearity of expectation over the uniform θ_line∈[0,π):
        Σ_{i<j} ang(y_i,y_j) = Σ_{i<j} π·P(separates ij) = π·E_θ_line[a(θ_line)(N-a(θ_line))].

20. **Integer maximization.** For any integer a∈{0,1,...,N}, a(N-a) ≤ ⌊N/2⌋⌈N/2⌉. Proof: the
    real function f(a)=a(N-a)=-(a-N/2)²+N²/4 is maximized over reals at a=N/2 and is symmetric
    and strictly decreasing in |a-N/2|; among integers the values closest to N/2 are ⌊N/2⌋ and
    ⌈N/2⌉ (equal if N even), giving the stated maximum ⌊N/2⌋⌈N/2⌉. For N=4 this value is
    2·2=4.

21. **Conclusion for d=2.** By Steps 19–20 (with N=4):
        Σ_{i<j} ang(y_i,y_j) = π·E[a(N-a)] ≤ π·max_a a(N-a) = π·4 = 4π.
    By Step 17, ang(y_i,y_j)=2θ_ij exactly, so Σ_{i<j} 2θ_ij ≤ 4π, i.e.
        S = Σ_{i<j} θ_ij ≤ 2π = (C(4,2)-2)·π/2.
    This holds for *every* configuration of 4 lines in R^2, including all degenerate cases
    (coincident lines, lines at any angles), since Steps 17–20 made no genericity assumption
    beyond finitely many points on a circle (ties are measure-zero events in θ_line and do not
    affect the expectation). ∎ (for d=2)

## Equality case (d=2)

22. Equality S=2π requires equality throughout: a(θ_line)(N-a(θ_line)) = 4 for (Lebesgue-)almost
    every θ_line, i.e. the two doubled points... this refinement (full characterization of all
    equality configurations) was not pursued in detail; the known example (2 axes, each doubled)
    achieves a(θ_line)∈{2,2} for a.e. θ_line by direct check (its two doubled image points are
    antipodal on S^1, each with multiplicity 2, so every line θ_line not through either image
    point splits the 4 points 2-2). **[GAP: full converse/equality characterization for d=2 not
    completed; only sufficiency of the conjectured extremizer is verified, not necessity/
    uniqueness.]**

## Summary of what is established

- Steps 1–3: a general-d structural lemma (Gram matrix / eigenvalue moment bound), correct for
  all d≥2, but demonstrably insufficient alone (Part II).
- Steps 4–8 (Approach A) and 9–15 (Approach B): two distinct, fully worked general-d attempts,
  each blocked at a precisely identified point — reported as GAPs, not asserted.
- Steps 16–21: a complete, unconditional proof of the exact target statement for d=2 (the N=4
  instance), with no numerical approximation load-bearing on the proof (Step 18's numeric
  sample values in the code are illustrative cross-checks only, not part of the logical chain).
- General d≥3: **not proved**; this is the acknowledged gap.
