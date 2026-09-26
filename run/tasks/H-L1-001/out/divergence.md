# Divergence: H-L1-001 (literature, Phase 1L)

There are no Phase 1 blind results for H-L1 (promoted lemma; inbox/earlier/ is empty by design), so
there is no blind proof to compare with. The comparison below is between (i) the literature,
(ii) the earlier literature-agent proof inbox/earlier-proof.md (task H-C1-006, d = 3, 4 plus a closing
Remark for general d), and (iii) this run. The blind runs H-C1-003 / H-C1-004 are known here only
through inbox/earlier-divergence.md (second-hand) and nothing from them is used.

## 1. Contradictions

None. The earlier proof, its Remark, and this run agree: U(Q_d) >= d*2^(d-1)+2 for d >= 3, with the
bound attained at d = 3, 4. The literature (as far as it could be searched; no page could be opened)
states nothing about U(Q_d), so there is nothing to contradict.

## 2. Provenance of each idea

| idea | origin |
|---|---|
| Recurrence N(v) = [valley] + sum over lower neighbours N(w); N(v) >= 1 | standard; also in the earlier proof (Steps 2-3) and, per earlier-divergence.md, independently in both blind C1 runs. Re-proved here (Steps 3-4) |
| Bound U(G) >= |E|+1 for every simple graph (one uphill path "ending at" each edge, plus the valley at label 1) | **literature**: IMO 2022 P6 official lower bound (Bajnok's report, grid case) and Grozev's blog (general graphs), both second-hand in this run (not opened). Proved here in full (Steps 1-6) |
| Exact identity P = |Val| + sum N(v) up(v), and the excess form P-(|E|+1) = (|Val|-1) + sum (N-1) up | earlier proof Step 4 has the identity; the excess form written as a sum of two non-negative terms is a presentational simplification made here (Step 6) |
| Equality P = |E|+1 forces a unique valley and "each edge ends exactly one uphill path" | **literature** (IMO 2022 P6 solution, grid case, second-hand) |
| Translation of equality into down(v) = 1 for every non-valley non-maximum and the count |E| = n-1-m + sum_{up=0} deg | **earlier proof** (Step 6 there); re-proved here (Step 7) |
| Divisibility obstruction (d-1)m = 2^(d-1)(d-2)+1 | **earlier proof** (Step 7 there, d = 3, 4) and its Remark (all d) |
| Reduction to k | 2^k - 1 with k = d-1, via the explicit identity 2^(d-1)-1 = (d-1)(2^(d-1)-m) | Remark of the earlier proof (as a congruence); explicit identity written here |
| k >= 2 never divides 2^k - 1 | classical (earlier Remark sketches the least-prime / order argument using Fermat implicitly). **Proof here avoids Fermat's little theorem**: order <= p-1 by pigeonhole, order | k by the division algorithm, then minimality of p (Step 8) |
| Everything for general d >= 3 written line by line (Steps 9-11) | **new in this run** relative to the earlier proof, which proved only d = 3, 4 and sketched the rest |

## 3. Where the approaches differ

* The earlier proof proves N(v) >= 1 by strong induction on the label (as here). Grozev's blog
  (second-hand) uses a downhill walk; that route needs a termination argument (labels strictly
  decrease), which the induction avoids.
* The earlier proof handled d = 3, 4 by direct parity / mod-3 checks (2m = 5, 3m = 17). Here those two
  cases are not treated separately; they are the instances k = 2, 3 of Step 8.
* Computation: the earlier proof used exhaustive search over 8! labellings of Q_3 as confirmation and
  per earlier-divergence.md the blind runs proved the Q_4 lower bound by branch and bound. This run's
  proof uses no computation; out/code/sanity.py only sanity-checks the lemmas (identity, equality
  structure, finite ranges of the number-theoretic statement) and re-counts the earlier witnesses.

## 4. Status of the Remark's extension

Checked line by line (stuck.md): correct for every d >= 3; the only gaps were unwritten standard steps
(order divides p-1, n odd, the congruence manipulation), all now written out. d = 2 genuinely fails
(Q_2 has 16 labellings with P = |E|+1, sanity check D), matching the TARGET's exclusion of d = 1, 2.
