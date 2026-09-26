**Statement proved.** For every $k\ge 1$: every partition of $T_k$ reaches $\delta_k$ under $B$, $\delta_k$ is the only cyclic partition of $T_k$, and $D_B(T_k)\ge k^2-k$, with the explicit partition $\lambda^{(k)}$ below satisfying $d_B(\lambda^{(k)})=k^2-k$ exactly. The matching upper bound $D_B(T_k)\le k^2-k$ (hence $D_B(T_k)=k^2-k$) is established only for $1\le k\le 11$, by an exhaustive exact computation over the finite set to which Step 6 reduces it; for $k\ge 12$ the upper bound is a **[GAP]** (Step 9).

Proposed formula: $F(k)=k^2-k$ for every $k\ge1$ (no small-$k$ exceptions: $F(1)=0$, $F(2)=2$).

Witness: $\lambda^{(1)}=(1)$, and for $k\ge 2$
$$\lambda^{(k)}=(k-1,\;k-1,\;k-2,\;\ldots,\;2,\;1,\;1),\qquad\text{i.e. } \lambda^{(k)}_1=k-1,\ \lambda^{(k)}_i=k+1-i\ (2\le i\le k),\ \lambda^{(k)}_{k+1}=1 .$$
Its sum is $(k-1)+\sum_{i=2}^{k}(k+1-i)+1=k+T_{k-1}=T_k$. For $k=2$ it is $(1,1,1)$.

Reading of the brief (no ambiguity found): "cyclic", $d_B$, $D_B$ are exactly as in the statement; nothing about cyclic partitions is assumed, it is proved in Steps 3–6.

---

## Step 0. Diagrams

**0.1 (Definition).** For a partition $\lambda=(\lambda_1,\ldots,\lambda_s)$ put $Y(\lambda)=\{(i,j)\in\mathbb Z_{\ge1}^2: 1\le i\le s,\ 1\le j\le\lambda_i\}$. The *diagonal index* of a cell $(i,j)$ is $w(i,j)=i+j-1$. For $d\ge1$ let $\Delta_d=\{(i,d+1-i):1\le i\le d\}$, the $d$ positions with $w=d$; we call $(i,d+1-i)$ *position $i$ of $\Delta_d$*.

**0.2 (Lemma).** A finite set $Y\subset\mathbb Z_{\ge1}^2$ equals $Y(\lambda)$ for some partition $\lambda$ (of $|Y|$) if and only if $Y$ is *down-closed*: $(i,j)\in Y,\ 1\le i'\le i,\ 1\le j'\le j\Rightarrow (i',j')\in Y$. Moreover $Y$ is down-closed if and only if every row $\{j:(i,j)\in Y\}$ and every column $\{i:(i,j)\in Y\}$ is an initial segment $\{1,\ldots,m\}$ ($m\ge0$). Also, if every row of $Y$ is an initial segment of length $\ell_i$ and $\ell_1\ge\ell_2\ge\cdots$, then $Y$ is down-closed and $Y=Y(\mu)$ where $\mu$ is the sequence of positive $\ell_i$.

*Proof.* If $Y=Y(\lambda)$ and $(i,j)\in Y$, $i'\le i$, $j'\le j$, then $j'\le j\le\lambda_i\le\lambda_{i'}$, so $(i',j')\in Y$. Conversely let $Y$ be down-closed and $\ell_i=\#\{j:(i,j)\in Y\}$. Down-closure in $j$ makes row $i$ equal to $\{1,\ldots,\ell_i\}$; $(i+1,j)\in Y\Rightarrow(i,j)\in Y$ gives $\ell_i\ge\ell_{i+1}$; so $Y=Y(\mu)$ with $\mu$ the positive $\ell_i$ (which form an initial run of indices since $\ell$ is weakly decreasing). If all rows and columns are initial segments and $(i,j)\in Y$, $i'\le i$, $j'\le j$: the column of $j$ is an initial segment containing $i$, so $(i',j)\in Y$; the row of $i'$ is an initial segment containing $j$, so $(i',j')\in Y$. The converse (down-closed $\Rightarrow$ rows and columns initial segments) is immediate from the definition with $i'=i$ or $j'=j$. Finally, if rows are initial segments with $\ell_1\ge\ell_2\ge\cdots$ and $(i,j)\in Y$, $i'\le i$, $j'\le j$, then $j'\le j\le\ell_i\le\ell_{i'}$, so $(i',j')\in Y$; the last claim follows from the first part. $\square$

