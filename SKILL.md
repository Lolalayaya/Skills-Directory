---
name: skills-directory
description: "Master index of every custom skill in this workspace (18 top-level skills, holding 230 sub-domains, consolidated/curated from 137 originally-installed skills plus several later third-party imports). Consult this FIRST whenever unsure which skill covers a need, when a task might span more than one skill, or to sanity-check what capabilities exist here at all. Several entries are marked UNIVERSAL — standing triggers (start-of-conversation skill discovery, brainstorming before creative work, verification before claiming completion, TDD, code-security review) that should fire on essentially every relevant turn, not only when explicitly asked for."
---

# Skills Directory

One-stop map of this workspace's 18 skills. Each row's "Full skill" links straight to that skill's own `SKILL.md`, which then routes further into its `references/<domain>/SKILL.md`.

## 🔁 Universal — apply these without being asked

These sub-domains carry "always / before any / MUST" language in their own source material. Don't wait for the user to invoke them by name. (A 2026-07-31 audit of a newly-imported third-party pack, `mattpocock-skills`, checked all 30 of its sub-domains for this same language and found none — see `SKILL-AUDIT.md`. This list is unchanged by that import. A 2026-08-02 import, `ip-guard`, reads as broader "invoke before any code/content generation" language than any entry below, but was explicitly kept OUT of this table per the user's own scoping decision — see `SKILL-AUDIT.md` for the full reasoning. A 2026-08-16 import, `ui-typography` (in `scaffolding-templating`), reads similarly broad — "auto-apply... silently... whenever generating UI output" — and was likewise kept OUT of this table by default, per the same precedent; see `SKILL-AUDIT.md`.)

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
| Browse/test/automate a website, sync login cookies, capture a debug trace, research a company/competitor/event, run a real-time/vertical-domain search query, or do one-off web scrape/crawl/monitor/parse via the Firecrawl CLI | `browser-automation` |
| Prove a fix/feature actually works (Playwright), apply the verification/TDD discipline, or ban truncated/placeholder output | `product-verification` |
| Figure out why a deployed (Vercel) app is slow/expensive from real metrics | `data-analysis` |
| Keep a long task's plan/progress on disk across sessions and `/clear`, or turn a recurring pattern into a workflow spec | `business-automation` |
| Create/edit .docx/.xlsx/.pptx/.pdf, build an MCP server, write React/Next.js/React Native code, wire Firecrawl into product code, or fetch/convert an arXiv paper to Markdown | `library-api-reference` |
| Build a banner/logo/slide deck/theme, set up a design system, review UI or writing style, scaffold pages from templates, make a frontend build stop looking like generic AI output, build/review/audit an interface animation, name a motion effect, pick a UI library, compare UI variants live, audit/scan/fix WCAG accessibility, enforce UI typography rules, design an agentic/relationship-centric UX, generate an infographic, or author a `DESIGN.md` token spec | `scaffolding-templating` |
| Review code for quality/SOLID/security (two frameworks available), run Semgrep, request/receive a code review, scan for deep-module opportunities, set up quality-gate hooks, check IP/license compliance and dependency security before shipping generated code/content | `code-quality-review` |
| Deploy to Vercel (interactive or CI/token-based) | `cicd-deployment` |
| Diagnose a bug/test failure systematically before proposing a fix, or triage incoming bug reports into agent-ready issues | `incident-runbooks` |
| Generate an interactive setup/migration wizard (day-to-day ops guardrails still unfilled) | `infrastructure-ops` |
| Anything marketing: ads, SEO, copywriting, pricing, onboarding, churn, email/SMS, referrals, launches, positioning, attribution | `marketing` |
| Create/edit/audit a Claude Code skill itself | `skill-authoring` |
| Study a book, build a personal knowledge base, get Socratic tutoring on a topic, or build a multi-session course workspace | `personal-learning` |
| Brainstorm → plan → isolate a workspace → execute → decide how to merge/integrate a branch; or interview-driven planning, formal spec/tickets, merge-conflict resolution, session handoff | `agentic-dev-workflow` |
| Run the OpenSpec explore/propose/apply/sync/archive change flow | `openspec-workflow` |
| Run a generic outline-driven topic research pipeline (Chinese), or a single-question background lookup | `deep-research` |
| Co-author a doc/proposal/spec, write internal company comms, draft/edit an article from raw material, delegate unanswerable questions as a questionnaire, revise an academic paper, or remove AI-writing tells from a draft | `internal-writing-comms` |
| Design/optimize/debug an agent system's context management, harness, or multi-agent architecture | `context-engineering-collection` |

## Full skill list

| # | Skill | One-line summary | Sub-domains inside |
|---|---|---|---|
| 1 | `browser-automation` | Browserbase toolkit: drive/test/automate a browser, plus B2B research/prospecting, a third-party unified search API, and the third-party Firecrawl CLI | 28 — see comment block below |
| 2 | `product-verification` | Prove work actually works before claiming done, plus full-output enforcement | 4 |
| 3 | `data-analysis` | Metrics-driven optimization (Vercel only, for now) | 1 |
| 4 | `business-automation` | Persistent file-based task planning across sessions, plus workflow-spec design | 5 (1 core +2 language variants +2 from third-party imports) |
| 5 | `library-api-reference` | Office file formats, MCP building, Vercel/React APIs, React Aria headless components/hooks, Firecrawl SDK integration, arXiv paper tooling | 17 |
| 6 | `scaffolding-templating` | Templates/scaffolds — general + full design system + anti-AI-slop frontend taste systems + animation/motion engineering + WCAG accessibility pipeline + typography/agentic-UX + design reference catalogs/spec generators + p5.js generative art/export pipeline + disposable UI sketch variants + shadcn/ui's own official skill/migration engine + two animated component galleries (Magic UI, react-bits) | 54 |
| 7 | `code-quality-review` | Code review (two frameworks), static analysis, secure coding, IP/license + dependency-security guardrails, architecture scanning | 14 — see comment block below |
| 8 | `cicd-deployment` | Deploy to Vercel, interactive or CI | 2 |
| 9 | `incident-runbooks` | Systematic debugging + diagnostic write-ups + issue triage | 4 |
| 10 | `infrastructure-ops` | Interactive setup/migration wizard (day-to-day ops still unfilled) | 1 |
| 11 | `marketing` | Full-funnel marketing, 5 internal sub-groups | 48 |
| 12 | `skill-authoring` | Build/audit/optimize skills themselves | 5 |
| 13 | `personal-learning` | Book study, knowledge base, Socratic tutor, multi-session course workspace | 4 |
| 14 | `agentic-dev-workflow` | Brainstorm → plan → isolate → execute → finish branch, plus interview-driven planning, git/session mechanics, and condensed coding-discipline/architectural-loyalty references | 25 — see comment block below |
| 15 | `openspec-workflow` | OpenSpec change lifecycle | 5 |
| 16 | `deep-research` | Generic outline-driven research pipeline (Chinese), plus single-question background lookup | 6 |
| 17 | `internal-writing-comms` | Doc co-authoring, internal comms formats, article drafting/editing, questionnaires, research-paper writing, AI-tell removal | 7 |
| 18 | `context-engineering-collection` | Context/harness engineering, multi-agent systems (untouched, never split) | 16 |

