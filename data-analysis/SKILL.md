---
name: data-analysis
description: "Collect and analyze operational/performance data from deployed infrastructure to find what's actually worth optimizing, grounded in real metrics rather than repo-wide guessing. Currently covers Vercel project cost and performance analysis (Function Invocations, Build Minutes, Fast Data Transfer, Core Web Vitals, caching, Fluid compute). Use when the user wants to investigate why a deployed project is slow or expensive, wants a cost/performance breakdown, or asks for optimization recommendations that should be backed by observed metrics rather than a code-only guess. This category is intentionally thin right now — extend `references/` with a new domain (e.g. a SQL database connector, a Grafana/Datadog integration) as those skills get installed, following the same metrics-first, evidence-before-recommendation pattern as the Vercel domain below."
---

# Data & Analysis

Router skill for "connect to a data/metrics source, then figure out what's actually worth optimizing." The governing principle across every domain here: **recommendations start from observed signals, not from grep-scale guessing.** Read metrics first, gate which candidates deserve investigation, then investigate only those.

## Domains

| Domain | When to use | Full guide |
|---|---|---|
| Vercel cost & performance audit | Deployed Next.js/SvelteKit/Nuxt/Astro project — bill reduction, slow/expensive routes, caching opportunities, Core Web Vitals | [references/vercel-optimize/SKILL.md](references/vercel-optimize/SKILL.md) |

## How to use this skill

1. Open the matching domain guide and follow its collection → gate → investigate → verify → report pipeline exactly as written — these pipelines are script-driven (see that domain's `scripts/` and `lib/`) specifically so recommendations stay tied to verified evidence rather than hallucinated file references. Do not skip the "gate" step to save time; ungated investigation is exactly the repo-wide-grep failure mode these skills exist to prevent.
2. If the task involves a data source with no domain listed above (a SQL/Postgres database, Grafana, Datadog, a data warehouse), say so explicitly rather than forcing the Vercel pipeline onto it — this category doesn't have that connector yet. Recommend the user install or point to a skill for that source, then this router can be extended with a new `references/<source>/` entry the same way `vercel-optimize` was added.

## Cross-cutting gotchas

- **Metrics first, source code second.** Every domain here front-loads data collection before touching source files — resist the urge to read code speculatively before the metrics say where to look.
- **Never fabricate a metric you didn't actually query.** If a data source is unreachable or a permission/scope is unresolved, stop and ask rather than guessing a plausible-sounding number.
