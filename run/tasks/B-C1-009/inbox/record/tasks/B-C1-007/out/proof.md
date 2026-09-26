**Statement proved.** For every $k\ge1$ and $1\le r\le k$, $n=T_{k-1}+r$: (a) a partition of $n$ is cyclic iff it equals $\lambda(\varepsilon)=(k-1+\varepsilon_1,\,k-2+\varepsilon_2,\,\dots,\,1+\varepsilon_{k-1},\,\varepsilon_k)$ (a final entry $0$ deleted) for some $\varepsilon\in\{0,1\}^k$ with $\varepsilon_1+\dots+\varepsilon_k=r$; there are exactly $\binom kr$ of them; (b) the number of distinct cycles of $B$ on the partitions of $n$ is $N(k,r)=\frac1k\sum_{d\mid\gcd(k,r)}\varphi(d)\binom{k/d}{r/d}$; (i) for $n=T_k$ ($r=k$), $\delta_k$ is the only cyclic partition and every partition $\lambda$ of $T_k$ has $B^i(\lambda)=\delta_k$ for some $i\ge0$.

---

Literature run (B-C1-007, Phase 1L). The *techniques* follow the literature (Björner's "cradle" potential energy with the single-insertion computation, as presented in Drensky, arXiv:1503.00885, proof of Thm 1; the adjacent-levels coprimality trick of the same proof and of Toom / Hart–Khan–Khan, arXiv:1101.1546, Lemma 6 and Thm 1; the necklace identification of Drensky Thm 2 / Hart–Khan–Khan Thm 8). No cited result is used as a step: every step is proved below. Burnside's lemma is proved inline (the sources call the necklace count a "standard exercise" in Pólya enumeration and do not write it out).

**Reading of the target.** "Distinct cycles of $B$ on the partitions of $n$": the distinct sets $\{B^t(\mu):t\ge0\}$ with $\mu$ cyclic (Step 9.1 shows they partition the cyclic partitions). "Explicit description as functions of $k$ and $r$": the family $\lambda(\varepsilon)$ above, indexed by the $r$-subsets of $\{1,\dots,k\}$.

## 0. Notation

0.1. Piles are indexed from 1. For a finite sequence $c=(c_1,\dots,c_m)$ of positive integers, its *cell set* is $\mathcal C(c)=\{(q,h)\in\mathbb N_{\ge1}^2: q\le m,\ 1\le h\le c_q\}$ (pile $q$, height $h$), so $|\mathcal C(c)|=\sum_q c_q$. For a partition $\lambda$ we set $\lambda_q=0$ for $q>\ell(\lambda)$; then $\lambda_q=\#\{h:(q,h)\in\mathcal C(\lambda)\}$ for all $q\ge1$, so **a partition is determined by its cell set**.

0.2. *Young property.* If $\lambda$ is a partition and $(1,h)\in\mathcal C(\lambda)$, then $(1,h')\in\mathcal C(\lambda)$ for $1\le h'\le h$ (as $h'\le h\le\lambda_1$).

0.3. *Levels.* The level of a cell is $\operatorname{lev}(q,h)=q+h-1\ge1$. $D_\ell=\{(q,h):q+h-1=\ell\}=\{(i,\ell+1-i):1\le i\le\ell\}$ has exactly $\ell$ cells; the $D_\ell$ ($\ell\ge1$) are disjoint and cover $\mathbb N_{\ge1}^2$. We call $(i,\ell+1-i)$ *position $i$* of $D_\ell$. $|D_1|+\dots+|D_m|=T_m$.

0.4. *Energy.* $E(c)=\sum_{x\in\mathcal C(c)}\operatorname{lev}(x)=\sum_{q=1}^m\sum_{h=1}^{c_q}(q-1+h)=\sum_{q=1}^m\bigl((q-1)c_q+\tfrac{c_q(c_q+1)}2\bigr)$. Consequence: if two sequences differ only in that one pile of size $c$ sits at position $q'$ instead of $q$, the contribution of that pile changes by $(q'-q)c$.

0.5. *Rank.* $T_0=0$ and $T_m-T_{m-1}=m\ge1$, so the intervals $(T_{m-1},T_m]$, $m\ge1$, are disjoint and cover $\mathbb N_{\ge1}$; the rank of $n$ is well defined. $n=T_{k-1}+r$ with $1\le r\le k$ is the same as rank$(n)=k$.

## 1. The shift as "unsorted shift, then insertion"

1.1. Let $\lambda=(\lambda_1,\dots,\lambda_s)$ and $t=\#\{q:\lambda_q\ge2\}$; since $\lambda$ is weakly decreasing, $\lambda_q\ge2\iff q\le t$. Define the *unsorted shift*
$$U(\lambda)=(c_1,\dots,c_{t+1}):=(s,\ \lambda_1-1,\ \dots,\ \lambda_t-1).$$
Its entries are positive, and as a multiset they are exactly the parts of $B(\lambda)$ (the positive numbers among $\lambda_q-1$, together with $s$). The tail $(c_2,\dots,c_{t+1})$ is weakly decreasing.

1.2. *Insertion.* Let $p-1=\#\{q\in\{2,\dots,t+1\}:c_q>s\}$. As the tail is weakly decreasing, these $q$ are exactly $q=2,\dots,p$. The sequence
$$\beta=(c_2,\dots,c_p,\ s,\ c_{p+1},\dots,c_{t+1})$$
is weakly decreasing: $c_2\ge\dots\ge c_p$, $c_p>s$ if $p\ge2$, $s\ge c_{p+1}$ if $p+1\le t+1$ (because $c_{p+1}\not>s$), and $c_{p+1}\ge\dots\ge c_{t+1}$. It has the same multiset as $U(\lambda)$. A finite multiset has exactly one weakly decreasing arrangement, so $\beta=B(\lambda)$. In particular $B(\lambda)$ is a partition of $\sum_{q\le t}(\lambda_q-1)+s=\sum_{q\le s}(\lambda_q-1)+s=n$.

1.3. $p=1$ iff ($t=0$ or $c_2\le s$) iff $\lambda_1-1\le s$ (if $t=0$ then $\lambda_1-1=0\le s$; if $t\ge1$ then $c_2=\lambda_1-1$). In that case $B(\lambda)=U(\lambda)$ as sequences.

## 2. Cells move along levels (the "cradle" rotation)

2.1. Define $R:\mathbb N_{\ge1}^2\to\mathbb N_{\ge1}^2$ by $R(q,h)=(q+1,h-1)$ if $h\ge2$ and $R(q,1)=(1,q)$. It preserves levels: $(q+1)+(h-1)-1=q+h-1$ and $1+q-1=q+1-1$. It is a bijection, with inverse $R^{-1}(q,h)=(q-1,h+1)$ if $q\ge2$ and $R^{-1}(1,h)=(h,1)$: for $h\ge2$, $R(q,h)$ has first coordinate $\ge2$ and $R^{-1}$ returns $(q,h)$; $R(q,1)=(1,q)\mapsto(q,1)$; symmetrically $R(R^{-1}(q,h))=(q,h)$ in both cases $q\ge2$ ($R^{-1}$ gives height $h+1\ge2$) and $q=1$.

2.2. **Lemma 1.** $R(\mathcal C(\lambda))=\mathcal C(U(\lambda))$, hence $E(U(\lambda))=E(\lambda)$.

*Proof.* $\mathcal C(\lambda)=\{(q,1):q\le s\}\sqcup\{(q,h):q\le t,\ 2\le h\le\lambda_q\}$ (for $h\ge2$, $(q,h)\in\mathcal C(\lambda)$ forces $\lambda_q\ge2$, i.e. $q\le t$). $R$ sends the first set onto $\{(1,q):q\le s\}=\{(1,h):h\le c_1\}$, and the second onto $\{(q+1,h-1):q\le t,\ 1\le h-1\le\lambda_q-1\}=\{(q',h'):2\le q'\le t+1,\ h'\le c_{q'}\}$. The union is $\mathcal C(U(\lambda))$. Since $R$ is injective and level-preserving, $E(U(\lambda))=E(\lambda)$. $\square$

2.3. **Lemma 2 ($R$ rotates each level).** For $\ell\ge1$, $R$ maps position $i$ of $D_\ell$ to position $i+1$ if $i<\ell$, and position $\ell$ to position $1$. Hence $R^t$ maps position $i$ to the position $\equiv i+t\pmod\ell$ (in $\{1,\dots,\ell\}$).

*Proof.* For $i<\ell$: $(i,\ell+1-i)$ has height $\ge2$, so $R$ gives $(i+1,\ell-i)$, position $i+1$. For $i=\ell$: $R(\ell,1)=(1,\ell)$, position $1$. Induction on $t$. $\square$

## 3. Energy never increases; it is constant exactly on sort-free steps

**Lemma 3.** For every partition $\lambda$ with $s$ parts: $E(B(\lambda))\le E(\lambda)$, with equality iff $\lambda_1-1\le s$. When equality holds, $\mathcal C(B(\lambda))=R(\mathcal C(\lambda))$.

*Proof.* With the notation of 1.2, $\beta=B(\lambda)$ is obtained from $U(\lambda)$ by moving the piles $c_2,\dots,c_p$ one place to the left (from position $q$ to $q-1$) and the pile $s$ from position $1$ to position $p$; every other pile keeps its position. By 0.4,
$$E(B(\lambda))-E(U(\lambda))=(p-1)s-\sum_{q=2}^{p}c_q=-\sum_{q=2}^{p}(c_q-s)\le-(p-1),$$
since $c_q\ge s+1$ for $2\le q\le p$. With Lemma 1, $E(B(\lambda))\le E(\lambda)-(p-1)$. If $p\ge2$ the inequality is strict; if $p=1$, $B(\lambda)=U(\lambda)$ and equality holds, and $\mathcal C(B(\lambda))=\mathcal C(U(\lambda))=R(\mathcal C(\lambda))$ by Lemma 1. By 1.3, $p=1\iff\lambda_1-1\le s$. $\square$

(This is the "cradle model" statement of Drensky's proof of Thm 1: when the new pile is shorter than the old first pile less one, boxes "fall", lowering the potential energy.)

**Lemma 4 (on a cycle, cells just rotate).** Let $\lambda$ be cyclic, $B^P(\lambda)=\lambda$ with $P\ge1$, and $\lambda^{(t)}=B^t(\lambda)$. Then $\mathcal C(\lambda^{(t)})=R^t(\mathcal C(\lambda))$ for all $t\ge0$, and each $\lambda^{(t)}$ is cyclic.

*Proof.* $E(\lambda^{(0)})\ge E(\lambda^{(1)})\ge\dots\ge E(\lambda^{(P)})=E(\lambda^{(0)})$ (Lemma 3), so all are equal and each step $\lambda^{(t)}\to\lambda^{(t+1)}$, $0\le t<P$, has equality. Since $\lambda^{(t+P)}=\lambda^{(t)}$ for every $t$ (induction), equality holds at every step $t\ge0$. Lemma 3 gives $\mathcal C(\lambda^{(t+1)})=R(\mathcal C(\lambda^{(t)}))$; induct on $t$. Also $B^P(\lambda^{(t)})=\lambda^{(t+P)}=\lambda^{(t)}$. $\square$

## 4. No hole directly below a cell (adjacent levels)

**Lemma 5.** Let $\lambda$ be cyclic and $\ell\ge1$. If $D_\ell\not\subseteq\mathcal C(\lambda)$, then $D_{\ell+1}\cap\mathcal C(\lambda)=\emptyset$.

*Proof.* Suppose position $a$ of $D_\ell$ is not a cell of $\lambda$ and position $b$ of $D_{\ell+1}$ is. Choose $t_0\in\{0,\dots,\ell\}$ with $b+t_0\equiv1\pmod{\ell+1}$. For $j=0,1,\dots,\ell-1$ put $t_j=t_0+j(\ell+1)$. Then $b+t_j\equiv1\pmod{\ell+1}$ for every $j$, and, because $\ell+1\equiv1\pmod\ell$, $a+t_j\equiv a+t_0+j\pmod\ell$. As $j$ runs over $0,\dots,\ell-1$ the residues $a+t_0+j$ run over all residues mod $\ell$, so there is $j$ with $a+t_j\equiv1\pmod\ell$. Put $t=t_j$ and $\mu=B^t(\lambda)$.

By Lemma 4, $\mathcal C(\mu)=R^t(\mathcal C(\lambda))$; as $R^t$ is a bijection of $\mathbb N_{\ge1}^2$ (2.1), it also maps the complement of $\mathcal C(\lambda)$ onto the complement of $\mathcal C(\mu)$. By Lemma 2, $R^t$ sends position $b$ of $D_{\ell+1}$ to position $1$, i.e. to $(1,\ell+1)$, and position $a$ of $D_\ell$ to position 1, i.e. to $(1,\ell)$. So $(1,\ell+1)\in\mathcal C(\mu)$ and $(1,\ell)\notin\mathcal C(\mu)$, contradicting 0.2 for the partition $\mu$. $\square$

(Drensky's proof of Thm 1 uses exactly the progression $0,(\ell+1),2(\ell+1),\dots$; Hart–Khan–Khan use the Chinese remainder theorem, their Lemma 6.)

## 5. Shape of a cyclic partition

**Proposition 6.** Let $\lambda$ be a cyclic partition of $n$, and let $k$ be the rank of $n$, $r=n-T_{k-1}$. Then
$$D_1\cup\dots\cup D_{k-1}\subseteq\mathcal C(\lambda)\subseteq D_1\cup\dots\cup D_k,\qquad|\mathcal C(\lambda)\cap D_k|=r.$$

*Proof.* $\mathcal C(\lambda)$ is finite, so some $D_\ell$ is not contained in it; let $L$ be the least such $\ell$. $D_1=\{(1,1)\}\subseteq\mathcal C(\lambda)$, so $L\ge2$, and $D_1,\dots,D_{L-1}\subseteq\mathcal C(\lambda)$. By Lemma 5, $D_{L+1}\cap\mathcal C(\lambda)=\emptyset$. Inductively, if $D_m\cap\mathcal C(\lambda)=\emptyset$ for some $m\ge L+1$, then $D_m\not\subseteq\mathcal C(\lambda)$ ($D_m\ne\emptyset$), so Lemma 5 gives $D_{m+1}\cap\mathcal C(\lambda)=\emptyset$. Hence $\mathcal C(\lambda)=D_1\cup\dots\cup D_{L-1}\cup S$ with $S=\mathcal C(\lambda)\cap D_L\subsetneq D_L$, and $n=T_{L-1}+|S|$, $0\le|S|\le L-1$ (0.3).

If $|S|\ge1$: $T_{L-1}<n\le T_{L-1}+L-1<T_L$, so $k=L$ and $r=|S|$ (0.5); the claim holds.
If $|S|=0$: $n=T_{L-1}$ with $L-1\ge1$, so $T_{L-2}<n\le T_{L-1}$ gives $k=L-1$, $r=T_k-T_{k-1}=k$, and $\mathcal C(\lambda)=D_1\cup\dots\cup D_k$; the claim holds with $|\mathcal C(\lambda)\cap D_k|=k=r$. $\square$

## 6. The family $\lambda(\varepsilon)$ and the action of $B$

6.1. Let $W(k,r)=\{\varepsilon\in\{0,1\}^k:\sum_i\varepsilon_i=r\}$, $|W(k,r)|=\binom kr$. For $\varepsilon\in W(k,r)$ let $\lambda(\varepsilon)$ be the list $(k-i+\varepsilon_i)_{i=1}^k$ with a final $0$ deleted. For $i\le k-1$, $k-i+\varepsilon_i\ge1$; the last entry is $\varepsilon_k$. Consecutive differences are $1+\varepsilon_i-\varepsilon_{i+1}\ge0$. The list is nonempty (for $k\ge2$ its first entry is $\ge1$; for $k=1$, $r=1$ forces $\varepsilon=(1)$). Its sum is $T_{k-1}+r$. So $\lambda(\varepsilon)$ is a partition of $n$, with $k-1+\varepsilon_k$ parts.

6.2. **Lemma 7 (cell set).** $\mathcal C(\lambda(\varepsilon))=D_1\cup\dots\cup D_{k-1}\cup\{\text{position } i\text{ of }D_k:\varepsilon_i=1\}$.

*Proof.* Pile $i\le k$ has cells $(i,h)$, $1\le h\le k-i+\varepsilon_i$. Those with $h\le k-i$ have levels $i,\dots,k-1$ and are exactly the cells of pile $i$ lying in $D_1\cup\dots\cup D_{k-1}$ (a cell $(i,h)$ lies in $D_\ell$ with $\ell=i+h-1$, and $\ell\le k-1\iff h\le k-i$). The cell $(i,k+1-i)$ = position $i$ of $D_k$ is present iff $\varepsilon_i=1$. There are no piles $i>k$, and $D_1\cup\dots\cup D_{k-1}$ has no cell in a pile $i\ge k$. $\square$

6.3. **Lemma 8.** $\varepsilon\mapsto\lambda(\varepsilon)$ is injective on $W(k,r)$, and $B(\lambda(\varepsilon))=\lambda(\rho\varepsilon)$, where $\rho(\varepsilon_1,\dots,\varepsilon_k)=(\varepsilon_k,\varepsilon_1,\dots,\varepsilon_{k-1})$.

*Proof.* Injective: by Lemma 7, $\varepsilon_i=1$ iff position $i$ of $D_k$ is a cell. For the shift, let $\lambda=\lambda(\varepsilon)$ with $s=k-1+\varepsilon_k$ parts. Then $\lambda_1-1=k-2+\varepsilon_1\le k-1\le s$ (for $k=1$: $\lambda_1-1=0\le s$). By Lemma 3, $\mathcal C(B(\lambda))=R(\mathcal C(\lambda))$. By Lemma 2, $R$ maps each $D_\ell$ onto itself, and on $D_k$ sends position $i$ to $i+1$ ($i<k$) and position $k$ to $1$. So $R(\mathcal C(\lambda))=D_1\cup\dots\cup D_{k-1}\cup\{\text{position }i\text{ of }D_k:(\rho\varepsilon)_i=1\}$, since $(\rho\varepsilon)_{i+1}=\varepsilon_i$, $(\rho\varepsilon)_1=\varepsilon_k$. By Lemma 7 this is $\mathcal C(\lambda(\rho\varepsilon))$, and $\rho\varepsilon\in W(k,r)$. A partition is determined by its cell set (0.1), so $B(\lambda)=\lambda(\rho\varepsilon)$. $\square$

6.4. **Corollary 9.** $B^t(\lambda(\varepsilon))=\lambda(\rho^t\varepsilon)$ for $t\ge0$; $\rho^k=\mathrm{id}$ (each application moves every letter one step cyclically: $(\rho^t\varepsilon)_i=\varepsilon_{i-t \bmod k}$ by induction), so $B^k(\lambda(\varepsilon))=\lambda(\varepsilon)$ with $k\ge1$: every $\lambda(\varepsilon)$ is cyclic.

## 7. Target (ii)(a)

**Theorem 10.** For $k\ge1$, $1\le r\le k$, $n=T_{k-1}+r$, the cyclic partitions of $n$ are exactly the $\lambda(\varepsilon)$, $\varepsilon\in W(k,r)$; there are $\binom kr$ of them.

*Proof.* If: Corollary 9 and 6.1. Only if: for cyclic $\lambda\vdash n$, Proposition 6 gives $\mathcal C(\lambda)=D_1\cup\dots\cup D_{k-1}\cup S$ with $S\subseteq D_k$, $|S|=r$; set $\varepsilon_i=1$ iff position $i$ of $D_k$ lies in $S$. Then $\varepsilon\in W(k,r)$ and $\mathcal C(\lambda)=\mathcal C(\lambda(\varepsilon))$ (Lemma 7), so $\lambda=\lambda(\varepsilon)$ (0.1). Count: Lemma 8 (injectivity). $\square$

In words: add $1$ to exactly $r$ of the $k$ entries of $(k-1,k-2,\dots,1,0)$ and delete a final zero; equivalently, the staircase $\delta_{k-1}$ plus any $r$ of the $k$ cells of level $k$.

## 8. Target (i)

**Theorem 11.** For $n=T_k$ ($k\ge1$): $\delta_k$ is the only cyclic partition, and for every $\lambda\vdash n$ there is $i\ge0$ with $B^i(\lambda)=\delta_k$.

*Proof.* The rank of $T_k$ is $k$ and $r=k$ (0.5). $W(k,k)=\{(1,\dots,1)\}$ and $\lambda(1,\dots,1)=(k,\dots,1)=\delta_k$; Theorem 10 gives uniqueness. For $\lambda\vdash n$, let $M$ be the (finite) number of partitions of $n$; the $M+1$ partitions $B^0(\lambda),\dots,B^M(\lambda)$ (1.2 shows $B$ maps partitions of $n$ to partitions of $n$) contain a repetition $B^i(\lambda)=B^j(\lambda)$, $i<j$; then $B^{j-i}(B^i\lambda)=B^i\lambda$, so $B^i(\lambda)$ is cyclic, hence equals $\delta_k$. $\square$

## 9. Target (ii)(b)

9.1. *Cycles.* For cyclic $\mu$ with $B^P\mu=\mu$ let $O(\mu)=\{B^t\mu:t\ge0\}$. If $\nu=B^t\mu$ then, writing $t=aP+t'$ with $0\le t'<P$, $B^{P-t'}\nu=B^{(a+1)P}\mu=\mu$, so $\mu\in O(\nu)$ and $O(\mu)=O(\nu)$. Hence two cycles are equal or disjoint, and the cycles partition the set of cyclic partitions.

9.2. *Transfer.* By Theorem 10 and Corollary 9, $\Lambda:\varepsilon\mapsto\lambda(\varepsilon)$ is a bijection $W(k,r)\to\{\text{cyclic partitions of }n\}$ with $B^t\Lambda(\varepsilon)=\Lambda(\rho^t\varepsilon)$. So $O(\Lambda(\varepsilon))=\Lambda(\{\rho^j\varepsilon:0\le j<k\})$, and the number of cycles equals the number of orbits of the group $G=\{\rho^0,\dots,\rho^{k-1}\}\cong\mathbb Z/k$ on $W(k,r)$ (binary necklaces of length $k$ with $r$ ones).

9.3. *Burnside (proved).* For a finite group $G$ acting on a finite set $X$: $\#\text{orbits}=\frac1{|G|}\sum_{g}|\mathrm{Fix}(g)|$. Count $F=\{(g,x):gx=x\}$: $|F|=\sum_x|\mathrm{Stab}(x)|$. For $x$ in an orbit $\Omega$, $g\mapsto gx$ is a surjection $G\to\Omega$ whose fibres are the cosets $g\,\mathrm{Stab}(x)$, so $|\mathrm{Stab}(x)|=|G|/|\Omega|$; summing over $x\in\Omega$ gives $|G|$ per orbit.

9.4. *Fixed words.* Index positions by $\mathbb Z/k$, so $(\rho^j\varepsilon)_i=\varepsilon_{i-j}$. Let $g=\gcd(j,k)$ ($\gcd(0,k)=k$). The subgroup of $\mathbb Z/k$ generated by $j$ equals the one generated by $g$ (it contains $g=uj+vk$ by Bézout, and $g\mid j$), i.e. the multiples of $g$. So $\rho^j\varepsilon=\varepsilon$ iff $\varepsilon_i=\varepsilon_{i-j}$ for all $i$ iff $\varepsilon$ is constant on the cosets $i+g\mathbb Z/k\mathbb Z$ (there are $g$ cosets, each of size $k/g$). Such a word is determined by the set of cosets where it is $1$, and has weight $(k/g)\cdot\#\{\text{those cosets}\}$. So $|\mathrm{Fix}(\rho^j)\cap W(k,r)|=\binom{g}{r g/k}$ if $(k/g)\mid r$, else $0$.

9.5. *Counting $j$.* For $g\mid k$, the $j\in\{0,\dots,k-1\}$ with $\gcd(j,k)=g$ are $j=gj'$, $0\le j'<k/g$, $\gcd(j',k/g)=1$; replacing $j'=0$ by $j'=k/g$ does not change the gcd, so there are $\varphi(k/g)$ of them.

**Theorem 12.** The number of distinct cycles of $B$ on the partitions of $n=T_{k-1}+r$ is
$$N(k,r)=\frac1k\sum_{d\mid\gcd(k,r)}\varphi(d)\binom{k/d}{r/d}.$$
*Proof.* By 9.2–9.5, the count is $\frac1k\sum_{g\mid k}\varphi(k/g)[\,(k/g)\mid r\,]\binom{g}{rg/k}$; substitute $d=k/g$ (runs over divisors of $k$; condition $d\mid r$, i.e. $d\mid\gcd(k,r)$). $\square$

Consistency: $r=k$ gives $\frac1k\sum_{d\mid k}\varphi(d)=1$ (9.5 summed over $g\mid k$ counts each $j$ once). The cycle through $\lambda(\varepsilon)$ has length equal to the least period of $\varepsilon$ under $\rho$, a divisor of $k$.

## 10. Edge cases

$k=1$: $n=1$, $W(1,1)=\{(1)\}$, $\lambda=(1)$, $B((1))=(1)$, $N(1,1)=1$; Lemmas 3, 5, 8 and Prop. 6 hold without restriction ($L\ge2$ in Prop. 6; for $n=1$, $L=2$, $S=\emptyset$, $k=1$). $r=k$ (triangular) is covered in Prop. 6 by the case $|S|=0$. Lemma 5 uses $\ell\ge1$ only.

## 11. What is established

(i), (ii)(a), (ii)(b) for all $k\ge1$, $1\le r\le k$ (Theorems 11, 10, 12). No step depends on computation. `out/code/check_c1_lit.py` (stdlib, exact) confirms Lemma 3's equality criterion, (i), (ii)(a), (ii)(b) for $1\le n\le50$ as a sanity check only. KNOWN GAPS in the proof: none found. Not addressed: time to cycle (cells C2+).
