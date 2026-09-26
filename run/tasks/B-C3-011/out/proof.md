**Statement proved.** For every $k\ge 4$, every $n$ with $T_{k-1}<n<T_k$ and every partition $\lambda$ of $n$: $d_B(\lambda)\le k^2-2k-1$. In particular $D_B(T_k-1)\le k^2-2k-1$ for every $k\ge 4$.

Reading of the target: exactly as in TARGET; no ambiguity had to be resolved.

**Repair note.** The subject proof (B-C3-004) proved (a) only for $\delta_{k-1}\subseteq\lambda\subseteq\delta_{k+1}$ and marked (a) in general as [GAP] (its Step 6.2). That route is not continued. Here (a) is proved for *all* $\lambda$ by the c-sequence method (the method of Part B of the gated Cell-2 proof), with a new end-of-orbit lemma for non-triangular $n$ (§9), two new length lemmas (§6, §7) and a new case analysis (§10–§11). Lemmas 1.1, 1.3, 2, 3, 4 below are Lemmas B1, B2, B3, B8, B7 of the gated Cell-2 proof; they are re-proved here so that this text is self-contained. The subject's lower bound $D_B(T_k-1)\ge k^2-2k-1$ is not re-proved here (TARGET says it is already proved).

**Only assumption used (B-C1, gated).** For $k\ge2$ and $n=T_{k-1}+r$ with $1\le r\le k-1$: a partition of $n$ is cyclic if and only if it equals $\lambda(e)$ for some $e\in\{0,1\}^k$ with $\sum_j e_j=r$, where $\lambda(e)$ is defined in §8.

**Standing notation.** $\lambda=(\lambda_1,\dots,\lambda_s)\vdash n\ge1$. For $i\ge1$, *row $i$* is the partition $B^{i-1}(\lambda)$ (row 1 is $\lambda$), and $c_i$ is its number of parts. Every $c_i\ge1$.

---

## §1. Column model (any $\lambda\vdash n\ge 1$)

**1.1 Lemma.** For every $i\ge1$ the parts of row $i$ are exactly the positive entries (with multiplicity) of the list
$$\Lambda_i=\bigl(\lambda_1-(i-1),\dots,\lambda_s-(i-1),\ c_1-(i-2),\ c_2-(i-3),\dots,\ c_{i-1}-0\bigr),$$
i.e. the entries $\lambda_j-(i-1)$ ($1\le j\le s$) and $c_u-(i-1-u)$ ($1\le u\le i-1$).

*Proof.* Induction on $i$. For $i=1$ the list is $(\lambda_1,\dots,\lambda_s)$, all positive, and row 1 is $\lambda$. Step $i\to i+1$: by the definition of $B$, the parts of row $i+1=B(\text{row }i)$ are the numbers $\pi-1$ for the parts $\pi\ge2$ of row $i$, together with one part $c_i$. The list $\Lambda_{i+1}$ is $\Lambda_i$ with every entry decreased by $1$, followed by the entry $c_i-0=c_i$. An entry $a$ of $\Lambda_i$ gives a positive entry $a-1$ of $\Lambda_{i+1}$ iff $a\ge2$; by the induction hypothesis the entries $a\ge2$ of $\Lambda_i$ are exactly the parts $\pi\ge2$ of row $i$. The last entry $c_i\ge1$ is positive. So the positive entries of $\Lambda_{i+1}$ are exactly the parts of row $i+1$. $\square$

**1.2 Columns.** Call the index $j$ of the entry $\lambda_j-(i-1)$ the *$\lambda$-column $j$* and the index $u$ of the entry $c_u-(i-1-u)$ the *c-column $u$*. Say a column *covers row $i$* if its entry in $\Lambda_i$ exists and is positive:
- $\lambda$-column $j$ covers row $i$ iff $1\le i\le\lambda_j$;
- c-column $u$ covers row $i$ iff $u+1\le i\le u+c_u$ (the entry exists iff $u\le i-1$, and $c_u-(i-1-u)>0$ iff $i\le u+c_u$).

