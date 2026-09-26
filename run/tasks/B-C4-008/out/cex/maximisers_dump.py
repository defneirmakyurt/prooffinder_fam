"""Referee B-C4-008: dump ALL maximisers of d_B on partitions of T_{k-1}+1 (stdlib only, exact).
Reuses partitions/B from exhaustive_check.py (same folder). Usage: python3 maximisers_dump.py KMIN KMAX"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.dont_write_bytecode = True
from exhaustive_check import partitions, B, lam_k

def dB_all(n):
    P = list(partitions(n)); nxt = {p: B(p) for p in P}
    color = set(); cyclic = set()
    for p in P:
        if p in color: continue
        path = []; idx = {}; q = p
        while q not in color and q not in idx:
            idx[q] = len(path); path.append(q); q = nxt[q]
        if q in idx: cyclic.update(path[idx[q]:])
        color.update(path)
    d = {p: 0 for p in cyclic}
    for p in P:
        st = []; q = p
        while q not in d: st.append(q); q = nxt[q]
        v = d[q]
        while st: v += 1; d[st.pop()] = v
    return d

if __name__ == "__main__":
    kmin, kmax = int(sys.argv[1]), int(sys.argv[2])
    for k in range(kmin, kmax + 1):
        n = k * (k - 1) // 2 + 1
        d = dB_all(n); D = max(d.values())
        mx = sorted([p for p in d if d[p] == D], reverse=True)
        print(f"# k={k} n={n} D_B={D} (k-1)(k-3)={(k-1)*(k-3)} #maximisers={len(mx)} lambda^(k) in maximisers: {lam_k(k) in mx}")
        for p in mx: print(" ", p)
