"""Float local search for max S (units of pi), then EXACT recheck of the best configs:
each float is an exact dyadic rational, converted with Fraction(float) and S recomputed exactly."""
from fractions import Fraction as F
import random, sys
random.seed(7)

def rho(z):
    z = z - (z.numerator // z.denominator)
    return min(z, 1 - z)

def Sf(a):
    N = len(a); s = 0.0
    for i in range(N):
        for j in range(i + 1, N):
            d = (a[i] - a[j]) % 1.0
            s += min(d, 1 - d)
    return s

Nmax = int(sys.argv[1]) if len(sys.argv) > 1 else 14
viol = 0
for N in range(2, Nmax + 1):
    bound = F(N * N // 4, 2)
    best_exact = F(-1)
    for r in range(30):
        a = [random.random() for _ in range(N)]
        cur = Sf(a); step = 0.25
        for it in range(3000):
            i = random.randrange(N); old = a[i]
            a[i] = (old + random.uniform(-step, step)) % 1.0
            new = Sf(a)
            if new >= cur: cur = new
            else: a[i] = old
            if it % 200 == 199: step *= 0.7
        ae = [F(x) for x in a]
        Se = sum((rho(ae[i] - ae[j]) for i in range(N) for j in range(i + 1, N)), F(0))
        if Se > bound: viol += 1
        best_exact = max(best_exact, Se)
    print(f"N={N}: best exact S/pi over 30 restarts = {float(best_exact):.15f} (exact <= bound: {best_exact <= bound}), bound={bound}, gap={float(bound-best_exact):.3e}")
print("exact violations:", viol)
