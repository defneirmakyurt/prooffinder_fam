Proved: for every $k\ge 3$, $D_B(T_k-1)\ge k^2-2k-1$, attained by $\lambda^*_k=(k-1,k-2,k-2,k-3,\dots,2,1,1)$; among partitions of $T_k-1$ with energy excess $\Phi=1$, $\lambda^*_k$ is the unique one with $d_B=k^2-2k-1$; for $k\ge 5$ every $\lambda$ with $B^{k^2-4k-2}(\lambda)=\mu_k=(k,k-1,k-1,k-3,k-4,\dots,3,1)$ has $d_B(\lambda)=k^2-2k-1$; $D_B(2)=0$, $D_B(5)=3$. Parts (a), (b) and (c) in full are established only for $4\le k\le 10$ (exhaustive exact computation); for $k\ge 11$ the upper bound (a) is a **[GAP]**, hence so are equality in (b) and the "no other partition" half of (c).

**Reading of the brief.** "Explicit functions of $k$" in (c): the maximiser sets are large ($1,6,34,175,831,3911,18163$ for $k=4,\dots,10$). So I give them as the explicit backward orbit $\{\lambda: B^{k^2-4k-2}(\lambda)=\mu_k\}$ ($k\ge 6$) rather than as a closed list. This is listed under KNOWN GAPS.

## 0. Notation

0.1. We identify a partition $\lambda=(\lambda_1,\dots,\lambda_s)$ with its diagram $C(\lambda)=\{(i,j)\in\mathbb N^2: 0\le j<\lambda_{i+1}\}$. Rows $i=0,\dots,s-1$ and columns $j$ are 0-based. A finite set $S\subset\mathbb N^2$ is the diagram of a partition iff it is an *order ideal*: $(i,j)\in S$ implies $(i-1,j)\in S$ when $i\ge1$ and $(i,j-1)\in S$ when $j\ge1$. Its rows are then initial segments, and their lengths are weakly decreasing.

0.2. The *diagonal index* of $(i,j)$ is $i+j$. Diagonal $d$ consists of the $d+1$ positions $(i,d-i)$, $0\le i\le d$; we call $i$ the *row* of the position. $D_m=\{(i,j):i+j\le m\}$ is the diagram of $\delta_{m+1}$ ($D_{-1}=\emptyset$).

0.3. The energy is $E(S)=\sum_{(i,j)\in S}(i+j)$, and $E(\lambda)=E(C(\lambda))$.

0.4. Throughout, $n=T_{k-1}+r$ with $k\ge 2$ and $1\le r\le k$; this $k$ is the rank of $n$.

## 1. Rotation lemma (R1)

1.1. Define $R$ on $\mathbb N^2$ by $R(i,j)=(i+1,j-1)$ if $j\ge1$, and $R(i,0)=(0,i)$. It preserves $i+j$. On diagonal $d$ it sends row $i$ to row $i+1$ for $i<d$ and row $d$ to row $0$, i.e. row $i\mapsto (i+1)\bmod (d+1)$. So $R$ is a bijection of each diagonal, hence injective on $\mathbb N^2$ and energy-preserving: $E(R(S))=E(S)$.

1.2. Let $\lambda$ have $s$ parts and $C=C(\lambda)$. Row $0$ of $R(C)$ is $\{(0,i):(i,0)\in C\}=\{(0,0),\dots,(0,s-1)\}$, of length $s$. For $0\le i\le s-1$, row $i+1$ of $R(C)$ is $\{(i+1,j-1):1\le j<\lambda_{i+1}\}$, i.e. columns $0,\dots,\lambda_{i+1}-2$, of length $\lambda_{i+1}-1$. So every row of $R(C)$ is an initial segment, and the row lengths in order are $\ell=(s,\lambda_1-1,\dots,\lambda_s-1)$.

1.3. **Lemma R1.** (i) If $\lambda_1\le s+1$, then $\ell$ is weakly decreasing, $R(C)$ is an order ideal, and $R(C)=C(B(\lambda))$. So $E(B(\lambda))=E(\lambda)$. (ii) If $\lambda_1\ge s+2$, then $R(C)$ is not an order ideal and $E(B(\lambda))\le E(\lambda)-1$.

