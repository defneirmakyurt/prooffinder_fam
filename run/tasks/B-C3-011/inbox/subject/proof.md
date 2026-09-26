Proved here (and nothing more): (i) for every $k\ge 3$, every $n$ with $T_{k-1}<n<T_k$ and every partition $\lambda$ of $n$ with $\delta_{k-1}\subseteq\lambda\subseteq\delta_{k+1}$ (diagram inclusion), $d_B(\lambda)\le k^2-2k-1$; (ii) for every $k\ge 3$ the partition $\lambda^*_k=(k-1,k-2,k-2,k-3,\dots,2,1,1)$ of $T_k-1$ has $d_B(\lambda^*_k)=k^2-2k-1$, hence $D_B(T_k-1)\ge k^2-2k-1$ for all $k\ge 4$; (iii) $D_B(2)=0$ and $D_B(5)=3$, with extremal sets $\{(2),(1,1)\}$ and $\{(1,1,1,1,1)\}$; (iv) every $\lambda\vdash T_k-1$ with $B^{k^2-2k-2}(\lambda)=\nu_k:=(k+1,k-1,k-2,\dots,3,1)$ has $d_B(\lambda)=k^2-2k-1$ ($k\ge 4$).

**Not proved (marked [GAP]):** target (a) for partitions outside the class $\delta_{k-1}\subseteq\lambda\subseteq\delta_{k+1}$; hence the upper half of (b) and the "no other partition" half of (c). These are verified by exact exhaustive computation only for $4\le k\le 10$ (which proves nothing for $k\ge 11$).

Reading of the target: exactly as stated in TARGET; no ambiguity was resolved by choice.

---

## Notation

N1. The diagram of a partition $\lambda=(\lambda_1\ge\dots\ge\lambda_s)$ is $\{(i,j):1\le i\le s,\ 1\le j\le\lambda_i\}$; we identify $\lambda$ with its diagram and write $\mu\subseteq\lambda$ for inclusion of diagrams. We put $\lambda_i=0$ for $i>s$ and $x^+=\max(x,0)$.

N2. The cell $(i,j)$ lies on *diagonal* $i+j-1$. $\delta_m$ (diagram of $(m,m-1,\dots,1)$) is the set of cells on diagonals $1,\dots,m$; row $i$ of $\delta_m$ has length $(m+1-i)^+$.

N3. $\mathcal C_k=\{\lambda:\ \delta_{k-1}\subseteq\lambda\subseteq\delta_{k+1}\}$.

## Step 1 (cyclic partitions, from Cell 1)

1.1. Let $n=T_{k-1}+r$ with $1\le r\le k-1$. By Cell 1 (ASSUMPTIONS), $\lambda\vdash n$ is cyclic iff $\lambda=\lambda(e)=(k-1+e_1,\dots,1+e_{k-1},e_k)$ with $e\in\{0,1\}^k$, $\sum e_i=r$. Row $i\le k$ of $\lambda(e)$ has length $(k-i)+e_i$, while row $i$ of $\delta_{k-1}$ has length $(k-i)^+$ and row $i$ of $\delta_k$ has length $k+1-i$ (N2). Hence $\delta_{k-1}\subseteq\lambda(e)\subseteq\delta_k$.
Conversely, if $\delta_{k-1}\subseteq\lambda\subseteq\delta_k$ and $|\lambda|=n$, then $k-i\le\lambda_i\le k+1-i$ for $i\le k$ and $\lambda_i=0$ for $i>k$, so $\lambda=\lambda(e)$ with $e_i=\lambda_i-(k-i)\in\{0,1\}$ and $\sum e_i=n-T_{k-1}=r$. Therefore
$$\lambda\vdash n \text{ is cyclic}\iff \delta_{k-1}\subseteq\lambda\subseteq\delta_k .\tag{1.1}$$

1.2. If $\mu$ is cyclic, $B^i(\mu)=\mu$ with $i\ge1$, then $B^i(B(\mu))=B(B^i(\mu))=B(\mu)$, so $B(\mu)$ is cyclic. By induction $B^j(\mu)$ is cyclic for all $j\ge0$.

1.3. Consequently, for every $\lambda$ and $t\ge0$: $d_B(\lambda)\le t\iff B^t(\lambda)$ is cyclic (the "$\Leftarrow$" direction is the definition of $d_B$ as a minimum; "$\Rightarrow$" is 1.2 applied to $\mu=B^{d_B(\lambda)}(\lambda)$).

