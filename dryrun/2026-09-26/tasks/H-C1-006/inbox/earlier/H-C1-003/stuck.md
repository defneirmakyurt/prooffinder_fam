# Stuck: H-C1-003

Nothing blocks the target: U(Q_3) = 14 and U(Q_4) = 34 are both settled, each with an explicit
attaining labelling scored by the provided checker and an exhaustive exact lower-bound search.

Where things would stall next (not part of this cell):
* The two controls that deliberately weaken the pruning both TIMED OUT at d = 4
  (dp_lower.py 4 33 --no-prune, 10 min; bb_lower.py 4 33 --no-fix --basic, 7 min). So the
  strength of the edge term in LB is what makes the Q_4 lower bound cheap; its correctness is
  argued in full in out/claims.md, not assumed.
* Scaling: dp_lower.py stores states keyed by (placed set, N on the boundary). For d = 5 the
  placed sets alone number 2^32, so this DP as written will not reach Q_5 without a genuinely
  different state space (e.g. a layered/profile encoding, or a lower bound proved by hand).
  I did not attempt d >= 5 in this cell.
* I have no proof of any general formula for U(Q_d). The three data points I established
  exactly are U(Q_2) = 5, U(Q_3) = 14, U(Q_4) = 34. A finite check proves nothing beyond them.
