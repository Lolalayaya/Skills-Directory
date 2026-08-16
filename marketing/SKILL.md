---
name: marketing
description: "Full-funnel marketing playbook covering paid acquisition & ASO/AI-SEO, content & SEO, conversion & lifecycle (CRO, onboarding, paywalls, pricing, churn, email/SMS), growth & partnerships (referrals, co-marketing, influencer, community, launches), and research & strategy (customer research, positioning, attribution, sales enablement, competitor analysis). Use whenever the user asks about ads, SEO, copywriting, conversion rate, pricing, onboarding, churn, email/SMS campaigns, referrals, influencer or community marketing, product launches, marketing plans/strategy, attribution, analytics, A/B testing, sales collateral, or competitor positioning — even if they only describe the business problem without naming a marketing discipline."
---

# Marketing

Router skill for the full marketing function. Organized into 5 sub-domains under `references/` — a task usually touches one, but growth/launch work often spans several.

## Sub-domains

| Sub-domain | Covers | Path |
|---|---|---|
| Paid acquisition | Ads (Google/Meta/LinkedIn/X), ad creative at scale, ASO, AI-search optimization (AEO/GEO), directory submissions | `references/paid-acquisition/` |
| Content & SEO | SEO audits, content strategy, copywriting/copy-editing, schema markup, site architecture, social content, video, image assets | `references/content-seo/` |
| Conversion & lifecycle | CRO, signup/onboarding flows, paywalls, popups, pricing/packaging, churn prevention, offers, email/SMS/cold-email sequences | `references/conversion-lifecycle/` |
| Growth & partnerships | Referrals/affiliates, co-marketing, influencer/creator partnerships, community-led growth, marketing loops, launches, free tools, lead magnets | `references/growth-partnerships/` |
| Research & strategy | Customer research, marketing plans, psychology/mental models, brainstorming (marketing-council, marketing-ideas), attribution, analytics, A/B testing, product marketing/positioning, prospecting, PR, RevOps, sales enablement, competitor comparison pages, a stage-gated grassroots/underdog campaign workflow (insurgent-campaign) | `references/research-strategy/` |

Each leaf domain (e.g. `references/content-seo/copywriting/`) is a full original skill with its own `SKILL.md` and any bundled scripts/templates — open the specific one that matches the task rather than reading the whole sub-domain.

Note: competitor *research* (profiling from URLs, or auto-discovered competitive intelligence) moved to `browser-automation` since it shares that tool family — this skill's `competitors` domain covers only the SEO/sales-enablement comparison *page* (the deliverable, not the research behind it).

## How to use this skill

1. Identify the sub-domain, then the specific leaf skill inside it (the table above names the leaf skills so you can jump straight there).
2. Cross-references between marketing skills are common and intentional — e.g. `cro` explicitly defers to `signup`/`onboarding`/`popups` for their specific flows, `copywriting` defers to `copy-editing` for polishing existing text, `attribution` defers to `analytics` for tracking setup. Follow those pointers inside each leaf `SKILL.md` rather than re-deriving the boundary yourself.
3. For a from-scratch strategy question ("what should our marketing look like"), start in `research-strategy` (`marketing-plan`, `marketing-council`, `product-marketing`) before jumping to execution sub-domains.

## `insurgent-campaign` vs. `attribution`

Imported 2026-08-16 (whole skill, MIT, bencium.io — see [`THIRD-PARTY-LICENSES.md`](../THIRD-PARTY-LICENSES.md)) as `references/research-strategy/insurgent-campaign/SKILL.md`. Both this skill and the existing `attribution` domain share the same incrementality/lift-testing research base (Lewis & Rao 2015 QJE on the wide confidence intervals of digital-ad ROI, the "platform-reported ROAS isn't causal lift" argument) — but they answer different questions. `attribution` is a measurement-methodology skill: how to set up and interpret lift tests, MMM, or multi-touch models for a spend mix you've already decided on. `insurgent-campaign` is a full stage-gated *strategy* workflow for organizations being outspent — campaign ideation across archetypes, a spend-asymmetry audit, a message-market-fit gate that can refuse to proceed, a 70/30 organic/paid channel-tier stack, and only *then* a lift-test plan (reusing the same measurement logic `attribution` documents in more depth). Reach for `attribution` when the question is "how do I measure whether this spend actually worked"; reach for `insurgent-campaign` when the question is "what should an outspent challenger's whole campaign look like" — the two compose rather than duplicate, and `insurgent-campaign`'s own Stage 5b measurement step is intentionally lighter-weight than `attribution`'s full treatment.

## Note on scope

`programmatic-seo` and general design/visual-asset generation are handled elsewhere: programmatic SEO page templates live under the `scaffolding-templating` skill (general scaffolding), and pure visual/brand design lives under `scaffolding-templating`'s design sub-tree — this skill covers the marketing *strategy and copy* layer, not page scaffolding or visual production.
