# Run log: H-C2-002

All runs on this machine; times measured with bash `time` (TIMEFORMAT real %R; /usr/bin/time is not
installed). Python = python3 (stdlib only for every script below). cwd = out/ unless noted.

| # | command | parameters | result | status | real time |
|---|---|---|---|---|---|
| 1 | code/sa (C, gcc -O2, from code/sa.c), cwd out/code | d=5, seeds 1-4, 2e6 iters, T 3.0->0.05 | best 88 each | COMPLETED | 0.74, 0.85, 0.76, 0.79 s |
| 2 | code/sa | d=5, seeds 11-13, 3e7 iters, T 5.0->0.05 | best 88 each | COMPLETED | 10.96, 11.12, 11.26 s |
| 3 | code/sa | d=6, seeds 1-2, 1e7 iters | best 204 each | COMPLETED | 6.68, 6.75 s |
| 4 | code/sa | d=7 seed 1 2e7 iters; d=8 seed 1 1.5e7 iters | 464; 1040 | COMPLETED | 25.72 s; 39.37 s |
| 5 | python3 code/decycle.py d k [--no-edge-prune], cwd out/code | (3,2),(3,3),(4,5),(4,6), each with and without cut | NONE, FOUND, NONE, FOUND (both modes) | COMPLETED | 0.012-0.019 s each |
| 6 | python3 code/decycle.py 5 13 | edge cut on | NONE (12742 nodes) | COMPLETED | 0.042 s |
| 7 | python3 code/decycle.py 5 14 | edge cut on | FOUND, is_decycling True | COMPLETED | 0.034 s |
| 8 | python3 code/decycle.py 5 13 --no-edge-prune | no edge cut | NONE (3907075 nodes) | COMPLETED | 5.38 s |
| 9 | python3 code/decycle.py 6 27 | edge cut on | NONE (1484706 nodes) | COMPLETED | 8.18 s |
| 10 | python3 code/construct.py d tmp/C<d>.txt, then copied to Q<d>.txt | d=5,6,7,8 | predicted 88, 204, 464, 1040 | COMPLETED | 0.053, 0.045, 0.026, 4.83 s |
| 11 | python3 ../inbox/checker/verify.py Q<d>.txt --d d | Q5..Q8 | VERIFIED 88, 204, 464, 1040 | COMPLETED | Q5: 0.021 s (others not individually timed, < 1 s) |
| 12 | python3 code/construct.py 3 / 4 + verify.py | d=3,4 | VERIFIED 14, 34 | COMPLETED | 0.041, 0.028 s |
| 13 | python3 code/sanity.py 3000 7 | 3000 random labellings, d in 3..6 | violations=0 | COMPLETED | 0.23 s |
| 14 | python3 code/decycle.py 7 55 (timeout 590) | edge cut on; d = 7, k = 55 | no answer (search space not exhausted) | TIMED OUT (exit 124) | 590.0 s |
| 15 | gcc -O2 -o brute13 brute13.c; ./brute13 13 (cwd out/code) | all 141120525 13-subsets of V(Q_5) containing 0 | decycling found=0 | COMPLETED | 2.41 s |
| 16 | ./brute13 14 | all 206253075 14-subsets containing 0 | decycling found=945 (control) | COMPLETED | 3.49 s |

Note on SA (runs 1-4): heuristic only, proves nothing; reproducible given the seed (xorshift RNG).
Hand-in Q5.txt is the construct.py output (run 10), not the SA output (tmp/q5_L11.txt, also 88).
