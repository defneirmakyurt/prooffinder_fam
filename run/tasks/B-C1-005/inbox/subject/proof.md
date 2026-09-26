**Statement proved.** Let $k\ge 1$ and $1\le r\le k$, and put $n=T_{k-1}+r$. (a) A partition of $n$ is cyclic if and only if it belongs to $\mathcal C(k,r)=\{\lambda(\varepsilon):\varepsilon\in\{0,1\}^k,\ \varepsilon_0+\dots+\varepsilon_{k-1}=r\}$, where $\lambda(\varepsilon)$ is the sequence $(k-1+\varepsilon_0,\,k-2+\varepsilon_1,\,\dots,\,1+\varepsilon_{k-2},\,\varepsilon_{k-1})$ with a final entry $0$ deleted; so there are exactly $\binom kr$ cyclic partitions of $n$. (b) The number of distinct cycles of $B$ on the partitions of $n$ is $N(k,r)=\frac1k\sum_{d\mid\gcd(k,r)}\varphi(d)\binom{k/d}{r/d}$ ($\varphi$ = Euler's totient). (i) In particular, for $n=T_k$ ($r=k$), $\delta_k$ is the only cyclic partition of $n$, and every partition $\lambda$ of $n$ has some $i\ge0$ with $B^i(\lambda)=\delta_k$.

---

**Reading of the target (stated as required).** "Distinct cycles of $B$ on the partitions of $n$" is read as the cycles of the map $B:\mathcal P(n)\to\mathcal P(n)$ ($\mathcal P(n)$ = set of partitions of $n$), i.e. the distinct sets $O(\lambda)=\{B^t(\lambda):t\ge0\}$ with $\lambda$ cyclic (Step 10.1 shows these sets partition the cyclic partitions). No other reading seems plausible.

**Tools used.** Only elementary facts: finiteness/pigeonhole, Bézout's identity, uniqueness of the weakly decreasing rearrangement of a finite multiset, and the orbit-counting lemma (Burnside's lemma), which is proved in Step 10.3 anyway. No result specific to this problem is cited. The computation in `out/code/` is a sanity check only; no step depends on it.

---

## 0. Conventions

0.1. We index rows from $0$. A partition $\lambda$ of $n$ with $s$ parts is written $\lambda=(\lambda_0,\dots,\lambda_{s-1})$, $\lambda_0\ge\dots\ge\lambda_{s-1}\ge1$, $\sum_a\lambda_a=n$. We write $s=\ell(\lambda)$ and set $\lambda_a:=0$ for $a\ge s$.

0.2. With this indexing, $B(\lambda)$ is the partition whose parts are the positive numbers among $\lambda_0-1,\dots,\lambda_{s-1}-1$ together with one part equal to $s$ (definition of the shift).

0.3. **Cell set.** $Y(\lambda)=\{(a,b)\in\mathbb Z_{\ge0}^2:\ b<\lambda_a\}$. Then $|Y(\lambda)|=\sum_a\lambda_a=n$. The map $\lambda\mapsto Y(\lambda)$ is injective, because $\lambda_a=\#\{b:(a,b)\in Y(\lambda)\}$.

0.4. **Young property.** If $(a,b)\in Y(\lambda)$ and $0\le a'\le a$, $0\le b'\le b$, then $(a',b')\in Y(\lambda)$. Proof: $b<\lambda_a$ forces $\lambda_a\ge1$, so $a<s$. Since $a'\le a<s$ and $\lambda$ is weakly decreasing, $\lambda_{a'}\ge\lambda_a>b\ge b'$.

0.5. **Diagonals.** For $d\ge0$ let $D_d=\{(a,b)\in\mathbb Z_{\ge0}^2:a+b=d\}=\{p_d(0),\dots,p_d(d)\}$, where $p_d(a):=(a,d-a)$. So $|D_d|=d+1$, the $D_d$ are pairwise disjoint, and their union is $\mathbb Z_{\ge0}^2$. A *hole of $\lambda$ on $D_d$* is a point of $D_d\setminus Y(\lambda)$, and a *cell of $\lambda$ on $D_d$* is a point of $D_d\cap Y(\lambda)$.

0.6. $T_d=d(d+1)/2=\sum_{j=0}^{d-1}(j+1)=\sum_{j<d}|D_j|$. Also $T_{d+1}-T_d=d+1>0$, so $(T_d)$ is strictly increasing and the rank is well defined.

## 1. An energy that does not increase

