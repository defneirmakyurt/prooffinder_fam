**Statement proved (PARTIAL relative to TARGET).** Let $k\ge 6$, $n=T_k-1$, $M_k=k^2-2k-1$, $j_k=k^2-4k-2$ and $P_k=(k,k-1,k-1,k-3,k-4,\dots,3,1)\vdash n$. (i) $d_B(P_k)=2k+1$; hence every $\lambda\vdash n$ with $B^{j_k}(\lambda)=P_k$ has $d_B(\lambda)=M_k$ (no hypothesis). (ii) Under (H), every $\lambda\in E_k$ has no $B$-preimage, i.e. $\lambda_1\le \ell(\lambda)-2$. (iii) For $4\le k\le 10$, $E_k$ is listed explicitly (exhaustive exact computation, no hypothesis). For $6\le k\le 10$, $E_k=\{\lambda: B^{j_k}(\lambda)=P_k\}$. For $k\ge 11$ two things are **not** proved: that every maximiser passes through $P_k$ (Direction 3), and a closed-form listing that does not go through preimages.

Reading adopted: "explicit description" means a rule that writes down every member directly. For $k\ge 11$ I do not have one (see KNOWN GAPS). Hypothesis (H) is used only in Step 8, where it is marked.

---

**Step 1 (notation).** For $\lambda=(\lambda_1\ge\dots\ge\lambda_\ell>0)$ write $\ell(\lambda)=\ell$. The conjugate is $\lambda'_j=\#\{i:\lambda_i\ge j\}$ for $j\ge1$, with $\lambda'_j=0$ for $j>\lambda_1$. We have $\lambda'_1=\ell(\lambda)$, $\sum_j\lambda'_j=|\lambda|$, and $\lambda\mapsto\lambda'$ is a bijection from partitions of $n$ to partitions of $n$. For a statement $S$, $[S]$ is $1$ if $S$ holds and $0$ otherwise.

**Step 2 (conjugate form of $B$).** *For every $\lambda$ with $\ell=\ell(\lambda)$ and every $j\ge1$: $(B\lambda)'_j=\lambda'_{j+1}+[j\le \ell]$.*
Proof. By definition, the multiset of parts of $B(\lambda)$ is the positive numbers among $\lambda_i-1$, together with one extra part $\ell$. The number of parts that are $\ge j$ is additive over this union. It equals $\#\{i:\lambda_i-1\ge j\}+[\ell\ge j]=\#\{i:\lambda_i\ge j+1\}+[j\le\ell]=\lambda'_{j+1}+[j\le\ell]$. (For $j\ge1$, the condition $\lambda_i-1\ge j$ already forces $\lambda_i-1>0$, so discarding the zero parts changes nothing.) $\square$

