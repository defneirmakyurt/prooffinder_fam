Proved here (and nothing more), for every $k\ge4$, $n=T_k-1$, $M=M_k=k^2-2k-1$, $\nu_k=(k+1,k-1,k-2,\dots,3,1)$, $E_k=\{\lambda\vdash n: d_B(\lambda)=M\}$, $R_k=\{\lambda\vdash n: B^{M-1}(\lambda)=\nu_k\}$: (P1) $R_k\subseteq E_k$, with no hypothesis; (P2) the explicit partitions $\lambda^*_k$ (all $k\ge4$) and $\alpha_k,\beta_k$ ($k\ge5$) of Step 4 lie in $R_k\subseteq E_k$; (P3) the set $D_1=\{\mu\vdash n: d_B(\mu)=1\}$ is the explicit list of $k-1$ partitions in Step 3, and $E_k=\{\lambda\vdash n: B^{M-1}(\lambda)\in D_1\}$, with no hypothesis; (P4) under (H), every $\lambda\in E_k$ is a Garden of Eden ($\lambda_1\le\ell(\lambda)-2$) and $E_k=\{\lambda\vdash n: B^{M-1}(\lambda)\text{ is not cyclic}\}$.

**Not proved ([GAP]):** target item 3 in the form $E_k\subseteq R_k$ (equivalently: no $\mu\in D_1\setminus\{\nu_k\}$ has a preimage chain of length $M-1$) for $k\ge12$; and target item 1, a closed-form description of $E_k$ as a function of $k$. What is available instead: (P2) gives three explicit members for every $k\ge5$; $R_k$ is listed explicitly by a finite, provably correct computation for any single $k$ (`out/code/print_R.py`); and $E_k=R_k$ is CHECKED unconditionally (exact exhaustive enumeration of all partitions, no use of (H)) for $4\le k\le 11$, with $|E_k|=1,6,34,175,831,3911,18163,84654$.

Reading of the target: exactly as stated in TARGET. (H) is used only in Step 5, where every use is marked **[uses (H)]**.

Source of reused material: Step 4.2 reuses Proposition 7.2 of the subject proof B-C3-004 (`inbox/subject/proof.md`, Step 7), which in turn rests on its Steps 1–4; nothing else from the subject is used.

---

## Step 1 (cyclic partitions of $n=T_k-1$ and the function $d_B$), $k\ge4$

1.1. Since $T_k-T_{k-1}=k\ge2$, we have $T_{k-1}<T_k-1<T_k$, so $n=T_k-1$ has rank $k$ and $n=T_{k-1}+r$ with $r=k-1$. By Cell 1 (ASSUMPTIONS), $\lambda\vdash n$ is cyclic iff $\lambda=(k-1+e_1,\dots,1+e_{k-1},e_k)$ (zero entries dropped) with $e\in\{0,1\}^k$ and $\sum_i e_i=k-1$. Such an $e$ has exactly one index $j\in\{1,\dots,k\}$ with $e_j=0$. Write $c_j$ for the corresponding partition: its row $i$ ($1\le i\le k$) has length $k+1-i$ for $i\ne j$ and $k-j$ for $i=j$. So $c_j$ is $\delta_k$ with the last cell of row $j$ removed, and the cyclic partitions of $n$ are exactly $c_1,\dots,c_k$.

1.2. Every cyclic partition of $n$ has first part $k-1+e_1\le k$. Hence **a partition of $n$ whose first part is at least $k+1$ is not cyclic.**

1.3. If $\mu$ is cyclic, say $B^i(\mu)=\mu$ with $i\ge1$, then $B^i(B(\mu))=B(B^i(\mu))=B(\mu)$, so $B(\mu)$ is cyclic. By induction, $B^j(\mu)$ is cyclic for every $j\ge0$.

1.4. For every $\lambda\vdash n$ and $t\ge0$: $d_B(\lambda)\le t\iff B^t(\lambda)$ is cyclic. ($\Leftarrow$: $d_B$ is a minimum over such $t$. $\Rightarrow$: apply 1.3 to $\mu=B^{d_B(\lambda)}(\lambda)$ and $j=t-d_B(\lambda)$.)

