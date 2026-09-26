**Proved here (less than TARGET):** for every $k\ge 4$, the partition $X_k=(k-1,k-2,k-2,k-3,\dots,2,1,1)$ of $T_k-1$ has $d_B(X_k)=k^2-2k-1$, so $D_B(T_k-1)\ge k^2-2k-1$; also $D_B(2)=0$ ($k=2$) and $D_B(5)=3$ ($k=3$). Within the class $\mathcal L_k$ defined in Step 5, $X_k$ is the unique partition of $T_k-1$ with the largest $d_B$, namely $k^2-2k-1$. **Not proved for general $k$:** the upper bound (a) and the upper half of (b) ([GAP], Step 7), and the characterisation (c) ([GAP], Step 8). (a), (b) and the extremal sets of (c) are checked by exhaustive exact computation for $4\le k\le 9$ only.

Reading of the brief: in (b) I take the range of $k$ to be all $k\ge 2$. For $k=1$, $T_1-1=0$ is not a size of a partition.

Notation: $k\ge 4$ and $m=k-1\ge 3$. Every $n$ with $T_{k-1}<n<T_k$ can be written $n=T_m+r$ with $1\le r\le m$. The cell in row $i$ and column $j$ of the (English) Young diagram is $(i,j)$, with $i,j\ge 0$. Its *diagonal* is $i+j$. Diagonal $d$ has the $d+1$ positions $(i,d-i)$, $0\le i\le d$, and "row $i$ of diagonal $d$" means $(i,d-i)$. A finite set of cells is the diagram of a partition exactly when it is closed under $(i,j)\mapsto(i-1,j)$ for $i\ge1$ and $(i,j)\mapsto(i,j-1)$ for $j\ge1$. I use this closure criterion (the definition of a Young diagram) throughout.

---

### Step 1 (cell map lemma, R1)
Let $\lambda$ have $s$ parts. Define $\varphi$ on the cells of $\lambda$ by
$$\varphi(i,0)=(0,i),\qquad \varphi(i,j)=(i+1,j-1)\ \ (1\le j\le s),\qquad \varphi(i,j)=(i,j-1)\ \ (j\ge s+1).$$
**Claim.** $\varphi$ is a bijection from the diagram of $\lambda$ onto the diagram of $B(\lambda)$.

*Proof.* Write $c_j(\lambda)=\#\{i:\lambda_{i+1}>j\}$ for the height of column $j$ (0-indexed rows). Let $\mu=B(\lambda)$. By definition its parts are $s$ together with the positive numbers among $\lambda_{i+1}-1$. So $c_j(\mu)=[s>j]+\#\{i:\lambda_{i+1}\ge j+2\}=[s>j]+c_{j+1}(\lambda)$.

Now list the image cells lying in column $j$.
- If $j\le s-1$, they are $\varphi(j,0)=(0,j)$ (which exists because $j<s$) and the cells $\varphi(i,j+1)=(i+1,j)$ for $0\le i<c_{j+1}(\lambda)$ (second rule, since $1\le j+1\le s$). Together these are exactly the rows $0,\dots,c_{j+1}(\lambda)$, which is $c_j(\mu)$ cells.
- If $j\ge s$, the first rule contributes nothing, because it only produces columns $i\le s-1$. The third rule contributes $\varphi(i,j+1)=(i,j)$ for $0\le i<c_{j+1}(\lambda)$. These are exactly the rows $0,\dots,c_{j+1}(\lambda)-1$, which is $c_j(\mu)$ cells.

Within each column the listed preimages are distinct, and images in different columns differ. Hence $\varphi$ is injective, and its image in each column $j$ is exactly the set of rows $0,\dots,c_j(\mu)-1$, which is the diagram of $\mu$. $\square$

**Consequence 1a.** Under the first two rules a cell keeps its diagonal. A cell $(i,d-i)$ on diagonal $d$ goes to row $i+1$ of diagonal $d$ if $i<d$, and from row $d$ to row $0$. Under the third rule the diagonal drops by one and the row stays the same.

