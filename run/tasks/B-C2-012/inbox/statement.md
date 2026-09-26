# Problem B: Bulgarian solitaire — verbatim statement

Source: sources/problem_description_bulgarian_solitaire.tex (official). Copied from skill problem-bulgarian-solitaire §1.


Repeatedly take one card from every pile and form a new pile. How many moves can it take before the piles start to cycle?

**Definition (Partition).** A *partition* of a positive integer \(n\) is a weakly decreasing sequence
\[
\lambda=(\lambda_1,\ldots,\lambda_s)
\]
of positive integers with
\[
\lambda_1+\cdots+\lambda_s=n.
\]
Think of it as a division of \(n\) cards into \(s\) piles.

**Definition (Shift).** The *shift* \(B(\lambda)\) is the partition of \(n\) obtained as follows: remove one card from every pile, discard the piles that become empty, and add one new pile consisting of the \(s\) removed cards. Formally, \(B(\lambda)\) is the partition whose parts are the positive numbers among
\[
\lambda_1-1,\;\ldots,\;\lambda_s-1
\]
together with one extra part equal to \(s\).

Iterating \(B\) from any starting partition must eventually repeat, since there are finitely many partitions of \(n\).

**Definition (Cyclic partitions and time to cycle).** Call \(\lambda\) *cyclic* if
\[
B^i(\lambda)=\lambda\qquad\text{for some } i\ge 1,
\]
and let
\[
\begin{aligned}
d_B(\lambda)&=\min\{\,i\ge 0: B^i(\lambda)\text{ is cyclic}\,\},\\
D_B(n)&=\max\{\,d_B(\lambda):\lambda\text{ is a partition of } n\,\}.
\end{aligned}
\]
Thus \(D_B(n)\) is the largest number of shifts that can be needed before the process starts to cycle.

**Notation (Triangular numbers and rank).** Write
\[
T_k=\frac{k(k+1)}{2},\qquad \delta_k=(k,k-1,\ldots,2,1),
\]
the partition of \(T_k\) into distinct parts. Every \(n\ge 1\) satisfies
\[
T_{k-1}<n\le T_k
\]
for exactly one \(k\), which we call the *rank* of \(n\).

**Example.**
\[
\begin{aligned}
B\bigl((2,1,1,1,1)\bigr)&=(5,1),\\
B\bigl((5,1)\bigr)&=(4,2),\\
B\bigl((4,2)\bigr)&=(3,2,1),\\
B\bigl((3,2,1)\bigr)&=(3,2,1).
\end{aligned}
\]
Here \(d_B\bigl((2,1,1,1,1)\bigr)=3\).

### Cells

| Cell | Title | Points | Checking |
|---|---|---|---|
| C1 | Cyclic Partitions and Cycles | 1 | written proof |
| C2 | \(D_B\) at Triangular \(n\) | 2 | written proof |
| C3 | A General Upper Bound | 3 | written proof |
| C4 | One Above a Triangular Number | 5 | written proof |
| C5 | Two Above a Triangular Number | 8 | written proof |
| C6 | \(D_B(n)\) for Every \(n\) | 13 | **open question** |

**C1: Cyclic Partitions and Cycles (verbatim).** First, the long-run behaviour: which partitions repeat under the shift, and how they fall into cycles. Let \(n=T_k\). Prove that for every partition \(\lambda\) of \(n\) there is an \(i\) with \(B^i(\lambda)=\delta_k\), and that \(\delta_k\) is the only cyclic partition of \(n\). Then let \(n\) be arbitrary of rank \(k\), say \(n=T_{k-1}+r\) with \(1\le r\le k\): determine all cyclic partitions of \(n\), and determine the number of distinct cycles of \(B\) on the partitions of \(n\). Prove both.

**C2: \(D_B\) at Triangular \(n\) (verbatim).** Next, how long the process can take to reach a cycle, starting with the triangular numbers. Determine
\[
D_B(T_k)
\]
for every \(k\), with proof of both bounds.

**C3: A General Upper Bound (verbatim).** Now the numbers strictly between two consecutive triangular numbers.
- (a) Prove that for every \(k\ge 4\) and every non-triangular \(n\) with \(T_{k-1}<n<T_k\),
\[
D_B(n)\le k^2-2k-1.
\]
- (b) Determine \(D_B(T_k-1)\) exactly.
- (c) Determine also, for that \(n\), which partitions attain the maximum.

**C4: One Above a Triangular Number (verbatim).** The first family just above a triangular number:
\[
n=T_{k-1}+1,
\]
that is,
\[
n=11,16,22,29,\ldots\qquad\text{for } k=5,6,7,8,\ldots.
\]
Determine
\[
D_B(T_{k-1}+1)
\]
for every \(k\ge 5\), with proof of both bounds.

**C5: Two Above a Triangular Number (verbatim).** The next family:
\[
n=T_{k-1}+2,
\]
that is,
\[
n=3,5,8,12,17,23,\ldots\qquad\text{for } k=2,3,4,5,6,7,\ldots.
\]
Determine
\[
D_B(T_{k-1}+2)
\]
for every \(k\), with proof of both bounds.
- State exactly for which \(k\) your formula holds, and give the remaining values separately.
- Your upper bound must be a single argument valid for all \(k\) in that range, not a separate treatment of each \(k\).
- You must give the extremal partitions explicitly as a function of \(k\).
- Say also where the straightforward extension of the Cell 3 argument stops: give the bound it does yield, show it is strictly weaker than the truth, and identify precisely what your proof supplies in its place.

**C6: \(D_B(n)\) for Every \(n\) (verbatim).** **Open question.** Finally, the whole function
\[
n\longmapsto D_B(n).
\]
Determine \(D_B(n)\) for every \(n\).