## Step 1. The rotation

Fix $\lambda=(\lambda_1,\ldots,\lambda_s)$, $Y=Y(\lambda)$. Define $\rho:Y\to\mathbb Z_{\ge1}^2$ by $\rho(i,j)=(i+1,j-1)$ if $j\ge2$, and $\rho(i,1)=(1,i)$.

**1.1** $w(\rho(c))=w(c)$ for every $c\in Y$: $(i+1)+(j-1)-1=i+j-1$ and $1+i-1=i=w(i,1)$.

**1.2** $\rho$ is injective: images of cells with $j\ge2$ lie in rows $\ge2$ and $(i,j)\mapsto(i+1,j-1)$ is injective; images of column-1 cells lie in row 1 and $(i,1)\mapsto(1,i)$ is injective.

**1.3** On $\Delta_d$, $\rho$ sends position $i$ to position $\pi_d(i)$, where $\pi_d(i)=i+1$ for $i<d$ and $\pi_d(d)=1$. Indeed position $i<d$ is $(i,d+1-i)$ with $d+1-i\ge2$, mapped to $(i+1,d-i)$ = position $i+1$; position $d$ is $(d,1)$, mapped to $(1,d)$ = position 1. So $\pi_d$ is a cyclic permutation of $\{1,\ldots,d\}$ and $\pi_d^t(i)=1+((i-1+t)\bmod d)$.

**1.4** Row $m$ of $\rho(Y)$ is $\{(m,j):1\le j\le r_m\}$ with $r_1=s$, $r_m=\lambda_{m-1}-1$ for $2\le m\le s+1$, $r_m=0$ for $m\ge s+2$. Proof: row 1 of $\rho(Y)$ consists of the images $(1,i)$ of $(i,1)$, $1\le i\le s$; for $m\ge2$, row $m$ consists of the images $(m,j-1)$ of $(m-1,j)$, $2\le j\le\lambda_{m-1}$ (none if $m-1>s$).

**1.5** By the definition of $B$, the parts of $B(\lambda)$ are exactly the positive entries of $(r_1,\ldots,r_{s+1})$ (namely $s$ and the positive $\lambda_i-1$), arranged in weakly decreasing order.

**1.6** If $\rho(Y)$ is down-closed, then $Y(B(\lambda))=\rho(Y)$. Proof: by 0.2, $\rho(Y)=Y(\mu)$ where the rows of $\rho(Y)$ have lengths $r_1\ge r_2\ge\cdots$ (down-closure gives $r_m\ge r_{m+1}$), so $\mu$ is the sequence of positive $r_m$ in order, which by 1.5 is $B(\lambda)$.

## Step 2. Energy does not increase

Define $E(\lambda)=\sum_{c\in Y(\lambda)}w(c)$. For a finitely supported sequence $a=(a_1,a_2,\ldots)$ of non-negative integers put
$$\Phi(a)=\sum_{m\ge1}\sum_{j=1}^{a_m}(m+j-1)=\sum_{m\ge1}\Big(m\,a_m+\tfrac{a_m(a_m-1)}{2}\Big),$$
the $w$-sum of the set whose row $m$ is $\{1,\ldots,a_m\}$.

**2.1 (Lemma).** Let $a^{\downarrow}$ be the weakly decreasing rearrangement of $a$ (same multiset of entries, zeros included). Then $\Phi(a^\downarrow)\le\Phi(a)$, with equality only if $a=a^\downarrow$.

*Proof.* $\sum_m a_m(a_m-1)/2$ is unchanged by rearrangement. Write $\sum_m m\,a_m=\sum_{m\ge1}\tau_m(a)$ with tail sums $\tau_m(a)=\sum_{m'\ge m}a_{m'}=A-\sum_{m'<m}a_{m'}$, $A=\sum a$. The sum of the first $m-1$ entries of $a$ is at most the sum of the $m-1$ largest entries, which is the sum of the first $m-1$ entries of $a^\downarrow$; hence $\tau_m(a)\ge\tau_m(a^\downarrow)$ for all $m$. If $a\ne a^\downarrow$, let $m_0$ be the first index with $a_{m_0}\ne a^\downarrow_{m_0}$. The entries $a_1,\ldots,a_{m_0-1}$ equal $a^\downarrow_1,\ldots,a^\downarrow_{m_0-1}$, which are $m_0-1$ largest entries of the multiset; $a^\downarrow_{m_0}$ is the largest entry of the remaining multiset and $a_{m_0}$ belongs to that remaining multiset, so $a_{m_0}<a^\downarrow_{m_0}$. Then $\tau_{m_0+1}(a)>\tau_{m_0+1}(a^\downarrow)$, so the inequality is strict. $\square$