## Step 2 (encoding of $\mathcal C_k$), $k\ge 2$

2.1. For $\lambda\in\mathcal C_k$ define $A=(A_0,\dots,A_{k-1})$ and $P=(P_0,\dots,P_k)$ in $\{0,1\}$ by
$A_x=1\iff(x+1,\,k-x)\in\lambda$ (the cell of diagonal $k$ in row $x+1$), and $P_q=1\iff(q+1,\,k+1-q)\in\lambda$ (the cell of diagonal $k+1$ in row $q+1$). Put $A_k:=0$.

2.2. **Row formula.** For $1\le i\le k+1$: $\lambda_i=(k-i)^++A_{i-1}+P_{i-1}$, and $\lambda_i=0$ for $i\ge k+2$.
*Proof.* Row $i$ of $\lambda$ is an initial segment $\{(i,1),\dots,(i,\lambda_i)\}$ lying between row $i$ of $\delta_{k-1}$ (length $(k-i)^+$) and row $i$ of $\delta_{k+1}$ (length $(k+2-i)^+$). For $i\le k$ the cells of row $i$ in $\delta_{k+1}\setminus\delta_{k-1}$ are $(i,k+1-i)$ (diagonal $k$) and $(i,k+2-i)$ (diagonal $k+1$); for $i=k+1$ it is only $(k+1,1)$ (diagonal $k+1$); for $i\ge k+2$ there is none. Since the row is an initial segment, $\lambda_i-(k-i)^+$ equals the number of these cells present, which is $A_{i-1}+P_{i-1}$ (with $A_k=0$). $\square$

2.3. **Support rule (S).** If $P_q=1$ then $A_q=1$ when $q\le k-1$, and $A_{q-1}=1$ when $q\ge1$.
*Proof.* $P_q=1$ means $(q+1,k+1-q)\in\lambda$. If $q\le k-1$ then $k+1-q\ge2$ and the left neighbour $(q+1,k-q)$ is in $\lambda$ (rows are initial segments); it is the diagonal-$k$ cell of row $q+1$, so $A_q=1$. If $q\ge1$ the upper neighbour $(q,k+1-q)$ is in $\lambda$ (as $\lambda_q\ge\lambda_{q+1}$); it lies on diagonal $q+(k+1-q)-1=k$ in row $q$, so $A_{q-1}=1$. $\square$
In particular $P_q\le A_q$ for $q\le k-1$.

2.4. **Converse.** Let $A\in\{0,1\}^k$, $P\in\{0,1\}^{k+1}$ satisfy (S), $A_k:=0$, and set $\mu_i=(k-i)^++A_{i-1}+P_{i-1}$ for $1\le i\le k+1$. Then $\mu_1\ge\mu_2\ge\dots\ge\mu_{k+1}\ge0$, the positive $\mu_i$ form a partition $\mu\in\mathcal C_k$, its vectors (2.1) are exactly $(A,P)$, and $|\mu|=T_{k-1}+|A|+|P|$.
*Proof.* For $1\le i\le k-1$: $\mu_i-\mu_{i+1}=1+(A_{i-1}+P_{i-1})-(A_i+P_i)$. This is $<0$ only if $A_i+P_i=2$ and $A_{i-1}+P_{i-1}=0$; but $P_i=1$ forces $A_{i-1}=1$ by (S). For $i=k$: $\mu_k-\mu_{k+1}=A_{k-1}+P_{k-1}-P_k$, and $P_k=1$ forces $A_{k-1}=1$ by (S); so it is $\ge0$. Hence the sequence is weakly decreasing and its zero entries come last. Since $(k-i)^+\le\mu_i\le(k-i)^++2$ for $i\le k$ and $\mu_{k+1}=P_k\le1$, rows of $\mu$ lie between those of $\delta_{k-1}$ and $\delta_{k+1}$, so $\mu\in\mathcal C_k$. By 2.2 applied to $\mu$, its vectors $(\tilde A,\tilde P)$ satisfy $\tilde A_{i-1}+\tilde P_{i-1}=A_{i-1}+P_{i-1}$ for $i\le k$ and $\tilde P_k=P_k$; as both pairs obey $P_q\le A_q$ ($q\le k-1$, by 2.3 and by (S)), the value $0,1,2$ of the sum determines the pair $(0,0),(1,0),(1,1)$; so $(\tilde A,\tilde P)=(A,P)$. Finally $\sum_i\mu_i=\sum_{i=1}^{k-1}(k-i)+|A|+|P|=T_{k-1}+|A|+|P|$. $\square$

