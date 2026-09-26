"""Referee's independent exhaustive computation (stdlib only, exact integers).
For k in [KMIN, KMAX], n = T_{k-1}+1: enumerate all partitions of n, build the
functional graph of B, find cyclic nodes by in-degree peeling (Kahn), compute
d_B by reverse BFS from the cyclic set, report D_B(n), ALL maximisers, and
whether lambda^(k) (built from the TARGET text) is a maximiser / the unique one.
Usage: python3 exhaustive_referee.py KMIN KMAX"""
import sys
from collections import deque

def parts_of(n):
    # iterative generation of partitions in reverse lex order
    a = [n]
    out = []
    while True:
        out.append(tuple(a))
        # find rightmost part > 1
        rem = 0
        while a and a[-1] == 1:
            a.pop(); rem += 1
        if not a:
            return out
        x = a.pop() - 1
        rem += 1
        a.append(x)
        while rem > x:
            a.append(x); rem -= x
        if rem:
            a.append(rem)

def shift(lam):
    s = len(lam)
    new = [p - 1 for p in lam if p > 1]
    new.append(s)
    new.sort(reverse=True)
    return tuple(new)

def lam_target(k):
    # (k-2, k-2, k-3, k-4, ..., 3, 2, 2, 1)
    return tuple([k - 2] + list(range(k - 2, 1, -1)) + [2, 1])

def run(k):
    n = k * (k - 1) // 2 + 1
    P = parts_of(n)
    idx = {p: i for i, p in enumerate(P)}
    N = len(P)
    nxt = [idx[shift(p)] for p in P]
    indeg = [0] * N
    for j in nxt:
        indeg[j] += 1
    q = deque(i for i in range(N) if indeg[i] == 0)
    removed = [False] * N
    while q:
        i = q.popleft(); removed[i] = True
        j = nxt[i]; indeg[j] -= 1
        if indeg[j] == 0:
            q.append(j)
    cyc = [i for i in range(N) if not removed[i]]
    rev = [[] for _ in range(N)]
    for i in range(N):
        rev[nxt[i]].append(i)
    d = [-1] * N
    q = deque()
    for i in cyc:
        d[i] = 0; q.append(i)
    while q:
        i = q.popleft()
        for j in rev[i]:
            if d[j] < 0:
                d[j] = d[i] + 1; q.append(j)
    assert min(d) >= 0
    D = max(d)
    maxers = [P[i] for i in range(N) if d[i] == D]
    lt = lam_target(k)
    assert sum(lt) == n
    # cycle structure: count cycles among cyclic nodes
    seen = set(); ncyc = 0; lens = []
    for i in cyc:
        if i in seen: continue
        ncyc += 1; L = 0; j = i
        while j not in seen:
            seen.add(j); L += 1; j = nxt[j]
        lens.append(L)
    delta = list(range(k - 1, 0, -1))
    gam = set()
    for j in range(k):
        mu = delta + [0]; mu[j] += 1
        gam.add(tuple(x for x in mu if x > 0))
    cycset = set(P[i] for i in cyc)
    return dict(k=k, n=n, N=N, D=D, F=(k-1)*(k-3), maxers=maxers,
                dlam=d[idx[lt]], lam=lt, ncyc=ncyc, lens=lens,
                cyc_is_gamma=(cycset == gam))

if __name__ == "__main__":
    a, b = int(sys.argv[1]), int(sys.argv[2])
    allok = True
    for k in range(a, b + 1):
        r = run(k)
        ok = r['D'] == r['F'] == r['dlam'] and r['cyc_is_gamma'] and r['ncyc'] == 1 and r['lens'] == [k]
        allok &= ok
        print(f"k={k} n={r['n']} #part={r['N']} D_B={r['D']} F={r['F']} d_B(lambda^(k))={r['dlam']} "
              f"lambda^(k)={r['lam']} #maximisers={len(r['maxers'])} maximisers={r['maxers'] if k <= 6 else '[omitted]'} "
              f"cycles={r['ncyc']} lengths={r['lens']} cyclic=gamma_j:{r['cyc_is_gamma']} OK={ok}", flush=True)
    print("ALL OK" if allok else "FAILURE")
