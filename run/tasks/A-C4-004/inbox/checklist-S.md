# Checklist A-C4

## Part S (specific; referees and the gate only, NEVER shown to blind agents)
- S1 Exact statement: BOTH (a) every 5 lines through the origin of R^3 have S <= 4 pi, and (b) every 6 lines through the
     origin of R^4 have S <= 13 pi/2; repetitions allowed; theta = arccos|<x,x'>| in [0, pi/2]. SOLVED needs both.
     (source: target.md, statement)
- S2 Equality configurations where any valid proof must be tight (a step strict at one of these is wrong):
     - (a) the axes with two repeated, e1,e1,e2,e2,e3: S = 4 pi (source: statement, Setting example k = 2);
     - (b) the axes with two repeated, e1,e1,e2,e2,e3,e4: S = 13 pi/2 (source: statement);
     - NON-orthogonal extremisers (head's arithmetic, verified with python-flint arb, residue < 3e-14):
       (a) three lines in the xy-plane pairwise at 60 degrees plus the z-axis twice: S = 4 pi;
       (b) three lines pairwise at 60 degrees in the (x1,x2)-plane plus three pairwise at 60 degrees in the (x3,x4)-plane:
       S = 13 pi/2. More generally, extremisers of lower cells glued along orthogonal subspaces stay extremal, so the
       maximisers form continuous families, not isolated points.
- S3 Cases to cover: both instances; repetitions allowed (coinciding lines, theta = 0); lines spanning a proper subspace;
     lines, not vectors (signs irrelevant). (source: statement, problem skill §8)
- S4 Known traps:
     - (head's arithmetic) averaging the gated A-C3 bound over all (d+1)-subsets is INSUFFICIENT: it gives S <= 25 pi/6
       for (a) and S <= 27 pi/4 for (b), both above the targets, so a proof needs more than subset averaging;
     - (team note, checked) arcsin t >= (pi/2) t^2 is false near t = 1 (t = 0.9), so a Frobenius / sum of squared
       inner products route with a pointwise quadratic bound fails for nearly coincident pairs;
     - (computer-assisted routes) the maximum is ATTAINED on continuous families (S2), so an interval branch-and-bound
       cannot close boxes around maximisers by a strict margin; it needs a written local argument there. The parameter
       space and every symmetry reduction must be written out, arithmetic must be interval/exact, runtime < 10 min.
       Floating-point search is evidence only.
- S5 Consistency with gated cells: A-C3 (VALID): any d+1 lines in R^d have S <= (C(d+1,2) - 1) pi/2, so every 4-subset
     in (a) has S <= 5 pi/2 and every 5-subset in (b) has S <= 9 pi/2; A-C1 and A-C2 (VALID). C4 is C5 at d = 3, 4, and
     C6 with k = 2 (M(d+2, d) = 2). (source: gated cells, problem skill §11)
- S6 Checkable instances: the four S2 configurations (S equals the bound); random configurations must stay below the
     bound (evidence only).