**2.2 (Proposition).** $E(B(\lambda))\le E(\lambda)$, and if equality holds then $Y(B(\lambda))=\rho(Y(\lambda))$.

*Proof.* By 1.1–1.2, $E(\lambda)=\sum_{c\in\rho(Y)}w(c)=\Phi(r)$ with $r=(r_1,\ldots,r_{s+1},0,\ldots)$ from 1.4. By 1.5, $Y(B(\lambda))$ has row $m$ equal to $\{1,\ldots,r^\downarrow_m\}$, so $E(B(\lambda))=\Phi(r^\downarrow)\le\Phi(r)$ by 2.1. If equality holds, 2.1 gives $r=r^\downarrow$, i.e. the row lengths of $\rho(Y)$ are weakly decreasing; its rows are initial segments (1.4), so $\rho(Y)$ is down-closed (0.2) and $Y(B(\lambda))=\rho(Y)$ by 1.6. $\square$

## Step 3. Minimum energy on $T_k$; the fixed point

**3.1** $Y(\delta_k)=\bigcup_{d=1}^{k}\Delta_d$: row $i$ of $Y(\delta_k)$ is $\{1,\ldots,k+1-i\}$, i.e. the cells with $i+j-1\le k$.

**3.2** $B(\delta_k)=\delta_k$: the positive numbers among $k-1,\ldots,1,0$ are $k-1,\ldots,1$; adding the part $s=k$ gives $(k,k-1,\ldots,1)$.

**3.3 (Lemma).** Let $\lambda\vdash T_k$, $N_d=|Y(\lambda)\cap\Delta_d|\le d$. Then $E(\lambda)\ge E_k:=\sum_{d=1}^k d^2$, with equality iff $\lambda=\delta_k$. Moreover, if $\lambda\ne\delta_k$ then $Y(\lambda)$ has a cell in some $\Delta_D$ with $D\ge k+1$ and misses some position of some $\Delta_d$ with $d\le k$.

*Proof.* $E(\lambda)-E_k=\sum_{d\le k}d(N_d-d)+\sum_{d>k}dN_d$. For $d\le k$, $N_d-d\le0$ so $d(N_d-d)\ge k(N_d-d)$; and $\sum_{d>k}dN_d\ge(k+1)\sum_{d>k}N_d$. Using $\sum_d N_d=T_k=\sum_{d\le k}d$, we get $E(\lambda)-E_k\ge k\big(-\sum_{d>k}N_d\big)+(k+1)\sum_{d>k}N_d=\sum_{d>k}N_d\ge0$. If $\lambda\ne\delta_k$, then $Y(\lambda)\ne\bigcup_{d\le k}\Delta_d$ (3.1); both sets have $T_k$ elements, so $Y(\lambda)$ has a cell outside $\bigcup_{d\le k}\Delta_d$ (so $\sum_{d>k}N_d\ge1$ and $E(\lambda)>E_k$) and misses a position inside it. If $\lambda=\delta_k$, $E=E_k$ by 3.1. $\square$

## Step 4. Pure rotation forever forces $\delta_k$

**4.1 (Lemma).** Let $\lambda\vdash T_k$, $Y_t=Y(B^t(\lambda))$, and suppose $Y_{t+1}=\rho(Y_t)$ for every $t\ge0$ (here $\rho$ is the rotation of $Y_t$). Then $\lambda=\delta_k$.

*Proof.* Suppose $\lambda\ne\delta_k$. By 3.3 there are $D\ge k+1$ and a position $i_0$ of $\Delta_D$ in $Y_0$, and $d\le k$ and a position $a_0$ of $\Delta_d$ not in $Y_0$. Since $\rho$ preserves $w$ (1.1) and acts on $\Delta_e$ by $\pi_e$ (1.3), $Y_{t+1}\cap\Delta_e=\rho(Y_t\cap\Delta_e)$, and $\pi_e$ is a bijection of the positions of $\Delta_e$; by induction on $t$, position $\pi_D^t(i_0)$ of $\Delta_D$ lies in $Y_t$ and position $\pi_d^t(a_0)$ of $\Delta_d$ does not.

