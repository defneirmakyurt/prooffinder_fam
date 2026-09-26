We prove: (a) for every $k\ge1$, $\delta_k$ is the unique cyclic partition of $T_k$; (b) for every $k\ge 1$ the explicit partition $\lambda^{(k)}$ below satisfies $d_B(\lambda^{(k)})=k^2-k$, so $D_B(T_k)\ge k^2-k$; (c) for every $k\ge1$, $d_B(\lambda)\le k^2-k$ for every partition $\lambda$ of $T_k$ with $\delta_{k-1}\subseteq\lambda\subseteq\delta_{k+1}$ (diagram containment); (d) $D_B(T_k)=k^2-k$ for $1\le k\le 11$ (computer-assisted, exhaustive). NOT established: $d_B(\lambda)\le k^2-k$ for arbitrary $\lambda\vdash T_k$ when $k\ge 12$ [GAP]. Hence the target $D_B(T_k)=F(k):=k^2-k$ is proved for $k\le 11$ and only the lower half is proved for all $k$.

**Proposed formula.** $F(k)=k^2-k$ for all $k\ge1$, with no small-$k$ exceptions (proved equal to $D_B(T_k)$ here only for $k\le11$; for $k\ge12$ only $D_B(T_k)\ge F(k)$ is proved) ($F(1)=0$, $F(2)=2$, $F(3)=6$). Witness: $\lambda^{(1)}=(1)$ and, for $k\ge2$, $\lambda^{(k)}=(k-1,\,k-1,\,k-2,\,\dots,\,2,\,1,\,1)$, i.e. $\lambda^{(k)}_1=k-1$, $\lambda^{(k)}_i=k+1-i$ for $2\le i\le k$, $\lambda^{(k)}_{k+1}=1$.

Reading of the brief: "cyclic" and $d_B$ are exactly as in the statement; $\delta_{k-1}\subseteq\lambda$ means containment of Young diagrams; for $k=1$, $\delta_0$ is the empty partition.

---

## Notation

N1. For a partition $\lambda=(\lambda_1,\dots,\lambda_s)$ its diagram is $D(\lambda)=\{(i,j)\in\mathbb Z_{\ge1}^2: i\le s,\ j\le\lambda_i\}$. A finite set $D\subset\mathbb Z_{\ge1}^2$ is the diagram of a partition iff it is a Young diagram: $(i,j)\in D$, $i\ge2\Rightarrow(i-1,j)\in D$ and $(i,j)\in D$, $j\ge2\Rightarrow (i,j-1)\in D$. Distinct partitions have distinct diagrams.

N2. The *track* of a position $(i,j)$ is $i+j-1$. Track $d$ consists of the $d$ positions $(r,d+1-r)$, $r=1,\dots,d$; we call $(r,d+1-r)$ "row $r$ of track $d$". For a partition $\lambda$, a position of track $d$ is a *cell* if it lies in $D(\lambda)$ and a *hole* otherwise. Track $d$ is *full* if all its $d$ positions are cells.