1.5. For every $\lambda\vdash n$: $d_B(B(\lambda))=\max(d_B(\lambda)-1,0)$.
*Proof.* For $t\ge0$, by 1.4 twice: $d_B(B(\lambda))\le t\iff B^{t+1}(\lambda)$ cyclic $\iff d_B(\lambda)\le t+1\iff d_B(\lambda)-1\le t$. Hence $d_B(B(\lambda))$ is the least $t\ge0$ with $t\ge d_B(\lambda)-1$, i.e. $\max(d_B(\lambda)-1,0)$. $\square$

1.6. By induction on $j$ from 1.5: $d_B(B^j(\lambda))=\max(d_B(\lambda)-j,0)$ for all $j\ge0$. In particular, for $j\ge0$ and $m\ge1$: $d_B(B^j(\lambda))=m\iff d_B(\lambda)=m+j$.

## Step 2 (preimages under $B$)

2.1. **Lemma (preimage rule).** Let $\mu\vdash n$ have $\ell=\ell(\mu)$ parts. For a value $s$ occurring as a part of $\mu$ with $s\ge\ell-1$, let $\pi_s(\mu)$ be the partition whose parts are: $x+1$ for each part $x$ of $\mu$ other than one copy of $s$ (that is $\ell-1$ parts), together with $s-(\ell-1)$ parts equal to $1$. Then
$$B^{-1}(\mu)=\{\pi_s(\mu):\ s\text{ a part value of }\mu,\ s\ge\ell-1\},$$
and distinct values $s$ give distinct preimages.

*Proof.* ($\supseteq$) $\pi_s(\mu)$ has $(\ell-1)+(s-\ell+1)=s$ parts and total $(n-s)+(\ell-1)+(s-\ell+1)=n$. Apply the definition of $B$: the new part is the number of parts, $s$; the parts equal to $1$ become $0$ and are discarded; the parts $x+1$ (all $\ge2$) become $x$. So $B(\pi_s(\mu))$ has parts $s$ and the parts of $\mu$ other than one copy of $s$, i.e. $B(\pi_s(\mu))=\mu$.
($\subseteq$) Let $B(\lambda)=\mu$, where $\lambda$ has $s$ parts, $a$ of which equal $1$. By definition the parts of $\mu$ are $s$ together with $\lambda_i-1$ for the $s-a$ parts $\lambda_i\ge2$. So $s$ is a part value of $\mu$, $\ell=1+(s-a)$, i.e. $a=s-(\ell-1)\ge0$, so $s\ge\ell-1$; and the parts $\ge2$ of $\lambda$ are exactly $x+1$ for the parts $x$ of $\mu$ other than one copy of $s$. Hence $\lambda=\pi_s(\mu)$.
(Distinctness) $\pi_s(\mu)$ has exactly $s$ parts. $\square$

2.2. **Corollary (Garden of Eden).** $\mu$ has no preimage under $B$ iff no part value $s$ of $\mu$ satisfies $s\ge\ell(\mu)-1$, iff $\mu_1\le\ell(\mu)-2$.

## Step 3 (the partitions with $d_B=1$), $k\ge4$

3.1. By 1.4, $d_B(\mu)=1$ iff $\mu$ is not cyclic and $B(\mu)$ is cyclic. So $D_1:=\{\mu\vdash n:d_B(\mu)=1\}$ is the set of non-cyclic elements of $\bigcup_{j=1}^kB^{-1}(c_j)$, which we compute with Lemma 2.1, using the row description of $c_j$ from 1.1.

3.2. *$j=1$.* Rows: $k-1$ (row 1), then $k-1,k-2,\dots,1$ (rows $2,\dots,k$). So $\ell(c_1)=k$ and the only part value $\ge k-1$ is $k-1$. $\pi_{k-1}(c_1)$: the other parts $k-1,\dots,1$ become $k,\dots,2$; $0$ ones are added. So $B^{-1}(c_1)=\{(k,k-1,\dots,2)\}=\{c_k\}$, cyclic. Contribution to $D_1$: none.

