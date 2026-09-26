# Where H-C5-007 stops

Strongest PROVED unconditional lower bound: U(Q_9) >= 2312 (unchanged from H-C5-002; edge counting gives
|S_f| >= 225). New but conditional-on-shape results: every induced forest of Q_9 missing at most 3 vertices of
one parity class has <= 279 vertices, so every labelling whose S_f = {down >= 2} has <= 3 vertices of one
parity has >= 2376 uphill paths (proof.md Steps 8-10). Any labelling with <= 2368 paths must therefore have
>= 4 vertices of EACH parity in S_f.

Exact failing rung: R9 (proof.md Step 11):
   for every induced forest F of Q_9 with z = |O \ F| <= |E \ F|:  tau(G_2[F n E]) <= z + 2,
where G_2[M] joins words of M at distance 2 and tau is the vertex-cover number. With inequality (2)
(|F| <= 277 + tau - z, proved for all forests via the code bound N <= 21) R9 gives F_9 <= 279, hence
U(Q_9) >= 2376 >= 2369.

Why the attempt fails: the only handle on tau is the clique cover (3), tau <= sum_{o in Z}(t_o - 1), with
Lemma 2 (z >= 1 + (t_o-1)(t_o-2)/2) limiting t_o. This closes z <= 3 only. For z >= 4 the cliques K_o = N(o) n M
overlap (Lemma 2's forced Z-vertices o + e_i + e_j share two M-neighbours with o) and (3) overcounts; for
z >= 29 a single o may have t_o = 9. The range 4 <= z <= 116 (z <= 116 forced by |F| >= 280 and the normalisation)
is open here.

What would be needed (either):
 (a) a charging argument showing each Z-vertex "pays" for at most one cover vertex beyond 2 in total
     (e.g. |M_K| <= |Z_K| + 1 for components K of Q_9[M u Z] of bounded size, plus a separate argument when a
     component is large; note the naive statement |M_K| <= |Z_K| + 1 for ALL components is FALSE in general
     (F = E u {u,v}, u,v odd at distance >= 4, gives one component with |M_K| = |Z_K| + 2), so the
     normalisation z <= |E \ F| or a size restriction is essential);
 (b) an exhaustive computation: e.g. SAT/CEGAR over 512 variables "Q_9 has an induced forest with >= 280
     vertices" with symmetry breaking and cycle clauses, or an enumeration over Z-configurations up to the
     hyperoctahedral group for small z combined with a global LP (Delsarte-type, on the pair (M, Z)) for large z.
Neither was completed within the 60-minute time box. The rung failed once (attempt 1, structural); a second
(computational) attempt was not run, so the stopping reason is the time box, not "failed twice".