N3. $\rho:\mathbb Z_{\ge1}^2\to\mathbb Z_{\ge1}^2$, $\rho(i,j)=(i+1,j-1)$ if $j\ge2$, $\rho(i,1)=(1,i)$. It is a bijection, with inverse $(i',j')\mapsto(i'-1,j'+1)$ if $i'\ge2$ and $(1,j')\mapsto(j',1)$.

N4. The energy of $\lambda$ is $E(\lambda)=\sum_{(i,j)\in D(\lambda)}(i+j-1)$.

## Part I: the shift in track coordinates

**Step 1 ($\rho$ preserves tracks and rotates each track).** For $j\ge2$: track of $(i+1,j-1)$ is $i+j-1$. For $j=1$: track of $(1,i)$ is $i$ = track of $(i,1)$. On track $d$: if $1\le r\le d-1$ then $\rho(r,d+1-r)=(r+1,d-r)$ = row $r+1$ of track $d$ (since $d+1-r\ge2$); and $\rho(d,1)=(1,d)$ = row $1$ of track $d$. So on track $d$, $\rho$ acts on row indices by $\sigma_d(r)=r+1$ ($r<d$), $\sigma_d(d)=1$. By induction on $t$, $\rho^t$ sends row $r$ of track $d$ to row $((r-1+t)\bmod d)+1$; in particular it is at row $1$ iff $r+t\equiv 1\pmod d$, and at row $2$ (when $d\ge2$) iff $r+t\equiv2\pmod d$.

**Step 2 (description of $B$).** Let $\lambda$ have $s$ parts and $R=\rho(D(\lambda))$. Row $1$ of $R$ is $\{(1,i):(i,1)\in D(\lambda)\}=\{(1,1),\dots,(1,s)\}$; for $1\le i\le s$, row $i+1$ of $R$ is $\{(i+1,j-1):2\le j\le\lambda_i\}=\{(i+1,1),\dots,(i+1,\lambda_i-1)\}$. So the row lengths of $R$ are $s,\lambda_1-1,\dots,\lambda_s-1$, whose positive members are, by definition, the parts of $B(\lambda)$.
Fix a column $j\ge1$ and put $c_j=\#\{i:\lambda_i\ge j+1\}$; since $\lambda$ is weakly decreasing, $\{i:\lambda_i\ge j+1\}=\{1,\dots,c_j\}$. Hence column $j$ of $R$ is $\{1\}\cup\{2,\dots,c_j+1\}$ if $j\le s$ and $\{2,\dots,c_j+1\}$ if $j>s$ (as sets of row indices). Column $j$ of $D(B(\lambda))$ is $\{1,\dots,h_j\}$ with $h_j=\#\{\text{parts of }B(\lambda)\ \ge j\}=[s\ge j]+c_j$. Therefore:
$D(B(\lambda))$ is obtained from $R$ by leaving every column $j\le s$ unchanged and moving every column $j>s$ up by one row, i.e. $(i,j)\mapsto(i-1,j)$ for $2\le i\le c_j+1$. A column $j$ actually changes iff $j>s$ and $c_j\ge1$, i.e. iff $(1,j)\notin R$ and $(2,j)\in R$. We call this the *compaction* of column $j$.

**Step 3 (compaction lowers tracks by one).** A compacted cell moves from $(i,j)$ to $(i-1,j)$, i.e. from track $i+j-1$ to track $i+j-2$. Positions not in compacted columns are unchanged.

**Step 4 (energy).** By Steps 1 and 3, $E(B(\lambda))=E(\lambda)-\sum_{j>s}c_j$. So $E(B(\lambda))\le E(\lambda)$, with equality iff no column is compacted iff $D(B(\lambda))=\rho(D(\lambda))$.

## Part II: $\delta_k$ is the only cyclic partition of $T_k$

**Step 5.** $D(\delta_k)=\{(i,j):i+j-1\le k\}$ = the union of tracks $1,\dots,k$, which contain $1+2+\dots+k=T_k$ positions. If $\lambda\vdash T_k$ and tracks $1..k$ are all full, then $D(\lambda)\supseteq D(\delta_k)$ and both have $T_k$ elements, so $\lambda=\delta_k$. Hence if $\lambda\ne\delta_k$ some track $d\le k$ has a hole; then tracks $1..k$ contain fewer than $T_k$ cells, so some cell lies on a track $>k$.

**Step 6 (tracks below a cell are non-empty).** If $(i,j)\in D(\lambda)$ has track $e\ge2$ then $(i,j-1)$ (if $j\ge2$) or $(i-1,j)$ (if $j=1$, so $i=e\ge2$) is in $D(\lambda)$ (Young diagram) and has track $e-1$. By induction, every track $1,\dots,e$ contains a cell.

**Step 7 ($\delta_k$ is fixed).** $\delta_k$ has $s=k$ parts; the positive numbers among $k-1,\dots,1,0$ are $k-1,\dots,1$; adding the part $k$ gives $\delta_k$. So $B(\delta_k)=\delta_k$ and $\delta_k$ is cyclic.

**Step 8 (uniqueness).** Let $\lambda\vdash T_k$ be cyclic, $B^p(\lambda)=\lambda$ with $p\ge1$. By Step 4, $E(\lambda)\ge E(B(\lambda))\ge\dots\ge E(B^p(\lambda))=E(\lambda)$, so all are equal, and the same holds for every step of the periodic orbit $(B^t(\lambda))_{t\ge0}$. By Step 4, $D(B^{t+1}\lambda)=\rho(D(B^t\lambda))$ for all $t$, hence $D(B^t\lambda)=\rho^t(D(\lambda))$. Suppose $\lambda\ne\delta_k$. By Step 5 choose the least track $d\le k$ having a hole, say at row $a$; there is a cell on a track $>k\ge d$, so by Step 6 track $d+1$ has a cell, say at row $b$. Since $\gcd(d,d+1)=1$, the Chinese remainder theorem gives $t\ge0$ with $a+t\equiv1\pmod d$ and $b+t\equiv1\pmod{d+1}$. As $\rho^t$ is a bijection preserving tracks (Steps 1, N3), holes go to holes: at time $t$ row $1$ of track $d$, i.e. $(1,d)$, is a hole, while row $1$ of track $d+1$, i.e. $(1,d+1)$, is a cell (Step 1). This contradicts the Young property of $D(B^t\lambda)$ ($(1,d+1)\in D\Rightarrow(1,d)\in D$). So $\lambda=\delta_k$.

**Step 9.** For any $\lambda\vdash T_k$ the sequence $B^i(\lambda)$ takes finitely many values, so $B^i(\lambda)=B^{j}(\lambda)$ for some $i<j$, and $B^i(\lambda)$ is cyclic. By Step 8 the cyclic partition reached is $\delta_k$, and $d_B(\lambda)=\min\{i\ge0:B^i(\lambda)=\delta_k\}$.

## Part III: the two-track region

**Step 10 (definition).** Let $\mathcal R_k=\{\lambda\vdash T_k:\ D(\delta_{k-1})\subseteq D(\lambda)\subseteq D(\delta_{k+1})\}$, i.e. tracks $1..k-1$ full and no cell on a track $\ge k+2$. For $\lambda\in\mathcal R_k$ let $H(\lambda)\subseteq\{1..k\}$ be the rows of the holes of track $k$ and $C(\lambda)\subseteq\{1..k+1\}$ the rows of the cells of track $k+1$. Counting cells, $T_k=T_{k-1}+(k-|H|)+|C|$, so $|H|=|C|$. Also $|H|=0$ iff $\lambda=\delta_k$ (Step 5 and $D(\delta_k)\subseteq D(\delta_{k+1})$).

**Step 11 (Young constraint).** If $i\in C(\lambda)$, the cell is $(i,k+2-i)$. If $i\le k$ then $(i,k+1-i)$ (row $i$ of track $k$) is a cell; if $i\ge2$ then $(i-1,k+2-i)$ (row $i-1$ of track $k$) is a cell. Hence for $h\in H(\lambda)$, $i\in C(\lambda)$: $i\ne h$ and $i\ne h+1$, i.e. $i-h\notin\{0,1\}$ (for $i=k+1$, $h\le k<i$; for $i=1$, $h\ge1$).

**Step 12 (dynamics in $\mathcal R_k$).** Let $\lambda\in\mathcal R_k$, $R=\rho(D(\lambda))$. By Step 1, tracks $1..k-1$ are full in $R$, tracks $\ge k+2$ are empty in $R$, and the holes of track $k$ in $R$ are at rows $\sigma_k(H)$, the cells of track $k+1$ at rows $\sigma_{k+1}(C)$. By Step 2 column $j$ is compacted iff $(1,j)\notin R$ and $(2,j)\in R$. $(1,j)$ has track $j$, so $j\ge k$; $(2,j)$ has track $j+1$, so $j+1\le k+1$. Thus only column $k$ can be compacted, and exactly when $1\in\sigma_k(H)$ and $2\in\sigma_{k+1}(C)$; then, since $(3,k)$ (track $k+2$) is not in $R$, compaction moves the single cell $(2,k)$ (row 2 of track $k+1$) to $(1,k)$ (row 1 of track $k$). Consequently $B(\lambda)\in\mathcal R_k$ and
$H(B\lambda)=\sigma_k(H)\setminus\{1\}$, $C(B\lambda)=\sigma_{k+1}(C)\setminus\{2\}$ if $1\in\sigma_k(H)$ and $2\in\sigma_{k+1}(C)$ (an *annihilation*), and $H(B\lambda)=\sigma_k(H)$, $C(B\lambda)=\sigma_{k+1}(C)$ otherwise.
In particular no hole of track $k$ and no cell of track $k+1$ is ever created: following positions by $\rho$, each hole (cell) at time $t+1$ is the image of a hole (cell) at time $t$, and at most one hole and one cell disappear per step.

**Step 13 (single-pair collision time).** Let $k\ge2$, $h\in\{1..k\}$, $i\in\{1..k+1\}$, $i-h\notin\{0,1\}$, and $\tau(h,i)=\min\{t\ge1: h+t\equiv1\ (\mathrm{mod}\ k),\ i+t\equiv2\ (\mathrm{mod}\ k+1)\}$. Write $t=1-h+kx$ (all solutions of the first congruence). Since $k\equiv-1\pmod{k+1}$, the second congruence becomes $1-h-x\equiv2-i$, i.e. $x\equiv i-h-1\pmod{k+1}$. Put $D=i-h\in[1-k,k]$, so $D-1\in[-k,k-1]\setminus\{-1,0\}$. Let $x_0$ be the least non-negative residue of $D-1$ mod $k+1$: if $D-1\in[1,k-1]$ then $x_0=D-1$; if $D-1\in[-k,-2]$ then $x_0=D+k\in[1,k-1]$. So $x_0\in[1,k-1]$ and the solutions are $t=1-h+k x_0+k(k+1)m$, $m\in\mathbb Z$. For $m=0$: $t\ge 1-k+k=1$. For $m\le-1$: $t\le 1-1+k(k-1)-k(k+1)<0$. Hence
$$\tau(h,i)=kx_0+1-h\le k(k-1)+0=k^2-k,$$
with equality iff $x_0=k-1$ and $h=1$. $x_0=k-1$ means $D=k$ (so $i=h+k$) or $D=-1$; with $h=1$ the second gives $i=0$, impossible. So equality holds iff $(h,i)=(1,k+1)$.

**Step 14 (upper bound on $\mathcal R_k$).** Let $\lambda\in\mathcal R_k$. If $\lambda=\delta_k$, $d_B=0\le k^2-k$. Otherwise $|H(\lambda)|\ge1$, which forces $k\ge2$, because for $k=1$ the only partition of $T_1=1$ is $(1)=\delta_1$. By Steps 9, 10, 12, $T:=d_B(\lambda)$ is the least $t$ with $H(B^t\lambda)=\emptyset$, and $T\ge1$. Since at most one hole disappears per step, at step $T$ an annihilation removes a hole $\eta$ and a cell $\gamma$. Following positions backwards via $\rho$ (Step 12: nothing is created), $\eta$ and $\gamma$ are the images of a hole at row $h_0$ of track $k$ and a cell at row $i_0$ of track $k+1$ at time $0$, both surviving up to step $T$. At step $T$, after rotation, $\eta$ is at row 1 and $\gamma$ at row 2, so (Step 1) $h_0+T\equiv1\pmod k$ and $i_0+T\equiv2\pmod{k+1}$. If some $1\le t<T$ satisfied the same congruences, then at step $t$ both $\eta,\gamma$ still exist and are at rows $1,2$ after rotation, so the annihilation of step $t$ (Step 12) would remove the unique hole at row 1, namely $\eta$, contradicting its survival until $T$. Hence $T=\tau(h_0,i_0)$. By Step 11, $i_0-h_0\notin\{0,1\}$, so Step 13 gives $d_B(\lambda)=T\le k^2-k$.

## Part IV: the lower bound (witness)

**Step 15.** $k=1$: $\lambda^{(1)}=(1)=\delta_1$ and $d_B=0=1^2-1$.
$k\ge2$: $\lambda^{(k)}=(k-1,k-1,k-2,\dots,1,1)$ is weakly decreasing, has positive parts, and sums to $(k-1)+T_{k-1}+1=T_k$. Its diagram is $D(\delta_k)\setminus\{(1,k)\}\cup\{(k+1,1)\}$: rows $2..k$ agree with $\delta_k$, row 1 lacks $(1,k)$, and row $k+1$ is $\{(k+1,1)\}$. $(1,k)$ is row 1 of track $k$ and $(k+1,1)$ is row $k+1$ of track $k+1$. Tracks $1..k-1$ lie in $D(\delta_k)\setminus\{(1,k)\}$ (since $(1,k)$ has track $k$), so they are full; no cell has track $\ge k+2$. So $\lambda^{(k)}\in\mathcal R_k$ with $H=\{1\}$, $C=\{k+1\}$. By Step 12, as long as no annihilation has occurred the state has exactly one hole and one cell, at rows $1+t$ (mod $k$) and $k+1+t$ (mod $k+1$) in the sense of Step 1, and $B^t\lambda^{(k)}\ne\delta_k$ (Step 10); the first annihilation happens at the first $t\ge1$ with $1+t\equiv1\pmod k$ and $k+1+t\equiv2\pmod{k+1}$, i.e. at $t=\tau(1,k+1)$ (Step 11 holds: $i-h=k\notin\{0,1\}$ as $k\ge2$). By Step 13, $\tau(1,k+1)=k(k-1)+1-1=k^2-k$. After it $H=\emptyset$, i.e. the state is $\delta_k$. By Step 9, $d_B(\lambda^{(k)})=k^2-k$.
Hence $D_B(T_k)\ge k^2-k$ for every $k\ge1$.

## Part V: the upper bound for arbitrary $\lambda\vdash T_k$

**Step 16 ($k=1,2$ by hand).** $k=1$: only $(1)$, $d_B=0$. $k=2$: $(2,1)=\delta_2$ ($d_B=0$); $B(3)=(2,1)$ ($d_B=1$); $B(1,1,1)=(3)$ ($d_B=2$). Max $=2=2^2-2$.

**Step 17 ($1\le k\le11$, computer-assisted).** For each $k\le 11$ the finite set to be checked is exactly the set of all partitions of $T_k$. `out/code/check_DB_triangular.py` enumerates them (the count is asserted equal to $p(T_k)$ from an independent dynamic program), iterates $B$ exactly on integer tuples until $\delta_k$, and finds $\max d_B=k^2-k$ for each $1\le k\le11$ (run: `python3 check_DB_triangular.py 1 11`, output ALL OK, 14.85 s). With Step 15 this proves $D_B(T_k)=k^2-k$ for $1\le k\le 11$.

**Step 18 (general $k$) [GAP].** We have NOT proved $d_B(\lambda)\le k^2-k$ for $\lambda\vdash T_k$ outside $\mathcal R_k$ when $k\ge12$. Steps 12–14 control the evolution only once the orbit is in $\mathcal R_k$ (which it enters, since $\delta_k\in\mathcal R_k$), but the orbit may spend up to $T_{k-1}$ steps outside $\mathcal R_k$ (observed for $k\le8$), and the pair that is annihilated last can be formed after time 0; the naive bound "entry time $+\ (k^2-k)$" is too weak, and the invariant "$t+\max\tau(\text{pairs at time }t)\le k^2-k$" is false (numerically refuted, see `out/stuck.md`). A proof of the general upper bound needs an argument controlling the phases of holes/cells that arrive on tracks $k,k+1$ after time 0.

## Summary of what is established

- $\delta_k$ is the unique cyclic partition of $T_k$, for all $k\ge1$ (Steps 7–9).
- Lower bound $D_B(T_k)\ge k^2-k$ for all $k\ge1$, with explicit witness $\lambda^{(k)}$ and $d_B(\lambda^{(k)})=k^2-k$ exactly (Step 15).
- Upper bound $d_B(\lambda)\le k^2-k$ for all $\lambda\in\mathcal R_k$, all $k\ge1$ (Step 14).
- $D_B(T_k)=k^2-k$ for $1\le k\le 11$ (Steps 15–17).
- NOT established: the upper bound for arbitrary $\lambda\vdash T_k$, $k\ge12$ [GAP, Step 18]. Consequently $D_B(T_k)=k^2-k$ for all $k$ is NOT proved here.

## Checklist G (self-review)

- G1: the statement proved is stated in the first line; it is weaker than the target (upper bound for general $\lambda$ and $k\ge12$ missing), and this is said explicitly.
- G2: every step is justified from definitions, earlier steps, or the Chinese remainder theorem.
- G3: $k=1$ and $k=2$ handled separately (Steps 14, 15, 16); the witness formula is checked for $k=2$ ($(1,1,1)$).
- G4: energy monotonicity (Step 4) is exact; strictness is not needed beyond Step 8; closure of $\mathcal R_k$ proved (Step 12).
- G5: the witness is proved for every $k\ge1$ (Step 15).
- G6: no circularity; no literature cited.
- G7: computation exact, exhaustive over all partitions of $T_k$ for $k\le 11$, completeness asserted against $p(T_k)$, 14.85 s; it proves nothing for $k\ge12$.
- G8: no cited results; only the Chinese remainder theorem (standard).
- G9: established / not established listed in the Summary and first line.
