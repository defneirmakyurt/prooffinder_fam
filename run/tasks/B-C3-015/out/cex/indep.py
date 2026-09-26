"""Independent exact (integer-only, stdlib) referee check for B-C3-007.
Cyclicity is decided FROM THE DEFINITION (lambda on its own B-orbit cycle), not from the Cell-1 formula.
For every k in [KMIN, KMAX] and every n with T_{k-1} < n < T_k, over ALL partitions of n:
  (A) D_B(n) <= k^2-2k-1 (target (a)); report D_B(n) and whether bound attained;
  (S5) definition-cyclic set == Cell-1 set {mu(e)};
  (tau) d_B <= tau-1 <= k^2-2k-1 (proof 4.1, 5.1);
  at n = T_k-1: D_B = k^2-2k-1, maximiser set == {lam: B^{k^2-2k-2}(lam) = nu_k} (proof 9.3),
  lambda*_k in it, #parts(B^{D-2}) = k+1 for every maximiser (9.2: c_{tau-2}=k+1),
  and S12: maximisers == {lam : B^{k^2-4k-2}(lam) = mu_k}, mu_k=(k,k-1,k-1,k-3,...,3,1).
Also for k=3 (n=4,5) and k=2 (n=2) small values.
"""
import sys
sys.setrecursionlimit(100000)
def T(k): return k*(k+1)//2
def parts(n, m=None):
    if m is None: m = n
    if n == 0: yield (); return
    for a in range(min(n, m), 0, -1):
        for r in parts(n-a, a): yield (a,)+r
def B(l):
    return tuple(sorted([x-1 for x in l if x > 1] + [len(l)], reverse=True))
def analyse(n):
    P = list(parts(n))
    succ = {l: B(l) for l in P}
    # cyclic by definition: functional graph; find nodes on cycles
    state = {}  # 0 unvisited,1 in stack,2 done
    cyc = set()
    for l in P:
        if l in state: continue
        path = []; x = l
        while x not in state:
            state[x] = 1; path.append(x); x = succ[x]
        if state[x] == 1:  # found new cycle
            i = path.index(x)
            cyc.update(path[i:])
        for y in path: state[y] = 2
    d = {}
    for l in P:
        if l in d: continue
        path = []; x = l
        while x not in d and x not in cyc:
            path.append(x); x = succ[x]
        base = 0 if x in cyc else d[x]
        if x in cyc: d[x] = 0
        for j, y in enumerate(reversed(path)):
            d[y] = base + j + 1
    return P, succ, cyc, d
def cell1(n, k):
    r = n - T(k-1); out = set()
    for mask in range(1 << k):
        e = [(mask >> i) & 1 for i in range(k)]
        if sum(e) != r: continue
        out.add(tuple(x for x in [k-1-i+e[i] for i in range(k)] if x > 0))
    return out
def tau_of(l, cyc, k):
    # tau = min i>=1 : lambda^(i-1) cyclic, c_i = k-1, c_{i+1} = k ; c_i = #parts of lambda^(i-1)
    i = 1; y = l
    while True:
        y1 = B(y)
        if y in cyc and len(y) == k-1 and len(y1) == k: return i
        y = y1; i += 1
def it(l, m):
    for _ in range(m): l = B(l)
    return l
KMIN = int(sys.argv[1]); KMAX = int(sys.argv[2])
ok = True
for k in range(KMIN, KMAX+1):
    bound = k*k-2*k-1
    for n in range(T(k-1)+1, T(k)):
        P, succ, cyc, d = analyse(n)
        c1 = cell1(n, k)
        D = max(d.values())
        taumax = 0; tauok = True
        for l in P:
            t = tau_of(l, cyc, k)
            if d[l] > t-1: tauok = False
            taumax = max(taumax, t-1)
        line = f"k={k} n={n} r={n-T(k-1)} #P={len(P)} D_B={D} bound={bound} attained={D==bound} cyc_def==cell1:{cyc==c1} (#cyc={len(cyc)}) d<=tau-1:{tauok} max(tau-1)={taumax}"
        if k >= 4:
            if D > bound or taumax > bound or not tauok: ok = False
        if cyc != c1: ok = False
        if n == T(k)-1:
            ext = {l for l in P if d[l] == D}
            line += f" | #max={len(ext)}"
            if k >= 3:
                nu = tuple([k+1] + list(range(k-1, 2, -1)) + [1])
                m = k*k-2*k-2
                pred = {l for l in P if it(l, m) == nu}
                lstar = tuple([k-1, k-2] + list(range(k-2, 0, -1)) + [1])
                par = all(len(it(l, D-2)) == k+1 and it(l, D-1) == nu for l in ext) if D >= 2 else None
                line += f" D==k^2-2k-1:{D==bound} ext==pred(nu_k):{ext==pred} d(lstar)={d[lstar]} parts(B^(D-2))=k+1 & B^(D-1)=nu:{par}"
                if k >= 4:
                    if not (D == bound and ext == pred and d[lstar] == bound and par): ok = False
                if k >= 6:
                    mu = tuple([k, k-1, k-1] + list(range(k-3, 2, -1)) + [1])
                    assert sum(mu) == n
                    predmu = {l for l in P if it(l, k*k-4*k-2) == mu}
                    line += f" S12 ext==pred(mu_k):{ext==predmu} B^(2k)(mu_k)==nu_k:{it(mu,2*k)==nu}"
            if k <= 5: line += f" ext={sorted(ext, reverse=True)}"
        print(line, flush=True)
print("ALL OK" if ok else "FAIL")
