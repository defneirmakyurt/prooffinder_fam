"""
Counterexample / sanity search for A-C5 (d+2 lines in R^d), floating point
(mpmath not needed here - this is exploratory search, not a proof step; no
claim in verdict.md rests on exactness of these numbers, only on whether a
violation of the *target* inequality turns up, which would refute the
statement itself regardless of precision, since violations would need to be
large to survive floating point noise).

Checks, for d = 2..8:
  (a) equality configuration (S2): d coordinate axes, two of them repeated
      once more -> S should equal (C(d+2,2)-2)*pi/2 exactly (symbolic/exact
      via fractions of pi, computed with math.pi as double but the pattern
      is fully combinatorial: C(d,2) orthogonal pairs among distinct axes
      contribute pi/2 each... verified by direct angle enumeration).
  (b) random unit-vector configurations (N=d+2 vectors in R^d), many trials,
      checking S <= (C(d+2,2)-2)*pi/2 (the TARGET, to hunt for a violation
      that would refute the statement) and also checking the proof's own
      weaker established bound T >= (d+2)/d (sanity of Step 3-4), and
      reporting how far T typically is from the needed pi.
  (c) adversarial configurations (near-orthogonal-axes with jitter, highly
      clustered vectors, random Gaussian frames) to stress-test (a).
"""
import random
import math
from itertools import combinations

def unit(v):
    n = math.sqrt(sum(c*c for c in v))
    return [c/n for c in v]

def theta(x, y):
    dot = sum(a*b for a, b in zip(x, y))
    dot = max(-1.0, min(1.0, abs(dot)))
    return math.acos(dot)

def S_of(vectors):
    N = len(vectors)
    total = 0.0
    for i, j in combinations(range(N), 2):
        total += theta(vectors[i], vectors[j])
    return total

def T_of(vectors):
    # T = sum arcsin|a_ij|
    N = len(vectors)
    total = 0.0
    for i, j in combinations(range(N), 2):
        dot = sum(a*b for a, b in zip(vectors[i], vectors[j]))
        dot = max(-1.0, min(1.0, abs(dot)))
        total += math.asin(dot)
    return total

def comb2(n):
    return n*(n-1)//2

def equality_config(d):
    # d coordinate axes, each once, plus 2 more copies of axis 0 and axis 1
    vecs = []
    for k in range(d):
        e = [0.0]*d
        e[k] = 1.0
        vecs.append(e)
    # repeat axes 0 and 1 once more (two of them repeated) -> total d+2 lines
    e0 = [0.0]*d; e0[0] = 1.0
    e1 = [0.0]*d; e1[1] = 1.0
    vecs.append(e0)
    vecs.append(e1)
    return vecs

def random_unit_vectors(d, N, rng):
    return [unit([rng.gauss(0,1) for _ in range(d)]) for _ in range(N)]

def main():
    rng = random.Random(42)
    print("=== (a) equality configuration check, d=2..8 ===")
    for d in range(2, 9):
        vecs = equality_config(d)
        N = d+2
        S = S_of(vecs)
        bound = (comb2(N) - 2) * math.pi/2
        print(f"d={d}: N={N}, S={S:.6f}, bound={bound:.6f}, diff={S-bound:.2e}")

    print()
    print("=== (b) random search for violations of the TARGET, d=2..8, 20000 trials each ===")
    max_violation = -1e9
    for d in range(2, 9):
        N = d+2
        worst = None
        for trial in range(20000):
            vecs = random_unit_vectors(d, N, rng)
            S = S_of(vecs)
            bound = (comb2(N) - 2) * math.pi/2
            viol = S - bound
            if worst is None or viol > worst[0]:
                worst = (viol, S, bound)
        print(f"d={d}: worst (S-bound) over 20000 random trials = {worst[0]:.6f} "
              f"(S={worst[1]:.6f}, bound={worst[2]:.6f})  -> {'VIOLATION' if worst[0] > 1e-9 else 'no violation'}")

    print()
    print("=== (b') adversarial configs: axes + small perturbation, d=3..6 ===")
    for d in range(3, 7):
        vecs = equality_config(d)
        N = d+2
        for eps in [1e-3, 1e-2, 1e-1]:
            pert = [unit([c + eps*rng.gauss(0,1) for c in v]) for v in vecs]
            S = S_of(pert)
            bound = (comb2(N)-2)*math.pi/2
            print(f"  d={d}, eps={eps}: S={S:.6f}, bound={bound:.6f}, diff={S-bound:.2e}")

    print()
    print("=== (c) sanity of proof's own weak bound (Step 3-4): T >= (d+2)/d, T vs pi, d=2..8 ===")
    for d in range(2, 9):
        N = d+2
        Ts = []
        for trial in range(2000):
            vecs = random_unit_vectors(d, N, rng)
            Ts.append(T_of(vecs))
        min_T = min(Ts)
        needed_weak = (d+2)/d
        print(f"d={d}: min T over 2000 random trials = {min_T:.6f}, weak bound (d+2)/d = {needed_weak:.6f} "
              f"({'OK, min_T>=weak bound' if min_T >= needed_weak - 1e-9 else 'VIOLATION of Step4 bound!'}), "
              f"needed target T>=pi={math.pi:.6f} ({'target holds here' if min_T >= math.pi - 1e-9 else 'below pi (expected, min over random is not the true worst case)'})")

if __name__ == "__main__":
    main()
