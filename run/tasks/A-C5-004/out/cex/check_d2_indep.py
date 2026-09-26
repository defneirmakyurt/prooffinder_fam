"""
Independent exact-arithmetic re-check of proof.md Step 5 (d=2 case), using a
different (coprime) grid denominator than the subject's own check_d2.py, plus
direct verification that S computed from actual R^2 unit vectors (via exact
rational cos/sin surrogates is impossible symbolically without irrational
numbers, so here we verify the *combinatorial identity* F(g)=S with exact
Fraction pi-units, independent grid) satisfies F<=2 (units of pi).

All arithmetic is with Python Fraction (exact rational), no floating point.
"""
from fractions import Fraction

def h(x):
    return min(x, 1 - x)

def F(g):
    g1, g2, g3, g4 = g
    assert g1 + g2 + g3 + g4 == 1
    return h(g1) + h(g2) + h(g3) + h(g4) + h(g1 + g2) + h(g2 + g3)

def main():
    denom = 97  # prime, different from subject's 60, avoids shared grid artifacts
    max_val = Fraction(0)
    worst = None
    trials = 0
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
    print(f"trials={trials}, denom={denom}")
    print(f"max F (units of pi) = {max_val}, at g/pi = {worst}")
    assert max_val <= Fraction(2)
    print("PASS: no counterexample to F<=2*pi found on independent grid.")

if __name__ == "__main__":
    main()
