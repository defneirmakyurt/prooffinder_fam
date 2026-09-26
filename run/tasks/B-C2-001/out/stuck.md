# Stuck point: B-C2-001

Exact failing rung: R8 = proof.md Step 9, the UPPER bound d_B(lambda) <= k^2 - k for every
lambda |- T_k and every k >= 12. Everything else (convergence, uniqueness of the cyclic
partition, the exact witness value d_B(lambda^(k)) = k^2 - k, and the upper bound for k <= 11 by
exhaustive exact computation) is written out.

What is available: the energy E (sum of diagonal indices) is non-increasing and drops at every
sorting step (Step 2), and a configuration that is never sorted again must be delta_k (Step 4).
This gives termination, not a time bound.

Attempt (a): energy + waiting time between sorts. E - E_min can be of order k^3, and Step 4
bounds the number of consecutive pure rotations only by an lcm/gcd argument
(about d*D steps for a hole on diagonal d and a cell on diagonal D), so summing gives nothing near k^2 - k.

Attempt (b): conjugate / queue model. With mu = lambda' and f_c = mu_c - max(0, k+1-c),
one step is: pop q = f_1, shift left, then add +1 at positions k+1..k+q (if q > 0) or -1 at
positions k+q+1..k (if q < 0). So a single positive unit has period k+1, a single negative unit
period k, and the configuration is delta_k iff f = 0. In the regime where every |f_c| <= 1
(delta_{k-1} <= lambda <= delta_{k+1}, which is invariant because B is monotone under diagram
containment), units never merge, and a single +/- pair is cancelled after at most k-1 laps. The
maximum over admissible positions is exactly k^2 - k, attained only by lambda^(k). (I checked
this for one pair by the CRT computation; it is not written up in proof.md.)
Failure point: in general, units merge (|f_c| >= 2). A merged positive group spreads forward,
a merged negative group spreads backward, and a negative unit may complete two laps while a
positive completes one. The "gap" potential G = (positive schedule) - (negative schedule), which rises by
exactly 1 per lap for isolated units, can then fall by up to k-1 in one lap, and unit identities
are not preserved when a slot holds several units.
What would be needed: a lemma bounding the total time spent outside the near regime,
jointly with the remaining near-regime time, by k^2 - k. For example: a potential Phi <= k-1 that
drops by at least 1 in every block of k+1 steps until delta_k is reached, valid for merged
groups too. Or a proof that the far regime is left fast enough to leave a near-regime
configuration whose pair offsets make up for the time already spent.
