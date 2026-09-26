Proved here (less than TARGET): for every partition $\lambda$ and every $e\ge 0$, $N_{\ge e}(B\lambda)\le N_{\ge e}(\lambda)$ (no cell ever moves to a higher diagonal). Consequently, for $n=T_{k-1}+r$ with $1\le r\le k-1$, the class $\mathcal C_k=\{\lambda: D_{k-2}\subseteq C(\lambda)\subseteq D_k\}$ is forward invariant, contains every cyclic partition, and $d_B(\lambda)=t_C(\lambda)+d_B(B^{t_C(\lambda)}\lambda)$. So target (a) is **equivalent** to: $d_B(B^{t_C}\lambda)\le k^2-2k-1-t_C(\lambda)$ for all $\lambda$. **Target (a) itself is NOT proved here [GAP], for any $k\ge 11$.**

Reading: 0-based rows and columns. Cell $(i,j)$ lies on diagonal $i+j$. Row $i$ of $C(\lambda)$ has length $\lambda_{i+1}$. $D_m=\{(i,j):i+j\le m\}$ ($D_{-1}=\emptyset$) has exactly $T_{m+1}$ positions. $N_{\ge e}(S)=\#\{(i,j)\in S: i+j\ge e\}$.

## 1. Lemma 1 (diagonal monotonicity)

1.1. Let $\lambda=(\lambda_1,\dots,\lambda_s)$ have $s$ parts. For a finite sequence $\ell=(\ell_0,\dots,\ell_M)$ of non-negative integers put $L(\ell)=\{(i,j):0\le i\le M,\ 0\le j<\ell_i\}$ and $F_e(\ell)=\#\{(i,j)\in L(\ell):i+j\ge e\}$. Row $i$ contributes the columns $j$ with $\max(0,e-i)\le j\le \ell_i-1$, so $F_e(\ell)=\sum_i f_i(\ell_i)$ with $f_i(x)=\big(x-(e-i)^+\big)^+$.

1.2. Define $R(i,j)=(i+1,j-1)$ for $j\ge1$ and $R(i,0)=(0,i)$. $R$ preserves $i+j$. On diagonal $d$ it maps row $i$ to row $i+1$ for $i<d$ and row $d$ to row $0$, so it is injective. Row $0$ of $R(C(\lambda))$ is $\{(0,i):(i,0)\in C(\lambda)\}=\{(0,0),\dots,(0,s-1)\}$. For $0\le i\le s-1$, row $i+1$ of $R(C(\lambda))$ is $\{(i+1,j-1):1\le j\le\lambda_{i+1}-1\}$, i.e. columns $0,\dots,\lambda_{i+1}-2$. Hence $R(C(\lambda))=L(\ell)$ with $\ell=(s,\lambda_1-1,\dots,\lambda_s-1)$, and $F_e(\ell)=N_{\ge e}(\lambda)$ because $R$ is an injective diagonal-preserving map.

1.3. *Swap step.* Suppose $\ell_i<\ell_{i+1}$ and let $\ell'$ be $\ell$ with these two entries exchanged. Put $a=(e-i)^+$ and $b=(e-i-1)^+$, so $a\ge b$. Then $F_e(\ell')-F_e(\ell)=g(\ell_{i+1})-g(\ell_i)$, where $g(x)=(x-a)^+-(x-b)^+$. For integers $x\ge0$ we have $(x-b)^+-(x-a)^+=\#\{y\in\mathbb Z: b\le y<a,\ y<x\}$, which is non-decreasing in $x$. So $g$ is non-increasing, and $\ell_{i+1}>\ell_i$ gives $F_e(\ell')\le F_e(\ell)$.

1.4. *Sorting.* Each swap in 1.3 lowers the number of pairs $i<i'$ with $\ell_i<\ell_{i'}$ by exactly one. The swapped pair stops being such a pair, and every other pair keeps its status or is exchanged with another such pair. When no adjacent pair with $\ell_i<\ell_{i+1}$ remains, the sequence is weakly decreasing. So finitely many swaps turn $\ell$ into its weakly decreasing rearrangement $\ell^{\downarrow}$, and by 1.3, $F_e(\ell^{\downarrow})\le F_e(\ell)$.

1.5. By definition the parts of $B(\lambda)$ are the positive entries of $\ell$, in decreasing order. The zero entries of $\ell^{\downarrow}$ come last and contribute no cells. So $L(\ell^{\downarrow})=C(B\lambda)$. **Lemma 1:** $N_{\ge e}(B\lambda)=F_e(\ell^{\downarrow})\le F_e(\ell)=N_{\ge e}(\lambda)$ for every $e\ge0$. $\square$

## 2. Corollary 2 (forward invariance)

