"""Sanity check (NOT part of the proof, which is symbolic in k) of the lower-bound orbit
of lambda^(k) = (k-2, k-2, k-3, ..., 3, 2, 2, 1) for k in [KMIN, KMAX] (stdlib only).
Checks, by direct iteration of B:
  (a) B^t(lambda) = P(h(t), b(t)) for 0 <= t <= t* = k^2-4k+2, with
      h(t) = 1 + (t mod (k-1)),  b(t) = 1 + ((t-2) mod k)   (b(t) = t-1 mod k in {1..k}),
      where P(h,b) = delta_{k-1} - cell(diag k-1,row h) + cells(diag k, rows b, b+1 mod k);
  (b) B^{t*}(lambda) = (k, k-1, k-3, k-4, ..., 2) and B^{t*+1}(lambda) = delta_{k-1}+e_3;
  (c) B^{t*+1}(lambda) is cyclic (returns after k steps), B^{t*}(lambda) is not cyclic
      (its forward orbit never returns to it: checked on k*(k-1) + 5 further steps, and
      its energy strictly exceeds that of its image).
Usage: python3 verify_lower_orbit.py KMIN KMAX"""
import sys

def B(lam):
    s = len(lam)
    new = [x - 1 for x in lam if x > 1] + [s]
    return tuple(sorted(new, reverse=True))

def from_cells(cells):
    rows = {}
    for (i, j) in cells:
        rows[i] = rows.get(i, 0) + 1
    lam = tuple(rows[i] for i in sorted(rows))
    # must be a Young diagram: row i has cells (i,1..lam_i) and lam weakly decreasing
    for (i, j) in cells:
        assert j <= rows[i]
    assert all(lam[a] >= lam[a + 1] for a in range(len(lam) - 1))
    assert sorted(rows) == list(range(1, len(rows) + 1))
    return lam

def cell(d, r):          # diagonal d, row r  ->  (row, column)
    return (r, d + 1 - r)

def P(k, h, b):
    cells = set()
    for d in range(1, k):
        for r in range(1, d + 1):
            cells.add(cell(d, r))
    cells.remove(cell(k - 1, h))
    b2 = b + 1 if b < k else 1
    cells.add(cell(k, b))
    cells.add(cell(k, b2))
    return from_cells(cells)

def energy(lam):
    return sum(i + j for i, x in enumerate(lam, 1) for j in range(1, x + 1))

def check(k):
    lam = tuple([k - 2, k - 2] + list(range(k - 3, 1, -1)) + [2, 1])
    assert sum(lam) == k * (k - 1) // 2 + 1
    tstar = k * k - 4 * k + 2
    mu = lam
    for t in range(tstar + 1):
        h = 1 + (t % (k - 1))
        b = 1 + ((t - 2) % k)
        assert mu == P(k, h, b), (k, t)
        if t < tstar:
            mu = B(mu)
    assert mu == tuple([k, k - 1] + list(range(k - 3, 1, -1))), (k, mu)
    nu = B(mu)
    delta = list(range(k - 1, 0, -1))
    d3 = delta[:]
    d3[2] += 1
    assert nu == tuple(d3)
    x = nu
    for _ in range(k):
        x = B(x)
    assert x == nu                       # cyclic
    assert energy(nu) == energy(mu) - 1  # strict energy drop
    x = nu
    for _ in range(k * (k - 1) + 5):
        assert x != mu
        x = B(x)
    return tstar + 1

if __name__ == "__main__":
    kmin, kmax = int(sys.argv[1]), int(sys.argv[2])
    for k in range(kmin, kmax + 1):
        d = check(k)
        assert d == (k - 1) * (k - 3)
    print(f"lower-bound orbit verified for k={kmin}..{kmax}: d_B(lambda^(k)) = (k-1)(k-3)")
