# Non-load-bearing sanity check (floating point) of the key inequality in Step 5:
# for alpha, beta in [0, pi/2] with alpha+beta < pi/2: sin(alpha)/cos(beta) <= sin(alpha+beta).
# Also random test of the target via Gram-matrix construction is NOT attempted; the proof is purely written.
import math, random
random.seed(1)
worst = float('inf')
for _ in range(10**6):
    a = random.uniform(0, math.pi/2); b = random.uniform(0, math.pi/2 - a)
    if math.cos(b) == 0: continue
    worst = min(worst, math.sin(a+b) - math.sin(a)/math.cos(b))
print("min of sin(a+b) - sin(a)/cos(b) over 1e6 samples:", worst)
