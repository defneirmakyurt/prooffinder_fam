# Run log: H-L1-001

All runs: `python3 out/code/sanity.py 100000 2000` (stdlib only, Python 3.11.15), timed with bash
`time` (/usr/bin/time is not installed). Exact integer arithmetic throughout. None of these runs is a
step of the proof in out/proof.md.

| run | command | range | result | status | measured time |
|---|---|---|---|---|---|
| 1 | `python3 code/sanity.py 100000 2000` (checks A-E) | A: k=2..100000; B: d=3..2000; C: all 40320 labellings of Q_3; D: all labellings of Q_1, Q_2, P4, K_{1,4}, K4, C5, paw; E: 200 random labellings each of Q_3..Q_8, seed 20260926 | all assertions pass; Q_3 min P = 14; output in out/tmp/sanity_run1.txt | COMPLETED | real 0.938 s |
| 2 | same, after adding check F (earlier-proof witnesses) | as run 1 plus F: the Q_3 and Q_4 labellings of inbox/earlier-proof.md Step 8 | all pass; F gives (3,14), (4,34); output in out/tmp/sanity_run2.txt | COMPLETED | real 1.014 s |
