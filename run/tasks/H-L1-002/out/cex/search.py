#!/usr/bin/env python3
"""Referee's own checks for H-L1 (independent code; exact integers only).
 1. Q_3: all 8! labellings, uphill paths counted by explicit enumeration of sequences
    (independent of any recurrence). Report min and whether any labelling has 13 = |E|+1.
 2. All graphs on 1..NG vertices (networkx atlas), all labellings: check
    Step 5 identity P = |Val| + sum N*up, Step 6 P >= |E|+1, and Step 7 identity on every
    equality labelling of graphs without isolated vertices; also Step 7's intermediate
    claims (|Val|=1, down(v)=1 on R).
 3. Step 8: k does not divide 2^k-1 for 2 <= k <= KMAX (exact pow).
 4. Step 10 algebra: (d-1)*m = 2^(d-1)(d-2)+1 has no integer m for 3<=d<=DMAX, and the
    identity 2^(d-1)-1 = (d-1)(2^(d-1)-m) given (**) (symbolic check via sympy).
 5. Hill-climbing (random swaps + restarts) on Q_d, d = 3..7: try to find a labelling with
    fewer than |E|+2 uphill paths.
"""
import itertools, random, sys, time
import networkx as nx
import sympy as sp

def cube(d):
    n = 1 << d
    return [[v ^ (1 << i) for i in range(d)] for v in range(n)]

def count_enum(adj, lab):
    # explicit enumeration of all uphill paths as sequences (stack-based)
    n = len(adj)
    total = 0
    for v in range(n):
        if all(lab[w] > lab[v] for w in adj[v]):
            stack = [v]
            while stack:
                x = stack.pop()
                total += 1
                for y in adj[x]:
                    if lab[y] > lab[x]:
                        stack.append(y)
    return total

def stats(adj, lab):
    n = len(adj)
    order = sorted(range(n), key=lambda v: lab[v])
    N = [0]*n
    for v in order:
        low = [w for w in adj[v] if lab[w] < lab[v]]
        N[v] = (0 if low else 1) + sum(N[w] for w in low)
    up = [sum(1 for w in adj[v] if lab[w] > lab[v]) for v in range(n)]
    down = [len(adj[v]) - up[v] for v in range(n)]
    return N, up, down

def part1():
    adj = cube(3)
    mn, c13 = None, 0
    for perm in itertools.permutations(range(1, 9)):
        P = count_enum(adj, perm)
        if P == 13: c13 += 1
        mn = P if mn is None else min(mn, P)
    return mn, c13

def part2(NG):
    checked = 0; eqlabs = 0
    for G in nx.graph_atlas_g():
        n = G.number_of_nodes()
        if n == 0 or n > NG: continue
        adj = [sorted(G.neighbors(v)) for v in range(n)]
        E = G.number_of_edges()
        noiso = all(len(a) > 0 for a in adj)
        for perm in itertools.permutations(range(1, n+1)):
            P = count_enum(adj, perm)
            N, up, down = stats(adj, perm)
            val = [v for v in range(n) if down[v] == 0]
            assert P == sum(N), (adj, perm)
            assert P == len(val) + sum(N[v]*up[v] for v in range(n)), (adj, perm)
            assert P >= E + 1
            assert min(N) >= 1
            checked += 1
            if P == E + 1 and noiso:
                eqlabs += 1
                M = [v for v in range(n) if up[v] == 0]
                assert len(val) == 1
                R = [v for v in range(n) if v not in M and v not in val]
                assert all(down[v] == 1 for v in R)
                assert E == n - 1 - len(M) + sum(len(adj[v]) for v in M), (adj, perm)
    return checked, eqlabs

def part3(KMAX):
    for k in range(2, KMAX+1):
        assert pow(2, k, k) != 1 % k, k
    return True

def part4(DMAX):
    for d in range(3, DMAX+1):
        assert (2**(d-1)*(d-2)+1) % (d-1) != 0, d
    d, m = sp.symbols('d m')
    # from |E| = (n-1-m) + m*d with n=2^d, |E| = d*2^(d-1):
    lhs = d*2**(d-1) - (2**d - 1 - m + m*d)
    rhs = (d-1)*m - (2**(d-1)*(d-2)+1)
    ok1 = sp.simplify(sp.expand(-lhs - rhs)) == 0
    # 2^(d-1)(d-1) - [2^(d-1)(d-2)+1] == 2^(d-1)-1
    ok2 = sp.simplify(2**(d-1)*(d-1) - (2**(d-1)*(d-2)+1) - (2**(d-1)-1)) == 0
    return ok1, ok2

def count_rec(adj, lab, order=None):
    n = len(adj)
    if order is None:
        order = sorted(range(n), key=lambda v: lab[v])
    N = [0]*n
    for v in order:
        s = 0; low = False
        for w in adj[v]:
            if lab[w] < lab[v]:
                low = True; s += N[w]
        N[v] = s + (0 if low else 1)
    return sum(N)

def part5(seed, dmax, iters, restarts):
    rng = random.Random(seed)
    res = []
    for d in range(3, dmax+1):
        adj = cube(d); n = 1 << d; E = d*2**(d-1)
        best_all = None; best_lab = None
        for r in range(restarts):
            # start: weight order with random tie-break (low-P family) or random
            if r % 2 == 0:
                verts = sorted(range(n), key=lambda v: (bin(v).count('1'), rng.random()))
            else:
                verts = list(range(n)); rng.shuffle(verts)
            lab = [0]*n
            for i, v in enumerate(verts): lab[v] = i+1
            cur = count_rec(adj, lab)
            for _ in range(iters):
                a, b = rng.randrange(n), rng.randrange(n)
                if a == b: continue
                lab[a], lab[b] = lab[b], lab[a]
                P = count_rec(adj, lab)
                if P <= cur:
                    cur = P
                else:
                    lab[a], lab[b] = lab[b], lab[a]
            assert cur >= E + 2, (d, cur, lab)
            if best_all is None or cur < best_all:
                best_all = cur; best_lab = lab[:]
        res.append((d, E+2, best_all))
        # write best labelling for checker
        order = sorted(range(n), key=lambda v: best_lab[v])
        with open('/home/user/bainsahackathon/run/tasks/H-L1-002/out/cex/labs/Q%d_hill.txt' % d, 'w') as fh:
            fh.write('\n'.join(format(v, '0%db' % d) for v in order) + '\n')
    return res

if __name__ == '__main__':
    import os
    os.makedirs('/home/user/bainsahackathon/run/tasks/H-L1-002/out/cex/labs', exist_ok=True)
    t = time.time(); print('1. Q_3 exhaustive (min P, #labellings with P=13):', part1(), '%.1fs' % (time.time()-t), flush=True)
    t = time.time(); print('2. all graphs n<=6, all labellings (labellings checked, equality labellings):', part2(6), '%.1fs' % (time.time()-t), flush=True)
    t = time.time(); print('3. k !| 2^k-1, 2<=k<=10^6:', part3(10**6), '%.1fs' % (time.time()-t), flush=True)
    t = time.time(); print('4. (d-1) !| 2^(d-1)(d-2)+1, 3<=d<=3000; symbolic identities:', part4(3000), '%.1fs' % (time.time()-t), flush=True)
    t = time.time(); print('5. hill-climb (d, |E|+2, best P found):', part5(20260926, 7, 4000, 6), '%.1fs' % (time.time()-t), flush=True)