2.5. By 2.2–2.4, $\lambda\mapsto(A,P)$ is a bijection from $\mathcal C_k$ onto pairs satisfying (S), and $|\lambda|=T_{k-1}+|A|+|P|$. Moreover $\lambda\subseteq\delta_k\iff P=0$ (the cells of $\delta_{k+1}\setminus\delta_k$ are exactly the diagonal-$(k+1)$ cells).

## Step 3 (the shift on $\mathcal C_k$), $k\ge2$

3.1. **Lemma.** Let $\lambda\in\mathcal C_k$ with vectors $(A,P)$ and define the rotations $A'_x=A_{(x-1)\bmod k}$ ($0\le x\le k-1$), $P'_q=P_{(q-1)\bmod(k+1)}$ ($0\le q\le k$).
(i) If not ($A_{k-1}=0$ and $P_0=1$), then $B(\lambda)\in\mathcal C_k$ with vectors $(A',P')$.
(ii) If $A_{k-1}=0$ and $P_0=1$ ("absorption"), then $B(\lambda)\in\mathcal C_k$ with vectors $(A'',P'')$, where $A''=A'$ except $A''_0=1$ (whereas $A'_0=A_{k-1}=0$), and $P''=P'$ except $P''_1=0$ (whereas $P'_1=P_0=1$).

*Proof.* 3.1.a (number of parts). Rows $1,\dots,k-1$ have $\lambda_i\ge k-i\ge1$. By 2.2, $\lambda_k=A_{k-1}+P_{k-1}$ and $\lambda_{k+1}=P_k$; by (S), $P_{k-1}=1\Rightarrow A_{k-1}=1$ and $P_k=1\Rightarrow A_{k-1}=1$. Hence $\lambda_k>0\iff A_{k-1}=1$, $\lambda_{k+1}>0\iff P_k=1$, and the number of parts is $s=k-1+A_{k-1}+P_k$.

3.1.b (parts of $B(\lambda)$). By definition the parts of $B(\lambda)$ are $s$ and the positive numbers among $\lambda_1-1,\dots,\lambda_s-1$. Put $\mu_1=s$, $\mu_{i+1}=\lambda_i-1$ for $1\le i\le k-1$, and $\mu_{k+1}=P_{k-1}$. For $i\le k-1$, $\lambda_i-1\ge k-i-1\ge0$. For $i=k$: if $A_{k-1}=1$ then $\lambda_k-1=P_{k-1}=\mu_{k+1}$; if $A_{k-1}=0$ then $\lambda_k=0$ is not a part and $\mu_{k+1}=P_{k-1}=0$ (by (S)). For $i=k+1$: $\lambda_{k+1}-1=P_k-1\le0$ contributes no part. Hence the multiset of parts of $B(\lambda)$ equals the multiset of positive entries of $(\mu_1,\dots,\mu_{k+1})$.

3.1.c (the $\mu_j$ in terms of the rotation). $\mu_1=(k-1)+A_{k-1}+P_k=(k-1)+A'_0+P'_0$; for $1\le i\le k-1$, $\mu_{i+1}=(k-i-1)+A_{i-1}+P_{i-1}=(k-(i+1))+A'_i+P'_i$; and $\mu_{k+1}=P_{k-1}=P'_k=(k-(k+1))^++A'_k+P'_k$ with $A'_k:=0$. So $\mu_j=(k-j)^++A'_{j-1}+P'_{j-1}$ for $1\le j\le k+1$.

3.1.d (when (S) holds for $(A',P')$). Let $P'_q=1$, i.e. $P_{(q-1)\bmod(k+1)}=1$. If $2\le q\le k-1$: (S) for $P_{q-1}$ gives $A_{q-1}=A_{q-2}=1$, i.e. $A'_q=A'_{q-1}=1$. If $q=k$: (S) for $P_{k-1}$ gives $A_{k-2}=1$, i.e. $A'_{k-1}=1$, which is all (S) requires at $q=k$. If $q=0$: $P_k=1$ gives $A_{k-1}=1$, i.e. $A'_0=1$, all that is required at $q=0$. If $q=1$: $P_0=1$ gives $A_0=1$, i.e. $A'_1=1$, and (S) also requires $A'_0=A_{k-1}=1$. Hence $(A',P')$ satisfies (S) unless $P_0=1$ and $A_{k-1}=0$, and in that exceptional case the only violated requirement is "$P'_1=1\Rightarrow A'_0=1$".