### Step 2 (cyclic partitions, R2; cited from Cell 1)
By Cell 1, for $n=T_m+r$ with $1\le r\le m+1$ the cyclic partitions are $\lambda(e)=(m+e_1,m-1+e_2,\dots,1+e_m,e_{m+1})$ with $e\in\{0,1\}^{m+1}$ and $\sum e=r$. Row $i$ (0-indexed) of $\lambda(e)$ consists of the cells $(i,0),\dots,(i,m-i-1)$, which lie on diagonals $\le m-1$, together with $(i,m-i)$ exactly when $e_{i+1}=1$. Thus $\lambda(e)=\delta_m\cup\{(i,m-i):e_{i+1}=1\}$. Conversely, $\delta_m$ together with any $r$ cells of diagonal $m$ is $\lambda(e)$ for the indicator vector $e$ of their rows.

**Hence:** $\lambda$ is cyclic $\iff$ $\lambda\supseteq\delta_m$ and every cell outside $\delta_m$ lies on diagonal $m$. In particular, a partition with a cell on a diagonal $\ge m+1$ is not cyclic.

### Step 3 (late-phase dynamics, R3)
Let $\lambda\vdash n$ satisfy three conditions: $\lambda\supseteq\delta_m$; $\lambda\setminus\delta_m=S^\ast\cup\{z\}$ with $S^\ast\subseteq$ diagonal $m$; and $z=(c,m+1-c)$ is a single cell on diagonal $m+1$. Let $S\subseteq\{0,\dots,m\}$ be the set of rows of $S^\ast$.

(i) The number of parts is $s=\#\{i:(i,0)\in\lambda\}$. The column-0 cells are $(i,0)$ for $i\le m-1$ (they lie in $\delta_m$), $(m,0)$ when $m\in S$, and $(m+1,0)$ when $c=m+1$. By closure, $(m+1,0)\in\lambda$ forces $(m,0)\in\lambda$. So $s=m+[m\in S]+[c=m+1]\ge m$.

(ii) The third rule of $\varphi$ applies only to cells with column $j\ge s+1\ge m+1$. Such a cell lies on diagonal $\ge m+1$, so it is $z$, and then its column $m+1-c$ is $\ge m+1$, so $c=0$. Moreover $s\le m$ must hold, so $s=m$. When $c=0$ we have $c\ne m+1$, and then $s=m$ holds exactly when $m\notin S$. **So the third rule is used exactly when $c=0$ and $m\notin S$, and then only for $z$.**

(iii) Therefore, by Step 1 and Consequence 1a, there are two cases.
 - **No drop** ($c\neq0$ or $m\in S$): $B(\lambda)=\delta_m\cup\{\text{diag-}m\text{ rows }S+1 \bmod (m+1)\}\cup\{(c',m+1-c')\}$ with $c'=c+1\bmod(m+2)$. Here $\delta_m$ is mapped onto itself because each full diagonal $d\le m-1$ is permuted by the row rotation. So $B(\lambda)$ satisfies the same three conditions, with $(S,c)$ replaced by $(S+1,c+1)$.
 - **Drop** ($c=0$ and $m\notin S$): $z\mapsto(0,m)$, and every other cell rotates within its diagonal. Then $B(\lambda)=\delta_m\cup(\text{cells of diagonal }m)$, which is cyclic by Step 2.

(iv) Iterating (iii): while no drop has occurred, $B^t(\lambda)$ has diagonal-$m$ row set $S+t\pmod{m+1}$ and diagonal-$(m+1)$ cell at row $c+t\pmod{m+2}$. Let $t^\ast$ be the first $t\ge0$ with $c+t\equiv0\pmod{m+2}$ and $m\notin S+t$, that is, $m-t\bmod(m+1)\notin S$. For $t\le t^\ast$, $B^t(\lambda)$ has a cell on diagonal $m+1$, so it is not cyclic (Step 2). $B^{t^\ast+1}(\lambda)$ is cyclic. Hence **$d_B(\lambda)=t^\ast+1$**, provided $t^\ast$ exists; existence is shown case by case in Step 5.

