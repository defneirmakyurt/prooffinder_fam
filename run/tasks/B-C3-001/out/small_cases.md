# Small cases (all CHECKED by exact enumeration; scripts in out/checks/)

D_B(n), n=1..30 (small_cases.py 30, COMPLETED 0.1 s) -- agrees with Griggs-Ho Figure 1 (n=4..36) on all overlapping n:
n : 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30
D : 0 0 2 2 3 6 4 5 7 12  8  8  9 14 20 15 12 13 16 23 30 24 18 18 19 26 34 42 35 28
(a) slack k^2-2k-1 - D_B(n) over non-triangular n, k=4..7: min slack 0, attained only at n=T_k-1 (n=9,14,20,27); CHECKED n<=30.
Violations of the (a) bound for k<4: n=2 (D=0 > -1), n=4,5 (k=3: D=2,3 vs 2: n=5 violates). k>=4 needed (n=5 is the k=3 exception).

(b) D_B(T_k-1): k=2: 0 (n=2); k=3: 3 (n=5); k=4..9: 7,14,23,34,47,62 = k^2-2k-1. CHECKED k=2..9 (tk_minus_1.py, merge.py).
Griggs-Ho construction lambda_k=(k-1,k-2,k-2,k-3,...,2,1,1) has d_B=k^2-2k-1 for k=4..15 (translations.py; exact simulation).

(c) extremizer set E_k for n=T_k-1: |E_k| = 1, 6, 34, 175, 831, 3911 for k=4..9 (OEIS: no match).
 k=4: E={(3,2,2,1,1)}.  k=5: E={(4,3,3,2,1,1),(4,3,2,2,2,1),(4,3,2,2,1,1,1),(3,3,3,2,2,1),(3,3,3,2,1,1,1),(3,3,2,2,2,1,1)}.
 k=6: 34 partitions listed by tk_minus_1.py.
 Structure CHECKED k=6..9 (merge.py, 2.5 s): all of E_k first coincide after L_k=k^2-4k-2 shifts, at
   mu_k=(k,k-1,k-1,k-3,k-4,...,3,1), d_B(mu_k)=2k+1, and E_k = {lambda |- T_k-1 : B^{L_k}(lambda)=mu_k} exactly.
   (k=5: merge after 4 steps at (4,4,3,3), d=10, E_5 = B^{-4}((4,4,3,3)).)  B is injective on E_k (|B(E_k)|=|E_k|).
 Drop events (energy = sum of diagonal indices strictly decreases) along extremal transients: every extremizer's
   last drop is at step D-1 (entry into the cycle); the Griggs-Ho lambda_k has exactly one drop. CHECKED k=4..9 (ext_drops.py).
Extremizers from the literature: Griggs-Ho Thm 4.4(2) lambda_k above (PROVED there, argument sketched "imitating Thm 3.1").