3.3. *$j=2$.* Rows: $k$, $k-2$, $k-2$, $k-3,\dots,1$. $\ell=k$; the only part value $\ge k-1$ is $k$. $\pi_k(c_2)$: the parts $k-2,k-2,k-3,\dots,1$ become $k-1,k-1,k-2,\dots,2$, and $k-(k-1)=1$ one is added: $(k-1,k-1,k-2,\dots,2,1)=c_1$, cyclic. Contribution: none.

3.4. *$3\le j\le k-1$* (this range is nonempty since $k\ge4$). Rows: $k+1-i$ for $i\ne j$, and $k-j$ in row $j$; row $k$ has length $1$ (as $j\ne k$), so $\ell=k$. Part values $\ge k-1$: $k$ (row 1) and $k-1$ (row 2, since $j\ne2$); no others.
- $\pi_k(c_j)$: the remaining parts are $k+1-i$ ($2\le i\le k$, $i\ne j$) and $k-j$; adding $1$ gives $k+2-i$ ($2\le i\le k$, $i\ne j$) and $k+1-j$; one part $1$ is added. The multiset $\{k+2-i:2\le i\le k\}\cup\{1\}$ is $\{k,k-1,\dots,1\}$, the rows of $\delta_k$ (value $k+2-i$ is row $i-1$); here the value $k+2-j$ is replaced by $k+1-j$, which is $\delta_k$ with row $j-1$ shortened by one: $c_{j-1}$, cyclic.
- $\pi_{k-1}(c_j)$: the remaining parts are $k$, $k+1-i$ ($3\le i\le k$, $i\ne j$) and $k-j$; adding $1$: $k+1$, $k+2-i$ ($3\le i\le k$, $i\ne j$), $k+1-j$; and $(k-1)-(k-1)=0$ ones are added. Since $\{k+2-i:3\le i\le k\}=\{k-1,\dots,2\}$, this is
$$\mu^{(v)}:=(k+1)\ \cup\ \bigl(\{k-1,k-2,\dots,2\}\text{ with the single value }v\text{ replaced by }v-1\bigr),\qquad v=k+2-j\in\{3,\dots,k-1\}.$$
Its first part is $k+1$, so it is not cyclic (1.2).

3.5. *$j=k$.* $c_k=(k,k-1,\dots,2)$, $\ell=k-1$; part values $\ge k-2$: $k$, $k-1$, $k-2$ (all present because $k-2\ge2$).
- $\pi_k(c_k)$: $k-1,\dots,2$ become $k,\dots,3$, plus $k-(k-2)=2$ ones: $(k,k-1,\dots,3,1,1)$, which is $\delta_k$ with row $k-1$ shortened: $c_{k-1}$, cyclic.
- $\pi_{k-1}(c_k)$: $k,k-2,\dots,2$ become $k+1,k-1,\dots,3$, plus $1$ one: $(k+1,k-1,\dots,3,1)=\nu_k=\mu^{(2)}$ (the formula of 3.4 with $v=2$). Not cyclic (1.2).
- $\pi_{k-2}(c_k)$: $k,k-1,k-3,\dots,2$ become $k+1,k,k-2,\dots,3$, plus $0$ ones: $\omega_k:=(k+1,k,k-2,k-3,\dots,3)$ (for $k=4$: $\omega_4=(5,4)$). Not cyclic (1.2).

