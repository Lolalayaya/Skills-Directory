---
name: infrastructure-ops
description: "Interactive setup/migration wizard generation — walk a human through a one-time manual procedure (initial setup, a state transition, a third-party migration) step by step, opening URLs and capturing values as it goes. Use when the user wants an interactive guided script for a setup or migration procedure. Does NOT yet cover day-to-day infrastructure operations, server/database/queue administration, or destructive-action guardrails on running production systems — see 'Scope' below before assuming otherwise."
---

# Infrastructure Ops

Router skill for infrastructure-adjacent tooling. Currently holds one sub-skill (added 2026-07-31, from the third-party `mattpocock-skills` pack — MIT license, see [`THIRD-PARTY-LICENSES.md`](../THIRD-PARTY-LICENSES.md)); day-to-day ops coverage is still unfilled.

## Domains

| Domain | When to use | Full guide |
|---|---|---|
| Interactive setup wizard | Generate a bash wizard that walks a human through a one-time manual procedure — setup, migration, state transition — opening URLs, capturing values, writing `.env`/secrets | [references/wizard/SKILL.md](references/wizard/SKILL.md) |

## Scope

**Covered**: one-time, human-in-the-loop setup/migration procedures, scripted as an interactive wizard.

**Not covered yet**: routine maintenance, health checks, scheduled housekeeping on *running* infrastructure, or guardrails around destructive operations on production systems (deletes, force-pushes to production config, resource teardown, credential rotation). None of the skills audited in this workspace (originally 137, now 160+) covered that — the closest adjacent material (`vercel-optimize`) is cost/metrics analysis, not day-to-day ops, and lives under `data-analysis` instead.

Do not give day-to-day infrastructure-operations guidance from general knowledge under this skill's name — that gap is real, not filled by `wizard`. If the user asks for that kind of help, say so plainly and offer to help ad hoc rather than pretending this skill covers it. When a real ops-oriented skill (server/container/database administration, infra-as-code apply/destroy, on-call runbook automation) gets installed, add it under `references/<skill-name>/` the same way `wizard` was added, and expand this section.
