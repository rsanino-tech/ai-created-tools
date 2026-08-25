#!/bin/zsh
set -euo pipefail

ROOT="$HOME/LovelysChoice/ig-agent"
REPO="rsanino-tech/ai-created-tools"
BRIDGE_PATH="agents/ig-agent/ig_agent_bridge.py"

mkdir -p "$ROOT"/{app,config,content/{approved,scheduled,posted,failed},logs,data,backups,docs}

if ! command -v gh >/dev/null 2>&1; then
  echo "ERROR: GitHub CLI (gh) is not installed."
  exit 1
fi

if ! gh auth status >/dev/null 2>&1; then
  echo "ERROR: GitHub CLI is not authenticated."
  exit 1
fi

if ! command -v ollama >/dev/null 2>&1; then
  echo "ERROR: Ollama is not available in PATH."
  exit 1
fi

gh api "repos/$REPO/contents/$BRIDGE_PATH" --jq .content | tr -d '\n' | base64 --decode > "$ROOT/ig_agent_bridge.py"
chmod 700 "$ROOT/ig_agent_bridge.py"

cat > "$ROOT/.gitignore" <<'EOF'
.env
*.log
__pycache__/
data/
backups/
.DS_Store
EOF

cat > "$ROOT/config/agent.env.example" <<'EOF'
IG_AGENT_GITHUB_REPO=rsanino-tech/rsanino-tech
IG_AGENT_GITHUB_ISSUE=9
IG_AGENT_POLL_SECONDS=20
IG_AGENT_WORKDIR=~/LovelysChoice/ig-agent
EOF

printf '\nIG AGENT BOOTSTRAP COMPLETE\n'
printf 'Workspace: %s\n' "$ROOT"
printf 'Bridge: %s\n' "$ROOT/ig_agent_bridge.py"
printf 'Control issue: rsanino-tech/rsanino-tech#9\n\n'
printf 'Starting bridge now...\n\n'

exec python3 "$ROOT/ig_agent_bridge.py"
