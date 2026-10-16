"""Referee H-C1-005: independent tools.

count_literal(d, order): counts uphill paths STRAIGHT FROM THE DEFINITION -- it
enumerates every sequence (v_1,...,v_k), k>=1, with v_1 a valley, consecutive
vertices adjacent, labels strictly increasing.  No counting recursion is used,
so this is logically independent of the subject's R2 identity and of the
provided checker's recursion.  Exact integers only.
"""


def nbrs(d, v):
    return [v ^ (1 << j) for j in range(d)]


def count_literal(d, order):
    n = 1 << d
    assert sorted(order) == list(range(n)), "not a bijection"
    f = [0] * n
    for i, v in enumerate(order, 1):
        f[v] = i
    total = 0
    for v in range(n):
        if all(f[w] > f[v] for w in nbrs(d, v)):      # v is a valley
            stack = [v]                               # extend path by DFS
            while stack:
                x = stack.pop()
                total += 1                            # one uphill path ends at x
                for w in nbrs(d, x):
                    if f[w] > f[x]:
                        stack.append(w)
    return total


def to_lines(d, order):
    return "".join(format(v, "0%db" % d) + "\n" for v in order)
