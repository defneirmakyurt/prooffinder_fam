"""Referee B-C3-016: independent exhaustive exact check (stdlib only, integers only).
Cyclicity is computed INDEPENDENTLY of Cell 1: on the functional graph of B on all partitions of n,
a node is cyclic iff it lies on a cycle. d_B = distance to the cyclic set (cycle-ENTRY time).
Checks, for every n with rank k in [KMIN, KMAX]:
  S5: cyclic set == C1 list {mu(e)}.
  (a): for non-triangular n with k>=4: D_B(n) <= k^2-2k-1.
  (b): D_B(T_k - 1) vs claimed F(k) (k>=4: k^2-2k-1; k=2:0; k=3:3).
  (c): argmax set == {lam : B^{k^2-2k-2}(lam) = nu_k} (k>=4); sizes; lambda*_k in it;
       S12 alt description {lam : B^{k^2-4k-2}(lam) = mu_k}, mu_k=(k,k-1,k-1,k-3,...,3,1), k>=6.
  Also: tau-1 <= k^2-2k-1 (tau of proof 4.1 with independent cyclic test) and the 9.2 row structure
        c_{tau-k}=k-1, c_{tau-k+1..tau-3}=k, c_{tau-2}=k+1 for every maximiser.
  Also: within each block, which n attain k^2-2k-1 (S9).
"""
import sys
def parts(n, m=None):
    if m is None: m = n
    if n == 0: yield (); return
    for a in range(min(n, m), 0, -1):
        for r in parts(n - a, a): yield (a,) + r
def B(l):
    return tuple(sorted([x - 1 for x in l if x > 1] + [len(l)], reverse=True))
def T(k): return k*(k+1)//2
def rank(n):
    k = 1
    while T(k) < n: k += 1
    return k
def c1_list(n, k):
    r = n - T(k-1); out = set()
    for mask in range(1 << k):
        e = [(mask >> i) & 1 for i in range(k)]
        if sum(e) != r: continue
        out.add(tuple(x for x in [k-1-i+e[i] for i in range(k)] if x > 0))
    return out
def graph(n):
    P = list(parts(n)); idx = {p: i for i, p in enumerate(P)}
    nxt = [idx[B(p)] for p in P]
    N = len(P); state = [0]*N; cyc = [False]*N
    for s in range(N):
        if state[s]: continue
        path = []; x = s
        while state[x] == 0:
            state[x] = 1; path.append(x); x = nxt[x]
        if state[x] == 1:  # found new cycle
            y = x
            while True:
                cyc[y] = True; y = nxt[y]
                if y == x: break
        for z in path: state[z] = 2
    d = [-1]*N
    for i in range(N):
        if cyc[i]: d[i] = 0
    for s in range(N):
        if d[s] >= 0: continue
        path = []; x = s
        while d[x] < 0:
            path.append(x); x = nxt[x]
        base = d[x]
        for z in reversed(path):
            base += 1; d[z] = base
    return P, idx, nxt, cyc, d
def tau_of(l, cycset, k):
    # tau = min i>=1 with lambda^(i-1) cyclic, c_i=k-1, c_{i+1}=k; c_i = #parts of lambda^(i-1)
    i = 1; y = l; seq = [l]
    while True:
        y1 = B(y)
        if y in cycset and len(y) == k-1 and len(y1) == k: return i, seq
        y = y1; seq.append(y); i += 1
KMIN = int(sys.argv[1]); KMAX = int(sys.argv[2])
allok = True
for k in range(KMIN, KMAX+1):
    bound = k*k-2*k-1
    for n in range(T(k-1)+1, T(k)+1):
        P, idx, nxt, cyc, d = graph(n)
        cycset = {P[i] for i in range(len(P)) if cyc[i]}
        c1ok = (cycset == c1_list(n, k))
        D = max(d); allok &= c1ok
        line = f"k={k} n={n} #par={len(P)} #cyc={len(cycset)} C1match={c1ok} D_B={D}"
        if n < T(k) and k >= 4:
            ok_a = D <= bound; allok &= ok_a
            line += f" bound={bound} (a)ok={ok_a} attains={D==bound}"
            # tau bound
            tmax = 0
            for p in P:
                t, _ = tau_of(p, cycset, k); tmax = max(tmax, t-1)
            line += f" max(tau-1)={tmax}"; allok &= tmax <= bound
        if n == T(k)-1:
            F = {2: 0, 3: 3}.get(k, bound)
            ok_b = (D == F); allok &= ok_b
            ext = {P[i] for i in range(len(P)) if d[i] == D}
            line += f" | F(k)={F} (b)ok={ok_b} |ext|={len(ext)}"
            if k >= 3:
                lstar = tuple([k-1, k-2] + list(range(k-2, 0, -1)) + [1])
                line += f" d(lstar)={d[idx[lstar]]}"
                if k >= 4: allok &= d[idx[lstar]] == D
            if k >= 4:
                nu = tuple([k+1] + list(range(k-1, 2, -1)) + [1])
                m = k*k-2*k-2
                pred = set()
                for p in P:
                    x = p
                    for _ in range(m): x = B(x)
                    if x == nu: pred.add(p)
                ok_c = (pred == ext); allok &= ok_c
                line += f" (c)ext==B^-m(nu)={ok_c}"
                # 9.2 row structure
                okrow = True
                for p in ext:
                    t, seq = tau_of(p, cycset, k)
                    c = lambda i: len(seq[i-1]) if i-1 < len(seq) else None
                    # extend seq if needed
                    while len(seq) < t+2: seq.append(B(seq[-1]))
                    c = lambda i: len(seq[i-1])
                    if not (t == k*k-2*k and c(t-k) == k-1 and all(c(j) == k for j in range(t-k+1, t-2)) and c(t-2) == k+1
                            and seq[t-2] == nu and seq[t-1] == tuple(range(k, 1, -1))):
                        okrow = False
                line += f" 9.2rows={okrow}"; allok &= okrow
                if k <= 5: line += f" ext={sorted(ext, reverse=True)}"
            if k >= 6:
                mu = tuple([k, k-1, k-1] + list(range(k-3, 2, -1)) + [1])
                assert sum(mu) == n
                m2 = k*k-4*k-2
                pred2 = set()
                for p in P:
                    x = p
                    for _ in range(m2): x = B(x)
                    if x == mu: pred2.add(p)
                x = mu
                for _ in range(2*k): x = B(x)
                line += f" S12alt==ext={pred2==ext} B^2k(mu_k)==nu_k={x==nu}"
        print(line, flush=True)
print("ALL OK" if allok else "SOME CHECK FAILED")
