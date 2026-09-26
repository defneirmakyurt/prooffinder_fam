# Code for H-C5-007

* check_code_bound.py  (stdlib only, exact integers/Fractions, < 1 s)
  Run: python3 check_code_bound.py
  Checks the finite arithmetic behind proof.md Step 6 (Lemma 3: even-weight length-9 codes with min distance
  >= 4 have <= 21 words): closed forms of K1, K2; the pair-sum identity over all 512 sign vectors; the dual
  certificate y1 = y2 = 1/3, u = 16/3 giving 64/3; the distance-8 structure over all 512 words.
  Expected last line: ALL OK. The proof itself is written out by hand in proof.md Step 6.
* lp_explore.py  (needs sympy; exploratory, NOT used by the proof)
  Run: /home/user/bainsahackathon/.venv/bin/python3 lp_explore.py
  Exact Delsarte LP for the same codes: plain LP 128/5, with A8 <= 1 it is 64/3; prints the dual solution
  that was then checked by check_code_bound.py.