So every column covers a non-empty interval of consecutive rows ($[1,\lambda_j]$, resp. $[u+1,u+c_u]$, non-empty as $c_u\ge1$); its largest element is the row where the column *ends*. If a column covers row $i$, its entry there, called its *remaining length at row $i$*, is (last row covered)$-i+1$: $\lambda_j-i+1$, resp. $u+c_u-i+1$. By 1.1:

(1.2a) $c_i$ = number of columns covering row $i$;

(1.2b) the multiset of remaining lengths at row $i$ of the columns covering row $i$ equals the multiset of parts of row $i$; in particular these remaining lengths sum to $n$.

Let $L_i$ be the number of columns that end at row $i$.

**1.3 Lemma (row step).** $c_{i+1}=c_i+1-L_i$ for all $i\ge1$. Hence $c_{i+1}\le c_i+1$; $c_{i+1}=c_i+1$ iff $L_i=0$; $c_{i+1}=c_i$ iff $L_i=1$. Iterating, $c_{u+d}\le c_u+d$ for $u\ge1$, $d\ge0$.

*Proof.* A column covering row $i+1$ but not row $i$ must have $i+1$ as the first row it covers. $\lambda$-columns start at row $1<i+1$; c-column $u$ starts at row $u+1$, so this column is c-column $i$, which does cover row $i+1$ (as $c_i\ge1$). A column covering row $i$ covers row $i+1$ iff it does not end at row $i$ (intervals). So the columns covering row $i+1$ are the $c_i-L_i$ columns covering row $i$ that do not end there, plus c-column $i$. Apply (1.2a). $\square$

