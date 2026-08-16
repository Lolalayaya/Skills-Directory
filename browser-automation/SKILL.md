---
name: browser-automation
description: "Full Browserbase-based browser automation toolkit — drive/verify/test a browser via natural-language CLI, capture and bisect DevTools traces, sync authenticated cookie state, build self-improving browsing agents, deploy browser automation as serverless functions, generate WebMCP scripts, turn traffic into an OpenAPI spec, run B2B research/prospecting (company/ICP discovery, competitor intelligence and profiling, event/conference prospecting, lightweight search), query a unified real-time search API with vertical-domain search, batch search, and URL extraction (AnySearch), and drive the official Firecrawl CLI for one-off web search/scrape/crawl/map/monitor/interact/parse/agent-extraction during the current session, including its research-paper and developer-issue/PR/README search indexes. Use for ANY task involving browsing a website, automating browser actions, testing a web app in a real browser, debugging a failed automation run, syncing login state, researching companies/competitors/events via live web data, looking up current facts/news/domain-specific data (finance, academic, travel, health, code, legal, etc.), or doing one-off web search/scrape/crawl/monitor/parse during a session — regardless of whether it's framed as testing, automation, research, or search, since they all run on the same underlying toolkit family."
---

# Browser Automation

Router skill unifying every skill built on the Browserbase browser-automation toolkit — previously split across 4 different categories by use case (verification / automation / API reference / research), now kept together because they share one underlying tool family and a task often crosses those use-case lines in a single session.

## Domains

### Core driving & verification
| Domain | When to use | Full guide |
|---|---|---|
| Browser CLI automation | Drive a real (optionally remote) browser via natural-language commands — navigate, extract, screenshot, fill forms, click | [references/browser/SKILL.md](references/browser/SKILL.md) |
| Adversarial UI testing | Diff-scoped or full-app exploration to find functional/accessibility/responsive/UX bugs | [references/ui-test/SKILL.md](references/ui-test/SKILL.md) |
| Trace capture & debugging | Capture a full DevTools-protocol trace and bisect it into per-page searchable buckets when a run fails | [references/browser-trace/SKILL.md](references/browser-trace/SKILL.md) |
| Agent-experience audit | Drop subagents on a product/SDK/docs/SKILL.md with a tiny prompt + real tools; score Setup Friction, Speed, Efficiency, Error Recovery, Doc Quality | [references/agent-experience/SKILL.md](references/agent-experience/SKILL.md) |

### Automation utilities
| Domain | When to use | Full guide |
|---|---|---|
| Cookie sync | Sync cookies from local Chrome into a Browserbase persistent context to browse as the authenticated user | [references/cookie-sync/SKILL.md](references/cookie-sync/SKILL.md) |
| Self-improving automation | Iteratively run a browsing task, read the trace, improve the strategy until it reliably passes; supports parallel runs | [references/autobrowse/SKILL.md](references/autobrowse/SKILL.md) |
| Serverless deployment | Deploy browser automation as cloud functions — cron schedules, webhook endpoints | [references/functions/SKILL.md](references/functions/SKILL.md) |

### Library / API reference
| Domain | When to use | Full guide |
|---|---|---|
| Simple URL fetch | Retrieve HTML/JSON without a full browser session | [references/fetch/SKILL.md](references/fetch/SKILL.md) |
| WebMCP script generation | Author/compile/validate site-specific WebMCP init scripts | [references/webmcp-gen/SKILL.md](references/webmcp-gen/SKILL.md) |
| Traffic → OpenAPI spec | Turn a captured trace into a best-effort OpenAPI 3.1 spec | [references/browser-to-api/SKILL.md](references/browser-to-api/SKILL.md) |

### Research & prospecting
| Domain | When to use | Full guide |
|---|---|---|
| Company/ICP research | Find companies to sell to, discover companies matching an ICP, score fit | [references/company-research/SKILL.md](references/company-research/SKILL.md) |
| Competitor analysis | Auto-discover competitors, deep-research each, compile a 4-view HTML intelligence report | [references/competitor-analysis/SKILL.md](references/competitor-analysis/SKILL.md) |
| Competitor profiling | Research/profile competitors from a given list of URLs into structured markdown profiles | [references/competitor-profiling/SKILL.md](references/competitor-profiling/SKILL.md) |
| Event/conference prospecting | Extract speakers from a conference URL, filter by ICP fit, deep-research the fits | [references/event-prospecting/SKILL.md](references/event-prospecting/SKILL.md) |
| Lightweight web search | Search results (URLs/titles/metadata) without a full browser session | [references/search/SKILL.md](references/search/SKILL.md) |
| Unified search API (AnySearch) | Real-time general web search, vertical-domain search (finance/academic/travel/health/code/legal/etc.), parallel batch search, and full-page URL extraction via a bundled cross-platform CLI — no browser session, no MCP install | [references/anysearch/SKILL.md](references/anysearch/SKILL.md) |

