# Stuck: H-C2-002

For the cell (U(Q_5)): none. Both halves are done (lower bound computer-assisted in one step,
proof.md Step 8; labelling out/Q5.txt, VERIFIED 88).

Residual risks for the head/referee:
1. Step 8 depends on out/code/decycle.py being a correct exhaustive search. Mitigations: reduction
   written out; run both with and without the edge-identity cut (both NONE); controls on Q_3, Q_4
   (known values reproduced) and Q_5 with k = 14 (FOUND, independently re-checked by is_decycling).
   A second, independent implementation (out/code/brute13.c: full enumeration of all 13-sets
   containing 0, edges-vs-components test, no edge cut) also finds none (2.4 s); its k = 14 control
   finds 945 sets.
2. No literature source could be opened (egress blocked), so nabla(Q_5) = 14 is not cross-checked
   against the literature.

Beyond the cell (neighbours): the method gives U(Q_d) = 2^d + (d-1) nabla(Q_d) whenever a minimum
decycling set of Q_d is independent. For d = 7, 8 it needs nabla(Q_7) >= 56, nabla(Q_8) >= 112
(Python search decycle.py 7 55 TIMED OUT at 590 s; a C version with the same cuts is the next step). For d = 9 it gives U(Q_9) >= 512 + 8 nabla(Q_9); to beat
2368 one needs nabla(Q_9) >= 233, and the Step 6 slack for non-independent decycling sets.
