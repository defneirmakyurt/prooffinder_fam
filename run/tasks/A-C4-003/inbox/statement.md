\documentclass[11pt]{article}

\usepackage[a4paper,margin=1in]{geometry}
\usepackage{amsmath,amssymb,amsthm}
\usepackage{enumitem}
\usepackage{microtype}
\usepackage{parskip}

% -------------------------------------------------------------------
% Environments
% -------------------------------------------------------------------
\theoremstyle{definition}
\newtheorem*{definition}{Definition}
\newtheorem*{conjecture}{Conjecture}
\newtheorem*{example}{Example}

% -------------------------------------------------------------------
% Notation
% -------------------------------------------------------------------
\newcommand{\R}{\mathbb{R}}

% A problem cell: \cell{<number>}{<title>}{<points>}
\newcommand{\cell}[3]{%
  \section*{Cell #1: #2\hfill{\normalsize\mdseries #3}}}

\title{Angles Between Lines\\[0.4em]\large Problem Description}
\author{}
\date{}

\begin{document}
\maketitle

% ===================================================================
\section*{Overview}
% ===================================================================

How large can the sum of pairwise angles between $N$ lines through
the origin be? Fejes T\'oth conjectured in 1959 that orthogonal lines
win.

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

The question is how large $S$ can be.

\begin{conjecture}[L.~Fejes T\'oth, 1959]
$S$ is maximised by taking $d$ mutually orthogonal lines, each used
either
\[
  \left\lfloor \frac{N}{d} \right\rfloor
  \qquad \text{or} \qquad
  \left\lceil \frac{N}{d} \right\rceil
\]
times.
\end{conjecture}

\begin{example}
When $N = d + k$ with $0 \leq k \leq d$, that configuration (the $d$
coordinate axes, $k$ of them used twice) has
\[
  S = \left( \binom{N}{2} - k \right) \frac{\pi}{2},
\]
because exactly $k$ pairs of lines coincide and every other pair is
orthogonal.
\end{example}

Each cell below asks you to prove this bound, or a special case of
it. Unless a cell says otherwise, you need a complete proof. Citing a
published result for the statement you are asked to prove does not
count.

% ===================================================================
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

% ===================================================================
\cell{1}{Lines in the Plane}{1 point}
% ===================================================================

We begin in the plane ($d = 2$), where the conjectured optimum splits
the $N$ lines as evenly as possible between two perpendicular
directions.

Let $\ell_1, \ldots, \ell_N$ be lines in $\R^2$. Prove that
\[
  S(\ell_1, \ldots, \ell_N)
  \leq \frac{\pi}{2} \left\lfloor \frac{N^2}{4} \right\rfloor.
\]

% ===================================================================
\cell{2}{An Orthogonality Lemma}{2 points}
% ===================================================================

A statement about a chain of vectors, in which each vector may fail
to be orthogonal only to its immediate neighbours in the list.

Let $m \geq 2$ and let $x_1, \ldots, x_m$ be unit vectors in
$\R^{m-1}$ with
\[
  \langle x_i, x_j \rangle = 0
  \qquad \text{whenever } |i - j| \geq 2.
\]
Prove that
\[
  \sum_{i=1}^{m-1} \theta(x_i, x_{i+1}) \leq (m - 2) \frac{\pi}{2},
\]
where
\[
  \theta(x, y) = \arccos \bigl| \langle x, y \rangle \bigr|.
\]

% ===================================================================
\cell{3}{$d + 1$ Lines in $\R^d$}{3 points}
% ===================================================================

The first case in every dimension: one line more than the dimension,
$N = d + 1$, where the conjectured optimum repeats exactly one of the
$d$ coordinate axes.

Let $d \geq 1$. Prove that any $d + 1$ lines in $\R^d$ satisfy
\[
  S \leq \left( \binom{d+1}{2} - 1 \right) \frac{\pi}{2}.
\]

% ===================================================================
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

% ===================================================================
\cell{5}{$d + 2$ Lines in $\R^d$}{8 points}
% ===================================================================

The case $N = d + 2$ in every dimension, with the same conjectured
optimum: the $d$ coordinate axes, two of them repeated.

Prove that for every $d \geq 2$, any $d + 2$ lines in $\R^d$ satisfy
\[
  S \leq \left( \binom{d+2}{2} - 2 \right) \frac{\pi}{2}.
\]

% ===================================================================
\cell{6}{$N$ Lines in $\R^d$}{13 points}
% ===================================================================

\textbf{Open question.}

Fejes T\'oth's conjecture from the setting, for every $N$ and every
$d$.

For $N$ lines in $\R^d$, write
\[
  N = qd + s, \qquad 0 \leq s < d,
\]
and let
\[
  M(N, d) = s \binom{q+1}{2} + (d - s) \binom{q}{2}.
\]
Prove or disprove: every $N$ lines in $\R^d$ satisfy
\[
  S \leq \left( \binom{N}{2} - M(N, d) \right) \frac{\pi}{2}.
\]

This is the value attained by splitting the lines as evenly as
possible among $d$ mutually orthogonal directions. Settling any
infinite family not already covered above counts as partial progress.

\end{document}
