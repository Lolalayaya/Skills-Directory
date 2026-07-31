---
name: skill-authoring
description: "Create, edit, audit, or optimize Claude Code skills themselves — skill architecture, progressive disclosure, description/triggering quality, workflow design, token efficiency, and packaging. Use whenever the user wants to create a new skill, turn a workflow into a skill, improve or debug an existing skill's triggering or structure, run evals/benchmarks on a skill, or review a skill against best practices before shipping it."
---

# Skill Authoring

Router skill for building the tooling that builds skills — meta, but frequently needed once a workspace has more than a couple of custom skills (as this one now does).

## Domains

| Domain | When to use | Full guide |
|---|---|---|
| Skill creation & eval loop | Draft a new skill, run test-prompt evals with/without the skill, review results, iterate, optimize the description for triggering, package it | [references/skill-creator/SKILL.md](references/skill-creator/SKILL.md) |
| Skill forging (architecture-first) | Expert guidance on skill architecture, workflow design, and prompt engineering when building a production-grade skill from scratch | [references/skill-forge/SKILL.md](references/skill-forge/SKILL.md) |
| Skill quality review/audit | Analyze an existing skill's structure, description quality, workflow design, token efficiency, and anti-patterns against best practices | [references/skill-review/SKILL.md](references/skill-review/SKILL.md) |
| Writing/verifying skills | Create or edit skills and verify they actually work before calling them done | [references/writing-skills/SKILL.md](references/writing-skills/SKILL.md) |

## How to use this skill

1. **Starting from scratch**: `skill-forge` for architecture/design decisions, then `skill-creator` for the actual draft → eval → iterate loop.
2. **Improving an existing skill**: `skill-review` first to get a structured audit (token efficiency, trigger accuracy, anti-patterns), then feed the findings into `skill-creator`'s improvement loop.
3. **Before shipping any new/edited skill**: `writing-skills` for the "did I actually verify this works" discipline — don't skip straight to packaging.
4. These four domains overlap by design (they come from different source repos but cover the same lifecycle) — when guidance conflicts, prefer `skill-creator`'s process since it's the most detailed and includes the eval/benchmark tooling (`scripts/`, `eval-viewer/`) the others don't bundle.

## Standing principle (shared across all four)

Progressive disclosure: keep `SKILL.md` lean (name+description always loaded, body loaded on trigger, bundled `scripts/`/`references/`/`assets/` loaded only as needed). This very skill (and its 8 siblings created in this workspace) follows that pattern — use them as a live reference for the router-plus-references structure if unsure what "good" looks like.
