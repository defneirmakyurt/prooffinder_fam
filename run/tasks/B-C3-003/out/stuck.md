# Stuck point

Rung R7 (the upper bound in (a), which is also the upper half of (b)) for general k.

Proved so far: the exact dynamics once lambda is in the "late phase" class L_k, i.e. delta_m is contained, the remaining
cells lie on diagonal m, and exactly one cell lies on diagonal m+1 (Steps 3 and 5). There, d_B <= m^2-2.

What is missing is control of the early phase: a bound on the time t_A until diagonals 0..m-1 are full, coupled with
the time the late phase still needs after t_A. The two cannot simply be added: the sum exceeds m^2-2.

Exhaustive data (k<=9) shows the following, but none of it is proved:
- when n is large enough relative to d, diagonals 0..d are full by time T_d + 1;
- for r = m the fill time of diagonals 0..m-1 is at most T_{m-1}+1;
- for small r (for example r = 1) the fill time is much larger, but the late phase is then short.

A proof would need a joint potential for (i) the holes on the lowest non-full diagonal d and (ii) the cells on diagonals
>= d+1. I found one tool that looks usable but did not develop it: while diagonals < d are full, the number of parts is
s_t = d + a_t, and the excess satisfies a_T = #{i >= 1 : a_{T-d-i} >= i} for T >= lambda_1. That is a delayed copy of the
same recurrence.

Rung R9 (c) depends on R7 with an equality analysis. The extremal set is not {X_k}: its size is 34 already at k = 6, and
it contains partitions whose orbits reach the orbit of X_k only after up to 10 steps (k=6). An explicit description as a
function of k was not found.