3.6. **Proposition.** For $k\ge4$,
$$D_1=\{\mu^{(v)}:2\le v\le k-1\}\cup\{\omega_k\},\qquad |D_1|=k-1,$$
where $\mu^{(v)}=(k+1)\cup(\{k-1,\dots,2\}$ with $v$ lowered to $v-1)$ and $\mu^{(2)}=\nu_k$. (For $k=4$: $D_1=\{(5,3,1),(5,2,2),(5,4)\}$.)
*Proof.* 3.1–3.5 list all preimages of all $c_j$ and discard the cyclic ones. The $k-1$ listed partitions are pairwise distinct: $\omega_k$ is the only one whose second part is $k$ (for $\mu^{(v)}$ the second part is $k-1$ if $v\ne k-1$ and $k-2$ if $v=k-1$), and $\mu^{(v)}\ne\mu^{(v')}$ for $v\ne v'$ because $v$ is the unique value in $\{2,\dots,k-1\}$ missing from the parts of $\mu^{(v)}$ after its first. $\square$

3.7. In particular $d_B(\nu_k)=1$, $B(\nu_k)=c_k=(k,k-1,\dots,2)$.

## Step 4 (target item 2 for $R_k$, and explicit members), $k\ge4$

4.1. **Proposition (no hypothesis).** If $\lambda\vdash n$ and $B^{M-1}(\lambda)=\nu_k$, then $d_B(\lambda)=M$. More generally, $d_B(\lambda)=M\iff B^{M-1}(\lambda)\in D_1$.
*Proof.* By 1.6 with $j=M-1\ge0$ and $m=1$: $d_B(B^{M-1}(\lambda))=1\iff d_B(\lambda)=M$. Since $\nu_k\in D_1$ (3.6), the first claim follows. $\square$
Hence $R_k\subseteq E_k$ and
$$E_k=\bigsqcup_{\mu\in D_1}B^{-(M-1)}(\mu),\qquad B^{-(M-1)}(\mu):=\{\lambda\vdash n:B^{M-1}(\lambda)=\mu\},$$
a disjoint union (a partition has one image under $B^{M-1}$). Each set $B^{-(M-1)}(\mu)$ is obtained by applying Lemma 2.1 $M-1$ times.

4.2. **$\lambda^*_k\in R_k$.** Let $\lambda^*_k=(k-1,k-2,k-2,k-3,\dots,2,1,1)$: row 1 is $k-1$, row 2 is $k-2$, row $i$ is $k+1-i$ for $3\le i\le k$, row $k+1$ is $1$; $|\lambda^*_k|=T_{k-1}+(k-2)+1=T_k-1$. By Proposition 7.2 of the subject proof (B-C3-004, `inbox/subject/proof.md`, Step 7, proved there for all $k\ge3$), $B^{k^2-2k-2}(\lambda^*_k)=\nu_k$, i.e. $\lambda^*_k\in R_k$. (Cross-check, not load-bearing: `out/code/check_families.py` iterates $B$ for $4\le k\le60$.)

4.3. **Two more explicit members for $k\ge5$.** For $k\ge5$ the last four parts of $\lambda^*_k$ are $3,2,1,1$ (rows $k-2,\dots,k+1$; row $k-2$ equals $k+1-(k-2)=3$ because $k-2\ge3$). Let $H_k$ be $\lambda^*_k$ with these four parts removed: its rows are row 1 $=k-1$, row 2 $=k-2$, and row $i=k+1-i$ for $3\le i\le k-3$ (so $H_5=(4,3)$, $H_6=(5,4,4)$, $H_7=(6,5,5,4)$). It has $k-3$ parts, all $\ge3$ (the last one is $3$ if $k=5$ and $4$ if $k\ge6$). Define
$$\alpha_k=H_k\cup(2,2,1,1,1),\qquad \beta_k=H_k\cup(2,2,2,1).$$
Both are partitions (all parts of $H_k$ are $\ge3>2$) of $|H_k|+7=|\lambda^*_k|=n$. For a multiset $X$ of integers write $X-c$ for $\{x-c:x\in X\}$ and $(X)^+$ for its positive elements. Since all elements of $H_k$ are $\ge3$, $H_k-1$ and $H_k-2$ consist of positive numbers.
- $\lambda^*_k=H_k\cup(3,2,1,1)$ has $k+1$ parts. $B(\lambda^*_k)=(H_k-1)\cup(2,1)\cup\{k+1\}$, with $k$ parts. $B^2(\lambda^*_k)=\{k\}\cup(H_k-2)\cup\{1\}\cup\{k\}$ (the part $1$ became $0$), with $k$ parts. $B^3(\lambda^*_k)=\{k-1,k-1\}\cup(H_k-3)^+\cup\{k\}$.
- $\alpha_k$ has $k+2$ parts. $B(\alpha_k)=(H_k-1)\cup(1,1)\cup\{k+2\}$, with $k$ parts. $B^2(\alpha_k)=\{k+1\}\cup(H_k-2)\cup\{k\}$ (both $1$'s became $0$), with $k-1$ parts. $B^3(\alpha_k)=\{k,k-1\}\cup(H_k-3)^+\cup\{k-1\}$.
- $\beta_k$ has $k+1$ parts. $B(\beta_k)=(H_k-1)\cup(1,1,1)\cup\{k+1\}$, with $k+1$ parts. $B^2(\beta_k)=\{k\}\cup(H_k-2)\cup\{k+1\}=B^2(\alpha_k)$.
Hence $B^3(\alpha_k)=B^3(\beta_k)=\{k,k-1,k-1\}\cup(H_k-3)^+=B^3(\lambda^*_k)$. Since $M-1=k^2-2k-2\ge3$, $B^{M-1}(\alpha_k)=B^{M-4}(B^3(\lambda^*_k))=B^{M-1}(\lambda^*_k)=\nu_k$, and likewise for $\beta_k$. So $\alpha_k,\beta_k\in R_k\subseteq E_k$ (4.1, 4.2). The three partitions $\lambda^*_k,\alpha_k,\beta_k$ are distinct ($\alpha_k$ has $k+2$ parts, the others $k+1$; $\beta_k$ has no part equal to $3$ among its last four parts, $\lambda^*_k$ does). Examples: $k=5$: $(4,3,2,2,1,1,1)$, $(4,3,2,2,2,1)$; $k=6$: $(5,4,4,2,2,1,1,1)$, $(5,4,4,2,2,2,1)$.

4.4. **Corollary.** $|E_k|\ge1$ for $k\ge4$ and $|E_k|\ge3$ for $k\ge5$; in particular $D_B(T_k-1)\ge M$.

## Step 5 (consequences of (H)), $k\ge4$

5.1. **[uses (H)]** $E_k=\{\lambda\vdash n:d_B(\lambda)\ge M\}=\{\lambda\vdash n:B^{M-1}(\lambda)\text{ is not cyclic}\}$.
*Proof.* By (H), $d_B(\lambda)\ge M\iff d_B(\lambda)=M$. By 1.4 with $t=M-1$, $d_B(\lambda)\ge M\iff B^{M-1}(\lambda)$ is not cyclic. $\square$

5.2. **[uses (H)]** Every $\lambda\in E_k$ is a Garden of Eden: $\lambda_1\le\ell(\lambda)-2$.
*Proof.* Suppose $\lambda=B(\kappa)$ for some $\kappa\vdash n$. By 1.5, $M=d_B(\lambda)=\max(d_B(\kappa)-1,0)$; as $M\ge7>0$, $d_B(\kappa)=M+1$, contradicting (H). So $\lambda$ has no preimage, and Corollary 2.2 gives $\lambda_1\le\ell(\lambda)-2$. $\square$

5.3. **[uses (H)]** For every $\mu\in D_1$ the preimage tree of $\mu$ has height at most $M-1$, i.e. $B^{-M}(\mu)=\emptyset$.
*Proof.* A $\kappa$ with $B^M(\kappa)=\mu$ would have $d_B(\kappa)=M+1$ by 1.6 ($m=1$, $j=M$), contradicting (H). $\square$

## Step 6 (target item 3) — [GAP] for $k\ge12$

6.1. By 4.1 (no hypothesis), target item 3 in the form "$E_k=R_k$" is equivalent to
$$\text{(R6)}\qquad B^{-(M-1)}(\mu)=\emptyset\quad\text{for every }\mu\in D_1\setminus\{\nu_k\}=\{\mu^{(v)}:3\le v\le k-1\}\cup\{\omega_k\}.$$
**[GAP]** (R6) is not proved here. (H) yields only height $\le M-1$ for these trees (5.3); (R6) needs height $\le M-2$, which (H) does not imply.

6.2. CHECKED (exact, exhaustive, unconditional; finite range only): for $4\le k\le11$, `out/code/check_E.py 11` enumerates all partitions of $T_k-1$, computes $d_B$ exactly from the definition and the Cell-1 cyclic test, and confirms $\max d_B=M$ (so (H) holds for these $k$), $E_k=R_k$ (so (R6) holds), and every member of $E_k$ is a Garden of Eden. This proves target items 1–3 for $4\le k\le11$ with $E_k=R_k$ the explicit finite list printed by `out/code/print_R.py k`, and nothing for $k\ge12$.

6.3. Data (exploratory, not used): the tree heights of the elements of $D_1$ for $4\le k\le9$ (`out/code/heights_out.txt`) are $M-1$ for $\nu_k$ only; the next largest is $M-2-k$ (attained by $\mu^{(3)}$ for $5\le k\le9$), so (R6) appears to hold with a margin of $k+1$ steps.

## Step 7 (target item 1: explicit description) — [GAP] for general $k$

7.1. Established explicit content, all $k\ge4$: the reduction $E_k=\bigsqcup_{\mu\in D_1}B^{-(M-1)}(\mu)$ with $D_1$ listed explicitly (3.6, 4.1); the explicit members $\lambda^*_k$, $\alpha_k$, $\beta_k$ (4.2, 4.3); the Garden-of-Eden property under (H) (5.2).

7.2. **[GAP]** No closed-form rule listing every member of $E_k$ (or of $R_k$) as a function of $k$ is given. The description "$R_k=B^{-(M-1)}(\nu_k)$, computed by Lemma 2.1" is an explicit finite algorithm but is exactly the form the target excludes. Obstruction observed in the data: the members of $E_k$ are not contained in the class $\delta_{k-1}\subseteq\lambda\subseteq\delta_{k+1}$ (for $k=5$ some have cells on diagonal $7=k+2$, for $k=6$ on diagonal $9=k+3$), and the time at which the orbit of a member of $E_k$ joins the orbit of $\lambda^*_k$ ranges up to $30$ for $k=8$, so no bounded-depth tail rule of the type in 4.3 covers $E_k$.

7.3. Explicit lists for small $k$ (CHECKED, 6.2): $E_4=\{(3,2,2,1,1)\}$; $E_5=\{(4,3,3,2,1,1),(4,3,2,2,2,1),(4,3,2,2,1,1,1),(3,3,3,2,2,1),(3,3,3,2,1,1,1),(3,3,2,2,2,1,1)\}$. The sizes $|E_k|=1,6,34,175,831,3911,18163$ for $k=4,\dots,10$ match the target's data, and $|E_{11}|=84654$.

## Step 8 (what is established)

- PROVED, all $k\ge4$: 1.1–1.6; Lemma 2.1 and Corollary 2.2; Proposition 3.6 ($D_1$ explicit); Proposition 4.1 ($R_k\subseteq E_k$ and $E_k=\{B^{M-1}(\lambda)\in D_1\}$, no hypothesis); 4.3 ($\alpha_k,\beta_k\in R_k$, $k\ge5$); 4.2 via the subject's Proposition 7.2; under (H): 5.1, 5.2, 5.3.
- [GAP], $k\ge12$: (R6), i.e. target item 3; closed form of $E_k$, i.e. target item 1 (only the partial explicit content of 7.1 is given).
- CHECKED (exact, exhaustive, $4\le k\le11$ only, no use of (H)): target items 1–3, with $E_k=R_k$.
