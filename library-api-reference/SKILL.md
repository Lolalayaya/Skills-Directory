---
name: library-api-reference
description: "Reference for correctly using specific third-party libraries, file formats, SDKs, and CLIs — Office documents (.docx/.xlsx/.pptx/.pdf), MCP server building, and Vercel/React APIs (performance best practices, React Native, View Transitions, composition patterns). Always consult this BEFORE writing code against one of these libraries — it holds the reference snippets, version-specific gotchas, and common mistakes needed to avoid outdated patterns or wrong function signatures. Use whenever the user mentions creating/editing/reading .docx/.xlsx/.pptx/.pdf files, building an MCP server, or writing/reviewing React/Next.js/React Native code — even if they don't name the library explicitly. For browser-automation libraries (fetch, functions, WebMCP, browser-use/Stagehand), see `browser-automation` instead."
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
| React View Transitions | `<ViewTransition>`, `addTransitionType`, CSS view-transition pseudo-elements | [references/vercel-react-view-transitions/SKILL.md](references/vercel-react-view-transitions/SKILL.md) |
| React composition patterns | Compound components, render props, context providers — React 19 API changes | [references/vercel-composition-patterns/SKILL.md](references/vercel-composition-patterns/SKILL.md) |

## How to use this skill

1. Identify which domain the task touches (a task can span more than one — e.g. "build an MCP server that returns a generated .xlsx" uses both `mcp-builder` and `xlsx`).
2. Open that domain's `SKILL.md` and follow it — most bundle their own `scripts/`, `references/`, and `assets/` (templates, schemas, code samples) one level deeper; read those only when the domain's SKILL.md points you there (progressive disclosure — don't preload everything).
3. If a domain's guide references a script, run it rather than hand-rolling the equivalent — that's the point of bundling it.

## Cross-domain gotchas worth keeping in working memory

- **Never infer one language's SDK/API shape from another's** — each domain's reference exists specifically because those shapes differ in non-obvious ways.
- **Office file domains (docx/xlsx/pptx/pdf) are format-specific** — don't cross-apply a docx templating trick to pptx; each has its own SKILL.md for a reason.
- **Vercel/React domains overlap with `cicd-deployment` and `scaffolding-templating`** — this skill covers *how the API/library works*; deploying it is `cicd-deployment`, and visual/design conventions are `scaffolding-templating`.
- **Browser/automation libraries live in `browser-automation`**, not here — `fetch`, Browserbase `functions`, WebMCP generation, and the browser-use→Stagehand migration guide all moved there since they share Browserbase's tool family.
