"""R9/R11 cross-checks.

(A) counter agreement: for many random labellings of Q_d, my internal counter uphill.count
    must equal the provided checker inbox/checker/verify.py.
(B) threshold sweep: bnb.py d T for T = 1..Tmax must say NONE BELOW T for T <= V and
    FOUND (a value < T) for T > V, where V is the claimed minimum.
Usage: python3 crosscheck.py counter <d> <trials> <checker_path>
       python3 crosscheck.py sweep <d> <Tmax>
"""
import os
import random
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from uphill import count, to_lines

HERE = os.path.dirname(os.path.abspath(__file__))


def counter_check(d, trials, checker):
    rng = random.Random(12345)
    n = 1 << d
    tmp = os.path.join(HERE, "_cc_tmp.txt")
    bad = 0
    for t in range(trials):
        order = list(range(n))
        rng.shuffle(order)
        mine = count(d, order)
        open(tmp, "w").write(to_lines(d, order))
        out = subprocess.run([sys.executable, checker, tmp, "--d", str(d)],
                             capture_output=True, text=True)
        theirs = int(out.stdout.split()[1])
        if mine != theirs:
            bad += 1
            print("MISMATCH", order, mine, theirs)
    os.remove(tmp)
    print("d=%d trials=%d mismatches=%d" % (d, trials, bad))


def sweep(d, tmax):
    for T in range(1, tmax + 1):
        out = subprocess.run([sys.executable, os.path.join(HERE, "bnb.py"), str(d), str(T)],
                             capture_output=True, text=True)
        lines = out.stdout.strip().split("\n")
        verdict = [l for l in lines if l.startswith("NONE") or l.startswith("FOUND")][0]
        print("T=%-3d %s" % (T, verdict), flush=True)


if __name__ == "__main__":
    if sys.argv[1] == "counter":
        counter_check(int(sys.argv[2]), int(sys.argv[3]), sys.argv[4])
    else:
        sweep(int(sys.argv[2]), int(sys.argv[3]))
