# (1) sympy: exact identity of Step 5: sin(a+b)cos b - sin a == sin b cos(a+b).
# (2) exploratory (float, NOT load-bearing): maximise chain sum over admissible chains built
#     by Gram-Schmidt in R^(m-1) (x_k projected off span(x_1..x_{k-2})), random restarts + hill climb.
import sympy as sp, math, random, time
a, b = sp.symbols('a b', real=True)
print("Step5 identity residual:", sp.simplify(sp.expand_trig(sp.sin(a+b)*sp.cos(b) - sp.sin(a) - sp.sin(b)*sp.cos(a+b))))
random.seed(3)
dot = lambda u, v: sum(p*q for p, q in zip(u, v))
def chain(m, P):
    X = []
    for k in range(m):
        v = list(P[k])
        if k >= 2:
            B = []
            for w in X[:k-1]:           # orthonormal basis of span(x_1..x_{k-1}) via GS
                w = list(w)
                for e in B:
                    t = dot(w, e); w = [wi - t*ei for wi, ei in zip(w, e)]
                n = math.sqrt(dot(w, w))
                if n > 1e-10: B.append([wi/n for wi in w])
            for e in B:
                t = dot(v, e); v = [vi - t*ei for vi, ei in zip(v, e)]
        n = math.sqrt(dot(v, v))
        if n < 1e-10: return None
        X.append([vi/n for vi in v])
    return X
def val(X): return sum(math.acos(min(1.0, abs(dot(X[i], X[i+1])))) for i in range(len(X)-1))
t0 = time.time()
for m in range(2, 8):
    best = -1
    for r in range(30):
        P = [[random.gauss(0, 1) for _ in range(m-1)] for _ in range(m)]
        X = chain(m, P); cur = val(X) if X else -1
        step = 0.5
        for it in range(400):
            Q = [[p + step*random.gauss(0, 1) for p in row] for row in P]
            Y = chain(m, Q)
            if Y is None: continue
            v = val(Y)
            if v > cur: P, cur = Q, v
            else: step *= 0.995
        best = max(best, cur)
    print(f"m={m}: best float chain sum {best:.12f}, bound {(m-2)*math.pi/2:.12f}, gap {(m-2)*math.pi/2-best:.2e}")
print("elapsed %.1fs" % (time.time()-t0))
