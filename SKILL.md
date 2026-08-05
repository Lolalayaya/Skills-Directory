---
name: skills-directory
description: "Master index of every custom skill in this workspace (18 top-level skills, holding 179 sub-domains, consolidated/curated from 137 originally-installed skills plus several later third-party imports). Consult this FIRST whenever unsure which skill covers a need, when a task might span more than one skill, or to sanity-check what capabilities exist here at all. Several entries are marked UNIVERSAL — standing triggers (start-of-conversation skill discovery, brainstorming before creative work, verification before claiming completion, TDD, code-security review) that should fire on essentially every relevant turn, not only when explicitly asked for."
---

# Skills Directory

One-stop map of this workspace's 18 skills. Each row's "Full skill" links straight to that skill's own `SKILL.md`, which then routes further into its `references/<domain>/SKILL.md`.

## 🔁 Universal — apply these without being asked

These sub-domains carry "always / before any / MUST" language in their own source material. Don't wait for the user to invoke them by name. (A 2026-07-31 audit of a newly-imported third-party pack, `mattpocock-skills`, checked all 30 of its sub-domains for this same language and found none — see `SKILL-AUDIT.md`. This list is unchanged by that import. A 2026-08-02 import, `ip-guard`, reads as broader "invoke before any code/content generation" language than any entry below, but was explicitly kept OUT of this table per the user's own scoping decision — see `SKILL-AUDIT.md` for the full reasoning.)

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
| Prove a fix/feature actually works (Playwright), apply the verification/TDD discipline, or ban truncated/placeholder output | `product-verification` |
| Figure out why a deployed (Vercel) app is slow/expensive from real metrics | `data-analysis` |
| Keep a long task's plan/progress on disk across sessions and `/clear`, or turn a recurring pattern into a workflow spec | `business-automation` |
| Create/edit .docx/.xlsx/.pptx/.pdf, build an MCP server, write React/Next.js/React Native code | `library-api-reference` |
| Build a banner/logo/slide deck/theme, set up a design system, review UI or writing style, scaffold pages from templates, or make a frontend build stop looking like generic AI output | `scaffolding-templating` |
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
| Co-author a doc/proposal/spec, write internal company comms, draft/edit an article from raw material, or delegate unanswerable questions as a questionnaire | `internal-writing-comms` |
| Design/optimize/debug an agent system's context management, harness, or multi-agent architecture | `context-engineering-collection` |

## Full skill list

| # | Skill | One-line summary | Sub-domains inside |
|---|---|---|---|
| 1 | `browser-automation` | Browserbase toolkit: drive/test/automate a browser, plus B2B research/prospecting | 15 — see comment block below |
| 2 | `product-verification` | Prove work actually works before claiming done, plus full-output enforcement | 4 |
| 3 | `data-analysis` | Metrics-driven optimization (Vercel only, for now) | 1 |
| 4 | `business-automation` | Persistent file-based task planning across sessions, plus workflow-spec design | 5 (1 core +2 language variants +2 from third-party imports) |
| 5 | `library-api-reference` | Office file formats, MCP building, Vercel/React APIs | 9 |
| 6 | `scaffolding-templating` | Templates/scaffolds — general + full design system + anti-AI-slop frontend taste systems | 28 |
| 7 | `code-quality-review` | Code review (two frameworks), static analysis, secure coding, IP/license + dependency-security guardrails, architecture scanning | 14 — see comment block below |
| 8 | `cicd-deployment` | Deploy to Vercel, interactive or CI | 2 |
| 9 | `incident-runbooks` | Systematic debugging + diagnostic write-ups + issue triage | 4 |
| 10 | `infrastructure-ops` | Interactive setup/migration wizard (day-to-day ops still unfilled) | 1 |
| 11 | `marketing` | Full-funnel marketing, 5 internal sub-groups | 47 |
| 12 | `skill-authoring` | Build/audit/optimize skills themselves | 5 |
| 13 | `personal-learning` | Book study, knowledge base, Socratic tutor, multi-session course workspace | 4 |
| 14 | `agentic-dev-workflow` | Brainstorm → plan → isolate → execute → finish branch, plus interview-driven planning, git/session mechanics, and a condensed coding-discipline reference | 24 — see comment block below |
| 15 | `openspec-workflow` | OpenSpec change lifecycle | 5 |
| 16 | `deep-research` | Generic outline-driven research pipeline (Chinese), plus single-question background lookup | 6 |
| 17 | `internal-writing-comms` | Doc co-authoring, internal comms formats, article drafting/editing, questionnaires | 5 |
| 18 | `context-engineering-collection` | Context/harness engineering, multi-agent systems (untouched, never split) | 16 |

