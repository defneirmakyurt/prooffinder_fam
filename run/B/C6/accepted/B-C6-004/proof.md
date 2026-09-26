**Statement proved (lower half only).** For every $n\ge 1$, writing $n=T_{k-1}+r$ with $1\le r\le k$, we have $D_B(n)\ge F(n)$, where $F(1)=F(2)=0$ and, for $n\ge 3$,
$$F(n)=\max\Bigl\{\,n-k+1,\ \ r(k+1)-2k\ \ [\text{only if } 2\le r\le k],\ \ (k-1)(k-2-r)\ \ [\text{only if } k\ge 4,\ 1\le r\le k-3]\,\Bigr\},$$
each term being $d_B$ of an explicit partition of $n$: $d_B(1^n)=n-k+1$ ($n\ge3$); $d_B(\delta_{k-1}\uplus\{r-1,1\})=r(k+1)-2k$ ($k\ge2$, $2\le r\le k$); $d_B(\delta_{k-2}\uplus\{k-2,r+1\})=(k-1)(k-2-r)$ ($k\ge4$, $1\le r\le k-3$).
The upper half $D_B(n)\le F(n)$ is **not** proved. $D_B(n)=F(n)$ is CONJECTURED; it is verified by exhaustive exact computation for $1\le n\le 62$ only (Section 6).

Reading of the brief: the cell is open; I deliver the lower half for every $n$ (explicit witness families, exact $d_B$) and a conjectured formula. No gated claim is used: the proof below is self-contained (Cells 1, 2 and the Cell 3 witness appear only as consistency remarks).

---

## 0. Conventions

0.1. A partition is identified with its multiset of parts; $B(\lambda)$ depends only on this multiset (definition: the positive numbers among $\lambda_i-1$, plus the part $s$). $\uplus$ denotes multiset union. For a finite sequence of nonnegative integers that is weakly decreasing, "zeros deleted" gives a partition.

0.2. Fix $k\ge 2$ and put $b_i=\max(k-i,0)$ for $i\ge1$ (so $b_i=k-i$ for $i\le k$, $b_k=b_{k+1}=0$). $[P]$ is $1$ if $P$ holds, else $0$.

0.3. For $A\subseteq\{1,\dots,k\}$ let $A\oplus1=\{a+1: a\in A,\ a\le k-1\}\cup(\{1\}\text{ if }k\in A)$, i.e. adding $1$ modulo $k$ with representatives $1,\dots,k$. Iterating, $A\oplus t$ is $A+t$ modulo $k$.

---

## 1. The rigid step

**Lemma 1.** Let $\lambda=(\lambda_1,\dots,\lambda_s)$ have $s$ parts. If $s\ge\lambda_1-1$, then $B(\lambda)$ is the sequence $(s,\lambda_1-1,\lambda_2-1,\dots,\lambda_s-1)$ with its zero entries deleted.

*Proof.* 1. By definition the parts of $B(\lambda)$ are $s$ and the positive numbers among $\lambda_i-1$.
2. $(\lambda_1-1,\dots,\lambda_s-1)$ is weakly decreasing because $\lambda$ is; hence its zero entries form a final segment.
3. Since $s\ge\lambda_1-1$, the sequence $(s,\lambda_1-1,\dots,\lambda_s-1)$ is weakly decreasing; deleting its final zeros gives a weakly decreasing sequence of positive integers whose multiset is that of Step 1. $\square$

---

## 2. The cyclic states $\kappa(A)$ and a criterion for $d_B$

**Definition.** For $A\subseteq\{1,\dots,k\}$ let $\kappa(A)$ be the sequence $(b_i+[i\in A])_{i=1}^{k}$ with zeros deleted. Let $S_k=\{\kappa(A):A\subseteq\{1,\dots,k\}\}$.

**Lemma 2.** $\kappa(A)$ is a partition of $T_{k-1}+|A|$, and $B(\kappa(A))=\kappa(A\oplus1)$. Consequently $B(S_k)\subseteq S_k$ and $B^k(\kappa(A))=\kappa(A)$, so every element of $S_k$ is cyclic.