Let $\lambda\vdash n$ and $m\ge -1$, $e\ge0$.
(i) If $N_{\ge e}(\lambda)=0$ then $N_{\ge e}(B\lambda)=0$. (Lemma 1, and $N\ge0$.)
(ii) If $D_m\subseteq C(\lambda)$ then $D_m\subseteq C(B\lambda)$. *Proof.* For any $n$-cell set $S$, $\#\{x\in S:\operatorname{diag}x\le m\}=n-N_{\ge m+1}(S)\le T_{m+1}$, with equality iff $D_m\subseteq S$ (there are exactly $T_{m+1}$ positions on diagonals $\le m$). By Lemma 1, $n-N_{\ge m+1}(B\lambda)\ge n-N_{\ge m+1}(\lambda)=T_{m+1}$. Hence equality holds. $\square$
(iii) So $\mathcal C_k=\{\lambda: D_{k-2}\subseteq C(\lambda)\text{ and }N_{\ge k+1}(\lambda)=0\}$ satisfies $B(\mathcal C_k)\subseteq\mathcal C_k$. Also $\{\lambda:D_{k-2}\subseteq C(\lambda)\}$ and $\{\lambda:N_{\ge k+1}(\lambda)=0\}$ are each forward invariant, so $t_C=\max(t_A,t_B)$ with $t_A,t_B$ their entry times.

## 3. Lemma 3 (cyclic partitions lie in $\mathcal C_k$; entry decomposition)

3.1. Let $n=T_{k-1}+r$, $1\le r\le k-1$. By Cell 1 (ASSUMPTIONS), $\lambda\vdash n$ is cyclic iff $\lambda=(k-1+e_1,\dots,1+e_{k-1},e_k)$ with $e\in\{0,1\}^k$, $\sum e=r$. Row $i$ ($0\le i\le k-1$) of this partition has length $k-1-i+e_{i+1}$. Row $i$ of $D_{k-2}$ has length $k-1-i$, row $i$ of $D_{k-1}$ has length $k-i$, and $D_{k-1}$ has no row $\ge k$. So $D_{k-2}\subseteq C(\lambda)\subseteq D_{k-1}\subseteq D_k$. Hence every cyclic partition lies in $\mathcal C_k$.

3.2. Put $t_C(\lambda)=\min\{t\ge0:B^t\lambda\in\mathcal C_k\}$. Since $B^{d_B(\lambda)}\lambda$ is cyclic, 3.1 gives $t_C(\lambda)\le d_B(\lambda)$. The cyclic set is forward invariant: if $B^p\nu=\nu$ with $p\ge1$, then $B^p(B\nu)=B\nu$. Let $\mu=B^{t_C}\lambda$. Then $B^{t_C+d_B(\mu)}\lambda=B^{d_B(\mu)}\mu$ is cyclic, so $d_B(\lambda)\le t_C+d_B(\mu)$. Also $B^{d_B(\lambda)-t_C}\mu=B^{d_B(\lambda)}\lambda$ is cyclic, so $d_B(\mu)\le d_B(\lambda)-t_C$. **Hence $d_B(\lambda)=t_C(\lambda)+d_B(B^{t_C(\lambda)}\lambda)$.** $\square$

## 4. What this gives for the target

4.1. By 3.2, target (a) is equivalent to the **entry inequality**
$$(\mathrm{EI})\qquad d_B\big(B^{t_C(\lambda)}\lambda\big)\le k^2-2k-1-t_C(\lambda)\quad\text{for all }\lambda\vdash n,\ T_{k-1}<n<T_k,\ k\ge4 .$$

4.2. Case $t_C(\lambda)=0$ (i.e. $\lambda\in\mathcal C_k$): (EI) is Theorem 6.1 of task B-C3-004 (proved there for all $k\ge3$ by a hole-label/particle counting argument; not gated; not reproduced here). Credit: B-C3-004.

4.3. Case $t_C(\lambda)\ge1$: **[GAP]**. Not proved here. (EI) cannot come from a bound on $t_C$ plus the worst case in $\mathcal C_k$: `code/phase_stats.py` (exact, exhaustive, $4\le k\le8$) gives $\max t_C+\max_\lambda(d_B-t_C)=12,23,38,58,82$, against $k^2-2k-1=7,14,23,34,47$. See why_not.md.

4.4. Finite range: (a) holds for $4\le k\le 10$ by the exhaustive exact computations of B-C3-002 (`check_c3.py`) and B-C3-004 (`check_small.py 10`), and for $4\le k\le8$ by `code/phase_stats.py` here. This proves nothing for $k\ge 11$.

## 5. Established / not established
- PROVED here: Lemma 1, Corollary 2, Lemma 3, and the equivalence (a) $\iff$ (EI).
- PROVED elsewhere (credited, not gated): (EI) when $t_C=0$ (B-C3-004 Thm 6.1).
- NOT PROVED: (EI) for $t_C\ge1$, hence (a) and the upper half of (b), for $k\ge11$. **[GAP]**
