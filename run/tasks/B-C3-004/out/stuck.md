# Stuck point

Rung R8 (target (a) for partitions outside C_k = {delta_{k-1} <= lambda <= delta_{k+1}}), proof.md 6.2.

What is proved: once the trajectory lies in C_k (diagonals 1..k-1 full, nothing beyond diagonal k+1), B is a
rigid rotation of two rings (diagonal k, period k; diagonal k+1, period k+1) plus particle/hole absorptions,
and a counting argument (Lemma 5.1) bounds the remaining time by k^2-2k-1; the bound is
only tight when the configuration is already in C_k at time 0.

What fails: for general lambda there are cells on diagonals >= k+2 and holes on diagonals <= k-1. Slides then
move whole columns (a hole jumps up several diagonals), several diagonal pairs interact at once, and I have
no quantity that charges the time spent before entering C_k against the slack left in Lemma 5.1 at the
entry time (the slack is (k^2-2k-2) - max_j[(k+1)v_j - Q_j]). Exhaustive data (k<=10) show that most extremal
partitions of T_k-1 lie outside C_k (e.g. 3874 of 3911 for k=9) and enter C_k "in phase", so a bound of the
form (time to enter C_k) + (worst C_k time) is too weak; what is needed is a monotone phase-plus-energy
potential valid on all partitions (a generalisation of the label-scanning of Step 4 to every pair of
consecutive diagonals d, d+1 with cascading slides).

Attempts that failed (twice, hence stopped per STOPPING CONDITION):
1. Energy E = sum of diagonal indices: non-increasing, strictly at slides, but max d_B is attained already at
   energy excess 1 (data), so energy alone gives nothing about the waiting time.
2. Lowest-hole-diagonal m_t (non-decreasing) and highest-cell-diagonal M_t (non-increasing): a hole on the
   lowest hole-diagonal is not necessarily filled on its visit to the bottom, and summing waiting times per
   level overshoots k^2-2k-1.

Consequently the upper half of (b) and the "only these" half of (c) are open here for k >= 11 (checked k<=10).