*Proof.* 1. For $1\le i\le k-1$: $\kappa_i-\kappa_{i+1}=1+[i\in A]-[i+1\in A]\ge0$. Entries $i\le k-1$ are $\ge b_i\ge1$; $\kappa_k=[k\in A]$. So the sequence is weakly decreasing, and zeros deleted it is a partition with $s=k-1+[k\in A]$ parts and sum $\sum_{i\le k}b_i+|A|=T_{k-1}+|A|$.
2. $\kappa_1-1=k-2+[1\in A]\le k-1\le s$, so Lemma 1 applies: $B(\kappa(A))=(s,\kappa_1-1,\dots,\kappa_s-1)$, zeros deleted.
3. Put $A'=A\oplus1$. First entry: $s=k-1+[k\in A]=b_1+[1\in A']$, since $1\in A'\iff k\in A$.
4. For $1\le i\le k-1$ the entry in position $i+1$ is $\kappa_i-1=(k-i-1)+[i\in A]=b_{i+1}+[i+1\in A']$, since $i+1\in A'\iff i\in A$ for $1\le i\le k-1$.
5. If $s=k$ there is one more entry, $\kappa_k-1=0$, which is deleted. So $B(\kappa(A))$ is $(b_i+[i\in A'])_{i=1}^k$ with zeros deleted, i.e. $\kappa(A')$.
6. $A\mapsto A\oplus1$ is a cyclic shift of $\{1,\dots,k\}$, so $A\oplus k=A$ and $B^k(\kappa(A))=\kappa(A)$ with $k\ge1$. $\square$

**Remark 2a (membership test).** $\mu\in S_k$ iff $\mu$ has at most $k$ parts and $\mu_i-b_i\in\{0,1\}$ for $1\le i\le k$ (with $\mu_i=0$ beyond its length). Indeed $\kappa(A)$ has these properties, and conversely such $\mu$ equals $\kappa(\{i\le k:\mu_i-b_i=1\})$. In particular every element of $S_k$ has largest part $\le b_1+1=k$ and at most $k$ parts.

**Lemma 3 ($d_B$ criterion).** Let $x$ be a partition and $t\ge0$ with $B^t(x)\in S_k$ and $B^i(x)\notin S_k$ for $0\le i<t$. Then $d_B(x)=t$.

*Proof.* 1. $B^t(x)$ is cyclic by Lemma 2.
2. Let $0\le i<t$ and $y=B^i(x)$. Then $B^{t-i}(y)\in S_k$ and, since $B(S_k)\subseteq S_k$ (Lemma 2), $B^{m}(y)\in S_k$ for all $m\ge t-i$.
3. If $y$ were cyclic, $B^p(y)=y$ for some $p\ge1$, hence $y=B^{jp}(y)$ for all $j\ge1$; choosing $jp\ge t-i$ gives $y\in S_k$, contradicting $y\notin S_k$.
4. So $B^i(x)$ is not cyclic for $i<t$ and $B^t(x)$ is; by definition $d_B(x)=t$. $\square$

---

## 3. The all-ones partition: $d_B(1^n)=n-k+1$ for $n\ge3$

**Proposition A.** Let $n\ge3$, $n=T_{k-1}+r$, $1\le r\le k$. Then $d_B(1^n)=n-k+1$.

*Proof.* 1. For integers $0\le j\le m$ let $N_{m,j}=n-T_m-j$ and let $P(m,j)$ be the multiset $\{N_{m,j}\}\uplus\{m+1-i+[i\le j]:1\le i\le m\}$ (the second part is $\delta_m$ with $1$ added to its $j$ largest parts; it is empty for $m=0$). Its sum is $N_{m,j}+T_m+j=n$.

2. *Transition.* Suppose $N_{m,j}\ge2$ (and $N_{m,j}$ is a positive part, so $P(m,j)$ has $s=m+1$ parts, all tail parts being $\ge1$). Subtracting $1$ from every part gives $N_{m,j}-1\ge1$ and the tail values $m-i+[i\le j]$, $1\le i\le m$; the value for $i=m$ is $[m\le j]$. The new part is $m+1$.
   - (i) If $j<m$: the value for $i=m$ is $0$ and is discarded. The remaining tail values for $1\le i\le m-1$, reindexed by $i'=i+1\in\{2,\dots,m\}$, are $m+1-i'+[i'\le j+1]$; the new part $m+1$ equals $m+1-1+[1\le j+1]$ (the value for $i'=1$). Hence $B(P(m,j))=\{N_{m,j}-1\}\uplus\{m+1-i'+[i'\le j+1]:1\le i'\le m\}=P(m,j+1)$, since $N_{m,j}-1=N_{m,j+1}$.
   - (ii) If $j=m$: the tail values are $m-i+1$, $1\le i\le m$, all positive; with the new part $m+1$ they form $\{m+2-i':1\le i'\le m+1\}=\delta_{m+1}$. And $N_{m,m}-1=n-T_m-m-1=n-T_{m+1}=N_{m+1,0}$. Hence $B(P(m,m))=P(m+1,0)$.

3. *Timing.* $B(1^n)=(n)=P(0,0)$ ($1^n$ has $n$ parts, all become $0$, new part $n$). Put $\tau(m,j)=1+T_m+j$. Then $\tau(0,0)=1$, $\tau(m,j+1)=\tau(m,j)+1$, and $\tau(m+1,0)=1+T_m+m+1=\tau(m,m)+1$. Also $N_{m,j}=n+1-\tau(m,j)$. By induction along the lexicographic order of pairs, using Step 2: $B^{\tau(m,j)}(1^n)=P(m,j)$ for every pair $(m,j)$ up to a pair $(m_1,j_1)$, provided $N\ge2$ at every pair strictly before $(m_1,j_1)$.

4. *Case $1\le r\le k-1$.* Take $(m_1,j_1)=(k-2,r-1)$; this is a legal pair since $0\le r-1\le k-2$. Its time is $\tau=1+T_{k-2}+r-1=T_{k-2}+r=n-(k-1)$, using $T_{k-1}=T_{k-2}+k-1$. For pairs strictly before it, $\tau\le n-k$, so $N=n+1-\tau\ge k+1\ge2$; Step 3 applies. So $B^{n-k+1}(1^n)=P(k-2,r-1)$, and for $1\le \tau< n-k+1$ the state $B^\tau(1^n)=P(m,j)$ has a part $N\ge k+1$.
   - $P(k-2,r-1)=\{k\}\uplus\{k-1-i+[i\le r-1]:1\le i\le k-2\}$. Sorted, position $1$ holds $k=b_1+1$, and position $p=i+1\in\{2,\dots,k-1\}$ holds $k-p+[p\le r]=b_p+[p\le r]$; position $k$ is empty, $=b_k+[k\le r]=0$ as $r\le k-1$. So $P(k-2,r-1)=\kappa(\{1,\dots,r\})\in S_k$. (The sorted order is valid: the values are strictly/weakly decreasing in $p$ by Lemma 2, Step 1.)

5. *Case $r=k$* ($n=T_k$, and $k\ge2$ because $n\ge3$). Take $(m_1,j_1)=(k-1,0)$, time $1+T_{k-1}=n-k+1$. Pairs strictly before have $\tau\le T_{k-1}$, so $N\ge T_k-T_{k-1}+1=k+1\ge2$. $P(k-1,0)=\{k\}\uplus\delta_{k-1}=\delta_k=\kappa(\{1,\dots,k\})\in S_k$.

6. *Earlier states are outside $S_k$.* At time $0$, $1^n$ has $n$ parts, and $n>k$: if $n\le k$ then $T_{k-1}<k$, i.e. $k\le2$, and then $n\le2$, contrary to $n\ge3$. At times $1\le\tau<n-k+1$ the state has a part $\ge k+1$ (Steps 4, 5). By Remark 2a none of these lies in $S_k$.

7. By Lemma 3, $d_B(1^n)=n-k+1$. $\square$

(Edge cases: for $n=1,2$ the statement fails — $(1)$, $(2)$, $(1,1)$ are cyclic since $B((1))=(1)$, $B((2))=(1,1)$, $B((1,1))=(2)$ — which is why $n\ge3$ is required and $F(1)=F(2)=0$.)

---

## 4. The family $U_{k,r}=\delta_{k-1}\uplus\{r-1,1\}$

**Configurations.** For $A\subseteq\{1,\dots,k\}$ and $c\in\{1,\dots,k+1\}$ with
(i) $c\le k\Rightarrow c\in A$, and (ii) $c\ge2\Rightarrow c-1\in A$,
let $\gamma_i=b_i+[i\in A]+[i=c]$ for $1\le i\le k+1$, and $\Gamma(A,c)=(\gamma_1,\dots,\gamma_{k+1})$ with zeros deleted. Let $c\oplus1=c+1$ for $c\le k$ and $c\oplus1=1$ for $c=k+1$.

**Claim B1.** $\Gamma(A,c)$ is a partition of $T_{k-1}+|A|+1$ and $\Gamma(A,c)\notin S_k$.

*Proof.* 1. For $1\le i\le k-1$: $\gamma_i-\gamma_{i+1}=1+[i\in A]-[i+1\in A]+[i=c]-[i+1=c]$. If $i+1=c$ then $c\le k$, so $c\in A$ by (i) and $i=c-1\in A$ by (ii): the value is $1+1-1+0-1=0$. Otherwise it is $\ge 1+0-1+0-0\ge0$.
2. For $i=k$: $\gamma_k-\gamma_{k+1}=[k\in A]+[c=k]-[c=k+1]$; if $c=k+1$ then $k\in A$ by (ii), value $\ge0$; otherwise the value is $\ge0$.
3. Entries $i\le k-1$ are $\ge1$, so the sequence is weakly decreasing with terminal zeros; the sum is $T_{k-1}+|A|+1$.
4. If $c\le k$: $\gamma_c-b_c=[c\in A]+1=2\notin\{0,1\}$. If $c=k+1$: $\gamma_{k+1}=1$ and $\gamma_k\ge1$ ($k\in A$), so there are $k+1$ positive parts. By Remark 2a, $\Gamma(A,c)\notin S_k$. $\square$

**Claim B2.** Let $x=\Gamma(A,c)$.
(a) If $c\ne1$ or $k\in A$, then $(A\oplus1,c\oplus1)$ satisfies (i),(ii) and $B(x)=\Gamma(A\oplus1,c\oplus1)$.
(b) If $c=1$ and $k\notin A$, then $B(x)=\kappa\bigl((A\oplus1)\cup\{1\}\bigr)\in S_k$.

*Proof.* 1. $\gamma_i\ge1$ for $i\le k-1$; $\gamma_k=[k\in A]+[c=k]$ is positive iff $k\in A$ (by (i), $c=k\Rightarrow k\in A$); $\gamma_{k+1}=[c=k+1]$. So $s=k-1+[k\in A]+[c=k+1]$. Also $\gamma_1-1=k-2+[1\in A]+[c=1]\le k$.

2. *(a).* If $c\ne1$ then $\gamma_1-1\le k-1\le s$. If $c=1$ and $k\in A$ then $\gamma_1-1=k\le s=k$. So Lemma 1 applies: entries $y_1=s$, $y_{i+1}=\gamma_i-1$ ($1\le i\le s$), zeros deleted. Put $A'=A\oplus1$, $c'=c\oplus1$.
   - $y_1=k-1+[k\in A]+[c=k+1]=b_1+[1\in A']+[1=c']$ (as $1\in A'\iff k\in A$, $c'=1\iff c=k+1$).
   - For $1\le i\le k-1$: $y_{i+1}=(k-i-1)+[i\in A]+[i=c]=b_{i+1}+[i+1\in A']+[i+1=c']$.
   - If $\gamma_k\ge1$ (i.e. $k\in A$): $y_{k+1}=\gamma_k-1=[c=k]=b_{k+1}+[k+1\in A']+[k+1=c']$ ($k+1\notin A'$). If $\gamma_k=0$ there is no such entry, and the corresponding entry of $\Gamma(A',c')$ is $[c'=k+1]=[c=k]=0$ (as $k\notin A$ forces $c\ne k$).
   - If $c=k+1$: $y_{k+2}=\gamma_{k+1}-1=0$, deleted.
   So $B(x)$ is $(b_i+[i\in A']+[i=c'])_{i=1}^{k+1}$ with zeros deleted.
   - Conditions for $(A',c')$: (i) if $c\le k-1$, $c'=c+1\in A'\iff c\in A$, true by (i); if $c=k+1$, $c'=1\in A'\iff k\in A$, true by (ii); if $c=k$, $c'=k+1$ and (i) is void. (ii) if $c'\ge2$ then $c\le k$ and $c'-1=c$; for $c\ge2$, $c\in A'\iff c-1\in A$, true by (ii); for $c=1$, $1\in A'\iff k\in A$, true by the hypothesis of (a). Hence $B(x)=\Gamma(A',c')$.

3. *(b).* Here $1\in A$ (by (i)), $k\notin A$, so $\gamma_1=k+1$, $\gamma_i=k-i+[i\in A]$ for $2\le i\le k-1$, $\gamma_k=\gamma_{k+1}=0$, $s=k-1$. The parts of $B(x)$ are $\gamma_1-1=k$, the positive values among $\gamma_i-1=k-i-1+[i\in A]\le k-2$ ($2\le i\le k-1$), and $s=k-1$. Sorted: $B(x)=(k,k-1,\gamma_2-1,\dots,\gamma_{k-1}-1)$, zeros deleted.
   Let $A^*=(A\oplus1)\cup\{1\}$. As $k\notin A$, $A\oplus1=\{a+1:a\in A\}\not\ni1$, and $2\in A\oplus1$ as $1\in A$. Then $\kappa(A^*)_1=b_1+1=k$, $\kappa(A^*)_2=b_2+1=k-1$, and for $3\le p\le k$: $\kappa(A^*)_p=k-p+[p-1\in A]=\gamma_{p-1}-1$. So $B(x)=\kappa(A^*)\in S_k$. $\square$

**Proposition B.** For $k\ge2$ and $2\le r\le k$, $U_{k,r}=\delta_{k-1}\uplus\{r-1,1\}$ is a partition of $n=T_{k-1}+r$ (rank $k$, position $r$) with $d_B(U_{k,r})=r(k+1)-2k=(r-2)(k+1)+2$.

*Proof.* 1. Let $A_0=\{k-r+2,\dots,k\}$ ($r-1\ge1$ elements) and $c_0=k+1$. (i) is void, (ii) holds as $k\in A_0$. The entries of $\Gamma(A_0,c_0)$: $\gamma_i=k-i$ for $1\le i\le k-r+1$ (values $k-1,\dots,r-1$); $\gamma_i=k-i+1$ for $k-r+2\le i\le k$ (values $r-1,\dots,1$); $\gamma_{k+1}=1$. The multiset is $\{1,\dots,k-1\}\uplus\{r-1\}\uplus\{1\}=U_{k,r}$. So $U_{k,r}=\Gamma(A_0,c_0)$.
2. Let $A_t=A_0\oplus t$ and $c_t=c_0\oplus t$ (so $c_t\equiv t \pmod{k+1}$ with representatives $1,\dots,k+1$, and $A_t\equiv A_0+t\pmod k$). By Claim B2(a) and induction, $B^t(U_{k,r})=\Gamma(A_t,c_t)$ as long as the hypothesis of B2(a) held at all times $t'<t$.
3. The hypothesis of (a) fails at time $t'$ iff $c_{t'}=1$ and $k\notin A_{t'}$. Now $c_{t'}=1$ iff $t'=1+m(k+1)$, $m\ge0$. Then $t'\equiv1+m\pmod k$, and since $A_0\equiv\{2-r,\dots,0\}\pmod k$, $A_{t'}\equiv\{3-r+m,\dots,1+m\}\pmod k$. So $k\in A_{t'}$ iff the integer interval $[3-r+m,\,1+m]$ contains a multiple of $k$.
   - For $0\le m\le r-3$: $3-r+m\le0\le1+m$, so it contains $0$; (a) holds.
   - For $m=r-2$: the interval is $[1,r-1]$ with $r-1\le k-1$; it contains no multiple of $k$; (a) fails and (b) applies.
4. Let $t^*=1+(r-2)(k+1)$. By Steps 2–3, $B^t(U_{k,r})=\Gamma(A_t,c_t)\notin S_k$ (Claim B1) for $0\le t\le t^*$, and $B^{t^*+1}(U_{k,r})\in S_k$ by B2(b). Lemma 3 gives $d_B(U_{k,r})=t^*+1=(r-2)(k+1)+2=r(k+1)-2k$. $\square$

(Consistency remarks, not used: $r=k$ gives $U_{k,k}=(k-1,k-1,k-2,\dots,1,1)$ with $d_B=k^2-k$, matching the gated Cell 2 value; $r=k-1$ gives $(k-1,k-2,k-2,\dots,2,1,1)$ with $d_B=k^2-2k-1$, matching the gated Cell 3 witness.)

---

## 5. The family $W_{k,r}=\delta_{k-2}\uplus\{k-2,r+1\}$

Assume $k\ge4$ in this section.

**Configurations.** For $h\in\{1,\dots,k-1\}$ and $A\subseteq\{1,\dots,k\}\setminus\{h,h+1\}$, let $\eta_i=b_i-[i=h]+[i\in A]$ ($1\le i\le k$) and $H(h,A)=(\eta_1,\dots,\eta_k)$ with zeros deleted. Let $h\oplus1=h+1$ for $h\le k-2$, $h\oplus1=1$ for $h=k-1$.

**Claim C1.** $H(h,A)$ is a partition of $T_{k-1}-1+|A|$ and $H(h,A)\notin S_k$.

*Proof.* 1. For $1\le i\le k-1$: $\eta_i-\eta_{i+1}=1-[i=h]+[i+1=h]+[i\in A]-[i+1\in A]$. If $i=h$: $1-1+0+0-0=0$ (as $h,h+1\notin A$). If $i+1=h$: $\ge1+1+0-0=2$ (as $h\notin A$). Otherwise $\ge1+0-1=0$.
2. $\eta_h=b_h-1=k-h-1\ge0$; all other $\eta_i\ge b_i\ge 0$. So the sequence is weakly decreasing and nonnegative, zeros terminal; sum $T_{k-1}-1+|A|$.
3. $\eta_h-b_h=-1\notin\{0,1\}$ with $h\le k$; by Remark 2a, $H(h,A)\notin S_k$. $\square$

**Claim C2.** Let $x=H(h,A)$.
(a) If $h\ne k-1$ or $1\notin A$, then $B(x)=H(h\oplus1,A\oplus1)$ (and this pair is a configuration).
(b) If $h=k-1$ and $1\in A$, then $B(x)=\kappa\bigl((A\setminus\{1\})\oplus1\bigr)\in S_k$.

*Proof.* 1. For $i\le k-2$: $\eta_i\ge k-i-1\ge1$. If $h=k-1$: $k-1,k\notin A$, so $\eta_{k-1}=\eta_k=0$ and $s=k-2$. If $h\ne k-1$: $\eta_{k-1}=1+[k-1\in A]\ge1$, $\eta_k=[k\in A]$, so $s=k-1+[k\in A]$. Also $\eta_1-1=k-2-[h=1]+[1\in A]$.

2. *(a), case $h\le k-2$.* Then $s\ge k-1\ge\eta_1-1$, Lemma 1 applies. Put $h'=h+1\in\{2,\dots,k-1\}$, $A'=A\oplus1$.
   - $y_1=s=k-1+[k\in A]=b_1-[1=h']+[1\in A']$.
   - For $1\le i\le k-1$: $y_{i+1}=\eta_i-1=(k-i-1)-[i=h]+[i\in A]=b_{i+1}-[i+1=h']+[i+1\in A']$.
   - If $k\in A$: $y_{k+1}=\eta_k-1=0$, deleted.
   - Configuration: $h'\in A'\iff h\in A$ (false); $h'+1=h+2\le k$ and $h+2\in A'\iff h+1\in A$ (false).
   So $B(x)=H(h',A')$.

3. *(a), case $h=k-1$, $1\notin A$.* Then $k\ge4$ gives $h\ne1$, so $\eta_1-1=k-2=s$; Lemma 1 applies. $h'=1$, $A'=A\oplus1$; note $1\notin A'$ since $k\notin A$.
   - $y_1=k-2=b_1-[1=h']+[1\in A']$.
   - For $1\le i\le k-2$ (so $i\ne h$): $y_{i+1}=\eta_i-1=k-i-1+[i\in A]=b_{i+1}-[i+1=h']+[i+1\in A']$.
   - There are $s+1=k-1$ entries; entry $k$ of $H(h',A')$ is $b_k+[k\in A']=[k-1\in A]=0$, consistent.
   - Configuration: $h'=1\notin A'$ (shown); $h'+1=2\in A'\iff1\in A$, false by hypothesis.
   So $B(x)=H(1,A')$.

4. *(b).* $h=k-1\ne1$, $1\in A$, $k-1,k\notin A$: $\eta_1=k$, $\eta_i=k-i+[i\in A]$ for $2\le i\le k-2$, $s=k-2$. The parts of $B(x)$: $\eta_1-1=k-1$; $\eta_i-1=k-i-1+[i\in A]\in[1,k-2]$ for $2\le i\le k-2$ (all positive since $i\le k-2$); and $s=k-2$. Sorted: $B(x)=(k-1,k-2,\eta_2-1,\dots,\eta_{k-2}-1)$ ($k-1$ entries).
   Let $A^*=(A\setminus\{1\})\oplus1=\{a+1:a\in A,\,2\le a\le k-2\}\subseteq\{3,\dots,k-1\}$. Then $\kappa(A^*)_1=b_1=k-1$, $\kappa(A^*)_2=b_2=k-2$, $\kappa(A^*)_p=k-p+[p-1\in A]=\eta_{p-1}-1$ for $3\le p\le k-1$, $\kappa(A^*)_k=[k-1\in A]=0$. So $B(x)=\kappa(A^*)\in S_k$. $\square$

**Proposition C.** For $k\ge4$ and $1\le r\le k-3$, $W_{k,r}=\delta_{k-2}\uplus\{k-2,r+1\}$ is a partition of $n=T_{k-1}+r$ with $d_B(W_{k,r})=(k-1)(k-2-r)$.

*Proof.* 1. Let $h_0=1$ and $A_0=\{k-r,\dots,k\}$ ($r+1$ elements). $A_0\cap\{1,2\}=\varnothing$ because $k-r\ge3$. Entries of $H(1,A_0)$: $\eta_1=k-2$; $\eta_i=k-i$ for $2\le i\le k-r-1$ (values $k-2,\dots,r+1$; nonempty as $k-r-1\ge2$); $\eta_i=k-i+1$ for $k-r\le i\le k$ (values $r+1,\dots,1$). The multiset is $\{k-2\}\uplus\{r+1,\dots,k-2\}\uplus\{1,\dots,r+1\}=\delta_{k-2}\uplus\{k-2,r+1\}$, of sum $T_{k-2}+k-1+r=T_{k-1}+r$. So $W_{k,r}=H(h_0,A_0)$.
2. Let $h_t=h_0\oplus t$ ($h_t\equiv1+t\pmod{k-1}$, representatives $1,\dots,k-1$) and $A_t=A_0\oplus t$ ($\equiv A_0+t\pmod k$). By C2(a) and induction, $B^t(W_{k,r})=H(h_t,A_t)$ as long as (a)'s hypothesis held at all earlier times.
3. (a) fails at time $t'$ iff $h_{t'}=k-1$ and $1\in A_{t'}$. $h_{t'}=k-1$ iff $t'=k-2+m(k-1)$, $m\ge0$. Since $A_0\equiv\{-r,\dots,0\}\pmod k$, $1\in A_{t'}$ iff $t'-1\bmod k\in\{0,\dots,r\}$. Here $t'-1=k-3+m(k-1)\equiv k-3-m\pmod k$.
   - For $0\le m<k-3-r$: $k-3-m\in[r+1,k-3]\subseteq[0,k-1]$ is the residue, not in $\{0,\dots,r\}$; (a) holds.
   - For $m=k-3-r$ ($\ge0$): the residue is $r$; (a) fails, (b) applies.
4. Let $t^*=k-2+(k-3-r)(k-1)$. For $0\le t\le t^*$, $B^t(W_{k,r})=H(h_t,A_t)\notin S_k$ (Claim C1); $B^{t^*+1}(W_{k,r})\in S_k$ (C2(b)). By Lemma 3, $d_B(W_{k,r})=t^*+1=(k-1)(k-2-r)$. $\square$

---

## 6. Conclusion and conjecture

**Theorem (lower half, every $n$).** For every $n\ge1$, $D_B(n)\ge F(n)$, with $F$ as in the first line.

*Proof.* $D_B(n)\ge0$ always, which covers $n=1,2$. For $n\ge3$: each term of $F(n)$ is $d_B$ of a partition of $n$, by Proposition A ($n-k+1$), Proposition B ($2\le r\le k$) and Proposition C ($k\ge4$, $1\le r\le k-3$). $D_B(n)$ is the maximum of $d_B$ over partitions of $n$. $\square$

**Conjecture.** $D_B(n)=F(n)$ for every $n\ge1$.

**Evidence (CHECKED, finite only).** Exhaustive exact computation of $D_B(n)$ over all partitions of $n$ agrees with $F(n)$ for every $1\le n\le 62$ (`out/code/conj_check.py`, runs recorded in `out/code/run_conj_1_55.txt`, `out/code/run_conj_56_62.txt`). This proves nothing for $n>62$.

**Not established.** The upper bound $d_B(\lambda)\le F(n)$ for all partitions $\lambda$ of $n$ is not proved for any $n$ beyond the finite check. [GAP: upper half]
