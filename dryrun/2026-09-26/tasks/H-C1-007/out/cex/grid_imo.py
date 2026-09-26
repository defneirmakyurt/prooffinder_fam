"""Referee H-C1-007: external cross-check of the counting semantics.

The statement quotes IMO 2022 P6: U(n x n grid) = 2n^2 - 2n + 1.  For n = 2 and n = 3 this
is exhaustively checkable (4! and 9! labellings).  If the subject's/checker's reading of
"uphill path" were wrong, these published values would not come out.  Note
2n^2-2n+1 = |E| + 1 for the grid, so this also witnesses that Step 5 is TIGHT and therefore
not over-strong.  Stdlib, exact integers.
"""
import itertools
import time


def grid(n):
    idx = {(i, j): i * n + j for i in range(n) for j in range(n)}
    nbr = [[] for _ in range(n * n)]
    for i in range(n):
        for j in range(n):
            for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                a, b = i + di, j + dj
                if 0 <= a < n and 0 <= b < n:
                    nbr[idx[(i, j)]].append(idx[(a, b)])
    return [tuple(x) for x in nbr]


def score(order, nbr):
    n = len(order)
    lab = [0] * n
    for i, v in enumerate(order, 1):
        lab[v] = i
    N = [0] * n
    tot = 0
    for v in order:
        s = 0
        low = False
        for w in nbr[v]:
            if lab[w] < lab[v]:
                low = True
                s += N[w]
        N[v] = s if low else 1
        tot += N[v]
    return tot


def literal(order, nbr):
    n = len(order)
    lab = [0] * n
    for i, v in enumerate(order, 1):
        lab[v] = i
    val = [v for v in range(n) if all(lab[w] > lab[v] for w in nbr[v])]
    tot = 0
    stack = [(v,) for v in val]
    while stack:
        p = stack.pop()
        tot += 1
        for w in nbr[p[-1]]:
            if lab[w] > lab[p[-1]]:
                stack.append(p + (w,))
    return tot


for n in (2, 3):
    nbr = grid(n)
    V = n * n
    E = sum(len(a) for a in nbr) // 2
    t0 = time.time()
    best = None
    k = 0
    for o in itertools.permutations(range(V)):
        t = score(o, nbr)
        if best is None or t < best:
            best = t
            best_o = o
        k += 1
    assert score(best_o, nbr) == literal(best_o, nbr)
    print("%dx%d grid: |V|=%d |E|=%d, exhaustive over all %d! = %d labellings, "
          "min = %d ; IMO 2022 P6 value 2n^2-2n+1 = %d ; |E|+1 = %d ; %.2fs"
          % (n, n, V, E, V, k, best, 2 * n * n - 2 * n + 1, E + 1, time.time() - t0))
