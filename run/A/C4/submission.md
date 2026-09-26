# Submission: Cell 4, "Five Lines in R^3, Six in R^4" (5 points)

**Cell status: SOLVED.**
**Claim status: PROVED** (both instances, (a) and (b)).

Everything mathematical in this document comes from the team's accepted artefacts `proof.md` and `claims.md`, pinned by `MANIFEST.sha256`. All three files ship unchanged in `submission/`. The Scribe added no mathematics and did not edit the proof. Section 4 reproduces it byte for byte.

---

## 1. Statement (verbatim)

The cell as it appears in the problem description (LaTeX source, unchanged):

```latex
\cell{4}{Five Lines in $\R^3$, Six in $\R^4$}{5 points}
% ===================================================================

Two concrete instances of the next case, $N = d + 2$: five lines in
three dimensions and six lines in four. In each, the conjectured
optimum repeats two of the coordinate axes.

Prove that any $5$ lines in $\R^3$ satisfy
\[
  S \leq 4\pi,
\]
and that any $6$ lines in $\R^4$ satisfy
\[
  S \leq \frac{13\pi}{2}.
\]
```

The definitions the cell relies on, from the same document (unchanged):

```latex
\begin{definition}[Lines and angles]
A \emph{line} here always means a line through the origin of $\R^d$.
The \emph{angle} between two lines $\ell, \ell'$ is the acute
(non-obtuse) angle
\[
  \theta(\ell, \ell') \in [0, \pi/2]
\]
between them. If $\ell, \ell'$ are spanned by unit vectors $x, x'$,
then
\[
  \theta(\ell, \ell') = \arccos \bigl| \langle x, x' \rangle \bigr|.
\]
\end{definition}

\begin{definition}[Angle sum]
For lines $\ell_1, \ldots, \ell_N$ in $\R^d$ (repetitions allowed),
write
\[
  S(\ell_1, \ldots, \ell_N)
  = \sum_{1 \leq i < j \leq N} \theta(\ell_i, \ell_j).
\]
\end{definition}
```

The general requirement that applies to every cell, from the same document (unchanged):

```latex
Each cell below asks you to prove this bound, or a special case of
it. Unless a cell says otherwise, you need a complete proof. Citing a
published result for the statement you are asked to prove does not
count.
```

The hand-in rules, from the same document (unchanged):

```latex
\section*{What to Hand In}
% ===================================================================

For each cell you attempt, hand in a written proof.

\begin{itemize}[leftmargin=*]
  \item \textbf{Computation.}
    You may use a computer to explore. A proof may rely on a
    computation only if you include the code, it runs in under
    10 minutes on a laptop, and it is rigorous: exact or interval
    arithmetic, or an argument that bounds the numerical error.
  \item \textbf{Status.}
    Say clearly which cells you consider solved and which are
    partial.
\end{itemize}
```

The exact target proved, as fixed for the team (unchanged):

