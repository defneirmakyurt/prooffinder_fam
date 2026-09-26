# Stuck: B-C4-011

Where the attempt fails: the target upper bound d_B(lambda) <= (k-1)(k-3) for all partitions of T_{k-1}+1, k >= 5.

1. Literature: the statement is the r = 1 case of Griggs-Ho (1998) Conjecture 4.7. The only published upper
   bounds found (Etienne/Griggs-Ho k^2-k; Griggs-Ho Thm 4.4 k^2-2k-1) are weaker at r = 1 than the elementary
   monotonicity bound (k-1)(k-2) (proof.md Step 5). No proof of the r = 1 case found (sources.md lists the
   sources and queries). Etienne 1991 (ScienceDirect blocked) and Igusa 1985 were not opened.

2. Static monotonicity fails by a full k-1: with nu = lambda minus a cell, d_B(lambda) <= d_B(nu), but for
   6 <= k <= 10 some lambda have EVERY removal nu at the maximal triangular depth (k-1)(k-2)
   (out/code/corner_obstruction.py). Any proof must use the dynamics of lambda itself, not only of nu.

3. Griggs-Ho sandwich machinery (Prop. 3.2, Lemmas 3.3-3.6, 4.3): its pattern-descent bound loses about
   2k-4 steps against the target at r = 1; the r = 1 information (sum of any k consecutive part counts
   <= k^2-k+1) would have to be used far more sharply. Not done.

What the next person needs to start (literature side):
- Griggs-Ho, Section 3 (diagram_B bookkeeping, Lemmas 3.3-3.6) and Section 4 (Lemma 4.3, Thm 4.4) at
  https://people.math.sc.edu/griggs/cycling.pdf, pp. 7-15.
- The blind runs' exact level-1 lifetime formula (B-C4-006 Step 12, B-C4-007 Lemma 7) is NOT in Griggs-Ho;
  combining it with Griggs-Ho's part-count sequence (in which the level-1 phase is visible as the positions of
  the k-1 -> k steps) is the most concrete untried route.
- Etienne 1991 should be opened (library access): its Theorem 5.1 / Conjecture 5.2 may contain finer
  per-r estimates than those quoted secondhand.
