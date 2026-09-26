# Plan A-C2-015 (breaker, BLIND, Phase 2C ADVERSARY)

Reformulation used throughout: put a_i = |<x_i,x_{i+1}>|, phi_i = arcsin a_i = pi/2 - theta_i.
Target  <=>  sum_i phi_i >= pi/2 for every admissible chain (m vectors in R^(m-1)).

Rungs (dependencies in brackets):
- R1 (task 1, contrapositive) sum phi_i < pi/2  =>  x_1..x_m linearly independent. [none]  -- PROVED (out/proof.md)
- R2 smallest cases m=2, m=3 by hand (m=3: equality on whole curve a1^2+a2^2=1). [none] -- PROVED (special cases of R1; hand check in contrapositive.md)
- R3 (task 2) equal-weight chains a_i=a, all m<=60. [none] -- CHECKED
- R4 (task 2) random directions a in (0,1]^(m-1) scaled to singularity, m=2..12, 20000 each, seed 12345. -- CHECKED
- R5 (task 2) local minimisation of sum phi on the singular variety, m=3..10, 200 restarts each (Nelder-Mead), seed 777. -- CHECKED
- R6 (task 2) exact check of worst case (margin 0, m=3, a=(3/5,4/5)) and of R1 recursion on rational instances. -- CHECKED
- R7 (task 3) local analysis at equality configurations. [R1] -- PROVED (global, follows from R1) + numerically CHECKED
- R8 (task 4) minimal sub-lemma where naive arguments fail. [R1] -- written

Status as of end of run: all rungs as marked above.
