# Code for H-C1-004 -- U(Q_3) and U(Q_4)

Python 3, standard library only, exact integer arithmetic.  No third-party packages.
Set `PY` to any Python 3 interpreter; the task's is
`/Users/raducucu/bainsahackathon/.venv/bin/python3`.
Run everything from the task folder `run/tasks/H-C1-004/`.

## Files

- `uphill.py` -- the counting recursion for the number of uphill paths of a labelling of `Q_d`
  (proof in `../claims.md`, section R2).  Imported by the other scripts.  Not the scorer of record:
  every reported score comes from `inbox/checker/verify.py`.
- `brute_q3.py` -- full enumeration of all 8! = 40320 bijections `V(Q_3) -> {1..8}`.
- `sa_q4.py` -- simulated annealing (transposition moves), a candidate generator for upper bounds.
- `bnb.py` -- exhaustive depth-first branch and bound over all `(2^d)!` bijections.  Decision form:
  `bnb.py d T` answers "does some labelling of `Q_d` have fewer than `T` uphill paths?".
- `crosscheck.py` -- two validators: internal counter vs the provided checker on random labellings,
  and a sweep of `bnb.py` over thresholds `T`.

## The two commands that establish the answer

```
$PY out/code/bnb.py 3 14 --nomemo --nolb     # -> NONE BELOW 14      (0.10 s)
$PY out/code/bnb.py 3 15 --out out/Q3.txt    # -> FOUND 14 + writes the labelling
$PY inbox/checker/verify.py out/Q3.txt --d 3 # -> VERIFIED 14

$PY out/code/bnb.py 4 34 --nomemo            # -> NONE BELOW 34      (0.85 s)
$PY out/code/bnb.py 4 35 --out out/Q4.txt    # -> FOUND 34 + writes the labelling
$PY inbox/checker/verify.py out/Q4.txt --d 4 # -> VERIFIED 34
```

Hence `U(Q_3) = 14` and `U(Q_4) = 34`.  Total rerun time well under 5 seconds.

## `bnb.py` in detail

```
$PY out/code/bnb.py <d> <T> [--nomemo] [--nolb] [--maxnodes M] [--out FILE]
```

Prints a statistics line, then either

- `NONE BELOW T` -- every one of the `(2^d)!` labellings of `Q_d` has at least `T` uphill paths, or
- `FOUND c` followed by `2^d` lines -- a labelling with `c < T` uphill paths, in the hand-in format.

It builds a labelling one label at a time: at depth `k` it tries **every** unplaced vertex as the
holder of label `k+1`.  There is no symmetry reduction and no restriction on which vertex may take
label 1, so the unpruned leaf set is exactly the set of all `(2^d)!` bijections.

Three prunes, each proved in `../claims.md`:

- the trivial one, `cost + N(v) >= T` (all `N` values are `>= 1`, so the total can only grow);
- `--nolb` disables the admissible lower bound `LB(S)` on the cost of the unplaced part (R5);
- `--nomemo` disables the state memo keyed on `(S, N restricted to the boundary of S)` (R6).

The reported Q_4 lower bound is taken from the `--nomemo` run, so it rests only on the trivial prune
and `LB(S)`.  The Q_3 lower bound is taken from the `--nomemo --nolb` run, i.e. from an essentially
unpruned traversal, and independently from `brute_q3.py`.

`--maxnodes M` aborts after `M` nodes and prints `ABORTED node cap M reached -- search NOT complete`
instead of a verdict; it exists so that an incomplete search can never be mistaken for a proof.

## Other commands (validation, see `../runlog.md`)

```
$PY out/code/brute_q3.py                                    # min = 14, 7104 minimisers, 0.25 s
$PY out/code/sa_q4.py 4 20 out/tmp/q4_sa.txt 60000          # 20 seeds, all reach 34, 13.1 s
$PY out/code/crosscheck.py counter 3 300 inbox/checker/verify.py   # mismatches=0
$PY out/code/crosscheck.py counter 4 300 inbox/checker/verify.py   # mismatches=0
$PY out/code/crosscheck.py sweep 3 16                       # NONE BELOW T for T<=14, FOUND 14 after
```

`sa_q4.py <d> <nseeds> <outfile> <iters>` uses `random.Random(seed)` for `seed = 0..nseeds-1`, so it
is reproducible.  `crosscheck.py counter` uses seed 12345.  `brute_q3.py` and `bnb.py` are
deterministic.