*Proof.* (i) $s\ge\lambda_1-1\ge\lambda_2-1\ge\cdots\ge\lambda_s-1\ge0$. So the rows (initial segments) have weakly decreasing lengths, which makes $R(C)$ an order ideal. The zero-length rows come last. By definition $B(\lambda)$ is the list of positive entries of $\ell$ sorted decreasingly, which here is $\ell$ with its trailing zeros removed. So $C(B(\lambda))=R(C)$, and $E$ is preserved by 1.1.
(ii) Row 1 of $R(C)$ has length $\lambda_1-1>s$, so $(1,s)\in R(C)$ but $(0,s)\notin R(C)$: not an order ideal. For an arrangement $\ell=(\ell_0,\ell_1,\dots)$ of row lengths, the set of left-justified rows has energy $\sum_i\big(i\,\ell_i+\ell_i(\ell_i-1)/2\big)$. The second sum does not depend on the order, and zero rows contribute $0$. Let $\ell'$ be $\ell$ with entries $0,1$ swapped. Then $\sum_i i\ell'_i=\sum_i i\ell_i-(\lambda_1-1-s)\le\sum_i i\ell_i-1$. By the rearrangement inequality, the decreasing arrangement $\ell^{\downarrow}$ of $\ell'$ satisfies $\sum_i i\ell^{\downarrow}_i\le\sum_i i\ell'_i$. Now $C(B(\lambda))$ is the left-justified set with row lengths $\ell^{\downarrow}$ (zeros dropped at the end). Hence $E(B(\lambda))\le E(R(C))-1=E(\lambda)-1$. $\square$

1.4. **Corollary.** $E(B(\lambda))\le E(\lambda)$ always, and $E(B(\lambda))=E(\lambda)$ iff $R(C(\lambda))$ is an order ideal, in which case $C(B(\lambda))=R(C(\lambda))$. (Combine (i) and (ii); the two cases are exhaustive.)

## 2. Minimum energy and cyclicity (R2)

2.1. For finite $S\subset\mathbb N^2$ with $|S|=n$, let $N_{\ge d}(S)=\#\{x\in S:\text{diag}(x)\ge d\}$. Then $E(S)=\sum_{x\in S}\text{diag}(x)=\sum_{d\ge1}N_{\ge d}(S)$, since a cell on diagonal $e$ is counted once for each $d=1,\dots,e$.

2.2. There are exactly $T_d$ positions with diagonal $\le d-1$. So $N_{\ge d}(S)\ge n-T_d$, and also $N_{\ge d}\ge0$. Put $\nu_d=\max(0,n-T_d)$ and $g_d(S)=N_{\ge d}(S)-\nu_d\ge 0$. Since $T_d\le T_{k-1}<n$ for $d\le k-1$ and $T_d\ge T_k\ge n$ for $d\ge k$, we get $\nu_d=n-T_d$ for $1\le d\le k-1$ and $\nu_d=0$ for $d\ge k$.

2.3. Set $E_{\min}(n)=\sum_{d\ge1}\nu_d$ and $\Phi(S)=E(S)-E_{\min}(n)=\sum_{d\ge1}g_d(S)$, a sum of non-negative integers.

2.4. **Lemma.** $\Phi(S)=0$ iff $S=D_{k-2}\cup Q$ with $Q$ a set of $r$ positions on diagonal $k-1$.
*Proof.* $\Phi=0$ iff $g_d=0$ for all $d$. For $d\ge k$ this says $N_{\ge k}=0$: no cell has diagonal $\ge k$. For $1\le d\le k-1$ it says $\#\{x:\text{diag}(x)\le d-1\}=T_d$, i.e. all positions of diagonals $0,\dots,d-1$ are in $S$. Taking $d=k-1$, $D_{k-2}\subseteq S$. The remaining $n-T_{k-1}=r$ cells lie on diagonal $k-1$. The converse is the same computation read backwards. $\square$

