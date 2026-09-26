"""Stdlib-only, exact. For each k in [KMIN,KMAX] simulate the witness orbit with the literal definition of B
and check, at EVERY time t, the proof's Step-15 description:
  for t < k^2-k: D(B^t w) = D(delta_k) minus (row sigma_k^t(1) of track k) plus (row sigma_{k+1}^t(k+1) of track k+1),
  B^t w != delta_k, and at t = k^2-k: B^t w = delta_k.
Row r of track d is the cell (r, d+1-r); sigma_d^t(r) = ((r-1+t) mod d)+1.
Also checks t=k^2-k is the least t>=1 with t = 0 mod k and t = 2 mod (k+1) by brute force.
A finite range: sanity only, not a proof."""
import sys
def B(l):
    s = len(l)
    return tuple(sorted([x - 1 for x in l if x > 1] + [s], reverse=True))
def diagram(l):
    return {(i + 1, j + 1) for i, x in enumerate(l) for j in range(x)}
def main(a, b):
    ok = True
    for k in range(a, b + 1):
        delta = tuple(range(k, 0, -1))
        if k == 1:
            w = (1,); ok &= (w == delta); continue
        w = tuple([k - 1] + list(range(k - 1, 0, -1)) + [1])
        assert sum(w) == k * (k + 1) // 2 and all(w[i] >= w[i + 1] for i in range(len(w) - 1))
        Dd = diagram(delta)
        F = k * k - k
        tb = next(t for t in range(1, 10 * k * k) if t % k == 0 and t % (k + 1) == 2)
        if tb != F: print("tau brute mismatch", k, tb); ok = False
        x = w
        for t in range(F + 1):
            if t < F:
                hr = ((1 - 1 + t) % k) + 1
                cr = ((k + 1 - 1 + t) % (k + 1)) + 1
                pred = (Dd - {(hr, k + 1 - hr)}) | {(cr, k + 2 - cr)}
                if diagram(x) != pred or x == delta:
                    print("MISMATCH k", k, "t", t, x); ok = False; break
            else:
                if x != delta:
                    print("NOT delta at F, k", k); ok = False
            x = B(x)
    print(f"witness orbit description verified for all t<=k^2-k, k={a}..{b}:", "OK" if ok else "FAIL")
    return ok
if __name__ == "__main__":
    sys.exit(0 if main(int(sys.argv[1]), int(sys.argv[2])) else 1)