Let $t_0\in\{0,\ldots,d-1\}$ with $t_0\equiv 1-a_0\pmod d$ and consider $t=t_0+md$, $m\ge0$; then $\pi_d^t(a_0)=1+((a_0-1+t)\bmod d)=1$. Let $g=\gcd(d,D)$. By Bézout's identity, $g=xd+yD$ for some integers $x,y$; replacing $(x,y)$ by $(x+nD,\,y-nd)$ for a large integer $n\ge0$ keeps the identity and makes $x\ge0$. Then for every $c\ge0$, $m=cx$ gives $md\equiv cg\pmod D$. Hence, as $m$ ranges over $\mathbb Z_{\ge0}$, $(i_0-1+t_0+md)\bmod D$ takes every value in $\{0,\ldots,D-1\}$ that is $\equiv i_0-1+t_0\pmod g$. Since $g\mid D-d$ and $D-d\ge1$, $g\le D-d$, so the $D-d+1$ consecutive integers $\{0,\ldots,D-d\}\subseteq\{0,\ldots,D-1\}$ contain such a value. Thus there is $t$ with $\pi_d^t(a_0)=1$ and $i^*:=\pi_D^t(i_0)\in\{1,\ldots,D-d+1\}$.

At that $t$, the cell $(i^*,D+1-i^*)$ is in $Y_t$ and $D+1-i^*\ge d$, so by down-closure (0.2) $(1,d)\in Y_t$. But $(1,d)$ is position $1=\pi_d^t(a_0)$ of $\Delta_d$, which is not in $Y_t$. Contradiction. $\square$

## Step 5. Every partition of $T_k$ reaches $\delta_k$

**5.1** Let $\lambda\vdash T_k$. By 2.2 and 3.3, $(E(B^t\lambda))_{t\ge0}$ is a non-increasing sequence of integers bounded below by $E_k$, hence constant from some $t_0$ on. By the equality clause of 2.2, $Y(B^{t+1}\lambda)=\rho(Y(B^t\lambda))$ for all $t\ge t_0$. Applying 4.1 to $\mu=B^{t_0}\lambda$ gives $B^{t_0}\lambda=\delta_k$.

## Step 6. $\delta_k$ is the only cyclic partition; $d_B$ is a hitting time

**6.1** $\delta_k$ is cyclic by 3.2 ($i=1$).

**6.2** If $\mu\vdash T_k$ is cyclic, say $B^i\mu=\mu$ with $i\ge1$, then $B^{ni}\mu=\mu$ for all $n\ge1$. By 5.1 there is $t_0$ with $B^{t_0}\mu=\delta_k$, and by 3.2 $B^{t}\mu=\delta_k$ for all $t\ge t_0$. Choosing $n$ with $ni\ge t_0$ gives $\mu=\delta_k$.

**6.3** Hence for $\lambda\vdash T_k$: $B^t\lambda$ is cyclic iff $B^t\lambda=\delta_k$, and $d_B(\lambda)=\min\{t\ge0:B^t\lambda=\delta_k\}$ (finite by 5.1).

## Step 7. Lower bound: $d_B(\lambda^{(k)})=k^2-k$ for every $k\ge1$

**7.0** $k=1$: $T_1=1$, the only partition is $(1)=\delta_1$, so $d_B(\lambda^{(1)})=0=1^2-1$ and $D_B(T_1)=0$. From now on $k\ge2$.

**7.1 (Configurations).** For $1\le q\le k$ and $1\le r\le k+1$ let
$$Z(q,r)=\bigcup_{d=1}^{k-1}\Delta_d\ \cup\ \big(\Delta_k\setminus\{\text{position }q\}\big)\ \cup\ \{\text{position } r \text{ of }\Delta_{k+1}\}.$$
Row $i$ ($1\le i\le k$) of $Z(q,r)$ consists of columns $1,\ldots,k-i$ (from $\Delta_1,\ldots,\Delta_{k-1}$), column $k+1-i$ iff $i\ne q$, and column $k+2-i$ iff $i=r$; row $k+1$ is $\{1\}$ if $r=k+1$ and empty otherwise; rows $\ge k+2$ are empty. Column $j$ ($1\le j\le k$) consists of rows $1,\ldots,k-j$, row $k+1-j$ iff $k+1-j\ne q$, and row $k+2-j$ iff $k+2-j=r$; column $k+1$ is $\{1\}$ if $r=1$ and empty otherwise; columns $\ge k+2$ are empty.

