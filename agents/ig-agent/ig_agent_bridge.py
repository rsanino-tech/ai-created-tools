#!/usr/bin/env python3
"""Lovely's Choice IG Agent bridge.

Polls a dedicated GitHub issue for COMMAND: comments and executes a very small,
allowlisted set of local IG-Agent maintenance actions. This bridge is intentionally
NOT a general shell executor.
"""

from __future__ import annotations

import json
import os
import subprocess
import time
from pathlib import Path

REPO = os.getenv("IG_AGENT_GITHUB_REPO", "rsanino-tech/rsanino-tech")
ISSUE = os.getenv("IG_AGENT_GITHUB_ISSUE", "9")
POLL_SECONDS = int(os.getenv("IG_AGENT_POLL_SECONDS", "20"))
WORKDIR = Path(os.getenv("IG_AGENT_WORKDIR", str(Path.home() / "LovelysChoice" / "ig-agent"))).expanduser()
STATE_FILE = WORKDIR / "data" / "bridge_state.json"
LOG_FILE = WORKDIR / "logs" / "bridge.log"


def run(cmd: list[str], timeout: int = 30) -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, capture_output=True, text=True, timeout=timeout, check=False)


def ensure_layout() -> None:
    for p in [
        WORKDIR / "app",
        WORKDIR / "config",
        WORKDIR / "content" / "approved",
        WORKDIR / "content" / "scheduled",
        WORKDIR / "content" / "posted",
        WORKDIR / "content" / "failed",
        WORKDIR / "logs",
        WORKDIR / "data",
        WORKDIR / "backups",
        WORKDIR / "docs",
    ]:
        p.mkdir(parents=True, exist_ok=True)
    if not STATE_FILE.exists():
        STATE_FILE.write_text(json.dumps({"last_comment_id": 0}, indent=2))


def log(message: str) -> None:
    stamp = time.strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{stamp}] {message}\n"
    print(line, end="")
    with LOG_FILE.open("a") as f:
        f.write(line)


def load_last_comment_id() -> int:
    try:
        return int(json.loads(STATE_FILE.read_text()).get("last_comment_id", 0))
    except Exception:
        return 0


def save_last_comment_id(comment_id: int) -> None:
    STATE_FILE.write_text(json.dumps({"last_comment_id": comment_id}, indent=2))


def gh_comments() -> list[dict]:
    cp = run([
        "gh", "api", f"repos/{REPO}/issues/{ISSUE}/comments", "--paginate"
    ], timeout=30)
    if cp.returncode != 0:
        raise RuntimeError(cp.stderr.strip() or "gh api failed")
    return json.loads(cp.stdout or "[]")


def post_result(body: str) -> None:
    cp = run([
        "gh", "issue", "comment", ISSUE, "--repo", REPO, "--body", body
    ], timeout=30)
    if cp.returncode != 0:
        raise RuntimeError(cp.stderr.strip() or "failed to post result")


def docker_status() -> str:
    cp = run(["docker", "ps", "--format", "table {{.Names}}\t{{.Status}}\t{{.Ports}}"], timeout=20)
    return cp.stdout.strip() if cp.returncode == 0 else f"docker error: {cp.stderr.strip()}"


def ollama_status() -> str:
    cp = run(["ollama", "list"], timeout=20)
    return cp.stdout.strip() if cp.returncode == 0 else f"ollama error: {cp.stderr.strip()}"


def tree_status() -> str:
    items = []
    for path in sorted(WORKDIR.rglob("*")):
        if ".git" in path.parts:
            continue
        try:
            rel = path.relative_to(WORKDIR)
        except ValueError:
            continue
        if len(rel.parts) <= 3:
            items.append(str(rel) + ("/" if path.is_dir() else ""))
    return "\n".join(items[:200]) or "(empty)"


def write_health_file() -> str:
    health = {
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "workdir": str(WORKDIR),
        "github_repo": REPO,
        "github_issue": ISSUE,
        "poll_seconds": POLL_SECONDS,
        "ollama": ollama_status(),
        "docker": docker_status(),
    }
    path = WORKDIR / "data" / "health.json"
    path.write_text(json.dumps(health, indent=2))
    return str(path)


def execute(command: str) -> str:
    c = command.strip().lower()

    if c in {"health", "health check", "status", "system status"}:
        path = write_health_file()
        return f"STATUS: VERIFIED\nACTION: health\nHEALTH_FILE: {path}\n\nOLLAMA:\n{ollama_status()}\n\nDOCKER:\n{docker_status()}"

    if c in {"show workspace", "list workspace", "workspace tree"}:
        return f"STATUS: VERIFIED\nACTION: workspace-tree\n\n{tree_status()}"

    if c in {"initialize workspace", "init workspace", "create workspace"}:
        ensure_layout()
        return f"STATUS: VERIFIED\nACTION: initialize-workspace\nWORKDIR: {WORKDIR}\n\n{tree_status()}"

    if c in {"check ollama", "ollama status"}:
        return f"STATUS: VERIFIED\nACTION: ollama-status\n\n{ollama_status()}"

    if c in {"check docker", "docker status"}:
        return f"STATUS: VERIFIED\nACTION: docker-status\n\n{docker_status()}"

    return (
        "STATUS: REJECTED\n"
        "DETAIL: Command is outside the IG Agent bridge allowlist.\n"
        "ALLOWED: initialize workspace | workspace tree | health check | ollama status | docker status"
    )


def main() -> None:
    ensure_layout()
    log("IG AGENT BRIDGE ONLINE")
    log(f"Workdir: {WORKDIR}")
    log(f"Watching GitHub issue {REPO}#{ISSUE}")
    log(f"Polling every {POLL_SECONDS} seconds")

    while True:
        try:
            last_id = load_last_comment_id()
            comments = gh_comments()
            for item in comments:
                cid = int(item.get("id", 0))
                body = (item.get("body") or "").strip()
                if cid <= last_id:
                    continue
                save_last_comment_id(cid)
                if not body.startswith("COMMAND:"):
                    continue
                command = body[len("COMMAND:"):].strip()
                log(f"Received command #{cid}: {command}")
                result = execute(command)
                post_result(f"RESULT:\n{result}")
        except KeyboardInterrupt:
            log("Bridge stopped by user")
            break
        except Exception as exc:
            log(f"ERROR: {exc}")
        time.sleep(POLL_SECONDS)


if __name__ == "__main__":
    main()
