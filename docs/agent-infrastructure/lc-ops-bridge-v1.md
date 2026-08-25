# LC OPS Bridge v1

## Purpose
Reusable local-agent command bridge pattern for Lovely's Choice and future AI-created agents.

## Verified architecture

ChatGPT / GitHub connector -> GitHub issue command channel -> local Python polling bridge -> Ollama qwen3:8b -> restricted application CLI (currently Signboard) -> local project data.

## Current verified implementation
- Local bridge script: `~/lc-ops-agent/lc_ops_agent.py`
- Local model: `qwen3:8b`
- GitHub account: `rsanino-tech`
- GitHub repository/control channel: `rsanino-tech/rsanino-tech`
- Existing LC OPS control issue: `#8`
- Polling interval: 20 seconds
- Signboard board path: `/Users/rafaelsaninocencio/Downloads/Lovely's Choice`
- Startup command: `python3 ~/lc-ops-agent/lc_ops_agent.py`
- GitHub CLI: authenticated locally through macOS keyring; HTTPS Git protocol

## Verified behavior
The bridge has successfully:
1. Read the Lovely's Choice Signboard board.
2. Created a card remotely.
3. Re-read the board and verified the card exists.
4. Moved cards between Signboard lists.
5. Rejected commands outside its allowed Signboard operation scope.

## Security design
- The existing LC OPS bridge is deliberately restricted to Signboard operations.
- Do NOT expand `lc_ops_agent.py` into an unrestricted shell executor.
- Do NOT store GitHub, Meta, Postiz, email, or other access tokens in this document or repository.
- Secrets belong in local protected environment/configuration storage and must be excluded from Git.
- New agents should receive their own restricted command surface and preferably their own GitHub control issue.

## Recovery / startup
1. Ensure Ollama is available locally and `qwen3:8b` is installed.
2. Confirm GitHub CLI authentication with `gh auth status`.
3. Confirm the target application/CLI is installed and accessible.
4. Start the bridge with `python3 ~/lc-ops-agent/lc_ops_agent.py`.
5. Confirm terminal output reports `LC OPS BRIDGE ONLINE` and shows the expected model, board, GitHub issue, and polling interval.
6. Send a harmless read-only `COMMAND:` through the control issue and verify a `RESULT:` response before permitting writes.

## IG Agent derivative
The IG Agent should reuse this proven command-channel pattern but run as a separate process/session. It should NOT modify or share the Signboard bridge's restricted execution logic.

Planned separation:
- LC OPS / Signboard: existing bridge + issue #8
- IG Agent: dedicated local workspace + dedicated bridge script + dedicated GitHub control issue
- Shared local inference provider: Ollama `qwen3:8b`
- IG Agent execution surface: allowlisted IG-Agent/Postiz/Meta/reporting operations only

## Compute policy for IG Agent
The IG Agent is intended to be event/schedule driven rather than continuously performing inference:
- Wake for scheduled post/audit windows.
- Publish or verify approved content.
- Return to idle/garage mode.
- Wake for a nightly social-intelligence shift.
- Collect Instagram comments, Threads replies, and engagement data.
- Use Ollama for theme classification/summarization only when needed.
- Produce and archive a nightly report, then email the report.
- Return to idle/garage mode.

Posting times and nightly shift time remain configurable and are intentionally not hard-coded yet.

## Documentation rule
Every future agent build must document architecture, paths, dependencies, allowed operations, startup/shutdown, testing, security, recovery, and major design decisions as the implementation is created. Chat history is not the system of record; version-controlled documentation is.

Last documented: 2026-08-24
