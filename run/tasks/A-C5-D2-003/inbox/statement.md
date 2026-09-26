# Problem A: Angles between lines — verbatim statement

How large can the sum of pairwise angles between N lines through the origin be? Fejes Tóth
conjectured in 1959 that orthogonal lines win.

**Definition (Lines and angles).** A *line* here always means a line through the origin of R^d.
The *angle* between two lines ℓ,ℓ' is the acute (non-obtuse) angle θ(ℓ,ℓ')∈[0,π/2] between them.
If ℓ,ℓ' are spanned by unit vectors x,x', then θ(ℓ,ℓ')=arccos|⟨x,x'⟩|.

**Definition (Angle sum).** For lines ℓ_1,...,ℓ_N in R^d (repetitions allowed), write
S(ℓ_1,...,ℓ_N) = Σ_{1≤i<j≤N} θ(ℓ_i,ℓ_j). The question is how large S can be.

**Conjecture (L. Fejes Tóth, 1959).** S is maximised by taking d mutually orthogonal lines,
each used either ⌊N/d⌋ or ⌈N/d⌉ times.

**Example.** When N=d+k with 0≤k≤d, that configuration (the d coordinate axes, k of them used
twice) has S=(C(N,2)-k)·π/2, because exactly k pairs of lines coincide and every other pair is
orthogonal.

Each cell asks you to prove this bound, or a special case of it. Unless a cell says otherwise, a
complete proof is required. Citing a published result for the statement you are asked to prove
does not count.

## Cell C5 (verbatim): d+2 Lines in R^d — 8 points

The case N=d+2 in every dimension, with the same conjectured optimum: the d coordinate axes, two
of them repeated. Prove that for every d≥2, any d+2 lines in R^d satisfy

    S ≤ (C(d+2,2) - 2) · π/2

## What to Hand In (official, verbatim)

For each cell you attempt, hand in a written proof. **Computation.** You may use a computer to
explore. A proof may rely on a computation only if you include the code, it runs in under 10
minutes on a laptop, and it is rigorous: exact or interval arithmetic, or an argument that bounds
the numerical error. **Status.** Say clearly which cells you consider solved and which are partial.

*(Scope note: this run attempts only Cell C5. Cells C1-C4 and C6 are not attempted here.)*
