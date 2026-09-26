# Why (a) is not solved here

**Obstruction.** Everything reduces to SP5 (subproblems.md): the time a partition outside C_k spends before entering
C_k must be charged against the time it has left after entering. Diagonal monotonicity (proof.md Lemma 1) makes
entry absorbing, and inside C_k the bound is known (B-C3-004 Thm 6.1). The coupling is the missing piece.

**Failing approaches, and why each fails.**
1. Additive two-phase bound (bound t_C, then add the worst C_k time). Fails numerically. Exact exhaustive data
   (code/phase_stats.py, k=4..8) give max t_C = 5,9,15,24,35 and max(d_B - t_C) = 7,14,23,34,47, with sums
   12,23,38,58,82 > 7,14,23,34,47. The worst C_k time is already k^2-2k-1 (it is attained by lambda*_k at t_C=0).
   So any positive entry time breaks a purely additive bound.
2. Energy E = sum of diagonals (B-C3-002, B-C3-004). It is non-increasing and strictly decreasing at falls. But the
   maximum is attained at energy excess 1, so energy says nothing about waiting times.
3. Lowest hole diagonal / highest cell diagonal (B-C3-004 stuck.md). Both are monotone. But a hole on the lowest
   hole diagonal need not be filled on its first visit to row 0, and summing the per-level waits overshoots.
4. Splitting into "until D_{k-2} full" and "after" (B-C3-002 stuck.md). Data for n=T_8-1 give 22 and 47, sum 69 > 47.
   This is the same failure as 1.

**What the next person needs.**
- Get the primary sources by hand (a browser download). Griggs & Ho, Adv. Appl. Math. 21 (1998) 205-227,
  doi:10.1006/aama.1998.0597 (Elsevier open archive; blocked for automated fetch). Etienne, JCTA 58 (1991) 181-197,
  Thm 5.1, doi:10.1016/0097-3165(91)90059-P. Check whether the k^2-2k-1 bound there is proved or only conjectured.
  Hopkins 2012, p. 139, says Griggs-Ho "conjectured maximal lengths ... for n != T_k". If proved, reproduce it
  lemma by lemma.
- Start from proof.md Lemmas 1-3 (monotonicity, absorbing C_k, entry decomposition) and B-C3-004 Steps 2-6
  (A/P encoding, rotating hole labels, counting lemma).
- A candidate target is SP5a: extend B-C3-004's hole-label frame to diagonal pairs (d, d+1) for every d. Then show
  that a particle entering diagonal k at time t_C has an effective first check index reduced by at least about
  t_C/(k+1).
- Useful exact data: max t_A = (k-2)^2 - 1 for k=5..8 and max t_B = T_{k-1} - 1 for k=4..8. Both are finite
  checks only.
