"""Independent exhaustive minimisation over ALL (2^d)! labellings of Q_d.

Different code, different method and a different (weaker) pruning rule from the
subject's bnb.py.  Exact integers only.

Method.  Build the labelling one label at a time.  After m labels the placed set is
S (labels 1..m) and every unplaced vertex has a larger label than every placed one.
For a vertex v receiving label m+1, its lower neighbours are exactly its neighbours
in S, so  N(v) = 1 if v has no neighbour in S, else sum of N(w) over neighbours w in S.
(Straight from the definitions; N(v) = #uphill paths ending at v.)

State merging.  Running this forward pass for the rest of the ordering needs, from
the past, only S and the values N(w) for placed w that still have an unplaced
neighbour: those are the only past N values any later vertex can read.  So two
prefixes with the same (S, N on the boundary of S) admit exactly the same set of
future costs, and keeping the cheaper prefix loses no optimum.  The DP therefore
explores every one of the (2^d)! label sequences, merging only provably equivalent
prefixes.  No symmetry reduction of any kind is used.

Pruning.  Every vertex has N >= 1 (induction on the label: a vertex is either a
valley, N >= 1, or has a lower neighbour w with N(v) >= N(w) >= 1).  So a prefix of
cost c with r vertices left yields total >= c + r; prefixes with c + r >= cutoff
cannot reach a total below cutoff and are dropped.  This is the ONLY bound used --
in particular the subject's LB(S) is not used, so this run is independent of it.

Usage: dp_exact.py <d> <cutoff>     cutoff = None means no pruning at all.
"""
import sys


def dp_min(d, cutoff=None, verbose=True):
    n = 1 << d
    NB = [[v ^ (1 << j) for j in range(d)] for v in range(n)]
    cur = {(0, ()): 0}                      # (S, boundary N values) -> min cost
    total_states = 0
    for level in range(n):
        nxt = {}
        for (S, bnd), cost in cur.items():
            Nd = dict(bnd)
            for v in range(n):
                if (S >> v) & 1:
                    continue
                low = [w for w in NB[v] if (S >> w) & 1]
                Nv = 1 if not low else sum(Nd[w] for w in low)
                c2 = cost + Nv
                rem = n - level - 1
                if cutoff is not None and c2 + rem >= cutoff:
                    continue
                S2 = S | (1 << v)
                Nd2 = dict(Nd)
                Nd2[v] = Nv
                b2 = tuple((w, Nd2[w]) for w in range(n)
                           if (S2 >> w) & 1 and any(not (S2 >> x) & 1 for x in NB[w]))
                k = (S2, b2)
                if k not in nxt or nxt[k] > c2:
                    nxt[k] = c2
        cur = nxt
        total_states += len(cur)
        if verbose:
            print("  level %2d: %d states" % (level + 1, len(cur)), flush=True)
        if not cur:
            break
    if verbose:
        print("  total states kept: %d" % total_states)
    if not cur:
        return None
    assert list(cur.keys()) == [((1 << n) - 1, ())], "unexpected terminal state"
    return min(cur.values())


if __name__ == "__main__":
    d = int(sys.argv[1])
    cutoff = None if sys.argv[2] == "none" else int(sys.argv[2])
    r = dp_min(d, cutoff)
    if r is None:
        print("d=%d cutoff=%s -> NO labelling of Q_%d has fewer than %s uphill paths"
              % (d, cutoff, d, cutoff))
    else:
        print("d=%d cutoff=%s -> exact minimum over ALL %d! labellings = %d"
              % (d, cutoff, 1 << d, r))