(v) (Membership.) For $S\subseteq\{0,..,m\}$ and $0\le c\le m+1$, the set $\delta_m\cup S^\ast\cup\{z\}$ is a Young diagram exactly when two conditions hold: $c-1\in S$ if $c\ge1$, and $c\in S$ if $c\le m$. *Proof:* the left and upper neighbours of a diagonal-$m$ cell $(i,m-i)$ are $(i,m-i-1)$ and $(i-1,m-i)$ (when they exist), and both lie on diagonal $m-1$, inside $\delta_m$. The neighbours of $\delta_m$ cells lie in $\delta_m$. The neighbours of $z$ are $(c,m-c)$ (row $c$ of diagonal $m$, which exists iff $c\le m$) and $(c-1,m+1-c)$ (row $c-1$ of diagonal $m$, which exists iff $c\ge1$). $\square$

### Step 4 (lower bound, R4): $d_B(X_k)=k^2-2k-1$ for every $k\ge4$
Let $X_k=(m,m-1,m-1,m-2,\dots,2,1,1)$. Its parts are $X_1=m$, $X_2=m-1$, $X_i=m+2-i$ for $3\le i\le m+1$, and $X_{m+2}=1$.
- *It is a partition of $T_k-1$:* its sum is $m+(m-1)+\sum_{i=3}^{m+1}(m+2-i)+1=2m+T_{m-1}=T_m+m=T_{m+1}-1=T_k-1$. The parts are weakly decreasing and positive.
- *Its diagonal description:* row $0$ has cells $(0,0..m-1)$, so diagonal $m$ is empty at row 0. Row $1$ has cells $(1,0..m-2)$, so diagonal $m$ is empty at row 1. For $2\le i\le m$, row $i$ has length $X_{i+1}=m+1-i$, with cells $(i,0..m-i)$; these contain $\delta_m$'s row and the diagonal-$m$ cell $(i,m-i)$. Row $m+1$ is the single cell $(m+1,0)$, on diagonal $m+1$. Hence $X_k$ satisfies the conditions of Step 3 with $S=\{2,\dots,m\}$ (holes $H=\{0,1\}$) and $c=m+1$.
- *Computing $t^\ast$:* $c+t\equiv0\pmod{m+2}$ iff $t\equiv1\pmod{m+2}$, i.e. $t=1+j(m+2)$ with $j\ge0$. For such $t$, $m-t\equiv m-1-j\pmod{m+1}$ (because $m+2\equiv1$). This value lies in $H=\{0,1\}$ iff $j\equiv m-1$ or $j\equiv m-2\pmod{m+1}$. For $0\le j\le m-3$ we get $m-1-j\in\{2,\dots,m-1\}$, which is not in $H$. For $j=m-2$ we get the value $1\in H$. So $t^\ast=1+(m-2)(m+2)=m^2-3$.
- By Step 3(iv), $d_B(X_k)=m^2-2=(k-1)^2-2=k^2-2k-1$. Hence $D_B(T_k-1)\ge k^2-2k-1$ for every $k\ge4$. (Checked independently by direct iteration for $4\le k\le 25$: `code/check.py`.)

### Step 5 (class $\mathcal L_k$, R5)
Let $\mathcal L_k$ be the set of partitions of $T_k-1=T_m+m$ as in Step 3. Then $|S|=m-1$, so the hole set $H=\{0..m\}\setminus S$ has exactly $2$ elements. **Claim:** every $\lambda\in\mathcal L_k$ has $d_B(\lambda)\le m^2-2$, with equality iff $\lambda=X_k$.

