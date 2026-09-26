#!/usr/bin/env python3
"""
certify.py -- rebuild the final CNF from scratch and certify UNSAT with a checked DRAT proof.

  python3 certify.py --d 9 --m 287 --kset 2,3,4,5,6,7,8 --sb root --cycles FILE \
                     --kissat PATH --drat PATH --work DIR

Steps (all exact):
 1. read the cycle list; check with enc.is_cycle_of_Qd that every entry is a cycle of Q_d
    (>= 4 distinct vertices, cyclically consecutive vertices differ in exactly one coordinate).
 2. build the CNF = subcube bounds (kset) + symmetry breaking (sb) + global sum >= m (stdlib
    totalizer) + one clause OR NOT x_v per cycle; write DIMACS.  stdlib only.
 3. run kissat on it with a textual DRAT proof; require exit status 20 (UNSAT).
 4. run drat-trim on (CNF, proof); require 's VERIFIED'.
Only step 4's verdict is used as the certificate; the solver is untrusted.
"""
import argparse
import os
import subprocess
import time

import enc
import symbreak


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--d", type=int, required=True)
    ap.add_argument("--m", type=int, required=True)
    ap.add_argument("--kset", default="2,3,4,5")
    ap.add_argument("--sb", default="")
    ap.add_argument("--cycles", default=None)
    ap.add_argument("--kissat", required=True)
    ap.add_argument("--drat", required=True)
    ap.add_argument("--work", required=True)
    ap.add_argument("--tlimit", type=int, default=500)
    ap.add_argument("--low", type=int, default=0, help="k_max for subcube lower bounds (0 = none)")
    ap.add_argument("--exact", type=int, default=0)
    a = ap.parse_args()
    t0 = time.time()
    d, m = a.d, a.m
    kset = [int(x) for x in a.kset.split(",") if x]
    pool = enc.Pool(1 << d)
    clauses = []
    if a.low:
        enc.build_subcube_S_counters(d, m, a.low, pool, clauses)
    if a.exact:
        enc.global_exact_and_edges(d, m, pool, clauses)
    if kset:
        enc.build_subcube_counters(d, set(kset), pool, clauses)
    if a.sb:
        symbreak.add(d, a.sb, pool, clauses)
    enc.global_atleast_stdlib(d, m, pool, clauses)
    ncyc = 0
    if a.cycles:
        for line in open(a.cycles):
            c = [int(x) for x in line.split()]
            if not c:
                continue
            if not enc.is_cycle_of_Qd(d, c):
                raise SystemExit("FAILED: not a cycle of Q_%d: %s" % (d, c))
            clauses.append([-(v + 1) for v in c])
            ncyc += 1
    os.makedirs(a.work, exist_ok=True)
    tag = "d%d_m%d" % (d, m)
    cnf = os.path.join(a.work, tag + ".cnf")
    prf = os.path.join(a.work, tag + ".drat")
    enc.write_dimacs(cnf, pool.top, clauses)
    t1 = time.time()
    print("CNF %s: vars=%d clauses=%d (cycle clauses %d) built in %.1fs" % (cnf, pool.top, len(clauses), ncyc, t1 - t0), flush=True)
    r = subprocess.run([a.kissat, "-q", "--no-binary", "--time=%d" % a.tlimit, cnf, prf],
                       stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    t2 = time.time()
    print("kissat exit %d (%s) in %.1fs" % (r.returncode, "UNSAT" if r.returncode == 20 else "SAT" if r.returncode == 10 else "UNKNOWN", t2 - t1), flush=True)
    if r.returncode != 20:
        print("NOT CERTIFIED")
        return
    psz = os.path.getsize(prf)
    r2 = subprocess.run([a.drat, cnf, prf, "-t", str(a.tlimit)], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    t3 = time.time()
    verdict = "s VERIFIED" if "s VERIFIED" in r2.stdout else "NOT VERIFIED"
    print("proof %d bytes; drat-trim: %s in %.1fs" % (psz, verdict, t3 - t2))
    print("CERTIFIED: no induced forest of Q_%d with %d vertices (so F_%d <= %d)" % (d, m, d, m - 1)
          if verdict == "s VERIFIED" else "NOT CERTIFIED")
    print("total %.1fs" % (t3 - t0))


if __name__ == "__main__":
    main()
