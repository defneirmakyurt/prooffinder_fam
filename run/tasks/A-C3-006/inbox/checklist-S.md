# Checklist A-C3

## Part S (specific; referees and the gate only, NEVER shown to blind agents)
- S1 Exact statement: for EVERY integer d >= 1 and all lines l_1..l_{d+1} through the origin of R^d, repetitions allowed:
     S = sum_{i<j} theta(l_i,l_j) <= (C(d+1,2) - 1) * pi/2, theta = arccos|<x,x'>| (acute angle in [0,pi/2]).
     (source: target.md, statement)
- S2 Equality configurations where any valid proof must be tight (a step that is strict at one of these is wrong):
     - the conjectured optimum: the d coordinate axes with one of them used twice (exactly one coinciding pair, all other
       pairs orthogonal): S = (C(d+1,2) - 1) pi/2 (source: statement, Setting example with k = 1);
     - d = 1: any 2 lines in R^1 coincide, S = 0 = bound: equality for every configuration (head's arithmetic);
     - d = 2: S = pi = bound for EVERY triple of lines whose three gaps on the projective line (directions mod pi, total
       length pi) are each <= pi/2; this includes three lines pairwise at 60 degrees (3 * pi/3 = pi), a non-orthogonal
       extremiser, and two perpendicular lines plus a repeat (head's arithmetic, flagged by the team; checked numerically
       on 761 random triples with python-flint arb, residue < 2e-14). So the extremiser is NOT unique for d = 2.
     - d >= 3: other extremisers unknown.
- S3 Cases to cover (source: statement, problem skill §8, §11):
     - every d >= 1, including d = 1 and d = 2 (the d = 2 case has a whole family of extremisers, see S2);
     - repetitions allowed: coinciding lines (theta = 0), and the lines may span a proper subspace of R^d;
     - lines, not vectors: signs of spanning vectors are irrelevant; vector angles in [0, pi] prove something else;
     - any reduction to the gated lemma A-C2 must produce EXACTLY its hypotheses: unit vectors x_1..x_m in R^(m-1)
       (dimension m-1, not m) with exact orthogonality for |i-j| >= 2; the chain sum covers only consecutive pairs.
- S4 Known traps:
     - (problem skill §8) lines vs vectors; repetitions allowed; range d >= 1;
     - (team note, checked) the pointwise bound arcsin t >= (pi/2) t^2 is FALSE near t = 1 (t = 0.9: arcsin 0.9 = 1.1198
       < (pi/2)(0.81) = 1.2723), so a route through sum <x_i,x_j>^2 (Frobenius / frame-potential averaging) plus a
       pointwise quadratic bound fails for nearly coincident pairs unless those are handled separately;
     - floating-point checks are evidence only.
- S5 Consistency with gated cells (both gate VALID in the dry run, pins verified):
     - A-C1: for every N >= 0 and all lines in R^2, S <= (pi/2) floor(N^2/4). At N = 3 this gives pi, equal to C3's bound
       at d = 2, so C3 at d = 2 must agree with A-C1 at N = 3.
     - A-C2: for every m >= 2 and unit x_1..x_m in R^(m-1) with <x_i,x_j> = 0 for |i-j| >= 2,
       sum_{i=1}^{m-1} theta(x_i,x_{i+1}) <= (m-2) pi/2. A proof may use it only with its exact hypotheses (S3).
     - C3 is the k = 1 case of C6: M(d+1, d) = 1 (source: problem skill §11).
- S6 Checkable instances: the orthogonal-with-one-repeat value (C(d+1,2) - 1) pi/2 for small d; d = 1 (S = 0); the d = 2
     family in S2 (S = pi); random configurations must stay below the bound (evidence only).
