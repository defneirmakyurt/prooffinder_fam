"""Stdlib-only exact checks for B-C3-007.
(1) k=4, n=T_4-1=9: exhaustive; extremal set of d_B equals {lam : B^6(lam)=(5,3,1)} (used in proof.md, Step 9.4).
(2) Sanity (not used as proof): for 4<=k<=K, all non-triangular n of rank k: D_B(n)<=k^2-2k-1;
    D_B(T_k-1)=k^2-2k-1; extremal set of T_k-1 equals {lam: B^(k^2-2k-2)(lam)=nu_k}; d_B(lambda*_k)=k^2-2k-1.
    Also checks the tau-bound of Lemma E: tau-1 <= k^2-2k-1 for every partition."""
import sys
def parts(n, m=None):
    if m is None: m = n
    if n == 0: yield (); return
    for a in range(min(n, m), 0, -1):
        for r in parts(n - a, a): yield (a,) + r
def B(l):
    return tuple(sorted([x - 1 for x in l if x > 1] + [len(l)], reverse=True))
def T(k): return k * (k + 1) // 2
def cyclic_set(n, k):
    r = n - T(k - 1); out = set()
    for mask in range(1 << k):
        e = [(mask >> i) & 1 for i in range(k)]
        if sum(e) != r: continue
        out.add(tuple(x for x in [k - 1 - i + e[i] for i in range(k)] if x > 0))
    return out
def analyse(n, k):
    cyc = cyclic_set(n, k); d = {}; taumax = 0
    for l in parts(n):
        seq = [l]; x = l
        while x not in cyc:
            x = B(x); seq.append(x)
        d[l] = len(seq) - 1
        # tau = min i>=1 with lambda^(i-1) cyclic, c_i=k-1, c_{i+1}=k  (c_i = #parts of lambda^(i-1))
        i = 1; y = l; hist = [l]
        while True:
            y1 = B(y)
            if y in cyc and len(y) == k - 1 and len(y1) == k: break
            y = y1; i += 1
        taumax = max(taumax, i - 1)
    return d, taumax
K = int(sys.argv[1]) if len(sys.argv) > 1 else 8
ok = True
for k in range(4, K + 1):
    for n in range(T(k - 1) + 1, T(k)):
        d, taumax = analyse(n, k)
        D = max(d.values())
        if D > k * k - 2 * k - 1 or taumax > k * k - 2 * k - 1: ok = False
        line = f"k={k} n={n} D_B={D} max(tau-1)={taumax} bound={k*k-2*k-1}"
        if n == T(k) - 1:
            nu = tuple([k + 1] + list(range(k - 1, 2, -1)) + [1])
            ext = {l for l in d if d[l] == D}
            m = k * k - 2 * k - 2
            pred = set()
            for l in d:
                x = l
                for _ in range(m): x = B(x)
                if x == nu: pred.add(l)
            lstar = tuple([k - 1, k - 2] + list(range(k - 2, 0, -1)) + [1])
            good = (D == k * k - 2 * k - 1) and ext == pred and d[lstar] == D
            ok &= good
            line += f" | T_k-1: extremal={len(ext)} pred(nu_k)={len(pred)} equal={ext==pred} d(lstar)={d[lstar]}"
            if k == 4: line += f" ext={sorted(ext)}"
        print(line)
print("ALL OK" if ok else "FAIL")
