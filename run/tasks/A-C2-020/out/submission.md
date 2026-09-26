# Cell 2: An Orthogonality Lemma (2 points)

## Statement

A statement about a chain of vectors, in which each vector may fail to be orthogonal only to its immediate neighbours in the list.

Let \( m \geq 2 \) and let \( x_1, \ldots, x_m \) be unit vectors in \( \mathbb{R}^{m-1} \) with
\[
  \langle x_i, x_j \rangle = 0 \qquad \text{whenever } |i - j| \geq 2.
\]
Prove that
\[
  \sum_{i=1}^{m-1} \theta(x_i, x_{i+1}) \leq (m - 2) \frac{\pi}{2},
\]
where
\[
  \theta(x, y) = \arccos \bigl| \langle x, y \rangle \bigr|.
\]

## Status

**Cell 2 (A-C2): SOLVED. Claim: PROVED.**

The proof below is complete and covers every \( m \geq 2 \).

## Cited results and our contribution

- **Cited:** we cite no published result. The proof uses only standard tools: the Cauchy–Schwarz inequality, elementary trigonometry, dimension counting (orthogonal complements, Gram–Schmidt) and induction.
- **Ours:** the whole proof below.
- **Computation:** the proof uses no computation.

## Proof

### Notation

Take a chain \( x_1, \ldots, x_m \) as in the statement and put
\[
  c_i = \langle x_i, x_{i+1} \rangle \qquad (1 \le i \le m-1).
\]
By Cauchy–Schwarz, \( |c_i| \le 1 \). Put \( a_i = \arcsin |c_i| \in [0, \pi/2] \).

An **\(m\)-chain** is a list of \( m \) unit vectors in an inner-product space of dimension \( m-1 \) satisfying \( \langle x_i, x_j \rangle = 0 \) for \( |i-j| \ge 2 \). For an \(m\)-chain \(x\), write
\[
  A(x) = \sum_{i=1}^{m-1} a_i .
\]

### Step 1 (reformulation)

For \( t \in [0,1] \) we have \( \arccos t + \arcsin t = \pi/2 \). Indeed, let \( s = \arcsin t \in [0, \pi/2] \). Then \( \cos(\pi/2 - s) = \sin s = t \), and \( \pi/2 - s \in [0, \pi/2] \), which is the range of \( \arccos \) on \( [0,1] \). So \( \arccos t = \pi/2 - s \).

Hence \( \theta(x_i, x_{i+1}) = \arccos |c_i| = \pi/2 - a_i \), and
\[
  \sum_{i=1}^{m-1} \theta(x_i, x_{i+1}) = (m-1)\frac{\pi}{2} - A(x).
\]
So the target is equivalent to
\[
  (*) \qquad A(x) \ge \frac{\pi}{2} \quad \text{for every } m\text{-chain and every } m \ge 2 .
\]

*Remark.* An inner-product space of dimension \( k \) is isometric to \( \mathbb{R}^k \): choose an orthonormal basis (Gram–Schmidt). Such an isometry preserves inner products. So \( (*) \) for chains in \( \mathbb{R}^{m-1} \) is the same as \( (*) \) for chains in any \( (m-1) \)-dimensional inner-product space. We use this in Step 4.

We prove \( (*) \) by induction on \( m \).

### Step 2 (base case \( m = 2 \))

Here \( x_1, x_2 \) are unit vectors in \( \mathbb{R}^1 \), so \( x_1, x_2 \in \{+1, -1\} \) and \( |c_1| = |x_1 x_2| = 1 \). Thus \( a_1 = \arcsin 1 = \pi/2 \) and \( A(x) = \pi/2 \ge \pi/2 \). (Equivalently, \( \theta(x_1, x_2) = 0 = (2-2)\pi/2 \).)

### Step 3 (inductive step: the degenerate case)

