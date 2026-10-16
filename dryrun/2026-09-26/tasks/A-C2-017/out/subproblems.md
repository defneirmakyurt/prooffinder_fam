# Sub-problems: A-C2 (analyst, A-C2-017)

Cell status on arrival: PROVED on the board (gate VALID for A-C2-002, referees A-C2-005 and A-C2-006; matrix ROBUST, with
A-C2-011 also accepted by A-C2-014 and cross-confirmed by A-C2-016). The reduction below says which ingredients a complete
proof needs, and where each comes from.

Notation: c_i = <x_i, x_{i+1}>, phi_i = arcsin|c_i| in [0, pi/2].

S1. Reformulation. For t in [0,1], arccos t = pi/2 - arcsin t. Hence the target is equivalent to
    sum_{i=1}^{m-1} phi_i >= pi/2.
    Label (a): a standard identity. It is reproduced in proof.md Step 1 anyway, because it is two lines long.

S2. Dimension. Any m vectors in R^(m-1) are linearly dependent. Equivalently, the Gram matrix G = I + tridiag(c) is PSD
    and singular.
    Label (a): standard linear algebra (rank <= dimension).

S3. Chain recursion. If x_1..x_k are linearly independent, let t_k be the distance from x_k to span(x_1..x_{k-1}). Then
    t_{k+1}^2 = 1 - c_k^2 / t_k^2.
    This uses x_{k+1} ⊥ x_1..x_{k-1}. Equivalent forms: the continuant/minor recursion D_{k+1} = D_k - c_k^2 D_{k-1} with t_k^2 = D_k/D_{k-1}
    (A-C2-001, A-C2-010), and the Schur-complement / projection step from the other end (A-C2-002).
    Label (b): known in principle (the finite form of the chain-sequence / continued-fraction criterion of Wall–Wetzel for
    Jacobi matrices; sources not opened, UNSURE), so it is reproduced from first principles in proof.md Step 3.

S4. Trigonometric merge inequality. If B, p >= 0 and B + p < pi/2, then sin p <= cos B · sin(B + p).
    It follows from the identity cos B sin(B+p) - sin p = sin B cos(B+p).
    Label (b): elementary but not citable as stated (not found in the searches listed in sources.md). Reproduced in proof.md Step 4.
    Equivalent forms in the team's work: A-C2-002 Step 5, A-C2-011 Step 3, A-C2-015's sub-lemma.

S5. Assembly. By induction, t_k >= cos(phi_1 + ... + phi_{k-1}) as long as the partial sum is < pi/2. So if the full sum is < pi/2,
    then x_1..x_m are independent, which contradicts S2.
    Label (b): reproduced in proof.md Step 5 (credit: this forward Gram–Schmidt route is A-C2-003 / A-C2-015's).

No sub-problem is labelled (c). No part of the cell is unknown: every ingredient is elementary and written out in proof.md.

Neighbour (not part of this cell, for the A-C3 team): whether this lemma is the intended step for N = d+1 lines (cell 3)
is not established here. No source was found or opened that uses it for that case.