(i) Outside the exceptional case, 2.4 applies to $(A',P')$: by 3.1.c the sequence $(\mu_j)$ is the row sequence of the partition with vectors $(A',P')$, it is weakly decreasing, and by 3.1.b its positive entries are the parts of $B(\lambda)$. So $B(\lambda)$ is that partition.

(ii) In the exceptional case $P_0=1$, $A_{k-1}=0$; by (S) $A_0=1$, $P_k=0$, $P_{k-1}=0$. The pair $(A'',P'')$ satisfies (S): the only requirement violated by $(A',P')$ concerned $P'_1$, now $P''_1=0$; all other requirements held for $(A',P')$ and remain true since $A''\ge A'$ and $P''\le P'$ entrywise. Let $\nu_j=(k-j)^++A''_{j-1}+P''_{j-1}$. Then $\nu_1=(k-1)+1+P_k=k$, $\nu_2=(k-2)+A_0+0=k-1$, and $\nu_j=\mu_j$ for $j\ge3$ (the vectors agree at indices $\ge2$). On the other hand $\mu_1=s=k-1$ (3.1.a) and $\mu_2=\lambda_1-1=(k-2)+A_0+P_0=k$. So $\{\mu_1,\mu_2\}=\{\nu_1,\nu_2\}$ as multisets and the positive entries of $\mu$ and $\nu$ agree as multisets. By 2.4, $\nu$ is weakly decreasing and is the row sequence of the partition with vectors $(A'',P'')$; by 3.1.b that partition is $B(\lambda)$. $\square$

3.2. (Cross-check, not used in the proof.) `out/code/check_classC.py` compares Lemma 3.1 with the definition of $B$ on every pair $(A,P)$ with $1\le|A|+|P|\le k-1$ for $3\le k\le 10$: no mismatch.

## Step 4 (rotating frame), $k\ge 2$

Fix $\lambda\in\mathcal C_k$, let $\lambda^{(t)}=B^t(\lambda)$; by Lemma 3.1 and induction, $\lambda^{(t)}\in\mathcal C_k$; let $(A^t,P^t)$ be its vectors. Say *absorption at time $t$* if $A^t_{k-1}=0$ and $P^t_0=1$.

4.1. **Hole labels.** Let $H_t=\{\ell\in\mathbb Z_k: A^t_{(\ell+t)\bmod k}=0\}$. Then $H_{t+1}=H_t$ if there is no absorption at time $t$, and $H_{t+1}=H_t\setminus\{\ell_t\}$ with $\ell_t:=(k-1-t)\bmod k\in H_t$ if there is.
*Proof.* $\ell\in H_{t+1}\iff A^{t+1}_{\ell+t+1}=0$ (indices mod $k$). If $\ell+t+1\not\equiv0$, Lemma 3.1 gives $A^{t+1}_{\ell+t+1}=A^t_{\ell+t}$. If $\ell+t+1\equiv0$, i.e. $\ell=\ell_t$, then $A^{t+1}_0=A^t_{k-1}$ without absorption, and $A^{t+1}_0=1$ with absorption (where $A^t_{k-1}=0$, i.e. $\ell_t\in H_t$). $\square$
Hence $H_{t}\subseteq H_0$ for all $t$, and $|H_0|-|H_t|$ equals the number of absorptions before time $t$.

4.2. **Particles.** Let $\Pi_t=\{q:P^t_q=1\}\subseteq\mathbb Z_{k+1}$. By Lemma 3.1, $\Pi_{t+1}=\Pi_t+1$ without absorption, and $\Pi_{t+1}=(\Pi_t+1)\setminus\{1\}$ with absorption (then $0\in\Pi_t$). So we may label the particles of $\Pi_0=\{q_1,\dots,q_p\}$ ($p=|P|$): particle $j$ is at position $q_j+t\bmod(k+1)$ at every time $t$ at which it is alive; it dies exactly at the first time $t$ with $q_j+t\equiv0\pmod{k+1}$ and absorption at $t$; each absorption kills exactly one particle and removes exactly one hole label; no particle is ever created.

