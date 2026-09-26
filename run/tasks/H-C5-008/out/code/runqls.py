#!/usr/bin/env python3
"""runqls.py r iters seed class_idx... -- run qls on quotient classes, verify & lift best forest."""
import sys, subprocess, time
import quotients as Q
r = int(sys.argv[1]); iters = sys.argv[2]; seed = sys.argv[3]
classes = Q.code_classes(r)
sel = [int(a) for a in sys.argv[4:]] or range(len(classes))
for i in sel:
    words = Q.codewords_from_counts(classes[i], r)
    k, H, gens, proj = Q.quotient(words)
    fn = "../tmp/qls_r%d_c%d_s%s.txt" % (r, i, seed)
    t0 = time.time()
    out = subprocess.run(["./qls", str(k)] + [str(g) for g in gens] + [seed, iters, "0.6", "0.05", fn],
                         capture_output=True, text=True).stdout.strip()
    F = set(int(l) for l in open(fn) if l.strip())
    nbr = Q.quotient_graph(gens, k)
    ok = Q.is_forest_multi(F, nbr)
    T = Q.lift(F, proj)
    okT = Q.is_forest_qd(T)
    with open("../tmp/lift_r%d_c%d_s%s_%d.txt" % (r, i, seed, len(T)), "w") as fh:
        fh.write("\n".join(format(x, "09b") for x in sorted(T)) + "\n")
    print("r=%d class=%d counts=%s seed=%s iters=%s: %s |F|=%d forest=%s |T|=%d liftforest=%s %.1fs" %
          (r, i, classes[i], seed, iters, out, len(F), ok, len(T), okT, time.time() - t0), flush=True)
