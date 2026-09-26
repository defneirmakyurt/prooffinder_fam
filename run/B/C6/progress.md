# B-C6 progress log: D_B(n) for every n (open question)

Every breakthrough reported by a worker is logged here as it arrives, with its status.
CLAIMED = the worker's claim, not yet refereed. PROVED = passed the gate (two referees).
Links point to the worker's proof document (out/proof.md, updated rung by rung).

## Established (gated)
- (Cell 2) D_B(T_k) = k^2 - k for every k.
- (Cell 3, gated 16:51, accepted/B-C3-007) D_B(n) <= k^2 - 2k - 1 for every non-triangular n of rank k >= 4; D_B(T_k - 1) = k^2 - 2k - 1 for k >= 4; D_B(2) = 0, D_B(5) = 3. So on each rank k >= 4 the open question is the exact value for r = 1, ..., k-2.

- (B-C6, gated 16:58, accepted/B-C6-004) LOWER BOUND for every n >= 1: D_B(n) >= F(n), F(1)=F(2)=0 and for n >= 3
  F(n) = max{ n-k+1 ; r(k+1)-2k if r >= 2 ; (k-1)(k-2-r) if k >= 4, r <= k-3 }, witnesses 1^n, delta_{k-1}+{r-1,1}, delta_{k-2}+{k-2,r+1}.
  With Cells 2 and 3: D_B = F exactly for n = T_k (all k >= 2) and n = T_k - 1 (all k >= 4).
- (COMPUTER-VERIFIED, pinned accepted/computation) D_B(n) = F(n) for every n <= 60, two independent exact programs.

## Claimed, awaiting referees

## Log
- [16:43] Cell 3 gated in full; its upper bound becomes an assumption for new C6 workers (B-C6-005 FRESH witness-family dispatched).
- [~16:45] CLAIMED (unrefereed, workers still running): all three blind provers (B-C6-002, 003, 004), independently, write the same general
  lower bound, for every n >= 3 with rank k and r = n - T_{k-1}:
      D_B(n) >= F(n) = max{ n-k+1 ;  (k+1)(r-2)+2 if r >= 2 ;  (k-1)(k-2-r) if k >= 4 and r <= k-3 },
  with three explicit witness families: (1^n); delta_{k-1} + parts {r-1, 1}; delta_{k-2} + parts {k-2, r+1} (notation as in each proof.md).
  Proof documents: run/tasks/B-C6-002/out/proof.md (Steps 11-28), B-C6-003/out/proof.md (Steps 2-5), B-C6-004/out/proof.md (sections 3-6).
- [~16:45] CHECKED by one worker (finite range; head re-ran n<=55 at ~16:48: 0 mismatches, 15 s): D_B(n) = F(n) for every 1 <= n <= 62 (B-C6-004 code/conj_check.py).
  So the conjecture D_B(n) = F(n) for all n is on the table; the upper half is OPEN (GAP in every proof).
- [16:47] Referees B-C6-006 (VERIFY) and B-C6-007 (GATE) dispatched on the lower bound of B-C6-004 (target run/B/C6/target_lower.md). Upper bound: repair prover B-C6-008 (from the gated Cell 3 method), literature B-C6-009.
- [16:52] CHECKED by head: B-C6-002's exhaustive program re-run, D_B(n) = F(n) for all n <= 60, 0 mismatches (40 s). Two independent
  exact programs (B-C6-002 conj_table.py, B-C6-004 conj_check.py) now agree on n <= 60; B-C6-003 reports n <= 66, the space map n <= 80.
- [16:52] LITERATURE (space map B-C6-001, sources not yet opened by a second agent): F(n) is Griggs-Ho 1998 Conjecture 4.7, open in all
  sources found. So the upper bound D_B(n) <= F(n) for all n is an open conjecture; our lower bound is a written-out proof of the witness side.
- [16:52] CLAIMED (unrefereed) by blind B-C6-003, structural: containment monotonicity (lambda in mu => B lambda in B mu); d_B = max(fill time,
  fit time); D_B quasi-convex on each block T_{k-1} <= n <= T_k; D_B(n) <= k^2 - k for every n of rank k. Proof: run/tasks/B-C6-003/out/proof.md
  Steps 7-8. Referees B-C6-011 (VERIFY) + B-C6-012 (GATE) dispatched (target run/B/C6/target_structure.md).
- [16:52] Upper bound attack: EXPLOIT B-C6-008 (gated Cell 3 method), FRESH B-C6-010 (fill/fit split, one-sided bounds), literature B-C6-009.
- [16:58] GATE VALID on the lower bound (B-C6-004, referees B-C6-006 VERIFY + B-C6-007 GATE, both ACCEPT). Pinned. Scribe B-C6-013 writing the PARTIAL LaTeX.
