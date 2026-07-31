---
name: handoff
description: Compact the current conversation into a handoff document for another agent to pick up — launched as a background agent immediately if the CLI supports it, otherwise saved for the next session to read.
argument-hint: "What will the next session be used for?"
disable-model-invocation: true
---

Write a handoff summary of the current conversation so a fresh agent can continue the work.

Include a "suggested skills" section in the summary, which suggests skills that the agent should invoke.

Do not duplicate content already captured in other artifacts (specs, plans, ADRs, issues, commits, diffs). Reference them by path or URL instead.

Redact any sensitive information, such as API keys, passwords, or personally identifiable information — the summary may become the next agent's prompt directly.

If the user passed arguments, treat them as a description of what the next session will focus on and tailor the summary accordingly.

## Delivery: background agent if available, file handoff otherwise

**If the CLI supports launching a background agent** (e.g. Claude Code's `claude --bg`): launch one immediately, seeded with the summary as its prompt — `claude --bg --name "<descriptive name>" "<handoff summary>"`. It starts in the current working directory and returns immediately; the user manages it with `claude agents`. Always pass `-n`/`--name` with a descriptive name (e.g. `--name "Fix login bug"`) — it sets the display name shown in the job list, session picker, and terminal title. This is the faster path — no manual restart needed.

**Otherwise** (no background-agent capability, or the user just wants a document to hand to a different session/agent manually): save the summary to the temporary directory of the user's OS — not the current workspace — and tell the user the path.