Let \( m \ge 3 \) and assume \( (*) \) for \( (m-1) \)-chains. Let \( x_1, \ldots, x_m \) be an \(m\)-chain.

If \( |c_{m-1}| = 1 \), then \( a_{m-1} = \pi/2 \). Since every \( a_i \ge 0 \), we get \( A(x) \ge a_{m-1} = \pi/2 \), and we are done.

### Step 4 (inductive step: reduction when \( |c_{m-1}| < 1 \))

Write \( c = c_{m-1} \) and let
\[
  W = x_m^{\perp} = \{ v \in \mathbb{R}^{m-1} : \langle v, x_m \rangle = 0 \}.
\]
Since \( x_m \ne 0 \), \( \dim W = m-2 \ge 1 \).

Define \( u = x_{m-1} - c\, x_m \). Then
\[
  \langle u, x_m \rangle = c - c \langle x_m, x_m \rangle = 0, \quad\text{so } u \in W,
\]
\[
  \|u\|^2 = 1 - 2c^2 + c^2 = 1 - c^2 > 0 .
\]
Now \( |c| = \sin a_{m-1} \) with \( a_{m-1} \in [0, \pi/2) \), so \( \sqrt{1-c^2} = \cos a_{m-1} > 0 \). Let
\[
  y = \frac{u}{\cos a_{m-1}},
\]
a unit vector in \( W \). Define
\[
  z_j = x_j \quad (1 \le j \le m-2), \qquad z_{m-1} = y .
\]

**(4a)** \( z_j \in W \) for \( j \le m-2 \): \( \langle x_j, x_m \rangle = 0 \) because \( |j - m| \ge 2 \).

**(4b)** Every \( z_j \) is a unit vector (by hypothesis for \( j \le m-2 \), and by construction of \( y \)).

**(4c)** Orthogonality for \( |i-j| \ge 2 \) within \( z \). If \( i, j \le m-2 \), this is the hypothesis on \( x \). If \( j = m-1 \) and \( i \le m-3 \), then
\[
  \langle x_i, y \rangle = \frac{\langle x_i, x_{m-1} \rangle - c \langle x_i, x_m \rangle}{\cos a_{m-1}} = \frac{0 - 0}{\cos a_{m-1}} = 0,
\]
since \( |i - (m-1)| \ge 2 \) and \( |i - m| \ge 3 \).

**(4d)** Consecutive coefficients of \( z \). For \( i \le m-3 \), \( \langle z_i, z_{i+1} \rangle = c_i \) (unchanged). For \( i = m-2 \),
\[
  \langle x_{m-2}, y \rangle = \frac{c_{m-2} - c \langle x_{m-2}, x_m \rangle}{\cos a_{m-1}} = \frac{c_{m-2}}{\cos a_{m-1}},
\]
because \( |(m-2) - m| = 2 \). Hence
\[
  |\langle z_{m-2}, z_{m-1} \rangle| = \frac{\sin a_{m-2}}{\cos a_{m-1}} .
\]

So \( z_1, \ldots, z_{m-1} \) is an \( (m-1) \)-chain in the \( (m-2) \)-dimensional space \( W \). Its angles are \( a_1, \ldots, a_{m-3} \) and
\[
  a' = \arcsin\!\left( \frac{\sin a_{m-2}}{\cos a_{m-1}} \right).
\]
(The argument lies in \( [0,1] \) by Cauchy–Schwarz applied to the unit vectors \( z_{m-2}, z_{m-1} \).)

