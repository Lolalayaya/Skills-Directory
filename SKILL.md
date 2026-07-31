---
name: skills-directory
description: "Master index of every custom skill in this workspace (18 top-level skills, holding 160 sub-domains, consolidated/curated from 137 originally-installed skills plus a later third-party import). Consult this FIRST whenever unsure which skill covers a need, when a task might span more than one skill, or to sanity-check what capabilities exist here at all. Several entries are marked UNIVERSAL — standing triggers (start-of-conversation skill discovery, brainstorming before creative work, verification before claiming completion, TDD, code-security review) that should fire on essentially every relevant turn, not only when explicitly asked for."
---

# Skills Directory

One-stop map of this workspace's 18 skills. Each row's "Full skill" links straight to that skill's own `SKILL.md`, which then routes further into its `references/<domain>/SKILL.md`.

## 🔁 Universal — apply these without being asked

These sub-domains carry "always / before any / MUST" language in their own source material. Don't wait for the user to invoke them by name. (A 2026-07-31 audit of a newly-imported third-party pack, `mattpocock-skills`, checked all 30 of its sub-domains for this same language and found none — see `SKILL-AUDIT.md`. This list is unchanged by that import.)

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
| Keep a long task's plan/progress on disk across sessions and `/clear`, or turn a recurring pattern into a workflow spec | `business-automation` |
| Create/edit .docx/.xlsx/.pptx/.pdf, build an MCP server, write React/Next.js/React Native code | `library-api-reference` |
| Build a banner/logo/slide deck/theme, set up a design system, review UI or writing style, scaffold pages from templates | `scaffolding-templating` |
| Review code for quality/SOLID/security (two frameworks available), run Semgrep, request/receive a code review, scan for deep-module opportunities, set up quality-gate hooks | `code-quality-review` |
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
| 2 | `product-verification` | Prove work actually works before claiming done | 3 |
| 3 | `data-analysis` | Metrics-driven optimization (Vercel only, for now) | 1 |
| 4 | `business-automation` | Persistent file-based task planning across sessions, plus workflow-spec design | 4 (1 core +2 language variants +1 from third-party import) |
| 5 | `library-api-reference` | Office file formats, MCP building, Vercel/React APIs | 9 |
| 6 | `scaffolding-templating` | Templates/scaffolds — general + full design system | 16 |
| 7 | `code-quality-review` | Code review (two frameworks), static analysis, secure coding, architecture scanning | 12 — see comment block below |
| 8 | `cicd-deployment` | Deploy to Vercel, interactive or CI | 2 |
| 9 | `incident-runbooks` | Systematic debugging + diagnostic write-ups + issue triage | 3 |
| 10 | `infrastructure-ops` | Interactive setup/migration wizard (day-to-day ops still unfilled) | 1 |
| 11 | `marketing` | Full-funnel marketing, 5 internal sub-groups | 47 |
| 12 | `skill-authoring` | Build/audit/optimize skills themselves | 5 |
| 13 | `personal-learning` | Book study, knowledge base, Socratic tutor, multi-session course workspace | 4 |
| 14 | `agentic-dev-workflow` | Brainstorm → plan → isolate → execute → finish branch, plus interview-driven planning and git/session mechanics | 22 — see comment block below |
| 15 | `openspec-workflow` | OpenSpec change lifecycle | 5 |
| 16 | `deep-research` | Generic outline-driven research pipeline (Chinese), plus single-question background lookup | 6 |
| 17 | `internal-writing-comms` | Doc co-authoring, internal comms formats, article drafting/editing, questionnaires | 5 |
| 18 | `context-engineering-collection` | Context/harness engineering, multi-agent systems (untouched, never split) | 16 |

Total: 160 sub-domains across the 17 non-`context-engineering-collection` skills + `context-engineering-collection`'s own 16 (never touched by the consolidation) = 176 sub-skill-level `SKILL.md` files. History: 137 originally installed → −7 removed at the 2026-07-31 health check → 130 → +30 from importing and distributing the third-party `mattpocock-skills` pack the same day (MIT license, Matt Pocock — see [`THIRD-PARTY-LICENSES.md`](THIRD-PARTY-LICENSES.md)) → 160. Full reasoning for every addition/removal/merge: `SKILL-AUDIT.md`.

## How to use this index

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

product-verification (3):
  webapp-testing, verification-before-completion, test-driven-development
  (test-driven-development absorbed mattpocock-skills' tdd — see
  THIRD-PARTY IMPORT below)

data-analysis (1):
  vercel-optimize

business-automation (4, was 3 after the 2026-07-31 removals, +1 from the
  third-party import):
  planning-with-files, planning-with-files-zh, planning-with-files-zht,
  loop-me

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

code-quality-review (12, was 6, +6 from the third-party import):
  code-review-expert, semgrep, code-security, llm-security,
  requesting-code-review, receiving-code-review, code-review,
  improve-codebase-architecture, codebase-design, design-an-interface,
  setup-ts-deep-modules, setup-pre-commit

cicd-deployment (2):
  deploy-to-vercel, vercel-cli-with-tokens

incident-runbooks (3, was 1, +2 from the third-party import):
  systematic-debugging (absorbed mattpocock-skills' diagnosing-bugs —
  see THIRD-PARTY IMPORT below), triage, qa

infrastructure-ops (1, was 0 placeholder, +1 from the third-party
  import):
  wizard

agentic-dev-workflow (22, was 8, +14 from the third-party import):
  brainstorming, dispatching-parallel-agents, executing-plans,
  subagent-driven-development, using-superpowers, writing-plans,
  using-git-worktrees, finishing-a-development-branch,
  ask-matt, grilling, grill-me, grill-with-docs, domain-modeling,
  to-spec, to-tickets, wayfinder, request-refactor-plan, prototype,
  setup-matt-pocock-skills, handoff, resolving-merge-conflicts,
  git-guardrails-claude-code

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
Total accounted for: 15+3+1+4+9+16+12+2+3+1+22+5+6+5+47+5+4 = 160
Plus context-engineering-collection: kept independent, never split
  (originally installed as one skill covering 17 internal sub-skills,
  now 16 after the REMOVALS below; re-wrapping it would have added no
  value).
160 sub-domains across 17 skills + context-engineering-collection's own
16 = 176 sub-skill-level SKILL.md files, down from 137 + 30 = 167
originally-installed-or-imported skill units after 7 removals from the
first batch (see REMOVALS below) — the 176 vs 167 discrepancy is because
"sub-domains" here counts each merge target once even where 2+ original
skills fed into it (test-driven-development, systematic-debugging,
writing-shape each absorbed one or two others' unique content without
becoming a second file).

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
-->
