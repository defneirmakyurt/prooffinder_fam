#!/usr/bin/env python3
"""check_forest.py -- stdlib only. For each file holding one line of 2^d characters (char v = '1' iff
vertex v is in F), check that F induces a forest in Q_d and report |S| = 2^d - |F|, e(S), parity split of S,
number of components c of F, and the identity c + e(S) = (d-1)|S| - (d-2)2^{d-1}."""
import sys

for fn in sys.argv[1:]:
    s = open(fn).read().strip()
    n = len(s)
    d = n.bit_length() - 1
    assert 2 ** d == n
    F = [s[v] == "1" for v in range(n)]
    par = list(range(n))

    def find(x):
        while par[x] != x:
            par[x] = par[par[x]]
            x = par[x]
        return x
    cyc = 0
    eF = 0
    for v in range(n):
        if F[v]:
            for j in range(d):
                w = v ^ (1 << j)
                if w > v and F[w]:
                    eF += 1
                    a, b = find(v), find(w)
                    if a == b:
                        cyc += 1
                    else:
                        par[a] = b
    comps = len({find(v) for v in range(n) if F[v]})
    S = [v for v in range(n) if not F[v]]
    eS = sum(1 for v in S for j in range(d) if (v ^ (1 << j)) > v and not F[v ^ (1 << j)])
    even = sum(1 for v in S if bin(v).count("1") % 2 == 0)
    ident = comps + eS == (d - 1) * len(S) - (d - 2) * 2 ** (d - 1)
    print("%s: d=%d forest=%s |S|=%d e(S)=%d S_even=%d S_odd=%d components=%d identity_ok=%s"
          % (fn, d, cyc == 0, len(S), eS, even, len(S) - even, comps, ident))
