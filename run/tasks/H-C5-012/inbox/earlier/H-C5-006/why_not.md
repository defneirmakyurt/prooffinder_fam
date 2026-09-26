# Why H-C5 is not solved here (H-C5-006, Phase 3 analyst)

## Where the obstruction is
Both routes are governed by the decycling number of Q_9 (H-C5-002 Step 8, restated in out/proof.md):
  512 + 8 nabla(Q_9) <= U(Q_9) <= 512 + 8 * 236 = 2400,
and, per labelling, P(f) = 512 + 8|S_f| + extra(f), extra(f) = sum_{u in S_f}(N(u)-2)up_S(u) >= 0.
* UPPER (<= 2399) needs a decycling set of size <= 235, i.e. nabla(Q_9) <= 235. Literature: the best known
  upper bound is 236 = 2^8 - A(9,4) (Pike 2003; Hertz 2021 Table 4, opened). By Pike's characterisation
  (reproduced as out/proof.md Lemma I + I8), nabla(Q_9) <= 235 holds iff Q_9 has a minimum decycling set that
  is NOT independent. Nobody (in the sources found) has exhibited one; no source claims nabla(Q_9) = 236 either.
* LOWER (>= 2369) needs, e.g., nabla(Q_9) >= 233. Literature: lower bound 225 (counting; Hertz Table 4
  attributes 225 to Pike) or 226 (Pike's kappa + eps >= n+1 as reported in Wodlinger's thesis). The organisers'
  2368 = 512 + 8*232 points to an unpublished nabla(Q_9) >= 232 (UNSURE). The gap 225/226 .. 236 has been open
  since 2003 in every source I could open.
So the cell, by either route, is at least as hard as improving a 20-year-old bound on nabla(Q_9) (UPPER: by
one, from 236 to 235; LOWER: from 226 to 233, or reproducing the organisers' 232 and adding a labelling-level
argument, see J6).

## Approaches that fail, and why
1. Parity constructions (S inside one colour class). Fail for UPPER: by Lemma I, every independent decycling
   set has size 2^8 - |C| with C a distance-4 code, so >= 256 - A(9,4) = 236 (A(9,4) = 20 cited). Any
   improvement must put an edge inside S.
2. Parity + a few odd vertices removed (S = (X \ M) u Z): |S| = 256 - (|M| - |Z|); need |M| - |Z| >= 21 with
   Q_9[M u (Y \ Z)] acyclic. The H-C5-002 SA found only |M| = 22, |Z| = 2 (net 20). Counting alone allows up to
   31 (8|M| <= 255 + 8|Z| from e(F) <= |F| - 1), so counting does not exclude it; nothing better was found.
3. Generic local search for large induced forests: H-C5-002 (7 SA runs, growth-with-eviction moves) and this
   task (fixed-size penalty SA at |F| = 277, 3 runs; see claims.md RAN lines) found no 277-vertex induced
   forest; the same code finds the optima 18/36/72/144 for d = 5..8 and 276 for d = 9 quickly (sanity run).
   Hertz 2021 ran only the independent-set-restricted CliqueSearch on Q_9 (which cannot beat 236 by Lemma I).
4. Symmetric exact search (this task, out/code/sym_cegar.py: forests invariant under coordinate cycling C9,
   SAT + lazy cycle clauses): even the sanity target |F| = 276 TIMED OUT after 120 s (37 CEGAR rounds, 6731
   cycle clauses; the sequential-counter cardinality over 512 inputs makes each SAT call slow). A symmetric
   solution is only a special case, and UNSAT for a group would prove nothing about non-symmetric forests.
   A better encoding (weighted PB constraint over orbits, or an ILP with lazy cycle cuts) is needed.