### Firecrawl CLI (third-party, one-off web work)

Imported 2026-08-16 from the official `firecrawl/cli` and `firecrawl/skills` repos (ISC license, Firecrawl; see [`THIRD-PARTY-LICENSES.md`](../../THIRD-PARTY-LICENSES.md)). This cluster is for **live, one-off web work during the current session** — a different job from `firecrawl-build*` in `library-api-reference`, which is for wiring Firecrawl into an application's own source code. Both are installed together by the vendor's own `firecrawl-cli init --all --browser` command, but only this cluster belongs here.

| Domain | When to use | Full guide |
|---|---|---|
| Firecrawl CLI (start here) | Escalation-pattern hub: search → scrape → map → crawl → monitor → interact. Also routes to `research`/`developer` search and to the `firecrawl-build`/onboarding skills | [references/firecrawl-cli/SKILL.md](references/firecrawl-cli/SKILL.md) |
| Firecrawl search | Web search with optional full-page content, `--categories developer` for the developer index, routes paper queries to `firecrawl research` | [references/firecrawl-search/SKILL.md](references/firecrawl-search/SKILL.md) |
| Firecrawl scrape | Extract clean markdown from a known URL, including JS-rendered SPAs; concurrent multi-URL | [references/firecrawl-scrape/SKILL.md](references/firecrawl-scrape/SKILL.md) |
| Firecrawl map | Discover/list all URLs on a site, with optional search filtering | [references/firecrawl-map/SKILL.md](references/firecrawl-map/SKILL.md) |
| Firecrawl crawl | Bulk-extract an entire site or section (e.g. all `/docs/`), depth/path limits | [references/firecrawl-crawl/SKILL.md](references/firecrawl-crawl/SKILL.md) |
| Firecrawl monitor | Scheduled recurring change detection on pages *or* the open web, with an AI noise-filtering judge, webhook/email alerts | [references/firecrawl-monitor/SKILL.md](references/firecrawl-monitor/SKILL.md) |
| Firecrawl interact | Post-scrape live browser session — clicks, form fills, pagination, login, persistent profiles | [references/firecrawl-interact/SKILL.md](references/firecrawl-interact/SKILL.md) |
| Firecrawl download | Bulk-download a site to local files (markdown/screenshots/multi-format per page) | [references/firecrawl-download/SKILL.md](references/firecrawl-download/SKILL.md) |
| Firecrawl agent | AI-powered autonomous multi-page structured-data extraction with a JSON schema | [references/firecrawl-agent/SKILL.md](references/firecrawl-agent/SKILL.md) |
| Firecrawl parse | Convert a local file (PDF/DOCX/DOC/ODT/RTF/XLSX/XLS/HTML) to markdown, with optional AI summary/Q&A | [references/firecrawl-parse/SKILL.md](references/firecrawl-parse/SKILL.md) |
| Firecrawl developer index | Answer a coding question from primary sources — GitHub issues, merged PRs, READMEs, curated docs — with matched passages, not just links | [references/firecrawl-developer-index/SKILL.md](references/firecrawl-developer-index/SKILL.md) |
| Firecrawl research paper index | Semantic search over ~43M paper abstracts (biomedical/PubMed/bioRxiv/medRxiv-heavy, plus arXiv), citation-graph expansion, in-body passage verification | [references/firecrawl-research-index/SKILL.md](references/firecrawl-research-index/SKILL.md) |

## How to pick a domain

