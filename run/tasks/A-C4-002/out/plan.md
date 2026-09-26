# Plan: A-C4-002 (BLIND, Phase 1)

TARGET: (a) any 5 lines through 0 in R^3 satisfy S <= 4*pi; (b) any 6 lines through 0 in R^4 satisfy S <= 13*pi/2.
(Repetitions allowed; theta = arccos|<x,x'>|.)

Notation: phi(x,y) = arcsin|<x,y>| = pi/2 - theta(x,y);  Phi = sum_{i<j} phi_ij;  S = C(N,2) pi/2 - Phi.
For N = d+2 the target is equivalent to  Phi >= pi.

Gated assumptions used: A-C1 (N=4 in R^2), A-C2 (chain lemma). A-C3 is NOT used.

## Ladder

- R1  Reformulation: S = C(N,2)pi/2 - Phi; target <=> Phi >= pi for N=d+2.            deps: none.   PROVED (proof.md S0)
- R2  Concavity: t -> arcsin(R cos(t-t0)) is concave on any interval where R cos(t-t0) >= 0 (0<R<=1).
                                                                                        deps: none.   PROVED (proof.md L1)
- R3  Path independence: if <y_i,y_j>=0 for |i-j|>=2 and <y_i,y_{i+1}> != 0, then y_2..y_m independent.
      Cor: a path component of n vertices spans dim >= n-1; a cycle component spans dim >= n-2.
                                                                                        deps: none.   PROVED (proof.md L2)
- R4  Graph fact: connected simple graph, max degree <= 2, n >= 2 vertices => path or cycle.
                                                                                        deps: none.   PROVED (proof.md L3)
- R5  Structural lemma: some maximiser X* has, for every k, either x_k orthogonal to all others, or
      the lines orthogonal to x_k span x_k^perp.  (Maximise #orthogonal pairs among maximisers; move one
      line along a great circle, F concave by R2, push to an endpoint.)               deps: R2.     PROVED (proof.md L4)
- R6  Path bound: n unit vectors with path-orthogonality in an (n-1)-dim space have sum of edge phi >= pi/2.
                                                                                        deps: A-C2.   PROVED (proof.md L5)
- R7  Cycle bound n=3,4: cycle-orthogonal vectors spanning dim n-2 have sum of edge phi >= pi.
                                                                                        deps: R6.     PROVED (proof.md L6)
- R8  5-cycle bound: y_1..y_5 in R^3, y_i perp y_{i+2}, edges non-orthogonal => sum phi >= pi.
      (Reduce to x2=(cos b, sin b cos A, sin b sin A); for fixed b the sum is concave in A with value pi
      at both ends A=0, A=pi/2.)                                                        deps: R2.     PROVED (proof.md L7)
- R9  6-cycle bound: y_1..y_6 in R^4, non-adjacent orthogonal, edges non-orthogonal => sum phi >= pi.
      (R^4 = span(y1,y2) (+) span(y4,y5); parameters alpha, beta, sigma; for fixed alpha, beta the sum
      is unimodal in sigma (log of the derivative-sign ratio strictly decreasing) with value pi at
      sigma=0, pi/2.)                                                                   deps: none.   PROVED (proof.md L8)
- R10 Main theorem: (a) d=3, then (b) d=4 (Case A uses A-C1 for d=3 and part (a) for d=4; Case B:
      non-orthogonality graph has max degree 2, deficiencies sum to 2, paths -> R6, cycles -> R7/R8/R9).
                                                                                        deps: R1-R9, A-C1, A-C2.  PROVED (proof.md S9)

## Status summary
All rungs PROVED. No step rests on computation. Numerical sanity checks (evidence only) are in out/code/.

## Dead ends explored
- Averaging A-C3 over 4-subsets (5 lines, R^3): gives S <= 25pi/6 > 4pi. Too weak.
- Frame-potential / arcsin >= t lower bounds: cannot be tight because the extremal configuration has
  |<x_i,x_j>| in {0,1}.
- Reducing the 6-cycle to the 5-cycle by projecting onto x1^perp: the three affected edge terms can only
  be bounded with phi12 + phi61 counted twice; loses too much.
- Concavity of the 6-cycle sum in sigma: true numerically but the second derivative is messy; replaced by
  a clean unimodality (quasi-concavity) argument.
