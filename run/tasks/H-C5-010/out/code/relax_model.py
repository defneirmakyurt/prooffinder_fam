#!/usr/bin/env python3
"""
relax_model.py -- exhibits a vertex set T of Q_9 with |T| = 287 that satisfies EVERY local
constraint family used by the encoder (subcube upper bounds k = 2..8, subcube lower bounds
k = 5..8 for m = 287, and the global S-edge bound e(S) <= 2303 - 8*287 = 7) but is NOT a forest.
Purpose (diagnostic, not part of any proof): shows that for m = 287 the local relaxation is
satisfiable, so any UNSAT certificate at m <= 287 must use cycle clauses (CEGAR) or other
global information.  stdlib only, exact counting.

Input: a 144-vertex induced forest T0 of Q_8 (file of vertex ints, e.g. from
       cegar.py --d 8 --m 144 ... --out X  ->  X.forest).
Construction: T = T0 x {0}  u  ((T0 xor u) minus {one vertex}) x {1}, for the first unit vector u
and first vertex removal that satisfies all checks.
"""
import sys
from itertools import combinations

FB = {1: 2, 2: 3, 3: 5, 4: 10, 5: 18, 6: 36, 7: 72, 8: 144}


def acyclic(d, T):
    par = {v: v for v in T}

    def f(x):
        while par[x] != x:
            par[x] = par[par[x]]
            x = par[x]
        return x
    for v in T:
        for j in range(d):
            w = v ^ (1 << j)
            if w > v and w in par:
                a, b = f(v), f(w)
                if a == b:
                    return False
                par[a] = b
    return True


def check(d, T, m):
    n = 1 << d
    if len(T) != m:
        return "size"
    for k in range(2, d):
        L = m - ((1 << (d - k)) - 1) * FB[k]
        for coords in combinations(range(d), k):
            fm = sum(1 << c for c in coords)
            sub = [s for s in range(n) if s & ~fm == 0]
            for b in range(n):
                if b & fm:
                    continue
                c = sum(1 for s in sub if (b | s) in T)
                if c > FB[k]:
                    return "upper k=%d" % k
                if L > 0 and c < L:
                    return "lower k=%d" % k
    eS = sum(1 for u in range(n) for j in range(d) if u < (u ^ (1 << j)) and u not in T and (u ^ (1 << j)) not in T)
    if eS > (d * (1 << (d - 1)) - (d - 1) * m - 1):
        return "eS=%d" % eS
    return "OK eS=%d" % eS


def main():
    T0 = set(int(x) for x in open(sys.argv[1]).read().split())
    assert len(T0) == 144 and acyclic(8, T0)
    for j in range(8):
        T1 = set(v ^ (1 << j) for v in T0)
        for r in sorted(T1):
            T = set(T0) | set((v | 256) for v in T1 if v != r)
            res = check(9, T, 287)
            if res.startswith("OK"):
                print("relaxation model: u = e_%d, removed %d: %s; |T| = %d; acyclic = %s"
                      % (j + 1, r, res, len(T), acyclic(9, T)))
                print("T =", " ".join(map(str, sorted(T))))
                return
    print("no model of this shape")


if __name__ == "__main__":
    main()