Total: 179 sub-domains across the 17 non-`context-engineering-collection` skills + `context-engineering-collection`'s own 16 (never touched by the consolidation) = 195 sub-skill-level `SKILL.md` files. History: 137 originally installed → −7 removed at the 2026-07-31 health check → 130 → +30 from importing and distributing the third-party `mattpocock-skills` pack the same day (MIT license, Matt Pocock — see [`THIRD-PARTY-LICENSES.md`](THIRD-PARTY-LICENSES.md)) → 160 → +1 from importing forrestchang's third-party `andrej-karpathy-skills` pack on 2026-08-01 (single skill, `karpathy-guidelines`, folded into `agentic-dev-workflow` — see [`THIRD-PARTY-LICENSES.md`](THIRD-PARTY-LICENSES.md)) → 161 → +4 from importing 4 of the 5 skills in Shubham Saboo's third-party `awesome-llm-apps` repo's `agent_skills/` folder on 2026-08-01 (Apache-2.0 license — see [`THIRD-PARTY-LICENSES.md`](THIRD-PARTY-LICENSES.md)): `commit-archaeologist` → `incident-runbooks`, `project-graveyard` → `business-automation`, `scope-creep-detector` → `code-quality-review`, `thinking-out-loud` → `agentic-dev-workflow` (the 5th, `advisor-orchestrator-worker`, was excluded as redundant with this environment's native `Workflow` tool) → 165 → +1 from importing Mugdha Vairagade's third-party `claude-skill-ip-guard` on 2026-08-02 (Apache-2.0 license, single skill `ip-guard`, folded into `code-quality-review` — see [`THIRD-PARTY-LICENSES.md`](THIRD-PARTY-LICENSES.md)) → 166 → +12 from importing Leonxlnx's third-party `taste-skill` pack on 2026-08-05 (MIT license, 12 sub-skills, 11 folded into `scaffolding-templating` and 1 — `output-skill` — folded into `product-verification` since it isn't a design skill — see [`THIRD-PARTY-LICENSES.md`](THIRD-PARTY-LICENSES.md)) → 178 → +1 from importing Nutlope's third-party `hallmark` on 2026-08-05 (MIT license, single skill, folded into `scaffolding-templating` — see [`THIRD-PARTY-LICENSES.md`](THIRD-PARTY-LICENSES.md)) → 179. Full reasoning for every addition/removal/merge: `SKILL-AUDIT.md`.

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

browser-automation (15, was 17 — see REMOVALS below):
  agent-experience, autobrowse, browser, browser-to-api, browser-trace,
  company-research, competitor-analysis, competitor-profiling,
  cookie-sync, event-prospecting, fetch, functions, search, ui-test,
  webmcp-gen

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

library-api-reference (9):
  docx, xlsx, pptx, pdf, mcp-builder, vercel-react-best-practices,
  vercel-react-native-skills, vercel-react-view-transitions,
  vercel-composition-patterns

scaffolding-templating (28, was 16 after the REMOVALS below, +12 from the
  taste-skill import, +1 from the hallmark import):
  programmatic-seo, design, design-system, ui-styling, ui-ux-pro-max,
  banner-design, brand, anthropic-brand-guidelines (renamed from
  brand-guidelines), canvas-design, algorithmic-art, theme-factory,
  frontend-design, web-artifacts-builder, web-design-guidelines,
  writing-guidelines, slides, taste-skill, taste-skill-v1, brandkit,
  brutalist-skill, gpt-tasteskill, image-to-code-skill,
  imagegen-frontend-mobile, imagegen-frontend-web, minimalist-skill,
  redesign-skill, soft-skill, stitch-skill, hallmark

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

agentic-dev-workflow (24, was 8, +14 from the mattpocock-skills import,
  +1 from the andrej-karpathy-skills import, +1 from the awesome-llm-apps
  import):
  brainstorming, dispatching-parallel-agents, executing-plans,
  subagent-driven-development, using-superpowers, writing-plans,
  using-git-worktrees, finishing-a-development-branch,
  ask-matt, grilling, grill-me, grill-with-docs, domain-modeling,
  to-spec, to-tickets, wayfinder, request-refactor-plan, prototype,
  setup-matt-pocock-skills, handoff, resolving-merge-conflicts,
  git-guardrails-claude-code, karpathy-guidelines, thinking-out-loud

openspec-workflow (5):
  openspec-apply-change, openspec-archive-change, openspec-explore,
  openspec-propose, openspec-sync-specs

deep-research (6, was 5, +1 from the third-party import):
  research, research-add-fields, research-add-items, research-deep,
  research-report, background-research (renamed from mattpocock-skills'
  research to avoid colliding with this skill's own "research" pipeline
  stage)

internal-writing-comms (5, was 2, +3 from the third-party import):
  doc-coauthoring, internal-comms, writing-fragments, writing-shape
  (absorbed writing-beats + edit-article — see THIRD-PARTY IMPORT
  below), to-questionnaire

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

skill-authoring (5, was 4, +1 from the third-party import):
  skill-creator, skill-forge, skill-review, writing-skills,
  writing-great-skills

personal-learning (4, was 3, +1 from the third-party import):
  book-study, wiki-ingest, sigma, teach

-----------------------------------------------------------------------
Total accounted for: 15+4+1+5+9+28+14+2+4+1+24+5+6+5+47+5+4 = 179
Plus context-engineering-collection: kept independent, never split
  (originally installed as one skill covering 17 internal sub-skills,
  now 16 after the REMOVALS below; re-wrapping it would have added no
  value).
179 sub-domains across 17 skills + context-engineering-collection's own
16 = 195 sub-skill-level SKILL.md files, down from 137 + 30 + 1 + 4 + 1 +
12 + 1 = 186 originally-installed-or-imported skill units after 7
removals from the first batch (see REMOVALS below) — the 195 vs 186
discrepancy is because "sub-domains" here counts each merge target once
even where 2+ original skills fed into it (test-driven-development,
systematic-debugging, writing-shape each absorbed one or two others'
unique content without becoming a second file).

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
-->

