# Stuck point

SP5 (= entry inequality (EI) for t_C >= 1, proof.md 4.1/4.3): partitions outside C_k.

Proved: cells never move to a higher diagonal (Lemma 1). So "diagonals 0..k-2 full" and "nothing on diagonals >= k+1" are
absorbing, and d_B = t_C + d_B(state at entry). Inside C_k the bound is B-C3-004 Thm 6.1.

Where it fails: bounding t_C alone and adding the worst C_k time is too weak. Exact data for k=4..8:
max t_C + max(d-t_C) = 12,23,38,58,82, against the bound 7,14,23,34,47. A proof must show that a late entry into C_k
lands in a configuration with little remaining time. In B-C3-004's frame that means the particles on diagonal k
arrive with their hole labels "in phase". No monotone phase quantity valid outside C_k was found in the time box.

Primary literature (Griggs-Ho 1998; Etienne 1991 Thm 5.1) could not be opened: HTTP 403 for automated fetch,
no mirror found.
