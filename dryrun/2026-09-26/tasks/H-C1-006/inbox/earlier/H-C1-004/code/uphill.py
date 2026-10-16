"""Independent uphill-path counter for Q_d (stdlib only, exact ints).

N(v) = number of uphill paths ending at v.
  * k = 1: the path (v) is uphill iff v is a valley.
  * k >= 2: (v_1..v_{k-1}, v) is uphill iff (v_1..v_{k-1}) is an uphill path ending at a
    neighbour w of v with f(w) < f(v).  Distinct w / distinct prefixes give distinct paths.
So N(v) = [v valley] + sum_{w ~ v, f(w) < f(v)} N(w); total = sum_v N(v).
"""


def nbrs(d, v):
    return [v ^ (1 << j) for j in range(d)]


def count(d, order):
    """order[i] = vertex (int) with label i+1."""
    n = 1 << d
    assert sorted(order) == list(range(n))
    f = [0] * n
    for i, v in enumerate(order):
        f[v] = i
    N = [0] * n
    for v in order:
        low = [w for w in nbrs(d, v) if f[w] < f[v]]
        N[v] = (0 if low else 1) + sum(N[w] for w in low)
    return sum(N)


def to_lines(d, order):
    return "".join(format(v, "0%db" % d) + "\n" for v in order)
