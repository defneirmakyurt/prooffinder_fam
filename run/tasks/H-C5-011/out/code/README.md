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
k = 6 (`python3 cluster_tau.py 6`) was attempted; see RAN in the report / stuck.md for its status.

## check_code_bound.py  (copied unchanged from the subject H-C5-007; used by proof.md Step 4)
Run:  python3 check_code_bound.py      Expected last line: ALL OK.
Re-checks the finite arithmetic of Lemma 3 (even-weight length-9 codes with minimum distance >= 4 have <= 21 words).

## sa_forest.c  (exploratory only, NOT used by any proof step)
Build: gcc -O2 -o sa_forest sa_forest.c -lm ; Run: ./sa_forest SEED ITERS 2.0 0.05 1.5 out.txt
Simulated annealing for large induced forests of Q_9 (maximises |F| - 1.5 * cyclomatic number); writes the best
forest found. Runs with seeds 2, 3, 4 and 2.5e7 moves each found 276 at best.

## test_r9.py  (exploratory, needs python-sat; NOT used by any proof step; not run to completion)
