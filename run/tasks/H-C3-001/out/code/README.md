# Code for H-C3-001 (U(Q_6) = 204)
Run everything: `sh run_all.sh` (gcc + python3 stdlib; ~10 s measured). Expected output:
four `VERIFIED 204`; lower-bound runs `solutions=0` with nodes 39783 / 2889353 / 103326594;
controls 240 / 14400 solutions, forest counts d5p13=0, d6p26=0, d6p27=0, d6p28=240;
regenerated artefacts byte-identical to ../Q6.txt and ../Q6_alt1.txt, both VERIFIED 204.
- verify.py: provided checker (library entry H-uphill-checker, sha256 2c0ba1a6...), the only scorer reported.
- anneal.c: SA on labellings (`./anneal d seed steps restarts out [T0 T1]`), produced Q6.txt (seed 1), Q6_alt2.txt (seed 2).
- forest_search.c: SA for independent P with forest complement, builds labelling (trees BFS, then P); produced Q6_alt1.txt (p=28 seed 5). forest_search.py: slow Python prototype (timed out; not used).
- exhaust_general.c: exhaustive search behind the lower bound (see ../lower_bound.md).
- exhaust_forest.c: exhaustive count of independent P, |P|=p, with forest complement (cross-check for S empty).
- analyze.py: prints V, X, peaks of a labelling (diagnostic only).
