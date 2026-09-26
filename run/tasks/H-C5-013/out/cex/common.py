"""Shared helpers (stdlib only). Vertices of Q_9 are ints 0..511, bit j = coordinate j+1."""
D = 9
NV = 1 << D
def wt(x): return bin(x).count("1")
EVEN = [v for v in range(NV) if wt(v) % 2 == 0]
ODD = [v for v in range(NV) if wt(v) % 2 == 1]
def nbrs(v): return [v ^ (1 << j) for j in range(D)]

def is_forest(Fset):
    """Exact: Q_9[F] acyclic (union-find over induced edges)."""
    parent = {v: v for v in Fset}
    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a
    for v in Fset:
        for j in range(D):
            w = v ^ (1 << j)
            if w > v and w in Fset:
                ra, rb = find(v), find(w)
                if ra == rb:
                    return False
                parent[ra] = rb
    return True

def find_cycle(Fset):
    """Return the vertex list of some cycle in Q_9[F], or None."""
    Fs = set(Fset)
    seen = {}
    for s in Fs:
        if s in seen: continue
        # iterative DFS with parent tracking
        seen[s] = None
        stack = [(s, iter(nbrs(s)))]
        depth = {s: 0}
        while stack:
            v, it = stack[-1]
            adv = False
            for w in it:
                if w not in Fs: continue
                if w == seen[v]: continue
                if w in seen:
                    # back edge v-w: cycle is path w..v in tree
                    cyc = [v]
                    u = v
                    while u != w:
                        u = seen[u]
                        cyc.append(u)
                    return cyc
                seen[w] = v
                depth[w] = depth[v] + 1
                stack.append((w, iter(nbrs(w))))
                adv = True
                break
            if not adv:
                stack.pop()
    return None
