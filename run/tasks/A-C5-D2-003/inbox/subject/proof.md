STATEMENT PROVED: For every 4 lines l_1,l_2,l_3,l_4 through the origin of R^2 (repetitions
allowed), S(l_1,l_2,l_3,l_4) = sum_{i<j} theta(l_i,l_j) <= 2*pi, where theta(l,l') =
arccos|<x,x'>| in [0,pi/2] for unit vectors x,x' spanning l,l'. This is A-C5's target
(C(d+2,2)-2)*pi/2 specialised to d=2, N=4: (C(4,2)-2)*pi/2 = (6-2)*pi/2 = 2*pi.

(This is Steps 1, 2 and 5 of A-C5-001's submission, verbatim and renumbered, isolated as their
own self-contained argument. Steps 3, 4, 6 of the original — the general-d weak bound and the
d>=3 gap — are not part of this narrower claim and are omitted.)

For each line l_i fix an arbitrary unit vector x_i spanning it (the sign of x_i is immaterial,
since only |<x_i,x_j>| appears below).

## Step 1 (identity: arccos + arcsin = pi/2)

For x in [-1,1], define phi(x) = arccos(x) + arcsin(x). Both arccos and arcsin are differentiable
on (-1,1) with arccos'(x) = -1/sqrt(1-x^2) and arcsin'(x) = 1/sqrt(1-x^2) (standard calculus
facts). Hence phi'(x) = 0 on (-1,1), so phi is constant there; by continuity it is constant on
all of [-1,1]. Evaluating at x=0: phi(0) = arccos(0) + arcsin(0) = pi/2 + 0 = pi/2. Hence

    arccos(x) + arcsin(x) = pi/2  for all x in [-1,1].                      (1)

## Step 2 (reduction to a lower bound on T)

Write a_ij = <x_i,x_j> for i != j. By definition theta(l_i,l_j) = arccos|a_ij|. Applying (1) with
x = |a_ij| in [0,1]:

    theta(l_i,l_j) = pi/2 - arcsin|a_ij|.

Summing over the 6 pairs i<j (N=4, C(4,2)=6) and setting T := sum_{i<j} arcsin|a_ij|:

    S = 6*(pi/2) - T = 3*pi - T.                                             (2)

Hence the target inequality S <= 2*pi is EXACTLY equivalent (pure algebraic rearrangement) to

    T >= pi.                                                                 (3)

So the whole task is to prove (3): T >= pi, i.e. sum_{i<j} arcsin|a_ij| >= pi, for every choice
of 4 unit vectors x_1,x_2,x_3,x_4 in R^2.

## Step 3 (exact proof of (3) for N=4, d=2)

A line in R^2 through the origin is uniquely determined by an angle phi in the circle group
R/(pi*Z) (circumference pi): the line is spanned by (cos phi, sin phi), and phi, phi' represent
the same line iff phi - phi' is a multiple of pi. For two lines with angles phi, phi', the acute
angle between them is theta = arccos|cos(phi-phi')|. For alpha = phi-phi' mod pi taken in [0,pi),
arccos|cos(alpha)| = min(alpha, pi-alpha) (standard fact: arccos(cos(alpha))=alpha for alpha in
[0,pi], and cos(pi-alpha)=-cos(alpha) has the same absolute value, so
arccos|cos(alpha)| = min(arccos(cos(alpha)), arccos(cos(pi-alpha))) = min(alpha,pi-alpha)).
Define h(x) := min(x,pi-x) for x in [0,pi]; so theta(l,l') = h(alpha) for any representative
alpha in [0,pi) of phi-phi' mod pi (h is well-defined on the class since h(alpha)=h(pi-alpha)).

Let the 4 lines have angles phi_1,...,phi_4 in R/(pi*Z) (repetitions allowed, i.e. some phi_i may
coincide). Relabel the 4 indices (a relabeling doesn't change S, a sum over unordered pairs of all
4 lines) so that representatives of phi_1,...,phi_4 in [0,pi) are in cyclic (non-decreasing, then
wrapping) order p_1 <= p_2 <= p_3 <= p_4, now indexed 1,2,3,4 in this cyclic order. Define the 4
consecutive gaps

    g_1 = p_2-p_1,  g_2 = p_3-p_2,  g_3 = p_4-p_3,  g_4 = pi-p_4+p_1  (wrap-around gap).

Each g_i >= 0 and g_1+g_2+g_3+g_4 = pi (telescoping sum over the full circle of circumference pi).

Compute all 6 pairwise theta's in terms of the g_i. For the 4 "adjacent" pairs (cyclic order
1-2,2-3,3-4,4-1): theta(l_1,l_2)=h(g_1), theta(l_2,l_3)=h(g_2), theta(l_3,l_4)=h(g_3),
theta(l_4,l_1)=h(g_4) (the two arcs between p_1,p_2 have lengths g_1 and pi-g_1, etc.). For the 2
"opposite" pairs: the two arcs between p_1,p_3 have lengths g_1+g_2 and pi-(g_1+g_2), so
theta(l_1,l_3)=h(g_1+g_2); similarly theta(l_2,l_4)=h(g_2+g_3). Hence

    S = h(g_1)+h(g_2)+h(g_3)+h(g_4) + h(g_1+g_2) + h(g_2+g_3) =: F(g_1,g_2,g_3,g_4).      (4)

Claim: F <= 2*pi whenever g_i >= 0 and sum g_i = pi.

Elementary bound: h(x) <= pi/2 for all x in [0,pi], since h(x)=min(x,pi-x) <= (x+(pi-x))/2 = pi/2
(the average of the two arguments of min upper-bounds the min).                (5)

At most one of g_1,...,g_4 exceeds pi/2: if g_j>pi/2 and g_k>pi/2 for j!=k, then g_j+g_k>pi, but
g_j+g_k <= g_1+g_2+g_3+g_4 = pi (the other two gaps are >=0), a contradiction.

Case A: all g_i <= pi/2. Then h(g_i)=g_i for each i (g_i<=pi/2<=pi-g_i), so
h(g_1)+..+h(g_4) = g_1+..+g_4 = pi. By (5), h(g_1+g_2)<=pi/2 and h(g_2+g_3)<=pi/2. Hence
F <= pi + pi/2 + pi/2 = 2*pi.

Case B: exactly one g_k > pi/2. For i!=k, g_i <= pi-g_k < pi/2 (since the other two gaps sum
with g_i to pi-g_k, and are >=0), so h(g_i)=g_i as in Case A. Also h(g_k)=pi-g_k (g_k>pi/2 means
g_k>pi-g_k). Hence h(g_1)+..+h(g_4) = (pi-g_k)+sum_{i!=k}g_i = (pi-g_k)+(pi-g_k) = 2*pi-2*g_k. By
(5), h(g_1+g_2)+h(g_2+g_3) <= pi. So F <= (2*pi-2*g_k)+pi = 3*pi-2*g_k < 3*pi-2*(pi/2) = 2*pi,
using g_k > pi/2 strictly.

In both cases F <= 2*pi. By (4), S = F <= 2*pi. This proves the target exactly, for every choice
of 4 lines in R^2, including all degenerate/repeated cases (some g_i=0, handled within Case A
since 0<=pi/2).

Equality is attained, e.g., by g=(0,pi/2,0,pi/2) (two coincident pairs of orthogonal lines: the
conjectured optimum: adjacent sum = 0+pi/2+0+pi/2=pi, opposite sum = h(pi/2)+h(pi/2)=pi, total
2*pi) and by g=(pi/4,pi/4,pi/4,pi/4) (4 evenly spaced lines: all h(g_i)=pi/4, adjacent sum=pi, and
g_1+g_2=g_2+g_3=pi/2 so opposite sum=pi, total 2*pi). Both cross-checked exactly in
out/code/check_d2.py (copied verbatim from A-C5-001/out/code/check_d2.py).

This completes a full, exact proof of S <= 2*pi for every 4 lines in R^2.
