#!/usr/bin/env python3
"""
check_identity.py -- stdlib only.  Sanity test (NOT a proof; the proof is out/proof.md)
of the identity, for a labelling f of Q_d with N(v) = #uphill paths ending at v,
S = {v : N(v) >= 2}, up(v) = #neighbours with larger label:

   P(f) = 2^d + (d-1)|S| + sum_{u in S} (N(u)-2) up(u)          (*)

and of the structural facts used in its proof:
   (a) V \\ S induces a forest whose number of components equals the number of valleys;
   (b) every neighbour of an S-vertex with larger label lies in S.
Also evaluates the files given on the command line (labellings, verify.py format).

Usage: python3 check_identity.py [ntrials] [file ...]
"""
import random
import sys


def analyse(d, order):
    n = 2 ** d
    lab = [0] * n
    for i, v in enumerate(order):
        lab[v] = i
    N = [0] * n
    valleys = 0
    for v in order:
        nb = [v ^ (1 << j) for j in range(d)]
        low = [w for w in nb if lab[w] < lab[v]]
        N[v] = (0 if low else 1) + sum(N[w] for w in low)
        valleys += 0 if low else 1
    P = sum(N)
    S = [v for v in range(n) if N[v] >= 2]
    Sset = set(S)
    up = lambda u: sum(1 for j in range(d) if lab[u ^ (1 << j)] > lab[u])
    rhs = 2 ** d + (d - 1) * len(S) + sum((N[u] - 2) * up(u) for u in S)
    # (a) forest on T = V \ S with #components == #valleys
    T = [v for v in range(n) if v not in Sset]
    eT = sum(1 for v in T for j in range(d) if (v ^ (1 << j)) > v and (v ^ (1 << j)) not in Sset)
    par = list(range(n))

    def find(x):
        while par[x] != x:
            par[x] = par[par[x]]
            x = par[x]
        return x
    cyc = False
    for v in T:
        for j in range(d):
            w = v ^ (1 << j)
            if w > v and w not in Sset:
                a, b = find(v), find(w)
                if a == b:
                    cyc = True
                par[a] = b
    comps = len({find(v) for v in T})
    okA = (not cyc) and comps == valleys and eT == len(T) - valleys
    okB = all((u ^ (1 << j)) in Sset for u in S for j in range(d) if lab[u ^ (1 << j)] > lab[u])
    return P, rhs, len(S), valleys, okA, okB


def main():
    ntr = int(sys.argv[1]) if len(sys.argv) > 1 else 200
    rng = random.Random(12345)
    bad = 0
    for t in range(ntr):
        d = 1 + t % 9
        order = list(range(2 ** d))
        mode = t % 3
        if mode == 0:
            rng.shuffle(order)
        elif mode == 1:
            order.sort(key=lambda v: (bin(v).count("1"), rng.random()))
        else:  # random local perturbation of weight order
            order.sort(key=lambda v: bin(v).count("1") + 2.5 * rng.random())
        P, rhs, s, V, okA, okB = analyse(d, order)
        if P != rhs or not okA or not okB:
            bad += 1
            print("MISMATCH d=%d P=%d rhs=%d okA=%s okB=%s" % (d, P, rhs, okA, okB))
    print("random trials: %d, mismatches: %d" % (ntr, bad))
    for fn in sys.argv[2:]:
        rows = [r.strip() for r in open(fn) if r.strip()]
        d = len(rows[0])
        P, rhs, s, V, okA, okB = analyse(d, [int(r, 2) for r in rows])
        print("%s: d=%d P=%d rhs=%d |S|=%d valleys=%d forest&comps=%s upclosed=%s"
              % (fn, d, P, rhs, s, V, okA, okB))


if __name__ == "__main__":
    main()
