---
name: library-api-reference
description: "Reference for correctly using specific third-party libraries, file formats, SDKs, and CLIs — Office documents (.docx/.xlsx/.pptx/.pdf), MCP server building, Vercel/React APIs (performance best practices, React Native, View Transitions, composition patterns), React Aria's headless accessible components and hooks, integrating the Firecrawl web-data SDK/REST API into application code, and fetching/converting arXiv papers to Markdown. Always consult this BEFORE writing code against one of these libraries — it holds the reference snippets, version-specific gotchas, and common mistakes needed to avoid outdated patterns or wrong function signatures. Use whenever the user mentions creating/editing/reading .docx/.xlsx/.pptx/.pdf files, building an MCP server, writing/reviewing React/Next.js/React Native code, building with React Aria/`react-aria-components`, wiring Firecrawl into product code, or fetching/converting an arXiv paper — even if they don't name the library explicitly. For browser-automation libraries (fetch, functions, WebMCP, browser-use/Stagehand, the Firecrawl CLI for one-off terminal use) see `browser-automation` instead."
---

# Library & API Reference

Router skill for "how do I use this library/API correctly, and what will trip me up." Each domain below is a self-contained reference with its own SKILL.md, scripts, and reference docs — read the linked file before writing code against that library. Do not guess function signatures or namespaces from memory; these references exist because training data goes stale.

