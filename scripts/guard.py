#!/usr/bin/env python3
"""PreToolUse hook enforcing worker isolation.

Calls from the head (no agent_id) pass untouched. A worker is bound to the
first run/tasks/<id>/ it touches; after that it may read only that folder
and write only its out/ (referees: only out/verdict.md). run/ outside the
task, .claude/ and dryrun/ are always off limits. Bash is checked by
scanning the command for path-like tokens, which is best effort only.
"""
import json
import os
import re
import shlex
import sys

PROJECT = os.path.realpath(os.environ.get("CLAUDE_PROJECT_DIR") or os.getcwd())
RUN = os.path.join(PROJECT, "run")
TASKS = os.path.join(RUN, "tasks")
FORBIDDEN_ROOTS = [os.path.join(PROJECT, ".claude"), os.path.join(PROJECT, "dryrun")]
BIND_DIR = os.path.join(RUN, ".guard")


def deny(reason):
    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": "deny",
        "permissionDecisionReason": "ISOLATION: " + reason +
        " Stay inside your own run/tasks/<task-id>/ (read brief.md + inbox/, write out/).",
    }}))
    sys.exit(0)


def under(path, root):
    return path == root or path.startswith(root + os.sep)


def resolve(p, cwd):
    p = os.path.expanduser(p)
    if not os.path.isabs(p):
        p = os.path.join(cwd, p)
    return os.path.realpath(p)


def task_of(path):
    if not under(path, TASKS) or path == TASKS:
        return None
    return os.path.relpath(path, TASKS).split(os.sep)[0]


def bound_task(agent_id):
    try:
        with open(os.path.join(BIND_DIR, agent_id)) as fh:
            return fh.read().strip()
    except FileNotFoundError:
        return None


def bind(agent_id, task):
    os.makedirs(BIND_DIR, exist_ok=True)
    with open(os.path.join(BIND_DIR, agent_id), "w") as fh:
        fh.write(task)


def check(path, write, agent_id, agent_type):
    if any(under(path, r) for r in FORBIDDEN_ROOTS):
        deny(f"{path} is outside your task folder.")
    if not under(path, RUN):
        if write:
            deny(f"writes are allowed only under your task's out/, not {path}.")
        return
    task = task_of(path)
    if task is None or "*" in task or "?" in task:
        deny(f"{path} is ledger space you may not see.")
    mine = bound_task(agent_id)
    if mine is None:
        bind(agent_id, task)
        mine = task
    if task != mine:
        deny(f"{path} belongs to another task ({task}); you are bound to {mine}.")
    if write:
        out = os.path.join(TASKS, mine, "out")
        if not under(path, out):
            deny(f"you may write only under {out}.")
        if agent_type == "referee" and path != os.path.join(out, "verdict.md"):
            deny("a referee writes only out/verdict.md.")


PATHISH = re.compile(r"(^|/)(run|\.claude|dryrun)/|/(run|\.claude|dryrun)$|^(\.claude|dryrun)$|(^|/)\.\.(/|$)")


def bash_paths(command):
    try:
        tokens = shlex.split(command, posix=True)
    except ValueError:
        tokens = command.split()
    found = []
    for tok in tokens:
        for piece in re.split(r"[=:;|&<>(){}\s,]+", tok):
            if piece and PATHISH.search(piece):
                found.append(piece)
    return found


def referee_writes(command):
    first = command.split("\n")[0] if "<<" in command else command
    try:
        tokens = shlex.split(first, posix=True)
    except ValueError:
        tokens = first.split()
    for i, tok in enumerate(tokens):
        if tok in ("tee", "cp", "mv", "touch", "mkdir", "dd"):
            return True
        m = re.match(r"^\d*>>?(.*)$", tok)
        if m:
            target = m.group(1) or (tokens[i + 1] if i + 1 < len(tokens) else "")
            if not (target.startswith("&") or target == "/dev/null"):
                return True
    return False


def main():
    data = json.load(sys.stdin)
    agent_id = data.get("agent_id")
    if not agent_id:
        sys.exit(0)
    agent_type = (data.get("agent_type") or "").split(":")[-1]
    cwd = data.get("cwd") or PROJECT
    tool = data.get("tool_name", "")
    ti = data.get("tool_input") or {}

    if tool in ("Read", "NotebookRead"):
        check(resolve(ti.get("file_path", ""), cwd), False, agent_id, agent_type)
    elif tool in ("Write", "Edit", "MultiEdit", "NotebookEdit"):
        check(resolve(ti.get("file_path") or ti.get("notebook_path", ""), cwd), True, agent_id, agent_type)
    elif tool in ("Glob", "Grep"):
        base = resolve(ti.get("path") or cwd, cwd)
        pattern = ti.get("pattern", "") if tool == "Glob" else ""
        prefix = re.split(r"[*?\[{]", pattern)[0]
        root = resolve(os.path.dirname(prefix), base) if prefix else base
        if under(RUN, root):
            deny(f"searching {root} would reach other tasks; search inside your task folder.")
        check(root, False, agent_id, agent_type)
    elif tool == "Bash":
        cmd = ti.get("command", "")
        if agent_type == "referee" and referee_writes(cmd):
            deny("a referee may run checks but not write files from Bash; write only out/verdict.md.")
        if under(RUN, resolve(cwd, PROJECT)):
            if re.search(r"\b(find|grep\s+-[a-zA-Z]*[rR]|rg|tree|ls\s+-[a-zA-Z]*R|du)\b", cmd) and not bash_paths(cmd):
                deny("recursive listing/search from the project root or run/ is not allowed; cd into your task folder first.")
        for p in bash_paths(cmd):
            check(resolve(p, cwd), False, agent_id, agent_type)
    sys.exit(0)


if __name__ == "__main__":
    main()
