# Exploratory float sanity check (the proof does NOT rest on this).
# Checks the key inductive inequality D_k >= cos^2(psi_{k-1}) D_{k-1} for random
# phi_i >= 0 with sum < pi/2, where D_k are leading minors of the tridiagonal
# matrix with 1 on the diagonal and sin(phi_i) off-diagonal.
import math, random
random.seed(1)
worst = float('inf'); trials = 0
for _ in range(200000):
    m = random.randint(2, 12)
    w = [random.random() for _ in range(m - 1)]
    tot = random.random() * math.pi / 2
    s = sum(w); phi = [tot * x / s for x in w]
    D = [1.0, 1.0]; psi = [0.0]
    for p in phi: psi.append(psi[-1] + p)
    for k in range(2, m + 1):
        D.append(D[k-1] - math.sin(phi[k-2])**2 * D[k-2])
    for k in range(1, m + 1):
        worst = min(worst, D[k] - math.cos(psi[k-1])**2 * D[k-1])
    trials += 1
print("trials", trials, "min of D_k - cos^2(psi_{k-1}) D_{k-1}:", worst)
