"""Independent exhaustive minimisation over ALL (2^d)! labellings of Q_d, level DP.

Same state-merging DP as dp_exact.py (validated there against the literal 8!
enumeration for d = 3 with NO pruning at all), plus lower bounds on the remaining
cost `future = sum_{v in R} N(v)`, R = unplaced vertices, P(v) = sum of N(w) over
placed neighbours w of v:

  B1 = sum_{v in R} max(1, P(v))
       from N(x) >= 1 (induction on the label) and N(x) >= P(x) (all placed
       neighbours of x are lower, and every term of the recursion is >= 0).

  B2 = [S empty] + sum_{v in R} P(v)
       + sum_{edges {u,v}, both ends in R} min(max(1,P(u)), max(1,P(v)))
       expanding N(v) for v in R, splitting the lower neighbours into placed
       (contributes exactly P(v)) and unplaced (each R-edge contributes N of its
       lower end, which is >= min over the two ends of max(1,P)); the valley term
       is dropped except at S = empty, where the label-1 vertex is a valley.

Both are valid lower bounds on `future`, so max(B1,B2) is.  Exact integers only.
Usage: dp2.py <d> <cutoff> [b1|b2|both]
"""
import sys


def run(d, cutoff, mode="both"):
    n = 1 << d
    NB = [[v ^ (1 << j) for j in range(d)] for v in range(n)]
    EDGES = [(u, v) for u in range(n) for v in NB[u] if u < v]
    cur = {(0, ()): 0}
    kept = 0
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
                if c2 >= cutoff:
                    continue
                S2 = S | (1 << v)
                Nd2 = dict(Nd)
                Nd2[v] = Nv
                # bounds for the child state S2
                P = {}
                b1 = 0
                sP = 0
                for x in range(n):
                    if not (S2 >> x) & 1:
                        p = sum(Nd2[w] for w in NB[x] if (S2 >> w) & 1)
                        P[x] = p
                        sP += p
                        b1 += p if p >= 1 else 1
                b2 = sP
                for (a, b) in EDGES:
                    if not (S2 >> a) & 1 and not (S2 >> b) & 1:
                        pa = P[a] if P[a] >= 1 else 1
                        pb = P[b] if P[b] >= 1 else 1
                        b2 += pa if pa < pb else pb
                if mode == "b1":
                    bound = b1
                elif mode == "b2":
                    bound = b2
                else:
                    bound = b1 if b1 > b2 else b2
                if c2 + bound >= cutoff:
                    continue
                b = tuple((w, Nd2[w]) for w in range(n)
                          if (S2 >> w) & 1 and any(not (S2 >> x) & 1 for x in NB[w]))
                k = (S2, b)
                if k not in nxt or nxt[k] > c2:
                    nxt[k] = c2
        cur = nxt
        kept += len(cur)
        print("  level %2d: %d states" % (level + 1, len(cur)), flush=True)
        if not cur:
            break
    print("  states kept: %d" % kept)
    if not cur:
        print("d=%d mode=%s -> NO labelling of Q_%d has fewer than %d uphill paths"
              % (d, mode, d, cutoff))
    else:
        assert list(cur.keys()) == [((1 << n) - 1, ())]
        print("d=%d mode=%s -> minimum over ALL %d! labellings = %d"
              % (d, mode, n, min(cur.values())))


if __name__ == "__main__":
    run(int(sys.argv[1]), int(sys.argv[2]),
        sys.argv[3] if len(sys.argv) > 3 else "both")
