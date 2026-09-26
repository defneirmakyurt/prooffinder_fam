# Code for H-C5-001 (searcher, BLIND, UPPER route)

Run everything from `run/tasks/H-C5-001/out/`.  PY = /home/user/bainsahackathon/.venv/bin/python3 (pysat) ;
checker and builder are stdlib-only (`python3`).

| file | what | stdlib? |
|---|---|---|
| verify.py | copy of the provided checker (inbox/checker/verify.py = library entry H-uphill-checker) | yes |
| build_labelling.py | S (independent, complement acyclic) -> labelling (F in BFS order, then S); prints predicted count 2^d+(d-1)|S| | yes |
| ifvs_sat.py | SAT (CaDiCaL via pysat) for an independent feedback vertex set with |S|<=K; orbit variables for a symmetry group; lazy cycle clauses. Flags --mixed, --evenonly, --noindep | needs PY |
| ifvs_ls.c | SA over independent sets of fixed size K, cost = #components of Q_d - S (equivalently cycle rank) | C |
| ifvs_ls2.c | SA over independent sets of variable size, cost 8|S| + W*rank; `-DNOINDEP` builds `fvs_ls` (plain FVS) | C |
| ls3.c | SA over arbitrary S, cost = EXACT uphill count of labelling L(S) (F BFS order, then S by #F-neighbours ascending) | C |
| symbatch.sh | the 12 symmetry-restricted SAT runs (d=9, K=235) | bash |
| symbatch_fvs.sh | same 12 groups, plain FVS (--noindep), 40 s cap each | bash |

Build: `gcc -O2 -o code/ifvs_ls code/ifvs_ls.c -lm; gcc -O2 -o code/ifvs_ls2 code/ifvs_ls2.c -lm;
gcc -O2 -DNOINDEP -o code/fvs_ls code/ifvs_ls2.c -lm; gcc -O2 -o code/ls3 code/ls3.c -lm`

Reproduce the handed-in artefact (2400, does NOT meet the target):
```
./code/ifvs_ls 9 236 3 60 1.0 0.2 > tmp/ls_d9_236_s3.out     # expect RESULT ... c=96 target_c=96 r=0 (48 s here)
tail -n +2 tmp/ls_d9_236_s3.out > tmp/S236_s3.txt             # (== S236_ifvsLS.txt)
python3 code/build_labelling.py S236_ifvsLS.txt Q9.txt        # expect predicted_uphill=2400
python3 code/verify.py Q9.txt                                  # expect VERIFIED 2400
```
Note: ifvs_ls/ls3 use CPU-time limits, so results can depend on machine load; the handed-in S is saved
as S236_ifvsLS.txt so the last two commands reproduce Q9.txt exactly (deterministic, < 1 s).

Other runs: see runlog.md for exact command lines.
