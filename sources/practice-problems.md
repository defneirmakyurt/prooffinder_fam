# Angles between lines

How large can the sum of pairwise angles between \(N\) lines through the origin be? Fejes Tóth conjectured in 1959 that orthogonal lines win.

A *line* here always means a line through the origin of \(\mathbb{R}^d\). The angle between two lines \(\ell,\ell'\) is the acute (non-obtuse) angle \(\theta(\ell,\ell')\in[0,\pi/2]\) between them. If \(\ell,\ell'\) are spanned by unit vectors \(x,x'\), then

\[
\theta(\ell,\ell')=\arccos |\langle x,x'\rangle|.
\]

For lines \(\ell_1,\ldots,\ell_N\) in \(\mathbb{R}^d\) (repetitions allowed), write

\[
S(\ell_1,\ldots,\ell_N)=\sum_{1\le i<j\le N}\theta(\ell_i,\ell_j).
\]

The question is how large \(S\) can be. In 1959 L. Fejes Tóth conjectured that \(S\) is maximised by taking \(d\) mutually orthogonal lines, each used either \(\lfloor N/d\rfloor\) or \(\lceil N/d\rceil\) times. When \(N=d+k\) with \(0\le k\le d\), that configuration (the \(d\) coordinate axes, \(k\) of them used twice) has

\[
S=\left(\binom{N}{2}-k\right)\cdot\frac{\pi}{2},
\]

because exactly \(k\) pairs of lines coincide and every other pair is orthogonal.

Each cell below asks you to prove this bound, or a special case of it. Unless a cell says otherwise, you need a complete proof. Citing a published result for the statement you are asked to prove does not count.

## What to hand in

For each cell you attempt, hand in a written proof. You may use a computer to explore. A proof may rely on a computation only if you include the code, it runs in under 10 minutes on a laptop, and it is rigorous: exact or interval arithmetic, or an argument that bounds the numerical error. Say clearly which cells you consider solved and which are partial.

---

# An orthogonality lemma

**2 points**  
**Judged**

A statement about a chain of vectors, in which each vector may fail to be orthogonal only to its immediate neighbours in the list. Let \(m\ge 2\) and let \(x_1,\ldots,x_m\) be unit vectors in \(\mathbb{R}^{m-1}\) with \(\langle x_i,x_j\rangle=0\) whenever \(|i-j|\ge 2\). Prove that

\[
\sum_{i=1}^{m-1}\theta(x_i,x_{i+1})\le (m-2)\cdot\frac{\pi}{2},
\]

where \(\theta(x,y)=\arccos|\langle x,y\rangle|\).

**Submit solution**

---

# \(d+1\) lines in \(\mathbb{R}^d\)

**3 points**  
**Judged**

The first case in every dimension: one line more than the dimension, \(N=d+1\), where the conjectured optimum repeats exactly one of the \(d\) coordinate axes. Let \(d\ge 1\). Prove that any \(d+1\) lines in \(\mathbb{R}^d\) satisfy

\[
S\le \left(\binom{d+1}{2}-1\right)\cdot\frac{\pi}{2}.
\]

**Submit solution**

---

# \(d+2\) lines in \(\mathbb{R}^d\)

**8 points**  
**Judged**

The case \(N=d+2\) in every dimension, with the same conjectured optimum: the \(d\) coordinate axes, two of them repeated. Prove that for every \(d\ge 2\), any \(d+2\) lines in \(\mathbb{R}^d\) satisfy

\[
S\le \left(\binom{d+2}{2}-2\right)\frac{\pi}{2}.
\]

**Submit solution**

---

# Five lines in \(\mathbb{R}^3\), six in \(\mathbb{R}^4\)

**5 points**  
**Judged**

Two concrete instances of the next case, \(N=d+2\): five lines in three dimensions and six lines in four. In each, the conjectured optimum repeats two of the coordinate axes. Prove that any \(5\) lines in \(\mathbb{R}^3\) satisfy \(S\le 4\pi\), and that any \(6\) lines in \(\mathbb{R}^4\) satisfy \(S\le 13\pi/2\).

**Submit solution**

---

# \(N\) lines in \(\mathbb{R}^d\)

**13 points**  
**Judged**  
**Open question**

Fejes Tóth's conjecture from the Setting, for every \(N\) and every \(d\). For \(N\) lines in \(\mathbb{R}^d\), write \(N=qd+s\) with \(0\le s<d\), and let

\[
M(N,d)=s\binom{q+1}{2}+(d-s)\binom{q}{2}.
\]

Prove or disprove: every \(N\) lines in \(\mathbb{R}^d\) satisfy

\[
S\le \left(\binom{N}{2}-M(N,d)\right)\frac{\pi}{2}.
\]

This is the value attained by splitting the lines as evenly as possible among \(d\) mutually orthogonal directions. Settling any infinite family not already covered above counts as partial progress.

**Submit solution**

---

# Uphill paths on the hypercube

Label the vertices of the hypercube to make as few uphill paths as possible. IMO 2022 settled the grid; the cube is still open.

Let \(G\) be a finite simple graph on \(n\) vertices. A *labelling* of \(G\) is a bijection \(f\) from \(V(G)\) to \(\{1,2,\ldots,n\}\). Fix a labelling.

- A vertex \(v\) is a *valley* if every neighbour \(w\) of \(v\) has \(f(w)>f(v)\). An isolated vertex counts as a valley.
- An *uphill path* is a sequence \((v_1,v_2,\ldots,v_k)\) with \(k\ge 1\) in which \(v_1\) is a valley, \(v_i\) and \(v_{i+1}\) are adjacent for each \(i\), and \(f(v_1)<f(v_2)<\cdots<f(v_k)\). A valley on its own (\(k=1\)) counts as an uphill path.

Let \(U(G)\) be the smallest possible number of uphill paths, taken over all labellings of \(G\).

IMO 2022 Problem 6 asks for \(U\) of the \(n\times n\) grid graph. The answer is \(2n^2-2n+1\).

This column asks about the \(d\)-dimensional hypercube \(Q_d\). Its vertex set is \(\{0,1\}^d\), and two vertices are adjacent when they differ in exactly one coordinate. \(Q_d\) has \(2^d\) vertices and \(d\cdot 2^{d-1}\) edges.

## What to hand in

For **C1 to C4**, hand in the values, and for each value an explicit labelling that attains it as a list of the \(2^d\) vertices in increasing label order, written as 0/1 strings. These cells are marked correct on the values alone, but a value with no labelling behind it will not survive the later cells, which build on the construction.

For **C5**, hand in either a labelling of \(Q_9\) in the same format, whose uphill paths will be counted mechanically, or a proof of the lower bound.

For **C6**, hand in all three of:

1. the value;
2. an explicit labelling that attains it, in the same format;
3. a proof that no labelling gives fewer uphill paths.

A lower-bound proof may be computer-assisted. If it is, include the code; it must run in under 10 minutes on a laptop, and you must explain why the computation proves the bound. Say clearly which cells you consider solved and which are partial.

---

# \(U(Q_3)\) and \(U(Q_4)\)

**1 point**  
**Checked instantly**

The two smallest interesting cubes: \(Q_3\) has \(8\) vertices and \(12\) edges, \(Q_4\) has \(16\) vertices and \(32\) edges. Determine \(U(Q_3)\) and \(U(Q_4)\).

**Submit solution**

---

# \(U(Q_5)\)

**2 points**  
**Checked instantly**

\(Q_5\) has \(32\) vertices and \(80\) edges. Determine \(U(Q_5)\).

**Submit solution**

---

# \(U(Q_6)\)

**3 points**  
**Checked instantly**

\(Q_6\) has \(64\) vertices and \(192\) edges. Determine \(U(Q_6)\).

**Submit solution**

---

# \(U(Q_7)\) and \(U(Q_8)\)

**5 points**  
**Checked instantly**

Two larger cubes: \(Q_7\) has \(128\) vertices and \(448\) edges, \(Q_8\) has \(256\) vertices and \(1024\) edges. Determine \(U(Q_7)\) and \(U(Q_8)\).

**Submit solution**

---

# Bounds for \(U(Q_9)\)

**8 points**  
**Judged**

\(Q_9\) has \(512\) vertices and \(2304\) edges. The best bounds known to the organisers are \(2368\le U(Q_9)\le 2400\); the lower bound is unpublished. Improve either one: prove that \(U(Q_9)\ge 2369\), or exhibit a labelling of \(Q_9\) with at most \(2399\) uphill paths.

**Submit solution**

---

# \(U(Q_9)\)

**13 points**  
**Judged**  
**Open question**

The same cube, settled completely. Determine \(U(Q_9)\) exactly, with proof of both bounds.

**Submit solution**
