#!/usr/bin/env python3
"""Scratch-copy tests for scripts/guard.py (build step B2): 15 baseline cases + referee out/cex/ cases."""
import json
import os
import shutil
import subprocess
import sys
import tempfile

REPO = os.path.realpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
S = os.path.join(tempfile.gettempdir(), "pp_tests", "guard_sandbox")
GUARD = os.path.join(S, "scripts", "guard.py")
T1, T2 = "A-C1-001", "A-C1-002"
fails = []


def setup():
    shutil.rmtree(S, ignore_errors=True)
    os.makedirs(os.path.join(S, "scripts"))
    shutil.copy2(os.path.join(REPO, "scripts", "guard.py"), GUARD)
    for t in (T1, T2):
        for sub in ("inbox", "out/cex"):
            os.makedirs(os.path.join(S, "run", "tasks", t, sub))
        open(os.path.join(S, "run", "tasks", t, "brief.md"), "w").close()
    os.makedirs(os.path.join(S, ".claude", "skills"))
    os.makedirs(os.path.join(S, "dryrun"))
    open(os.path.join(S, "run", "board.md"), "w").close()


def task(*parts, t=T1):
    return os.path.join(S, "run", "tasks", t, *parts)


def case(name, expect, tool, tool_input, agent="prover", cwd=None, agent_id="w1", bound=T1):
    os.makedirs(os.path.join(S, "run", ".guard"), exist_ok=True)
    bind = os.path.join(S, "run", ".guard", agent_id)
    if bound:
        with open(bind, "w") as fh:
            fh.write(bound)
    elif os.path.exists(bind):
        os.remove(bind)
    payload = {"tool_name": tool, "tool_input": tool_input, "cwd": cwd or task()}
    if agent:
        payload.update(agent_id=agent_id, agent_type=agent)
    res = subprocess.run([sys.executable, GUARD], input=json.dumps(payload), capture_output=True, text=True,
                         env={**os.environ, "CLAUDE_PROJECT_DIR": S})
    got = "deny" if '"deny"' in res.stdout else "allow"
    ok = got == expect and res.returncode == 0
    print(f"{'PASS' if ok else 'FAIL'} {expect:5} {name}" + ("" if ok else f"  (got {got}; {res.stdout}{res.stderr})"))
    if not ok:
        fails.append(name)


def baseline():
    print("== baseline (15)")
    case("head call passes untouched", "allow", "Read", {"file_path": os.path.join(S, "run", "board.md")}, agent=None)
    case("worker reads own brief (binds)", "allow", "Read", {"file_path": task("brief.md")}, bound=None)
    case("worker reads another task", "deny", "Read", {"file_path": task("out", "proof.md", t=T2)})
    case("worker reads the board", "deny", "Read", {"file_path": os.path.join(S, "run", "board.md")})
    case("worker reads .claude/", "deny", "Read", {"file_path": os.path.join(S, ".claude", "skills", "x.md")})
    case("worker reads dryrun/", "deny", "Read", {"file_path": os.path.join(S, "dryrun", "x.md")})
    case("worker writes own out/", "allow", "Write", {"file_path": task("out", "proof.md")})
    case("worker writes own inbox/", "deny", "Write", {"file_path": task("inbox", "x.md")})
    case("worker writes outside run/", "deny", "Write", {"file_path": "/tmp/pp_guard_x.md"})
    case("worker reads a system file", "allow", "Read", {"file_path": "/usr/share/dict/words"})
    case("Glob from project root", "deny", "Glob", {"pattern": "**/*.md", "path": S})
    case("Grep inside own task", "allow", "Grep", {"pattern": "x", "path": task()})
    case("Bash cat another task", "deny", "Bash", {"command": f"cat run/tasks/{T2}/out/proof.md"}, cwd=S)
    case("Bash recursive find from root", "deny", "Bash", {"command": "find . -name '*.md'"}, cwd=S)
    case("Bash ../ into another task", "deny", "Bash", {"command": f"cat ../{T2}/brief.md"}, cwd=task())


def cex():
    print("== referee out/cex/ cases")
    r = dict(agent="referee", agent_id="r1")
    case("referee Write verdict.md", "allow", "Write", {"file_path": task("out", "verdict.md")}, **r)
    case("referee Write out/notes.md", "deny", "Write", {"file_path": task("out", "notes.md")}, **r)
    case("referee Write out/cex/search.py", "allow", "Write", {"file_path": task("out", "cex", "search.py")}, **r)
    case("referee Bash mkdir -p out/cex", "allow", "Bash", {"command": "mkdir -p out/cex"}, **r)
    case("referee Bash heredoc into out/cex", "allow", "Bash",
         {"command": "cat > out/cex/s.py <<'EOF'\nimport sys\nprint(1) > 0\nEOF"}, **r)
    case("referee Bash heredoc body is not parsed", "allow", "Bash",
         {"command": "cat > out/cex/s.sh <<EOF\necho x > /tmp/elsewhere\nEOF"}, **r)
    case("referee Bash redirect into out/cex + 2>&1", "allow", "Bash",
         {"command": "python3 out/cex/s.py > out/cex/log.txt 2>&1"}, **r)
    case("referee Bash timed run into out/cex", "allow", "Bash",
         {"command": "/usr/bin/time -p python3 out/cex/s.py > out/cex/t.log 2>/dev/null"}, **r)
    case("referee Bash cd out/cex && ... | tee", "allow", "Bash",
         {"command": "cd out/cex && python3 s.py | tee run.log"}, **r)
    case("referee Bash absolute path into out/cex", "allow", "Bash",
         {"command": f"echo 1 > {task('out', 'cex', 'a.txt')}"}, cwd=S, **r)
    case("referee Bash check only, no writes", "allow", "Bash", {"command": "python3 -c 'print(2**10)' 2>/dev/null"}, **r)
    case("referee Bash writes verdict.md", "deny", "Bash", {"command": "echo ACCEPT > out/verdict.md"}, **r)
    case("referee Bash writes out/notes.txt", "deny", "Bash", {"command": "python3 s.py > out/notes.txt"}, **r)
    case("referee Bash rm verdict.md", "deny", "Bash", {"command": "rm out/verdict.md"}, **r)
    case("referee Bash tee to /tmp", "deny", "Bash", {"command": "python3 x.py | tee /tmp/pp_x.log"}, **r)
    case("referee Bash cp into another task's cex", "deny", "Bash",
         {"command": f"cp out/cex/a.py run/tasks/{T2}/out/cex/"}, cwd=S, **r)
    case("referee Bash cd .. then write", "deny", "Bash", {"command": "cd .. && echo x > leak.txt"}, **r)
    case("referee Bash glued redirect to out/", "deny", "Bash", {"command": "echo x>out/x.txt"}, **r)
    case("prover Bash writes out/ (unchanged)", "allow", "Bash", {"command": "python3 a.py > out/log.txt"})


if __name__ == "__main__":
    setup()
    baseline()
    cex()
    print("ALL PASSED" if not fails else f"{len(fails)} FAILED: {'; '.join(fails)}")
    sys.exit(1 if fails else 0)
