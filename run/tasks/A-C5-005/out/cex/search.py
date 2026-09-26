"""
Referee counterexample / sanity search for A-C5 (d+2 lines in R^d).
Pure stdlib (random, math) -- no numpy available in the venv.

Searched (numerically, floating point -- exploratory only, not part of any
proof, per protocol step 6 / step 3):

1. Whether the TARGET statement S <= (C(d+2,2)-2)*pi/2 can ever be violated,
   for random and locally-optimized configurations of d+2 unit vectors in
   R^d, for d = 2..8.
2. Whether the proof's intermediate Step-3 bound
   sum_{i<j} a_ij^2 >= (d+2)/d  (eq. 7)
   ever fails numerically on random configurations.
3. The conjectured extremal configuration (d axes, two repeated) is checked
   for exact equality with the bound.
"""
import math, random

random.seed(0)

def dot(u, v):
    return sum(a*b for a, b in zip(u, v))

def norm(u):
    return math.sqrt(dot(u, u))

def random_unit_vector(d, rng):
    v = [rng.gauss(0, 1) for _ in range(d)]
    n = norm(v)
    return [x/n for x in v]

def S_and_a2(vecs):
    n = len(vecs)
    S = 0.0
    a2 = 0.0
    for i in range(n):
        for j in range(i+1, n):
            c = abs(dot(vecs[i], vecs[j]))
            c = min(1.0, max(-1.0, c))
            S += math.acos(c)
            a2 += c*c
    return S, a2

def bound(d):
    N = d + 2
    C = N*(N-1)//2
    return (C - 2) * math.pi/2

def axes_config(d):
    N = d+2
    V = [[0.0]*d for _ in range(N)]
    for i in range(d):
        V[i][i] = 1.0
    V[d][0] = 1.0
    V[d+1][1] = 1.0
    return V

print("=== Equality-case check (conjectured optimum: axes, two repeated) ===")
for d in range(2, 9):
    V = axes_config(d)
    S, a2 = S_and_a2(V)
    b = bound(d)
    print(f"d={d}: S={S:.6f}, bound={b:.6f}, diff={S-b:.2e}")

print()
print("=== Random search for violations of S <= bound (target statement) ===")
for d in range(2, 9):
    N = d+2
    b = bound(d)
    worst = -1e9
    rng = random.Random(1234+d)
    trials = 4000
    for _ in range(trials):
        V = [random_unit_vector(d, rng) for _ in range(N)]
        S, a2 = S_and_a2(V)
        if S - b > worst:
            worst = S - b
    print(f"d={d}: random trials={trials}, max(S-bound) observed = {worst:.6f}  (positive would be a violation)")

print()
print("=== Local hill-climbing search attempting to approach/exceed bound ===")
for d in range(2, 7):
    N = d+2
    b = bound(d)
    rng = random.Random(999+d)
    best_S = -1
    for restart in range(40):
        V = [random_unit_vector(d, rng) for _ in range(N)]
        cur_S, _ = S_and_a2(V)
        step = 0.3
        for it in range(200):
            i = rng.randrange(N)
            pert = [rng.gauss(0,1)*step for _ in range(d)]
            newvi = [a+b_ for a, b_ in zip(V[i], pert)]
            n = norm(newvi)
            newvi = [x/n for x in newvi]
            old = V[i]
            V[i] = newvi
            newS, _ = S_and_a2(V)
            if newS > cur_S:
                cur_S = newS
            else:
                V[i] = old
            step *= 0.99
        if cur_S > best_S:
            best_S = cur_S
    print(f"d={d}: best S found by local search = {best_S:.6f}, bound = {b:.6f}, gap(bound-best)={b-best_S:.6f}")

print()
print("=== Sanity check of proof's Step 3 intermediate bound: sum_{i<j} a_ij^2 >= (d+2)/d ===")
for d in range(2, 9):
    N = d+2
    rng = random.Random(42+d)
    worst_ratio = 1e9
    target = (d+2)/d
    for _ in range(4000):
        V = [random_unit_vector(d, rng) for _ in range(N)]
        _, a2 = S_and_a2(V)
        ratio = a2/target
        if ratio < worst_ratio:
            worst_ratio = ratio
    print(f"d={d}: min observed sum a_ij^2 / ((d+2)/d) over 4000 random trials = {worst_ratio:.4f} (should be >= 1)")
