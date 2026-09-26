# Plan: H-C5-008 (searcher, CONTRARIAN, UPPER route)

Target: a labelling of Q_9 with <= 2399 uphill paths (checker score), saved as out/Q9.txt.
By gated Lemma A this needs an induced forest T of Q_9 with |T| >= 277 (|S| <= 235).

Contrarian angle (not in the forbidden list): **translation-invariant forests via covering quotients.**
For a binary linear code C <= F_2^9 (dim r, no word of weight 1) the map Q_9 -> Q_9/C is a graph
covering onto the Cayley multigraph Cay(F_2^9/C, {e_i + C}). A C-invariant vertex set T is an induced
forest of Q_9 iff its image is an induced forest (no parallel pair, no cycle) of the quotient.
So C-invariant forests of Q_9 of size 2^r m <-> forests of size m in a 2^(9-r)-vertex 9-regular
multigraph. Classes: codes up to coordinate permutation (= up to Aut(Q_9) conjugation).
Size constraint: |T| in [277, 287] (counting bound) and 2^r | |T|: r=1 -> m >= 139 (256 vertices),
r=2 -> m >= 70 (128 v.), r=3 -> m = 35 (64 v.), r >= 4 impossible by counting.
Also: an exact "excess" analysis of Lemma A (which S-structures a <= 2399 labelling must have).

Ladder (dependencies in brackets):
- R1 checker sanity: verify.py on hand-checkable small cases and on a decoded Q_9 labelling. [none]
- R2 covering lemma (written proof): T = pi^{-1}(F) forest <-> F forest of quotient multigraph. [none]
- R3 counting: no C-invariant forest with |T| >= 277 for r >= 4; size targets per r. [R2]
- R4 code-class enumeration: codes up to permutation <-> column multisets up to GL(r,2); list classes r=1,2,3. [R2]
- R5 exact search r=3 (all classes, 64-vertex quotients, forest >= 35). [R4]
- R6 search r=2 (all classes, 128-vertex quotients, forest >= 70). [R4]
- R7 search r=1 (8 classes, 256-vertex quotients, forest >= 139). [R4]
- R8 decode best lifted forest to a labelling, score with checker; save out/Q9.txt if <= 2399. [R1, R5-R7]
- R9 Lemma-A excess structure: any labelling with <= 2399 and |S| = 235 has S = (maxima) + (down-2 vertices whose 7 up-neighbours are maxima) up to one exceptional vertex. [none]

Status (kept current):
- R1 NOT STARTED
- R2 NOT STARTED
- R3 NOT STARTED
- R4 NOT STARTED
- R5 NOT STARTED
- R6 NOT STARTED
- R7 NOT STARTED
- R8 NOT STARTED
- R9 NOT STARTED
