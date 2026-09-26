# Stuck point (B-C2-006)

Exact failing rung: R10 = proof.md Step 24: d_B(lambda) <= k^2 - k for lambda |- T_k outside R_k, k >= 12.

Equivalent open statement (by Steps 19-22, proved): for the queue map
  e -> e',  e'_j = e_{j+1} + [j <= k + e_1] - [j <= k],
started from any integer sequence e with finite support, sum 0, e_{j+1} <= e_j + [j <= k], e_j >= -(k+1-j)_+,
the sequence is identically 0 after at most k^2 - k steps.

What is known: one +1 and one -1 unit => this is Steps 13-14 (bound k^2-k, sharp).

Attempt (a) [failed]: last annihilated pair (eta hole on track k, gamma cell on track k+1). If both are on these
tracks from time 0, Step 14 applies. If one arrives at time t1 > 0 (hole bubbling from track < k, or cell sinking
from track k+2 - the latter always coincides with another annihilation in the same column when its new row is >= 2),
the Young constraint at t1 only gives T <= t1 + (k^2-k). A needed extra lemma: an object arriving on track k or
k+1 at time t1 has next meeting with every partner within k^2-k-t1 steps. Not proved; the subject showed the naive
all-pairs version of this invariant is false.

Attempt (b) [failed]: in queue form, a -unit recurs with period k+1-r <= k and a +unit with period k+r >= k+1
(r = rank among units processed together). If the -unit visits the head exactly once per +lap, the offset
a_j = (first -visit after the j-th +visit) - (j-th +visit) satisfies a_{j+1} <= a_j - r_j, giving at most a_0 <= k-1
laps. But when several -units share the window, the -unit can visit the head twice within one +lap and the offset
can jump back up to k-1; I could not control this, nor the initial position of the +unit (it can start far beyond
position k when lambda has a long first row).

Dead end (c): sandwich lambda^- <= lambda <= lambda^+ with |lambda^+-| = T_k +- 1 (Step 23) gives only
d_B(lambda) <= max(d_B(lambda^-), d_B(lambda^+)) + k^2 - k, circular and too weak.

What would be needed: a potential on queue configurations (Step 22) that is <= k^2-k initially and drops by
>= 1 per step while e != 0, reducing to tau of Step 13 in the one-pair case.