5. LOWER via counting: 8|S| = 1792 + c(F) + e(S) gives only c + e(S) >= 1 -> 225. Needs c + e(S) >= 72.
6. LOWER via halving / subcube averaging: with H_0, H_1 the two Q_8 halves, |S| = s_0 + s_1 >= 2*112 = 224;
   combining with the identity in each half reproduces exactly the global identity (tautology, H-C5-002 stuck.md).
   Averaging over all Q_k subcubes gives 2^{9-k} nabla(Q_k) = 224 for k <= 8.
7. LOWER via spectral bounds: Gunderson-Meagher-Morris-Pantangi Thm 1.4 gives |F| <= about 313 for Q_9
   (weaker than counting's 287). Hoffman-type bounds see only the colour classes.
8. LOWER via the square rule alone (every 4-cycle meets S; out/proof.md I1): each vertex is on 36 squares and
   there are 36*128 squares, so only |S| >= 128.
9. LOWER via labelling structure without nabla: extra(f) >= 0 is all one can say in general; J3 shows extra is
   positive only when S has edges with "light" lower endpoints, so it cannot lift a nabla bound by more than the
   structure of S allows. By J4, zero-extra labellings with S not independent force a vertex u in S with
   1 <= deg_F(u) <= 2 and >= 7 upper S-neighbours.

## Why each failing branch fails (summary)
* Upper-route constructions are all capped by A(9,4) = 20 as long as S is independent (Lemma I). Non-independent
  S costs e(S) in the identity 8|S| = 1792 + c + e(S), so each S-edge must be paid for by merging forest
  components (c must drop below 96 - e(S) - 8), and each S-edge also costs labelling extra unless clustered (J5).
* Lower-route arguments that are "local and averaged" (counting, subcubes, squares, spectra) cannot see the
  interaction between the Q_8 halves beyond the identity; a proof must use the STRUCTURE of near-optimal forests
  of Q_8 (or Q_7), or an exhaustive computation with heavy symmetry breaking.

## What the next person needs to start
1. Primary sources: Pike 2003 (Graphs Combin. 19:547-550, DOI 10.1007/s00373-003-0529-9) full text, to see
   whether it contains any structure of non-independent decycling sets or a table for n = 9 (its lower bound
   for n = 9 is reported inconsistently: 225 in Hertz, 226 from Wodlinger's formula). Bau et al. (Utilitas) for
   the "elaborate proof" of 225 <= nabla(Q_9) <= 237.
2. UPPER: search for an induced forest of Q_9 with 277 vertices whose complement has edges. Suggested moves:
   Hertz's LargeForest with both k_X, k_Y free (not run on Q_9 in his paper); exact search over forests invariant
   under larger groups (e.g. subgroups of Aut(Q_9) fixing a good 20-word code, or translations by an even vector
   of weight >= 4 combined with coordinate permutations); ILP with lazy cycle constraints. Then order S so that
   J5's budget 1887 - 8|S| holds (lower ends of S-edges should have >= 7 upper S-neighbours).
3. LOWER: a proof of nabla(Q_9) >= 233 (equivalently c(F) + e(S) >= 72 for every induced forest F of Q_9).
   Plausible plan: classify induced forests of Q_8 with |S n H| <= 112 + t for small t (t <= 8) up to
   Aut(Q_8) (size 2^8 * 8! = 10,321,920), recording component structure; then show that two halves with
   s_0 + s_1 <= 232 cannot be glued: the matching edges between F_0 and F_1 at the positions F_0 n F_1 must form a
   forest on the component graph (bipartite multigraph on comp(F_0) u comp(F_1)), which is much stronger than the
   counting |F_0 n F_1| <= c_0 + c_1 - 1 that only reproduces 225. Alternatively, (8-neighbour) bootstrap
   percolation formulation: nabla(Q_9) = min percolating set of threshold 8 on Q_9 (Dreyer-Roberts, via
   Wodlinger Sect. 2), amenable to SAT with time-indexed encodings.
4. Lemma I, J and the reductions (J5, J6) are written in out/proof.md; checks in out/code/.
