# Code for H-C4-001 (U(Q_7) = 464, U(Q_8) = 1040)

All commands from `run/tasks/H-C4-001/out/`. `python3` = plain stdlib python3 (the SAT cross-check
needs the venv python with python-sat).

## 1. Score the artefacts (the provided checker; sha256 2c0ba1a6...db6e = library H-uphill-checker)
    python3 code/verify.py Q7.txt        # expected: VERIFIED 464
    python3 code/verify.py Q7_alt1.txt   # expected: VERIFIED 464
    python3 code/verify.py Q8.txt        # expected: VERIFIED 1040
    python3 code/verify.py Q8_alt1.txt   # expected: VERIFIED 1040

## 2. Lower-bound computation (headline; stdlib; < 1 s)
    python3 code/lb_forest.py
Expected output (last lines):
    Q_4: 25015 induced forests (incl. empty); F_4 = 10; counts by size >= 7: {7: 6848, 8: 4090, 9: 1008, 10: 8}
    Q_5: no induced forest with 20 vertices (...)
    Q_5: no induced forest with 19 vertices (...)
    Q_5: F_5 = 18; witness T0=0b1011011101001 T1=0b1110100110010111
    pairs examined = 16928, passed edge-count filter = 1100
Why this proves the bound: claims.md sections A (Lemma A), C (Lemma C), B (reduction), D.

## 3. Independent cross-check of F_5 = 18 (not used in the headline; < 1 s)
    /home/user/bainsahackathon/.venv/bin/python3 code/crosscheck_F5_sat.py
Expected: `m=19: UNSAT after 707 iterations, 786 cycle clauses` and `m=18: SAT, induced forest of size 18`.

## 4. Sanity check of Lemma A on random labellings and on the artefacts (not a proof; < 1 s)
    python3 code/lemmaA_sanity.py Q7.txt Q8.txt
Expected: `random trials: 1580, violations: 0`, and count = bound = 464 (|S| = 56), 1040 (|S| = 112).

## 5. Search that produced the artefacts (C, deterministic given the arguments)
    gcc -O2 -o code/fvs_sa code/fvs_sa.c -lm
    cd code
    ./fvs_sa 7 11 10000000 0   ../Q7.txt      200000       # ~20 s, Q7.txt   (init 0: start S = even-weight vertices)
    ./fvs_sa 7 31 10000000 0.3 ../Q7_alt1.txt 200000 2     # ~25 s, Q7_alt1 (init 2: random start)
    ./fvs_sa 8 21 20000000 0.3 ../Q8.txt      200000       # ~2 min, Q8.txt
    ./fvs_sa 8 22 20000000 0.3 ../Q8_alt1.txt 200000       # ~2 min, Q8_alt1
Arguments: d seed SA-iterations mu outfile polish-iterations [init]. stderr prints |S|, e(S), the
decoded count and the polished count (internal 128-bit counter; the reported score is always the
checker's). Method: simulated annealing over vertex subsets S minimising (d-1)|S| + d*cyc(Q_d - S)
+ mu*e(S) (cyc = cyclomatic number), decoding the best acyclic state to a labelling (each tree of
T = V \ S in BFS order, then S greedily), then an order-move local search on the exact count.
