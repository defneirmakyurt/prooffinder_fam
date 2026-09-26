# Code for H-C2-001 (U(Q_5))

All commands from this directory (`out/code/`). C code: `gcc -O2`, no dependencies; Python: stdlib only.
`verify.py` is an unmodified copy of `inbox/checker/verify.py` (library entry H-uphill-checker).

## Upper bound (search)
    gcc -O2 -o anneal anneal.c -lm
    ./anneal 5 SEED 20000000 OUT.txt      # SEED in 1..6 used; each ~7.5 s
    python3 verify.py OUT.txt --d 5       # expected: VERIFIED 88
Simulated annealing over label orders (swap / insertion moves, geometric temperature 3.0 -> 0.05,
xorshift RNG seeded from SEED). `anneal` prints its internal best (search-only scorer); the reported
score is always the checker's. Seeds 1 and 2 (20M iterations) reproduce ../Q5.txt and ../Q5_alt1.txt
byte for byte.

## Lower bound (exact layered DP; argument in ../proof.md)
    gcc -O2 -o lbdp lbdp.c
    ./lbdp 5 7 0 1   # translations only, matching heuristic on; ~3 min; expected last line:
                     # RESULT: no labelling of Q_5 has X <= 7 (T <= 87); states visited 18696829
    ./lbdp 5 7 1 1   # orbit merging (3840 automorphisms), heuristic on; ~1-2 s; states visited 19510
    ./lbdp 5 7 1 0   # orbit merging, heuristic OFF; see ../runlog.md for time and state count
    ./lbdp 5 8 1 1   # sanity: the DP itself finds minimal X = 8 (U = 88)
Arguments: D LIMIT SYM [HEUR]. X = T - E. "no labelling has X <= 7" means T >= 88 for every labelling.
Sanity (milliseconds): `./lbdp 3 5 0` -> minimal X = 2 (U(Q_3)=14), `./lbdp 4 5 0` -> minimal X = 2
(U(Q_4)=34).

## Independent checks
    python3 brute_q3.py        # all 8! labellings of Q_3; expected: min T: 14 (0.5 s)
    python3 check_identity.py  # Lemma 3 identity T = E + X on 1800 random labellings, d=1..6; 0 failures