1. **Verifying your own change works**: `browser` / `ui-test` / `browser-trace` (pairs with `product-verification`'s discipline — this skill supplies the tool, that one supplies the "don't claim done without evidence" rule).
2. **Automating a recurring browsing chore**: `cookie-sync` for auth, `autobrowse` to harden a flaky task into a reliable one, `functions` to run it on a schedule/webhook.
3. **Writing code against these tools**: the "Library / API reference" section — don't guess function names, read the actual reference.
4. **Researching companies/competitors/events for sales or GTM**: the "Research & prospecting" section. `competitor-analysis` (auto-discover, full intelligence report) and `competitor-profiling` (you already have the URLs, want a lighter profile doc) are complementary — pick based on whether you're starting from a known list or need discovery first.
5. **General fact-lookup, news, or vertical-domain queries** (stock quotes, CVEs, DOIs, patents, IATA codes, etc.): `anysearch` — it has structured vertical-domain search across 16 domains and batch/parallel queries that `search` doesn't.
6. **One-off web work during the current session** (search/scrape/crawl/map/monitor/interact/parse a file/AI-extract structured data): the Firecrawl CLI cluster — start at `firecrawl-cli`, which routes to the narrower skill for the specific verb. Escalate in the order search → scrape → map → crawl → interact, and reach for `monitor` the moment the ask implies recurrence ("alert me when...") rather than a single read.
7. **A programming question that belongs in a primary source** (an error message, an API contract, a known bug fixed by a merged PR): `firecrawl-developer-index` before a generic web search — it returns the actual matched passage from the issue/PR/README/doc, not just a link.
8. **Finding research papers** (biomedical/clinical/life-science or arXiv): `firecrawl-research-index` searches the paper corpus itself (abstracts, citation graph, full-text verification) — a different job from `deep-research`'s outline-driven report pipeline and from `library-api-reference`'s `arxiv-doc-builder` (which converts a paper you already have the ID for into Markdown, it doesn't search for one).

## Note on the `competitors` skill in `marketing`

`marketing`'s `research-strategy/competitors` domain is a **different job**: it generates public-facing comparison/alternative *pages* for SEO and sales content, not a research report. If the ask is "build a vs-page for our website," go there instead of here.

## Note on `search` vs `anysearch`

Both return search results without opening a browser, but they're different tools with no true overlap — read each in full before assuming one replaces the other:

- **`search`** — thin `curl`-only wrapper around Browserbase's own Search API. One endpoint, one query shape, no CLI to install, requires `BROWSERBASE_API_KEY`.
- **`anysearch`** — a separate third-party service (AnySearch) with a bundled multi-runtime CLI (Python/Node/PowerShell/Bash, auto-detected), vertical-domain search across 16 named domains (finance, academic, travel, health, code, legal, gaming, film, business, security, ip, energy, environment, agriculture, resource, social_media) with per-domain required parameters via `get_sub_domains`, parallel `batch_search` over multiple queries, and a separate `extract` command for full-page Markdown content. Works anonymously with lower rate limits or with an optional `ANYSEARCH_API_KEY`.

Default to `anysearch` when the query overlaps a supported vertical domain or needs batch/parallel search or URL extraction; default to `search` for a quick one-off lightweight lookup when Browserbase credentials are already the project's standard. `anysearch` sends queries/URLs/keys to `https://api.anysearch.com` — treat that the same as any other third-party network call (see its own `SKILL.md` for the credential-handling and auto-registration rules before using it).

## Note on the Firecrawl CLI cluster vs. `search`/`anysearch`/`fetch`

Three separate vendors now solve overlapping jobs in this skill — read each one's own `SKILL.md` before assuming one subsumes another, since each has capabilities the others don't:

- **`fetch`** — plain HTTP, no rendering, no credentials beyond what the target site itself requires. Cheapest option when JS rendering isn't needed.
- **`search`** (Browserbase) / **`anysearch`** (AnySearch) — search-only (see the dedicated note above for how those two differ from each other).
- **Firecrawl CLI cluster** — the broadest single vendor here: search *and* scrape *and* crawl *and* map *and* monitor (scheduled change detection with an AI noise judge — nothing else in this skill does this) *and* interact *and* local-file parsing *and* AI-schema-driven extraction *and* dedicated developer/research-paper search indexes, all behind one `firecrawl` binary and one `FIRECRAWL_API_KEY` (keyless free tier available). Reach for it when the task needs more than a single search/fetch call, or specifically needs `monitor`, `agent` (schema-driven extraction), or the developer/research indexes — none of which `search`, `anysearch`, `browser`, or `fetch` provide.

Not a strict hierarchy: a project already standardized on Browserbase or AnySearch credentials has a reason to stay there for simple search even though Firecrawl could also do it. Don't install a third vendor's CLI for a one-line search when the project already has working credentials for another.