> Prove BOTH: (a) any 5 lines through the origin of R^3 (repetitions allowed) satisfy S <= 4*pi; (b) any 6 lines through the origin of R^4 (repetitions allowed) satisfy S <= 13*pi/2. Here S = sum over pairs i<j of theta(l_i, l_j), with theta(l, l') = arccos |<x, x'>| for spanning unit vectors (the acute angle, in [0, pi/2]). A computer-assisted step is allowed only with code included, runtime under 10 minutes on a laptop, exact or interval arithmetic (or a proved bound on the numerical error), and a written argument explaining why the computation proves the claim.

---

## 2. Status

- **Cell status:** SOLVED
- **Claim status:** PROVED

Both required inequalities are proved, for every configuration of lines. Repetitions are allowed and the lines may span any subspace (`claims.md`, rows (a) and (b); `proof.md`, 9.3 and 10.1):

- (a) any 5 lines in R^3 satisfy S <= 4pi. PROVED (`proof.md`, Steps 0-9, conclusion in 9.3).
- (b) any 6 lines in R^4 satisfy S <= 13pi/2. PROVED (`proof.md`, Steps 0-9, conclusion in 9.3).

No step of the proof relies on a computer (`proof.md`, 10.1).

---

## 3. Cited vs. ours

**Cited.** No published result is cited, and no problem-specific result is cited. In particular, nothing is cited for the statement being proved. The proof uses only the textbook tools listed in `proof.md`, lines 6-9:

- the extreme value theorem on a compact set;
- the intermediate value theorem;
- the rank of a Gram matrix equals the dimension of the span of the vectors;
- a function that is continuous on a closed interval and has non-positive second derivative inside is concave;
- a concave function lies above its chords;
- elementary trigonometric identities.

(`proof.md` 4.2 also includes its own proof of the fact that a graph of maximum degree <= 2 has components that are vertices, paths or cycles.)

**Ours.** The whole argument, `proof.md` Steps 0-9, is the team's own work. The header of `claims.md` attributes it to task A-C4-003. Its components, as listed in `claims.md`:

| claim | status | where proved (file, step) |
|---|---|---|
| (a) any 5 lines in R^3 satisfy S <= 4pi | PROVED | proof.md, Steps 0-9 (9.3) |
| (b) any 6 lines in R^4 satisfy S <= 13pi/2 | PROVED | proof.md, Steps 0-9 (9.3) |
| Reformulation: target iff D = sum_{i<j} arcsin\|<x_i,x_j>\| >= pi for N = d+2, d in {3,4} | PROVED | proof.md, Step 0 |
| R1: S attains its max; a maximizer with the most orthogonal pairs exists | PROVED | proof.md, Step 1 |
| R2 (Lemma T): arcsin(alpha cos s + beta sin s) concave where the argument is >= 0 (amplitude <= 1) | PROVED | proof.md, Step 2 |
| R3 (Lemma A): at that maximizer each x_k is orthogonal to all others, or its orthogonal partners span x_k^perp | PROVED | proof.md, Step 3 |
| R4: non-orthogonality graph G' has max degree <= N-d = 2; components are vertices, paths, cycles | PROVED | proof.md, Step 4 |
| R5a: dim U_K <= m_K - deg(k) for any non-isolated vertex k of component K | PROVED | proof.md, 5.1 |
| R5b: tridiagonal Gram with nonzero off-diagonal has rank >= m-1 | PROVED | proof.md, 5.2 |
| R5c: components are isolated vertices, coincident pairs, or cycles with dim U_K = m-2, m <= d+2 | PROVED | proof.md, 5.3 |
| R6: 3-cycle (dim 1) has D = 3pi/2; 4-cycle (dim 2) has D = pi | PROVED | proof.md, Step 6 |
| R7: 5-cycle spanning a 3-space has sum of consecutive arcsin\|.\| >= pi | PROVED | proof.md, Step 7 |
| R8: 6-cycle spanning a 4-space has sum of consecutive arcsin\|.\| >= pi | PROVED | proof.md, Step 8 |
| R9: assembly D >= sum_K e_K pi/2 >= (N-d) pi/2 = pi | PROVED | proof.md, Step 9 |
| Sharpness: e1,e1,e2,e2,e3 and e1,e1,e2,e2,e3,e4 attain the bounds | PROVED | proof.md, 10.2 |
| Floating-point sanity: formulas of Steps 7-8 match sampled cycles; hill-climbing never exceeds bounds | CHECKED (evidence only, not load-bearing) | code/check_cycles.py, code/random_search.py |
| Symbolic re-check of hand identities in Steps 2, 7 | CHECKED (support only; hand derivations are in proof.md) | code/check_identities.py |

The inbox shipped to this Scribe task contains no literature-search record. This document therefore makes no statement about whether this argument, or parts of it, appear in the literature.

---

## 4. Proof

The accepted proof is reproduced below byte for byte, including the team's internal step labels ("rung R1" ... "rung R9") and one reference to a code folder (see Section 6). Section 5 gives a stdlib-only command that checks this block is identical to the pinned `proof.md`.

Reading guide. The step map is `claims.md`, reproduced in Section 3. The logical order is:

- Step 0 reduces both inequalities to (*): D(x) = sum_{i<j} arcsin|<x_i,x_j>| >= pi.
- Steps 1-3 pick a maximiser with the most orthogonal pairs and derive its local structure (Lemma A).
- Steps 4-5 show every component of that maximiser's non-orthogonality graph is an isolated vertex, a coincident pair, or a cycle of length m <= 6 whose span has dimension m - 2.
- Steps 6-8 prove D(K) >= pi for such cycles with m = 3, 4, 5, 6.
- Step 9 assembles the pieces.

<!-- BEGIN EMBEDDED proof.md -->
````text
Any 5 lines through the origin of R^3 (repetitions allowed) satisfy S <= 4*pi, and any 6 lines through the origin of R^4 (repetitions allowed) satisfy S <= 13*pi/2.

(Reading of the statement: none needed. Lines may coincide and may span a proper subspace;
theta(l,l') = arccos|<x,x'>| in [0, pi/2] for spanning unit vectors x, x'.)

Tools used (all textbook): extreme value theorem on a compact set; intermediate value theorem;
rank of a Gram matrix equals the dimension of the span of the vectors; a function continuous on
a closed interval with non-positive second derivative inside is concave; a concave function lies
above its chords; elementary trigonometric identities. No problem-specific result is cited.

---------------------------------------------------------------------------------------------------

## 0. Reformulation

0.1. For unit vectors x, y put phi(x,y) := arcsin|<x,y>| in [0, pi/2]. Since arccos t + arcsin t = pi/2
for t in [0,1], theta(x,y) = pi/2 - phi(x,y). Note phi(x,y) = 0 iff x is orthogonal to y, and
phi(x,y) = pi/2 iff x = +-y.

0.2. For unit vectors x_1..x_N put D(x) := sum_{i<j} phi(x_i,x_j). Then
S = C(N,2) pi/2 - D(x).
For (N,d) = (5,3): C(5,2) pi/2 - pi = 5pi - pi = 4pi. For (N,d) = (6,4): C(6,2) pi/2 - pi = 15pi/2 - pi = 13pi/2.
So both claims are equivalent to:

  (*) for d in {3,4} and N = d+2, every N unit vectors x_1..x_N in R^d satisfy D(x) >= pi.

Every family of lines is given by unit vectors spanning them, and S depends only on the lines,
so (*) proves both claims. Throughout, N = d + 2 and d in {3,4}; Steps 1-5 use only N = d+2.

## 1. A convenient maximizer (rung R1)

1.1. X := (S^{d-1})^N is compact and S(x) = sum_{i<j} arccos|<x_i,x_j>| is continuous on X
(composition of continuous maps). By the extreme value theorem S attains a maximum value M on X.
The set of maximizers is nonempty.

1.2. For x in X let omega(x) be the number of pairs i<j with <x_i,x_j> = 0; it is an integer in
[0, C(N,2)]. Choose a maximizer x with omega(x) as large as possible among all maximizers.
Fix this x for Steps 3-9.

## 2. A concavity lemma (rung R2)

Lemma T. Let alpha, beta be real, A := sqrt(alpha^2 + beta^2) <= 1, g(s) := alpha cos s + beta sin s,
and let I be a closed bounded interval.
 (i) If A < 1 and g >= 0 on I, then psi := arcsin o g is concave on I.
 (ii) If A = 1, g >= 0 on I and g > 0 on the interior of I, then psi := arcsin o g is concave on I.

Proof. (i) |g(s)| <= A < 1 for all s (Cauchy-Schwarz in R^2), so psi is twice differentiable on R,
with psi' = g'/(1-g^2)^{1/2} and
  psi'' = [g''(1-g^2) + g (g')^2] / (1-g^2)^{3/2}.
Here g'' = -g and g^2 + (g')^2 = (alpha cos s + beta sin s)^2 + (-alpha sin s + beta cos s)^2 = A^2. Hence
  psi'' = g (g^2 + (g')^2 - 1) / (1-g^2)^{3/2} = g (A^2 - 1) / (1-g^2)^{3/2},
which is <= 0 wherever g >= 0, in particular on I. So psi is concave on I.
(ii) Write alpha = cos sigma, beta = sin sigma, so g(s) = cos(s - sigma). The zeros of cos are the
points pi/2 + k pi (k integer), and between two consecutive zeros cos has constant sign; it is
positive exactly on the intervals (2 pi n - pi/2, 2 pi n + pi/2). The open interval int(I) - sigma
contains no zero of cos (cos > 0 there), so it lies inside one such interval, and therefore
I - sigma is contained in [2 pi n - pi/2, 2 pi n + pi/2] for one integer n. For r in that interval put
r' = r - 2 pi n in [-pi/2, pi/2]; then cos r = cos r' = sin(pi/2 - |r'|) with pi/2 - |r'| in [0, pi/2],
so arcsin(cos r) = pi/2 - |r'|. Hence psi(s) = pi/2 - |s - sigma - 2 pi n| on I, which is concave
(minus the absolute value of an affine function). QED

## 3. Local structure of the maximizer (rung R3)

Lemma A. For every k in {1..N}, with J_k := { j != k : <x_j,x_k> = 0 }, one of the following holds:
 (i) J_k = {1..N} \ {k}, i.e. x_k is orthogonal to every other x_j;
 (ii) span{ x_j : j in J_k } = x_k^perp (a subspace of dimension d-1); in particular |J_k| >= d-1.

Proof. Fix k. Let R := {1..N} \ ({k} u J_k) (the j != k with <x_j,x_k> != 0) and
L := { y in R^d : <y,x_j> = 0 for all j in J_k } = (span{x_j : j in J_k})^perp. Then x_k is in L.
Suppose R is nonempty and dim L >= 2; we derive a contradiction.

3.1. Since dim L >= 2 there is a unit vector w in L with <w,x_k> = 0. Put x(s) := cos s x_k + sin s w
(s real). Each x(s) is a unit vector (x_k, w orthonormal) and lies in L.

3.2. For j in R let eps_j := sign<x_k,x_j> in {+1,-1} and g_j(s) := eps_j <x(s),x_j>
= eps_j<x_k,x_j> cos s + eps_j<w,x_j> sin s. Its amplitude A_j = (<x_k,x_j>^2 + <w,x_j>^2)^{1/2}
satisfies 0 < A_j <= |x_j| = 1 (Bessel's inequality for the orthonormal pair x_k, w).
g_j(0) = |<x_k,x_j>| > 0 and g_j(pi) = g_j(-pi) = -g_j(0) < 0.

3.3. By the intermediate value theorem each g_j has a zero in (0, pi); the zero set of g_j in [0, pi] is
closed, nonempty and does not contain 0, so it has a least element, which is > 0. Let s_+ be the least
of these least elements over j in R (R is finite). On the negative side: g_j(0) > 0 > g_j(-pi), so by
the intermediate value theorem each g_j has a zero in (-pi, 0); the zero set of g_j in [-pi, 0] is closed,
nonempty and does not contain 0, so it has a largest element, which is < 0; let s_- be the largest of
these largest elements over j in R. Put I := [s_-, s_+]; 0 lies in the interior of I. By construction no g_j
vanishes on (s_-, s_+), and g_j(0) > 0, so (intermediate value theorem) g_j > 0 on (s_-, s_+), and
g_j >= 0 on I by continuity. Moreover some j* in R has g_{j*}(s_+) = 0.

3.4. Let Phi(s) := sum_{j != k} arccos|<x(s),x_j>|. For j in J_k, <x(s),x_j> = 0 (x(s) in L), so the
term is pi/2. For j in R and s in I, |<x(s),x_j>| = g_j(s), so the term is pi/2 - arcsin(g_j(s)).
By Lemma T (case (i) if A_j < 1, case (ii) if A_j = 1; hypotheses verified in 3.2-3.3), each
s -> arcsin(g_j(s)) is concave on I. Hence Phi is convex on I.

3.5. Replacing x_k by x(s) changes only the pairs containing k, so the new configuration has angle sum
S(x) - Phi(0) + Phi(s). Since x is a maximizer, Phi(s) <= Phi(0) for all s. Let s in I, s != 0, and
let s' := s_+ if s < 0, s' := s_- if s > 0. Then 0 = lambda s + (1-lambda) s' for some lambda in (0,1),
and convexity gives Phi(0) <= lambda Phi(s) + (1-lambda) Phi(s') <= lambda Phi(s) + (1-lambda) Phi(0),
so Phi(0) <= Phi(s). Hence Phi is constant (= Phi(0)) on I.

3.6. Let x' be x with x_k replaced by x(s_+). By 3.5, S(x') = S(x) = M, so x' is a maximizer. Pairs not
containing k are unchanged; for j in J_k, x(s_+) is orthogonal to x_j (it lies in L); and x(s_+) is
orthogonal to x_{j*} by 3.3, while <x_k,x_{j*}> != 0. Hence omega(x') >= omega(x) + 1, contradicting the
choice of x in 1.2.

3.7. Therefore R is empty, which is (i), or dim L <= 1. In the latter case dim L = 1 because x_k is in L,
so L = span{x_k} and span{x_j : j in J_k} = L^perp = x_k^perp, which is (ii); its dimension d-1 is at most
|J_k|. QED

## 4. The non-orthogonality graph (rung R4)

4.1. Let G' be the graph on {1..N} with an edge {j,k} (j != k) iff <x_j,x_k> != 0. The neighbours of k are
exactly the elements of R = {1..N} \ ({k} u J_k). In case (i) of Lemma A, deg(k) = 0. In case (ii),
deg(k) = (N-1) - |J_k| <= (N-1) - (d-1) = N - d = 2. So every vertex of G' has degree <= 2.

4.2. Every connected component of a finite graph with maximum degree <= 2 is a single vertex, a path, or
a cycle (as a graph: its edges are exactly the path or cycle edges). Proof: take a path P = v_1...v_m in
the component that cannot be extended at either end. Every neighbour of v_1 or v_m lies on P (else P
extends). Each interior v_i (1<i<m) already has the two neighbours v_{i-1}, v_{i+1}, so it has no others.
Hence a second neighbour of v_1 (besides v_2) could only be v_m (with m >= 3), and a second neighbour of
v_m (besides v_{m-1}) could only be v_1, because every other vertex of P already has its two neighbours
on P. So the vertices of P have no neighbours outside P; by connectivity the component is {v_1..v_m}, and its
edges are the path edges, plus the edge v_1 v_m if present (then m >= 3 and the component is a cycle).

4.3. Notation. For a component K let V_K be its vertex set, m_K := |V_K|, U_K := span{x_i : i in V_K},
e_K := m_K - dim U_K >= 0, and D(K) := sum over pairs {i,j} in V_K of phi(x_i,x_j).
If i, j lie in different components, {i,j} is not an edge, so <x_i,x_j> = 0 and phi(x_i,x_j) = 0.
If i, j lie in the same component but {i,j} is not an edge, again <x_i,x_j> = 0 and phi = 0. Therefore
  D(x) = sum_K D(K),  and D(K) = sum over the edges {i,j} of K of phi(x_i,x_j).
The subspaces U_K are pairwise orthogonal, so their sum is direct and sum_K dim U_K <= d; hence
  sum_K e_K = N - sum_K dim U_K >= N - d = 2.                                   (4.3.1)

## 5. Which components occur (rung R5)

5.1. (Dimension bound.) Let K be a component and k in V_K with deg(k) >= 1. Then dim U_K <= m_K - deg(k).
Proof. Since k has a neighbour, Lemma A(i) fails, so Lemma A(ii) holds: span{x_j : j in J_k} has dimension
d-1. Now J_k consists of all vertices outside V_K (no edges leave K) together with
V_K \ ({k} u N(k)), where N(k) is the neighbour set of k (inside a component, j != k is orthogonal to x_k
iff j is not adjacent to k). Let W_K := span{x_j : j not in V_K}; W_K is orthogonal to U_K, so
dim W_K <= d - dim U_K. Hence
  d - 1 <= dim W_K + |V_K \ ({k} u N(k))| <= (d - dim U_K) + (m_K - 1 - deg(k)),
which rearranges to dim U_K <= m_K - deg(k). QED

5.2. (Paths have near-full rank.) Let y_1..y_m (m >= 2) be unit vectors with <y_i,y_j> = 0 for |i-j| >= 2
and <y_i,y_{i+1}> != 0 for all i. Then dim span{y_i} >= m-1.
Proof. The Gram matrix Gm = (<y_i,y_j>) has rank equal to dim span{y_i}. Its submatrix with rows 2..m and
columns 1..m-1 has entry (r,c) = <y_{r+1},y_c> (r,c = 1..m-1), which is 0 when c <= r-1 (then
|r+1-c| >= 2); so it is upper triangular with diagonal entries <y_{r+1},y_r> != 0, hence invertible.
So rank Gm >= m-1. QED

5.3. (Classification.) Let K be a component.
 (a) m_K = 1: e_K = 0 and D(K) = 0.
 (b) K is a path with m_K = 2, vertices v_1 v_2: by 5.1, dim U_K <= 2 - 1 = 1, so x_{v_2} = +-x_{v_1};
     then e_K = 1 and D(K) = phi(x_{v_1},x_{v_2}) = pi/2.
 (c) K is a path v_1...v_m with m >= 3: v_2 has degree 2, so dim U_K <= m-2 by 5.1; but the vectors
     x_{v_1},..,x_{v_m} satisfy the hypotheses of 5.2 (non-consecutive vertices of the path are
     non-adjacent in G', hence orthogonal; consecutive ones are adjacent, hence non-orthogonal), so
     dim U_K >= m-1. Contradiction: this case does not occur.
 (d) K is a cycle v_1...v_m v_1 with m >= 3: every vertex has degree 2, so dim U_K <= m-2 by 5.1.
     Deleting v_m leaves the path v_1...v_{m-1} (m-1 >= 2 vertices, consecutive ones non-orthogonal,
     non-consecutive ones non-adjacent in G' hence orthogonal), so by 5.2 dim U_K >= m-2.
     Hence dim U_K = m - 2 and e_K = 2. Also m - 2 = dim U_K <= d, so m <= d + 2 <= 6.
     In the cycle, x_{v_i} is orthogonal to x_{v_j} whenever v_i, v_j are not cyclically consecutive.

So it remains to show D(K) >= pi for cycles of length m = 3, 4, 5, 6 with dim U_K = m - 2
(Steps 6-8). Below y_i := x_{v_i}, indices mod m, and phi_i := phi(y_i, y_{i+1}); then D(K) = sum_i phi_i.
For m >= 4 each phi_i lies in (0, pi/2): phi_i > 0 because {v_i,v_{i+1}} is an edge; and if
y_{i+1} = +-y_i, then y_{i+2} (orthogonal to y_i, since i and i+2 are not cyclically consecutive when
m >= 4) would be orthogonal to y_{i+1}, contradicting that {v_{i+1},v_{i+2}} is an edge; so phi_i < pi/2.

## 6. Cycles of length 3 and 4 (rung R6)

6.1. m = 3: dim U_K = 1, so y_1, y_2, y_3 are all +-y_1 and each phi_i = pi/2; D(K) = 3pi/2 >= pi.

6.2. m = 4: dim U_K = 2, y_1 orthogonal to y_3 and y_2 orthogonal to y_4. So {y_1,y_3} and {y_2,y_4} are
orthonormal bases of U_K. Expanding y_2 in the first basis: <y_2,y_1>^2 + <y_2,y_3>^2 = 1, i.e.
sin^2 phi_1 + sin^2 phi_2 = 1, so sin phi_2 = cos phi_1 = sin(pi/2 - phi_1); both phi_2 and pi/2 - phi_1 lie in
[0, pi/2], where sin is injective, so phi_1 + phi_2 = pi/2. Expanding y_4 in the same basis gives
<y_4,y_1>^2 + <y_4,y_3>^2 = 1, i.e. sin^2 phi_4 + sin^2 phi_3 = 1, so phi_3 + phi_4 = pi/2. Hence D(K) = pi.

## 7. Cycles of length 5 (rung R7)

Setting: y_1..y_5 unit vectors in a 3-dimensional space U, y_i orthogonal to y_{i+2} and to y_{i+3}
(indices mod 5; these are exactly the non-consecutive pairs), phi_i in (0, pi/2) (end of Step 5).

7.1. (Four-term relation.) For unit vectors z_1..z_4 with z_1 orth z_3, z_1 orth z_4, z_2 orth z_4 and
p = <z_1,z_2>, q = <z_2,z_3>, r = <z_3,z_4>, the Gram matrix is
  [[1,p,0,0],[p,1,q,0],[0,q,1,r],[0,0,r,1]],
whose determinant, by cofactor expansion along the first row, is
  (1 - q^2 - r^2) - p (p (1 - r^2)) = (1-p^2)(1-r^2) - q^2.
If z_1..z_4 lie in a 3-dimensional space the Gram matrix is singular, so q^2 = (1-p^2)(1-r^2), i.e.
  sin phi(z_2,z_3) = cos phi(z_1,z_2) cos phi(z_3,z_4)
(take square roots; cos phi(z,z') = (1 - <z,z'>^2)^{1/2} >= 0).

7.2. For each i, (z_1,z_2,z_3,z_4) := (y_i, y_{i+1}, y_{i+2}, y_{i+3}) satisfies the hypotheses of 7.1
(pairs (i,i+2), (i,i+3), (i+1,i+3) are non-consecutive mod 5; all four vectors lie in U). With
i = 3, i = 5 and i = 1 respectively:
  sin phi_4 = cos phi_3 cos phi_5,   sin phi_1 = cos phi_5 cos phi_2,   sin phi_2 = cos phi_1 cos phi_3.
Put u := phi_3, v := phi_5 (both in (0, pi/2)), P := cos v, Q := cos u (both in (0,1)), and
c := cos phi_4 = (1 - Q^2 P^2)^{1/2} > 0.

7.3. (Solving for phi_1, phi_2.) From sin phi_1 = P cos phi_2 and sin phi_2 = Q cos phi_1:
  sin^2 phi_1 = P^2 (1 - sin^2 phi_2) = P^2 (1 - Q^2 + Q^2 sin^2 phi_1),
so sin^2 phi_1 (1 - P^2 Q^2) = P^2 (1 - Q^2), i.e. sin^2 phi_1 = cos^2 v sin^2 u / c^2. Then
cos^2 phi_1 = (1 - cos^2 u cos^2 v - cos^2 v sin^2 u)/c^2 = sin^2 v / c^2. Next
sin^2 phi_2 = Q^2 cos^2 phi_1 = cos^2 u sin^2 v / c^2 and
cos^2 phi_2 = (1 - cos^2 u cos^2 v - cos^2 u sin^2 v)/c^2 = sin^2 u / c^2.
All of sin phi_i, cos phi_i (i = 1,2), sin u, sin v, cos u, cos v, c are >= 0, so
  sin phi_1 = sin u cos v / c,  cos phi_1 = sin v / c,  sin phi_2 = cos u sin v / c,  cos phi_2 = sin u / c.

7.4. Hence
  cos(phi_1 + phi_2) = cos phi_1 cos phi_2 - sin phi_1 sin phi_2
                     = sin u sin v (1 - cos u cos v) / (1 - cos^2 u cos^2 v)
                     = sin u sin v / (1 + cos u cos v) =: w(u),
using 1 - cos^2 u cos^2 v = (1 - cos u cos v)(1 + cos u cos v) and 1 - cos u cos v > 0.
As phi_1 + phi_2 lies in [0, pi], where cos is injective, phi_1 + phi_2 = arccos w(u).
(Note 0 <= w(u) <= 1, because 1 + cos u cos v - sin u sin v = 1 + cos(u+v) >= 0.)

7.5. Using arcsin t = pi/2 - arccos t and arccos t = pi/2 - arcsin t (t in [0,1]):
  D(K) = phi_1 + phi_2 + phi_3 + phi_4 + phi_5
       = arccos w(u) + u + arcsin(cos u cos v) + v
       = pi + F(u),   where F(r) := r + v - arccos(cos r cos v) - arcsin(w(r)),  r in [0, pi/2],
and w(r) := sin r sin v / (1 + cos r cos v). (Here v in (0, pi/2) is fixed.)

7.6. (F >= 0.) F is continuous on [0, pi/2]. Values at the ends: F(0) = v - arccos(cos v) - arcsin 0 = 0
(v in [0,pi]); F(pi/2) = pi/2 + v - arccos 0 - arcsin(sin v) = pi/2 + v - pi/2 - v = 0 (v in [0,pi/2]).
Second derivative on (0, pi/2):
 * g(r) := arccos(cos r cos v). With E := 1 - cos^2 r cos^2 v > 0 (as cos v < 1):
   g' = sin r cos v E^{-1/2}, and, since dE/dr = 2 cos r sin r cos^2 v,
   g'' = cos r cos v E^{-1/2} - sin^2 r cos^3 v cos r E^{-3/2}
       = cos r cos v E^{-3/2} (E - sin^2 r cos^2 v) = cos r cos v sin^2 v E^{-3/2} >= 0.
 * h(r) := arcsin(w(r)). One computes w'(r) = sin v (cos r + cos v)/(1 + cos r cos v)^2 (quotient rule:
   numerator sin v [cos r (1 + cos r cos v) + sin^2 r cos v] = sin v (cos r + cos v)), and
   (1 + cos r cos v)^2 - sin^2 r sin^2 v = 2 cos r cos v + cos^2 r + cos^2 v = (cos r + cos v)^2 (expand
   sin^2 = 1 - cos^2), so 1 - w^2 = (cos r + cos v)^2/(1 + cos r cos v)^2 > 0 (cos v > 0). Hence
   h' = w'/(1-w^2)^{1/2} = sin v / (1 + cos r cos v),   h'' = sin v cos v sin r / (1 + cos r cos v)^2 >= 0.
 So F'' = -g'' - h'' <= 0 on (0, pi/2), and F is concave on [0, pi/2]. A concave function lies above its
 chord: for r in [0,pi/2], F(r) >= (1 - 2r/pi) F(0) + (2r/pi) F(pi/2) = 0.
Hence D(K) = pi + F(u) >= pi.

## 8. Cycles of length 6 (rung R8)

Setting: y_1..y_6 unit vectors in a 4-dimensional space U, y_i orthogonal to y_j whenever i, j are not
cyclically consecutive mod 6, phi_i in (0, pi/2) (end of Step 5). So
y_1 orth y_3,y_4,y_5;  y_2 orth y_4,y_5,y_6;  y_3 orth y_5,y_6,y_1;  y_4 orth y_6,y_1,y_2;
y_5 orth y_1,y_2,y_3;  y_6 orth y_2,y_3,y_4.

8.1. Let A := span{y_2,y_3}, B := span{y_5,y_6}. y_2 != +-y_3 (phi_2 < pi/2), so dim A = 2; and
y_5 != +-y_6 (phi_5 < pi/2), so dim B = 2. A is orthogonal to B (y_2, y_3 are both orthogonal to y_5, y_6). So A (+) B is a 4-dimensional
subspace of U, hence equals U, and every y_i decomposes uniquely as (part in A) + (part in B).

8.2. Choose unit vectors n_2, n_3 in A with n_2 orth y_2, n_3 orth y_3, and unit n_5, n_6 in B with
n_5 orth y_5, n_6 orth y_6. Write y_1 = a_1 + b_1 (a_1 in A, b_1 in B). Since b_1 orth A,
<a_1,y_3> = <y_1,y_3> = 0, so a_1 = lam n_3 (the vectors of the 2-dimensional A orthogonal to y_3 are
the multiples of n_3). Since a_1 orth B, <b_1,y_5> = <y_1,y_5> = 0, so b_1 = mu n_5 (same reason in B).
Write y_4 = a_4 + b_4 (a_4 in A, b_4 in B). Then <a_4,y_2> = <y_4,y_2> = 0 gives a_4 = lam' n_2, and
<b_4,y_6> = <y_4,y_6> = 0 gives b_4 = mu' n_6. As a_1 orth b_1,
lam^2 + mu^2 = |y_1|^2 = 1, and lam'^2 + mu'^2 = 1. Choose s, t in [0, pi/2] with
cos s = |lam|, sin s = |mu|, cos t = |lam'|, sin t = |mu'|. Put a := phi_2, b := phi_5 (in (0, pi/2)).

8.3. In the 2-dimensional A, {y_3,n_3} and {y_2,n_2} are orthonormal bases. Expanding the unit vector
y_2 in the first: <y_2,n_3>^2 = 1 - <y_2,y_3>^2 = 1 - sin^2 a = cos^2 a. Expanding y_3 in the second:
<y_3,n_2>^2 = 1 - <y_3,y_2>^2 = cos^2 a. Expanding n_3 in the second:
<n_3,n_2>^2 = 1 - <n_3,y_2>^2 = sin^2 a. In the 2-dimensional B, {y_5,n_5} and {y_6,n_6} are orthonormal
bases, and <y_5,y_6>^2 = sin^2 b. Expanding y_6 in the first: <y_6,n_5>^2 = 1 - sin^2 b = cos^2 b.
Expanding y_5 in the second: <y_5,n_6>^2 = cos^2 b. Expanding n_5 in the second:
<n_5,n_6>^2 = 1 - <n_5,y_6>^2 = sin^2 b. Therefore (inner products with the other summand vanish):
  sin phi_1 = |<y_1,y_2>| = |lam| |<n_3,y_2>| = cos s cos a,
  sin phi_3 = |<y_3,y_4>| = |lam'| |<y_3,n_2>| = cos t cos a,
  sin phi_4 = |<y_4,y_5>| = |mu'| |<n_6,y_5>| = sin t cos b,
  sin phi_6 = |<y_6,y_1>| = |mu| |<y_6,n_5>| = sin s cos b,
and from 0 = <y_1,y_4> = lam lam' <n_3,n_2> + mu mu' <n_5,n_6>, taking absolute values,
  cos s cos t sin a = sin s sin t sin b.                                              (8.3.1)

8.4. Let f(r) := arcsin(cos a cos r) + arcsin(cos b sin r) for r in [0, pi/2]. Then
D(K) = a + b + f(s) + f(t). The function r -> cos a cos r has amplitude cos a < 1 and is >= 0 on
[0, pi/2]; r -> cos b sin r has amplitude cos b < 1 and is >= 0 on [0, pi/2]. By Lemma T(i) both
arcsin terms are concave on [0, pi/2], so f is concave there. f(0) = arcsin(cos a) = pi/2 - a and
f(pi/2) = arcsin(cos b) = pi/2 - b (a, b in [0,pi/2]). By the chord inequality, for r in [0, pi/2]:
  f(r) >= (1 - 2r/pi)(pi/2 - a) + (2r/pi)(pi/2 - b) = pi/2 - a + (2r/pi)(a - b).
Therefore
  D(K) >= a + b + pi - 2a + (2(s+t)/pi)(a - b) = pi + (a - b)(2(s+t)/pi - 1).

8.5. Claim: (a - b)(s + t - pi/2) >= 0. If a = b this is 0. If a > b: suppose s + t < pi/2; then
cos(s+t) > 0, i.e. cos s cos t > sin s sin t >= 0; as sin a > sin b >= 0 (sin increasing on [0,pi/2]) and
sin a > 0, we get cos s cos t sin a > sin s sin t sin a >= sin s sin t sin b, contradicting (8.3.1); so
s + t >= pi/2. If a < b: suppose s + t > pi/2; then sin s sin t > cos s cos t >= 0, and with
sin b > sin a >= 0: sin s sin t sin b > cos s cos t sin b >= cos s cos t sin a, contradicting (8.3.1);
so s + t <= pi/2. In all cases the claim holds, so D(K) >= pi.

## 9. Assembly (rung R9)

9.1. By 5.3, every component K of G' is (a) an isolated vertex with e_K = 0, D(K) = 0; or (b) a pair of
coincident lines with e_K = 1, D(K) = pi/2; or (d) a cycle of length m in {3,4,5,6} with e_K = 2, and then
D(K) >= pi by 6.1 (m=3), 6.2 (m=4), Step 7 (m=5, U_K 3-dimensional) and Step 8 (m=6, U_K
4-dimensional). In every case D(K) >= e_K pi/2.

9.2. By 4.3 and (4.3.1): D(x) = sum_K D(K) >= (pi/2) sum_K e_K >= (pi/2)(N - d) = pi.

9.3. By 0.2, S(x) = C(N,2) pi/2 - D(x) <= C(N,2) pi/2 - pi. Since x is a maximizer (Step 1), every
configuration y of N lines in R^d satisfies S(y) <= M = S(x) <= C(N,2) pi/2 - pi. For (N,d) = (5,3)
this is S <= 4pi; for (N,d) = (6,4) it is S <= 13pi/2. QED

## 10. What is established, and remarks

10.1. Established: both inequalities of the target, for all configurations (repetitions allowed, any
span). No step rests on computation; the code in out/code/ only re-checks identities and samples.

10.2. Sharpness (not required): e_1,e_1,e_2,e_2,e_3 in R^3 has S = 8 pi/2 = 4pi, and e_1,e_1,e_2,e_2,e_3,e_4
in R^4 has S = 13 pi/2 (exactly two coinciding pairs, all other pairs orthogonal).

10.3. Scope remark (not claimed): Steps 1-5 and 9 use only N = d+2, for any d >= 2. They reduce the general
case N = d+2 to the inequality "sum of consecutive phi >= pi" for m-cycles spanning an (m-2)-dimensional
space, m <= d+2. That inequality is proved here only for m <= 6, which is exactly what d in {3,4} needs.
````
<!-- END EMBEDDED proof.md -->

---

## 5. How to verify

**Mathematics.** The proof is a written, computer-free argument, so it is verified by reading Section 4 (equivalently `submission/proof.md`). No computation is load-bearing (`proof.md`, 10.1). The hand-in rule on computation (code included, under 10 minutes, rigorous arithmetic) therefore does not apply to any step.

**Integrity of the shipped files.** These commands only confirm byte identity; they do not check any mathematics. Run them from the directory that contains this `submission.md`. The Scribe ran both in its copy under `out/` and recorded the real output and time.

1. The shipped artefacts match the pinned hashes:

   ```
   cd submission && /usr/bin/time -p shasum -a 256 -c MANIFEST.sha256
   ```

   Expected output:

   ```
   proof.md: OK
   claims.md: OK
   ```

   Measured runtime: real 0.01 s; shasum 6.02 on macOS, Darwin 24.3.0 (log: `verify/logs/01_manifest_check.txt`).

2. The proof embedded in Section 4 is byte-identical to `submission/proof.md` and to the pinned hash. The script `verify/check_embedded.py` uses the Python standard library only:

   ```
   /usr/bin/time -p python3 verify/check_embedded.py submission.md submission/proof.md 66449ec26e2a5bfc1f0c5fc00d2980aeb1dd3c1d791364a3a80af3b8ab289518
   ```

   Expected output:

   ```
   embedded proof sha256: 66449ec26e2a5bfc1f0c5fc00d2980aeb1dd3c1d791364a3a80af3b8ab289518
   proof.md       sha256: 66449ec26e2a5bfc1f0c5fc00d2980aeb1dd3c1d791364a3a80af3b8ab289518
   embedded == proof.md: OK
   embedded == pinned hash: OK
   ```

   Measured runtime: real 0.02 s (log: `verify/logs/02_embedded_check.txt`). The Scribe ran it with /Users/defneirmakyurt/bainsahackathon/.venv/bin/python3 (Python 3.11.9), and again with the plain system python3 (Python 3.11.9, /Library/Frameworks/Python.framework/Versions/3.11/bin/python3; real 0.01 s, log `verify/logs/03_embedded_check_plain_python3.txt`). The same output was produced both times. The script imports only `hashlib` and `sys`.

The Scribe re-ran both checks on the final version of this file, with identical output (logs `verify/logs/04_embedded_check_final.txt` and `verify/logs/05_manifest_check_final.txt`). Both runtimes are far below the 10-minute limit.

---

## 6. Limitations

- **Only (a) and (b) are established.** The general case N = d + 2 for every d >= 2 (Cell 5) is **not** established. `proof.md` 10.3 marks its scope remark as "not claimed". Steps 1-5 and 9 use only N = d + 2, but the cycle inequality (Steps 6-8) is proved only for cycles of length m <= 6. That is exactly what d in {3, 4} needs.
- **Sharpness** (`proof.md` 10.2) is noted, not required. The configurations e1,e1,e2,e2,e3 and e1,e1,e2,e2,e3,e4 attain the two bounds.
- **Code referenced but not shipped.** `proof.md` 10.1 mentions "the code in out/code/", and `claims.md` lists `code/check_cycles.py`, `code/random_search.py` and `code/check_identities.py`. Those rows have status CHECKED, which means evidence or support only, not load-bearing. This code was not among the accepted artefacts shipped to this Scribe task. It is therefore not included in this submission and was not re-run by the Scribe. No step of the proof depends on it (`proof.md` 10.1).
- **Internal labels kept.** The embedded proof keeps the team's internal labels ("rung R1" ... "R9") and the path "out/code/", because it is reproduced byte for byte. These labels carry no mathematical content.
- **What the verification commands show.** They confirm file integrity only. The correctness of the result rests on the written proof in Section 4. The statuses SOLVED / PROVED are copied from the team's brief and have not been upgraded.
- The Scribe flagged no step of the proof as reading wrong, and made no edits to it.
