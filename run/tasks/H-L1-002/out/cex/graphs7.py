#!/usr/bin/env python3
"""Part 2 of search.py extended to all graphs on exactly 7 vertices (networkx atlas), all 7! labellings."""
import sys, time, itertools
sys.path.insert(0, '/home/user/bainsahackathon/run/tasks/H-L1-002/out/cex')
import networkx as nx
from search import count_enum, stats
t = time.time(); checked = 0; eq = 0; graphs = 0
for G in nx.graph_atlas_g():
    n = G.number_of_nodes()
    if n != 7: continue
    graphs += 1
    adj = [sorted(G.neighbors(v)) for v in range(n)]
    E = G.number_of_edges(); noiso = all(adj)
    for perm in itertools.permutations(range(1, n+1)):
        P = count_enum(adj, perm)
        N, up, down = stats(adj, perm)
        val = [v for v in range(n) if down[v] == 0]
        assert P == sum(N) == len(val) + sum(N[v]*up[v] for v in range(n))
        assert P >= E + 1 and min(N) >= 1
        checked += 1
        if P == E + 1 and noiso:
            eq += 1
            M = [v for v in range(n) if up[v] == 0]
            assert len(val) == 1
            assert all(down[v] == 1 for v in range(n) if v not in M and v not in val)
            assert E == n - 1 - len(M) + sum(len(adj[v]) for v in M)
print('graphs on 7 vertices:', graphs, 'labellings checked:', checked, 'equality labellings (no isolated vtx):', eq, '%.1fs' % (time.time()-t))