4.3. **Checks.** Let $Q_j\in\{1,\dots,k+1\}$, $Q_j\equiv q_j\pmod{k+1}$ (so $Q_j=q_j$ if $q_j\ge1$, $Q_j=k+1$ if $q_j=0$). The times $t\ge0$ with $q_j+t\equiv0\pmod{k+1}$ are $t_j(v)=(k+1)v-Q_j$, $v=1,2,\dots$ At time $t_j(v)$ ("the $v$-th check of $j$"), if $j$ is alive, $j$ dies iff $\ell_{t_j(v)}\in H_{t_j(v)}$, and
$$\ell_{t_j(v)}=(k-1-(k+1)v+Q_j)\bmod k=(Q_j-1-v)\bmod k,$$
because $(k+1)v\equiv v\pmod k$. So the $v$-th check of $j$ inspects the label $Q_j-1-v$.

4.4. **Forbidden labels at time 0.** By (S) at $t=0$: if $1\le Q_j\le k-1$ then $A_{Q_j-1}=A_{Q_j}=1$, i.e. $Q_j-1,\,Q_j\notin H_0$; if $Q_j=k$ then $A_{k-1}=1$, i.e. $Q_j-1\notin H_0$; if $Q_j=k+1$ ($q_j=0$) then $A_0=1$, i.e. $0\equiv Q_j-1\notin H_0$.

## Step 5 (counting lemma), $k\ge3$

5.1. **Lemma.** Assume $|H_0|\ge p+1$. Then every particle $j$ dies at some check $v_j$ with $v_j\le k-3$ if $Q_j\le k-1$, and $v_j\le k-2$ if $Q_j\in\{k,k+1\}$.
*Proof.* Let $m_j=k-3$ if $Q_j\le k-1$ and $m_j=k-2$ otherwise; suppose $j$ is alive after its checks $v=1,\dots,m_j$. The inspected labels $L_j=\{Q_j-1-v: 1\le v\le m_j\}$ are $m_j\le k-2$ consecutive residues, hence distinct: $L_j=\mathbb Z_k\setminus\{Q_j-1,Q_j,Q_j+1\}$ if $Q_j\le k-1$ and $L_j=\mathbb Z_k\setminus\{Q_j-1,Q_j\}$ otherwise (the excluded residues are distinct since $k\ge3$). By 4.4, $Q_j-1\notin H_0$ always and $Q_j\notin H_0$ if $Q_j\le k-1$; so $|L_j\cap H_0|\ge|H_0|-1\ge p$. Each $\ell\in L_j\cap H_0$ is, at the time of the check of $j$ inspecting it, not in $H_t$ (else $j$ would have died), so by 4.1 it was removed at an earlier absorption, which by 4.2 killed a particle other than $j$ ($j$ is alive). Distinct labels are removed at distinct absorptions, killing distinct particles. So at least $p$ particles other than $j$ exist, contradicting $|\Pi_0|=p$. $\square$
(For $k=3$ and $Q_j\le2$ the bound $v_j\le0$ means no such particle exists; the proof covers this: then $L_j=\emptyset$ and $0\ge p\ge1$ is already the contradiction.)

## Step 6 (target (a) on the class $\mathcal C_k$)

6.1. **Theorem.** Let $k\ge3$, $n=T_{k-1}+r$ with $1\le r\le k-1$, and $\lambda\vdash n$ with $\lambda\in\mathcal C_k$. Then $d_B(\lambda)\le k^2-2k-1$.
*Proof.* With $(A,P)$ the vectors of $\lambda$ and $p=|P|$: by 2.5, $|A|=r-p$, so $|H_0|=k-|A|=k-r+p\ge p+1$. By Lemma 5.1, particle $j$ dies at time $t_j(v_j)=(k+1)v_j-Q_j$, which is at most $(k+1)(k-3)-1=k^2-2k-4$ if $Q_j\le k-1$ (using $Q_j\ge1$), at most $(k+1)(k-2)-k=k^2-2k-2$ if $Q_j=k$, and at most $(k+1)(k-2)-(k+1)=k^2-2k-3$ if $Q_j=k+1$. By 4.2 no particle is created, so $P^{t}=0$ for $t=k^2-2k-1$ (also if $p=0$). Then $\delta_{k-1}\subseteq\lambda^{(t)}\subseteq\delta_k$ (2.5), so $\lambda^{(t)}$ is cyclic by (1.1), and $d_B(\lambda)\le k^2-2k-1$ by 1.3. $\square$

