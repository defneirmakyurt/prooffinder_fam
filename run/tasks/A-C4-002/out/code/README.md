# out/code: numerical sanity checks (EVIDENCE ONLY)

No step of out/proof.md depends on these scripts. They are floating-point checks used to catch algebra
errors. All are stdlib-only (plain `python3`).

| script | what it checks | command | measured runtime |
|---|---|---|---|
| check_c5.py | Lemma 7: closed form Dbar(b,A) equals the direct 5-cycle sum; g'(A) = -cos b/(1+sin b cos A); D >= pi (2000 random (b,A)) | `/usr/bin/time -p python3 check_c5.py` | real 0.02 s |
| check_c6.py | Lemma 8: parametrised y_1..y_6 are unit and satisfy (H0); closed form Delta equals the direct sum; D >= pi; h decreasing (5000 random (alpha,beta,sigma)) | `/usr/bin/time -p python3 check_c6.py` | real 0.09 s |
| check_cycles_generic.py | Lemmas 7, 8 without the parametrisation: n-cycles in R^{n-2} (n=5,6) found by gradient descent from 300 random starts each; D >= pi | `/usr/bin/time -p python3 check_cycles_generic.py` | real 23.03 s |
| hillclimb.py | Global sanity check: random-restart hill climbing for max S, (N,d)=(5,3) and (6,4); best found just below 4*pi and 13*pi/2 | `/usr/bin/time -p python3 hillclimb.py 5 3 1` ; `... 6 4 2` | real 1.77 s ; 2.74 s |

Outputs observed:
- check_c5.py: `C5 formula max discrepancy 1.07e-14` (asserts passed)
- check_c6.py: `C6 formula max discrepancy 9.77e-15 min D-pi 1.79e-04` (asserts passed)
- check_cycles_generic.py: `n=5: 300 valid, min(D-pi)=2.838e-04`; `n=6: 300 valid, min(D-pi)=4.970e-03`
- hillclimb.py 5 3 1: best S = 12.566229991846374 vs 4*pi = 12.566370614359172
- hillclimb.py 6 4 2: best S = 20.419855643426178 vs 13*pi/2 = 20.420352248333657
