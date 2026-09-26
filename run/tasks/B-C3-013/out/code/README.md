# Code for B-C3-013 (stdlib only, exact integer arithmetic)

Run from this directory with plain `python3`:

- `python3 check_Ek.py 4 10`
  - Computes $d_B$ exhaustively on all partitions of $T_k-1$ for $k=4..10$. "Cyclic" means lying on a cycle of $B$, which is definitional.
  - Checks: $\max d_B=M_k$; $|E_k|$; the preimage rule of proof.md Step 3 against brute force on every partition; every maximiser has $\lambda_1\le\ell-2$; the conjugate box is a necessary condition; for $k\ge6$, $B^{j_k}(E_k)=\{P_k\}$, $d_B(P_k)=2k+1$, and $E_k$ equals the set of depth-$j_k$ ancestors of $P_k$.
  - Measured: real 16.69 s. Output ends `ALL OK`.
- `python3 check_Pk.py 6 200`
  - Checks, directly from the definition of cyclic, that $d_B(P_k)=2k+1$ for $6\le k\le200$.
  - Measured: real 0.36 s. Output: True.
- `python3 count_anc.py 6 7 8 9 10 11 12`
  - Computes $|A_k|$ by backward search with the Step-3 rule: 34, 175, 831, 3911, 18163, 84654, 394317.
  - Measured: real 187.10 s (timed separately from check_Pk.py).
- `python3 list_Ek.py 4 10`
  - Writes the explicit lists `lists/E_k.txt`.
  - Measured: real 5.53 s.

`../tmp/` holds exploration scripts only; nothing in the proof rests on them.
