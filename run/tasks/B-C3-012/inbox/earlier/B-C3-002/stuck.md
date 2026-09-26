# Stuck point

Rung R8 (target (a), and through it equality in (b) and completeness in (c) for k >= 11).

What is proved: the exact dynamics of all partitions whose energy excess Phi = E - E_min is 0 or 1
of "case B" type (one cell on diagonal k, holes on diagonal k-1): d_B = 1-c+(k+1)min_a((c-1-a) mod k),
max (k+1)(r-2)+2 (proof.md sections 4-5).

Where it fails: partitions with Phi >= 2 (several cells above diagonal k-1, and/or holes on lower
diagonals), and Phi = 1 case A (r <= k-3). The energy argument only says E is non-increasing with a
drop of >= 1 at each non-rotation step. It gives no bound on the number of consecutive pure-rotation
steps when several excess cells/holes interact, and none on the initial excess.
Splitting the orbit into "until delta_{k-1} is contained" + "after" and bounding each separately is
too weak. Exhaustive data for n = T_8 - 1: maxima 22 and 47, sum 69 > 47. So the phases must be coupled.

What would be needed: a multi-particle version of Lemma 4.4. Track the relative phase (level) of each
excess cell against each hole on the next-lower diagonal: levels rise by one per revolution and a drop
happens when a level reaches k-1. Then show that a drop at any level either resets nothing
or reduces a potential like (Phi, sum of levels) lexicographically, fast enough that the total is
<= k^2-2k-1. I did not carry this out.
