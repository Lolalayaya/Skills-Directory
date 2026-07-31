---
name: skills-directory
description: "Master index of every custom skill in this workspace (18 top-level skills, consolidated from 137 originally-installed ones). Consult this FIRST whenever unsure which skill covers a need, when a task might span more than one skill, or to sanity-check what capabilities exist here at all. Several entries are marked UNIVERSAL — standing triggers (start-of-conversation skill discovery, brainstorming before creative work, verification before claiming completion, TDD, code-security review) that should fire on essentially every relevant turn, not only when explicitly asked for."
---

# Skills Directory

One-stop map of this workspace's 18 skills. Each row's "Full skill" links straight to that skill's own `SKILL.md`, which then routes further into its `references/<domain>/SKILL.md`.

## 🔁 Universal — apply these without being asked

These sub-domains carry "always / before any / MUST" language in their own source material. Don't wait for the user to invoke them by name.

| Trigger point | Sub-domain | Lives in | Why it's universal |
|---|---|---|---|
| Start of any conversation | `using-superpowers` | `agentic-dev-workflow` | Establishes how to find/use the right skill before any response, including clarifying questions |
| Before any creative/feature work | `brainstorming` | `agentic-dev-workflow` | Explore intent and requirements before designing a solution — MUST use, not optional |
| Before implementing any feature/bugfix | `test-driven-development` | `product-verification` | Write the test that defines success before writing implementation code |
| Before claiming anything "fixed", "passing", or "complete" | `verification-before-completion` | `product-verification` | Evidence before assertions — run the verification command and read real output, every time |
| Writing/reviewing code touching input, auth, files, DB, network, crypto, or infra config | `code-security` | `code-quality-review` | Standing trigger even when the user doesn't say "security" |

## 📋 Quick lookup — "I need to..."

| ...do this | Go to |
|---|---|
| Browse/test/automate a website, sync login cookies, capture a debug trace, research a company/competitor/event | `browser-automation` |
| Prove a fix/feature actually works (Playwright), or apply the verification/TDD discipline | `product-verification` |
| Figure out why a deployed (Vercel) app is slow/expensive from real metrics | `data-analysis` |
| Keep a long task's plan/progress on disk across sessions and `/clear` | `business-automation` |
| Create/edit .docx/.xlsx/.pptx/.pdf, build an MCP server, write React/Next.js/React Native code | `library-api-reference` |
| Build a banner/logo/slide deck/theme, set up a design system, review UI or writing style, scaffold pages from templates | `scaffolding-templating` |
| Review code for quality/SOLID/security, run Semgrep, request or receive a code review | `code-quality-review` |
| Deploy to Vercel (interactive or CI/token-based) | `cicd-deployment` |
| Diagnose a bug/test failure systematically before proposing a fix | `incident-runbooks` |
| (day-to-day infra ops, destructive-action guardrails) | `infrastructure-ops` — **placeholder, no content yet** |
| Anything marketing: ads, SEO, copywriting, pricing, onboarding, churn, email/SMS, referrals, launches, positioning, attribution | `marketing` |
| Create/edit/audit a Claude Code skill itself | `skill-authoring` |
| Study a book, build a personal knowledge base, get Socratic tutoring on a topic | `personal-learning` |
| Brainstorm → plan → isolate a workspace → execute → decide how to merge/integrate a branch | `agentic-dev-workflow` |
| Run the OpenSpec explore/propose/apply/sync/archive change flow | `openspec-workflow` |
| Run a generic outline-driven topic research pipeline (Chinese) | `deep-research` |
| Co-author a doc/proposal/spec, or write internal company comms | `internal-writing-comms` |
| Design/optimize/debug an agent system's context management, harness, or multi-agent architecture | `context-engineering-collection` |

## Full skill list