2.5. **Lemma R2.** $\lambda\vdash n$ is cyclic iff $\Phi(\lambda)=0$.
*Proof.* By Cell 1 (assumed), the cyclic partitions are $\lambda(e)=(k-1+e_1,\dots,1+e_{k-1},e_k)$ with $e\in\{0,1\}^k$ and $\sum e=r$. Row $i$ ($0\le i\le k-1$) of $\lambda(e)$ has length $k-1-i+e_{i+1}$. So $C(\lambda(e))=D_{k-2}\cup\{(i,k-1-i):e_{i+1}=1\}$, which has $\Phi=0$ by 2.4. Conversely, suppose $\Phi(\lambda)=0$. By 2.4, $C(\lambda)=D_{k-2}\cup Q$. Set $e_{i+1}=[(i,k-1-i)\in Q]$. Then row $i$ has length $k-1-i+e_{i+1}$ for $0\le i\le k-1$ and there are no further rows. So $\lambda=\lambda(e)$ with $\sum e=r$, and $\lambda$ is cyclic by Cell 1. $\square$

2.6. **Consequence.** If $\Phi(\lambda)=1$, then $\lambda$ is not cyclic. Either $\Phi(B\lambda)=1$ and $C(B\lambda)=R(C(\lambda))$, or $\Phi(B\lambda)=0$ and $B\lambda$ is cyclic. (By 1.4 the energy stays the same or drops by $\ge 1$, and $\Phi\ge0$.)

## 3. Partitions with $\Phi=1$ (R3)

3.1. Let $\Phi(S)=1$ for an order ideal $S$ with $|S|=n$. Then there is exactly one $d^*$ with $g_{d^*}=1$, and $g_d=0$ for $d\ne d^*$.

3.2. *Case $d^*\ge k$.* Here $g_d=0$ for $d\le k-1$, so $D_{k-2}\subseteq S$ as in 2.4. For $d\ge k$, $N_{\ge d}=g_d$. $N_{\ge d}$ is non-increasing in $d$ and $N_{\ge d^*}=1$, so if $d^*>k$ then $N_{\ge k}\ge1$, contradicting $g_k=0$. Hence $d^*=k$, $N_{\ge k}=1$ and $N_{\ge k+1}=0$: exactly one cell lies off $D_{k-1}$, and it is on diagonal $k$. Diagonal $k-1$ then holds $r-1$ cells. Call this **case B**.

3.3. *Case $d^*\le k-1$.* Here $N_{\ge k}=0$. Suppose first $d^*\le k-2$. Then $\#\{\text{diag}\le d^*-1\}=T_{d^*}-1$ and $\#\{\text{diag}\le d^*\}=T_{d^*+1}$ (because $g_{d^*+1}=0$). So diagonal $d^*$ would hold $d^*+2$ cells, but it has only $d^*+1$ positions. Hence $d^*=k-1$. Diagonals $0..k-3$ are full, and diagonal $k-2$ has exactly one missing position $(i,k-2-i)$. The order-ideal property then excludes $(i,k-1-i)$ (whose left neighbour is $(i,k-2-i)$) and $(i+1,k-2-i)$ (whose upper neighbour is $(i,k-2-i)$). So diagonal $k-1$ holds at most $k-2$ cells. It holds $n-(T_{k-1}-1)=r+1$ cells, so $r\le k-3$. Call this **case A**.

3.4. **Lemma R3.** If $r\ge k-2$, every $\lambda\vdash n$ with $\Phi(\lambda)=1$ is of case B. In particular this holds for $n=T_k-1$, where $r=k-1$. (Immediate from 3.2 and 3.3.)

3.5. *Parametrising case B.* Let $2\le r\le k-1$ and $h=k-r+1$, so $2\le h\le k-1$. A case-B diagram is determined by the set $H\subseteq\{0,\dots,k-1\}$ of rows of the $h$ empty positions of diagonal $k-1$ ("holes") and the row $c\in\{0,\dots,k\}$ of the cell on diagonal $k$:
$$S(H,c)=D_{k-2}\cup\{(i,k-1-i):0\le i\le k-1,\ i\notin H\}\cup\{(c,k-c)\}.$$
Call $(H,c)$ *admissible* if ($c\ge1\Rightarrow c-1\notin H$) and ($c\le k-1\Rightarrow c\notin H$).
**Claim:** $S(H,c)$ is an order ideal iff $(H,c)$ is admissible.
*Proof.* A cell of $D_{k-2}$ has its up/left neighbours in $D_{k-3}\subseteq D_{k-2}$. A cell on diagonal $k-1$ has its neighbours on diagonal $k-2$, which is full. The cell $(c,k-c)$ has upper neighbour $(c-1,k-c)$ (present iff $c\ge1$ and $c-1\notin H$, required only if $c\ge 1$) and left neighbour $(c,k-1-c)$ (present iff $c\le k-1$ and $c\notin H$, required only if $k-c\ge1$). $\square$
The partition with diagram $S(H,c)$ is written $\Lambda(H,c)$. Its row $i$ ($0\le i\le k$) has length $k-1-i+[i\notin H]+[i=c]$ (with row $k$ of length $[c=k]$).

