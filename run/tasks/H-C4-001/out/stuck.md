# Stuck

none for the target: both values U(Q_7) = 464 and U(Q_8) = 1040 have an attaining labelling (checker
VERIFIED) and a lower-bound proof (Lemma A + Lemma C + exhaustive F_5 = 18).

Observation for later cells (not part of this claim): the same chain gives only
U(Q_9) >= 2^9 + 8 * (512 - 2*144) = 2304 (via F_9 <= 2 F_8 <= 288), well below what the statement quotes
for Q_9, so the doubling bound F_d <= 2 F_{d-1} is presumably not tight at d = 9; beyond d = 8 the
lower-bound route needs F_8 or F_9 computed directly (not attempted here).
