#!/usr/bin/env python3
"""lp_A94.py -- H-C5-006. stdlib only, exact rational arithmetic (fractions).
Delsarte linear-programming bound for EVEN binary codes of length 9 with minimum distance >= 4.
An even code has all pairwise distances in {4, 6, 8}. Distance distribution A_i = (1/|C|) #{(x,y): d(x,y)=i}
satisfies A_0 = 1, A_i >= 0, sum_i A_i = |C| and (Delsarte) sum_i A_i K_k(i) >= 0 for k = 0..9, where
K_k(i) = sum_j (-1)^j C(i,j) C(9-i,k-j) (Krawtchouk). The script
 (1) enumerates all vertices of the 3-variable polytope {A_4, A_6, A_8 >= 0, Delsarte constraints} exactly and
     reports the maximum of 1 + A_4 + A_6 + A_8, checks boundedness;
 (2) finds and VERIFIES a dual certificate beta_k >= 0 with f(x) = 1 + sum_k beta_k K_k(x) <= 0 at x = 4, 6, 8,
     which proves |C| <= f(0) for every even (9,4) code (proof in out/proof.md, Step L3).
Combined with puncture+extend (proof.md) this gives A(9,4) <= floor(f(0))."""
from fractions import Fraction as Fr
from itertools import combinations
from math import comb

n = 9
def K(k, i):
    return sum((-1) ** j * comb(i, j) * comb(n - i, k - j) for j in range(0, k + 1))

D = [4, 6, 8]
# constraints as a.x >= b with x = (A4, A6, A8)
cons = []
for k in range(0, n + 1):
    cons.append(([Fr(K(k, i)) for i in D], Fr(-K(k, 0)), "Delsarte k=%d" % k))
for t in range(3):
    e = [Fr(0)] * 3; e[t] = Fr(1)
    cons.append((e, Fr(0), "A_%d>=0" % D[t]))

def solve3(M, b):
    # exact Gaussian elimination, returns None if singular
    M = [row[:] + [bb] for row, bb in zip(M, b)]
    for c in range(3):
        p = next((r for r in range(c, 3) if M[r][c] != 0), None)
        if p is None:
            return None
        M[c], M[p] = M[p], M[c]
        for r in range(3):
            if r != c and M[r][c] != 0:
                f = M[r][c] / M[c][c]
                M[r] = [a - f * bq for a, bq in zip(M[r], M[c])]
    return [M[r][3] / M[r][r] for r in range(3)]

best, bestv, bestset = None, None, None
nverts = 0
for trip in combinations(range(len(cons)), 3):
    x = solve3([cons[t][0] for t in trip], [cons[t][1] for t in trip])
    if x is None:
        continue
    if all(sum(a * xx for a, xx in zip(c[0], x)) >= c[1] for c in cons):
        nverts += 1
        val = 1 + sum(x)
        if best is None or val > best:
            best, bestv, bestset = val, x, trip
print("vertices:", nverts)
print("LP maximum of 1+A4+A6+A8 over vertices:", best, "=", float(best), "at A4,A6,A8 =", bestv,
      "tight:", [cons[t][2] for t in bestset])
# boundedness: sum of Delsarte k=... ; we verify directly with the dual certificate below (a certificate
# proves the bound for every feasible point, so boundedness is not needed for the final claim).

# dual certificate: choose beta_k >= 0 supported on the Delsarte rows tight at the optimum (k >= 1),
# solve f(x) = 0 at the D-points where A_x > 0 ... simplest robust way: small exact search.
tight_k = [int(cons[t][2].split("=")[1]) for t in bestset if cons[t][2].startswith("Delsarte")]
print("tight Delsarte rows:", tight_k)
# Solve for beta on tight rows: require f(i) = 0 for i in D with A_i > 0, f(i) <= 0 otherwise.
pos = [i for i, v in zip(D, bestv) if v > 0]
ks = [k for k in tight_k if k >= 1]
beta = None
if len(ks) == len(pos):
    # square system  sum_k beta_k K_k(i) = -1  for i in pos
    m = len(ks)
    M = [[Fr(K(k, i)) for k in ks] + [Fr(-1)] for i in pos]
    for c in range(m):
        p = next(r for r in range(c, m) if M[r][c] != 0)
        M[c], M[p] = M[p], M[c]
        for r in range(m):
            if r != c and M[r][c] != 0:
                f = M[r][c] / M[c][c]
                M[r] = [a - f * bq for a, bq in zip(M[r], M[c])]
    sol = [M[r][m] / M[r][r] for r in range(m)]
    beta = dict(zip(ks, sol))
print("beta:", beta)
ok = beta is not None and all(v >= 0 for v in beta.values())
fvals = {x: 1 + sum(b * K(k, x) for k, b in beta.items()) for x in [0] + D} if beta else {}
print("f values:", fvals)
ok = ok and all(fvals[x] <= 0 for x in D)
print("CERTIFICATE", "VALID" if ok else "INVALID", ": every even (9,4) code has |C| <= f(0) =", fvals.get(0))
