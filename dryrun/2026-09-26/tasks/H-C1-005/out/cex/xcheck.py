"""Cross-check: literal path enumeration vs the provided checker inbox/checker/verify.py,
on the two submitted artefacts and on random labellings of Q_3, Q_4, Q_5."""
import os, random, subprocess, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from indep import count_literal, to_lines

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
CHECKER = os.path.join(ROOT, "inbox", "checker", "verify.py")
TMP = os.path.join(HERE, "_tmp.txt")


def checker(path, d):
    r = subprocess.run([sys.executable, CHECKER, path, "--d", str(d)],
                       capture_output=True, text=True)
    assert r.stdout.startswith("VERIFIED"), r.stdout + r.stderr
    return int(r.stdout.split()[1])


for d, name in ((3, "Q3.txt"), (4, "Q4.txt")):
    path = os.path.join(ROOT, "inbox", "subject", name)
    rows = [l.strip() for l in open(path).read().split("\n") if l.strip()]
    assert len(rows) == 2 ** d, (name, len(rows))
    assert len(set(rows)) == 2 ** d, "repeated vertex"
    assert all(len(r) == d and set(r) <= set("01") for r in rows)
    order = [int(r, 2) for r in rows]
    mine, theirs = count_literal(d, order), checker(path, d)
    print("%s: literal enumeration = %d, provided checker = %d, %s"
          % (name, mine, theirs, "AGREE" if mine == theirs else "MISMATCH"))

rng = random.Random(987654321)
for d in (3, 4, 5):
    bad = 0
    trials = 400 if d < 5 else 100
    for _ in range(trials):
        order = list(range(1 << d))
        rng.shuffle(order)
        open(TMP, "w").write(to_lines(d, order))
        if count_literal(d, order) != checker(TMP, d):
            bad += 1
            print("MISMATCH", order)
    print("d=%d random trials=%d mismatches=%d" % (d, trials, bad))
os.remove(TMP)
