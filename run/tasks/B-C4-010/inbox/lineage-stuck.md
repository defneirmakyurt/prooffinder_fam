# Stuck point

Rung R11 (proof.md Step 14): the upper bound d_B(lambda) <= (k-1)(k-3) for partitions lambda of T_{k-1}+1 with
excess energy eps(lambda) = E(lambda) - E_min >= 2.

What is proved: every non-rigid step lowers eps by >= 1 (Step 4); on level eps = 1 the dynamics is an explicit
rotation of a triple (Q; P, P'), and the time to exit is at most (k-1)(k-3) (Steps 10-12).

Why the obvious extension fails: the exhaustive data (k = 5..11) show that for k >= 7 every level eps = 1..13
contains partitions with d_B = (k-1)(k-3) exactly. High-energy extremal orbits drop to level 1 within about 6-12
steps and land on a triple whose remaining lifetime is shorter by exactly the time already spent. So bounding the time
spent above level 1 and the time spent on level 1 separately loses on the order of k steps.

What would be needed: a phase invariant that survives the sorting (non-rigid) steps. For example, a function
Phi(lambda) >= d_B(lambda) that equals the Step 12 lifetime on level 1 and satisfies Phi(B(lambda)) <= Phi(lambda) - 1.
Alternatively, a description of all configurations at levels >= 2 (holes on lower diagonals, cells on D_{k+1}, ...)
together with the triple on which each first enters level <= 1. A possibly useful reformulation, not developed: the
piles present at time t are exactly the positive numbers among {lambda_i(0) - t} and {s(u) - (t-1-u) : 0 <= u < t},
where s(u) is the number of piles at time u. Once the original piles have died out this gives the one-dimensional
recursion s(t) = #{j >= 1 : s(t-j) >= j}.
