# Where the attempt stops (H-C5-002)

Both routes of the cell reduce (proof.md Step 8) to the decycling number nabla(Q_9) = minimum size of a vertex
set S whose removal leaves an induced forest:

  512 + 8 nabla(Q_9) <= U(Q_9) <= 2400.

## UPPER route (<= 2399): blocked at "find a decycling set of Q_9 of size <= 235"
* Necessary condition, proved: a labelling with <= 2399 paths has |S_f| <= 235, where S_f = {N >= 2} is a
  decycling set. So a hand-in would simultaneously beat the best upper bound on nabla(Q_9) I know of
  (236, from 2^8 - A(9,4) = 256 - 20; Pike 2003 [not opened] apparently characterises exactly when
  nabla(Q_n) = 2^{n-1} - A(n,4)).
* Not sufficient: a decycling set of size s must also be labellable with extra
  sum_{u in S}(N(u)-2)up(u) <= 1887 - 8s (extra = 0 automatically when S is independent; for non-independent
  S the lower endpoint of each S-edge must have N as small as possible).
* Search done: max-induced-forest simulated annealing on Q_9, 7 runs (RAN lines): 6 runs ended at |S| = 236,
  one low-temperature run (seed 21) at |S| = 238; never <= 235;
  also a labelling-level SA seeded with out/Q9.txt made no improvement in the time it ran (killed, no result
  file; reported as PARTIAL). The SA reaches the known optima 14, 28, 56, 112 for d = 5..8 in < 1 s.
* Observation for the next worker: the SA optima at d = 9 are NOT the parity construction. They are
  S = (E \ M) u Z with |M| = 22 even words kept in the forest and |Z| = 2 odd words removed (e(S) = 13,
  83 components). In this language (no loss of generality: M = F n E, Z = S n O), |S| = 256 - (|M| - |Z|),
  and the cell's upper route needs |M| - |Z| >= 21 such that O \ Z plus M induces a forest. Parity (Z empty)
  caps |M| at A(9,4) = 20. Counting alone allows |M| <= 31 + |Z|.

## LOWER route (>= 2369): blocked at "prove nabla(Q_9) >= 233" (or a finer statement)
* Sufficient, proved: nabla(Q_9) >= 233 gives U(Q_9) >= 2376.
* Alternative sufficient condition: nabla(Q_9) >= 232 AND every labelling with |S_f| = 232 has positive extra.
* What I have: only nabla(Q_9) >= 225 (edge counting, Step 9) -> U(Q_9) >= 2312. The published bound I could
  open is also 225 (Bau et al. 2000 via Bau's survey). The organisers' 2368 = 512 + 8*232 suggests they know
  nabla(Q_9) >= 232 by some unpublished argument (UNSURE).
* Why counting stalls: for an induced forest F = V \ S with c components, (d-1)|S| = (d-2)2^{d-1} + c + e(S),
  i.e. |S| = 224 + (c + e(S))/8 for d = 9. Any lower bound needs c + e(S) >= 65 (for |S| >= 233). Splitting
  Q_9 into two Q_8 halves only reproduces the same identity (m_F - m_S = 256 - s is a tautology), and subcube
  averaging with nabla(Q_k) = 2^{k-1} - A(k,4) for k <= 8 gives 2^{9-k} nabla(Q_k) = 224 for k = 7, 8, even
  weaker. A proof must use structure of near-optimal forests of Q_8 (e.g. that |S n half| close to 112 forces
  a parity-minus-extended-Hamming-code structure) or a computer search with symmetry breaking. Not attempted
  in the time box.

## GAPs in proof.md
* Step 11 (exact values for d <= 8) depends on nabla(Q_d) values cited from a survey; primary source not opened.
