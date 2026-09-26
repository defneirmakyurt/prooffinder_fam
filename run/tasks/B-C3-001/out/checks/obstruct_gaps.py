# (i) S3 obstruction: lam |- T_k - 1 with min_{beta = lam + cell} d(beta) maximal; (ii) S4: drop events (energy
# decreases) along orbits: number of drops, max gap between consecutive drops, for n = T_k - 1. Exact, stdlib only.
import time
from small_cases import analyse, B
from order_tree import add_cell  # noqa (order_tree runs its own checks on import with default K)
from translations import energy
t0 = time.time()
for k in range(4, 8):
    Tk = k*(k+1)//2; n = Tk - 1
    _, _, _, dT = analyse(Tk); D, ext, cyc, d = analyse(n)
    m = {l: min(dT[b] for b in add_cell(l)) for l in d}
    top = max(m.values()); arg = sorted([l for l in d if m[l] == top], key=lambda x: (x[0], -len(x)))
    print(f"k={k} n={n}: max_lam min_beta d(beta) = {top} (k^2-k={k*k-k}), #argmax={len(arg)}, smallest-first-part argmax: {arg[:3]}, their d_B: {[d[a] for a in arg[:3]]}")
    # drops along orbits until cycle
    maxgap = 0; maxdrops = 0; ext_prof = None
    for l in d:
        x = l; drops = []; 
        for i in range(d[l]):
            y = B(x)
            if energy(y) < energy(x): drops.append(i)
            x = y
        gaps = [b - a for a, b in zip([-1] + drops, drops + [d[l]])]
        maxgap = max(maxgap, max(gaps)); maxdrops = max(maxdrops, len(drops))
        if l == ext[0]: ext_prof = (len(drops), drops)
    print(f"   drop events: max #drops over lam = {maxdrops}, max gap between drops = {maxgap}; extremizer {ext[0]}: #drops={ext_prof[0]} at steps {ext_prof[1]}")
print("runtime %.2fs" % (time.time()-t0))
