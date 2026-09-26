# Plan: H-C5-011 (EXPLOIT / REPAIR of H-C5-007, rung R9)

Notation as in subject proof.md: F induced forest of Q_9, M = F n E, Z = O \ F, z = |Z|, a = |E \ F|,
normalisation z <= a (parity swap). tau = vertex cover number of G_2[M] (distance-2 graph).

Ladder (start 14:33):
 R1  Inherited (subject Steps 3-9): parity swap; Lemma 1; Lemma 2; code bound alpha(G_2[M]) <= 21;
     |F| <= 277 + tau - z; R9 holds for z <= 3.                         status: PROVED in subject (re-used)
 R2  Sanity test of R9 on concrete large induced forests found by local search
     (compute z, a, tau exactly). If some induced forest violates tau <= z + 2 with z <= a, R9 is REFUTED
     as stated (F_9 <= 279 may still hold).                                depends: none (computation)
 R3  Search for an induced forest of Q_9 with >= 280 vertices (would refute F_9 <= 279, so the Lemma-A
     route to 2369 is dead).                                               depends: none
 R4  Structural lemmas for z >= 4 (charging / clique overlaps): e.g. tau <= z + 2 for z = 4, 5.
                                                                            depends: R1
 R5  Largest z-range closed; exact statement of what remains.             depends: R1, R4
 R6  Target: F_9 <= 279, hence U(Q_9) >= 2376 (via Lemma A).               depends: R5 over all z <= 116

Status (updated as work proceeds): see bottom.

## Revised ladder and status (15:02)
 R1  Inherited: parity swap, Lemma 1, code bound <= 21, inequality (2) |F| <= 277 + tau - z.
                                                             PROVED (re-proved in proof.md Steps 2-5)
 R2  Sanity test of R9 on SA forests.                        DONE, exploratory: SA only finds 276-forests, all
     with one parity missing 0 or 1 vertex (covered by R6); tau via MaxSAT not run to completion (not needed).
 R3  Search for a 280-forest.                                NOT FOUND (3 SA runs, best 276); exploratory only.
 R4  Cluster decomposition: tau(G_2[M]) <= sum_C tau(G_2[M_C]) over clusters C of Z (components of the
     distance-2 graph on Z).                                 PROVED (proof.md Steps 8-9)
 R5  Local validity: M_C is C-valid, so tau(G_2[M_C]) <= tau*(C), tau* depends only on C and is invariant
     under parity-preserving automorphisms.                  PROVED (Steps 10-11)          uses R4
 R6  tau*(C) <= |C| for every connected C with |C| <= 5.     CHECKED (Step 12, cluster_tau.py, 1+1+2+8+31
     classes, 2.5 min)                                                                      uses R5
 R6' same for |C| = 6.                                       GAP: run killed/timed out at 19/268 classes, 0 violations
 R7  R9 (indeed tau <= z) for z <= 5; |F| <= 277 when min(|O\F|,|E\F|) <= 5; labelling corollary >= 2392.
                                                             PROVED (Steps 13-14)         uses R1, R4-R6
 R8  R9 for 6 <= z <= 116.                                   GAP (Step 15; stuck.md)
 R9  Target F_9 <= 279 / U(Q_9) >= 2369.                     GAP (needs R8)
