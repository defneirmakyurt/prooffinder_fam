# stdlib only, exact integer arithmetic. Independent exhaustive computation of D_B(T_k).
# d_B is computed as CYCLE-ENTRY time from the functional graph (cyclic set found without
# assuming delta_k is the only cyclic partition), then compared with F(k) = k^2 - k.
import sys
def partitions(n):
    # iterative generation of all partitions of n as weakly decreasing tuples
    out = []
    a = [0] * (n + 1); k = 1; a[0] = 0; y = n - 1
    # accelerated ascending-composition algorithm (Kelleher), then reverse
    a = [0] * (n + 1); k = 1; y = n - 1
    while k != 0:
        x = a[k - 1] + 1; k -= 1
        while 2 * x <= y:
            a[k] = x; y -= x; k += 1
        l = k + 1
        while x <= y:
            a[k] = x; a[l] = y
            out.append(tuple(reversed(a[:k + 2])))
            x += 1; y -= 1
        a[k] = x + y; y = x + y - 1
        out.append(tuple(reversed(a[:k + 1])))
    return out
def B(l):
    return tuple(sorted([x - 1 for x in l if x > 1] + [len(l)], reverse=True))
K = int(sys.argv[1])
for k in range(1, K + 1):
    n = k * (k + 1) // 2
    P = partitions(n)
    idx = {p: i for i, p in enumerate(P)}
    assert len(idx) == len(P)
    N = len(P)
    nxt = [idx[B(p)] for p in P]
    # find cyclic nodes: standard coloring on functional graph
    state = [0] * N  # 0 new, 1 on stack, 2 done
    cyc = [False] * N
    for s in range(N):
        if state[s]: continue
        path = []; v = s
        while state[v] == 0:
            state[v] = 1; path.append(v); v = nxt[v]
        if state[v] == 1:  # new cycle found
            u = v
            while True:
                cyc[u] = True; u = nxt[u]
                if u == v: break
        for u in path: state[u] = 2
    cyclic = [P[i] for i in range(N) if cyc[i]]
    # distances to cyclic set
    d = [-1] * N
    for i in range(N):
        if cyc[i]: d[i] = 0
    for s in range(N):
        if d[s] >= 0: continue
        path = []; v = s
        while d[v] < 0:
            path.append(v); v = nxt[v]
        base = d[v]
        for u in reversed(path):
            base += 1; d[u] = base
    D = max(d)
    arg = [P[i] for i in range(N) if d[i] == D]
    delta = tuple(range(k, 0, -1))
    wit = (1,) if k == 1 else tuple([k - 1] + [k + 1 - j for j in range(2, k + 1)] + [1])
    ok = (D == k * k - k) and (cyclic == [delta]) and (d[idx[wit]] == k * k - k)
    print("k=%d T_k=%d #partitions=%d cyclic=%s D_B=%d F(k)=%d d_B(witness)=%d #maximisers=%d witness_is_max=%s OK=%s"
          % (k, n, N, cyclic if len(cyclic) < 3 else len(cyclic), D, k*k-k, d[idx[wit]], len(arg), wit in arg, ok))
    sys.stdout.flush()
