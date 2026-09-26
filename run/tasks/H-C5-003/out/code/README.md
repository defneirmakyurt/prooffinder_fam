# Code for H-C5-003 (searcher, EXPLOIT of H-C5-002)

All paths relative to `run/tasks/H-C5-003/out/`. PYTHON = /home/user/bainsahackathon/.venv/bin/python3
(only needed for the pysat scripts); everything else is stdlib python3 / gcc.

| file | what | how to run | expected output |
|---|---|---|---|
| `code/mcut_sa.c` | simulated annealing for a maximum induced forest of Q_d with the multiway-cut repair move (add v; for every tree holding >= 2 F-neighbours of v delete a minimum vertex multiway cut separating them) | `gcc -O2 -o tmp/mcut_sa code/mcut_sa.c -lm; cd tmp; ./mcut_sa d seed iters T0 T1 pnb outfile [initfile]` | e.g. `./mcut_sa 9 1 20000000 0.6 0.1 0.0 F9_s1.txt` -> `best |F|=276 |S|=236` in ~11 s |
| `code/forest_to_labelling.py` | forest indicator line -> labelling file (forest components in BFS order, then S greedily by smallest current N) | `python3 code/forest_to_labelling.py tmp/F9_s1.txt tmp/L9_s1.txt` | `|F|=276 |S|=236 e(S)=7 components=89 internal_count=2400` |
| `code/sat_forest.py` | lazy (CEGAR) SAT: induced forest of Q_d with >= K vertices (face + hexagon clauses, cardinality, cycle cuts) | `PYTHON code/sat_forest.py d K` | d=5 K=18 FOUND; d=6 K=36 FOUND (~1.5 s); d=7 K=72 does not finish in 120 s |
| `code/region_code.py` | max even-weight code, min distance 4, inside {wt(last 5 coords) >= t} (room left by a Q_4 cluster) | `PYTHON code/region_code.py 3 K` | K <= 16 SAT, K = 17, 18, 19 UNSAT (solver verdict, no certificate) |
| `code/clusters.py` | enumerates G2-connected clusters of even words up to symmetry and their best net contribution |M_K| - delta(K) | `python3 code/clusters.py SMAX` | see runlog |
| `code/clusters_q5.py` | all G2-connected sets of s even words inside one Q_5 subcube (containing 0) with net >= 2, exact | `python3 code/clusters_q5.py 8` | `net >= 2 for 5 of them`, support sizes [(4, 5)] (~1 s); sizes 9..16 take ~5 min |
| `code/sym_pen_sa.c` | penalty SA (energy -\|F\| + lambda * cycle rank) over forests invariant under a coordinate permutation sigma | `gcc -O2 -o tmp/sym_pen_sa code/sym_pen_sa.c -lm; cd tmp; ./sym_pen_sa d seed iters T0 T1 lambda "p0 ... p_{d-1}" outfile` | d=8 identity: `best |F|=144 |S|=112` in ~13 s |

Scoring: every labelling is scored only with `python3 ../inbox/checker/verify.py <file>`.
Forest statistics: `python3 ../inbox/subject/code/check_forest.py <forest file>` (predecessor's stdlib checker).