By the induction hypothesis, together with the Remark in Step 1,
\[
  \text{(4e)} \qquad a_1 + \cdots + a_{m-3} + a' \ge \frac{\pi}{2}.
\]
(For \( m = 3 \) the sum \( a_1 + \cdots + a_{m-3} \) is empty, and (4e) reads \( a' \ge \pi/2 \).)

### Step 5 (a trigonometric lemma)

**Lemma.** Let \( \alpha \in [0, \pi/2] \) and \( \beta \in [0, \pi/2) \) with \( \sin\alpha \le \cos\beta \). Then
\[
  \arcsin\!\left( \frac{\sin\alpha}{\cos\beta} \right) \le \alpha + \beta \quad \text{whenever } \alpha + \beta < \pi/2,
\]
and \( \arcsin(\sin\alpha / \cos\beta) \le \pi/2 \) always.

*Proof.* The second claim is the range of \( \arcsin \). For the first, assume \( \alpha + \beta < \pi/2 \). Then
\[
\begin{aligned}
  \sin(\alpha+\beta)\cos\beta - \sin\alpha
  &= \sin\alpha\cos^2\beta + \cos\alpha\sin\beta\cos\beta - \sin\alpha \\
  &= -\sin\alpha\sin^2\beta + \cos\alpha\sin\beta\cos\beta \\
  &= \sin\beta\,(\cos\alpha\cos\beta - \sin\alpha\sin\beta) \\
  &= \sin\beta\,\cos(\alpha+\beta) \;\ge\; 0,
\end{aligned}
\]
since \( \sin\beta \ge 0 \) (as \( \beta \in [0, \pi/2) \)) and \( \cos(\alpha+\beta) > 0 \) (as \( \alpha+\beta \in [0, \pi/2) \)). Dividing by \( \cos\beta > 0 \) gives
\[
  \frac{\sin\alpha}{\cos\beta} \le \sin(\alpha+\beta).
\]
Both sides lie in \( [0,1] \) and \( \arcsin \) is increasing on \( [0,1] \), so
\[
  \arcsin\!\left( \frac{\sin\alpha}{\cos\beta} \right) \le \arcsin(\sin(\alpha+\beta)) = \alpha + \beta,
\]
the last equality because \( \alpha + \beta \in [0, \pi/2] \). \( \blacksquare \)

### Step 6 (end of the inductive step)

Apply Step 5 with \( \alpha = a_{m-2} \) and \( \beta = a_{m-1} \). Its hypotheses hold: \( \beta < \pi/2 \) because \( |c_{m-1}| < 1 \); and \( \sin\alpha \le \cos\beta \) by (4d) and Cauchy–Schwarz.

- If \( a_{m-2} + a_{m-1} \ge \pi/2 \), then \( A(x) \ge a_{m-2} + a_{m-1} \ge \pi/2 \), since all \( a_i \ge 0 \).
- If \( a_{m-2} + a_{m-1} < \pi/2 \), then \( a' \le a_{m-2} + a_{m-1} \) by Step 5, so by (4e)
\[
  A(x) = a_1 + \cdots + a_{m-3} + a_{m-2} + a_{m-1} \ge a_1 + \cdots + a_{m-3} + a' \ge \frac{\pi}{2}.
\]

Together with Step 3, \( (*) \) holds for all \(m\)-chains. By induction, with base case Step 2, \( (*) \) holds for every \( m \ge 2 \).

### Step 7 (the target)

By Step 1,
\[
  \sum_{i=1}^{m-1} \theta(x_i, x_{i+1}) = (m-1)\frac{\pi}{2} - A(x) \le (m-1)\frac{\pi}{2} - \frac{\pi}{2} = (m-2)\frac{\pi}{2}. \qquad \blacksquare
\]

### Remarks on edge cases

- \( m = 2 \) is Step 2.
- \( m = 3 \) is covered by the empty prefix sum in (4e).
- Parallel or antiparallel consecutive vectors: Step 3.
- Orthogonal consecutive vectors (\( c_i = 0 \), \( a_i = 0 \)) need no separate treatment.

## How to verify

The proof uses no computation, so there is no program to run. A judge verifies it by reading Steps 1–7.

## Limitations

- The statement is proved in full, for every \( m \ge 2 \), with no extra hypotheses. Nothing in the cell is left open.
- The proof is a human-readable argument; it has not been formally machine-checked.
