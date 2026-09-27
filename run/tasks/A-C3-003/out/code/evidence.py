#!/usr/bin/env python3
"""Floating-point EVIDENCE ONLY (no proof step rests on this file). Stdlib only.

Checks, on random and adversarial inputs:
  (a) trig lemma R2:  sum_j sin(a_j) cos(D - a_j) <= sin(D)   for a_j >= 0, D = sum a_j <= pi/2
  (b) certificate R3: u_i = cos(T - D_i) > 0 and sum_j sin(phi_ij) u_j < u_i  when T < pi/2
  (c) matrix lemma R5: lambda_max(A) < 1 (power iteration), A_ij = sin(phi_ij), T < pi/2
  (d) target: S(l_1..l_{d+1}) <= (C(d+1,2)-1) pi/2 for random lines in R^d, d = 1..8,
      plus a hill-climb that tries to push S above the bound, and two equality examples.
Usage:  python3 evidence.py [seed]
"""
import math
import random
import sys

TOL = 1e-12


def rand_unit(d, rng):
    while True:
        v = [rng.gauss(0, 1) for _ in range(d)]
        n = math.sqrt(sum(t * t for t in v))
        if n > 1e-9:
            return [t / n for t in v]


def angle_sum(xs):
    s = 0.0
    m = len(xs)
    for i in range(m):
        for j in range(i + 1, m):
            g = abs(sum(a * b for a, b in zip(xs[i], xs[j])))
            g = min(1.0, g)
            s += math.acos(g)
    return s


def rand_phi(n, rng, T_target):
    """symmetric phi with zero diagonal, random sparsity, total T_target."""
    pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
    w = [rng.random() ** rng.choice([1, 3, 8]) if rng.random() < 0.7 else 0.0 for _ in pairs]
    if sum(w) == 0:
        w[0] = 1.0
    s = sum(w)
    phi = [[0.0] * n for _ in range(n)]
    for (i, j), wt in zip(pairs, w):
        phi[i][j] = phi[j][i] = T_target * wt / s
    return phi


def lam_max(A, iters=3000):
    n = len(A)
    v = [1.0] * n
    lam = 0.0
    for _ in range(iters):
        w = [sum(A[i][j] * v[j] for j in range(n)) for i in range(n)]
        nrm = math.sqrt(sum(t * t for t in w))
        if nrm == 0:
            return 0.0
        v = [t / nrm for t in w]
        lam = nrm
    # Rayleigh quotient at the final vector
    w = [sum(A[i][j] * v[j] for j in range(n)) for i in range(n)]
    return sum(a * b for a, b in zip(v, w))


def main():
    seed = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    rng = random.Random(seed)

    # (a) trig lemma
    worst_a = -1e9
    for _ in range(20000):
        k = rng.randint(1, 8)
        D = rng.uniform(0, math.pi / 2)
        w = [rng.random() for _ in range(k)]
        s = sum(w)
        a = [D * t / s for t in w]
        lhs = sum(math.sin(x) * math.cos(D - x) for x in a)
        worst_a = max(worst_a, lhs - math.sin(D))
    print(f"(a) trig lemma: max(lhs - sin D) = {worst_a:.3e}  (should be <= ~0)")

    # (b),(c) certificate and matrix lemma
    worst_b = -1e9
    worst_c = 0.0
    for _ in range(4000):
        n = rng.randint(2, 7)
        T = (math.pi / 2) * (1 - 10 ** rng.uniform(-6, 0))
        phi = rand_phi(n, rng, T)
        D = [sum(phi[i]) for i in range(n)]
        u = [math.cos(T - D[i]) for i in range(n)]
        assert min(u) > 0
        for i in range(n):
            lhs = sum(math.sin(phi[i][j]) * u[j] for j in range(n) if j != i)
            worst_b = max(worst_b, lhs - u[i])
        A = [[math.sin(phi[i][j]) if i != j else 0.0 for j in range(n)] for i in range(n)]
        worst_c = max(worst_c, lam_max(A))
    print(f"(b) certificate: max(sum_j sin(phi_ij) u_j - u_i) = {worst_b:.3e}  (should be < 0)")
    print(f"(c) matrix lemma: max lambda_max over tests = {worst_c:.12f}  (should be < 1)")

    # (d) target on random lines, then hill-climb
    worst_d = -1e9
    for d in range(1, 9):
        bound = (math.comb(d + 1, 2) - 1) * math.pi / 2
        for _ in range(2000):
            xs = [rand_unit(d, rng) for _ in range(d + 1)]
            worst_d = max(worst_d, angle_sum(xs) - bound)
    print(f"(d1) random lines d=1..8: max(S - bound) = {worst_d:.3e}  (should be <= ~0)")

    worst_h = -1e9
    for d in range(1, 6):
        bound = (math.comb(d + 1, 2) - 1) * math.pi / 2
        for _ in range(30):
            xs = [rand_unit(d, rng) for _ in range(d + 1)]
            cur = angle_sum(xs)
            step = 0.5
            for it in range(1500):
                i = rng.randrange(d + 1)
                y = [a + step * rng.gauss(0, 1) for a in xs[i]]
                nrm = math.sqrt(sum(t * t for t in y))
                if nrm < 1e-9:
                    continue
                y = [t / nrm for t in y]
                old = xs[i]
                xs[i] = y
                new = angle_sum(xs)
                if new >= cur:
                    cur = new
                else:
                    xs[i] = old
                if it % 300 == 299:
                    step *= 0.5
            worst_h = max(worst_h, cur - bound)
    print(f"(d2) hill-climb d=1..5: max(S - bound) = {worst_h:.3e}  (should be <= ~0, near 0)")

    # equality examples
    ex1 = angle_sum([[1, 0], [0.5, math.sqrt(3) / 2], [-0.5, math.sqrt(3) / 2]])
    print(f"(e1) three lines at 60 deg in R^2: S - pi = {ex1 - math.pi:.3e}")
    d = 4
    xs = [[1.0 if k == i else 0.0 for k in range(d)] for i in range(d)] + [[1.0, 0, 0, 0]]
    ex2 = angle_sum(xs)
    print(f"(e2) axes of R^4, e1 repeated: S - (C(5,2)-1)pi/2 = {ex2 - 9 * math.pi / 2:.3e}")


if __name__ == "__main__":
    main()
