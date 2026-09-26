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
