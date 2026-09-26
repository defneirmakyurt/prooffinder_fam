"""Independent exhaustive check (stdlib only, exact integers). Does NOT assume delta_k is the unique
cyclic partition: builds the full functional graph of B on partitions of n, finds all cyclic nodes
(nodes on cycles), then d_B(l) = distance to the cyclic set (cycle-ENTRY time).
Reports: number of cyclic partitions, D_B(n), number of maximisers, d_B(witness).
Usage: python3 exhaustive.py KMIN KMAX"""
import sys

def parts_rec(n, maxp):
    # partitions of n with parts <= maxp, recursive, weakly decreasing tuples
    if n == 0:
        yield ()
        return
    for p in range(min(n, maxp), 0, -1):
        for rest in parts_rec(n - p, p):
            yield (p,) + rest

def pcount(n):
    # pentagonal-number recurrence (independent of the DP in the subject's code)
    p = [1] + [0] * n
    for m in range(1, n + 1):
        s = 0; j = 1
        while True:
            g1 = j * (3 * j - 1) // 2
            if g1 > m: break
            sgn = 1 if j % 2 == 1 else -1
            s += sgn * p[m - g1]
            g2 = j * (3 * j + 1) // 2
            if g2 <= m: s += sgn * p[m - g2]
            j += 1
        p[m] = s
    return p[n]

def shift(l):
    # B via multiplicities: counts[v] = number of parts equal to v
    s = len(l)
    out = [x - 1 for x in l if x >= 2]   # still weakly decreasing
    # insert s in sorted position (descending)
    pos = 0
    while pos < len(out) and out[pos] >= s:
        pos += 1
    out.insert(pos, s)
    return tuple(out)

def run(k):
    n = k * (k + 1) // 2
    P = list(parts_rec(n, n))
    assert len(P) == pcount(n), "enumeration incomplete"
    assert len(set(P)) == len(P)
    idx = {p: i for i, p in enumerate(P)}
    N = len(P)
    nxt = [idx[shift(p)] for p in P]
    # cyclic nodes: iterative colouring
    state = [0] * N   # 0 unvisited, 1 on stack, 2 done
    cyc = [False] * N
    for s0 in range(N):
        if state[s0]: continue
        path = []
        x = s0
        while state[x] == 0:
            state[x] = 1; path.append(x); x = nxt[x]
        if state[x] == 1:  # found a new cycle starting at x
            y = x
            while True:
                cyc[y] = True; y = nxt[y]
                if y == x: break
        for y in path: state[y] = 2
    cyclic = [P[i] for i in range(N) if cyc[i]]
    # distances to cyclic set via reverse BFS
    rev = [[] for _ in range(N)]
    for i in range(N): rev[nxt[i]].append(i)
    dist = [-1] * N
    frontier = [i for i in range(N) if cyc[i]]
    for i in frontier: dist[i] = 0
    d = 0
    while frontier:
        new = []
        for i in frontier:
            for j in rev[i]:
                if dist[j] < 0:
                    dist[j] = d + 1; new.append(j)
        frontier = new; d += 1
    assert min(dist) >= 0
    DB = max(dist)
    maxers = [P[i] for i in range(N) if dist[i] == DB]
    wit = (1,) if k == 1 else tuple([k - 1] + list(range(k - 1, 0, -1)) + [1])
    dw = dist[idx[wit]]
    delta = tuple(range(k, 0, -1))
    ok = (cyclic == [delta]) and DB == k * k - k and dw == k * k - k
    print(f"k={k} n={n} p(n)={N} cyclic={cyclic if len(cyclic)<4 else len(cyclic)} D_B={DB} k^2-k={k*k-k} "
          f"#maximisers={len(maxers)} d_B(witness)={dw} witness_is_maximiser={wit in maxers} "
          f"maximisers(first 3)={maxers[:3]} {'OK' if ok else 'FAIL'}", flush=True)
    return ok

if __name__ == "__main__":
    a, b = int(sys.argv[1]), int(sys.argv[2])
    allok = True
    for k in range(a, b + 1):
        allok &= run(k)
    # statement example
    x = (2, 1, 1, 1, 1); chain = [x]
    for _ in range(4): x = shift(x); chain.append(x)
    print("example chain:", chain)
    print("ALL OK" if allok else "SOME FAILURE")
