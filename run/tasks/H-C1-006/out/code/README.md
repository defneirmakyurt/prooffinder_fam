# code (H-C1-006)

Stdlib-only, exact integer arithmetic. Run from this directory.

* `uphill.py <file> <d>` -- reads a labelling in the hand-in format (2^d lines of 0/1 strings,
  line i = the vertex with label i, leftmost character = coordinate d-1) and prints the number of
  uphill paths computed twice: by the recurrence of proof.md Step 2, and by explicitly enumerating
  every uphill path with a DFS from each valley. It asserts the two agree. Also prints the number
  of valleys and of local maxima.
* `q3_exhaustive.py [out]` -- iterates over all 8! = 40320 bijections V(Q_3) -> {1..8}
  (`itertools.permutations`), no symmetry reduction, prints the minimum and the value distribution,
  cross-checks the recurrence against the explicit enumeration on every 997th permutation and on the
  minimiser, and optionally writes the minimiser.
* `q4_upper.py <d> <target> [out]` -- seeded first-improvement transposition local search; a
  heuristic that only ever certifies an UPPER bound (the labelling it prints is then scored exactly
  by `uphill.py`). It proves nothing about optimality.
* `identity_check.py` -- checks the identities `total = #valleys + sum_v N(v)*up(v)` and
  `|E| = sum_v down(v)` and the consequence `total >= |E| + #valleys` on 2000 random labellings for
  each d = 2..5 and on all 8! labellings of Q_3.
