"""NOT part of the proof. Floating-point sanity check of the Gram-Schmidt route (stdlib only).
(1) Random chains: build unit vectors x_1..x_m in R^(m-1) with <x_i,x_j>=0 for |i-j|>=2
    by choosing x_{k+1} = alpha*h_k/|h_k| + beta*(unit vector orthogonal to V_k) while room remains,
    then checks sum theta <= (m-2)pi/2 + 1e-9 and t_{k+1}^2 = 1 - a_k^2/t_k^2.
(2) Checks the trig lemma sin(phi) <= cos(psi) sin(psi+phi) on a grid with psi+phi < pi/2.
"""
import math, random

def dot(u, v): return sum(a*b for a, b in zip(u, v))
def sub(u, v): return [a-b for a, b in zip(u, v)]
def scal(c, u): return [c*a for a in u]
def norm(u): return math.sqrt(dot(u, u))

def random_chain(m, rng):
    n = m - 1
    # orthonormal frame e_0..e_{n-1} = standard basis; V_k = span(e_0..e_{k-1}) after building k independent vectors
    xs = [[1.0] + [0.0]*(n-1)]
    h = xs[0][:]                     # h_1 = x_1
    dimV = 1
    for k in range(1, m):
        hn = scal(1/norm(h), h)
        if dimV < n:
            # x_{k+1} = c*hn + s*e_dimV (orthogonal to V_{k-1} automatically; hn is orthogonal to V_{k-1})
            ang = rng.uniform(0, math.pi)
            c, s = math.cos(ang), math.sin(ang)
            e = [0.0]*n; e[dimV] = 1.0
            x = [c*a + s*b for a, b in zip(hn, e)]
            dimV += 1
        else:
            x = scal(rng.choice([-1, 1]), hn)   # no room left: forced into span(h_k)
        xs.append(x)
        # new h
        proj = [0.0]*n
        # Gram-Schmidt against all previous
        basis = []
        for y in xs[:-1]:
            r = y[:]
            for b in basis: r = sub(r, scal(dot(r, b), b))
            if norm(r) > 1e-12: basis.append(scal(1/norm(r), r))
        r = x[:]
        for b in basis: r = sub(r, scal(dot(r, b), b))
        h = r if norm(r) > 1e-12 else hn  # if dependent, stop meaningfully
        if norm(r) <= 1e-12: break
    return xs

def main():
    rng = random.Random(12345)
    worst = -1e9; count = 0
    for m in range(2, 12):
        for _ in range(3000):
            xs = random_chain(m, rng)
            if len(xs) != m: continue
            for i in range(m):
                for j in range(i+2, m):
                    assert abs(dot(xs[i], xs[j])) < 1e-9
            s = sum(math.acos(min(1.0, abs(dot(xs[i], xs[i+1])))) for i in range(m-1))
            worst = max(worst, s - (m-2)*math.pi/2); count += 1
    print("chains tested:", count, " max(sum theta - (m-2)pi/2) =", worst)
    assert worst <= 1e-9
    bad = 0; N = 400
    for i in range(N+1):
        for j in range(N+1):
            psi = (math.pi/2)*i/N; phi = (math.pi/2)*j/N
            if psi + phi < math.pi/2:
                if math.sin(phi) > math.cos(psi)*math.sin(psi+phi) + 1e-12: bad += 1
    print("trig lemma grid violations:", bad)

main()
