# Specification ledger

SPEC1: (a) must hold for every k>=4 and fail for k=3 (n=5: D_B=3>2) — the proof must use k>=4 somewhere (GH use it for k=4 by table) — CHECKED (n<=30)
SPEC2: the (a) bound is attained only at n=T_k-1 within each block (k=4..7); any proof of (a) is tight exactly there — CHECKED (n<=30)
SPEC3: tight on lambda_k=(k-1,k-2,k-2,...,2,1,1) (d_B=k^2-2k-1) — CHECKED k=4..15
SPEC4: the proof must use more than containment comparison with T_k / T_{k-1}: that relaxation gives only k^2-k at n=T_k-1 (objects (3,3,3,3,1,1), (4,4,4,2,2,1,1,1,1), (4,4,4,4,4,2,1,1,1,1,1)) — CHECKED k=5..7
SPEC5: (b) small k separately: D_B(2)=0 (k=2), D_B(5)=3 (k=3); formula k^2-2k-1 from k=4 — CHECKED
SPEC6: (c) the answer is a set of size 1,6,34,175,831,3911 (k=4..9); a finite list in k is impossible — the description must be structural — CHECKED k=4..9
SPEC7: (c) any correct description must agree with E_k = B^{-(k^2-4k-2)}(mu_k), mu_k=(k,k-1,k-1,k-3,...,3,1), for k=6..9 — CHECKED k=6..9 (k=5: B^{-4}((4,4,3,3)))
SPEC8: every extremizer makes its final drop exactly at step D-1 (entering the cycle); upper-bound arguments must be tight on orbits with 1 and with several drops — CHECKED k=4..9
SPEC9: any cited result (GH Thm 4.4) cannot stand in as the proof; the hand-in must re-prove it, and a k=4 computer step must be an exhaustive check over n in {7,8,9} (67 partitions) with code — per TARGET/G6/G7