**7.2 (Lemma).** $Z(q,r)$ is down-closed iff $r-q\notin\{0,1\}$.

*Proof.* By 0.2, down-closed iff all rows and columns are initial segments. From 7.1: row $i\le k$ fails to be an initial segment iff column $k+2-i$ is present while $k+1-i$ is absent, i.e. iff $i=r$ and $i=q$; row $k+1$ and higher rows are always initial segments. Column $j\le k$ fails iff row $k+2-j$ is present while $k+1-j$ is absent, i.e. iff $r=k+2-j$ and $q=k+1-j$, i.e. iff $r=q+1$ (with $j=k+1-q\in\{1,\ldots,k\}$); columns $\ge k+1$ are always initial segments. $\square$

**7.3 (Lemma).** If $Z(q,r)=Y(\lambda)$, then $\rho(Y(\lambda))=Z(\pi_k(q),\pi_{k+1}(r))$ as sets; if moreover $\pi_{k+1}(r)-\pi_k(q)\notin\{0,1\}$ then $Y(B(\lambda))=Z(\pi_k(q),\pi_{k+1}(r))$.

*Proof.* By 1.1 and 1.3, $\rho$ maps the cells of $Y\cap\Delta_d$ to $\Delta_d$ via $\pi_d$. For $d\le k-1$, $Y\cap\Delta_d=\Delta_d$ and $\pi_d$ is a bijection, so the image is $\Delta_d$. The cells of $\Delta_k$ other than position $q$ go bijectively to the positions of $\Delta_k$ other than $\pi_k(q)$. Position $r$ of $\Delta_{k+1}$ goes to position $\pi_{k+1}(r)$. The second claim follows from 7.2 and 1.6. $\square$

**7.4 (Initial state).** Row lengths of $Z(1,k+1)$ (7.1): row 1 has $k-1$ cells, row $i$ ($2\le i\le k$) has $k+1-i$, row $k+1$ has 1. Since $r-q=k\ge2$, $Z(1,k+1)$ is down-closed (7.2), so $Z(1,k+1)=Y(\lambda^{(k)})$ by 0.2.

**7.5 (Index sequences).** Put $q_t=1+(t\bmod k)$ and $r_t=1+((t+k)\bmod(k+1))$ for $t\ge0$. Then $q_0=1$, $r_0=k+1$, $q_{t+1}=\pi_k(q_t)$, $r_{t+1}=\pi_{k+1}(r_t)$ (1.3). Call $t$ *bad* if $r_t-q_t\in\{0,1\}$.

*Claim.* For $k\ge2$: no $t$ with $0\le t\le k^2-k-1$ is bad, $t=k^2-k$ is bad, and $(q_{k^2-k},r_{k^2-k})=(1,2)$.

*Proof.* Write $t=m(k+1)+b$ with $m\ge0$, $0\le b\le k$. Then $(t+k)\bmod(k+1)=(b+k)\bmod(k+1)$, which is $k$ if $b=0$ and $b-1$ if $b\ge1$; so $r_t=k+1$ if $b=0$ and $r_t=b$ if $b\ge1$. Also $t=mk+(m+b)$, so $q_t=1+((m+b)\bmod k)$.
- $b=0$: $r_t-q_t=k-(m\bmod k)\ge1$, with equality iff $m\equiv k-1\pmod k$.
- $b\ge1$: $r_t-q_t=(b-1)-((m+b)\bmod k)$. This is $0$ iff $(m+b)\bmod k=b-1$ (note $0\le b-1\le k-1$) iff $m\equiv-1\pmod k$. It is $1$ iff $b\ge2$ and $(m+b)\bmod k=b-2$ iff $b\ge2$ and $m\equiv-2\pmod k$.

So $t$ is bad iff $m\equiv-1\pmod k$, or ($m\equiv-2\pmod k$ and $b\ge2$). The least $m\ge0$ with $m\equiv-1$ is $k-1$; the least with $m\equiv-2$ is $k-2\ge0$ (and $k-2\not\equiv-1\pmod k$ since $k\ge2$). Hence the bad $t$ with $m\le k-2$ are exactly $m=k-2$, $2\le b\le k$, the least being $t=(k-2)(k+1)+2=k^2-k$. Every $t\le k^2-k-1$ has $m\le k-2$ and, if $m=k-2$, $b\le1$; so it is not bad. At $t=k^2-k$: $b=2$, $r_t=2$, $q_t=1+(k\bmod k)=1$. $\square$