1.1. **Definition.** For a finite sequence $x=(x_0,\dots,x_m)$ of nonnegative integers put
$$E(x)=\sum_{a=0}^{m}\Bigl(a\,x_a+\tbinom{x_a}{2}\Bigr),\qquad \tbinom{x}{2}=\tfrac{x(x-1)}2 .$$
A zero entry contributes $a\cdot0+\binom02=0$. So appending or deleting zero entries at the end does not change $E$. For a partition $\lambda$, $E(\lambda)$ means $E(\lambda_0,\dots,\lambda_{s-1})$.

1.2. **Lemma 1 (the unsorted shift keeps $E$).** Let $\lambda$ have $s$ parts, and let $\mu=(\mu_0,\dots,\mu_s):=(s,\lambda_0-1,\dots,\lambda_{s-1}-1)$. Then $E(\mu)=E(\lambda)$.

*Proof.* For an integer $x\ge1$, $\binom{x-1}{2}=\binom x2-(x-1)$. Hence for $0\le a\le s-1$ the entry $\mu_{a+1}=\lambda_a-1$ contributes
$$(a+1)(\lambda_a-1)+\tbinom{\lambda_a}{2}-(\lambda_a-1)=a(\lambda_a-1)+\tbinom{\lambda_a}{2}=a\lambda_a+\tbinom{\lambda_a}2-a .$$
The entry $\mu_0=s$ contributes $0\cdot s+\binom s2$. Summing,
$$E(\mu)=\tbinom s2+\sum_{a=0}^{s-1}\Bigl(a\lambda_a+\tbinom{\lambda_a}2\Bigr)-\sum_{a=0}^{s-1}a=\tbinom s2+E(\lambda)-\tbinom s2=E(\lambda).\qquad\square$$

1.3. **Lemma 2 (sorting lowers $E$).** Let $x=(x_0,\dots,x_m)$ be nonnegative integers and $x^*$ the weakly decreasing rearrangement of $x$. Then $E(x^*)\le E(x)$. If $x$ is not weakly decreasing, then $E(x^*)<E(x)$.

*Proof.* The part $\sum_a\binom{x_a}2$ does not change under rearrangement. So it suffices to compare $F(x)=\sum_a a\,x_a$.

