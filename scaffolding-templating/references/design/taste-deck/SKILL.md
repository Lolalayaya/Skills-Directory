---
name: taste-deck
description: Generate fixed-stage HTML slide decks/presentations (pitch decks, keynotes, "8 slides about X") with real-brand value-layer fidelity — pick from a 30-brand showcase library and copy its colors/fonts/spacing 1:1, or author a self-consistent custom style when nothing in the library fits. Use for deck/slide/presentation briefs specifically, not general landing pages, portfolios, or app UI (see taste-skill/hallmark for those). Covers page-plan/stage/navigation/motion rules, four mandatory QA gates, a CJK typography fallback, and local PDF/PPTX export or public-URL deployment.
---

# Taste Deck — Fixed-Stage Slide Decks

Generates single-file, standalone HTML presentation decks (1920×1080 fixed stage, fit-scaled to viewport, no build step) that read as a specific real brand's design system rather than a generic AI deck. Not for landing pages, portfolios, redesigns, or app UI — route those to [`../taste-skill/SKILL.md`](../taste-skill/SKILL.md) or [`../hallmark/SKILL.md`](../hallmark/SKILL.md) instead. Not for a lighter-weight, non-value-locked slide container either — the existing [`../slides/SKILL.md`](../slides/SKILL.md) covers that simpler case.

## Two routes

**素材模式 (default)** — the brief's style can be matched by a style in the showcase library (`refero-styles/`):
1. Filter `showcase/selection-index.json` by mood / tone / density / scheme / `best_for` / `avoid_for` to narrow to 2-4 candidates.
2. Preview the shortlist's slides at `showcase/gallery/<slug>/slide-{0,4,7}.png`, or browse everything at `showcase/gallery/index.html`.
3. Read the chosen style's `refero-styles/<Brand>/DESIGN.md` in full before generating.
4. Generate against it with **1:1 value-layer fidelity** — see [`deck-mode.md`](deck-mode.md) §15.3, the single highest-leverage rule in this skill: `tokens.json` is the only numeric source, never invent a color or font that isn't in it.

Field semantics for `design-manifest.json` (the machine-readable detail behind `selection-index.json`) and the 30 known per-style exceptions (e.g. a few styles have no `radius` group) are in [`manifest-schema.md`](manifest-schema.md). The word-list and field conventions for annotating a *new* style when extending the library are in [`annotation-guide.md`](annotation-guide.md).

**自由發揮模式 (fallback)** — the brief needs a style outside the library (hand-drawn wedding invite, cartoon kids' product, a fully custom voice):
1. Fill [`freeplay-declaration.md`](freeplay-declaration.md) FIRST — a self-authored mini design-system (palette voice / typographic voice / signature moves / anti-convergence statement / CJK plan). This is both the generation discipline and the QA anchor.
2. Generate against that declaration. QA gates 2-4 (below) run as normal; gate 1 downgrades from "value ⊆ real brand tokens" to "value ⊆ what you declared".

If a brief is borderline, default to 素材模式 — real brand systems are the anti-slop ammunition; freeplay is for when nothing in the library legitimately fits.

## The full rule set

Read [`deck-mode.md`](deck-mode.md) in full before generating — it is the complete contract (externalized here as its own top-level file rather than a §15-16 section, since this skill doesn't carry the longform §0-14 brief-inference/dial/AI-tell content that the original source bundled it with; that content already lives in `../taste-skill/SKILL.md`). It covers, non-negotiably:
- **§15.1-15.2**: default 8-page plan, the deterministic fixed-stage/scale/switch/navigation mechanics (bottom-center pill-capsule dot nav, tone-adaptive contrast, a `color-mix()` gotcha that silently kills the capsule's visibility if gotten wrong)
- **§15.3**: value-layer fidelity boundary (the rule above)
- **§15.4**: layout hard rules (flow layout only, content must not cross y=900, a 160px bottom safety zone)
- **§15.5**: story-reveal motion (transition-driven stagger, not CSS `animation` — forbidden patterns listed explicitly)
- **§15.6**: four mandatory QA gates — value-layer check, automated structural/line-height check, visual screenshot QA, anti-convergence structure check. Reference implementations for all four ship in `showcase/*.py` (pure Python, mostly no external deps beyond Playwright for the screenshot gate)
- **§15.7**: deck-specific banned patterns
- **§15.8**: the CONFIG-block customization contract every generated deck must expose
- **§15.9**: export (local PDF/PPTX via `showcase/export-pdf.py` / `export-pptx.py`) and public-URL sharing (Vercel or Feishu/妙搭) — **read [`deploy-guide.md`](deploy-guide.md) in full before deploying**, don't improvise platform CLI calls from memory
- **§16**: the style contract distinguishing what's binding (source tokens, usage constraints) from what's creative freedom (color composition, typographic voice, page personality, copy)
- **§16.5**: the CJK/Chinese typography fallback contract (font pairing per role, line-height bumps, 盘古之白 spacing, no italic/uppercase on CJK)

Fonts are self-hosted from `showcase/fonts/` (62 Google-Fonts `.woff2` subsets covering the 23 families the library actually uses, all OFL-licensed) — never link Google Fonts externally for a deck; `deck-mode.md` §15.9 explains why (unreliable reachability for some audiences) and ships rebuild tooling (`fonts_download.py`, `fonts_rewrite.py`) if the font set needs to change.

Reference skeleton: `showcase/_skeleton.html` is a working, non-hypothetical implementation of the stage/scale/nav/print/reduced-motion mechanics in §15.2 — start a new deck from it rather than rebuilding that machinery from memory.

## What's deliberately NOT carried over from the source project

This is a surgical import, not a wholesale one. The upstream project (`design-taste-frontend`) bundles this deck system together with a much longer general frontend-design skill (§0-14: brief inference, the three-dial system, a design-system map, an AI-tell catalog, a redesign protocol, a pre-flight checklist). That content was **not** imported here because it is near word-for-word identical to this repo's own pre-existing [`../taste-skill/SKILL.md`](../taste-skill/SKILL.md) — importing it again would have created two competing copies of the same rules. If a deck brief also needs general brief-inference or dial-setting guidance, read `taste-skill` for that part; this file only owns what's specific to decks. `brand-style-reference.md` (a real-website style-learning report referenced once in §16.1) was excluded for a different reason: its own text states it is **not** distributed under the source repo's MIT license (brand names/trademarks belong to their owners) — fetch it live from the source repo yourself if you want it, rather than relying on a copy here.

## Notes

- Everything under `showcase/` and `refero-styles/` is vendored data/tooling, not prose to read end-to-end — consult it per `deck-mode.md`'s pointers rather than browsing it upfront.
- Several files here (`deck-mode.md`, `deploy-guide.md`, `annotation-guide.md`, `manifest-schema.md`, `freeplay-declaration.md`) are vendored close to verbatim from the source and mix English with Simplified Chinese prose (the source project's working language) — not translated, since the content is functional as-is and the effort wasn't requested. Say so if you'd like this translated to English for consistency with the rest of this repo.