6.2. **[GAP] Target (a) in general.** For $\lambda\notin\mathcal C_k$ (a cell on a diagonal $\ge k+2$, or a hole on a diagonal $\le k-1$) no argument is given here. Nothing in Steps 1–6 bounds the time to enter $\mathcal C_k$ jointly with the remaining time in $\mathcal C_k$. Exact exhaustive computation (`out/code/check_small.py 10`, all partitions of all $n$ with $T_{k-1}<n<T_k$, $4\le k\le10$) finds $D_B(n)\le k^2-2k-1$ in every case; this proves (a) only for $4\le k\le10$.

## Step 7 (lower bound for (b))

7.1. For $k\ge3$ let $A^*=(0,0,1,\dots,1)\in\{0,1\}^k$ (holes at $x=0,1$) and $P^*=(0,\dots,0,1)\in\{0,1\}^{k+1}$ ($P^*_k=1$). (S) holds: its only requirement is $A^*_{k-1}=1$, true as $k-1\ge2$. By 2.2/2.4 the partition is $\lambda^*_k$ with rows $\lambda_1=k-1$, $\lambda_2=k-2$, $\lambda_i=k-i+1$ ($3\le i\le k$), $\lambda_{k+1}=1$, i.e.
$$\lambda^*_k=(k-1,\,k-2,\,k-2,\,k-3,\,\dots,\,2,\,1,\,1),\qquad|\lambda^*_k|=T_{k-1}+(k-2)+1=T_k-1 .$$
(For $k=3$: $(2,1,1,1)$; $k=4$: $(3,2,2,1,1)$; $k=5$: $(4,3,3,2,1,1)$.)

7.2. **Proposition.** For $k\ge3$, $d_B(\lambda^*_k)=k^2-2k-1$ and $B^{k^2-2k-2}(\lambda^*_k)=\nu_k:=(k+1,k-1,k-2,\dots,3,1)$.
*Proof.* Here $H_0=\{0,1\}$ and there is one particle, $Q_1=q_1=k$. Until its death, $H_t=H_0$ (4.1: labels are removed only by absorptions, each of which kills a particle). Its $v$-th check inspects label $k-1-v\bmod k$ (4.3): for $v=1,\dots,k-3$ these are $k-2,k-3,\dots,2\notin H_0$, so it survives; the check $v=k-2$ inspects label $1\in H_0$, so it dies at time $t^*=(k+1)(k-2)-k=k^2-2k-2$. For $0\le t\le t^*$ the particle is alive, so $P^t\neq0$, $\lambda^{(t)}\not\subseteq\delta_k$ (2.5) and $\lambda^{(t)}$ is not cyclic by (1.1). At $t^*+1$ the particle is gone, $P^{t^*+1}=0$, and $\lambda^{(t^*+1)}$ is cyclic by 2.5 and (1.1). Hence $d_B(\lambda^*_k)=t^*+1=k^2-2k-1$.
At $t=t^*$: $t^*\equiv-2\pmod k$, so $A^{t^*}_x=0\iff x-t^*\in\{0,1\}\iff x\in\{k-2,k-1\}$; the particle is at $k+t^*=(k+1)(k-2)\equiv0\pmod{k+1}$, so $P^{t^*}=(1,0,\dots,0)$. By 2.2 the rows are $\lambda_1=(k-1)+1+1=k+1$, $\lambda_i=k-i+1$ for $2\le i\le k-2$, $\lambda_{k-1}=1+0+0=1$, $\lambda_k=\lambda_{k+1}=0$: this is $\nu_k$. $\square$

7.3. **Corollary.** For every $k\ge4$: $D_B(T_k-1)\ge k^2-2k-1$ (7.2, since $\lambda^*_k\vdash T_k-1$).

## Step 8 (target (b))

8.1. **Claim (b).** $D_B(T_k-1)=k^2-2k-1$ for every $k\ge4$; $D_B(T_2-1)=D_B(2)=0$; $D_B(T_3-1)=D_B(5)=3$; for $k=1$, $T_1-1=0$ is not a positive integer, so there is nothing to determine.
Status: the lower bound is 7.3 (all $k\ge4$). The upper bound for $k\ge4$ is target (a) at $n=T_k-1$: **[GAP]** in general; proved for $\lambda\in\mathcal C_k$ (6.1); verified exhaustively for $4\le k\le10$ (6.2).