Write $t_0=(-c)\bmod(m+2)\in\{0,..,m+1\}$. The times with $c+t\equiv0$ are $t=t_0+j(m+2)$ with $j\ge0$, and then $m-t\equiv m-t_0-j\pmod{m+1}$. Let $j^\ast$ be the least $j\ge0$ with $m-t_0-j\bmod(m+1)\in H$. Then $t^\ast=t_0+j^\ast(m+2)$ and $d_B=t^\ast+1$.
- **$c=m+1$:** here $t_0=1$ and, by Step 3(v), $m\in S$, so $H\subseteq\{0,..,m-1\}$. As $j$ runs over $0..m-1$, $m-1-j$ runs over $m-1,\dots,0$, so $j^\ast=m-1-\max H$. Two distinct elements of $\{0,..,m-1\}$ have maximum $\ge1$, so $j^\ast\le m-2$, with equality iff $H=\{0,1\}$. Hence $d_B=2+j^\ast(m+2)\le m^2-2$, with equality iff $S=\{2..m\}$ and $c=m+1$. By Step 4, that is $X_k$.
- **$c=0$:** here $t_0=0$ and $0\in S$, so $H\subseteq\{1..m\}$ and $j^\ast=m-\max H\le m-2$. Hence $d_B=1+j^\ast(m+2)\le m^2-3$.
- **$1\le c\le m$:** here $t_0=m+2-c\le m+1$ and $c-1,c\in S$. The residue $m-t_0-j\equiv c-2-j$. For $j=0,..,m$ this runs through all residues mod $m+1$; it reaches $c$ at $j=m-1$ and $c-1$ at $j=m$. So both elements of $H$ are reached at indices in $\{0..m-2\}$, and the first of them at an index $j^\ast\le m-3$. Hence $d_B\le m+1+(m-3)(m+2)+1=m^2-4$.

In each case $t^\ast$ exists, which completes Step 3(iv). $\square$ (Cross-checked for $4\le k\le 25$ by enumerating all of $\mathcal L_k$: `code/check.py`.)

### Step 6 (small $k$, R6)
- $k=1$: $T_1-1=0$, so there is no partition (excluded).
- $k=2$, $n=2$: $B((2))=(1,1)$ and $B((1,1))=(2)$, so both partitions are cyclic and $D_B(2)=0$. Both attain it.
- $k=3$, $n=5$: by Step 2 with $m=2$, $r=2$, the cyclic partitions are $(3,2),(3,1,1),(2,2,1)$. Direct computation gives $(5)\to(4,1)\to(3,2)$, $(2,1,1,1)\to(4,1)$, and $(1^5)\to(5)$. So $d_B$ equals $1,2,2,3$ for $(4,1),(5),(2,1,1,1),(1^5)$. Hence $D_B(5)=3$, attained only by $(1,1,1,1,1)$. (Here $3\ne k^2-2k-1=2$.)

### Step 7 (upper bound (a), R7), [GAP]
I have **no proof** that $d_B(\lambda)\le k^2-2k-1$ for all $\lambda\vdash n$, $T_{k-1}<n<T_k$, and general $k\ge4$. Step 5 proves it only for $\lambda\in\mathcal L_k$ (with $n=T_k-1$). **CHECKED (finite, exact, exhaustive):** for $4\le k\le 9$ and every $n$ with $T_{k-1}<n<T_k$, $\max_\lambda d_B(\lambda)\le k^2-2k-1$, with equality at $n=T_k-1$ (`code/check.py`). This proves nothing for $k\ge10$.

### Step 8 (extremal set (c), R9), [GAP]
Proved: $X_k\in E_k:=\{\lambda\vdash T_k-1: d_B(\lambda)=D_B(T_k-1)\}$ **provided** Step 7 holds. Unconditionally, $X_k$ has the largest $d_B$ inside $\mathcal L_k$, and it is the only partition that does (Step 5). Exhaustive computation gives $|E_k|=1,6,34,175,831,3911$ for $k=4,\dots,9$, with $E_4=\{(3,2,2,1,1)\}$ and $E_5=\{(4,3,3,2,1,1),(4,3,2,2,2,1),(4,3,2,2,1,1,1),(3,3,3,2,2,1),(3,3,3,2,1,1,1),(3,3,2,2,2,1,1)\}$. So **$E_k\ne\{X_k\}$ for $5\le k\le 9$**. The other members lie outside $\mathcal L_k$ and reach states of the orbit of $X_k$ (or other states with the same remaining time) after several steps. I have no explicit description of $E_k$ as a function of $k$ and no proof of one.

### What is established
(b) lower bound for all $k\ge4$: PROVED. (b) values for $k=2,3$: PROVED. Upper bound restricted to $\mathcal L_k$: PROVED. (a), and the upper half of (b), for general $k$: GAP (verified only for $k\le 9$). (c): GAP (exact sets computed only for $k\le 9$).
