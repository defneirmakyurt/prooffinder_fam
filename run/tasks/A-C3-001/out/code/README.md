# out/code

`sanity.py` — stdlib-only, floating point. EVIDENCE ONLY; no step of proof.md rests on it.

Run: `python3 sanity.py` (from this directory). Measured: real 5.81 s.

Checks:
1. closed form of h'' for h(t) = arcsin(r cos t) (Lemma 2) against central finite differences, 20000 random (r, t);
2. F(x) = sum_{i<j} arcsin|<x_i,x_j>| >= pi/2 on 5000 random configurations of d+1 unit vectors in R^d, d = 1..6;
3. crude local search minimising F (20 starts x 3000 moves per d, d = 1..6): minimum found stays >= pi/2;
4. concavity of g(t) = sum_j arcsin|<y(t),x_j>| between consecutive zeros along random great circles
   (second differences on a 4000-point grid), the situation of Lemma 4.
Seeded (random.seed(20260926)), so output is reproducible on the same Python.
