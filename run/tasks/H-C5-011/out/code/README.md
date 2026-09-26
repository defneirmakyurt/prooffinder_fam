# Code for H-C5-011

All proof-relevant code is stdlib-only Python 3 with exact integer / bitmask arithmetic.

## cluster_tau.py  (used by proof.md Step 12; proof-relevant)
Run:  python3 cluster_tau.py 5        (proof run; prints one line per k = 1..5)
Expected output: for every k = 1..5 the line ends with "clusters with tau*(C) > k+0: 0";
class counts 1, 1, 2, 8, 31.
What it checks: for every set C of k odd vertices of Q_9 that is connected in the distance-2 graph (up to the
automorphisms x -> pi(x) XOR v, pi a coordinate permutation, v of even weight), no C-valid set M' has
tau(G_2[M']) > k, where M' is C-valid iff M' is contained in N_E(C) and Q_9[M' u (N_O(M') \ C)] is acyclic.
Why the enumeration covers every class, why equal keys imply equivalence, why the acyclicity test and the two
pruning bounds are sound: proof.md Step 12 (a)-(c).
Options: second argument OFF changes the threshold to k + OFF (self-test: `python3 cluster_tau.py 4 -1` must
report violations, it reports 1,1,2,5 of 1,1,2,8 classes); OFF = 99 runs the exact unpruned evaluator
(`python3 cluster_tau.py 4 99` prints the exact histogram of tau*(C) - k: k=4 gives {-1: 3, 0: 5});
a third argument prints per-class progress on stderr.
k = 6 (`python3 cluster_tau.py 6 0 prog`) was attempted: 268 keys at k = 6, 19 of them finished (0 violations)
after about 3.7 minutes, when the run was stopped (projected > 1 hour); NOT used by the proof.
Measured: `python3 cluster_tau.py 5` real 2m32.5s (user 1m43s); `python3 cluster_tau.py 4 -1` 1.9 s;
`python3 cluster_tau.py 4 99` 11.3 s.

## crosscheck_validity.py  (cross-check of cluster_tau.py, not needed for the proof)
Run:  python3 crosscheck_validity.py 3   (or 4)
For every class of size k <= KMAX it enumerates the C-valid family twice -- with the incremental label test of
cluster_tau.py and with a from-scratch union-find on the explicitly built graph L(C, M') -- and checks that the two
families coincide; it also recomputes max tau over the family with a brute-force minimum vertex cover.
Output for KMAX = 3: families identical, max tau - k = 0 for every class (2.7 s). A KMAX = 4 run was stopped after
54 s (k <= 3 printed, k = 4 not finished); PARTIAL, not used.

## check_code_bound.py  (copied unchanged from the subject H-C5-007; used by proof.md Step 4)
Run:  python3 check_code_bound.py      Expected last line: ALL OK.
Re-checks the finite arithmetic of Lemma 3 (even-weight length-9 codes with minimum distance >= 4 have <= 21 words).

## sa_forest.c  (exploratory only, NOT used by any proof step)
Build: gcc -O2 -o sa_forest sa_forest.c -lm ; Run: ./sa_forest SEED ITERS 2.0 0.05 1.5 out.txt
Simulated annealing for large induced forests of Q_9 (maximises |F| - 1.5 * cyclomatic number); writes the best
forest found. Runs with seeds 2, 3, 4 and 2.5e7 moves each found 276 at best.

## test_r9.py  (exploratory, needs python-sat; NOT used by any proof step; not run to completion)
