# Code for H-C5-009 (UPPER route of H-C5; target NOT reached)

All scores come from `inbox/checker/verify.py`. The C programs are exact integer code (no floating point in any
decision except the SA acceptance rule of fsa.c, which is a heuristic and proves nothing).
Run from `run/tasks/H-C5-009/out/`. Build: `gcc -O2 -o tmp/<name> code/<name>.c` (add `-lm` for fsa).

| file | what | command | expected output (measured on this machine) |
|---|---|---|---|
| clusters.c | EXHAUSTIVE: every distance-2-connected set of even words of Q_9 of size 1..KMAX, up to the group G (even translations x coordinate permutations), with exact net(K) = |K| - tau(K); prints the net histogram per size and every class with net >= 2 | `tmp/clusters 8` (about 12-15 s); `tmp/clusters 9` (about 7 min, 300 MB) | size 1..7: best net 1; size 8: 67715 classes, one net-2 class (|N(K)|=48); size 9: 1593877 classes, two net-2 classes (|N(K)|=52, 55). Full log: tmp/c9.log |
| crosscheck_classes.py (stdlib) | independent cross-check of clusters.c for sizes 2..5: different canonical form (min over row orders of sorted column tuples), brute-force tau | `python3 code/crosscheck_classes.py 5` (about 90 s) | classes 1, 2, 8, 31; value histograms {1:1}, {1:2}, {1:6,<=0:2}, {1:24,<=0:7} (same as clusters.c) |
| maxcode.c | exact max number of even words pairwise at distance >= 4 and at distance >= 4 from a given set K (branch and bound max clique with colouring bound; self-checks the optimum) | `tmp/maxcode 0,480,384,320,288,192,160,96` | `region=128 max|C|=16` (under 1 s); size-9 types: 15, 15 |
| fsa.c | heuristic SA for a large induced forest, with optional forced-in / forced-out vertices | `tmp/fsa - 1 2000000 2.0 0.1 tmp/fsa_free_s1.txt` | `best |F|=276 |S|=236` (5 s) |
| make_fixed_doubled.py (stdlib) | forced-vertex file for the doubled class (half x_8 = 0 = perfect Q_8 forest: odd words + first-order Reed-Muller code) | `python3 code/make_fixed_doubled.py` | `H ok ...` |
| build_labelling.py, check_forest.py (stdlib) | copied unchanged from the subject H-C5-005: forest indicator -> labelling; forest check with the identity c + e(S) = 8|S| - 1792 | `python3 code/build_labelling.py F.txt Q9.txt 0` | see runlog |
| make_code_forest.py (stdlib) | from a 20-word even code C (distance >= 4) build the forest indicator F = C u O | `python3 code/make_code_forest.py <code list> tmp/F.txt` | forest with |S| = 236 |

Reproduce the hand-in (a 2400 labelling; it does not meet the target): see runlog.md, section "Artefacts".