**Step 3 (all preimages).** *Let $\nu\vdash n$, $L=\nu_1=\ell(\nu')$, and $\nu'_{L+1}=0$. The partitions $\lambda$ with $B(\lambda)=\nu$ are exactly those with*
$$\lambda'=(m,\ \nu'_1-1,\dots,\nu'_m-1,\ \nu'_{m+1},\dots,\nu'_L)\quad(\text{zeros deleted}),$$
*one for each $m\in\{1,\dots,L\}$ with $\nu'_m>\nu'_{m+1}$ and $m\ge\nu'_1-1$. In particular $\nu$ has a preimage iff $\nu_1\ge\ell(\nu)-1$.*
Proof. ($\Rightarrow$) Let $B(\lambda)=\nu$ and $m=\ell(\lambda)=\lambda'_1$. By Step 2, $\lambda'_{j+1}=\nu'_j-[j\le m]$ for all $j\ge1$, so $\lambda'$ has the displayed form. Since $\lambda'$ is weakly decreasing, $m=\lambda'_1\ge\lambda'_2=\nu'_1-1$ and $\nu'_m-1=\lambda'_{m+1}\ge\lambda'_{m+2}=\nu'_{m+1}$, i.e. $\nu'_m>\nu'_{m+1}$. The last inequality gives $\nu'_m\ge1$, so $m\le L$.
($\Leftarrow$) Take such an $m$ and let $x$ be the displayed sequence. It is weakly decreasing: $m\ge\nu'_1-1$; $\nu'_j-1\ge\nu'_{j+1}-1$ for $j<m$; $\nu'_m-1\ge\nu'_{m+1}$; and $\nu'$ is decreasing beyond $m$. Its entries are nonnegative because $\nu'_j\ge\nu'_m\ge1$ for $j\le m$. It has finite support and sum $m+\sum_j\nu'_j-m=n$. So $x=\lambda'$ for a unique $\lambda\vdash n$, and $\ell(\lambda)=\lambda'_1=m$. Step 2 now gives $(B\lambda)'_j=\lambda'_{j+1}+[j\le m]=\nu'_j$, so $B(\lambda)=\nu$.
Finally, $m=L$ always satisfies $\nu'_L>0=\nu'_{L+1}$. So a preimage exists iff some $m\le L$ has $m\ge\nu'_1-1$, iff $L\ge\nu'_1-1$, iff $\nu_1\ge\ell(\nu)-1$. $\square$
(`out/code/check_Ek.py` also compares this rule with brute force on every partition of $T_k-1$, $4\le k\le10$.)

**Step 4 (behaviour of $d_B$ along orbits).** (a) If $x$ is cyclic then $B(x)$ is cyclic: from $B^i(x)=x$ we get $B^i(B(x))=B(x)$. (b) If $\lambda$ is not cyclic, then $d_B(\lambda)\ge1$ and $\{i\ge0:B^i(B\lambda)\text{ cyclic}\}=\{i\ge0:B^{i+1}(\lambda)\text{ cyclic}\}$, so $d_B(B\lambda)=d_B(\lambda)-1$. (c) If $B^j(\lambda)=\nu$ and $\nu$ is not cyclic, then by (a) none of $\lambda,B\lambda,\dots,B^{j}\lambda$ is cyclic. Applying (b) $j$ times gives $d_B(\lambda)=j+d_B(\nu)$. $\square$

**Step 5 (a $k$-cycle).** For $1\le v\le k$ let $Y_v$ be $\delta_k$ with the part $v$ decreased by $1$ (zero deleted). Then $Y_1=(k,\dots,2)$, $Y_v=(k,\dots,v+1,v-1,v-1,v-2,\dots,1)$ for $v\ge2$, and every part of every $Y_v$ is $\le k$.
- For $v\ge2$, $Y_v$ has $k$ parts. Subtracting $1$ gives $(k-1,\dots,v,v-2,v-2,\dots,0)$; the last part is $0$ and is deleted. Adding the part $k$ gives $Y_{v-1}$. (For $v=2$ the result is $(k,\dots,2)=Y_1$.)
- $Y_1$ has $k-1$ parts. Subtracting $1$ gives $(k-1,\dots,1)$. Adding $k-1$ gives $(k-1,k-1,k-2,\dots,1)=Y_k$.

So $Y_1\to Y_k\to Y_{k-1}\to\dots\to Y_2\to Y_1$, and each $Y_v$ is cyclic by definition. $\square$

**Step 6 ($d_B(P_k)=2k+1$ for every $k\ge6$).** Define the following partitions of $T_k-1$. Descending runs such as "$k,\dots,c$" are empty when $c>k$, and similarly for other runs.
- $P_k=(k,k-1,k-1,\ k-3,k-4,\dots,3,\ 1)$, with $k-1$ parts.
- $U=(k-1,k-1,k-2,k-2,\ k-4,\dots,2)$, with $k-1$ parts.
- $Q_a=(k,\dots,k-a+3,\ k-a+1,\ (k-a)^2,\ (k-a-1)^2,\ k-a-3,\dots,1)$ for $2\le a\le k-3$, with $(a-2)+1+2+2+(k-a-3)=k$ parts.
- $Q_{k-2}=(k,\dots,5,\ 3,\ 2,2,\ 1,1)$, with $k+1$ parts.
- $S_1=(k+1,\ k-1,\dots,4,\ 2,1,1)$, with $k$ parts.
- $S_2=(k,k,\ k-2,\dots,3,\ 1)$, with $k-1$ parts.
- $S_3=(k-1,k-1,k-1,\ k-3,\dots,2)$, with $k-1$ parts.
- $R_b=(k,\dots,k-b+3,\ k-b+1,\ (k-b)^3,\ k-b-2,\dots,1)$ for $2\le b\le k-2$, with $(b-2)+1+3+(k-b-2)=k$ parts.
- $R_{k-1}=(k,\dots,4,\ 2,1,1,1)$, with $k+1$ parts.
- $S_4=(k+1,\ k-1,\dots,3,\ 1)$, with $k-1$ parts.

Each is weakly decreasing: consecutive blocks drop by $1$ or $2$ as written. $|P_k|=k+2(k-1)+(3+\dots+(k-3))+1=3k-4+\tfrac{(k-3)(k-2)}2=\tfrac{k^2+k-2}2=T_k-1$. The others have the same sum because they are the images of $P_k$ computed below, and $B$ preserves the sum. The transitions follow. In each, "$-1$" means subtract $1$ from every part, and the added part is the number of parts of the source.
1. $P_k\to U$. Subtracting 1 gives $(k-1,k-2,k-2,k-4,\dots,2,0)$; delete the $0$ and add $k-1$.
2. $U\to Q_2$. Subtracting 1 gives $(k-2,k-2,k-3,k-3,k-5,\dots,1)$, all positive. Adding $k-1$ gives $(k-1,(k-2)^2,(k-3)^2,k-5,\dots,1)=Q_2$.
3. $Q_a\to Q_{a+1}$ for $2\le a\le k-4$. The tail $k-a-3,\dots,1$ is nonempty and ends in $1$. Subtracting 1 gives $(k-1,\dots,k-a+2,\ k-a,\ (k-a-1)^2,(k-a-2)^2,\ k-a-4,\dots,1,0)$; delete the $0$ and add $k$. The result is $(k,\dots,k-a+2,\ k-a,\ (k-a-1)^2,(k-a-2)^2,\ k-a-4,\dots,1)=Q_{a+1}$.
4. $Q_{k-3}\to Q_{k-2}$. Here $Q_{k-3}=(k,\dots,6,4,3,3,2,2)$ has $k$ parts. Subtracting 1 gives $(k-1,\dots,5,3,2,2,1,1)$, no zero. Adding $k$ gives $Q_{k-2}$.
5. $Q_{k-2}\to S_1$. Subtracting 1 gives $(k-1,\dots,4,2,1,1,0,0)$; delete the zeros and add $k+1$.
6. $S_1\to S_2$. Subtracting 1 gives $(k,k-2,\dots,3,1,0,0)$; delete the zeros and add $k$.
7. $S_2\to S_3$. Subtracting 1 gives $(k-1,k-1,k-3,\dots,2,0)$; delete the zero and add $k-1$.
8. $S_3\to R_2$. Subtracting 1 gives $((k-2)^3,k-4,\dots,1)$, all positive. Adding $k-1$ gives $(k-1,(k-2)^3,k-4,\dots,1)=R_2$.
9. $R_b\to R_{b+1}$ for $2\le b\le k-3$. The tail $k-b-2,\dots,1$ is nonempty and ends in $1$. Subtracting 1 gives $(k-1,\dots,k-b+2,\ k-b,\ (k-b-1)^3,\ k-b-3,\dots,1,0)$; delete the zero and add $k$. The result is $R_{b+1}$.
10. $R_{k-2}\to R_{k-1}$. Here $R_{k-2}=(k,\dots,5,3,2,2,2)$. Subtracting 1 gives $(k-1,\dots,4,2,1,1,1)$, no zero. Adding $k$ gives $R_{k-1}$.
11. $R_{k-1}\to S_4$. Subtracting 1 gives $(k-1,\dots,3,1,0,0,0)$; delete the zeros and add $k+1$.
12. $S_4\to Y_1$. Subtracting 1 gives $(k,k-2,\dots,2,0)$; delete the zero and add $k-1$. The result is $(k,k-1,\dots,2)=Y_1$.

Since $k\ge6$, the ranges in items 3 and 9 are nonempty, and all the runs used exist. So $B^i(P_k)$ is: $U$ for $i=1$; $Q_i$ for $2\le i\le k-2$; $S_1,S_2,S_3$ for $i=k-1,k,k+1$; $R_{i-k}$ for $k+2\le i\le 2k-1$; $S_4$ for $i=2k$; $Y_1$ for $i=2k+1$.
By Step 5, $Y_1$ is cyclic. $S_4$ is not cyclic: $B(S_4)=Y_1$, so every $B^i(S_4)$ with $i\ge1$ lies in $\{Y_1,\dots,Y_k\}$, whose parts are all $\le k$, while $S_4$ has the part $k+1$. By Step 4(a), none of $B^i(P_k)$ with $i\le 2k$ is cyclic (otherwise $S_4$ would be). Hence $d_B(P_k)=2k+1$. $\square$
(Independent exact check: `check_Pk.py`, $6\le k\le200$.)

**Step 7 (Direction 2, no hypothesis).** Let $k\ge6$ and $A_k=\{\lambda\vdash T_k-1: B^{j_k}(\lambda)=P_k\}$, where $j_k=k^2-4k-2\ge10$. By Step 6, $P_k$ is not cyclic. By Step 4(c), every $\lambda\in A_k$ has $d_B(\lambda)=j_k+2k+1=k^2-2k-1=M_k$. So $A_k\subseteq E_k$. Iterating Step 3 $j_k$ times, backwards from $P_k$, generates $A_k$ member by member.
[GAP] For $k\ge 13$ I do not prove that $A_k\neq\varnothing$. Nonemptiness is CHECKED for $6\le k\le 12$ (`count_anc.py`: $|A_k|=34,175,831,3911,18163,84654,394317$).

**Step 8 (uses (H)).** Let $k\ge4$ and $\lambda\in E_k$. Since $M_k\ge7>0$, $\lambda$ is not cyclic. Suppose $B(\mu)=\lambda$. Then $\mu$ is not cyclic, by Step 4(a). By Step 4(b), $d_B(\mu)=M_k+1$, which contradicts **(H)**. So $\lambda$ has no preimage, and by Step 3, $\lambda_1\le\ell(\lambda)-2$. Also under **(H)**, $E_k=\{\lambda:d_B(\lambda)\ge M_k\}=\{\lambda: B^{M_k-1}(\lambda)\text{ is not cyclic}\}$. The second equality holds because $d_B(\lambda)\ge M_k$ iff $B^{M_k-1}(\lambda)$ is not cyclic: by Step 4(a), cyclicity is inherited by images. $\square$

**Step 9 (finite range $4\le k\le 10$; exhaustive exact computation, no hypothesis).** `check_Ek.py` computes $d_B$ on every partition of $T_k-1$ directly from the definition. "Cyclic" means lying on a cycle of the finite map $B$, found by iteration. The results:
- $\max d_B=M_k$, and $|E_k|=1,6,34,175,831,3911,18163$ for $k=4,\dots,10$.
- For $6\le k\le10$, $B^{j_k}(E_k)=\{P_k\}$ and $E_k=A_k$, where $A_k$ is generated independently by Step 3.
- Every member of $E_k$ satisfies $\lambda_1\le\ell(\lambda)-2$.
- Every member of $E_k$ has conjugate in the box $\max(0,k+3-2i)\le\lambda'_i\le\max(0,2k-1-2i)$. This is a necessary condition only; the box is strictly larger than $E_k$ for $k=6,8,9,10$ (35, 834, 3935, 18330 members).

The explicit lists are in `out/code/lists/E_k.txt` for $k=4,\dots,10$. Small cases in closed form:
- $E_4=\{(3,2,2,1,1)\}$.
- $E_5=\{\lambda:\lambda'=(7,5,3,1)-e_a-e_b,\ 1\le a<b\le4\}$, i.e. $(4,3,3,2,1,1),(4,3,2,2,2,1),(4,3,2,2,1,1,1),(3,3,3,2,2,1),(3,3,3,2,1,1,1),(3,3,2,2,2,1,1)$.
- For $k=5$ the pattern differs: the orbits merge at $B^4(E_5)=\{(4,4,3,3)\}$, not at $P_5$.

So Target items 1–3 hold for $4\le k\le10$ unconditionally, with the explicit lists above.

**Step 10 (what is not established).** For $k\ge11$:
- (a) [GAP] Under (H), I do not prove that every $\lambda\in E_k$ satisfies $B^{j_k}(\lambda)=P_k$ (Direction 3).
- (b) [GAP] I have no closed-form listing of $A_k$ that avoids iterated preimages. The box of Step 9 is not exact.
- (c) [GAP] I do not prove $A_k\ne\varnothing$ for $k\ge13$.
