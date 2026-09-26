# Where the attempt stops (H-C5-006)

* UPPER route: stops at sub-problem U5 (an induced forest of Q_9 with >= 277 vertices; by Lemma I + I8 its
  complement must contain an edge). Literature (Pike 2003 via Hertz 2021 Table 4 and Wodlinger's thesis) has
  236 as the best decycling set; no source gives <= 235. My searches (fixed-size penalty SA at |F| = 277; C9-symmetric
  SAT/CEGAR at |F| = 276, timed out) found nothing. U6 (ordering S within the J5 budget) not reached.
* LOWER route: stops at L4 (nabla(Q_9) >= 233) and L3 (nabla(Q_9) >= 232, the presumable source of the
  organisers' 2368). Only 225 is proved (226 is attributed to Pike by Wodlinger, not reproduced). No argument
  for c(F) + e(S) >= 72 was found; see why_not.md items 5-9 for the approaches that stall.
* [GAP] A(9,4) = 20 is cited (Best et al. 1978 via Brouwer's table), not reproduced; the plain Delsarte LP gives
  only 25 (out/code/lp_A94.py). I8 and J5's "S contains an edge" depend on it.
* [GAP] Pike 2003 not opened (paywall); the statements attributed to it come from two secondary sources which
  disagree on the n = 9 lower bound (225 vs 226).
