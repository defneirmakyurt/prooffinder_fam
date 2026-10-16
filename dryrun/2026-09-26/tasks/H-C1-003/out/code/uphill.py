"""Shared helpers (stdlib only, exact integers).

Vertices of Q_d are ints 0..2^d-1 (bit j = coordinate); v ~ w iff v ^ w is a power of 2.
An "order" is the list of vertices in increasing label order: f(order[i]) = i+1.
"""


def nbrs(v, d):
    return [v ^ (1 << j) for j in range(d)]


def count_uphill(d, order):
    """Internal fast scorer (same recurrence as the checker):
    N(v) = [v valley] + sum_{w ~ v, f(w) < f(v)} N(w); total = sum_v N(v)."""
    n = 1 << d
    f = [0] * n
    for i, v in enumerate(order, 1):
        f[v] = i
    N = [0] * n
    total = 0
    for v in order:
        lower = [w for w in nbrs(v, d) if f[w] < f[v]]
        N[v] = (1 if not lower else 0) + sum(N[w] for w in lower)
        total += N[v]
    return total


def to_lines(d, order):
    return "".join(format(v, "0%db" % d) + "\n" for v in order)


def brute_paths(d, order):
    """Independent slow count: enumerate uphill paths explicitly by DFS from each valley."""
    n = 1 << d
    f = [0] * n
    for i, v in enumerate(order, 1):
        f[v] = i
    valleys = [v for v in range(n) if all(f[w] > f[v] for w in nbrs(v, d))]
    cnt = 0
    stack = [(v,) for v in valleys]
    while stack:
        p = stack.pop()
        cnt += 1
        last = p[-1]
        for w in nbrs(last, d):
            if f[w] > f[last]:
                stack.append(p + (w,))
    return cnt