Let $y$ be any rearrangement of $x$ with an index $a$ such that $y_a<y_{a+1}$, and let $y'$ be $y$ with entries $a$ and $a+1$ swapped. Then
$$F(y')-F(y)=a\,y_{a+1}+(a+1)y_a-a\,y_a-(a+1)y_{a+1}=y_a-y_{a+1}<0 .$$

Start from $y^{(0)}=x$. While $y^{(j)}$ is not weakly decreasing, it has an index $a$ with $y^{(j)}_a<y^{(j)}_{a+1}$; let $y^{(j+1)}$ be the swapped sequence. Then $F$ strictly decreases along the process. All $y^{(j)}$ lie in the finite set of rearrangements of $x$, so no rearrangement repeats and the process stops, at some $y^{(J)}$ that is weakly decreasing. A finite multiset has exactly one weakly decreasing arrangement, so $y^{(J)}=x^*$. Hence $F(x^*)\le F(x)$. If $x$ is not weakly decreasing, then $J\ge1$ and $F(x^*)<F(x)$. $\square$

1.4. **Lemma 3 (monotonicity).** For every partition $\lambda$ (with $s$ parts and $\mu$ as in Lemma 1):

(a) $E(B(\lambda))\le E(\lambda)$;

(b) if $E(B(\lambda))=E(\lambda)$, then $s\ge\lambda_0-1$;

(c) if $s\ge\lambda_0-1$, then $B(\lambda)$ is $\mu$ with its zero entries deleted, and these zero entries all lie at the end of $\mu$.

*Proof.* By Step 0.2, the entries of $\mu$ are the parts of $B(\lambda)$ together with some zeros (the entries $\lambda_a-1=0$). So the weakly decreasing rearrangement is $\mu^*=(B(\lambda),0,\dots,0)$, and by Step 1.1, $E(\mu^*)=E(B(\lambda))$.

(a) By Lemma 2 and Lemma 1, $E(B(\lambda))=E(\mu^*)\le E(\mu)=E(\lambda)$.

The sequence $(\mu_1,\dots,\mu_s)=(\lambda_0-1,\dots,\lambda_{s-1}-1)$ is always weakly decreasing. So $\mu$ is weakly decreasing if and only if $\mu_0\ge\mu_1$, i.e. $s\ge\lambda_0-1$.

(b) If $E(B(\lambda))=E(\lambda)=E(\mu)$, then by Lemma 2, $\mu$ is weakly decreasing, i.e. $s\ge\lambda_0-1$.

(c) If $s\ge\lambda_0-1$, then $\mu$ is weakly decreasing, so $\mu=\mu^*=(B(\lambda),0,\dots,0)$. $\square$

## 2. Cell dynamics on a cycle

2.1. **Definition.** Let $\tau:\mathbb Z_{\ge0}^2\to\mathbb Z_{\ge0}^2$ be given by $\tau(a,b)=(a+1,b-1)$ if $b\ge1$, and $\tau(a,0)=(0,a)$.

$\tau$ is a bijection, with inverse $(a,b)\mapsto(a-1,b+1)$ if $a\ge1$ and $(0,b)\mapsto(b,0)$. Check: for $b\ge1$, $\tau(a,b)=(a+1,b-1)$ has first coordinate $\ge1$ and maps back to $(a,b)$; and $\tau(a,0)=(0,a)$ maps back to $(a,0)$. Conversely, for $a\ge1$ the inverse gives $(a-1,b+1)$, whose second coordinate is $\ge1$, and $\tau(a-1,b+1)=(a,b)$; and $(0,b)\mapsto(b,0)\mapsto(0,b)$.

2.2. **Lemma 4 (sort-free step moves cells by $\tau$).** If $s\ge\lambda_0-1$, then $Y(B(\lambda))=\tau(Y(\lambda))$.

*Proof.* Let $\nu=B(\lambda)$. By Lemma 3(c) and the convention in Step 0.1, $\nu_0=s$, $\nu_{a+1}=\lambda_a-1$ for $0\le a\le s-1$, and $\nu_c=0$ for $c>s$. Hence
$$Y(\nu)=\{(0,b):0\le b<s\}\ \sqcup\ \{(a+1,b'):0\le a<s,\ 0\le b'<\lambda_a-1\}.$$
Also $Y(\lambda)=\{(a,0):0\le a<s\}\sqcup\{(a,b):0\le a<s,\ 1\le b<\lambda_a\}$, because every row $a<s$ has $\lambda_a\ge1$.

$\tau$ maps the first set onto $\{(0,a):0\le a<s\}$, which is the first set for $Y(\nu)$. It maps the second set onto $\{(a+1,b-1):0\le a<s,\ 1\le b<\lambda_a\}$, which is the second set for $Y(\nu)$ (put $b'=b-1$). $\square$

2.3. **Lemma 5 ($\tau$ rotates each diagonal).** For $d\ge0$ and $0\le a\le d$: $\tau(p_d(a))=p_d(a+1)$ if $a<d$, and $\tau(p_d(d))=p_d(0)$. Hence $\tau(D_d)=D_d$, and for every $t\ge0$,
$$\tau^t(p_d(a))=p_d\bigl((a+t)\bmod (d+1)\bigr).$$

*Proof.* If $a<d$, then $p_d(a)=(a,d-a)$ with $d-a\ge1$, so $\tau(p_d(a))=(a+1,d-a-1)=p_d(a+1)$. Also $p_d(d)=(d,0)\mapsto(0,d)=p_d(0)$. So in both cases $\tau(p_d(a))=p_d((a+1)\bmod(d+1))$. The formula for $\tau^t$ follows by induction on $t$: $\tau^{t+1}(p_d(a))=\tau(p_d(c))$ with $c=(a+t)\bmod(d+1)$, and this equals $p_d((c+1)\bmod(d+1))=p_d((a+t+1)\bmod(d+1))$. $\square$

2.4. **Lemma 6 (on a cycle every step is sort-free).** Let $\lambda$ be cyclic and $\lambda^{(t)}:=B^t(\lambda)$ for $t\ge0$. Then for every $t\ge0$:

(a) $\lambda^{(t)}$ is cyclic;

(b) $\ell(\lambda^{(t)})\ge\lambda^{(t)}_0-1$;

(c) $Y(\lambda^{(t)})=\tau^t(Y(\lambda))$.

*Proof.* Let $p\ge1$ with $B^p(\lambda)=\lambda$. Then $\lambda^{(t+p)}=\lambda^{(t)}$ for all $t$.

(a) $B^p(\lambda^{(t)})=\lambda^{(t+p)}=\lambda^{(t)}$.

(b) By Lemma 3(a), $E(\lambda^{(0)})\ge E(\lambda^{(1)})\ge\dots\ge E(\lambda^{(p)})=E(\lambda^{(0)})$, so all these values are equal. Hence $E(B(\lambda^{(t)}))=E(\lambda^{(t)})$ for $0\le t<p$, and by $p$-periodicity for all $t\ge0$. Lemma 3(b) gives (b).

(c) By (b) and Lemma 4, $Y(\lambda^{(t+1)})=\tau(Y(\lambda^{(t)}))$ for all $t$. Induction on $t$ gives (c). $\square$

## 3. Shape of a cyclic partition

3.1. **Proposition 7 (no hole on a lower diagonal than a cell).** Let $\lambda$ be cyclic and $0\le d<d'$. Then $\lambda$ cannot have both a hole on $D_d$ and a cell on $D_{d'}$.

*Proof.* Suppose, for a contradiction, that $q=p_d(x)\notin Y(\lambda)$ and $c=p_{d'}(y)\in Y(\lambda)$. Put $P=d+1$, $Q=d'+1$, $g=\gcd(P,Q)$.

(1) *Positions at time $t$.* By Lemma 6(c), $Y(\lambda^{(t)})=\tau^t(Y(\lambda))$. Since $\tau^t$ is injective (Step 2.1) and $q\notin Y(\lambda)$, we get $\tau^t(q)\notin Y(\lambda^{(t)})$. Also $\tau^t(c)\in Y(\lambda^{(t)})$. By Lemma 5, $\tau^t(q)=p_d((x+t)\bmod P)$ and $\tau^t(c)=p_{d'}((y+t)\bmod Q)$.

(2) *Choice of $t$.* Let $t_0\in\{0,\dots,P-1\}$ with $t_0\equiv -x\pmod P$.

$g$ divides $Q-P=d'-d\ge1$, so $g\le Q-P$. The integers $0,1,\dots,Q-P$ therefore include at least $g$ consecutive integers, so one of them, call it $c^*$, satisfies $c^*\equiv y+t_0\pmod g$.

By Bézout's identity there are integers $u,v$ with $uP+vQ=g$. Write $c^*-y-t_0=gm$ with $m\in\mathbb Z$, and let $j=(um)\bmod Q\in\{0,\dots,Q-1\}$. Then $jP\equiv umP\equiv gm=c^*-y-t_0\pmod Q$.

Put $t=t_0+jP\ge0$. Then $(x+t)\bmod P=(x+t_0)\bmod P=0$. Also $(y+t)\bmod Q=(y+t_0+jP)\bmod Q=c^*$, because $0\le c^*\le Q-P<Q$.

(3) *Contradiction.* At this time $t$, (1) gives $p_d(0)=(0,d)\notin Y(\lambda^{(t)})$ and $p_{d'}(c^*)=(c^*,d'-c^*)\in Y(\lambda^{(t)})$. Here $0\le c^*$ and $d'-c^*\ge d'-(Q-P)=d$. So the Young property (Step 0.4), applied with $(a',b')=(0,d)$, gives $(0,d)\in Y(\lambda^{(t)})$, a contradiction. $\square$

3.2. **Corollary 8.** Let $\lambda$ be a cyclic partition of $n$. Then there are integers $e\ge0$ and $r'$ with $0\le r'\le e$ such that:

- $D_j\subseteq Y(\lambda)$ for $j<e$;
- $|D_e\cap Y(\lambda)|=r'$;
- $D_j\cap Y(\lambda)=\varnothing$ for $j>e$;
- $n=T_e+r'$.

*Proof.* If $D_0,\dots,D_n$ were all contained in $Y(\lambda)$, then $|Y(\lambda)|\ge\sum_{d=0}^n(d+1)>n$, contradicting Step 0.3. So $e:=\min\{d\ge0:D_d\not\subseteq Y(\lambda)\}$ exists, and $D_j\subseteq Y(\lambda)$ for $j<e$.

$D_e$ has a hole. So by Proposition 7 (with $d=e$), no $D_j$ with $j>e$ contains a cell.

$r':=|D_e\cap Y(\lambda)|$ satisfies $r'\le|D_e|-1=e$.

Since $\mathbb Z_{\ge0}^2=\bigsqcup_d D_d$ (Step 0.5), $n=|Y(\lambda)|=\sum_{j<e}(j+1)+r'=T_e+r'$ (Step 0.6). $\square$

## 4. The family $\mathcal C(k,r)$ and the action of $B$ on it

4.1. **Definitions.** Fix $k\ge1$ and $1\le r\le k$. Let $W(k,r)=\{\varepsilon=(\varepsilon_0,\dots,\varepsilon_{k-1})\in\{0,1\}^k:\sum_a\varepsilon_a=r\}$.

For $\varepsilon\in W(k,r)$, let $L(\varepsilon)$ be the length-$k$ list with entries $L_a=k-1-a+\varepsilon_a$ ($0\le a\le k-1$). Let $\lambda(\varepsilon)$ be $L(\varepsilon)$ with its last entry deleted if that entry is $0$.

Put $\mathcal C(k,r)=\{\lambda(\varepsilon):\varepsilon\in W(k,r)\}$, and let $\rho$ be the cyclic shift $\rho(\varepsilon)=(\varepsilon_{k-1},\varepsilon_0,\dots,\varepsilon_{k-2})$, i.e. $(\rho\varepsilon)_a=\varepsilon_{(a-1)\bmod k}$.

4.2. **Theorem 9.** For $\varepsilon\in W(k,r)$:

(a) $\lambda(\varepsilon)$ is a partition of $T_{k-1}+r$ with $\ell(\lambda(\varepsilon))=k-1+\varepsilon_{k-1}$;

(b) $Y(\lambda(\varepsilon))=D_0\cup\dots\cup D_{k-2}\cup\{p_{k-1}(a):\varepsilon_a=1\}$;

(c) $\varepsilon\mapsto\lambda(\varepsilon)$ is injective on $W(k,r)$;

(d) $B(\lambda(\varepsilon))=\lambda(\rho\varepsilon)$, and $\rho\varepsilon\in W(k,r)$.

*Proof.*

(a) For $a\le k-2$: $L_a\ge k-1-a\ge1$. The last entry is $L_{k-1}=\varepsilon_{k-1}\in\{0,1\}$. For $0\le a\le k-2$: $L_a-L_{a+1}=1+\varepsilon_a-\varepsilon_{a+1}\ge0$. So $\lambda(\varepsilon)$ is weakly decreasing with positive entries.

It is nonempty: if $k\ge2$ then $L_0\ge1$ is kept, and if $k=1$ then $r=1$ forces $\varepsilon_0=1$ and $L_0=1$. Its sum is $\sum_{a=0}^{k-1}(k-1-a)+r=T_{k-1}+r$. Its number of parts is $k-1$ plus one if $\varepsilon_{k-1}=1$.

(b) Row $a\le k-1$ of $Y(\lambda(\varepsilon))$ is $\{(a,b):0\le b<k-1-a+\varepsilon_a\}$. This is $\{(a,b):a+b\le k-2\}$, together with $(a,k-1-a)=p_{k-1}(a)$ exactly when $\varepsilon_a=1$. There are no rows $a\ge k$. Every point of $D_0\cup\dots\cup D_{k-2}$ has first coordinate $\le k-2$. So the union over rows is the displayed set.

(c) $\varepsilon_a=1$ if and only if $p_{k-1}(a)\in Y(\lambda(\varepsilon))$, by (b). So $Y(\lambda(\varepsilon))$ determines $\varepsilon$.

(d) Write $\lambda=\lambda(\varepsilon)$ and $s=\ell(\lambda)=k-1+\varepsilon_{k-1}$. Then $\lambda_0-1=L_0-1=k-2+\varepsilon_0\le k-1\le s$ (this also holds for $k=1$: $\lambda_0-1=0\le s$). So Lemma 3(c) applies, and $B(\lambda)$ is $\mu=(s,\lambda_0-1,\dots,\lambda_{s-1}-1)$ with its trailing zeros deleted. Compare $\mu$ with $L(\rho\varepsilon)$:

- $\mu_0=s=k-1+\varepsilon_{k-1}=k-1-0+(\rho\varepsilon)_0=L(\rho\varepsilon)_0$.
- For $1\le a\le\min(s,k-1)$: $\mu_a=\lambda_{a-1}-1=(k-1-(a-1)+\varepsilon_{a-1})-1=k-1-a+(\rho\varepsilon)_a=L(\rho\varepsilon)_a$. (Here $a-1\le k-2$, so $\lambda_{a-1}=L_{a-1}$.)
- Case $\varepsilon_{k-1}=0$: then $s=k-1$, so $\mu=(\mu_0,\dots,\mu_{k-1})=L(\rho\varepsilon)$.
- Case $\varepsilon_{k-1}=1$: then $s=k$ and $\mu_k=\lambda_{k-1}-1=L_{k-1}-1=0$, so $\mu=(L(\rho\varepsilon),0)$.

In $L(\rho\varepsilon)$ only the last entry can be $0$ (by (a) applied to $\rho\varepsilon$). So in both cases, deleting trailing zeros from $\mu$ gives $\lambda(\rho\varepsilon)$. Finally, $\rho$ permutes the coordinates, so $\sum_a(\rho\varepsilon)_a=r$. $\square$

4.3. **Corollary 10.** Every element of $\mathcal C(k,r)$ is cyclic.

*Proof.* $\rho^k=\mathrm{id}$, since $(\rho^t\varepsilon)_a=\varepsilon_{(a-t)\bmod k}$ by induction on $t$. By Theorem 9(d) and induction, $B^t(\lambda(\varepsilon))=\lambda(\rho^t\varepsilon)$ for all $t\ge0$. Hence $B^k(\lambda(\varepsilon))=\lambda(\varepsilon)$, with $k\ge1$. $\square$

## 5. Target (ii)(a): the cyclic partitions

5.1. **Theorem 11.** Let $k\ge1$, $1\le r\le k$, $n=T_{k-1}+r$. A partition $\lambda$ of $n$ is cyclic if and only if $\lambda\in\mathcal C(k,r)$. The number of cyclic partitions of $n$ is $\binom kr$.

*Proof.* ($\Leftarrow$) By Theorem 9(a), every element of $\mathcal C(k,r)$ is a partition of $n$. It is cyclic by Corollary 10.

($\Rightarrow$) Let $\lambda\vdash n$ be cyclic, and take $e,r'$ from Corollary 8, so that $n=T_e+r'$ with $0\le r'\le e$.

*Case $r'\ge1$.* Then $T_e<n\le T_e+e<T_e+e+1=T_{e+1}$, so the rank of $n$ is $e+1$. The rank of $n$ is also $k$, since $T_{k-1}<n\le T_{k-1}+k=T_k$. By uniqueness of the rank (Step 0.6), $k=e+1$, and then $r=n-T_{k-1}=r'$.

Corollary 8 gives $Y(\lambda)=D_0\cup\dots\cup D_{k-2}\cup S$ with $S\subseteq D_{k-1}$, $|S|=r$. Define $\varepsilon_a=1$ if $p_{k-1}(a)\in S$ and $\varepsilon_a=0$ otherwise. Then $\varepsilon\in W(k,r)$, and by Theorem 9(b), $Y(\lambda(\varepsilon))=Y(\lambda)$. Since $Y$ is injective (Step 0.3), $\lambda=\lambda(\varepsilon)\in\mathcal C(k,r)$.

*Case $r'=0$.* Then $n=T_e$, and $e\ge1$ because $n\ge1=T_1>T_0$. Since $T_{e-1}<T_e\le T_e$, the rank of $n$ is $e$. So $k=e$ and $r=n-T_{k-1}=T_k-T_{k-1}=k$.

Corollary 8 gives $Y(\lambda)=D_0\cup\dots\cup D_{k-1}$, and this equals $Y(\lambda(1,\dots,1))$ by Theorem 9(b) (all of $D_{k-1}$ included). So $\lambda=\lambda(1,\dots,1)\in\mathcal C(k,k)=\mathcal C(k,r)$.

*Count.* By Theorem 9(c), $|\mathcal C(k,r)|=|W(k,r)|=\binom kr$. $\square$

5.2. **Explicit description.** $\mathcal C(k,r)$ is the set of partitions $(k-1+\varepsilon_0,\,k-2+\varepsilon_1,\,\dots,\,1+\varepsilon_{k-2},\,\varepsilon_{k-1})$ (a final $0$ omitted) with $\varepsilon_a\in\{0,1\}$ and exactly $r$ of the $\varepsilon_a$ equal to $1$. In words: add $1$ to exactly $r$ of the $k$ entries of $(k-1,k-2,\dots,1,0)$. Equivalently: the cell set consists of all diagonals $D_0,\dots,D_{k-2}$ plus any $r$ of the $k$ points of $D_{k-1}$.

## 6. Target (ii)(b): the number of cycles

6.1. **Cycles are well defined.** For cyclic $\lambda$ with $B^p(\lambda)=\lambda$ ($p\ge1$), put $O(\lambda)=\{B^t(\lambda):t\ge0\}$. Every element of $O(\lambda)$ is cyclic (Lemma 6(a)).

If $\mu=B^t(\lambda)$, write $t'=t\bmod p$. Then $B^{p-t'}(\mu)=B^{p-t'+t}(\lambda)=\lambda$, because $p-t'+t$ is a multiple of $p$. So $\lambda\in O(\mu)$, hence $O(\lambda)\subseteq O(\mu)$; together with $O(\mu)\subseteq O(\lambda)$ this gives $O(\mu)=O(\lambda)$.

Therefore two sets $O(\lambda),O(\lambda')$ either coincide or are disjoint (if $\mu$ lies in both, both equal $O(\mu)$). So the distinct cycles partition the set of cyclic partitions of $n$, which is $\mathcal C(k,r)$ by Theorem 11.

6.2. **Transfer to words.** Let $\Lambda:W(k,r)\to\mathcal C(k,r)$, $\Lambda(\varepsilon)=\lambda(\varepsilon)$. This is a bijection: it is surjective by definition and injective by Theorem 9(c). By Theorem 9(d), $B^t(\Lambda(\varepsilon))=\Lambda(\rho^t\varepsilon)$. Hence
$$O(\Lambda(\varepsilon))=\Lambda\bigl(\{\rho^t\varepsilon:t\ge0\}\bigr)=\Lambda\bigl(\{\rho^j\varepsilon:0\le j<k\}\bigr),$$
the last equality because $\rho^k=\mathrm{id}$ (Corollary 10).

The group $G=\mathbb Z/k\mathbb Z$ acts on $W(k,r)$ by $j\cdot\varepsilon=\rho^j\varepsilon$; this is well defined since $\rho^k=\mathrm{id}$. So $\Lambda$ maps $G$-orbits bijectively onto cycles of $B$, and the number of cycles equals the number of $G$-orbits on $W(k,r)$. (Moreover, the cycle through $\Lambda(\varepsilon)$ has as many elements as the $G$-orbit of $\varepsilon$, which is a divisor of $k$.)

6.3. **Orbit counting (Burnside's lemma, proved here).** For a finite group $G$ acting on a finite set $X$, the number of orbits is $\frac1{|G|}\sum_{h\in G}|\mathrm{Fix}(h)|$.

*Proof.* Count pairs $\{(h,x):hx=x\}$ in two ways:
$$\sum_h|\mathrm{Fix}(h)|=\sum_x|\mathrm{Stab}(x)|=\sum_x\frac{|G|}{|Gx|}.$$
The middle equality regroups the pairs by $x$; the last uses the orbit–stabiliser bijection $h\,\mathrm{Stab}(x)\mapsto hx$. Each orbit $\Omega$ contributes $\sum_{x\in\Omega}|G|/|\Omega|=|G|$. So the sum is $|G|$ times the number of orbits. $\square$

6.4. **Fixed points.** Let $0\le j\le k-1$ and $g=\gcd(j,k)$, with $\gcd(0,k)=k$. We claim that $\rho^j\varepsilon=\varepsilon$ holds if and only if $\varepsilon_a=\varepsilon_{a'}$ whenever $a\equiv a'\pmod g$.

*($\Rightarrow$)* By Bézout, $g=uj+vk$ for some integers $u,v$. Replace $u$ by $u\bmod k\ge0$; this keeps $uj\equiv g\pmod k$. If $\rho^j\varepsilon=\varepsilon$, then $\rho^{uj}\varepsilon=\varepsilon$, and $\rho^{uj}=\rho^{g}$ because $\rho^k=\mathrm{id}$. So $\varepsilon_a=\varepsilon_{(a-g)\bmod k}$ for all $a$. Iterating, $\varepsilon_a=\varepsilon_{(a-mg)\bmod k}$ for all $m\ge0$. Since $g\mid k$, the numbers $(a-mg)\bmod k$, $m\ge0$, run through every index in $\{0,\dots,k-1\}$ congruent to $a$ mod $g$.

*($\Leftarrow$)* If $\varepsilon$ is constant on residue classes mod $g$, then since $g\mid j$ and $g\mid k$, $(a-j)\bmod k\equiv a\pmod g$. So $(\rho^j\varepsilon)_a=\varepsilon_{(a-j)\bmod k}=\varepsilon_a$.

*Counting fixed words.* Such $\varepsilon$ correspond bijectively to $(\varepsilon_0,\dots,\varepsilon_{g-1})\in\{0,1\}^g$, and each value is repeated $k/g$ times. So $\sum_a\varepsilon_a=(k/g)\sum_{a<g}\varepsilon_a$. Hence
$$|\mathrm{Fix}(\rho^j)\cap W(k,r)|=\begin{cases}\binom{g}{rg/k}&\text{if }(k/g)\mid r,\\ 0&\text{otherwise.}\end{cases}$$

6.5. **Counting $j$ with a given gcd.** For $g\mid k$, the $j\in\{0,\dots,k-1\}$ with $\gcd(j,k)=g$ are exactly $j=gj'$ with $j'\in\{0,\dots,k/g-1\}$ and $\gcd(j',k/g)=1$.

Their number is $\varphi(k/g)$, where $\varphi(m)=\#\{1\le i\le m:\gcd(i,m)=1\}$. Indeed, replacing $j'=0$ by $j'=m$ ($m=k/g$) turns the index range into $\{1,\dots,m\}$ and does not change $\gcd(j',m)$, which is $m$ in both cases.

6.6. **Theorem 12.** The number of distinct cycles of $B$ on the partitions of $n=T_{k-1}+r$ is
$$N(k,r)=\frac1k\sum_{d\mid\gcd(k,r)}\varphi(d)\binom{k/d}{r/d}.$$

*Proof.* By Steps 6.2 and 6.3 (with $|G|=k$) and Steps 6.4 and 6.5, the number of cycles is
$$\frac1k\sum_{g\mid k}\varphi(k/g)\,[\,(k/g)\mid r\,]\binom{g}{rg/k}.$$
Substitute $d=k/g$. As $g$ runs over the divisors of $k$, so does $d$. The condition becomes $d\mid r$, i.e. $d\mid\gcd(k,r)$, and the summand becomes $\varphi(d)\binom{k/d}{r/d}$. $\square$

6.7. **Special values (consistency).** For $r=k$: $N(k,k)=\frac1k\sum_{d\mid k}\varphi(d)=1$, using $\sum_{d\mid k}\varphi(d)=k$, which follows from Step 6.5 by summing over $g\mid k$. This matches $\mathcal C(k,k)=\{\delta_k\}$.

For $r=1$ or $r=k-1$ (with $k\ge2$): $\gcd(k,r)=1$, so $N=\binom k r/k=1$. There is a single cycle, of length $k$.

## 7. Target (i): triangular $n$

7.1. **Theorem 13.** Let $k\ge1$ and $n=T_k$. Then $\delta_k$ is the only cyclic partition of $n$, and for every partition $\lambda$ of $n$ there is $i\ge0$ with $B^i(\lambda)=\delta_k$.

*Proof.* Since $T_{k-1}<T_k\le T_k$, the rank of $n$ is $k$, and $n=T_{k-1}+k$, i.e. $r=k$. By Theorem 11, the cyclic partitions of $n$ form $\mathcal C(k,k)$. Since $W(k,k)=\{(1,\dots,1)\}$, this set is $\{\lambda(1,\dots,1)\}=\{(k,k-1,\dots,1)\}=\{\delta_k\}$.

Now let $\lambda\vdash n$, and let $M=|\mathcal P(n)|<\infty$. The $M+1$ partitions $B^0(\lambda),\dots,B^M(\lambda)$ all lie in $\mathcal P(n)$, so by the pigeonhole principle $B^i(\lambda)=B^j(\lambda)$ for some $0\le i<j\le M$. Then $B^{j-i}(B^i(\lambda))=B^i(\lambda)$ with $j-i\ge1$, so $B^i(\lambda)$ is cyclic, hence $B^i(\lambda)=\delta_k$. $\square$

## 8. Edge cases

- $k=1$ ($n=1$, $r=1$): $\mathcal C(1,1)=\{(1)\}$, $B((1))=(1)$, $N(1,1)=1$. The proofs above cover this case: Theorem 9(a),(d) treat $k=1$ explicitly, and Proposition 7 and Corollary 8 involve no restriction on $k$.
- $r=k$ is the triangular case of Section 7.
- In Corollary 8 the case $r'=0$ ($n$ triangular) is handled separately in Theorem 11.
- In Proposition 7 the argument needs $d<d'$ (so that $Q-P\ge1$ and $g\le Q-P$); nothing else about $d,d'$ is used.

## 9. What is established

All three targets are proved for every $k\ge1$ and every $1\le r\le k$:

- (i) is Theorem 13;
- (ii)(a) is Theorem 11: the cyclic partitions are exactly $\mathcal C(k,r)$, and there are $\binom kr$ of them;
- (ii)(b) is Theorem 12: there are $N(k,r)=\frac1k\sum_{d\mid\gcd(k,r)}\varphi(d)\binom{k/d}{r/d}$ cycles, i.e. the number of binary necklaces of length $k$ with $r$ ones.

No step relies on computation. As a sanity check only, `out/code/check_c1.py` confirms (ii)(a), (ii)(b) and (i) by brute force for $1\le n\le45$.

KNOWN GAPS: none found.
