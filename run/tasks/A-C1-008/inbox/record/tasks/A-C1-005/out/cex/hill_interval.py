"""Continuous counterexample search for A-C1 with ball-arithmetic certification (python-flint arb, 200 bits).
Float hill-climbing from random starts for N=2..12; each final configuration (angles = the exact binary floats found)
is re-evaluated rigorously straight from the definition: S = sum arccos|cos(a_i - a_j)|, and compared with
(pi/2) floor(N^2/4). A violation needs lower(S) > upper(bound). Report certified-below / overlapping / certified-above.
"""
import random, math
import flint
from flint import arb, ctx
ctx.prec = 200

def S_float(a):
    n = len(a); s = 0.0
    for i in range(n):
        for j in range(i + 1, n):
            s += math.acos(min(1.0, abs(math.cos(a[i] - a[j]))))
    return s

def S_arb(a):
    n = len(a); s = arb(0)
    A = [arb(x) for x in a]  # exact binary floats
    for i in range(n):
        for j in range(i + 1, n):
            c = abs((A[i] - A[j]).cos())
            # acos of a ball that may poke above 1 is nan; clamp rigorously: |cos| <= 1 always
            if c.upper() > 1:
                lo = c.lower()
                c = arb.union(lo, arb(1)) if lo < 1 else arb(1)
            s += c.acos()
    return s

def main():
    rng = random.Random(777)
    below = overlap = above = 0
    worst = {}
    for N in range(2, 13):
        for trial in range(6):
            a = [rng.uniform(0, math.pi) for _ in range(N)]
            s = S_float(a); step = 0.6
            for it in range(6000):
                b = list(a); i = rng.randrange(N); b[i] += rng.gauss(0, step)
                t = S_float(b)
                if t >= s: a, s = b, t
                if it % 600 == 599: step *= 0.5
            Sa = S_arb(a)
            B = arb.pi() / 2 * (N * N // 4)
            if Sa.upper() < B.lower(): below += 1
            elif Sa.lower() > B.upper(): above += 1; print("CERTIFIED VIOLATION", N, a)
            else: overlap += 1
            gap = float(B.lower() - Sa.upper())
            worst[N] = min(worst.get(N, 1e9), gap)
    print(f"ball-certified (200 bits): below bound {below}, overlapping (not decided) {overlap}, above bound {above}")
    for N, gp in worst.items():
        print(f"N={N}: min over 6 climbs of certified lower bound on (bound - S): {gp:.3e}")

main()
