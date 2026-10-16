"""Uphill-path counting for Q_d. Stdlib only, exact integer arithmetic.

Conventions: a vertex of Q_d is an int 0..2^d-1; bit j of the int is coordinate j.
A labelling is given as a list `order` of the 2^d vertices: order[i] receives label i+1.
"""
import sys


def neighbours(d):
    n = 1 << d
    return [tuple(v ^ (1 << j) for j in range(d)) for v in range(n)]


def count_recurrence(order, nbr):
    """Total number of uphill paths, via N(v) = [v valley] + sum_{w~v, f(w)<f(v)} N(w)."""
    n = len(order)
    lab = [0] * n
    for i, v in enumerate(order):
        lab[v] = i + 1
    N = [0] * n
    total = 0
    for v in order:                      # increasing label order
        s = 0
        low = 0
        for w in nbr[v]:
            if lab[w] < lab[v]:
                low += 1
                s += N[w]
        N[v] = (1 if low == 0 else 0) + s
        total += N[v]
    return total, N, lab


def count_bruteforce(order, nbr):
    """Independent count: explicitly enumerate every uphill path by DFS."""
    n = len(order)
    lab = [0] * n
    for i, v in enumerate(order):
        lab[v] = i + 1
    valleys = [v for v in range(n) if all(lab[w] > lab[v] for w in nbr[v])]
    total = 0
    stack = [v for v in valleys]
    while stack:
        v = stack.pop()
        total += 1                       # the path currently ending at v
        for w in nbr[v]:
            if lab[w] > lab[v]:
                stack.append(w)
    return total


def stats(order, nbr):
    """(total, #valleys, #local maxima, multiset of down-degrees)."""
    total, N, lab = count_recurrence(order, nbr)
    n = len(order)
    valleys = sum(1 for v in range(n) if all(lab[w] > lab[v] for w in nbr[v]))
    maxima = sum(1 for v in range(n) if all(lab[w] < lab[v] for w in nbr[v]))
    return total, valleys, maxima, N


def read_labelling(path, d):
    with open(path) as f:
        lines = [ln.strip() for ln in f if ln.strip()]
    assert len(lines) == (1 << d), "expected %d lines, got %d" % (1 << d, len(lines))
    order = []
    for ln in lines:
        assert len(ln) == d and set(ln) <= {"0", "1"}, "bad line %r" % ln
        # line is written most-significant bit first: ln[0] is coordinate d-1
        v = 0
        for j, ch in enumerate(ln):
            if ch == "1":
                v |= 1 << (d - 1 - j)
        order.append(v)
    assert sorted(order) == list(range(1 << d)), "not a bijection"
    return order


def write_labelling(path, order, d):
    with open(path, "w") as f:
        for v in order:
            f.write("".join("1" if (v >> (d - 1 - j)) & 1 else "0" for j in range(d)) + "\n")


if __name__ == "__main__":
    d = int(sys.argv[2])
    order = read_labelling(sys.argv[1], d)
    nbr = neighbours(d)
    t1, N, lab = count_recurrence(order, nbr)
    t2 = count_bruteforce(order, nbr)
    tot, val, mx, _ = stats(order, nbr)
    assert t1 == t2, "recurrence %d != explicit enumeration %d" % (t1, t2)
    print("%s d=%d uphill_paths=%d (recurrence) =%d (explicit enumeration) valleys=%d local_maxima=%d"
          % (sys.argv[1], d, t1, t2, val, mx))
