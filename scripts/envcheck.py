#!/usr/bin/env python3
"""Report which tools the workers will need are available. Installs nothing.

Run with the interpreter the workers will use, e.g. .venv/bin/python3 scripts/envcheck.py
"""
import importlib
import os
import shutil
import subprocess
import sys

REQUIRED_MODULES = [("sympy", "sympy"), ("mpmath", "mpmath"), ("networkx", "networkx"),
                    ("flint", "python-flint"), ("pysat", "python-sat")]
SAT_SOLVERS = ["kissat", "cadical", "cryptominisat5", "glucose", "minisat"]
PROOF_CHECKERS = ["drat-trim", "cake_lpr", "lrat-check", "dpr-trim"]


def version_of(mod):
    return getattr(mod, "__version__", None) or getattr(mod, "VERSION", None) or "?"


def main():
    missing = []
    in_venv = sys.prefix != getattr(sys, "base_prefix", sys.prefix)
    print(f"python   {sys.version.split()[0]}  {sys.executable}  ({'venv' if in_venv else 'NOT a venv'})")
    if sys.version_info < (3, 9):
        missing.append("python >= 3.9")

    for mod_name, pip_name in REQUIRED_MODULES:
        try:
            mod = importlib.import_module(mod_name)
            print(f"ok       {pip_name} {version_of(mod)}")
        except Exception as exc:
            print(f"MISSING  {pip_name} ({type(exc).__name__})")
            missing.append(pip_name)

    try:
        from pysat.solvers import SolverNames
        names = sorted(k for k in vars(SolverNames) if not k.startswith("_"))
        print(f"info     python-sat bundled solvers: {', '.join(names)}")
    except Exception:
        pass

    found_sat = [s for s in SAT_SOLVERS if shutil.which(s)]
    found_chk = [c for c in PROOF_CHECKERS if shutil.which(c)]
    for s in found_sat:
        print(f"ok       SAT solver {s}: {shutil.which(s)}")
    for c in found_chk:
        print(f"ok       proof checker {c}: {shutil.which(c)}")
    if not found_sat:
        print(f"OPTIONAL no standalone SAT solver on PATH (looked for {', '.join(SAT_SOLVERS)})")
    if not found_chk:
        print(f"OPTIONAL no DRAT/LRAT proof checker on PATH (looked for {', '.join(PROOF_CHECKERS)})")

    root = os.path.realpath(os.path.join(os.path.dirname(__file__), ".."))
    guard = os.path.join(root, "scripts", "guard.py")
    probe = subprocess.run([shutil.which("python3") or "python3", guard], input="{}", capture_output=True, text=True)
    print(f"{'ok      ' if probe.returncode == 0 else 'BROKEN  '} isolation hook runs under PATH python3")
    if probe.returncode != 0:
        missing.append("working guard.py")

    print()
    if missing:
        print("Missing required: " + ", ".join(missing))
        print("To install (not done automatically):")
        print("  python3 -m venv .venv && .venv/bin/pip install -r requirements.txt")
        print("  brew install kissat cadical          # optional standalone SAT solvers")
        print("  drat-trim: build from https://github.com/marijnheule/drat-trim  # optional")
        sys.exit(1)
    print("All required tools present.")


if __name__ == "__main__":
    main()
