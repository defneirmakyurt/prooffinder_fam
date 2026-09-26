# Proposals (ranked; the head decides)

P1 — S2 seqB-diagram — feeds: proof of (a) and upper half of (b).
  Task (prover): write a self-contained proof that d_B(lambda)<=k^2-2k-1 for k>=4, T_{k-1}<|lambda|<T_k, via the
  number-of-parts sequence and its window-sum/sandwich properties (Griggs-Ho Secs. 3-4 as the route; re-prove every lemma;
  k=4 by exhaustive check of 67 partitions with code). Assumes: C1 result (Brandt) as proved by board or re-proved.
  Output: LaTeX proof. Stop: proof complete, or a lemma whose GH proof has a gap (report it). Cost: medium.
  Ranks first: it is the only route with a known complete argument for (a); everything else depends on (a).

P2 — S1 diag-array (+S4 CRT) — feeds: construction for (b).
  Task (prover): prove d_B(lambda_k)=k^2-2k-1 for all k>=4, lambda_k=(k-1,k-2,k-2,k-3,...,2,1,1), by explicit array
  tracking (single drop at step k^2-2k-2). Output: lemma + checked table k=4..15. Stop: proof or break. Cost: low-medium.
  Ranks second: short, required, and GH only sketch it.

P3 — S5 reverse-tree — feeds: construction side of (c) (conjecture generation, then sufficiency).
  Task (searcher): enumerate E_k for k=5..11, confirm E_k = B^{-L_k}(mu_k), and find an explicit structural description
  (array conditions or reversed-word language) matching all k<=11. Output: conjectured description + agreement table.
  Stop: match found or 10 min runtime. Cost: low (compute). Ranks third: (c) cannot be proved before its answer is known.

P4 — S2 equality case — feeds: "no other partition" in (c).
  Task (prover): run the P1 argument with d_B=k^2-2k-1 and extract the forced seq_B pattern; show it forces B^{L_k}(lambda)=mu_k.
  Assumes: P1 done, P3 description. Output: necessity proof. Stop: proof or an extremizer escaping the forced pattern.
  Cost: high. Ranks fourth: depends on P1 and P3.

P5 — S3 containment-order — breaker/lemma.
  Task (breaker): give an explicit family lambda |- T_k-1, all one-cell extensions of depth k^2-k (k>=5), recording that the
  comparison route cannot prove (a). Cost: low. Payoff low; ranks last (documentation of a dead end).

Pairing: (b) bound P1 + construction P2 agree on k=4..9. (c) necessity P4 + sufficiency P3 agree on k=5..9 (E_k computed).
