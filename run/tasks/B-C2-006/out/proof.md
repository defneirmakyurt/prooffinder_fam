We prove: (a) for every $k\ge1$, $\delta_k$ is the unique cyclic partition of $T_k$ and $d_B(\lambda)=\min\{i\ge0:B^i\lambda=\delta_k\}$; (b) for every $k\ge1$, $d_B(\lambda)\le k^2-k$ for every $\lambda\vdash T_k$ with $D(\delta_{k-1})\subseteq D(\lambda)\subseteq D(\delta_{k+1})$; (c) for $1\le k\le 11$, $d_B(\lambda)\le k^2-k$ for every $\lambda\vdash T_k$ (computer-assisted, exhaustive); (d) the shift is monotone for diagram inclusion ($D(\lambda)\subseteq D(\mu)\Rightarrow D(B\lambda)\subseteq D(B\mu)$, any sizes), and in conjugate coordinates $B$ is the queue map $(B\lambda)'_j=\lambda'_{j+1}+[j\le\lambda'_1]$. NOT established: $d_B(\lambda)\le k^2-k$ for arbitrary $\lambda\vdash T_k$ when $k\ge12$ [GAP, Step 24].

**Reading of the brief.** The brief's TARGET line names `run/B/C2/target_upper.md`, which is outside my readable area; the inbox holds `target.md` (the full C2 target). I read the task as its UPPER half: prove $d_B(\lambda)\le F(k)$ with $F(k)=k^2-k$ for every $\lambda\vdash T_k$ and every $k\ge1$ (the formula $F(k)=k^2-k$ is the one of the subject B-C2-002). The ASSUMPTIONS line allows the Cell 1 facts; Part II below proves the one we use anyway. EXPLOIT: the subject's listed problem is its Step 18 (general $\lambda$, $k\ge12$). This report does **not** close it; it adds Part IV (monotonicity and the queue form, new, fully proved) and reduces the open part to a precise statement (Step 24).

Steps 1–14 below are the subject's Parts I–III, re-checked line by line and kept verbatim (they are correct as written; "time $t$" means the partition $B^t\lambda$ and "step $t$" the passage from $B^{t-1}\lambda$ to $B^t\lambda$). $\delta_0$ is the empty partition.

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


## Part IV (new): monotonicity and the queue form of $B$

For a partition $\lambda$ (the empty partition allowed, with $B(\emptyset)=\emptyset$), let $\lambda'_j=\#\{i:\lambda_i\ge j\}$ ($j\ge1$) be the height of column $j$ of $D(\lambda)$; $\lambda'_1=s$ is the number of parts. $D(\lambda)=\{(i,j): i\le\lambda'_j\}$, so $D(\lambda)\subseteq D(\mu)$ iff $\lambda'_j\le\mu'_j$ for all $j\ge1$.

**Step 19 (conjugate formula).** For every partition $\lambda$ and every $j\ge1$: $(B\lambda)'_j=\lambda'_{j+1}+[\,j\le\lambda'_1\,]$.
Proof. By definition the parts of $B\lambda$ are the number $s=\lambda'_1$ together with the positive numbers among $\lambda_i-1$. For $j\ge1$ the number of parts of $B\lambda$ that are $\ge j$ is therefore $[s\ge j]+\#\{i:\lambda_i-1\ge j\}=[j\le\lambda'_1]+\#\{i:\lambda_i\ge j+1\}=[j\le\lambda'_1]+\lambda'_{j+1}$ (a part $\lambda_i-1\ge j\ge1$ is automatically positive, so discarding zeros does not affect the count). $\square$

**Step 20 (monotonicity).** If $D(\lambda)\subseteq D(\mu)$ (sizes may differ) then $D(B\lambda)\subseteq D(B\mu)$; hence $D(B^t\lambda)\subseteq D(B^t\mu)$ for all $t\ge0$.
Proof. $\lambda'_j\le\mu'_j$ for all $j$. Then $\lambda'_{j+1}\le\mu'_{j+1}$, and $[j\le\lambda'_1]\le[j\le\mu'_1]$ because $\lambda'_1\le\mu'_1$. By Step 19, $(B\lambda)'_j\le(B\mu)'_j$ for all $j$, i.e. $D(B\lambda)\subseteq D(B\mu)$. Induction on $t$ gives the second claim. $\square$

**Step 21 (persistence).** For every $m\ge0$ and every partition $\lambda$: if $D(\delta_m)\subseteq D(\lambda)$ then $D(\delta_m)\subseteq D(B^t\lambda)$ for all $t$; if $D(\lambda)\subseteq D(\delta_m)$ then $D(B^t\lambda)\subseteq D(\delta_m)$ for all $t$.
Proof. $B\delta_m=\delta_m$ (Step 7 for $m\ge1$; $B(\emptyset)=\emptyset$), so $B^t\delta_m=\delta_m$; apply Step 20 to the pair $(\delta_m,\lambda)$, resp. $(\lambda,\delta_m)$. $\square$
Consequence: $\mathcal R_k$ is $B$-invariant (a second proof of this part of Step 12), and for $\lambda\vdash T_k$ the times $f_m(\lambda)=\min\{t: D(\delta_m)\subseteq D(B^t\lambda)\}$ satisfy $f_1\le f_2\le\dots\le f_k=d_B(\lambda)$ (for $f_k$: $D(\delta_k)\subseteq D(B^t\lambda)$ with equal sizes means $B^t\lambda=\delta_k$; Steps 9, 21).

**Step 22 (queue form around $\delta_k$).** Fix $k\ge1$ and write $e_j(\lambda)=\lambda'_j-(k+1-j)_+$ ($j\ge1$), where $x_+=\max(x,0)$; note $(\delta_k)'_j=(k+1-j)_+$. Then for every partition $\lambda$ and every $j\ge1$,
$$e_j(B\lambda)=e_{j+1}(\lambda)+[\,j\le k+e_1(\lambda)\,]-[\,j\le k\,].$$
Proof. By Step 19, $e_j(B\lambda)=\lambda'_{j+1}+[j\le\lambda'_1]-(k+1-j)_+=e_{j+1}(\lambda)+(k-j)_+ +[j\le\lambda'_1]-(k+1-j)_+$. For integers, $(k+1-j)_+-(k-j)_+=[j\le k]$, and $\lambda'_1=k+e_1(\lambda)$. $\square$
Reading: the sequence $e$ is shifted one place to the left; the discarded head value $v=e_1$ is re-inserted as $+1$ on positions $k+1,\dots,k+v$ if $v>0$, or as $-1$ on positions $k+v+1,\dots,k$ if $v<0$. For $\lambda\vdash T_k$, $\sum_j e_j=0$, and $\lambda=\delta_k$ iff $e\equiv0$. The Young (weakly decreasing) condition on $\lambda'$ reads $e_{j+1}\le e_j+[j\le k]$ for all $j\ge1$; with $\lambda'_j\ge0$ this forces $e_j\ge0$ for $j\ge k+1$. So negative units live only on positions $1..k$ and recur with period $\le k$; positive units recur with period $\ge k+1$; units of opposite sign cancel when a negative unit is re-inserted on a position holding a positive one. (Step 22 is proved; this reading is only a paraphrase of it.)

**Step 23 (sandwich, used only in stuck.md).** If $D(\lambda^-)\subseteq D(\lambda)\subseteq D(\lambda^+)$ then $D(B^t\lambda^-)\subseteq D(B^t\lambda)\subseteq D(B^t\lambda^+)$ for all $t$ (Step 20 twice).

## Part V: the upper bound, what is and is not proved

**Step 23a ($k=1,2$ by hand).** $k=1$: only $(1)=\delta_1$, $d_B=0=1^2-1$. $k=2$: $(2,1)=\delta_2$ ($d_B=0$); $B(3)=(2,1)$ ($d_B=1$); $B(1,1,1)=(3)$, so $d_B(1,1,1)=2$. All are $\le 2=2^2-2$.

**Step 23b ($1\le k\le11$, computer-assisted).** The finite set to be checked for a given $k$ is exactly the set of all partitions of $T_k$, since the claim is "$d_B(\lambda)\le k^2-k$ for every $\lambda\vdash T_k$". `out/code/check_DB_triangular.py` (stdlib, exact integer tuples; copied unchanged from the subject) enumerates all of them, asserts that the count equals $p(T_k)$ computed by an independent dynamic program, iterates $B$ until $\delta_k$ (reporting failure if a cycle avoiding $\delta_k$ occurs), and prints $\max d_B$. Run by me: `/usr/bin/time -p python3 check_DB_triangular.py 1 11` $\to$ `ALL OK`, $\max d_B=k^2-k$ for each $1\le k\le 11$, real 40.57 s. Hence $d_B(\lambda)\le k^2-k$ for all $\lambda\vdash T_k$, $1\le k\le11$.

**Step 24 (general $\lambda$, $k\ge12$) [GAP].** Not proved: $d_B(\lambda)\le k^2-k$ for every $\lambda\vdash T_k$ with $k\ge 12$ and $\lambda\notin\mathcal R_k$. By Steps 21–22 it would suffice to prove, in the queue form of Step 22, that every configuration $e$ satisfying the Young condition $e_{j+1}\le e_j+[j\le k]$, $e_j\ge-(k+1-j)_+$, $\sum e_j=0$ reaches $e\equiv0$ within $k^2-k$ steps. In the one-pair case ($e$ = one $+1$ and one $-1$) this is exactly Steps 13–14; for several units the re-insertion spreads ($+1$'s to $k+1,\dots,k+v$, $-1$'s to $k+v+1,\dots,k$) change the recurrence periods, and I have no proof that the last cancellation occurs by time $k^2-k$. See `out/stuck.md`.

## Summary of what is established

- $\delta_k$ is the unique cyclic partition of $T_k$, all $k\ge1$ (Steps 5–9).
- $d_B(\lambda)\le k^2-k$ for every $\lambda\in\mathcal R_k$, all $k\ge1$ (Step 14).
- $d_B(\lambda)\le k^2-k$ for every $\lambda\vdash T_k$, $1\le k\le 11$ (Steps 23a–23b; computer-assisted, exhaustive).
- New: monotonicity of $B$ for diagram inclusion (Step 20), persistence of $\delta_m\subseteq\cdot$ and $\cdot\subseteq\delta_m$ (Step 21), exact queue form of $B$ around $\delta_k$ (Step 22).
- NOT established: the upper bound for arbitrary $\lambda\vdash T_k$ with $k\ge12$ [GAP, Step 24]. The target's upper half is therefore NOT proved for all $k$.

## Checklist G (self-review)

- G1: the first line states exactly what is proved; it is weaker than the target (general $\lambda$, $k\ge12$ missing) and says so.
- G2: Steps 19–22 are derived from the definition of $B$ with every identity written out; Steps 1–14 were re-checked (Step 12's claim that only column $k$ can be compacted uses that $(1,j)\notin R$ forces track $j\ge k$ and $(2,j)\in R$ forces $j+1\le k+1$; correct).
- G3: $k=1,2$ by hand (Step 23a); the empty partition is allowed in Steps 19–21 with $B(\emptyset)=\emptyset$ (Step 19 then reads $0=0+0$).
- G4: monotonicity is an inequality between column heights, no strictness needed; persistence uses $B\delta_m=\delta_m$.
- G5: no construction (the lower bound is not part of this task).
- G6: no circularity; Step 23b is a finite check over exactly the set it claims.
- G7: exact integer computation, completeness asserted against $p(T_k)$, 40.57 s measured; proves nothing for $k\ge12$.
- G8: no literature cited; only the Chinese remainder theorem (Step 8) and elementary counting.
- G9: established / not established listed above.
