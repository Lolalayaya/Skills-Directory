---
name: business-automation
description: "Persistent, file-based task planning and progress logging that survives context resets and /clear — keeps task_plan.md, findings.md, and progress.md on disk instead of relying on conversation memory. Also covers turning a recurring personal/business pattern into a workflow spec via interview. Use when the user wants to plan out, break down, or organize a multi-step project or research task, track progress across a long task, asks for planning/bookkeeping that should survive a session reset, or wants a recurring life/business pattern turned into a repeatable workflow spec."
---

# Business Automation

Router skill for standardized session/task bookkeeping — turning "keep track of where I am on this long task" into a repeatable file-based process instead of relying on conversation memory alone.

## Domains

| Domain | When to use | Full guide |
|---|---|---|
| Persistent file-based task planning | Long/multi-step tasks that need to survive `/clear` or context loss — keeps `task_plan.md`, `findings.md`, `progress.md` on disk | [references/planning-with-files/SKILL.md](references/planning-with-files/SKILL.md) |
| Recurring pattern → workflow spec | Grill the user about a repeated life/business pattern until it's a concrete, implementable workflow document | [references/loop-me/SKILL.md](references/loop-me/SKILL.md) |

## How to use this skill

Follow `planning-with-files`'s scripted bookkeeping flow (`init-session`, `ledger-append`, `ledger-summary`, `phase-status`, `check-complete`, etc.) rather than improvising an ad hoc set of markdown files — the scripts keep the format consistent across sessions so a fresh session (or a fresh `/clear`) can pick up exactly where the last one left off.

`loop-me` is a different job — not bookkeeping an in-progress task, but designing the spec for a pattern that recurs (a life/business workflow), via the same kind of relentless interview `agentic-dev-workflow`'s `grilling` uses.

Localized variants (Simplified/Traditional Chinese) live alongside the English version under `references/planning-with-files-<lang>/` if the session isn't in English. (Arabic/German/Spanish variants were removed 2026-07-31 as never-triggered for this workspace — see `SKILL-AUDIT.md`.)

## Note on scope

This category used to also cover cookie-sync, self-improving browser automation, and safety-constrained browsing agents, and isolated git-worktree setup — those moved to `browser-automation` and `agentic-dev-workflow` respectively, since they're each closer in kind to that company than to file-based task bookkeeping. This skill is intentionally narrow now: one domain, one job.
