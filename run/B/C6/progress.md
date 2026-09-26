# B-C6 progress log: D_B(n) for every n (open question)

Every breakthrough reported by a worker is logged here as it arrives, with its status.
CLAIMED = the worker's claim, not yet refereed. PROVED = passed the gate (two referees).
Links point to the worker's proof document (out/proof.md, updated rung by rung).

## Established (gated)
- (Cell 2) D_B(T_k) = k^2 - k for every k.
- (Cell 3, gated 16:51, accepted/B-C3-007) D_B(n) <= k^2 - 2k - 1 for every non-triangular n of rank k >= 4; D_B(T_k - 1) = k^2 - 2k - 1 for k >= 4; D_B(2) = 0, D_B(5) = 3. So on each rank k >= 4 the open question is the exact value for r = 1, ..., k-2.

## Claimed, awaiting referees

## Log
- [16:52] Cell 3 gated in full; its upper bound becomes an assumption for new C6 workers (B-C6-005 FRESH witness-family dispatched).
- [16:58] CLAIMED (unrefereed, workers still running): all three blind provers (B-C6-002, 003, 004), independently, write the same general
  lower bound, for every n >= 3 with rank k and r = n - T_{k-1}:
      D_B(n) >= F(n) = max{ n-k+1 ;  (k+1)(r-2)+2 if r >= 2 ;  (k-1)(k-2-r) if k >= 4 and r <= k-3 },
  with three explicit witness families: (1^n); delta_{k-1} + parts {r-1, 1}; delta_{k-2} + parts {k-2, r+1} (notation as in each proof.md).
  Proof documents: run/tasks/B-C6-002/out/proof.md (Steps 11-28), B-C6-003/out/proof.md (Steps 2-5), B-C6-004/out/proof.md (sections 3-6).
- [16:58] CHECKED by one worker (finite range; head re-ran n<=55 at 17:03: 0 mismatches, 15 s): D_B(n) = F(n) for every 1 <= n <= 62 (B-C6-004 code/conj_check.py).
  So the conjecture D_B(n) = F(n) for all n is on the table; the upper half is OPEN (GAP in every proof).
- [17:03] Referees B-C6-006 (VERIFY) and B-C6-007 (GATE) dispatched on the lower bound of B-C6-004 (target run/B/C6/target_lower.md). Upper bound: repair prover B-C6-008 (from the gated Cell 3 method), literature B-C6-009.
