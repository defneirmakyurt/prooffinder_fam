"""
Exact-arithmetic sanity check for the d=2 (N=4) case.

We verify, using exact rational arithmetic (via Python's Fraction, with pi
kept symbolic through sympy), the algebraic identity used in the proof:

    F(g1,g2,g3,g4) = h(g1)+h(g2)+h(g3)+h(g4)+h(g1+g2)+h(g2+g3) <= 2*pi

whenever g1,g2,g3,g4 >= 0 and g1+g2+g3+g4 = pi, where h(x) = min(x, pi-x).

This is not itself the proof (the proof is the case analysis in proof.md,
Step 4-5); this script is a finite sanity check on many rational sample
points (expressed as rational multiples of pi, so all comparisons are
between exact rational numbers, no floating point involved) to catch
algebra mistakes. It cannot substitute for the general argument (a finite
check proves nothing about all real g_i), so proof.md does not rest on it.
"""
from fractions import Fraction
import itertools
import random

def h(x):
    # x is a Fraction representing a multiple of pi (x in [0,1] means x*pi)
    return min(x, 1 - x)

def F(g):
    g1, g2, g3, g4 = g
    assert g1 + g2 + g3 + g4 == 1  # sum = pi, in units of pi
    return h(g1) + h(g2) + h(g3) + h(g4) + h(g1 + g2) + h(g2 + g3)

def check_all_nonneg(g):
    return all(x >= 0 for x in g)

def random_rational_partition(denom, n=4, rng=random.Random(0)):
    # random composition of 'denom' into n nonnegative integer parts, each part/denom used
    cuts = sorted(rng.sample(range(0, denom + 1), n - 1))
    parts = []
    prev = 0
    for c in cuts:
        parts.append(c - prev)
        prev = c
    parts.append(denom - prev)
    return tuple(Fraction(p, denom) for p in parts)

def main():
    max_val = Fraction(0)
    worst = None
    trials = 0
    denom = 60  # fine grid, exact fractions
    rng = random.Random(12345)
    # 1) exhaustive grid over compositions of `denom` into 4 nonneg parts (exact)
    for c1 in range(denom + 1):
        for c2 in range(denom + 1 - c1):
            for c3 in range(denom + 1 - c1 - c2):
                c4 = denom - c1 - c2 - c3
                g = (Fraction(c1, denom), Fraction(c2, denom), Fraction(c3, denom), Fraction(c4, denom))
                val = F(g)
                trials += 1
                if val > max_val:
                    max_val = val
                    worst = g
    print(f"Exhaustive grid (denom={denom}): trials={trials}")
    print(f"max F found (units of pi) = {max_val}  (bound to prove: 2)")
    print(f"achieved at g/pi = {worst}")
    assert max_val <= Fraction(2), "COUNTEREXAMPLE to F <= 2*pi found!"
    # 2) also check the two known extremal families exactly
    # doubled axes: g=(0,1/2,0,1/2)*pi
    g_doubled = (Fraction(0), Fraction(1,2), Fraction(0), Fraction(1,2))
    # evenly spaced: g=(1/4,1/4,1/4,1/4)*pi
    g_even = (Fraction(1,4), Fraction(1,4), Fraction(1,4), Fraction(1,4))
    print("F(doubled-axes config) / pi =", F(g_doubled), " (expect 2)")
    print("F(evenly-spaced config) / pi =", F(g_even), " (expect 2)")
    assert F(g_doubled) == 2
    assert F(g_even) == 2
    print("All checks passed: max over grid <= 2*pi, both known extremal configs attain exactly 2*pi.")

if __name__ == "__main__":
    main()