8.2. **$k=2$, $n=2$.** Cell 1 with $k=2$, $r=1$: cyclic partitions are $(1+e_1,e_2)$ with $e_1+e_2=1$, i.e. $(2)$ and $(1,1)$, all partitions of 2. So $D_B(2)=0$, attained by both.

8.3. **$k=3$, $n=5$.** Cell 1 with $k=3$, $r=2$: the cyclic partitions are $(2+e_1,1+e_2,e_3)$ with two $e_i=1$: $(3,2),(3,1,1),(2,2,1)$. From the definition: $B(4,1)=(3,2)$; $B(5)=(4,1)$; $B(2,1,1,1)=(4,1)$ (parts $1,4$); $B(1,1,1,1,1)=(5)$. So $d_B$ equals $0,0,0$ on the cyclic ones, $d_B(4,1)=1$, $d_B(5)=2$, $d_B(2,1,1,1)=2$, $d_B(1,1,1,1,1)=3$. These are all $7$ partitions of $5$. Hence $D_B(5)=3$ (not $3^2-2\cdot3-1=2$), attained only by $(1,1,1,1,1)$.

## Step 9 (target (c))

9.1. **Proposition.** Let $k\ge4$, $n=T_k-1$, $m=k^2-2k-2$. If $\lambda\vdash n$ and $B^{m}(\lambda)=\nu_k$, then $d_B(\lambda)=k^2-2k-1$.
*Proof.* $\nu_k$ is not cyclic: its first part $k+1$ exceeds the first row $k$ of $\delta_k$, so $\nu_k\not\subseteq\delta_k$, and (1.1). $B(\nu_k)=B^{t^*+1}(\lambda^*_k)$ is cyclic (7.2). If some $B^i(\lambda)$ with $i\le m$ were cyclic, then $B^m(\lambda)=\nu_k$ would be cyclic by 1.2; so $d_B(\lambda)>m$, while $B^{m+1}(\lambda)=B(\nu_k)$ is cyclic, so $d_B(\lambda)=m+1$. $\square$

9.2. **Claim (c).** For $k\ge4$ the set of $\lambda\vdash T_k-1$ with $d_B(\lambda)=D_B(T_k-1)$ is exactly $\mathcal E_k=\{\lambda\vdash T_k-1: B^{k^2-2k-2}(\lambda)=\nu_k\}$, $\nu_k=(k+1,k-1,k-2,\dots,3,1)$; it contains $\lambda^*_k$. For $k=2$: $\{(2),(1,1)\}$; for $k=3$: $\{(1,1,1,1,1)\}$ (8.2, 8.3, proved).
Status for $k\ge4$: "$\lambda^*_k\in\mathcal E_k$" is 7.2. "Every element of $\mathcal E_k$ is extremal" follows from 9.1 **once the upper bound of (b) holds** ([GAP] beyond $\mathcal C_k$; true for $4\le k\le10$ by computation). "No other partition is extremal", i.e. every extremal $\lambda$ satisfies $B^{k^2-2k-2}(\lambda)=\nu_k$: **[GAP]**, verified exhaustively for $4\le k\le10$ (`check_small.py`, all extremals of $T_k-1$). The sizes $|\mathcal E_k|$ for $k=4,\dots,10$ are $1,6,34,175,831,3911,18163$; so $\mathcal E_k$ is not a short explicit list, and the dynamical description above is the form in which it is stated. For $k=4$, $\mathcal E_4=\{(3,2,2,1,1)\}=\{\lambda^*_4\}$ (computation).

## Step 10 (what is established)

- PROVED for all $k$ in the stated ranges: (1.1); Lemma 3.1; Lemma 5.1; Theorem 6.1 ((a) on $\mathcal C_k$, $k\ge3$); Proposition 7.2 and Corollary 7.3 (lower half of (b), $k\ge4$); 8.2, 8.3 (small $k$); 9.1.
- [GAP]: (a) outside $\mathcal C_k$; hence upper half of (b) for $k\ge4$ and both inclusions of (c) for $k\ge 4$ except $\lambda^*_k\in\mathcal E_k$ and "$\mathcal E_k\subseteq$ extremal set, conditional on (b)".
- CHECKED (exact, exhaustive, finite range only): (a), (b), (c) for $4\le k\le10$.
