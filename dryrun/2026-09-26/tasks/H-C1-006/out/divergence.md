# Divergence: H-C1-006 (literature) vs the blind runs H-C1-003 and H-C1-004

## 1. The values agree

| | U(Q_3) | U(Q_4) |
|---|---|---|
| H-C1-003 (blind) | 14 | 34 |
| H-C1-004 (blind) | 14 | 34 |
| this run (literature) | 14 | 34 |
| literature | **no source found that states either value** (see out/sources.md, "Not found") |  |

No contradiction anywhere: three independent runs, three different code bases, same two integers.
The literature does not report these values, so there is nothing to contradict; what the literature
does supply is the general bound U(G) >= |E(G)| + 1 (Bajnok, arXiv:2509.19303, IMO 2022 P6 solution,
opened), which gives 13 and 33 -- consistent with, and one short of, the values all three runs give.

## 2. Where the approaches differ: the lower bound

This is the substantive divergence.

* **Both blind runs proved the lower bounds by exhaustive computer search.**
  H-C1-003: an exact prefix DP with state merging (`dp_lower.py 4 33 --no-fix`, 0.11 s) plus an
  independent branch and bound without merging (`bb_lower.py 4 33 --no-fix`, 1.32 s).
  H-C1-004: a depth-first branch and bound over all 16! bijections (`bnb.py 4 34 --nomemo`, 0.85 s).
  Both rest on an admissible bound LB(S) for partial labellings, which each proved carefully.
  Neither produced a human-readable reason why 34 rather than 33.
* **This run proves both lower bounds by hand, with no computation at all** (out/proof.md Steps 1-7).
  The route is: the exact identity P = #valleys + sum_v N(v)*up(v) (Step 4); hence P >= |E| + 1
  (Step 5, the known IMO bound); then an analysis of the equality case P = |E| + 1, which forces
  exactly one valley, N(v) = 1 whenever up(v) >= 1, and therefore down(v) = 1 for every vertex that
  is neither the valley nor a local maximum (Step 6); counting down-degrees then gives, for a
  d-regular graph on 2^d vertices, (d-1)m = 2^{d-1}(d-2) + 1 with m the number of local maxima.
  For d = 3 this is 2m = 5 and for d = 4 it is 3m = 17, neither solvable in integers (Step 7).
  So P = |E| + 1 is impossible and P >= |E| + 2 = 14, 34.

  Consequence: the blind exhaustive searches over 8! and 16! labellings are, for this cell, not
  needed. My only exhaustive run (all 8! labellings of Q_3) is a confirmation, not the proof, and I
  ran nothing exhaustive for Q_4.

  Second consequence, outside the cell: the same argument gives U(Q_d) >= d*2^{d-1} + 2 for **every**
  d >= 3 (proof.md Remark, using the classical fact that n | 2^n - 1 forces n = 1). Neither blind run
  claims anything for d >= 5; H-C1-003 and H-C1-004 both explicitly record that their method does not
  scale past d = 4. So this is a strict extension of what the blind runs establish, though it is far
  from the organisers' quoted 2368 <= U(Q_9).

## 3. Where the approaches agree

* The counting recurrence N(v) = [v valley] + sum over lower neighbours of N(w) was derived
  independently in all three runs, with essentially the same bijection proof
  (H-C1-003 claims.md "Recurrence"; H-C1-004 claims.md R2; here proof.md Step 2). Convergent.
* N(v) >= 1 for all v (H-C1-003 (i); H-C1-004 R2b; here Step 3). Convergent.
* Both blind runs' LB(S) contains, as its simplest ingredient, exactly the inequality
  N(x) >= max(1, P(x)) -- the same "each edge contributes at least 1" idea that underlies the
  literature's |E| + 1 bound. Neither blind run isolated the closed-form bound |E| + #valleys, and
  neither looked at the equality case; that is what the literature route supplies.
* The Q_3 artefact `000,001,010,011,101,110,100,111` came out identical in all three runs. This is
  convergence, not copying: it is simply the lexicographically first minimiser that
  `itertools.permutations` reaches, and all three brute forces scan in that order. My Q_4 artefact
  is a different labelling from the blind one (mine has 2 valleys and 6 local maxima; theirs is the
  one starting 0000, 0001, 0010, 0100, ...), and both score 34.
* The value distribution over all 8! labellings of Q_3 agrees term by term between H-C1-003 run 2,
  H-C1-004 run 2 and my run 2: `(14,7104), (16,14112), (17,6720), (18,4704), (19,576), (20,3648)`.
  Note 15 is absent in all three -- consistent with, but not implied by, Step 7.

## 4. Provenance of each idea

| idea | origin |
|---|---|
| counting recurrence for N(v) | independently in both blind runs and here; standard |
| N(v) >= 1 | independently in both blind runs and here |
| U(G) >= |E(G)| + 1 for every simple graph | **literature** (Bajnok arXiv:2509.19303, IMO 2022 P6 lower bound; Grozev's blog states it for arbitrary simple graphs). Re-proved in full here (Steps 1-5) because a citation is not a proof |
| equality P = |E| + 1 requires exactly one valley and each adjacent pair to be the last two cells of a unique uphill path | **literature** (Bajnok, same solution, stated for the grid as the target of his construction) |
| translating that equality condition into down(v) = 1 for all non-valley non-maximum v, and the count |E| = (n-1-m) + sum_{up(v)=0} deg(v) | **new here** -- not found in any source, and absent from both blind runs |
| the divisibility obstruction (d-1)m = 2^{d-1}(d-2) + 1, ruling out 13 and 33 | **new here** |
| U(Q_d) >= d*2^{d-1} + 2 for all d >= 3 | **new here**, outside the cell |
| exact DP / branch and bound with an admissible LB(S) over partial labellings | **blind runs** (H-C1-003, H-C1-004). Not used here |
| state merging on (placed set, N restricted to the boundary) | **blind run H-C1-003** (and H-C1-004's memo). Not used here |
| exhaustive enumeration of all 8! labellings of Q_3 | independently in both blind runs and here |

## 5. Contradictions found

None. No blind claim is contradicted by the literature or by this run, and no claim here is
contradicted by either blind run. The one place where a blind run is weaker than it could be is
that both present the lower bound as a purely computational fact; out/proof.md shows it is not.

Nothing from the blind proofs was copied into out/proof.md: Steps 1-8 are written from the
definitions in inbox/statement.md and the literature bound, and the code in out/code/ was written
here (different files, different algorithms -- no DP, no branch and bound).
