# Plan for A-C5-001

Target: for every d>=2, any N=d+2 lines in R^d satisfy S <= (C(d+2,2)-2)*pi/2.

## Ladder

R1. **Reduction identity (all d).** arccos(x)+arcsin(x)=pi/2 for x in [-1,1] (standard calculus
    fact). Consequently, writing a_ij=<x_i,x_j> for chosen unit-vector representatives of lines
    l_i, l_j, and T := sum_{i<j} arcsin|a_ij|, we get
        S = C(N,2)*pi/2 - T,
    so the target inequality S <= (C(N,2)-2)*pi/2 is EXACTLY equivalent to T >= pi.
    Status: PROVED (elementary calculus identity + algebra).
    Depends on: nothing.

R2. **Gram matrix rank bound (all d, all N).** For any N unit vectors in R^d, the Gram matrix
    G=(a_ij) (a_ii=1) is symmetric PSD with rank(G) <= d, trace(G)=N, and
        sum_{i<j} a_ij^2 >= N(N-d)/(2d).
    Proved via Cauchy-Schwarz on the (<=d) nonzero eigenvalues of G.
    Status: PROVED.
    Depends on: nothing (standard linear algebra: PSD-ness of X^T X, Cauchy-Schwarz).

R3. **General weak lower bound on T (all d>=2).** Using arcsin(x) >= x >= x^2 for x in [0,1]
    together with R2 (N=d+2 so N(N-d)/(2d) = (d+2)/d):
        T >= (d+2)/d = 1 + 2/d.
    Status: PROVED, but numerically NEVER reaches pi (since (d+2)/d <= 2 < pi for all d>=2), so
    it does not by itself prove the target for any d. Kept as an honestly-weaker general result.
    Depends on: R2.

R4. **Exact case d=2 (N=4 lines in R^2).** Represent each line by an angle phi in R/(pi Z);
    circular distance h(x)=min(x,pi-x) on a circle of circumference pi gives theta_ij exactly.
    Sorting the 4 angles cyclically into gaps g1,g2,g3,g4 >=0 summing to pi, S becomes an
    explicit function F(g)= h(g1)+h(g2)+h(g3)+h(g4)+h(g1+g2)+h(g2+g3). Case split on whether some
    g_i > pi/2 (at most one can be, since the others are nonnegative and sum to pi) shows F <= 2*pi
    always (Case A: all g_i<=pi/2 gives adjacent sum exactly pi, plus each opposite term <=pi/2;
    Case B: exactly one g_i>pi/2 gives adjacent sum = 2pi-2g_k < pi, total < 2pi). Hence for d=2,
    S <= (C(4,2)-2)*pi/2 = 2*pi exactly, matching the target with equality attained (e.g. two
    doubled orthogonal axes, or 4 evenly spaced lines).
    Status: PROVED (complete, elementary, exact).
    Depends on: definitions only (R1 not even needed, this is a direct argument on S itself).
    Sanity-checked by exact-rational exhaustive grid, out/code/check_d2.py (not load-bearing).

R5. **General d>=3: target inequality T>=pi.** Attempted via (a) averaging Lemma-B-type
    (d+1)-subset bounds over all N=d+2 deletions - shown algebraically to only give
    T >= (d+2)/(2d)*pi, weaker than pi for d>=3; (b) sharper "vertex" extremal-principle bound
    using convexity structure of arcsin(sqrt(t)) - gives T >= pi/2 + arcsin(sqrt(2/d)), matching
    pi exactly at d=2 but still short of pi for d>=3 (e.g. d=3: ~2.53 < pi), and this refined bound
    would itself need an additional un-derived extremal-principle lemma to be made fully rigorous.
    Status: GAP. Neither approach closes the case d>=3.
    Depends on: R2, R3.

R6. **Target (d>=2 combined).** S <= (C(d+2,2)-2)*pi/2.
    Status: PROVED for d=2 (via R4); PARTIAL (only the weaker R3 bound proved) for d>=3.
    Depends on: R1, R3, R4, R5.
