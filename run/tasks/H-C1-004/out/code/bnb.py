"""R8: exhaustive branch-and-bound over ALL bijections V(Q_d) -> {1..2^d}, stdlib only, exact ints.

Usage: python3 bnb.py d T [--nomemo] [--nolb] [--maxnodes M]
Decides whether some labelling of Q_d has at most T-1 uphill paths.  Prints
  "NONE BELOW T"  (every labelling has >= T uphill paths)   or
  "FOUND c" + the labelling (a labelling with c < T paths).
No symmetry reduction is used.  Labellings are built as label sequences: at depth k the next
vertex gets label k+1.  Soundness of the two prunings is argued in out/claims.md / README.md:
  (P1) LB: cost_so_far + LB(state) >= T  => no completion has total < T.
  (P2) memo: future cost depends only on (S, N restricted to placed vertices with an unplaced
       neighbour); a state already fully explored with cost <= current cost is skipped.
"""
import sys


def main(d, T, use_memo=True, use_lb=True, maxnodes=None):
    n = 1 << d
    NB = [[v ^ (1 << j) for j in range(d)] for v in range(n)]
    EDGES = [(u, v) for u in range(n) for v in NB[u] if u < v]
    FULL = (1 << n) - 1
    N = [0] * n
    memo = {}
    stats = {"nodes": 0, "memo_hits": 0}
    aborted = []
    found = []
    order = []

    def lower_bound(S):
        # Remaining vertices R = complement of S.  For v in R let P(v) = sum of N(s) over
        # placed neighbours s of v.  Final total over R =
        #   #valleys in R + sum_{v in R} P(v) + sum_{edges {u,v} in R} N(lower endpoint)
        # and N(x) >= max(1, P(x)) for every x in R.  Valleys in R: dropped (>= 0), except
        # when S is empty, where the label-1 vertex is a valley (+1).
        P = [0] * n
        tot = 0
        for v in range(n):
            if not (S >> v) & 1:
                p = 0
                for w in NB[v]:
                    if (S >> w) & 1:
                        p += N[w]
                P[v] = p
                tot += p
        for (u, v) in EDGES:
            if not (S >> u) & 1 and not (S >> v) & 1:
                tot += min(max(1, P[u]), max(1, P[v]))
        if S == 0:
            tot += 1
        return tot

    def key(S):
        # boundary of S = placed vertices with at least one unplaced neighbour
        return (S, tuple(N[v] for v in range(n)
                         if (S >> v) & 1 and any(not (S >> w) & 1 for w in NB[v])))

    def dfs(S, cost):
        if aborted:
            return True
        stats["nodes"] += 1
        if maxnodes is not None and stats["nodes"] > maxnodes:
            aborted.append(True)
            return True
        if S == FULL:
            if cost < T:
                found.append((cost, order[:]))
                return True
            return False
        k = key(S) if use_memo else None
        prev = memo.get(k) if use_memo else None
        if prev is not None and prev <= cost:
            stats["memo_hits"] += 1
            return False
        if use_lb and cost + lower_bound(S) >= T:
            if use_memo:
                memo[k] = cost if prev is None else min(prev, cost)
            return False
        for v in range(n):
            if (S >> v) & 1:
                continue
            low = [w for w in NB[v] if (S >> w) & 1]
            Nv = (0 if low else 1) + sum(N[w] for w in low)
            if cost + Nv >= T:
                continue
            N[v] = Nv
            order.append(v)
            r = dfs(S | (1 << v), cost + Nv)
            order.pop()
            N[v] = 0
            if r:
                return True
        if use_memo:
            memo[k] = cost if prev is None else min(prev, cost)
        return False

    sys.setrecursionlimit(10000)
    dfs(0, 0)
    print("d=%d T=%d memo=%s lb=%s nodes=%d memo_hits=%d memo_size=%d"
          % (d, T, use_memo, use_lb, stats["nodes"], stats["memo_hits"], len(memo)))
    if aborted and not found:
        print("ABORTED node cap %d reached -- search NOT complete" % maxnodes)
        return
    if found:
        c, o = found[0]
        print("FOUND %d" % c)
        for v in o:
            print(format(v, "0%db" % d))
    else:
        print("NONE BELOW %d" % T)


if __name__ == "__main__":
    a = sys.argv[1:]
    mn = None
    if "--maxnodes" in a:
        i = a.index("--maxnodes")
        mn = int(a[i + 1])
        del a[i:i + 2]
    main(int(a[0]), int(a[1]), use_memo="--nomemo" not in a, use_lb="--nolb" not in a,
         maxnodes=mn)