Never summarize or paraphrase code snippets, function signatures, or gotcha tables from the referenced files — copy them verbatim into your working context. Compressing code destroys the one thing that makes it useful (see `context-engineering-collection`'s compression guidance: code and structured data must survive verbatim, unlike prose).

## Domains

| Domain | When to use | Full guide |
|---|---|---|
| Word documents | Create/edit/read `.docx`/`.dotx` — reports, letters, tracked changes, templates | [references/docx/SKILL.md](references/docx/SKILL.md) |
| Excel spreadsheets | Create/edit `.xlsx`/`.xlsm`/`.csv`/`.tsv` — formulas, formatting, charts, cleaning messy data | [references/xlsx/SKILL.md](references/xlsx/SKILL.md) |
| PowerPoint decks | Create/edit/extract `.pptx`/`.potx` — slide decks, pitch decks | [references/pptx/SKILL.md](references/pptx/SKILL.md) |
| PDF files | Read, extract, merge, split, rotate, watermark PDFs | [references/pdf/SKILL.md](references/pdf/SKILL.md) |
| MCP servers | Build a Model Context Protocol server that exposes tools to LLMs | [references/mcp-builder/SKILL.md](references/mcp-builder/SKILL.md) |
| React/Next.js performance | Vercel Engineering's performance guidelines for components, data fetching, bundling | [references/vercel-react-best-practices/SKILL.md](references/vercel-react-best-practices/SKILL.md) |
| React Native/Expo | Best practices for performant mobile apps, lists, animations, native modules | [references/vercel-react-native-skills/SKILL.md](references/vercel-react-native-skills/SKILL.md) |
| React View Transitions | `<ViewTransition>`, `addTransitionType`, `router.push(href, { transitionTypes })`, CSS view-transition pseudo-elements, shared-element readiness/prefetching for Next.js | [references/vercel-react-view-transitions/SKILL.md](references/vercel-react-view-transitions/SKILL.md) |
| React composition patterns | Compound components, render props, context providers — React 19 API changes | [references/vercel-composition-patterns/SKILL.md](references/vercel-composition-patterns/SKILL.md) |
| React Aria | Headless, unstyled accessible components (`react-aria-components`) and the lower-level `@react-aria/*` hooks — building a custom design system from scratch with deep WAI-ARIA coverage and heavy i18n (RTL, 30+ locales) | [references/react-aria/SKILL.md](references/react-aria/SKILL.md) |
| Firecrawl app integration (start here) | Choose fresh vs. existing project flow, pick the right endpoint (`/scrape`, `/search`, `/interact`), install the SDK, wire up `FIRECRAWL_API_KEY` | [references/firecrawl-build/SKILL.md](references/firecrawl-build/SKILL.md) |
| Firecrawl `/scrape` integration | Single-page extraction from a known URL — markdown, links, screenshots, structured output | [references/firecrawl-build-scrape/SKILL.md](references/firecrawl-build-scrape/SKILL.md) |
| Firecrawl `/search` integration | Discovery-first flows — query instead of URL, optional result hydration | [references/firecrawl-build-search/SKILL.md](references/firecrawl-build-search/SKILL.md) |
| Firecrawl `/interact` integration | Post-scrape browser actions in product code — clicks, forms, pagination, auth flows | [references/firecrawl-build-interact/SKILL.md](references/firecrawl-build-interact/SKILL.md) |
| Firecrawl onboarding | Get `FIRECRAWL_API_KEY`/SDK into a project for the first time, browser auth flow | [references/firecrawl-build-onboarding/SKILL.md](references/firecrawl-build-onboarding/SKILL.md) |
| arXiv paper lookup | Get a journal DOI from an arXiv ID, or find an arXiv ID from a title/keyword search | [references/arxiv-lookup/SKILL.md](references/arxiv-lookup/SKILL.md) |
| arXiv paper → Markdown | Fetch an arXiv paper (LaTeX source preferred, PDF fallback) and convert it to structured Markdown for implementation reference | [references/arxiv-doc-builder/SKILL.md](references/arxiv-doc-builder/SKILL.md) |

## How to use this skill

1. Identify which domain the task touches (a task can span more than one — e.g. "build an MCP server that returns a generated .xlsx" uses both `mcp-builder` and `xlsx`).
2. Open that domain's `SKILL.md` and follow it — most bundle their own `scripts/`, `references/`, and `assets/` (templates, schemas, code samples) one level deeper; read those only when the domain's SKILL.md points you there (progressive disclosure — don't preload everything).
3. If a domain's guide references a script, run it rather than hand-rolling the equivalent — that's the point of bundling it.

## Cross-domain gotchas worth keeping in working memory

- **Never infer one language's SDK/API shape from another's** — each domain's reference exists specifically because those shapes differ in non-obvious ways.
- **Office file domains (docx/xlsx/pptx/pdf) are format-specific** — don't cross-apply a docx templating trick to pptx; each has its own SKILL.md for a reason.
- **Vercel/React domains overlap with `cicd-deployment` and `scaffolding-templating`** — this skill covers *how the API/library works*; deploying it is `cicd-deployment`, and visual/design conventions are `scaffolding-templating`.
- **`react-aria` vs. `scaffolding-templating`'s `pick-ui-library`**: this domain covers *how to use* React Aria once it's the chosen library; whether to choose it over base-ui/Radix for a given project is `pick-ui-library`'s call, not this file's.
- **Browser/automation libraries live in `browser-automation`**, not here — `fetch`, Browserbase `functions`, WebMCP generation, and the browser-use→Stagehand migration guide all moved there since they share Browserbase's tool family.
- **`firecrawl-build*` vs. the `firecrawl-*` CLI skills in `browser-automation`**: same vendor, different job. The `firecrawl-build*` domains above are for writing Firecrawl into an application's own source code (choosing an SDK, an endpoint, wiring `.env`). One-off terminal use during the current session — "scrape this page for me right now," "search the web," "crawl this docs site" — is `browser-automation`'s `firecrawl-cli`/`firecrawl-scrape`/`firecrawl-search`/etc. instead. Both installed by the same `firecrawl-cli init --all --browser` command in the source project, so a session may legitimately need both.
- **`arxiv-doc-builder` vs. `pdf`**: `arxiv-doc-builder` is arXiv-specific — it fetches a paper by ID (preferring LaTeX source over PDF, since pandoc-from-LaTeX preserves math/structure that PDF extraction loses) and is optimized for implementation-reference reading. Reach for the general `pdf` domain instead when the source is an arbitrary PDF with no arXiv id, or when the task is merge/split/rotate/watermark rather than paper-to-Markdown conversion.