| # | Skill | One-line summary | Sub-domains inside |
|---|---|---|---|
| 1 | `browser-automation` | Browserbase toolkit: drive/test/automate a browser, plus B2B research/prospecting | 15 — see comment block below |
| 2 | `product-verification` | Prove work actually works before claiming done | 3 |
| 3 | `data-analysis` | Metrics-driven optimization (Vercel only, for now) | 1 |
| 4 | `business-automation` | Persistent file-based task planning across sessions | 1 (+2 language variants) |
| 5 | `library-api-reference` | Office file formats, MCP building, Vercel/React APIs | 9 |
| 6 | `scaffolding-templating` | Templates/scaffolds — general + full design system | 16 |
| 7 | `code-quality-review` | Code review, static analysis, secure coding | 6 |
| 8 | `cicd-deployment` | Deploy to Vercel, interactive or CI | 2 |
| 9 | `incident-runbooks` | Systematic debugging + diagnostic write-ups | 1 |
| 10 | `infrastructure-ops` | *(empty placeholder — no installed content)* | 0 |
| 11 | `marketing` | Full-funnel marketing, 5 internal sub-groups | 47 |
| 12 | `skill-authoring` | Build/audit/optimize skills themselves | 4 |
| 13 | `personal-learning` | Book study, knowledge base, Socratic tutor | 3 |
| 14 | `agentic-dev-workflow` | Brainstorm → plan → isolate → execute → finish branch | 8 |
| 15 | `openspec-workflow` | OpenSpec change lifecycle | 5 |
| 16 | `deep-research` | Generic outline-driven research pipeline (Chinese) | 5 |
| 17 | `internal-writing-comms` | Doc co-authoring + internal comms formats | 2 |
| 18 | `context-engineering-collection` | Context/harness engineering, multi-agent systems (untouched, never split) | 16 |

Total: 130 consolidated sub-domains + `context-engineering-collection`'s own 16 (never touched by the consolidation) + the `infrastructure-ops` placeholder = everything originally installed, minus 7 removed after the 2026-07-31 health check (see `SKILL-AUDIT.md`): `browser-use-to-stagehand`, `safe-browser`, `slack-gif-creator`, `planning-with-files-ar`/`-de`/`-es`, `latent-briefing`.

## How to use this index