## 4. Exact dynamics in case B (R4)

4.1. By 1.1, $R$ maps diagonal $d$ to itself by row $i\mapsto(i+1)\bmod(d+1)$. So $R(S(H,c))=S(H+1,\,c')$, where $H+1=\{(a+1)\bmod k:a\in H\}$ and $c'=(c+1)\bmod(k+1)$. (It fixes $D_{k-2}$ setwise, permutes diagonal $k-1$ with period $k$ and diagonal $k$ with period $k+1$.)

4.2. Let $\lambda=\Lambda(H,c)$ with $(H,c)$ admissible. By 2.6 and 1.4: if $(H+1,c')$ is admissible, then $R(C(\lambda))$ is an order ideal (3.5), so $B\lambda=\Lambda(H+1,c')$, again with $\Phi=1$. Otherwise $R(C(\lambda))$ is not an order ideal, so the energy drops (1.4), so $B\lambda$ is cyclic (2.6). By induction on $t$:
$$d_B(\Lambda(H,c))=\tau(H,c):=\min\{t\ge1:\ (H+t,\ (c+t)\bmod(k+1))\text{ not admissible}\}.$$
Here $H+t$ is taken mod $k$. For $t<\tau$ the partition $B^t\lambda=\Lambda(H+t,c+t)$ has $\Phi=1$ and is not cyclic (2.5), and $B^{\tau}\lambda$ is cyclic. (Finiteness of $\tau$ follows from 4.4.)

4.3. *Reduction to one hole.* For $\alpha\in[0,k-1]$ and $\gamma\in[0,k]$, the pair $(\{\alpha\},\gamma)$ fails admissibility iff $\alpha=\gamma-1$ or $\alpha=\gamma$. The side conditions $\gamma\ge1$ and $\gamma\le k-1$ are automatic in these two equalities, because $0\le\alpha\le k-1$. So $(H,\gamma)$ is admissible iff every $(\{a\},\gamma)$, $a\in H$, is admissible. Hence $\tau(H,c)=\min_{a\in H}\tau_a$, where $\tau_a$ is the first $t\ge1$ at which $w_t:=\alpha_t-\gamma_t\in\{-1,0\}$, with $\alpha_t=(a+t)\bmod k$ and $\gamma_t=(c+t)\bmod(k+1)$.

4.4. **Lemma.** If $(\{a\},c)$ is admissible, then $\tau_a=\min\{t\ge1: a+t\equiv0\ (\mathrm{mod}\ k),\ c+t\equiv1\ (\mathrm{mod}\ k+1)\}=1-c+(k+1)\,m_a$, where $m_a=(c-1-a)\bmod k\in[0,k-1]$.
*Proof.* Suppose $w_{t-1}\notin\{-1,0\}$. We have $w_{t-1}\in[-k,k-1]$. Four cases:
(1) Neither $\alpha$ nor $\gamma$ wraps ($\alpha_{t-1}<k-1$, $\gamma_{t-1}<k$). Then $w_t=w_{t-1}\notin\{-1,0\}$.
(2) Only $\alpha$ wraps ($\alpha_{t-1}=k-1$, $\gamma_{t-1}\le k-1$). Then $w_t=w_{t-1}-k$. Since $w_{t-1}\le k-1$, this is $\le-1$, and it equals $-1$ iff $w_{t-1}=k-1$, i.e. $\gamma_{t-1}=0$, i.e. $(\alpha_t,\gamma_t)=(0,1)$.
(3) Only $\gamma$ wraps ($\gamma_{t-1}=k$, $\alpha_{t-1}\le k-2$). Then $w_t=\alpha_{t-1}+1\ge1$.
(4) Both wrap. Then $w_{t-1}=k-1-k=-1$, which is excluded.
So if $t$ is the first failure time, $w_{t-1}$ is admissible (for $t=1$ by hypothesis), and only case (2) with $(\alpha_t,\gamma_t)=(0,1)$ can fail. Conversely $(\alpha_t,\gamma_t)=(0,1)$ gives $w_t=-1$, a failure. Hence $\tau_a$ is the least $t\ge1$ with $a+t\equiv0\pmod k$ and $c+t\equiv1\pmod{k+1}$.
Solve by the Chinese remainder theorem ($\gcd(k,k+1)=1$). Write $t=1-c+(k+1)m$. Since $k+1\equiv1\pmod k$, the first congruence becomes $m\equiv c-1-a\pmod k$. So the solutions are $t=1-c+(k+1)(m_a+kq)$, $q\in\mathbb Z$. Put $t_0=1-c+(k+1)m_a$. Then $t_0\le 1+(k+1)(k-1)=k^2$, so $t_0-k(k+1)\le -k<1$. And $t_0\ge1$: if $m_a\ge1$ then $(k+1)m_a\ge k+1>c$. If $m_a=0$ then $a\equiv c-1\pmod k$; for $c\ge1$ this means $a=c-1$, which contradicts admissibility, so $c=0$ and $t_0=1$. Hence $\tau_a=t_0$. $\square$

4.5. **Lemma R4.** For admissible $(H,c)$:
$$d_B(\Lambda(H,c))=1-c+(k+1)\min_{a\in H}\big((c-1-a)\bmod k\big).$$
(From 4.2, 4.3 and 4.4.) Exact check: `out/code/check_c3.py` compares this formula with brute-force $d_B$ for every case-B partition, for $3\le k\le 10$ and $2\le r\le k-1$ (lines "(L)"). All match.

## 5. Maximum over case B (R5)

5.1. The map $a\mapsto m_a=(c-1-a)\bmod k$ is a bijection of $\{0,\dots,k-1\}$, so the $m_a$ ($a\in H$) are $h$ distinct values. Admissibility says: $c\ge1\Rightarrow m_a\ne0$ (since $a\ne c-1$), and $c\le k-1\Rightarrow m_a\ne k-1$ (since $a\ne c$ iff $c-1-a\not\equiv -1$).

5.2. The minimum of $h$ distinct integers in an interval $[x,y]$ is at most $y-h+1$. Hence:
- $c=0$: $m_a\in[0,k-2]$, so $\min m_a\le k-1-h$ and $d_B\le 1+(k+1)(k-1-h)$.
- $1\le c\le k-1$: $m_a\in[1,k-2]$, so $d_B\le 1-c+(k+1)(k-1-h)\le (k+1)(k-1-h)$.
- $c=k$: $m_a\in[1,k-1]$, so $\min m_a\le k-h$ and $d_B\le 1-k+(k+1)(k-h)=(k+1)(k-1-h)+2$.

5.3. **Lemma R5.** Over all case-B partitions of $n=T_{k-1}+r$ ($2\le r\le k-1$), $\max d_B=(k+1)(r-2)+2$. It is attained only by $c=k$ with $\{m_a\}=\{k-h,\dots,k-1\}$, i.e. $H=\{a=k-1-m\}=\{0,\dots,h-1\}$. (This $(H,c)$ is admissible: it needs $k-1\notin H$, i.e. $h\le k-1$, which holds.) Here $h=k-r+1$ gives $(k+1)(k-1-h)+2=(k+1)(r-2)+2$. The first two bullets of 5.2 are strictly smaller.

5.4. For $n=T_k-1$ ($r=k-1$, $h=2$, $k\ge3$), the maximiser is $H=\{0,1\}$, $c=k$. Its row lengths (3.5) are: row 0: $k-1$; row 1: $k-2$; row $i$ for $2\le i\le k-1$: $k-i$; row $k$: $1$. That is,
$$\lambda^*_k=(k-1,\,k-2,\,k-2,\,k-3,\,\dots,\,2,\,1,\,1),$$
with sum $(k-1)+(k-2)+T_{k-2}+1=T_k-1$. Its value is $(k+1)(k-3)+2=k^2-2k-1$. By 3.4 every $\Phi=1$ partition of $T_k-1$ is of case B. So **$\lambda^*_k$ is the unique partition of $T_k-1$ with $\Phi=1$ and $d_B=k^2-2k-1$.**

## 6. Lower bound for (b) (R6)

6.1. For every $k\ge3$, $d_B(\lambda^*_k)=k^2-2k-1$ (5.4). So $D_B(T_k-1)\ge k^2-2k-1$. Direct check with 4.5: $m_0=k-1$ and $m_1=k-2$, so $d=1-k+(k+1)(k-2)=k^2-2k-1$. Examples: $k=4$: $(3,2,2,1,1)$, $d=7$. $k=5$: $(4,3,3,2,1,1)$, $d=14$.

## 7. A large explicit family of partitions with $d_B=k^2-2k-1$ (R7)

7.1. Let $k\ge5$ and $\mu_k=\Lambda(\{k-2,k-1\},2)$. This is admissible because $1,2\notin\{k-2,k-1\}$ when $k\ge5$. By 3.5 its rows are: $k$ ($i=0$); $k-1$ ($i=1$); $k-2+1=k-1$ ($i=2$); $k-i$ for $3\le i\le k-3$; $1$ ($i=k-2$); $0$ ($i=k-1$). So
$$\mu_k=(k,k-1,k-1,k-3,k-4,\dots,3,1)\vdash T_k-1.$$
By 4.5, $m_{k-2}=(1-(k-2))\bmod k=3$ and $m_{k-1}=2$, so $d_B(\mu_k)=1-2+2(k+1)=2k+1$.

7.2. **Lemma.** If $B^m(\lambda)=\mu$ and $d_B(\mu)=j\ge1$, then $d_B(\lambda)=m+j$.
*Proof.* $B^{m+j}\lambda=B^j\mu$ is cyclic, so $d_B(\lambda)\le m+j$. The cyclic set is forward invariant: if $B^p\nu=\nu$ then $B^p(B\nu)=B(B^p\nu)=B\nu$. Suppose $B^i\lambda$ were cyclic for some $i<m+j$. If $i\le m$, then $\mu=B^{m-i}(B^i\lambda)$ would be cyclic, contradicting $j\ge1$. If $m<i<m+j$, then $B^{i-m}\mu$ would be cyclic, contradicting $d_B(\mu)=j$. $\square$

7.3. **Corollary R7.** For $k\ge5$, every $\lambda\vdash T_k-1$ with $B^{k^2-4k-2}(\lambda)=\mu_k$ satisfies $d_B(\lambda)=k^2-4k-2+2k+1=k^2-2k-1$. For instance $\lambda^*_k$ is one of them: by 4.2, $B^{t}\lambda^*_k=\Lambda(\{0,1\}+t,(k+t)\bmod(k+1))$. With $t=k^2-4k-2\equiv-2\pmod k$ and $k+t=k^2-3k-2\equiv 1+3-2=2\pmod{k+1}$, this gives $\Lambda(\{k-2,k-1\},2)=\mu_k$.

## 8. Upper bound (a) and equality in (b) (R8, R9)

8.1. **[GAP] (R8).** I have **no proof** that $d_B(\lambda)\le k^2-2k-1$ for all $k\ge4$, all $T_{k-1}<n<T_k$ and all $\lambda\vdash n$. What is proved: by 2.5 it holds for $\Phi(\lambda)=0$ ($d=0$). By 5.3, it holds for every case-B partition with $2\le r\le k-1$, with the sharper bound $(k+1)(r-2)+2\le (k+1)(k-3)+2=k^2-2k-1$. By 3.4 this covers every $\Phi=1$ partition when $r\ge k-2$. For $r=1$ there are no case-B partitions: the cell on diagonal $k$ needs at least one supporting cell on diagonal $k-1$ (3.5), but diagonal $k-1$ holds $r-1=0$ cells. Case A of $\Phi=1$ ($r\le k-3$) was not analysed, nor was anything with $\Phi\ge2$.
The missing ingredient is control of the dynamics with several cells above diagonal $k-1$ and holes on several diagonals. Empirically (exhaustive, $k\le 8$), bounding "time to reach $D_{k-2}\subseteq C$" and "time after that" separately and adding does not give $k^2-2k-1$. For $n=T_8-1$ the two maxima are $22$ and $47$. So a proof must couple the two phases.

8.2. **CHECKED (finite range).** `out/code/check_c3.py 10` computes $d_B$ for every partition of every $n$ with $T_{k-1}<n<T_k$, $2\le k\le10$ (exact integer arithmetic, full enumeration, cyclic set found by cycle detection, independent of Cell 1). It confirms $D_B(n)\le k^2-2k-1$ for all such $n$ with $4\le k\le 10$, and $D_B(T_k-1)=k^2-2k-1$ for $4\le k\le10$. This is a statement about exactly those finitely many $n$ only.

8.3. **Small $k$ for (b), by hand.**
- $k=1$: $T_1-1=0$ is not a valid $n$ (and the interval $T_0<n<T_1$ is empty).
- $k=2$, $n=2$: $B(2)=(1,1)$ and $B(1,1)=(2)$. Both partitions lie on a 2-cycle, so $D_B(2)=0$ ($\ne k^2-2k-1=-1$), and both attain it.
- $k=3$, $n=5$: we have $B(3,2)=(2,2,1)$, $B(2,2,1)=(3,1,1)$ and $B(3,1,1)=(3,2)$ (a 3-cycle, $d=0$). Also $B(5)=(4,1)$, $B(4,1)=(3,2)$, $B(2,1,1,1)=(4,1)$, $B(1^5)=(5)$. So $d=2,1,2,3$ respectively, and $D_B(5)=3$ ($\ne k^2-2k-1=2$), attained only by $(1,1,1,1,1)$. These are all 7 partitions of 5.

8.4. **Status of (b).** $D_B(T_k-1)\ge k^2-2k-1$ is proved for all $k\ge3$ (6.1). Equality is established for $4\le k\le10$ (6.1 + 8.2). For $k\ge 11$ it is conditional on R8 **[GAP]**. Values: $D_B(2)=0$, $D_B(5)=3$.

## 9. Maximisers (c) (R10)

9.1. $k=2$: $\{(2),(1,1)\}$. $k=3$: $\{(1^5)\}$ (8.3, by hand).

9.2. $k=4$: only $(3,2,2,1,1)=\lambda^*_4$. $k=5$: $\{(4,3,3,2,1,1),(4,3,2,2,2,1),(4,3,2,2,1,1,1),(3,3,3,2,2,1),(3,3,3,2,1,1,1),(3,3,2,2,2,1,1)\}$. Both are CHECKED by exhaustive computation over all partitions of $9$ and $14$.

9.3. $6\le k\le 10$ (CHECKED exhaustively): the maximisers are exactly $M_k=\{\lambda\vdash T_k-1: B^{k^2-4k-2}(\lambda)=\mu_k\}$, of sizes $34,175,831,3911,18163$.

9.4. All $k\ge 6$: $M_k\subseteq\{\lambda: d_B(\lambda)=k^2-2k-1\}$ is proved (7.3). So every element of $M_k$ attains the maximum *provided* $D_B(T_k-1)=k^2-2k-1$, which is R8 **[GAP]** for $k\ge11$. The reverse inclusion (no other maximiser) is **[GAP]** for $k\ge11$. Also, $\lambda^*_k$ is the unique maximiser with $\Phi=1$ (5.4). For $k=5$ the set $M_5$ is not the full maximiser set: $(3,3,3,2,2,1)$ reaches $(5,5,4)$ instead of $\mu_5$ after 3 steps.

## 10. What is established

- PROVED (all $k$ in stated range): R1 to R7. Lower bound $D_B(T_k-1)\ge k^2-2k-1$ ($k\ge3$). Exact $d_B$ of all $\Phi=1$ partitions of $T_k-1$, with unique maximiser $\lambda^*_k$. $d_B=k^2-2k-1$ on $M_k$ ($k\ge5$). $D_B(2)=0$, $D_B(5)=3$.
- CHECKED (finite): (a), (b), (c) for $4\le k\le 10$.
- NOT PROVED: (a) for $k\ge 11$ **[GAP]**; hence equality in (b) and completeness in (c) for $k\ge11$ **[GAP]**.