**7.6 (Orbit).** For $0\le t\le k^2-k-1$, $Y(B^t\lambda^{(k)})=Z(q_t,r_t)$. Induction: $t=0$ is 7.4. If it holds for $t\le k^2-k-2$, then $t+1$ is not bad (7.5), so by 7.3, $Y(B^{t+1}\lambda^{(k)})=Z(q_{t+1},r_{t+1})$.

**7.7** For $0\le t\le k^2-k-1$, $B^t\lambda^{(k)}\ne\delta_k$: $Z(q_t,r_t)$ contains a cell of $\Delta_{k+1}$, while $Y(\delta_k)\subseteq\bigcup_{d\le k}\Delta_d$ (3.1).

**7.8** $B^{k^2-k}\lambda^{(k)}=\delta_k$. Let $t=k^2-k-1$ and $Y=Y(B^t\lambda^{(k)})=Z(q_t,r_t)$. Since $q_{t+1}=1,r_{t+1}=2$ (7.5), 7.3 gives $\rho(Y)=Z(1,2)$ as a set. By 7.1 its rows have lengths: row 1: $k-1$; row 2: $(k-2)+1+1=k$; row $i$ for $3\le i\le k$: $k+1-i$; row $k+1$: $0$. By 1.4–1.5 the parts of $B(B^t\lambda^{(k)})$ are these positive row lengths sorted: $\{k,k-1,k-2,\ldots,1\}$, i.e. $\delta_k$. (For $k=2$: rows $1,2$, sorted $(2,1)=\delta_2$.)

**7.9 (Conclusion).** By 6.3, 7.7 and 7.8, $d_B(\lambda^{(k)})=k^2-k$ for every $k\ge2$, and by 7.0 also for $k=1$. Hence $D_B(T_k)\ge k^2-k$ for every $k\ge1$.

## Step 8. Upper bound for $1\le k\le 11$ (exhaustive exact computation)

**8.1 (Reduction).** For fixed $k$, by 6.3, $D_B(T_k)=\max_{\lambda\vdash T_k}\min\{t\ge0:B^t\lambda=\delta_k\}$, a maximum over the finite set of partitions of $T_k$ of a quantity that is finite (5.1) and computable by iterating $B$ with integer arithmetic. So "$D_B(T_k)\le k^2-k$" for a fixed $k$ is exactly the statement that this finite computation returns a value $\le k^2-k$.

**8.2 (Computation).** `code/check_triangular.py` enumerates all partitions of $T_k$ (counts $1,3,11,42,176,792,3718,17977,89134,451276,2323520$ for $k=1,\ldots,11$), iterates $B$ exactly until $\delta_k$, and returns the maximum hitting time. Output: maximum $=k^2-k$ for every $k=1,\ldots,11$. (Command, output and runtime in `code/README.md`.) Hence $D_B(T_k)=k^2-k$ for $1\le k\le 11$, using 7.9 for the lower bound.

## Step 9. Upper bound for general $k$ — **[GAP]**

**9.1 [GAP].** I did not prove $d_B(\lambda)\le k^2-k$ for every $\lambda\vdash T_k$ when $k\ge12$. Steps 2–5 give termination but no quantitative bound (the energy can exceed $E_k$ by order $k^3$, and the number of pure-rotation steps between two sorting steps is not controlled by the argument). See `stuck.md` for the attempted routes and the exact point of failure.

## Summary of what is established

- Proved for all $k\ge1$: every partition of $T_k$ reaches $\delta_k$; $\delta_k$ is the unique cyclic partition of $T_k$; $d_B(\lambda^{(k)})=k^2-k$; hence $D_B(T_k)\ge k^2-k$.
- Proved for $1\le k\le 11$ (Steps 6 + 8, exhaustive exact computation): $D_B(T_k)=k^2-k$.
- Not established: $D_B(T_k)\le k^2-k$ for $k\ge12$ **[GAP]**. The conjectured formula $F(k)=k^2-k$ is therefore proved as an exact value only for $k\le 11$ and as a lower bound for all $k$.