Total: 230 sub-domains across the 17 non-`context-engineering-collection` skills + `context-engineering-collection`'s own 16 (never touched by the consolidation) = 246 sub-skill-level `SKILL.md` files. History: 137 originally installed → −7 removed at the 2026-07-31 health check → 130 → +30 from importing and distributing the third-party `mattpocock-skills` pack the same day (MIT license, Matt Pocock — see [`THIRD-PARTY-LICENSES.md`](THIRD-PARTY-LICENSES.md)) → 160 → +1 from importing forrestchang's third-party `andrej-karpathy-skills` pack on 2026-08-01 (single skill, `karpathy-guidelines`, folded into `agentic-dev-workflow` — see [`THIRD-PARTY-LICENSES.md`](THIRD-PARTY-LICENSES.md)) → 161 → +4 from importing 4 of the 5 skills in Shubham Saboo's third-party `awesome-llm-apps` repo's `agent_skills/` folder on 2026-08-01 (Apache-2.0 license — see [`THIRD-PARTY-LICENSES.md`](THIRD-PARTY-LICENSES.md)): `commit-archaeologist` → `incident-runbooks`, `project-graveyard` → `business-automation`, `scope-creep-detector` → `code-quality-review`, `thinking-out-loud` → `agentic-dev-workflow` (the 5th, `advisor-orchestrator-worker`, was excluded as redundant with this environment's native `Workflow` tool) → 165 → +1 from importing Mugdha Vairagade's third-party `claude-skill-ip-guard` on 2026-08-02 (Apache-2.0 license, single skill `ip-guard`, folded into `code-quality-review` — see [`THIRD-PARTY-LICENSES.md`](THIRD-PARTY-LICENSES.md)) → 166 → +12 from importing Leonxlnx's third-party `taste-skill` pack on 2026-08-05 (MIT license, 12 sub-skills, 11 folded into `scaffolding-templating` and 1 — `output-skill` — folded into `product-verification` since it isn't a design skill — see [`THIRD-PARTY-LICENSES.md`](THIRD-PARTY-LICENSES.md)) → 178 → +1 from importing Nutlope's third-party `hallmark` on 2026-08-05 (MIT license, single skill, folded into `scaffolding-templating` — see [`THIRD-PARTY-LICENSES.md`](THIRD-PARTY-LICENSES.md)) → 179 → +1 from importing the AnySearch Team's third-party `anysearch-skill` on 2026-08-07 (Apache-2.0 license, single skill `anysearch`, folded into `browser-automation` — see [`THIRD-PARTY-LICENSES.md`](THIRD-PARTY-LICENSES.md)) → 180 → +9 from importing Emil Kowalski's third-party `emilkowalski/skills` pack on 2026-08-09 (MIT license, 9 sub-skills — animation/motion engineering + 2 UI-decision tools — folded into `scaffolding-templating`, one renamed to avoid a name collision — see [`THIRD-PARTY-LICENSES.md`](THIRD-PARTY-LICENSES.md)) → 189 → +17 from importing Firecrawl's own official `firecrawl/cli` + `firecrawl/skills` repos on 2026-08-16 (ISC license — see [`THIRD-PARTY-LICENSES.md`](THIRD-PARTY-LICENSES.md)): 5 app-integration skills → `library-api-reference`, 12 live-web-tool + search-index skills → `browser-automation` → 206 → +2 from importing ultimatile's third-party `arxiv-skills` the same day (MIT license, `arxiv-lookup` + `arxiv-doc-builder`, folded into `library-api-reference` — see [`THIRD-PARTY-LICENSES.md`](THIRD-PARTY-LICENSES.md)) → 208 → +1 from importing Master-cai's third-party `research-paper-writing` the same day (MIT license, folded into `internal-writing-comms` — see [`THIRD-PARTY-LICENSES.md`](THIRD-PARTY-LICENSES.md)) → 209 → +1 from importing kevintsai1202's third-party `Humanizer-zh-TW` the same day (MIT license, folded into `internal-writing-comms` — see [`THIRD-PARTY-LICENSES.md`](THIRD-PARTY-LICENSES.md)) → 210. A 5th source offered the same day, `guillaumemeyer/watermarks-remover`, was **declined** — not imported, see the note at the end of the audit trail below and `SKILL-AUDIT.md` for the full reasoning. → +10 from importing four more sources on 2026-08-16 (evaluated via user-directed comparison against installed skills, not a raw repo import — see `SKILL-AUDIT.md`): AccessLint (5, MIT) → `scaffolding-templating`, bencium.io typography+relationship-design (2, MIT) → `scaffolding-templating`, NousResearch/hermes-agent popular-web-designs+design-md+baoyu-infographic (3, MIT) → `scaffolding-templating` → 220 → +4 from a user-directed set of 9 precision extractions/whole-skill-installs the same day, spanning `bencium-marketplace` and `hermes-agent` (see `SKILL-AUDIT.md`'s "2026-08-16（三）" section): 2 whole-skill installs (`p5js`, `sketch`, both MIT, hermes-agent) → `scaffolding-templating`, 1 whole-skill install (`insurgent-campaign`, MIT, bencium.io) → `marketing`, 1 new standing-reference file (`loyalty-mindset`, extracted from bencium.io's `human-architect-mindset`) → `agentic-dev-workflow`; the remaining 5 items in that batch were surgical fragment-extractions folded into already-existing files (`frontend-design`, `redesign-skill`, `taste-skill`, `hallmark`'s `audit` verb, `ai-seo`) and correctly add **no** new sub-domain `SKILL.md` files → 224 → +1 correction found during this same batch's verification pass: a direct file-count of `scaffolding-templating/references/design/` + `references/general/` turned up 50 sub-domain `SKILL.md` files after adding `p5js`/`sketch`, not 49 — meaning the *prior* session's stated baseline of 47 (before this batch) was itself off by one (should have been 48). Not traced further back through every earlier delta (out of this batch's scope); corrected forward from here. → 225 → +5 from a user-directed deep integration of four external UI references the same day (evaluated via discussion before any file was written, not a raw repo import — see `SKILL-AUDIT.md`'s "2026-08-16（四）" section): shadcn/ui's own official repo ([github.com/shadcn-ui/ui](https://github.com/shadcn-ui/ui), MIT) contributed 2 skills vendored byte-for-byte (`shadcn-official`, `migrate-radix-to-base`) → `scaffolding-templating`; Magic UI Design's own official repo ([github.com/magicuidesign/magicui](https://github.com/magicuidesign/magicui), MIT) contributed 1 skill (`magicui`) → `scaffolding-templating`, its official CLI-workflow skill vendored verbatim plus a new supplementary reference authored for this repo embedding real source for 20 representative components; Adobe's `react-spectrum` monorepo ([github.com/adobe/react-spectrum](https://github.com/adobe/react-spectrum), Apache-2.0) contributed 1 skill (`react-aria`) → `library-api-reference`, authored directly from the repo's own package READMEs/`AGENTS.md`/official Tailwind starter kit source (not vendored wholesale, and not from the live docs site, which was unreachable from this environment); DavidHDev's `react-bits` ([github.com/DavidHDev/react-bits](https://github.com/DavidHDev/react-bits), **MIT + Commons Clause** — a non-standard license clause forbidding redistribution of the components themselves) contributed 1 skill (`react-bits`) → `scaffolding-templating`, deliberately containing zero embedded component source (catalog/comparison content only) because of that clause — the first time a license restriction, rather than content overlap or scope mismatch, has driven this repo to deliberately narrow a skill's content depth → 230. Full reasoning for every addition/removal/merge: `SKILL-AUDIT.md`.

## How to use this index

0. For a human searching by keyword rather than scanning tables, open [`skills-search.html`](skills-search.html) — a static, self-contained HTML page mirroring every row of `TRIGGER-MAP.md` with instant keyword filtering. It's a snapshot, not a live view (see the maintenance note in the standard procedure below, step 15).
1. Scan the quick-lookup table first — most tasks match one row directly.
2. If a task spans more than one skill (common for anything shipping code: `agentic-dev-workflow` → `product-verification` → `code-quality-review` → `cicd-deployment`), open each in that order rather than picking just one.
3. If nothing matches, the task may not be covered yet — say so rather than forcing a mismatched skill onto it.
4. When a new skill gets installed later, follow the standard procedure below rather than just dropping it in and leaving this index stale.

## Standard procedure for adding a new skill (or a whole new skill pack)

Established 2026-07-31 after importing and distributing `mattpocock-skills` (see `SKILL-AUDIT.md` for the full worked example this procedure is extracted from). Follow every phase in order — skipping ahead to "just add the files" is exactly how this index goes stale.

### Phase A — Assess

1. **Check for overlap or conflict with existing skills.** Do not judge this from `description` text alone — three separate misjudgments happened in one session from doing exactly that. Read the new skill's full `SKILL.md` and any bundled `scripts/`/`references/`/`agents/` in full, and read the same for whatever existing skill it superficially resembles, before concluding anything.

### Phase B — Decide placement and classification

2. **Fold it into one of the existing top-level skills**, chosen by theme/subject matter, not by source repo. If genuinely nothing fits, propose a new top-level category to the user for discussion — do not unilaterally create one. (A new 19th top-level skill was created and then explicitly reversed in this repo's own history; folding into the existing 18 is the default outcome, a new category is the exception that needs sign-off.)
3. **Apply the five-category classification** to the new material (and to whichever existing skill it's being compared against, if relevant): 核心常用 (core, used constantly) / 偶爾需要 (occasional, context-specific) / 功能重疊 (overlapping with something existing) / 不確定用途 (unclear when it'd trigger) / 可能可以刪 (candidate for removal — downloaded but unused, or fully superseded).
4. **Default to NOT physically merging on "functional overlap."** Clarify both sides' `description` with explicit cross-references first ("if X, see Y instead"). Only physically merge when full-content reading confirms it's a *true* duplicate (same core logic, no independently-useful bundled tooling on either side) AND the user has explicitly asked for the content to be integrated rather than just disambiguated.

### Phase C — Execute the move/integration

5. **Check for name collisions before moving anything** — both the destination folder name and the `SKILL.md` frontmatter `name:` field, against every existing skill in the repo (a full-repo `name:` dedup grep is cheap, do it). Moving a folder into a destination that already has one of that name does not error and does not overwrite — it nests the source one level deeper inside the existing folder, silently. Rename to something distinct (folder AND frontmatter `name:`, both) if a collision is found.
6. **Verify internal cross-references still resolve** if the incoming pack's own files reference each other by name or relative path — after any move/rename/merge, re-check every such reference (a source-repo's own router/README files are the most likely place these break).
7. **Remove the source pack's own category-level index files** (per-folder README.md, plugin manifests, etc.) once its content has been distributed/merged in — they go stale immediately and create a second index that drifts from reality. This repo's own per-skill `SKILL.md` files are the only index going forward.
8. **Handle attribution.** Third party content kept in one dedicated folder: its own `LICENSE` file is enough. Third-party content distributed across multiple existing top-level skills: create or update a root-level `THIRD-PARTY-LICENSES.md` listing the full license text plus which files/folders came from it, and update `README.md`'s copyright section to point at it.
9. **Check universal-tier eligibility.** Grep the incoming material for `MUST use` / `before any` / `ALWAYS use` language. Distinguish a skill's own internal step-level instructions (not universal) from an actual "invoke this before any response" claim (would be universal) before adding anything to the 🔁 Universal table above — most matches turn out to be the former.

### Phase D — Update documentation

10. **Update every affected top-level skill's own `SKILL.md`**: new Domains-table row(s), an updated `description` if the skill's scope grew, and a note on how the new sub-domain relates to its new siblings.
11. **Update `README.md`**: the affected top-level skill's own section (new bullet(s), updated sub-skill count, a note if the addition is third-party), and the copyright section if attribution changed.
12. **Update this file (`SKILL.md`)**: the Quick-lookup table, the Full skill list's sub-domain counts, and the audit-trail comment block at the bottom (add a new dated entry rather than editing history away).
13. **Update `SKILL-AUDIT.md`**: record the classification results, the placement decision and why, and any collisions/fixes from Phase C — this is what lets a future session judge "was this already considered?" instead of re-litigating it.
14. **Update `TRIGGER-MAP.md`**: fold trigger examples for the new sub-domain(s) into the relevant existing category section (not a new standalone section, per Phase B point 2).
15. **Regenerate `skills-search.html`**: this is a static, self-contained searchable HTML index of every row in `TRIGGER-MAP.md` (built 2026-08-02, see the note below the table) — it is a local file, not a published Artifact, and has no way to read `TRIGGER-MAP.md` at runtime. After step 14 changes that file, add/update the matching entries in `skills-search.html`'s inline `DATA` array by hand so the two never drift apart. Skipping this step is exactly how the search page goes stale.

<!--
=======================================================================
CONSOLIDATED-SKILL AUDIT TRAIL — full list of the (originally 136, now
130 after the 2026-07-31 removals, now 160 after the same-day third-party
import below) installed skills folded into the 18 skills above, grouped
by which current skill now holds them under its references/ tree.
This history exists so a future session never reinstalls one of these
under its old name without realizing it already exists here — that
includes the REMOVALS/MERGES listed below: they were deleted/folded on
purpose, not lost.
=======================================================================

browser-automation (28, was 17 — see REMOVALS below, +1 from the
  anysearch-skill import, +12 from the firecrawl/cli + firecrawl/skills
  import):
  agent-experience, autobrowse, browser, browser-to-api, browser-trace,
  company-research, competitor-analysis, competitor-profiling,
  cookie-sync, event-prospecting, fetch, functions, search, ui-test,
  webmcp-gen, anysearch, firecrawl-cli, firecrawl-agent, firecrawl-crawl,
  firecrawl-download, firecrawl-interact, firecrawl-map,
  firecrawl-monitor, firecrawl-parse, firecrawl-scrape, firecrawl-search,
  firecrawl-developer-index, firecrawl-research-index

product-verification (4, was 3, +1 from the taste-skill import):
  webapp-testing, verification-before-completion, test-driven-development
  (test-driven-development absorbed mattpocock-skills' tdd — see
  THIRD-PARTY IMPORT below), output-skill

data-analysis (1):
  vercel-optimize

business-automation (5, was 3 after the 2026-07-31 removals, +1 from the
  mattpocock-skills import, +1 from the awesome-llm-apps import):
  planning-with-files, planning-with-files-zh, planning-with-files-zht,
  loop-me, project-graveyard

library-api-reference (17, was 9, +5 from the firecrawl/skills import,
  +2 from the arxiv-skills import, +1 from the adobe/react-spectrum
  import on 2026-08-16 — see THIRD-PARTY IMPORT below):
  docx, xlsx, pptx, pdf, mcp-builder, vercel-react-best-practices,
  vercel-react-native-skills, vercel-react-view-transitions,
  vercel-composition-patterns, react-aria, firecrawl-build,
  firecrawl-build-scrape, firecrawl-build-search, firecrawl-build-interact,
  firecrawl-build-onboarding, arxiv-lookup, arxiv-doc-builder

scaffolding-templating (54, was 16 after the REMOVALS below, +12 from the
  taste-skill import, +1 from the hallmark import, +9 from the
  emilkowalski/skills import, +10 from the AccessLint +
  bencium.io + hermes-agent imports on 2026-08-16, +2 from the same-day
  hermes-agent p5js/sketch whole-skill install, +4 from the same-day
  react-bits/React Aria/shadcn/Magic UI deep-integration request (3 of
  the 4 land here, react-aria lands in library-api-reference instead) —
  see THIRD-PARTY IMPORT below. Note: the running total stated after the
  AccessLint/bencium.io/ hermes-agent batch was 47; a direct file-count
  during the later p5js/sketch batch's own verification found 48
  pre-existing sub-domain SKILL.md files at that point, not 47 —
  corrected here, not traced further back):
  programmatic-seo, design, design-system, ui-styling, shadcn-official
  (frontmatter name `shadcn`), migrate-radix-to-base, magicui,
  react-bits, ui-ux-pro-max,
  banner-design, brand, anthropic-brand-guidelines (renamed from
  brand-guidelines), canvas-design, algorithmic-art, theme-factory,
  frontend-design, web-artifacts-builder, web-design-guidelines,
  writing-guidelines, slides, taste-skill, taste-skill-v1, brandkit,
  brutalist-skill, gpt-tasteskill, image-to-code-skill,
  imagegen-frontend-mobile, imagegen-frontend-web, minimalist-skill,
  redesign-skill, soft-skill, stitch-skill, hallmark, emil-design-eng,
  animate, review-animations, improve-animations,
  find-animation-opportunities, animation-vocabulary, apple-design,
  pick-ui-library, prototype-variants (renamed from the source repo's
  `prototype` — see THIRD-PARTY IMPORT below), accessibility-audit,
  accessibility-scan, accessibility-inspect, accessibility-diff,
  accessibility-fix, ui-typography, relationship-design,
  popular-web-designs, design-md, baoyu-infographic, p5js, sketch

code-quality-review (14, was 6, +6 from the mattpocock-skills import,
  +1 from the awesome-llm-apps import, +1 from the claude-skill-ip-guard
  import):
  code-review-expert, semgrep, code-security, llm-security,
  requesting-code-review, receiving-code-review, code-review,
  improve-codebase-architecture, codebase-design, design-an-interface,
  setup-ts-deep-modules, setup-pre-commit, scope-creep-detector, ip-guard

cicd-deployment (2):
  deploy-to-vercel, vercel-cli-with-tokens

incident-runbooks (4, was 1, +2 from the mattpocock-skills import,
  +1 from the awesome-llm-apps import):
  systematic-debugging (absorbed mattpocock-skills' diagnosing-bugs —
  see THIRD-PARTY IMPORT below), triage, qa, commit-archaeologist

infrastructure-ops (1, was 0 placeholder, +1 from the third-party
  import):
  wizard

agentic-dev-workflow (25, was 8, +14 from the mattpocock-skills import,
  +1 from the andrej-karpathy-skills import, +1 from the awesome-llm-apps
  import, +1 from the human-architect-mindset "Loyalty" extraction on
  2026-08-16 — see THIRD-PARTY IMPORT below):
  brainstorming, dispatching-parallel-agents, executing-plans,
  subagent-driven-development, using-superpowers, writing-plans,
  using-git-worktrees, finishing-a-development-branch,
  ask-matt, grilling, grill-me, grill-with-docs, domain-modeling,
  to-spec, to-tickets, wayfinder, request-refactor-plan, prototype,
  setup-matt-pocock-skills, handoff, resolving-merge-conflicts,
  git-guardrails-claude-code, karpathy-guidelines, thinking-out-loud,
  loyalty-mindset

openspec-workflow (5):
  openspec-apply-change, openspec-archive-change, openspec-explore,
  openspec-propose, openspec-sync-specs

deep-research (6, was 5, +1 from the third-party import):
  research, research-add-fields, research-add-items, research-deep,
  research-report, background-research (renamed from mattpocock-skills'
  research to avoid colliding with this skill's own "research" pipeline
  stage)

internal-writing-comms (7, was 2, +3 from the mattpocock-skills import,
  +1 from the research-paper-writing import, +1 from the Humanizer-zh-TW
  import):
  doc-coauthoring, internal-comms, writing-fragments, writing-shape
  (absorbed writing-beats + edit-article — see THIRD-PARTY IMPORT
  below), to-questionnaire, research-paper-writing, humanizer-zh-tw

marketing (48, was 47, +1 from the bencium.io insurgent-campaign
  whole-skill install on 2026-08-16 — see THIRD-PARTY IMPORT below):
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
    public-relations, revops, sales-enablement, competitors,
    insurgent-campaign
  (competitor-profiling originally landed here too, then moved to
   browser-automation once the naming/overlap issue with competitor
   research was worked out — see browser-automation's list above)

skill-authoring (5, was 4, +1 from the third-party import):
  skill-creator, skill-forge, skill-review, writing-skills,
  writing-great-skills

personal-learning (4, was 3, +1 from the third-party import):
  book-study, wiki-ingest, sigma, teach

-----------------------------------------------------------------------
Total accounted for: 28+4+1+5+16+50+14+2+4+1+25+5+6+7+48+5+4 = 225
Plus context-engineering-collection: kept independent, never split
  (originally installed as one skill covering 17 internal sub-skills,
  now 16 after the REMOVALS below; re-wrapping it would have added no
  value).
225 sub-domains across 17 skills + context-engineering-collection's own
16 = 241 sub-skill-level SKILL.md files, down from 137 + 30 + 1 + 4 + 1 +
12 + 1 + 1 + 9 + 17 + 2 + 1 + 1 + 5 + 2 + 3 + 4 + 1 = 232
originally-installed-or-imported skill units after 7 removals from the
first batch (see REMOVALS below) — the 241 vs 232 discrepancy is because
"sub-domains" here counts each merge target once even where 2+ original
skills fed into it (test-driven-development, systematic-debugging,
writing-shape each absorbed one or two others' unique content without
becoming a second file). The penultimate "+4" is the 2026-08-16 9-item
batch (see THIRD-PARTY IMPORT below): only 4 of the 9 items became new
standalone `SKILL.md` files (`p5js`, `sketch`, `insurgent-campaign`,
`loyalty-mindset`) — the other 5 items in that same batch were surgical
fragment-extractions folded into already-existing files
(`frontend-design`, `redesign-skill`, `taste-skill`, `hallmark`'s `audit`
verb, `ai-seo`), so they correctly contribute 0 to this count, exactly
like the mattpocock-skills fragments folded into
test-driven-development/systematic-debugging above. The final "+1" is a
correction, found while verifying this same batch's arithmetic by direct
file count: `scaffolding-templating`'s stated pre-batch baseline of 47
was itself off by one (a direct enumeration of every `SKILL.md` under
`scaffolding-templating/references/` — both before and after adding
`p5js`/`sketch` — turns up 50 sub-domain files post-batch, meaning 48
pre-batch, not 47). Not traced further back through every earlier
session's delta to find exactly where the original miscount entered (out
of this batch's scope) — corrected forward from this point on; see
SKILL-AUDIT.md's "2026-08-16（三）" section.

REMOVALS (2026-07-31 health check on the original 137, see SKILL-AUDIT.md
for the full methodology and reasoning) — these 7 were deleted as
low/never-triggered and are NOT missing installs, do not reinstall them
without a new reason:
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

THIRD-PARTY IMPORT — mattpocock-skills (Matt Pocock, aihero.dev, MIT
license), 2026-07-31. Full license text and per-file attribution list:
THIRD-PARTY-LICENSES.md. Full audit methodology and reasoning:
SKILL-AUDIT.md.

Imported all 41 folders from the vendor's repo (22 officially declared
in its plugin.json, plus 19 more under deprecated/in-progress/misc/
personal that the vendor shipped but didn't declare). Read every file in
full (not just description) before any classification decision, per the
lesson learned earlier the same day on 3 consolidated-skill "merge"
misjudgments (see the note in SKILL-AUDIT.md).

After curation, 30 remained (5 removed as author-private/superseded, 2
merged into this repo's own pre-existing skills, 4 merged as competing
in-pack variants into 2 files). At the user's explicit request, these 30
were then distributed by topic into 9 of this repo's existing 18
top-level skills — NOT kept as a separate 19th "mattpocock-skills"
top-level skill or folder. See each skill's entry above (marked "+N from
the third-party import") for where each one landed.

REMOVED entirely (5) — hardcoded to the original author's private
environment, or fully superseded, no general applicability:
  - personal/obsidian-vault — hardcoded author WSL path
  - misc/scaffold-exercises — depends on author's private course CLI
  - misc/migrate-to-shoehorn — migrates to a niche npm package the
    author maintains himself
  - engineering/implement — thin stub, fully superseded by this repo's
    own agentic-dev-workflow/subagent-driven-development +
    executing-plans (dispatch-a-fresh-subagent-per-task, already more
    complete)
  - deprecated/ubiquitous-language — superseded by this same pack's
    newer domain-modeling; qa's reference to its output file
    (UBIQUITOUS_LANGUAGE.md) was repointed to domain-modeling's
    CONTEXT.md

MERGED into this repo's own pre-existing skills, not kept as separate
files (2):
  - engineering/tdd → product-verification/test-driven-development
    (contributed: Seams section, 3 named anti-patterns, Mocking section
    — see that skill's anti-pattern-examples.md / mocking.md)
  - engineering/diagnosing-bugs → incident-runbooks/systematic-debugging
    (contributed: build-a-feedback-loop-first method — see that skill's
    building-a-feedback-loop.md — ranked multi-hypothesis generation,
    debug-tag convention, correct-seam nuance for regression tests)

MERGED within the pack itself, competing variants of the same mechanic
folded into one file rather than kept as two (4 folders → 2 files, both
now living in agentic-dev-workflow/internal-writing-comms respectively):
  - in-progress/batch-grill-me → agentic-dev-workflow/grilling (as its
    --batch whole-frontier-per-round mode)
  - in-progress/claude-handoff → agentic-dev-workflow/handoff (as its
    background-agent delivery path)
  - in-progress/writing-beats + personal/edit-article →
    internal-writing-comms/writing-shape (beat-sized narrative mode; the
    dependency-respecting section-reorder step for editing an existing
    draft)

Deliberately NOT merged despite looking like duplicates by name/
description alone — read in full, each side had independent scripts/
frameworks/depth, so both stay (now in the same top-level skill as their
counterpart in every case) with cross-reference notes added to each
side's description instead:
  - code-quality-review/code-review vs .../code-review-expert
  - personal-learning/teach vs .../sigma
  - skill-authoring/writing-great-skills vs .../writing-skills
  - deep-research/background-research vs deep-research's own pipeline

Renamed to avoid a name collision with this repo's own skill of the same
name (1):
  - engineering/research → deep-research/background-research (both the
    folder and the SKILL.md frontmatter `name:` field)

Category README.md files the vendor shipped per-folder (deprecated/,
engineering/, in-progress/, misc/, personal/, productivity/) were all
removed as duplicate, now-stale indexes once distributed — this file,
each destination skill's own SKILL.md, and SKILL-AUDIT.md are the index
now.
=======================================================================

THIRD-PARTY IMPORT — andrej-karpathy-skills (forrestchang, MIT license),
2026-08-01. Full license text and attribution: THIRD-PARTY-LICENSES.md.

Source repo (github.com/forrestchang/andrej-karpathy-skills, mirrored at
github.com/multica-ai/andrej-karpathy-skills) ships a Claude Code plugin
containing exactly one skill, skills/karpathy-guidelines/SKILL.md (a
condensed 4-principle behavioral checklist: Think Before Coding,
Simplicity First, Surgical Changes, Goal-Driven Execution), plus vendor
root docs (README.md, README.zh.md, CLAUDE.md, CURSOR.md, EXAMPLES.md,
.claude-plugin/, .cursor/) that are the vendor's own installation/plugin
scaffolding, not additional skill content — none of those were copied in.

Read in full against the three existing skills it resembles by theme
(agentic-dev-workflow/brainstorming, product-verification's
test-driven-development + verification-before-completion,
code-quality-review) before deciding: no true duplicate found on any
side — brainstorming is a structured multi-step interview/spec-writing
process, the verification pair is a specific red-green-refactor +
evidence-before-claiming protocol, and code-quality-review is an
after-the-fact review protocol. karpathy-guidelines is a short, general,
in-the-moment coding-discipline reference that doesn't overlap in
mechanism with any of them, so it was kept as its own file (not merged
into any of the three) and given cross-reference notes instead, per the
"don't merge on thematic overlap alone" rule.

Folded into agentic-dev-workflow (not a new top-level category) as
`references/karpathy-guidelines/SKILL.md`, listed in that skill's own
SKILL.md as a standing reference rather than a lifecycle step. No name
collision with any existing skill's folder or frontmatter `name:`. No
internal cross-references in the source file needed fixing (self-
contained, no relative links to other files). Not added to the Universal
table: its description is phrased "Use when writing/reviewing/
refactoring code," not an explicit "invoke before any response" claim.
=======================================================================

THIRD-PARTY IMPORT — awesome-llm-apps agent_skills/ (Shubham Saboo /
Matt Van Horn, Apache-2.0 license), 2026-08-01. Full license text and
attribution: THIRD-PARTY-LICENSES.md.

Source repo (github.com/Shubhamsaboo/awesome-llm-apps) is mostly a large
collection of unrelated example LLM applications; only its agent_skills/
subfolder contains actual SKILL.md-format skills (5 of them), plus a
non-skill demo web app (self-improving-agent-skills/, a Next.js+Python
tool, not copied in) and its own evals/ test harness (not copied in —
this repo's imports don't carry source-repo test suites).

Read all 5 skills' full SKILL.md + bundled scripts/references in full
before deciding. 4 were kept: commit-archaeologist, project-graveyard,
scope-creep-detector, thinking-out-loud. The 5th,
advisor-orchestrator-worker, was excluded — it re-implements a
model-team orchestration loop (advisor reviews plan, worker models
execute) that duplicates this environment's own native multi-agent
`Workflow` tool; importing it would add a second, conflicting mechanism
for the same job.

Each kept skill was compared against the existing skill it most
resembled by theme, full-content not description-only:
  - commit-archaeologist vs incident-runbooks/systematic-debugging: both
    are "investigate before you act" disciplines, but distinct axes
    (why code exists historically vs. root-causing a live bug) — no
    duplicate, folded in as a sibling domain.
  - project-graveyard: no existing skill does machine-wide dead-project
    scanning/triage; novel, placed in business-automation as a
    prioritization/planning decision tool.
  - scope-creep-detector vs code-quality-review/code-review-expert +
    receiving-code-review: three distinct axes (diff-vs-intent scope
    triage vs. SOLID/security review vs. feedback-reception etiquette) —
    no duplicate, cross-references added on both sides instead of
    merging.
  - thinking-out-loud vs agentic-dev-workflow/brainstorming: distinct —
    thinking-out-loud is a front-end listening/echo-confirmation
    discipline for messy rambling input, brainstorming is a
    spec-production pipeline that assumes already-parseable intent; no
    duplicate, cross-references added on both sides (thinking-out-loud
    hands off an approved brief to brainstorming when the brief
    describes creative/feature work).

Each kept skill's own per-repo README.md (source repo's own marketing
copy, `npx skills add` install instructions, externally-hosted demo
GIFs) was dropped rather than copied — per this repo's own convention
that SKILL.md is the only index going forward. No name collisions with
any existing skill's folder or frontmatter `name:`. Internal
references/scripts links inside each kept skill are self-contained
(relative to their own folder) and needed no fixing after the move.

Folded into 4 different existing top-level skills (not a new category):
  - commit-archaeologist → incident-runbooks/references/
  - project-graveyard → business-automation/references/
  - scope-creep-detector → code-quality-review/references/
  - thinking-out-loud → agentic-dev-workflow/references/

Not added to the Universal table: none of the 4 carry "MUST use before
any response" language — each is scoped to a specific triggering
situation (rambling input, pre-PR diff, abandoned-project question,
pre-edit history question), not a standing trigger.
=======================================================================

THIRD-PARTY IMPORT — claude-skill-ip-guard (Mugdha Vairagade, Apache-2.0
license), 2026-08-02. Full license text and attribution:
THIRD-PARTY-LICENSES.md.

Source repo (github.com/mugdhav/claude-skill-ip-guard) ships one skill,
ip-guard/SKILL.md plus references/license-compatibility.md,
references/dependency-security.md, scripts/license_audit.sh, and
scripts/dependency_security_scan.sh. Vendor root docs (README.md,
CHANGELOG.md, CONTRIBUTING.md, LICENSE, user-reports/ example write-ups)
are the vendor's own marketing/install scaffolding, not additional skill
content — none of those were copied in, per this repo's standing
convention that SKILL.md is the only index going forward.

Read in full against the two existing skills it resembles by theme
(code-quality-review/code-security, code-quality-review/llm-security)
before deciding: no true duplicate found on either side — code-security
is a general secure-coding checklist (injection, auth, file ops, crypto,
infra config) with no license/IP content; llm-security's supply-chain
section covers LLM/model supply chain (unverified model downloads,
malicious pickle files, LoRA adapters), not general npm/pip/cargo
dependency licensing or transitive vulnerability scanning. ip-guard is a
three-stage IP/license compliance + dependency-security-scan guardrail
with its own bundled scripts, so it was kept as its own file (not merged
into either) with cross-reference notes added on all three sides.

Scripts were read in full before copying: license_audit.sh and
dependency_security_scan.sh only install/invoke standard, name-brand
scanning tools (pip-audit, pipdeptree, npm audit, cargo-audit,
license-checker, pip-licenses, cargo-license, go-licenses) against the
current project's own manifest/lockfile — no network exfiltration, no
destructive operations, nothing outside the project directory except the
already-standard "install the CLI scanner tool itself" step every
license/audit tool in this repo already does the same way.

Folded into code-quality-review (not a new top-level category) as
`references/ip-guard/SKILL.md`, listed in that skill's own SKILL.md
domain table with an explicit cross-reference disambiguating it from
code-security and llm-security. No name collision with any existing
skill's folder or frontmatter `name:`. No internal cross-references in
the source file needed fixing (all relative paths point within its own
folder: references/license-compatibility.md,
references/dependency-security.md, scripts/*.sh).

Universal-tier eligibility — the one non-default judgment call in this
import: ip-guard's own description reads as "activates automatically
whenever Claude is about to generate code, suggest dependencies, or
produce content for commercial use... even if the user doesn't mention
copyright" — broader in scope than any of the 5 entries in the Universal
table above (those trigger on specific sensitive surfaces; this reads as
"any generation task"). Per the standard procedure's Phase C step 9,
this was flagged to the user rather than decided unilaterally, since
adding it to the Universal table would add license-declaration/
dependency-plan/provenance-block overhead to every future code
generation across every project on this machine — a much bigger
blast-radius decision than a normal skill import. The user's explicit
decision (2026-08-02): do NOT add it to the Universal table, and scope
its actual triggering granularity to (a) once per newly-introduced
external dependency (Stage 1b/2 of the skill's own design) and (b) once
per completed file/artifact for the provenance block (Stage 3) — not
per conversational turn/paragraph. This matches the skill's own
as-authored design already (Stage 1/2 fire on new-dependency events,
Stage 3 fires per artifact), so no internal rewrite of ip-guard/SKILL.md
was needed — only the placement decision (kept out of the Universal
table) and a documentation note in code-quality-review/SKILL.md and this
file spelling out the agreed granularity, so a future session doesn't
re-promote it to Universal without re-checking this reasoning.
=======================================================================

THIRD-PARTY IMPORT — taste-skill (Leonxlnx, MIT license), 2026-08-05.
Full license text and attribution: THIRD-PARTY-LICENSES.md.

Source repo (github.com/Leonxlnx/taste-skill) ships a Claude Code plugin
(.claude-plugin/marketplace.json + plugin.json) bundling 12 independent
skills under skills/: taste-skill, taste-skill-v1, brandkit,
brutalist-skill, gpt-tasteskill, image-to-code-skill,
imagegen-frontend-mobile, imagegen-frontend-web, minimalist-skill,
output-skill, redesign-skill, soft-skill, stitch-skill (the last also
ships a DESIGN.md alongside its SKILL.md). Vendor root docs (README.md,
CHANGELOG.md, .github/copilot-instructions.md, research/ — a laziness
research writeup unrelated to any individual skill's content) are the
vendor's own marketing/research scaffolding, not additional skill
content — none of those were copied in.

All 12 were read in full (not just frontmatter description) before any
placement decision. 11 are frontend visual-design "taste" specs of
varying scope (full anti-slop pipelines, named aesthetics, image-only
direction, an image-first Codex workflow, a Google-Stitch DESIGN.md
generator) — compared each against every existing scaffolding-templating
design domain (`frontend-design`, `brand`, `design`, `ui-styling`,
`ui-ux-pro-max`) and against each other: no true duplicate found anywhere
in the set — each has its own concrete, largely mutually-incompatible
rule set (different banned-font lists, different numeric dial systems,
different code skeletons, different output modality). All 11 kept as
separate files, folded into scaffolding-templating/references/design/
with a dedicated "Anti-AI-slop frontend taste systems" table and picking
guidance added to that skill's own SKILL.md (see its "How to use this
skill" points 7-8).

The 12th, `output-skill` (frontmatter name `full-output-enforcement`), is
NOT a design skill — it's an anti-truncation/complete-output-generation
discipline (bans placeholder code comments and "I'll leave the rest as
an exercise"-style prose, defines a pause/resume format for responses
that would hit the token limit). Compared against
product-verification/verification-before-completion: adjacent but
distinct axes (verification-before-completion governs *claiming* work is
done; output-skill governs actually *delivering* the full thing without
silent truncation) — no duplicate, kept as its own file, folded into
product-verification/references/ instead of scaffolding-templating, with
cross-reference notes added on both sides.

No name collisions with any existing skill's folder or frontmatter
`name:` (checked all 12 candidate frontmatter names plus all 12 folder
names against the full repo). No internal cross-references needed
fixing — none of the 12 skills reference each other or any file outside
their own single SKILL.md (+DESIGN.md for stitch-skill).

Not added to the Universal table: none of the 12 carry "invoke before
any response" language — each is scoped to an explicit design/build/
enforcement request, not a standing trigger.

Folded into 2 existing top-level skills (not a new category):
  - scaffolding-templating/references/: taste-skill, taste-skill-v1,
    brandkit, brutalist-skill, gpt-tasteskill, image-to-code-skill,
    imagegen-frontend-mobile, imagegen-frontend-web, minimalist-skill,
    redesign-skill, soft-skill, stitch-skill (11)
  - product-verification/references/: output-skill (1)
=======================================================================

THIRD-PARTY IMPORT — hallmark (Nutlope, MIT license), 2026-08-05. Full
license text and attribution: THIRD-PARTY-LICENSES.md.

Source repo (github.com/Nutlope/hallmark) is a full npm package (a CLI +
demo site under site/, docs/ for humans, package.json, ROADMAP.md) whose
only agent-facing skill content lives at skills/hallmark/SKILL.md plus
its own references/ tree (105 files: anti-patterns, color, typography,
layout-and-space, motion, copy, macrostructures/ [21 named page shapes],
components/ [50 nav/hero/section/CTA/testimonial/footer archetypes],
genres/ [editorial, modern-minimal, atmospheric, playful], verbs/audit.md
+ verbs/redesign.md, study.md, custom-theme.md, slop-test.md [58 gates],
and more). The site/, docs/, package.json, ROADMAP.md, and root README
are the vendor's own product/demo/build tooling, not skill content — none
of those were copied in, only skills/hallmark/ (SKILL.md + its full
references/ tree, since — unlike taste-skill's 12 single-file skills —
hallmark's own references are load-on-demand content the skill's own
Step 3 explicitly instructs loading selectively rather than eagerly).

Read the full SKILL.md (558 lines) plus a representative sample of its
references/ (macrostructures.md index, anti-patterns.md, the genres/ and
verbs/ files) before deciding placement. Compared against `taste-skill`
(imported the same day) and `frontend-design`: real thematic overlap
(both `taste-skill` and `hallmark` are complete anti-slop frontend
pipelines with brief-intake, a numeric/categorical style-selection step,
hard layout rules, and a mandatory pre-ship self-check) but NOT a true
duplicate — distinct mechanisms throughout: hallmark's mandatory
three-question context gate vs. taste-skill's one-line inferred "design
read"; hallmark's named 20-theme catalog + custom-OKLCH branch vs.
taste-skill's numeric 3-dial system; hallmark's own `audit`/`redesign`/
`study` verbs (including URL/screenshot DNA-extraction) with no
equivalent in taste-skill; hallmark's persistent `.hallmark/log.json`
diversification log forcing a different macrostructure/theme/nav/footer
than the last N runs, which taste-skill has no equivalent mechanism for.
Kept as its own file rather than merged into taste-skill or
frontend-design, with cross-reference/picking guidance added to
scaffolding-templating/SKILL.md instead (see its "Anti-AI-slop frontend
taste systems" table intro and "How to use this skill" point 7) — per the
standing "don't merge on thematic overlap alone" rule, since both sides
have independent, non-overlapping depth.

No name collision with any existing skill's folder or frontmatter `name:`
(`hallmark`). Internal cross-references inside the copied references/
tree are entirely self-contained relative paths within hallmark's own
folder (references/<file>.md, references/components/<code>.md, etc.) —
none needed fixing after the move. Vendor's own per-file "Powered by
Together AI" branding line in SKILL.md was left as-is (attribution to the
tool that powers hallmark's own image-generation tier, not a claim this
repo endorses or operates that service).

Not added to the Universal table: hallmark's own description is phrased
as a design skill invoked for build/audit/redesign/study requests, not an
"invoke before any response" claim.

Folded into scaffolding-templating (not a new top-level category) as
`references/design/hallmark/SKILL.md` (+ its references/ tree), listed in
that skill's own "Anti-AI-slop frontend taste systems" table.
=======================================================================

THIRD-PARTY IMPORT — anysearch-skill (AnySearch Team, Apache-2.0
license), 2026-08-07. Full license text and attribution:
THIRD-PARTY-LICENSES.md.

Source repo (github.com/anysearch-ai/anysearch-skill) ships one skill:
SKILL.md plus a bundled multi-runtime CLI under scripts/
(anysearch_cli.py, anysearch_cli.js, anysearch_cli.ps1, anysearch_cli.sh,
generate.py, shared/constants.json, shared/doc_spec.md),
runtime.conf.example, and .env.example. Vendor root docs (README.md,
README_zh.md, SECURITY.md, LICENSE, NOTICE) are the vendor's own
marketing/install/vulnerability-reporting scaffolding, not agent-facing
skill content — none of those were copied in, per this repo's standing
convention that SKILL.md is the only index going forward (license text
centralized in THIRD-PARTY-LICENSES.md instead of a vendored LICENSE
file, matching the claude-skill-ip-guard precedent).

All 4 CLI scripts were read in full before copying: each hits exactly one
hardcoded endpoint (https://api.anysearch.com/mcp, consistent across all
4 runtimes), contains no eval/exec/subprocess-shell-out/base64-obfuscation
patterns, and performs no filesystem or network operation outside that
one documented endpoint plus reading its own local .env/runtime.conf.

Read in full against the one existing skill it resembles by theme
(browser-automation/search, a Browserbase-only curl-based lightweight
search wrapper) before deciding: no true duplicate — `search` is a
single-endpoint, no-CLI, Browserbase-credentialed lookup with no vertical
domains and no batch mode; `anysearch` is a separate third-party service
with its own bundled 4-runtime CLI, structured vertical-domain search
across 16 named domains (finance, academic, travel, health, code, legal,
gaming, film, business, security, ip, energy, environment, agriculture,
resource, social_media) via `get_sub_domains`, parallel `batch_search`,
and a distinct `extract` command for full-page Markdown content. Kept as
its own file, not merged into `search`, with cross-reference/disambiguation
notes added to both sides in browser-automation/SKILL.md ("Note on
`search` vs `anysearch`") per the standing "don't merge on thematic
overlap alone" rule.

Folded into browser-automation (not a new top-level category) as
`references/anysearch/SKILL.md` (+ its scripts/ tree), listed in that
skill's own Domains table under Research & prospecting. No name collision
with any existing skill's folder or frontmatter `name:` (checked
`anysearch` against the full repo). No internal cross-references needed
fixing — the skill's own SKILL.md only references paths relative to its
own `<skill_dir>` (scripts/, runtime.conf, .env), which still resolve
correctly after the move.

Credential/network note (not a placement blocker, but worth flagging for
future sessions): this skill sends search queries, extracted URLs, and
(if configured) an API key to the third-party endpoint
https://api.anysearch.com, and its own SKILL.md instructs the agent to be
able to auto-register a user account (via a `/v1/auth/email/register`
call using a real email address, with a password emailed to that
address) and to persist any resulting API key to a local `.env` file —
but only after showing the user what was received and getting explicit
confirmation before writing it to disk. This mirrors the same
network-boundary and credential-handling caution already applied to
`search` (Browserbase) and other networked skills in this repo; no
change to the skill's own logic was made.

Not added to the Universal table: anysearch's own description is scoped
to explicit information-retrieval/fact-checking/search triggers, not an
"invoke before any response" claim.
=======================================================================

THIRD-PARTY IMPORT — emilkowalski/skills (Emil Kowalski, MIT license),
2026-08-09. Full license text and attribution: THIRD-PARTY-LICENSES.md.

Source repo (github.com/emilkowalski/skills) ships 9 skills under
skills/: emil-design-eng, animate (+RECIPES.md), animation-vocabulary,
apple-design, find-animation-opportunities, improve-animations
(+AUDIT.md, +PLAN-TEMPLATE.md), pick-ui-library, prototype (+PICKER.md),
review-animations (+STANDARDS.md). Vendor root docs (README.md, LICENSE)
are the vendor's own marketing/install/license scaffolding — README.md
was not copied in per this repo's standing convention that SKILL.md is
the only index going forward; LICENSE text was centralized in
THIRD-PARTY-LICENSES.md instead of vendoring a LICENSE file, matching
the claude-skill-ip-guard / anysearch-skill precedent. No scripts/ tree —
every file across all 9 skills is Markdown (SKILL.md + bundled reference
docs), so no code-execution review was needed.

All 9 read in full (not just frontmatter description) before any
placement decision, then compared against every existing design/review/
prototyping skill it could thematically resemble:
- vs the "Anti-AI-slop frontend taste systems" table (`taste-skill`,
  `hallmark`, etc.) and `frontend-design`: those are about visual
  language (color, layout, typography, named aesthetics/macrostructures);
  this pack is specifically about interface *motion mechanics* (easing
  curves, spring physics, gesture velocity/interruptibility, GPU
  properties). `hallmark`'s own `references/motion.md` covers adjacent
  ground (same three-bucket duration idea, similar cubic-bezier shape)
  but at ~109 lines as one facet of a much broader pipeline, using its
  own distinct concrete values (e.g. `cubic-bezier(0.16,1,0.3,1)` vs this
  pack's `cubic-bezier(0.23,1,0.32,1)`) — independently authored, not a
  duplicate, no merge; both sides now cross-reference each other's
  section instead.
- vs `code-quality-review` (code-review-expert, code-review,
  receiving-code-review, scope-creep-detector): different axis entirely
  — general code correctness/SOLID/security/scope, not animation feel.
  No overlap.
- vs `library-api-reference` (docx/xlsx/pptx/pdf/mcp-builder/vercel-*):
  those are API-usage references for specific libraries/formats;
  `pick-ui-library` is a *decision* tool (which library to reach for,
  from a curated opinionated list) with no API documentation of its own.
  No overlap — placed in scaffolding-templating instead, alongside the
  other design-decision skills, since it's from the same source pack and
  the same "which UI building-block to reach for" question class.

**Name collision found and resolved**: the source repo's `prototype`
(folder + frontmatter `name: prototype`) collides with this repo's own
pre-existing `agentic-dev-workflow/references/prototype` (imported from
mattpocock-skills on 2026-07-31). Read both in full: the existing skill
is a general throwaway-code discipline — one artifact, one hard design
question (state/logic OR UI), captured to a branch when done. The
incoming skill is narrower and more elaborate — always UI, always
*multiple* (3–5) genuinely divergent variants rendered together behind a
specific, verbatim visual-picker component (keyboard nav, URL-param
persistence, replay button — spec'd in its own PICKER.md) that the user
flips through live before promoting a winner. Real depth on both sides,
not a true duplicate — kept as two separate files rather than merged.
Renamed the incoming one to `prototype-variants` (both the folder name
and the frontmatter `name:` field) to resolve the collision, per Phase C
step 5 of the standard procedure. Cross-reference notes added on both
sides: `agentic-dev-workflow/references/prototype/SKILL.md`'s own
description, `agentic-dev-workflow/SKILL.md`'s domain table, and
`scaffolding-templating/SKILL.md`'s new domain table entry all now point
at each other.

**Phase B (placement)**: classified as 偶爾需要 (occasional, context-
specific — invoked when a motion/animation/UI-library/prototyping request
comes up, not a standing trigger). Folded into the existing
`scaffolding-templating` top-level skill (design & visual templating
cluster) as a new "Animation, motion & UI-decision tools" table, not a
new top-level category — consistent with this repo's default "fold into
one of the existing 18" rule.

No other name collisions (checked all 9 candidate frontmatter names —
`emil-design-eng`, `animate`, `animation-vocabulary`, `apple-design`,
`find-animation-opportunities`, `improve-animations`, `pick-ui-library`,
`review-animations`, plus the renamed `prototype-variants` — and all 9
folder names against the full repo). Internal cross-references (SKILL.md
→ RECIPES.md/AUDIT.md/PLAN-TEMPLATE.md/STANDARDS.md/PICKER.md) are all
relative paths within each skill's own folder and needed no fixing after
the move.

`review-animations` and `pick-ui-library` both ship
`disable-model-invocation: true` in their own frontmatter (only run when
explicitly invoked, per the vendor's own design) — left as-is, not
overridden.

Not added to the Universal table: none of the 9 carry "invoke before any
response" language — each is scoped to an explicit animation/motion/
library-choice/prototyping request.

Folded into scaffolding-templating (not a new top-level category) as
`references/design/{emil-design-eng,animate,animation-vocabulary,
apple-design,find-animation-opportunities,improve-animations,
pick-ui-library,review-animations,prototype-variants}/SKILL.md`, listed
in that skill's own new "Animation, motion & UI-decision tools" table.
=======================================================================

THIRD-PARTY IMPORT — firecrawl/cli + firecrawl/skills (Firecrawl, ISC
license), 2026-08-16. Full license text and attribution:
THIRD-PARTY-LICENSES.md.

User provided `https://github.com/firecrawl/firecrawl.git` — the
company's main product monorepo (Node/Rust app source, dashboard,
infrastructure — apps/api/, native/, etc.). Read in full: it contains no
`SKILL.md` anywhere. It ships two pointer READMEs
(`firecrawl-cli-skills/README.md`, `firecrawl-skills/README.md`) that
name two *separate* official repos as the actual skill sources:
`github.com/firecrawl/skills` (application-integration skills) and
`github.com/firecrawl/cli/tree/main/skills` (live one-off web-tool
skills, bundled inside the CLI's own repo). Both were cloned and
evaluated in full instead of fabricating skill content from the
non-skill monorepo the user linked.

`firecrawl/skills` ships 7 skills: `firecrawl-build` (hub),
`firecrawl-build-scrape`, `firecrawl-build-search`,
`firecrawl-build-interact`, `firecrawl-build-onboarding`,
`firecrawl-developer-index`, `firecrawl-research-index`. `firecrawl/cli`
ships 10: `firecrawl-cli` (hub, frontmatter `name: firecrawl`, kept
as-shipped — no collision with any existing skill's exact frontmatter
name), `firecrawl-scrape`, `firecrawl-search`, `firecrawl-map`,
`firecrawl-crawl`, `firecrawl-monitor`, `firecrawl-interact`,
`firecrawl-download`, `firecrawl-agent`, `firecrawl-parse` (the last two
folded in `rules/install.md` + `rules/security.md`, each with its own
frontmatter, kept as bundled references rather than promoted to
top-level entries). All 17 SKILL.md files read in full. Vendor root docs
in both repos (README.md, CLAUDE.md, AGENTS.md, CONTRIBUTING.md,
marketplace/plugin manifests, `.mcp.json`) are install/marketing/plugin
scaffolding, not skill content — none copied in.

**Split placement, by job, not by source repo**: the `firecrawl-build*`
5 skills are for wiring Firecrawl into an application's own source code
(choosing an SDK/endpoint, `.env` setup) — folded into
`library-api-reference`, alongside this repo's other "how do I call this
API/library correctly" domains. The 10 `firecrawl/cli` skills plus the 2
index skills are for live, one-off web work during the current session
(search/scrape/crawl/map/monitor/interact/parse a local file/AI-schema
extraction) — folded into `browser-automation`, alongside the existing
`browser`/`fetch`/`search`/`anysearch` domains. This mirrors the source
project's own stated distinction (`firecrawl-build`'s own SKILL.md: "Use
this skill when the task is... not 'use Firecrawl as a terminal tool
right now'").

Compared in full against every existing domain it could resemble:
- vs `browser-automation/search` + `anysearch`: three separate vendors
  now do search in this skill. No true duplicate — Firecrawl is the
  broadest (adds crawl/map/monitor/interact/parse/agent-extraction/
  developer-index/research-index, none of which the other two have).
  Cross-reference note added to `browser-automation/SKILL.md` ("Note on
  the Firecrawl CLI cluster vs. `search`/`anysearch`/`fetch`") rather
  than merging or picking a winner — a project's existing credentials
  for one vendor are a legitimate reason to stay there for simple search.
- vs `browser-automation/fetch`: `fetch` is plain HTTP with no rendering
  and no third-party credentials; `firecrawl-scrape` handles JS-rendered
  SPAs and needs `FIRECRAWL_API_KEY` (or the keyless free tier) — no
  duplicate, `fetch` stays the cheaper default when JS rendering isn't
  needed.
- vs `library-api-reference`'s existing docx/xlsx/pptx/pdf domains:
  `firecrawl-parse` converts local files (PDF/DOCX/XLSX/etc.) to
  Markdown via Firecrawl's cloud API, a different mechanism from this
  repo's own file-creation/editing skills for those same formats — no
  duplicate, no merge, `firecrawl-parse` stayed in `browser-automation`
  (it's a CLI-verb skill, not an app-integration one) rather than moving
  to `library-api-reference`.
- vs `deep-research` and (later this same day) `arxiv-skills`:
  `firecrawl-research-index` searches Firecrawl's own paper-abstract
  corpus (semantic search + citation graph + full-text verification) —
  a different mechanism from `deep-research`'s outline-driven pipeline
  and from `arxiv-doc-builder`'s fetch-and-convert-a-known-paper job.
  Cross-references added in `browser-automation/SKILL.md`'s "How to pick
  a domain" rather than merging.

**Security review of bundled scripts**: none — all 17 skills across both
repos are pure Markdown (SKILL.md + `rules/*.md` + `references/*.md`),
no bundled executable scripts of any kind. `rules/security.md`
(frontmatter `name: firecrawl-security`) is itself a prompt-injection/
untrusted-content-handling guide for agents consuming fetched web
content — read in full, it recommends exactly the file-based output
isolation and incremental-reading pattern this repo's own networked
skills already follow.

No name collisions: all 17 candidate frontmatter names (`firecrawl-build`
through `firecrawl-research-index`, plus bare `firecrawl` for the CLI
hub) checked against the full repo — none collide with anything
existing.

Not added to the Universal table: all 17 are scoped to explicit web-data/
integration requests, no "invoke before any response" language.

Folded into `library-api-reference` (5: `firecrawl-build`,
`firecrawl-build-scrape`, `firecrawl-build-search`,
`firecrawl-build-interact`, `firecrawl-build-onboarding`) and
`browser-automation` (12: `firecrawl-cli`, `firecrawl-agent`,
`firecrawl-crawl`, `firecrawl-download`, `firecrawl-interact`,
`firecrawl-map`, `firecrawl-monitor`, `firecrawl-parse`,
`firecrawl-scrape`, `firecrawl-search`, `firecrawl-developer-index`,
`firecrawl-research-index`) — not a new top-level category.
=======================================================================

THIRD-PARTY IMPORT — arxiv-skills (ultimatile, MIT license), 2026-08-16.
Full license text and attribution: THIRD-PARTY-LICENSES.md.

Source repo (github.com/ultimatile/arxiv-skills) ships a Claude Code
plugin (`.claude-plugin/marketplace.json`) with 2 skills:
`arxiv-lookup` (thin scripts — `get_doi.py`, `search_id.py` — querying
the arXiv API directly) and `arxiv-doc-builder` (a real installable
Python package: `arxiv_doc_builder/` fetch/convert modules, `tests/`,
`pyproject.toml`, `uv.lock`, plus `references/` docs) that fetches an
arXiv paper by id, converts LaTeX source to Markdown via pandoc
(preferred path, preserves math/structure), and falls back to naive PDF
text extraction when no LaTeX source exists. Both SKILL.md files and the
full `arxiv_doc_builder/` source read in full, including its extensive
pandoc-hang/glossaries/multi-documentclass troubleshooting notes. Vendor
root docs (README.md, ruff.toml, `.pre-commit-config.yaml`) are the
vendor's own lint/install scaffolding — not copied in.

**Security review**: `convert_latex.py`/`fetch_paper.py` call
`subprocess.run`/`Popen`, including one `shell=True` call
(`fetch_paper.py`, gzip-type detection) that interpolates a file path
built from the arXiv id. Checked `arxiv_id.py`: every id is validated
against a strict regex (`^\d{2}\d{2}\.\d{4,5}(v\d+)?$` for new-style ids,
a similarly narrow legacy pattern) before it's used to build any path, so
no shell metacharacter can survive into the interpolated string — no
command-injection risk. All network calls are to `arxiv.org`/
`export.arxiv.org` only. No other suspicious patterns (`eval`, `os.system`
with unvalidated input) found.

Compared against `deep-research` and (the same day) Firecrawl's
`firecrawl-research-index`: neither existing skill fetches-and-converts
a *specific already-identified* paper into implementation-reference
Markdown — `deep-research` builds a multi-source report from an outline,
`firecrawl-research-index` searches a corpus to *find* papers. No
overlap once the job (search vs. fetch-and-convert) is made explicit;
cross-references added instead of merging.

Folded into `library-api-reference` (not a new top-level category) as
`references/arxiv-lookup/SKILL.md` and
`references/arxiv-doc-builder/SKILL.md` (+ its full Python package and
`references/` tree) — grouped with the existing docx/xlsx/pptx/pdf
"convert this format to something usable" domains, with a cross-
reference to `pdf` for non-arXiv PDFs. No name collisions
(`arxiv-lookup`, `arxiv-doc-builder` checked against the full repo).
Internal cross-references are all relative to each skill's own folder
and needed no fixing.

Not added to the Universal table: both skills are scoped to explicit
paper-lookup/conversion requests.
=======================================================================

THIRD-PARTY IMPORT — research-paper-writing (Master-cai, MIT license),
2026-08-16. Full license text and attribution: THIRD-PARTY-LICENSES.md.

Source repo (github.com/Master-cai/Research-Paper-Writing-Skills) ships
one skill, `research-paper-writing/SKILL.md`, with a substantial
`references/` tree (per-section guides for abstract/introduction/
related-work/method/experiments/conclusion/paper-review, a paragraph-flow
self-check, and a large `references/examples/` bank of annotated
before/after paper excerpts). Also ships `agents/openai.yaml` — read in
full: this is OpenAI-platform Agent Builder display metadata (display
name, short description, default prompt), not agent-facing skill content
for Claude Code — not copied in, per the same convention used for every
other import's vendor-platform scaffolding. Root `README.md`/
`README_zh.md` also not copied in.

Compared against `internal-writing-comms/doc-coauthoring`: `doc-
coauthoring` is a general structured-document co-authoring *process*
(context transfer → draft → refine → verify against readers) applicable
to any proposal/spec/decision doc; `research-paper-writing` is
academic-paper-specific with a fixed section taxonomy (Abstract/
Introduction/Method/etc.), a mandatory claim-evidence alignment check
against experimental results, and a five-dimension adversarial
self-review before submission — no true duplicate, folded in as a
sibling domain with a cross-reference on both sides rather than merged.

Folded into `internal-writing-comms` (not a new top-level category) as
`references/research-paper-writing/SKILL.md` (+ its `references/` tree,
minus `agents/`). No name collision (`research-paper-writing` checked
against the full repo). Internal references are all relative to the
skill's own folder and needed no fixing.

Not added to the Universal table: scoped to explicit paper-drafting/
revision requests.
=======================================================================

THIRD-PARTY IMPORT — Humanizer-zh-TW (kevintsai1202, MIT license),
2026-08-16. Full license text and attribution: THIRD-PARTY-LICENSES.md.

Source repo (github.com/kevintsai1202/Humanizer-zh-TW) ships one skill,
a single `SKILL.md` (no bundled references/scripts). Its own metadata
records its lineage: a Traditional-Chinese fork of op7418/humanizer-zh,
itself translated from blader/humanizer, cross-referencing
hardikpandya/stop-slop. Read in full: it is a prose-editing pattern
catalog based on Wikipedia's "Signs of AI writing" page (maintained by
WikiProject AI Cleanup) — puffery/false-significance phrasing, promotional
language, vague attribution, em-dash overuse, the rule-of-three, filler
phrases, sycophantic tone, generic positive closers, etc. — with
before/after rewrite examples and a 5-dimension 50-point quality rubric,
all written in Traditional Chinese.

**Explicitly distinguished from detection evasion**: this skill's stated
job is writing-quality improvement (removing generic/robotic LLM prose
patterns, adding authorial voice) — it makes no claim about defeating an
AI-content detector, and it does not touch watermarks, C2PA/provenance
metadata, or any statistical/cryptographic marking. That distinction is
the reason this import was accepted the same day a different offered
source (`guillaumemeyer/watermarks-remover`, whose stated purpose
includes "anti-detect clean AI output" and stripping vendor provenance
marks) was declined — see the note immediately below.

Compared against `internal-writing-comms/writing-shape`: `writing-shape`
shapes raw material into an article structure or restructures an
existing draft section-by-section; this skill operates at the sentence/
phrase level on a finished draft to remove specific LLM tells — adjacent
but distinct passes, no duplicate, cross-reference added on both sides.

Folded into `internal-writing-comms` (not a new top-level category) as
`references/humanizer-zh-tw/SKILL.md`. No name collision
(`humanizer-zh-tw` checked against the full repo, and against the
frontmatter name `humanizer-zh-tw` specifically).

Not added to the Universal table: scoped to explicit text-editing
requests.
=======================================================================

DECLINED (not imported) — guillaumemeyer/watermarks-remover, evaluated
2026-08-16 alongside the four imports above (same user request, same
"add + merge + reinstall" ask). Full reasoning kept here rather than in
a THIRD-PARTY IMPORT section because nothing was copied into the repo.

Source repo (github.com/guillaumemeyer/watermarks-remover) ships one
skill, `skills/remove-ai-marks/SKILL.md`, backed by a separate HTTP
service (`service/`) with heavy backends (CtrlRegen, MarkDiffusion,
MarkLLM, a SynthID scorer) for stripping AI-provenance signals: invisible
Unicode markers, statistical token-sampling watermarks (via LLM-driven
paraphrase/back-translate/humanize rewrite passes), and C2PA/EXIF/XMP/
container metadata across PNG/JPEG/WebP/SVG/PDF/DOCX/ODT/HTML/MD. Read
the skill's SKILL.md and `references/ethics.md` in full before deciding.

The skill's own trigger language is explicit: "anti-detect clean AI
output" is listed as a first-class use case in its own frontmatter
description, and its workflow always offers a rewrite pass specifically
to defeat statistical/watermark-based AI-content detection. `ethics.md`
does list "academic fraud" and "circumventing lawful transparency or
platform disclosure rules" as "Not appropriate" uses, and instructs the
agent to warn (not necessarily refuse) in those cases while "still only
perform[ing] technical cleaning they own" — i.e. the disclaimer shifts
liability without gating the actual capability. C2PA Content Credentials
and Google's SynthID exist specifically as content-provenance/
transparency mechanisms; a general-purpose, always-available skill whose
core function is removing those signals from arbitrary content is, in
substance, a detection-evasion tool regardless of the ethics section
appended to it.

Decision: declined per this environment's standing instruction to refuse
"detection evasion for malicious purposes," and because the disclaimer
does not change what the tool does — it remains usable, by design, to
strip AI-provenance signals from any content a user hands it, including
content someone has reason to misrepresent as human-written. This is
distinct from `Humanizer-zh-TW` (imported the same day, see above), whose
job is prose-quality editing with no watermark/metadata/provenance
component. Not merged into any existing skill, not added as a new
top-level category, and nothing from its source repo was copied in. The
user was told directly why in the same turn this decision was made.
=======================================================================

THIRD-PARTY IMPORT — AccessLint/skills (AccessLint, MIT license),
2026-08-16 (second batch, same day as the firecrawl/arxiv-skills/
research-paper-writing/Humanizer-zh-TW batch above but a separate user
request evaluated via user-directed comparison against installed skills —
see SKILL-AUDIT.md's "續" section for the full methodology). Full license
text and attribution: THIRD-PARTY-LICENSES.md.

Source repo (github.com/AccessLint/skills) ships a Claude Code plugin
(.claude-plugin/plugin.json, version 0.10.2) with 5 skills under skills/:
accessibility-audit, accessibility-scan, accessibility-inspect,
accessibility-diff, accessibility-fix, plus a shared/methodology.md all
5 reference by relative path (../shared/methodology.md) and
accessibility-inspect's own references/checkpoints.md. The plugin's own
.mcp.json (read for its operational requirement, not copied in as skill
content) declares a required MCP server, accesslint (npx -y
@accesslint/mcp@latest), supplying list_rules/explain_rule/audit_html/
audit_live tools that accessibility-audit and accessibility-fix call
directly. Vendor root docs (README.md, CHANGELOG.md, docs/, benchmark/)
are the vendor's own marketing/benchmark scaffolding, not skill content —
not copied in.

Copied the entire skills/ subtree verbatim (all 5 skill folders + shared/
as siblings) specifically so the ../shared/methodology.md and
accessibility-inspect's references/checkpoints.md relative links resolve
with zero path rewriting — verified after the move (both files exist at
the expected relative paths).

Compared against nothing pre-existing in this repo: no accessibility/WCAG
skill existed before this import. No name collisions (all 5 frontmatter
names — accessibility-audit, accessibility-scan, accessibility-inspect,
accessibility-diff, accessibility-fix — checked against the full repo).

Folded into scaffolding-templating (not a new top-level category) as
references/design/accesslint/{accessibility-audit,accessibility-scan,
accessibility-inspect,accessibility-diff,accessibility-fix,shared}/,
listed in that skill's own new "Accessibility auditing, scanning,
inspecting & fixing (AccessLint)" table with the MCP-server requirement
called out prominently (not silently dropped like ordinary vendor
scaffolding, since it's operationally load-bearing).

Not added to the Universal table: all 5 are scoped to explicit
accessibility/WCAG/a11y requests, not "invoke before any response"
language.
=======================================================================

THIRD-PARTY IMPORT — bencium.io typography + relationship-design
(Bencium Limited, MIT license), 2026-08-16. Full license text and
attribution: THIRD-PARTY-LICENSES.md.

Two single-skill repos from the bencium.io Claude Code plugin
marketplace: typography/skills/typography/ (SKILL.md, css-templates.md,
html-entities.md) and relationship-design/skills/relationship-design/
(SKILL.md, CHECKLIST.md, EXAMPLES.md, REFERENCE.md). Each repo's own
.claude-plugin/plugin.json confirms author bencium.io; the batch's MIT
license text was taken from a sibling skill in the same marketplace
(eu-ai-act-reviewer/skills/eu-ai-act-reviewer/LICENSE — "Copyright (c)
2026 Bencium Limited"), since the two imported skills' own folders don't
vendor a LICENSE file individually. No vendor root docs copied in (README
etc.) per this repo's standing convention.

Naming-collision check on typography: the source's own frontmatter
already reads name: ui-typography (distinct from its folder name
typography) — the vendor had already disambiguated from the generic
word before this import. A full-repo grep for name: typography and a
folder literally named typography found no existing collision either
way, but this repo's own folder was named ui-typography anyway, to keep
the folder name and frontmatter name: field consistent with each other
(the same folder-matches-frontmatter convention `prototype-variants`
established on 2026-08-09) rather than because of an actual clash.
relationship-design had no collision (folder or frontmatter) — its own
frontmatter name: field is an unusual non-slug string ("Agentic UX
Design - Relationship-Centric Interfaces"), left as shipped since fixing
vendor frontmatter format isn't this repo's convention absent an actual
collision.

Universal-tier check: ui-typography's own description reads "auto-apply
every rule in this skill silently... even if the user doesn't mention
typography... whenever generating UI output" — broader-scoped than any
existing Universal-table entry, structurally identical in kind to the
ip-guard case from 2026-08-02. Per that precedent, NOT unilaterally added
to the Universal table — flagged instead in scaffolding-templating's own
SKILL.md and the root SKILL.md's Universal-table intro note, defaulting
to explicit-request triggering like every other domain in this skill,
since elevating it would add typography-enforcement overhead to every
future UI-generating turn across every project on this machine.
relationship-design's own frontmatter explicitly scopes itself to
"ONLY use when specifically asked" — unambiguously not universal.

Folded into scaffolding-templating (not a new top-level category) as
references/design/{ui-typography,relationship-design}/, listed in a new
"Typography & agentic UX philosophy (bencium.io)" table.
=======================================================================

THIRD-PARTY IMPORT — NousResearch/hermes-agent popular-web-designs +
design-md + baoyu-infographic (Nous Research, MIT license; baoyu-
infographic additionally credits 宝玉/JimLiu as original author),
2026-08-16. Full license text and attribution: THIRD-PARTY-LICENSES.md.

Source repo (github.com/NousResearch/hermes-agent) ships a large
skills/creative/ folder; only 3 of its skills were in scope for this
batch (the others — claude-design, p5js, sketch, etc. — were evaluated
and left uninstalled as redundant with existing skills, see
SKILL-AUDIT.md): popular-web-designs/ (SKILL.md + templates/, 54 real
design-system files), design-md/ (SKILL.md + templates/starter.md),
baoyu-infographic/ (SKILL.md + PORT_NOTES.md + references/ tree:
analysis-framework.md, base-prompt.md, structured-content-template.md,
layouts/ [21 files], styles/ [21 files]). Copied each folder's full
contents as-is; PORT_NOTES.md (the porter's own adaptation notes, not
vendor marketing) was kept since it documents baoyu-infographic's own
port-specific decisions, unlike a generic README/CHANGELOG.

baoyu-infographic's own frontmatter records author: 宝玉 (JimLiu),
license: MIT, homepage github.com/JimLiu/baoyu-skills — it was itself
adapted BY hermes-agent/Nous Research from that original source, not
authored fresh by Nous Research. Attributed both: the hermes-agent repo's
MIT license covers the adaptation/repo as a whole, and 宝玉/JimLiu is
credited by name as the original author in THIRD-PARTY-LICENSES.md,
mirroring the multi-author attribution pattern already used for the
Shubham Saboo / Matt Van Horn awesome-llm-apps batch. popular-web-designs'
own frontmatter similarly credits "Hermes Agent + Teknium (design systems
sourced from VoltAgent/awesome-design-md)" — also noted in
THIRD-PARTY-LICENSES.md and in scaffolding-templating/SKILL.md's own
domain-table row.

**Naming/collision note — design-md vs. the already-installed
stitch-skill**: both ultimately produce a "DESIGN.md"-shaped artifact and
sit in the same design-reference cluster, but are not duplicates —
stitch-skill (from the 2026-08-05 taste-skill import) emits Stitch-
specific natural-language visual-description prose for Google Stitch's
screen generator, no formal spec, no CLI; design-md authors/lints/diffs/
exports Google's actual open, versioned DESIGN.md spec
(google-labs-code/design.md, Apache-2.0) via a real npm CLI
(@google/design.md — WCAG contrast linting, Tailwind/DTCG export). Kept
as two separate files, not merged; a disambiguation note was added to
both scaffolding-templating/SKILL.md's new domain-table section and its
"How to use this skill" list (point 11) so a future reader doesn't assume
they're duplicates. No actual name collision either way: design-md's own
folder/frontmatter name: field checked against the full repo, none found.
popular-web-designs and baoyu-infographic likewise checked, no
collisions.

Folded into scaffolding-templating (not a new top-level category) as
references/design/{popular-web-designs,design-md,baoyu-infographic}/,
listed in a new "Design reference catalogs & spec generators
(NousResearch/hermes-agent)" table.

Not added to the Universal table: all 3 are scoped to explicit
design-catalog/token-spec/infographic requests.
=======================================================================

SAME-DAY RESYNC (not a new import) — vercel-react-view-transitions,
2026-08-16, alongside the batch above. The already-installed
library-api-reference/references/vercel-react-view-transitions/ (from
the vercel-labs/agent-skills THIRD-PARTY IMPORT recorded further above)
was compared file-by-file against the same upstream repo's current
skills/react-view-transitions/ and found stale: README.md, SKILL.md, and
references/nextjs.md had each gained content upstream since the original
import (router.push(href, { transitionTypes }) API documentation, a
"When Content Must Be Ready" prefetching/caching section, and a "Shared
Element Readiness" subsection). AGENTS.md, metadata.json, and the other 3
references/ files were byte-identical, no change needed. Overwrote the
3 stale files with the upstream versions; re-diffed afterward to confirm
zero remaining differences. No new THIRD-PARTY-LICENSES.md entry — this
is a refresh of already-licensed content, not new material.
=======================================================================

THIRD-PARTY IMPORT — 9 user-directed precision extractions/whole-skill
installs, spanning bencium-marketplace and hermes-agent, 2026-08-16
(third same-day batch — see SKILL-AUDIT.md's "2026-08-16（三）" section
for the full per-item reasoning). Full license text: THIRD-PARTY-
LICENSES.md (extends the existing "bencium.io" and "NousResearch —
hermes-agent" sections rather than adding new dated blocks, since both
sources were already vendored earlier the same day).

Unlike every batch above, this one was not "clone a repo, evaluate it
whole, decide what to keep" — the user had already seen a full prior
comparison of both source repos against this repo's installed skills and
specified exactly 9 surgical actions: 4 whole-skill installs and 5
fragment-extractions. Each is summarized here; see SKILL-AUDIT.md for the
full extracted-vs-discarded reasoning per item.

**Whole-skill installs (4, each a new sub-domain SKILL.md file):**
- `p5js` (hermes-agent, MIT) → scaffolding-templating/references/design/p5js/
  — full SKILL.md + references/ (10 files) + templates/viewer.html +
  scripts/ (4 files: setup.sh, serve.sh, render.sh, export-frames.js —
  all read in full, standard puppeteer/ffmpeg pipeline, no
  network-exfiltration or obfuscation patterns found). Source's own
  README.md dropped per this repo's standing SKILL.md-is-the-only-index
  convention (it only restated the SKILL.md's own File Structure/Modes
  tables).
- `sketch` (hermes-agent, MIT — single SKILL.md file, no
  references/templates subtree in the source) →
  scaffolding-templating/references/design/sketch/. Two-author note: the
  skill's own "Attribution" section credits it as adapted from the GSD
  (Get Shit Done) project's `/gsd-sketch` workflow, MIT (c) 2025 Lex
  Christopherson (github.com/gsd-build/get-shit-done, now archived) —
  both hermes-agent and Lex Christopherson are credited in
  THIRD-PARTY-LICENSES.md's hermes-agent section for this file.
- `insurgent-campaign` (bencium.io, MIT) →
  marketing/references/research-strategy/insurgent-campaign/ — full
  SKILL.md + references/ (7 files: asymmetry-audit-table.md,
  authenticity-playbook.md, campaign-archetypes.md,
  channel-tier-stack.md, hungarian-case-study.md, lift-test-templates.md,
  sector-riders.md). Source's own root README.md dropped per convention.
- `loyalty-mindset` (extracted from bencium.io's `human-architect-mindset`,
  MIT) → agentic-dev-workflow/references/loyalty-mindset/SKILL.md — a
  new condensed standing-reference file, judged the better fit than
  cramming a philosophical framing into agentic-dev-workflow/SKILL.md's
  own dense, routing-only table structure (same precedent as
  karpathy-guidelines). Only the "Loyalty" foundation section (The AI
  Perfection Trap, The Human Moat, the Loyalty Question, 5 named
  anti-patterns from REFERENCE.md, the Loyalty Decision Matrix, and the
  Betrayal Test from CHECKLIST.md's Phase 0) was extracted — the source
  skill's Domain Modeling / Systems Thinking / Constraint Navigation /
  AI-Aware Decomposition pillars and its Spec-Driven-Development
  extension were left uninstalled as duplicates of this repo's own
  `domain-modeling`, `brainstorming`, and `code-quality-review`'s
  `codebase-design`.

**Fragment extractions (5, folded into existing files, 0 new sub-domain
files):**
- The "Surface-First" 7-archetype naming step from hermes-agent's
  `claude-design` (MIT) → new early section in
  scaffolding-templating/references/design/frontend-design/SKILL.md,
  placed right before its existing "Process" section. `claude-design`'s
  own diagnostic slop-scoring and hosted-tool-plumbing removal logic were
  left uninstalled (redundant with this skill and `web-artifacts-builder`,
  as already noted in the 2026-08-16（續） section above).
- The glassmorphism ban from bencium.io's `bencium-innovative-ux-designer`
  (MIT) → used to **flip** an existing, now-contradictory recommendation
  in the already-installed
  scaffolding-templating/references/design/redesign-skill/SKILL.md, whose
  "Surface Upgrades" section previously recommended "True glassmorphism"
  as an upgrade technique. Replaced with a ban plus a note explaining the
  reversal and citing the bencium source. **Deliberately not applied to
  `hallmark`** even though the same prior comparison found hallmark's own
  material treats glassmorphism as contextually appropriate for an
  Apple-adjacent brand — out of scope per the user's explicit
  instruction; flagged as a known, intentionally-unresolved tension in
  scaffolding-templating/SKILL.md's "How to use this skill" point 13
  rather than silently left invisible.
- The "Creative Reframing Prompts" (Designer lens / Context shift / Era
  lens) from bencium.io's `bencium-impact-designer` (MIT) → new optional
  §0.E in the already-installed
  scaffolding-templating/references/design/taste-skill/SKILL.md, framed
  as a lateral-thinking nudge, not a mandatory rule. That skill's 40-name
  aesthetic-studio catalog and its dice-roll "Force Variety" mechanism
  were left uninstalled as overlapping with taste-skill's own 3-dial
  system.
- The doc-grounded, phased/approval-gated workflow from bencium.io's
  `design-audit` (MIT) → new "Alternate mode" section appended to the
  already-installed
  scaffolding-templating/references/design/hallmark/references/verbs/audit.md,
  triggered only when a project actually has
  DESIGN_SYSTEM.md/FRONTEND_GUIDELINES.md/APP_FLOW.md/PRD.md/
  TECH_STACK.md/LESSONS.md present — explicitly an alternate, stricter
  mode of the same `audit` verb, not a replacement for its default flat-
  severity-list behavior. `design-audit`'s own 14-dimension checklist was
  left uninstalled as pure duplication of the dimension table already in
  that same audit.md file.
- The "Authority Level Determines Strategy" table (Challenger vs.
  Established, including the Rank-5/Rank-1 Princeton data point) from
  bencium.io's `bencium-aeo` (MIT) → new supplementary section in the
  already-installed
  marketing/references/paid-acquisition/ai-seo/SKILL.md, placed directly
  after the existing Princeton GEO 9-method table, explicitly additive to
  (not replacing) that skill's existing freshness/citation/query-testing
  guidance.

**Naming-collision checks**: `p5js`, `sketch`, and `insurgent-campaign`
(both folder name and frontmatter `name:`) grepped against the full repo
— no collisions found (the word "sketch" appears elsewhere only as
ordinary prose, e.g. in `hallmark`'s own component docs and various
"sketch this UI" trigger examples, never as a skill folder/frontmatter
name).

**Universal-tier check**: none of the 4 new files or 5 fragments carry
"invoke before any response" language — every one is scoped to an
explicit design/marketing/architecture-decision request. Not added to
the Universal table.

Folded into 3 existing top-level skills (not a new category):
scaffolding-templating (`p5js`, `sketch`, plus the frontend-design/
redesign-skill/taste-skill/hallmark fragment edits), marketing
(`insurgent-campaign`, plus the ai-seo fragment edit), agentic-dev-workflow
(`loyalty-mindset`).
=======================================================================
-->

