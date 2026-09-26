# Code for H-C5-005 (search for a labelling of Q_9 with <= 2399 uphill paths)

All scores reported come from `inbox/checker/verify.py`. Everything here is search code; none of it proves a bound.
PY = /home/user/bainsahackathon/.venv/bin/python3 (needs python-sat) for the two SAT tools; the others are stdlib / C.
Run from `run/tasks/H-C5-005/out/`.

| file | what | example | expected output |
|---|---|---|---|
| build_labelling.py (stdlib) | forest indicator -> labelling file (F components in BFS order, then S, each S-component in the order minimising sum of N) and internal count | `python3 code/build_labelling.py forest_Q9.txt Q9.txt 0` | `built labelling: |F|=276 |S|=236 uphill paths (internal count) = 2400` |
| check_forest.py (stdlib, copied from the lineage H-C5-002) | checks an indicator line induces a forest, prints |S|, e(S), components | `python3 code/check_forest.py forest_Q9.txt` | `forest=True |S|=236 e(S)=0 ... components=96 identity_ok=True` |
| msa.c | SA over the even part M of a forest, Z chosen greedily | `gcc -O2 -o tmp/msa code/msa.c -lm; tmp/msa 9 1 20000000 4 0.3 tmp/msa_d9_s1.txt` | `d=9 best P_est=2400 (re-eval 2400) |M|=20 |Z|=0 |S|=236` (about 22 s) |
| orbitsa.c | SA for large induced forests that are unions of orbits of a group given by generators | `gcc -O2 -o tmp/orbitsa code/orbitsa.c -lm; tmp/orbitsa 9 11 3000000 2 0.15 tmp/ob_triv.txt` | `d=9 orbits=512 best |F|=276 |S|=236` (about 50 s; seed-dependent) |
| sat_cegar.py | SAT + lazy cycle clauses for a decycling set with |S| <= K; option `--oddmax z` restricts to |S cap O| <= z, |S cap E| <= K - z | `$PY code/sat_cegar.py 7 56 --time 100` | `FOUND decycling set |S|=56 ...` (about 75 s) |
| sat_group.py | same, restricted to sets invariant under a group (generators `--perm p0,..,p8:t`) | `$PY code/sat_group.py 7 56 --perm 1,2,3,4,5,6,0` | `FOUND decycling set |S|=56 after 1 iterations` |
| cluster_value.py (stdlib) | exact: max value |K| - tau(K) over distance-2-connected even sets K of size 2..smax (lemma L2) | `python3 code/cluster_value.py 5` | four lines, best value 1 at every size; size 5: 111300 sets (about 70 s) |
| sat_lns.py | large-neighbourhood search: re-solve a random subcube region exactly by SAT, rest fixed | `$PY code/sat_lns.py 9 tmp/ob_triv.txt tmp/lns1.txt --rounds 40 --k 6 --sub-time 10 --seed 1` | 40 lines `UNSAT`, `final |S|=236` |

Reproduce the hand-in: `tmp/msa 9 1 20000000 4 0.3 tmp/msa_d9_s1.txt` then
`python3 code/build_labelling.py tmp/msa_d9_s1.txt Q9.txt 0` then `python3 ../inbox/checker/verify.py Q9.txt`
-> `VERIFIED 2400`. (The SA is seeded xorshift; the same binary and seed reproduce the same file on this machine.
The hand-in itself is checked directly; reproduction of the search is not needed for its score.)