(1.3') In particular, if $L_i=0$, every column covering row $i$ also covers row $i+1$; if $L_i=1$ and some known column ends at row $i$, every other column covering row $i$ covers row $i+1$.

**Definition (pattern).** A *pattern* $(p,q,x)$ is a triple of integers with $q\ge p+2$ and
$$c_p=x-1,\qquad c_{p+1}=\dots=c_{q-1}=x,\qquad c_q=x+1 .$$
Its *length* is $\ell=q-p\ge2$. Since $c_p\ge1$, $x\ge2$.

## §2. Sandwich lemma

**Lemma 2.** If $1\le i<j$ and $c_i<x<c_j$ ($x$ an integer), there is a pattern $(p,q,x)$ with $i\le p$ and $q\le j$.

*Proof.* Let $p$ be the largest index in $[i,j-1]$ with $c_p\le x-1$ ($p=i$ qualifies). If $p+1<j$ then $c_{p+1}\ge x$ by maximality; if $p+1=j$ then $c_{p+1}=c_j>x$. By 1.3, $c_{p+1}\le c_p+1\le x$. Hence $c_{p+1}=x$, $c_p=x-1$, and $p+1\ne j$ (as $c_j>x$), so $j\ge p+2$. Every index in $[p+1,j-1]$ has $c\ge x$ (maximality of $p$). Let $q$ be the least index $\ge p+2$ with $c_q\ne x$; it exists and $q\le j$ because $c_j\ne x$. If $q<j$ then $c_q\ge x$ (as $q\in[p+1,j-1]$), and if $q=j$ then $c_q>x$; with $c_q\ne x$ we get $c_q\ge x+1$. By 1.3, $c_q\le c_{q-1}+1=x+1$. So $c_q=x+1$, and $(p,q,x)$ is a pattern with $i\le p$, $q\le j$. $\square$

## §3. Triple lemma

**Lemma 3.** If $(p,p+2,x)$ is a pattern, i.e. $(c_p,c_{p+1},c_{p+2})=(x-1,x,x+1)$, then $p\le x$.

*Proof.* Suppose $p\ge x+1$. The $p-1$ c-columns $u=1,\dots,p-1$ are distinct columns; at most $c_p=x-1<p-1$ of them cover row $p$ (1.2a). So some c-column $i\le p-1$ does not cover row $p$. c-column $p-1$ covers row $p$ ($c_{p-1}\ge1$), so $i\le p-2$; take $i$ maximal, so c-column $i+1$ ($\le p-1$) covers row $p$. Since $c_{p+1}=c_p+1$ and $c_{p+2}=c_{p+1}+1$, $L_p=L_{p+1}=0$ (1.3), so by (1.3') c-column $i+1$ covers rows $p+1$ and $p+2$: $(i+1)+c_{i+1}\ge p+2$, i.e. $c_{i+1}\ge p-i+1$. c-column $i$ does not cover row $p>i$: $i+c_i\le p-1$, i.e. $c_i\le p-i-1$. Then $c_{i+1}\ge c_i+2$, contradicting 1.3. $\square$

## §4. Shortening lemma

**Lemma 4.** Let $(p,q,x)$ be a pattern with $q\ge p+3$ and $p\ge x+1$. Then there is a pattern $(p',q',x')$ with $x'\le x$, $2\le q'-p'\le q-p-1$ and $p'=p-x'\ge p-x$.

*Proof.* (i) The $x$ c-columns $u\in[p-x,p-1]$ exist ($p-x\ge1$). At most $c_p=x-1$ of them cover row $p$, so one does not; c-column $p-1$ does. Let $p'$ be the largest $u\in[p-x,p-2]$ such that c-column $u$ does not cover row $p$. Then c-columns $u\in[p'+1,p-1]$ cover row $p$.

(ii) $c_{p+1}=c_p+1$ gives $L_p=0$, so c-columns $u\in[p'+1,p-1]$ cover row $p+1$ (1.3'); c-column $p$ covers row $p+1$ too. From "c-column $p'+1$ covers row $p+1$": $c_{p'+1}\ge p-p'$. From "c-column $p'$ does not cover row $p$" (and $p'<p$): $c_{p'}\le p-p'-1$. By 1.3, $c_{p'+1}\le c_{p'}+1\le p-p'$. Put $y:=p-p'$; then $c_{p'}=y-1$, $c_{p'+1}=y$, and $2\le y\le x$.

(iii) Invariant $I(m)$ ($m\ge1$): $c_{p'+1}=\dots=c_{p'+m}=y$, and every c-column $u\in[p'+m,\,p+m-1]$ covers row $p+m$. By (ii), $I(1)$ holds. Under $I(m)$, c-column $p'+m$ has length $y$, so it covers exactly rows $p'+m+1,\dots,p'+m+y=p+m$: it ends at row $p+m$.

(iv) Step. Assume $I(m)$ and $p+m\le q-1$.
(a) If $p+m=q-1$: $c_q=c_{q-1}+1$ forces $L_{q-1}=0$, but c-column $p'+m$ ends at row $q-1$. Contradiction. So $p+m\le q-2$; then $p+m,\,p+m+1\in[p+1,q-1]$, so $c_{p+m+1}=c_{p+m}=x$ and $L_{p+m}=1$: c-column $p'+m$ is the only column ending at row $p+m$. By (1.3') the c-columns $u\in[p'+m+1,p+m-1]$ (which cover row $p+m$ by $I(m)$) cover row $p+m+1$, and so does c-column $p+m$. Hence every c-column $u\in[p'+m+1,p+m]$ covers row $p+m+1$.
(b) In particular c-column $p'+m+1$ covers row $p+m+1$: $c_{p'+m+1}\ge (p+m+1)-(p'+m+1)=y$; and $c_{p'+m+1}\le c_{p'+m}+1=y+1$ (1.3). If $c_{p'+m+1}=y+1$, stop and set $q':=p'+m+1$. Otherwise $c_{p'+m+1}=y$ and, with (a), $I(m+1)$ holds; moreover $p+m+1\le q-1$.

(v) Termination. $I(1)$ holds with $p+1\le q-1$. By (iv), as long as the process does not stop, $I(m)$ holds with $p+m\le q-2$, so $m\le q-p-2$; hence it stops at some $m\le q-p-2$ with $c_{p'+m+1}=y+1$. Then $(c_{p'},c_{p'+1},\dots,c_{p'+m},c_{p'+m+1})=(y-1,y,\dots,y,y+1)$: $(p',q',x')$ with $x'=y\le x$ is a pattern of length $q'-p'=m+1\in[2,q-p-1]$, and $p'=p-y=p-x'\ge p-x$. $\square$

## §5. Descent lemma

**Lemma 5.** Every pattern $(p,q,x)$ satisfies $p\le (q-p-1)\,x$.

*Proof.* Induction on $\ell=q-p\ge2$. $\ell=2$: Lemma 3 gives $p\le x=(\ell-1)x$. $\ell\ge3$: if $p\le x$ we are done since $x\le(\ell-1)x$. Otherwise Lemma 4 gives a pattern $(p',q',x')$ with $x'\le x$, $2\le \ell':=q'-p'\le\ell-1$, $p'\ge p-x$. By induction $p'\le(\ell'-1)x'\le(\ell-2)x$, so $p\le p'+x\le(\ell-1)x$. $\square$

## §6. Length lemma (new)

**Lemma 6.** Every pattern $(p,q,x)$ satisfies (i) $q-p\ne x$ and (ii) $q-p\le x+1$.

*Proof.* (i) c-column $p$ has length $c_p=x-1\ge1$, so it ends at row $p+x-1$. If $q=p+x$, it ends at row $q-1$, so $L_{q-1}\ge1$ and $c_q\le c_{q-1}=x$ by 1.3, contradicting $c_q=x+1$.

(ii) Suppose $q-p\ge x+2$. The $x$ c-columns $u\in[q-x,q-1]$ lie in $[p+1,q-1]$, so $c_u=x$ and they cover rows $u+1,\dots,u+x$, which contain $q$. As $c_q=x+1$, exactly one further column $Z$ covers row $q$. $Z$ is not a c-column $u\in[p+1,q-x-1]$ (such a column has $c_u=x$ and ends at row $u+x\le q-1$). So $Z$ is a $\lambda$-column or a c-column $u\le p$; in both cases $Z$ covers row $q-1$ as well (a $\lambda$-column covers $[1,\lambda_j]\ni q-1$; a c-column $u\le p$ covering row $q$ covers $[u+1,q]\ni q-1$ since $u+1\le p+1\le q-1$). The $x$ c-columns $u\in[q-1-x,q-2]$ lie in $[p+1,q-1]$ (because $q-1-x\ge p+1$), have $c_u=x$, and cover row $q-1$. Together with $Z$ (which is not in $[p+1,q-1]$) these are $x+1$ distinct columns covering row $q-1$, so $c_{q-1}\ge x+1$ by (1.2a). But $c_{q-1}=x$. Contradiction. $\square$

## §7. Long-pattern lemma

**Lemma 7.** If $(p,q,x)$ is a pattern of length $q-p=x+1$, then, with $m:=x+1\ (\ge3)$, $\ q=p+m\le T_{m-1}+2$.

*Proof.* The pattern is $(c_p,\dots,c_{p+m})=(m-2,m-1,\dots,m-1,m)$. c-column $p$ covers rows $p+1,\dots,p+m-2$, not row $p+m$. For $u\in[p+1,p+m-1]$, $c_u=m-1$ and c-column $u$ covers rows $u+1,\dots,u+m-1$, which contain $p+m$. These are $m-1$ columns and $c_{p+m}=m$, so exactly one further column $Z$ covers row $p+m$; $Z$ is a $\lambda$-column or a c-column $u_0\le p-1$.

*Claim: if $Z$ is a c-column $u_0$, then $u_0=1$.* Suppose $u_0\ge2$. The columns covering row $p+m$ are $[p+1,p+m-1]$ and $u_0$, so c-column $u_0-1$ ($\le p-2$) does not cover row $p+m$. Since $c_{p+m}=c_{p+m-1}+1$, $L_{p+m-1}=0$, so c-column $u_0-1$ does not cover row $p+m-1$ either (if it did, it would end there). Since $p+m-2\ge p+1$ (as $m\ge3$), $c_{p+m-1}=c_{p+m-2}=m-1$, so $L_{p+m-2}=1$, and the one column ending at row $p+m-2$ is c-column $p$. c-column $u_0-1\ne p$ does not cover row $p+m-1$; if it covered row $p+m-2$ it would end there; so it does not cover row $p+m-2$. As $u_0-1<p+m-2$, this means $(u_0-1)+c_{u_0-1}\le p+m-3$. And c-column $u_0$ covers row $p+m$: $u_0+c_{u_0}\ge p+m$. So $c_{u_0}\ge c_{u_0-1}+2$, contradicting 1.3. This proves the claim.

*Sum.* By (1.2b) the remaining lengths at row $p+m$ sum to $n$. c-column $u\in[p+1,p+m-1]$ has remaining length $u+(m-1)-(p+m)+1=u-p$, and these sum to $1+2+\dots+(m-1)=T_{m-1}$. So $Z$ has remaining length $n-T_{m-1}$ at row $p+m$.
- If $Z$ is $\lambda$-column $j$: $\lambda_j-(p+m)+1=n-T_{m-1}$, so $p+m=\lambda_j+1-n+T_{m-1}\le T_{m-1}+1$ (as $\lambda_j\le n$).
- If $Z$ is c-column $1$: $1+c_1-(p+m)+1=n-T_{m-1}$, so $p+m=c_1+2-n+T_{m-1}\le T_{m-1}+2$ (as $c_1=s\le n$). $\square$

## §8. The cycle (non-triangular $n$; uses B-C1)

From now on $k\ge4$, $n=T_{k-1}+r$ with $1\le r\le k-1$; these are exactly the $n$ with $T_{k-1}<n<T_k$ (since $T_k=T_{k-1}+k$).

For $e=(e_1,\dots,e_k)\in\{0,1\}^k$ with $\sum e_j=r$ put $a_j(e)=k-j+e_j$ ($1\le j\le k$) and let $\lambda(e)$ be the partition whose parts are the positive numbers among $a_1(e),\dots,a_k(e)$. (Here $a_j(e)\ge1$ for $j\le k-1$, $a_k(e)=e_k$, $a_j(e)-a_{j+1}(e)=1+e_j-e_{j+1}\ge0$, and $\sum_j a_j(e)=T_{k-1}+r=n$; $\lambda(e)$ has $k-1+e_k$ parts.) This is the partition $(k-1+e_1,\dots,1+e_{k-1},e_k)$ of B-C1. Let $\rho e:=(e_k,e_1,\dots,e_{k-1})$, i.e. $(\rho e)_1=e_k$, $(\rho e)_j=e_{j-1}$ for $2\le j\le k$.

**8.1 Lemma.** $B(\lambda(e))=\lambda(\rho e)$.

*Proof.* $\lambda(e)$ has $k-1+e_k$ parts, so by definition $B(\lambda(e))$ has the part $k-1+e_k=a_1(\rho e)$ and the positive numbers among $a_j(e)-1$, $1\le j\le k$. For $1\le j\le k-1$: $a_j(e)-1=k-(j+1)+e_j=a_{j+1}(\rho e)$. For $j=k$: $a_k(e)-1=e_k-1\le0$, not positive. So the parts of $B(\lambda(e))$ are the positive numbers among $a_1(\rho e),\dots,a_k(\rho e)$, i.e. $B(\lambda(e))=\lambda(\rho e)$ (and $\sum\rho e=r$). $\square$

**8.2 Lemma (cycle).** Let $t=d_B(\lambda)$. Row $t+1=B^t(\lambda)$ is cyclic, so by B-C1 it equals $\lambda(e)$ for some $e$ with $\sum e_j=r$. Then (a) $c_u\in\{k-1,k\}$ for all $u\ge t+1$; (b) $c_{t+i}=k-1+e_{k+1-i}$ for $1\le i\le k$; (c) exactly $r$ of $c_{t+1},\dots,c_{t+k}$ equal $k$, the others equal $k-1$.

*Proof.* By 8.1 and induction on $m\ge0$, row $t+1+m=\lambda(\rho^m e)$, which has $k-1+(\rho^m e)_k\in\{k-1,k\}$ parts: (a). By induction on $m$, $(\rho^m e)_j=e_{j-m}$ for $m<j\le k$ ($m=0$ trivial; $(\rho^{m+1}e)_j=(\rho^m e)_{j-1}=e_{j-1-m}$ for $m+1<j\le k$, using $j\ge2$). With $j=k$ and $m=i-1\le k-1$: $c_{t+i}=k-1+e_{k+1-i}$: (b). As $i$ runs over $1..k$, $k+1-i$ runs over $1..k$, and $\sum e_j=r$: (c). $\square$

## §9. End lemma (new)

**Lemma 9.** Let $t=d_B(\lambda)\ge1$, $\mu:=$ row $t=B^{t-1}(\lambda)$, $\nu:=$ row $t+1=\lambda(e)$ (8.2). Then $c_t\in\{k-2,k-1\}$. If $c_t=k-1$, then $e_1=e_2=1$, $c_{t+k-1}=c_{t+k}=k$, and $\mu$ has exactly one part equal to $k+1$ while all its other parts are $\le k-1$.

*Proof.* $\mu$ is not cyclic, by minimality of $t$. Write $c=c_t$ (the number of parts of $\mu$), $a_j=a_j(e)$, $s_\nu=k-1+e_k$ (the number of parts of $\nu$). By definition of $B$, the multiset of parts of $\nu$ is $\{c\}\uplus\{\mu_j-1:\mu_j\ge2\}$. Hence: (i) $c$ is a part of $\nu$; (ii) the parts $\ge2$ of $\mu$ are the numbers $\pi+1$, $\pi$ running over the parts of $\nu$ with one copy of $c$ removed; (iii) $\mu$ has $c-(s_\nu-1)\ge0$ parts equal to $1$. So $\mu$ is determined by $\nu$ and the value $c$, and $c\ge s_\nu-1=k-2+e_k$.

*Step 1: $c\in\{a_1,a_2,a_3\}$ (as values).* The parts of $\nu$ are $a_1\ge\dots\ge a_{k-1}\ge1$ and, if $e_k=1$, $a_k=1$. For $4\le j\le k-1$: $a_j\le k-j+1\le k-3<k-2\le c$. If $e_k=1$: $a_k=1<k-1=s_\nu-1\le c$ (as $k\ge3$). Since $k\ge4$, the indices $1,2,3$ are $\le k-1$. So $c$ equals $a_1$, $a_2$ or $a_3$.

*Step 2: $c\ne a_1$.* Suppose $c=a_1=k-1+e_1$. By (ii), the parts $\ge2$ of $\mu$ are $a_j+1=k-j+1+e_j$ ($2\le j\le k-1$) and, if $e_k=1$, $a_k+1=2$; by (iii) $\mu$ has $(k-1+e_1)-(k-2+e_k)=1+e_1-e_k$ parts equal to 1. Let $e'=(e_2,\dots,e_k,e_1)$, $\sum e'_j=r$. Then $a_j(e')=k-j+e_{j+1}=a_{j+1}+1$ for $1\le j\le k-2$, $a_{k-1}(e')=1+e_k$, $a_k(e')=e_1$. If $e_k=1$ the last two are $2$ and $e_1$, and $\mu$ has the part $2$ and $e_1$ parts $1$; if $e_k=0$ they are $1$ and $e_1$, and $\mu$ has $1+e_1$ parts $1$. In both cases $\mu=\lambda(e')$, which is cyclic by B-C1. Contradiction.

*Step 3.* So $c\in\{a_2,a_3\}$ and $c\ne a_1$ as values. Now $a_2=k-2+e_2\le k-1$ and $a_3=k-3+e_3\le k-2$; with $c\ge k-2$ this gives $c\in\{k-2,k-1\}$. If $c=k-1$: $c\ne a_3$, so $c=a_2$ and $e_2=1$; $c\ne a_1$ gives $a_1\ne k-1$, so $e_1=1$. Then 8.2(b) with $i=k$ and $i=k-1$ gives $c_{t+k}=k-1+e_1=k$, $c_{t+k-1}=k-1+e_2=k$. The parts of $\nu$ are $a_1=k$, $a_2=k-1$, and $a_j\le k-j+1\le k-2$ for $j\ge3$ (including $a_k=1$ if present); so $c=k-1$ occurs only once among them, as $a_2$. By (ii) the parts $\ge2$ of $\mu$ are $a_1+1=k+1$ and $a_j+1\le k-1$ ($j\ge3$); the other parts of $\mu$ equal $1\le k-1$. $\square$

## §10. Case $c_t=k-2$

**Lemma 10.** If $t=d_B(\lambda)\ge1$ and $c_t=k-2$, then $t\le k^2-2k-1$.

*Proof.* By 1.3 and 8.2(a), $k-1\le c_{t+1}\le c_t+1=k-1$, so $c_{t+1}=k-1$. By 8.2(c) (with $r\ge1$) some $j\in[t+1,t+k]$ has $c_j=k$, and $j\ne t+1$. Lemma 2 with $i=t$, $x=k-1$ ($c_t=k-2<k-1<k=c_j$) gives a pattern $(p,q,k-1)$ with $t\le p$. Since $c_p=k-2$ and $c_u\ge k-1$ for $u\ge t+1$ (8.2(a)), $p=t$. Let $\ell=q-t$. By Lemma 6, $\ell\ne k-1$ and $\ell\le k$; so $2\le\ell\le k-2$ or $\ell=k$.
- $\ell\le k-2$: Lemma 5 gives $t=p\le(\ell-1)(k-1)\le(k-3)(k-1)=k^2-2k-1-(2k-4)\le k^2-2k-1$.
- $\ell=k=x+1$: Lemma 7 (with $m=k$) gives $t+k\le T_{k-1}+2$, so $t\le T_{k-1}+2-k\le T_{k-1}+1\le k^2-2k-1$, the last step because $k^2-2k-1-(T_{k-1}+1)=\tfrac{(k-4)(k+1)}{2}\ge0$. $\square$

## §11. Case $c_t=k-1$

**Lemma 11.** If $t=d_B(\lambda)\ge1$ and $c_t=k-1$, then $t\le k^2-2k-1$.

*Proof.* If $t\le k$, then $t\le k\le k^2-2k-1$ since $k^2-3k-1=k(k-3)-1\ge3$. Assume $t\ge k+1$; then $t-k\ge1$. By Lemma 9, row $t$ ($=\mu$) has exactly $c_t=k-1$ parts, exactly one equal to $k+1$, all others $\le k-1$, and $c_{t+k-1}=k$. By (1.2b), exactly one column covering row $t$ — call it $Z$ — has remaining length $k+1$ at row $t$, and every other column covering row $t$ has remaining length $\le k-1$ there. c-column $t-1$ always covers row $t$ (as $c_{t-1}\ge1$); its remaining length at row $t$ is $c_{t-1}$.

**Case A: every c-column $u\in[t-k+1,t-1]$ covers row $t$.** These are $k-1$ distinct columns and $c_t=k-1$, so by (1.2a) they are *all* the columns covering row $t$. Consequences: $Z$ is a c-column $u_0\in[t-k+1,t-1]$ with $u_0+c_{u_0}-t+1=k+1$, i.e. $c_{u_0}=t+k-u_0$; and c-column $t-k$ does not cover row $t$, i.e. $(t-k)+c_{t-k}\le t-1$, i.e. $c_{t-k}\le k-1$.

*A1: $u_0=t-1$*, i.e. $c_{t-1}=k+1$. Suppose $c_u\ge k$ for all $u\in[t-k+1,t-2]$. For $u=t-a$ ($2\le a\le k-1$) the remaining length at row $t$ is $u+c_u-t+1=c_u-a+1\ge k+1-a$. By (1.2b),
$$n\ \ge\ (k+1)+\sum_{a=2}^{k-1}(k+1-a)=(k+1)+(2+3+\dots+(k-1))=(k+1)+T_{k-1}-1=T_k ,$$
contradicting $n\le T_k-1$. So some $i\in[t-k+1,t-2]$ has $c_i\le k-1$. Lemma 2 with $x=k$ on $[i,t-1]$ ($c_i\le k-1<k<k+1=c_{t-1}$) gives a pattern $(p,q,k)$ with $t-k+1\le i\le p$ and $q\le t-1$; its length is $\ell=q-p\le k-2$. Lemma 5: $p\le(\ell-1)k\le(k-3)k$. Hence $t\le p+k-1\le(k-3)k+k-1=k^2-2k-1$.

*A2: $u_0\le t-2$.* Put $b=t-u_0\ge2$, so $c_{u_0}=k+b$. If $u_0=t-k+1$, then 1.3 gives $c_{u_0}\le c_{t-k}+1\le k$, contradicting $c_{u_0}=k+b\ge k+2$. So $u_0\ge t-k+2$, i.e. $u_0-1\in[t-k+1,t-3]$, and c-column $u_0-1$ covers row $t$ (Case A) with remaining length $(u_0-1)+c_{u_0-1}-t+1=c_{u_0-1}-b$. By 1.3, $c_{u_0-1}\ge c_{u_0}-1=k+b-1$, so this remaining length is $\ge k-1$; since c-column $u_0-1\ne Z$, it is $\le k-1$. Hence $c_{u_0-1}=k+b-1\ge k+1$. Lemma 2 with $x=k$ on $[t-k,u_0-1]$ ($t-k<u_0-1$; $c_{t-k}\le k-1<k<k+1\le c_{u_0-1}$) gives a pattern $(p,q,k)$ with $t-k\le p$, $q\le u_0-1\le t-3$, so $2\le\ell=q-p\le k-3$. For $k=4$ this is impossible, so A2 does not occur. For $k\ge5$, Lemma 5 gives $p\le(k-4)k$, and $t\le p+k\le k^2-3k\le k^2-2k-1$.

**Case B: some c-column $i\in[t-k+1,t-2]$ does not cover row $t$** (Cases A and B are exhaustive, as c-column $t-1$ covers row $t$). Then $i+c_i\le t-1$, so $c_i\le t-1-i\le k-2$. Since $c_{t+k-1}=k$ (Lemma 9) and $i<t+k-1$, Lemma 2 with $x=k-1$ on $[i,t+k-1]$ gives a pattern $(p,q,k-1)$ with $i\le p$, $q\le t+k-1$. As $c_p=k-2$, while $c_t=k-1$ and $c_u\in\{k-1,k\}$ for $u\ge t+1$ (8.2(a)), $p\le t-1$. So $t-k+1\le p\le t-1$. Let $\ell=q-p$; by Lemma 6, $2\le\ell\le k-2$ or $\ell=k$.
- $\ell\le k-2$: Lemma 5 gives $p\le(k-3)(k-1)$, so $t\le p+k-1\le(k-2)(k-1)=k^2-2k-1-(k-3)\le k^2-2k-1$.
- $\ell=k$: $q=p+k\ge t+1$, so $t\le q-1$; Lemma 7 ($m=k$) gives $q\le T_{k-1}+2$; so $t\le T_{k-1}+1\le k^2-2k-1$ (as in §10). $\square$

## §12. Conclusion

**Theorem.** For every $k\ge4$, every $n$ with $T_{k-1}<n<T_k$ and every $\lambda\vdash n$: $d_B(\lambda)\le k^2-2k-1$.

*Proof.* Let $t=d_B(\lambda)$. If $t=0$ there is nothing to prove. If $t\ge1$, Lemma 9 gives $c_t\in\{k-2,k-1\}$, and Lemma 10, resp. Lemma 11, gives $t\le k^2-2k-1$. $\square$

**Corollary (b-upper).** For $k\ge4$, $n=T_k-1=T_{k-1}+(k-1)$ satisfies $T_{k-1}<n<T_k$, so $D_B(T_k-1)=\max_{\lambda\vdash n}d_B(\lambda)\le k^2-2k-1$. With the already-proved lower bound (TARGET; subject Prop. 7.2: $d_B((k-1,k-2,k-2,k-3,\dots,2,1,1))=k^2-2k-1$), $D_B(T_k-1)=k^2-2k-1$ for all $k\ge4$. Taking the maximum over $\lambda$ in the Theorem gives also $D_B(n)\le k^2-2k-1$ for every non-triangular $n$ of rank $k\ge4$ (Cell 3(a) as worded in the statement).

## §13. What is established

- PROVED here, for all $k\ge4$ (written proof, no computation used): target (a) for every partition of every non-triangular $n$ of rank $k$; hence $D_B(T_k-1)\le k^2-2k-1$.
- Used without proof: only B-C1 (gated), in §8.2 (row $t+1$ has the form $\lambda(e)$) and §9 Step 2 ($\lambda(e')$ is cyclic).
- Not addressed here: Cell 3(c) (the extremal partitions of $T_k-1$); the lower bound of (b) is quoted from the subject, not re-proved.
- Sanity check only (proves nothing beyond its range): `out/code/check_c3a.py 9` verifies Lemmas 3/5/6/7 on every pattern of every partition of $n\le44$, and Lemma 9 and the case certificates of §10–§11 for every partition of every non-triangular $n$ of rank $4\le k\le9$; all pass.
