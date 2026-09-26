| claim | status | where proved |
|---|---|---|
| $(B\lambda)'_j=\lambda'_{j+1}+[j\le\ell(\lambda)]$ | PROVED | proof.md Step 2 |
| Preimage rule; $\nu$ has a preimage iff $\nu_1\ge\ell(\nu)-1$ | PROVED (+ CHECKED k=4..10 vs brute force) | proof.md Step 3; code/check_Ek.py |
| $d_B(B\lambda)=d_B(\lambda)-1$ for non-cyclic $\lambda$; $B^j\lambda=\nu$ non-cyclic gives $d_B(\lambda)=j+d_B(\nu)$ | PROVED | proof.md Step 4 |
| $Y_1\to Y_k\to\dots\to Y_2\to Y_1$ is a $k$-cycle | PROVED | proof.md Step 5 |
| $d_B(P_k)=2k+1$ for all $k\ge6$ | PROVED (+ CHECKED k=6..200) | proof.md Step 6; code/check_Pk.py |
| Every $\lambda$ with $B^{j_k}\lambda=P_k$ has $d_B=M_k$ ($k\ge6$, no hypothesis) | PROVED | proof.md Step 7 |
| $A_k\ne\varnothing$ | CHECKED k=6..12 only; GAP k>=13 | code/count_anc.py |
| Under (H): every maximiser has $\lambda_1\le\ell(\lambda)-2$; $E_k=\{B^{M_k-1}\lambda$ not cyclic$\}$ | PROVED (uses H) | proof.md Step 8 |
| Explicit lists of $E_k$, $4\le k\le10$; counts 1,6,34,175,831,3911,18163 | CHECKED | proof.md Step 9; code/check_Ek.py, code/list_Ek.py, code/lists/ |
| $E_k=A_k$ for $6\le k\le10$ | CHECKED | code/check_Ek.py |
| Conjugate box is necessary for $E_k$, $k\le10$ | CHECKED | code/check_Ek.py |
| Conjugate box is an exact description of $E_k$ | REFUTED (k=6: (8,6,4,2)' is in the box, $d_B=11$) | proof.md Step 9 |
| Under (H), $E_k=A_k$ for all $k\ge11$ | GAP | proof.md Step 10(a) |
| Closed-form listing of $E_k$ for general $k$ | GAP | proof.md Step 10(b) |
