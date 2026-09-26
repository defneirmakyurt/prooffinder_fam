"""
Illustrative check for Part II (Approach A) of out/proof.md, Step 7.
NOT load-bearing for the d=2 proof (Part IV), which is unconditional and does not use this
script. This only substantiates the claim that the aggregate-moment + Jensen bound is too weak
at d=2, N=4, by evaluating arcsin(1/3) to high precision with mpmath (arbitrary precision,
error explicitly bounded by mpmath's working precision) and comparing to pi.

Run: /home/user/bainsahackathon/.venv/bin/python3 approach_A_check.py
"""
import mpmath as mp

mp.mp.dps = 50  # 50 decimal digits of precision

N, d = 4, 2
m = N * (N - 1) // 2  # C(N,2) = 6
r = d
mean_lower_bound = mp.mpf(N) * (N - r) / (2 * r * m)  # = N(N-r)/(2 r m)
jensen_bound = m * mp.asin(mean_lower_bound)

print("N(N-r)/(2 r m) =", mean_lower_bound)
print("Jensen lower bound on sum arcsin|G_ij| :", jensen_bound)
print("pi                                     :", mp.pi)
print("Jensen bound < pi ?", jensen_bound < mp.pi)
print("gap (pi - jensen_bound) =", mp.pi - jensen_bound)

assert jensen_bound < mp.pi, "expected the Jensen bound to be insufficient"
print("\nConfirmed: Approach A's aggregate bound (%.6f) is strictly less than the required "
      "pi (%.6f), by a margin of %.6f rad -- Approach A does not close (*)."
      % (jensen_bound, mp.pi, mp.pi - jensen_bound))
