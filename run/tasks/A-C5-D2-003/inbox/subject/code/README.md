# Code for A-C5-001

## check_d2.py

Exact-arithmetic (Python `fractions.Fraction`, no floating point) sanity check for the d=2
case of proof.md Step 5. It evaluates F(g1,g2,g3,g4) = h(g1)+h(g2)+h(g3)+h(g4)+h(g1+g2)+h(g2+g3),
with h(x)=min(x,pi-x), over an exhaustive grid of rational compositions of pi into 4 nonnegative
parts (denominator 60, i.e. all g_i are multiples of pi/60 summing to pi: 39711 grid points), and
confirms max F <= 2*pi on the grid, with equality at the two known extremal configurations
(doubled orthogonal axes, and 4 evenly spaced lines).

This is a finite check and, on its own, proves nothing about the continuum of real-valued
g_i (per the brief's rule G7): the actual proof that F<=2*pi for ALL real g_i>=0 summing to pi is
the case-A/case-B algebraic argument in proof.md Step 5, which is a complete written proof not
resting on this computation. The script is included purely as an independent sanity check that
did not turn up any counterexample or algebra error.

### How to run

```
/home/user/bainsahackathon/.venv/bin/python3 check_d2.py
```

### Measured run

Command: `time /home/user/bainsahackathon/.venv/bin/python3 check_d2.py`
Output (abridged):
```
Exhaustive grid (denom=60): trials=39711
max F found (units of pi) = 2  (bound to prove: 2)
achieved at g/pi = (Fraction(0, 1), Fraction(1, 2), Fraction(0, 1), Fraction(1, 2))
F(doubled-axes config) / pi = 2  (expect 2)
F(evenly-spaced config) / pi = 2  (expect 2)
All checks passed: ...
```
Measured wall time: 0.85s (real), well under the 10-minute limit. All arithmetic is exact
(Python Fraction), so this is not subject to floating-point error.