1. Scan the quick-lookup table first — most tasks match one row directly.
2. If a task spans more than one skill (common for anything shipping code: `agentic-dev-workflow` → `product-verification` → `code-quality-review` → `cicd-deployment`), open each in that order rather than picking just one.
3. If nothing matches, the task may not be covered yet — say so rather than forcing a mismatched skill onto it.
4. When a new skill gets installed later, add it as its own row here (or fold it into an existing skill's `references/` the same way these 136 were folded in) rather than leaving this index stale.

<!--
=======================================================================
CONSOLIDATED-SKILL AUDIT TRAIL — full list of the (originally 136, now
130 after the 2026-07-31 removals below) installed skills folded into
the 18 skills above, grouped by which current skill now holds them
under its references/ tree.
This history exists so a future session never reinstalls one of these
under its old name without realizing it already exists here — that
includes the 7 REMOVALS listed at the bottom: they were deleted on
purpose, not lost.
=======================================================================

browser-automation (15, was 17 — see REMOVALS below):
  agent-experience, autobrowse, browser, browser-to-api, browser-trace,
  company-research, competitor-analysis, competitor-profiling,
  cookie-sync, event-prospecting, fetch, functions, search, ui-test,
  webmcp-gen

product-verification (3):
  webapp-testing, verification-before-completion, test-driven-development

data-analysis (1):
  vercel-optimize

business-automation (3, was 6 — see REMOVALS below):
  planning-with-files, planning-with-files-zh, planning-with-files-zht

library-api-reference (9):
  docx, xlsx, pptx, pdf, mcp-builder, vercel-react-best-practices,
  vercel-react-native-skills, vercel-react-view-transitions,
  vercel-composition-patterns

scaffolding-templating (16, was 17 — see REMOVALS below):
  programmatic-seo, design, design-system, ui-styling, ui-ux-pro-max,
  banner-design, brand, anthropic-brand-guidelines (renamed from
  brand-guidelines), canvas-design, algorithmic-art, theme-factory,
  frontend-design, web-artifacts-builder, web-design-guidelines,
  writing-guidelines, slides

code-quality-review (6):
  code-review-expert, semgrep, code-security, llm-security,
  requesting-code-review, receiving-code-review

cicd-deployment (2):
  deploy-to-vercel, vercel-cli-with-tokens

incident-runbooks (1):
  systematic-debugging

infrastructure-ops (0):
  (none — placeholder, nothing to list)

agentic-dev-workflow (8):
  brainstorming, dispatching-parallel-agents, executing-plans,
  subagent-driven-development, using-superpowers, writing-plans,
  using-git-worktrees, finishing-a-development-branch

openspec-workflow (5):
  openspec-apply-change, openspec-archive-change, openspec-explore,
  openspec-propose, openspec-sync-specs

deep-research (5):
  research, research-add-fields, research-add-items, research-deep,
  research-report

internal-writing-comms (2):
  doc-coauthoring, internal-comms

marketing (47):
  paid-acquisition: ads, ad-creative, aso, ai-seo, directory-submissions
  content-seo: seo-audit, content-strategy, copywriting, copy-editing,
    schema, site-architecture, social, video, image
  conversion-lifecycle: cro, signup, onboarding, paywalls, popups,
    pricing, churn-prevention, offers, emails, sms, cold-email
  growth-partnerships: referrals, co-marketing, influencer-marketing,
    community-marketing, marketing-loops, launch, free-tools, lead-magnets
  research-strategy: customer-research, marketing-plan,
    marketing-psychology, marketing-ideas, marketing-council, attribution,
    analytics, ab-testing, product-marketing, prospecting,
    public-relations, revops, sales-enablement, competitors
  (competitor-profiling originally landed here too, then moved to
   browser-automation once the naming/overlap issue with competitor
   research was worked out — see browser-automation's list above)

skill-authoring (4):
  skill-creator, skill-forge, skill-review, writing-skills

personal-learning (3):
  book-study, wiki-ingest, sigma

-----------------------------------------------------------------------
Total accounted for: 15+3+1+3+9+16+6+2+1+0+8+5+5+2+47+4+3 = 130
Plus context-engineering-collection: kept independent, never split
  (originally installed as one skill covering 17 internal sub-skills,
  now 16 after the REMOVALS below; re-wrapping it would have added no
  value).
Plus infrastructure-ops: placeholder, 0 sources (no installed skill
  matched this category as of 2026-07-31; kept as a deliberate empty
  reservation, not removed).
130 + 1 (context-engineering-collection, counted as a single original
install) = 131 currently-installed skill units, down from the original
137 after the REMOVALS below.

REMOVALS (2026-07-31 health check, see SKILL-AUDIT.md for the full
methodology and reasoning) — these 7 were deleted as low/never-triggered
and are NOT missing installs, do not reinstall them without a new reason:
  - browser-automation/browser-use-to-stagehand — one-time Python→TS
    migration tool, used once then never triggered again
  - browser-automation/safe-browser — hardcoded Hacker-News demo
    scaffold, low reusability as a generic skill
  - scaffolding-templating/slack-gif-creator — narrow, low-frequency use
  - business-automation/planning-with-files-ar, -de, -es — identical
    logic to the English version, only useful if conversing in that
    language; kept -zh and -zht since Chinese is actually used here
  - context-engineering-collection/latent-briefing — requires direct
    KV-cache access the user does not have; the skill's own text called
    itself "a research idea, not deployable technology"
Kept despite being flagged as narrow-use in the same health check:
  anthropic-brand-guidelines (kept as a UI-styling reference when
  producing websites) and bdi-mental-states (kept on hold, no removal
  reason given).
=======================================================================
-->
