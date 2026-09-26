# Claims table (A-C5-001)

| # | Claim | Status | Where proved |
|---|-------|--------|--------------|
| 1 | arccos(x)+arcsin(x)=pi/2 for x in [-1,1] | PROVED | proof.md Step 1 |
| 2 | S = C(N,2)*pi/2 - T, where T=sum arcsin\|a_ij\|; target <=> T>=pi | PROVED | proof.md Step 2 |
| 3 | Gram matrix G=X^TX is symmetric PSD, rank(G)<=d | PROVED | proof.md Step 3 |
| 4 | trace(G)=N, trace(G^2)>=N^2/d (Cauchy-Schwarz on eigenvalues) | PROVED | proof.md Step 3, eq (5) |
| 5 | sum_{i<j} a_ij^2 >= N(N-d)/(2d); for N=d+2, >= (d+2)/d | PROVED | proof.md Step 3, eq (6)-(7) |
| 6 | arcsin(x) >= x^2 for x in [0,1] | PROVED | proof.md Step 4, eq (8) |
| 7 | T >= (d+2)/d for all d>=2 (weaker than target) | PROVED | proof.md Step 4, eq (9) |
| 8 | (d+2)/d < pi for all d>=2, so claim 7 does not reach target | PROVED (arithmetic) | proof.md Step 4, remark after (9') |
| 9 | theta(l,l')=h(alpha)=min(alpha,pi-alpha) for angle representative alpha in [0,pi) | PROVED | proof.md Step 5 |
| 10 | S=F(g_1,...,g_4) for the 4 cyclic gaps of 4 lines in R^2 | PROVED | proof.md Step 5, eq (10) |
| 11 | At most one gap g_i can exceed pi/2 | PROVED | proof.md Step 5, "Claim" paragraph |
| 12 | F<=2*pi always (Case A and Case B) | PROVED | proof.md Step 5, Case A/B |
| 13 | Target S<=(C(4,2)-2)*pi/2 = 2*pi for d=2 (all N=4 configurations) | PROVED | proof.md Step 5 (combines 9-12) |
| 14 | Equality attained by doubled-axes and by evenly-spaced 4-line configs (d=2) | PROVED / CHECKED | proof.md Step 5 end; out/code/check_d2.py |
| 15 | F<=2*pi holds on an exact rational grid of 39711 sample points (denom=60) | CHECKED | out/code/check_d2.py, RAN below |
| 16 | Target S<=(C(d+2,2)-2)*pi/2 for general d>=3 | GAP | proof.md Step 6 |
| 17 | Averaging a hypothetical corank-1 (N=d+1) lemma only gives T>=(d+2)/d*(pi/2), insufficient for d>=3 | PROVED (conditional arithmetic), lemma itself GAP | proof.md Step 6(a) |
| 18 | "Vertex" bound T>=pi/2+arcsin(sqrt(2/d)) insufficient for d>=3 and itself unproved rigorously | GAP | proof.md Step 6(b) |
