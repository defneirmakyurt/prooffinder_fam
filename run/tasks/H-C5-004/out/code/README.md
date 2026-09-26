# H-C5-004 code (run from run/tasks/H-C5-004/out/)

P=/home/user/bainsahackathon/.venv/bin/python3 (needs python-sat); the checker is stdlib-only.

| file | what | how to run | expected |
|---|---|---|---|
| build_labelling.py | forest indicator line -> labelling (F in BFS order per tree, then S with best order per G[S] component) | `$P code/build_labelling.py tmp/forest_subject.txt tmp/x.txt 1` then `python3 ../inbox/checker/verify.py tmp/x.txt` | `extra=0 internal count=2400`, checker `VERIFIED 2400` (< 1 s) |
| sym_forest_sat.py | exact SAT + lazy cycle cuts: induced forest of Q_d, size >= K, invariant under given automorphisms | `$P code/sym_forest_sat.py 9 277 1,2,3,4,5,6,0,7,8:0` | `UNSAT after 9 iterations ...` (~2 s) |
| prime_order_classes.py | one generator per class of prime-order automorphisms of Q_9, with orbit counts | `$P code/prime_order_classes.py` | 34 lines, first `80 7 7:7cyc ...` |
| run_classes.sh | loops sym_forest_sat.py over tmp/classes.txt (make it first: `$P code/prime_order_classes.py > tmp/classes.txt`) | `code/run_classes.sh 277 90 4` | 7cyc, 5cyc UNSAT; 3cyc3, 3cyc2 TIMED OUT |
| lns_forest.py | large-neighbourhood search: re-solve a region (subcube / ball) exactly by SAT, plateau moves | `$P code/lns_forest.py tmp/mif_s201.txt 11 400 0 tmp/o.txt --plateau 0.7 --budget 30000` | ends at |F| = 276 (no improvement), ~4 min |
| mif_sa.c | subject's max-induced-forest SA (copied unchanged) | `gcc -O2 -o tmp/mif_sa code/mif_sa.c -lm; tmp/mif_sa 9 201 50000000 2.0 0.05 tmp/f.txt` | `best |F|=276 |S|=236` (~30 s) |
| mif_sa_bal.c | same SA with both parity classes of F kept >= L | `gcc -O2 -o tmp/mif_sa_bal code/mif_sa_bal.c -lm; tmp/mif_sa_bal 9 401 100000000 2.0 0.05 60 tmp/b.txt` | `best |F|=272 ... F_even=135 F_odd=137` (~55 s) |

Forest files: one line of 512 characters, character v = '1' iff vertex v (integer whose binary digits are
the 0/1 string) is in F. `python3 ../inbox/subject/code/check_forest.py <file>` checks acyclicity and prints
|S|, e(S), components.

Seeds are fixed on the command line; the SA uses xorshift64 seeded from the seed argument, so reruns
reproduce exactly on the same compiler. The SAT runs are deterministic given the solver (cadical153);
lns_forest.py is deterministic given the seed (Python random) up to solver behaviour.
