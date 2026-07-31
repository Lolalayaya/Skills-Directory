---
name: infrastructure-ops
description: "PLACEHOLDER — day-to-day infrastructure operations and maintenance (server management, database/queue administration, guardrails against destructive commands on production systems) with no installed skill content yet. Do not treat this as an authoritative source; it currently has no reference material. Fill in when an infra-ops-related skill is installed."
---

# Infrastructure Ops (placeholder)

No currently installed skill maps to this category. Of the 137 skills audited when this workspace was reorganized (2026-07-31), none covered routine infrastructure maintenance or destructive-operation guardrails — the closest adjacent material (`vercel-optimize`) is metrics/cost analysis, not day-to-day ops, and lives under `data-analysis` instead.

## Intended scope (for when content exists)

Based on the category definition this skill was reserved for:

- Day-to-day operational tasks: routine maintenance, health checks, scheduled housekeeping on running infrastructure.
- Guardrails around destructive operations (deletes, force-pushes to production config, resource teardown, credential rotation) — the point is reducing both engineer cognitive load and blast radius from mistakes, not blocking legitimate ops work.

## How to fill this in later

1. Install an ops-oriented skill (e.g. something covering server/container/database administration, infra-as-code apply/destroy workflows, or on-call runbook automation).
2. Copy it into `references/<skill-name>/` the same way the other consolidated skills in this workspace are structured (see `library-api-reference` or `business-automation` for the pattern).
3. Rewrite this file's frontmatter `description` and body into a real router pointing at `references/<skill-name>/SKILL.md`, following the same format as the other 8 consolidated skills.
4. Remove the "PLACEHOLDER" language once real content exists.

## Do not

Do not attempt to give infrastructure operations guidance from general knowledge under this skill's name while it's empty — that would fabricate authority this skill doesn't have yet. If the user asks for infra-ops help before this is filled in, say so plainly and offer to help ad hoc rather than pretending this skill covers it.
