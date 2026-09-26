# Runlog: H-C1-003

PYTHON = /Users/raducucu/bainsahackathon/.venv/bin/python3 (all code is stdlib-only and also
runs under plain python3). All arithmetic is exact Python integers. Everything is deterministic
except the local search, which uses seeded `random.Random(seed)`.
All runtimes below were measured with `/usr/bin/time -p`.

## Hand computations used for run 1
* Q_2, order 00,01,10,11: N(00)=1, N(01)=1, N(10)=1, N(11)=N(01)+N(10)=2; total 5.
  (paths: (00), (00,01), (00,10), (00,01,11), (00,10,11))
* Q_2, order 00,01,11,10: N(00)=1, N(01)=1, N(11)=1, N(10)=N(00)+N(11)=2; total 5.
* Q_3, order 000,001,010,011,100,101,110,111: N = 1,1,1,2,1,2,2,6; total 16.

## Runs

1. Checker sanity. `verify.py out/tmp/q2_id.txt --d 2` -> `VERIFIED 5`;
   `verify.py out/tmp/q2_cyc.txt --d 2` -> `VERIFIED 5`;
   `verify.py out/tmp/q3_id.txt --d 3` -> `VERIFIED 16`. All three match the hand computation.
   COMPLETED, < 0.1 s each.

2. `python3 out/code/brute_q3.py out/Q3.txt` -- exhaustive over ALL 8! = 40320 permutations of
   V(Q_3), no symmetry reduction. COMPLETED, real 0.22 s. Output:
       labellings checked: 40320
       min uphill paths U(Q_3) = 14 attained by 7104 labellings
       value distribution (lowest 6): [(14, 7104), (16, 14112), (17, 6720), (18, 4704), (19, 576), (20, 3648)]
       wrote out/Q3.txt
   (The script also asserts that the explicit DFS enumeration of uphill paths agrees with the
   recurrence on the minimiser and on every 997th permutation.)

3. Local search for Q_4: `python3 out/code/search_q4.py 4 200 <seed> out/tmp/q4_s<seed>.txt`
   for seed = 1, 2, 3. 200 random restarts each, first-improvement transposition local search
   with 30 random kicks per restart. COMPLETED, real 11.27 / 11.27 / 11.28 s.
   Best found: 34, 34, 34 -- all three seeds, never below 34.
   Scored: `verify.py out/tmp/q4_s<seed>.txt --d 4` -> `VERIFIED 34` for each.
   (An earlier run of the same script, seed 1, produced out/tmp/q4_ls_seed1.txt, also 34.)

4. `python3 out/code/dp_lower.py 4 33 --no-prune` -- control: exact prefix DP with state merging
   but with the LB pruning switched off (only "running total <= 33" pruning left).
   TIMED OUT at 10 min (600 s), no output. Range actually covered: nothing concluded.
   Its purpose is covered instead by run 7.
   A second control, `bb_lower.py 4 33 --no-fix --basic` (branch and bound with the weakest
   bound sum_v A(v) only), also TIMED OUT at 7 min (420 s). Nothing concluded from it.

5. DP and branch-and-bound cross-checks on the cases where the answer is known independently:
   * `dp_lower.py 3 13`            -> "no labelling with label 1 at vertex 0 of Q_3 has at most
                                      13 uphill paths => U(Q_3) >= 14".  COMPLETED, real 0.02 s.
   * `dp_lower.py 3 14 out/tmp/q3_dp.txt` -> "found labelling with 14 uphill paths".
                                      COMPLETED, real 0.02 s.
   * `dp_lower.py 3 13 --no-prune --no-fix` -> "no labelling of Q_3 has at most 13 uphill paths".
                                      COMPLETED, real 0.03 s, 1532 states.
   * `bb_lower.py 2 4 --no-fix` -> NONE (=> U(Q_2) >= 5);  `bb_lower.py 2 5 --no-fix` -> FOUND 5.
   * `bb_lower.py 3 13 --no-fix` -> NONE (=> U(Q_3) >= 14), 1840 nodes, real 0.02 s;
     `bb_lower.py 3 14 --no-fix` -> FOUND 14, real 0.01 s.
   All agree with the exhaustive result of run 2.

6. Q_4 lower bound, program 1. `python3 out/code/dp_lower.py 4 33 --no-fix` -- exact prefix DP
   over ALL labellings of Q_4 (every one of the 16 vertices tried as the vertex with label 1;
   no symmetry reduction), state merging as in claims.md, LB pruning as in claims.md.
   COMPLETED, real 0.11 s. Output:
       d = 4, threshold T = 33, label-1-fixed-at-0 = False, pruning = True
       total states generated: 800
       RESULT: no labelling of Q_4 has at most 33 uphill paths  => U(Q_4) >= 34
   (The same run with the symmetry fix on, `dp_lower.py 4 33`, COMPLETED in real 0.04 s with
   212 states and the same conclusion.)

7. Q_4 lower bound, program 2 (independent, no state merging).
   `python3 out/code/bb_lower.py 4 33 --no-fix` -- plain depth-first branch and bound over ALL
   labellings of Q_4, no symmetry fix, no merging. COMPLETED, real 1.32 s. Output:
       d = 4, T = 33, label-1-fixed-at-0 = False, basic-bound = False, search nodes = 135168
       NONE: no labelling of Q_4 has at most 33 uphill paths => U(Q_4) >= 34
   `python3 out/code/bb_lower.py 4 34 --no-fix out/tmp/q4_bb.txt` -> FOUND 34, real 0.03 s,
   46 nodes, same witness as run 8.

8. Q_4 witness. `python3 out/code/dp_lower.py 4 34 out/Q4.txt` -- COMPLETED, real 0.25 s:
       RESULT: found labelling with 34 uphill paths (<= 34); witness:
       ['0000','0001','0010','0100','0111','1000','1111','1011','0011','1101','0101','1001','1110','0110','1010','1100']
       wrote out/Q4.txt

9. Final scoring with the provided checker and an independent explicit enumeration.
   `python3 out/code/check_artefacts.py out/Q3.txt out/Q4.txt` COMPLETED, real 0.07 s:
       out/Q3.txt: d=3 recurrence=14 explicit-enumeration=14 OK
       out/Q4.txt: d=4 recurrence=34 explicit-enumeration=34 OK
   `python3 inbox/checker/verify.py out/Q3.txt --d 3` -> `VERIFIED 14`
   `python3 inbox/checker/verify.py out/Q4.txt --d 4` -> `VERIFIED 34`

## What the searches were exhaustive over
* Run 2: exhaustive over the full set of all 8! = 40320 bijections V(Q_3) -> {1,...,8}.
* Runs 6 and 7: exhaustive over the full set of all 16! bijections V(Q_4) -> {1,...,16},
  in the sense that every bijection is represented by exactly one root-to-leaf branch of the
  search tree, and a branch is cut only by a pruning rule proved in claims.md to discard no
  labelling of score <= 33. No symmetry reduction was used in these two runs.
* Run 3 is a heuristic and is NOT exhaustive; it only supplies the upper bound 34, which is
  independently certified by the checker on out/Q4.txt.
