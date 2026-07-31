---
name: openspec-workflow
description: "The OpenSpec change lifecycle — explore an idea before committing to it, propose a change with full specs/design/tasks generated in one step, implement tasks from an approved change, sync delta specs back to the main specs, and archive a completed change. Use whenever the user wants to think through a feature before writing a spec, quickly turn a description into a complete change proposal, implement or continue implementing tasks from an OpenSpec change, update main specs from a change without archiving, or finalize/archive a change after implementation is done."
---

# OpenSpec Workflow

Router skill for the OpenSpec experimental spec-driven workflow — a change moves through explore → propose → apply → sync → archive.

## Domains (in typical lifecycle order)

| Domain | When to use | Full guide |
|---|---|---|
| Explore | Thinking partner for exploring ideas, investigating problems, clarifying requirements before or during a change | [references/openspec-explore/SKILL.md](references/openspec-explore/SKILL.md) |
| Propose | Turn a description into a complete change proposal — specs, design, tasks — in one step | [references/openspec-propose/SKILL.md](references/openspec-propose/SKILL.md) |
| Apply | Implement tasks from an OpenSpec change — start, continue, or work through tasks | [references/openspec-apply-change/SKILL.md](references/openspec-apply-change/SKILL.md) |
| Sync specs | Update main specs with a change's delta specs without archiving | [references/openspec-sync-specs/SKILL.md](references/openspec-sync-specs/SKILL.md) |
| Archive | Finalize and archive a change after implementation is complete | [references/openspec-archive-change/SKILL.md](references/openspec-archive-change/SKILL.md) |

## How to use this skill

Follow the lifecycle in order for a new change: `explore` (optional, for fuzzy ideas) → `propose` → `apply` (repeatedly, as tasks get worked through) → `sync-specs` (if main specs need updating before archiving) → `archive` (once done).

Not every change needs every step — a well-understood change can skip straight to `propose`, and `sync-specs` is only needed when main specs must reflect the change before formal archiving.

## Relationship to `agentic-dev-workflow`

This is a specific, more formal alternative to the general `writing-plans` → `executing-plans` flow in `agentic-dev-workflow` — use OpenSpec when the project already uses the OpenSpec convention (delta specs, `openspec/changes/` directory structure); use the general workflow otherwise. Don't run both for the same change.
