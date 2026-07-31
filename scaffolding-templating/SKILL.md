---
name: scaffolding-templating
description: "Turn best practices into ready-to-use templates, scaffolds, token systems, and reference databases so output quality stays consistent instead of being reinvented from scratch each time. Covers general content/page scaffolding (programmatic SEO page templates) and a full design sub-system: brand identity, design tokens, UI styling (shadcn/Tailwind), logo/banner/slide/theme/icon generation, algorithmic art, canvas posters, Anthropic brand guidelines, web-artifact building, and UI/writing-style compliance review. Use whenever the user wants to scaffold a new project/page/deliverable from a template or data-backed pattern, needs consistent visual design (colors, typography, layout, components, presentations, brand assets, themes), wants a UI or docs review against a design/writing style guide, or says things like 'make this look good', 'set up the design system', 'generate a banner/logo/slide deck', or 'build pages at scale from this data'."
---

# Scaffolding & Templating

Router skill for "codify the best-practice pattern once, then stamp it out consistently" — as opposed to solving the same design/structure problem freshly every time. Two sub-groups: general scaffolding, and a much larger design & visual templating cluster (`references/design/`).

## General scaffolding

| Domain | When to use | Full guide |
|---|---|---|
| Programmatic SEO pages | Generate SEO-driven pages at scale from templates + data (directory pages, location pages, "[keyword] + [modifier]" patterns) | [references/general/programmatic-seo/SKILL.md](references/general/programmatic-seo/SKILL.md) |

## Design & visual templating

| Domain | When to use | Full guide |
|---|---|---|
| Design (umbrella) | Brand identity, design tokens, logo generation, CIP mockups, HTML presentations, banners, icons, social photos — the broadest entry point | [references/design/design/SKILL.md](references/design/design/SKILL.md) |
| Design system | Three-layer design tokens (primitive→semantic→component), CSS variables, spacing/typography scales, component specs | [references/design/design-system/SKILL.md](references/design/design-system/SKILL.md) |
| UI styling | shadcn/ui + Radix + Tailwind components, canvas-based visual designs, dark mode, accessible patterns | [references/design/ui-styling/SKILL.md](references/design/ui-styling/SKILL.md) |
| UI/UX design intelligence | Searchable database of styles, palettes, font pairings, charts, and per-stack conventions (React, Next.js, Vue, Flutter, etc.) | [references/design/ui-ux-pro-max/SKILL.md](references/design/ui-ux-pro-max/SKILL.md) |
| Banner design | Social/ad/web-hero/print banners across platforms with art-direction options | [references/design/banner-design/SKILL.md](references/design/banner-design/SKILL.md) |
| Brand voice & identity (build your own) | Define/apply a *new* brand's tone of voice, messaging framework, visual identity, asset management, consistency rules | [references/design/brand/SKILL.md](references/design/brand/SKILL.md) |
| Anthropic's own brand guidelines (apply preset) | Apply Anthropic's specific, pre-existing colors/typography to an artifact — not for building a generic brand system | [references/design/anthropic-brand-guidelines/SKILL.md](references/design/anthropic-brand-guidelines/SKILL.md) |
| Canvas design | Beautiful static visual art as `.png`/`.pdf` — posters, original artwork | [references/design/canvas-design/SKILL.md](references/design/canvas-design/SKILL.md) |
| Algorithmic art | Generative art with p5.js, seeded randomness, flow fields, particle systems | [references/design/algorithmic-art/SKILL.md](references/design/algorithmic-art/SKILL.md) |
| Theme factory | Apply one of 10 preset color/font themes to any artifact (slides, docs, HTML pages) | [references/design/theme-factory/SKILL.md](references/design/theme-factory/SKILL.md) |
| Frontend design direction | Aesthetic direction, typography, and intentional choices that avoid templated-default look | [references/design/frontend-design/SKILL.md](references/design/frontend-design/SKILL.md) |
| Web artifacts builder | Elaborate multi-component claude.ai HTML artifacts — React/Tailwind/shadcn, state management, routing | [references/design/web-artifacts-builder/SKILL.md](references/design/web-artifacts-builder/SKILL.md) |
| Web design guidelines review | Review UI code for Web Interface Guidelines compliance — accessibility, UX audit | [references/design/web-design-guidelines/SKILL.md](references/design/web-design-guidelines/SKILL.md) |
| Writing guidelines review | Review docs/prose for writing-style-guide compliance — tone, voice | [references/design/writing-guidelines/SKILL.md](references/design/writing-guidelines/SKILL.md) |
| Slide decks | Strategic HTML presentations with Chart.js, design tokens, responsive layouts | [references/design/slides/SKILL.md](references/design/slides/SKILL.md) |

## How to use this skill

1. **Producing a new deliverable** (banner, slide deck, logo, page-at-scale): start from the closest-matching domain's template/data rather than designing from a blank page — that consistency is the entire point of this category.
2. **Reviewing existing output**: `web-design-guidelines` and `writing-guidelines` are compliance-review domains, not generation domains — use them to audit, not to create.
3. **When multiple design domains could apply** (e.g. a slide deck needs both `slides` and `theme-factory` and `design-system` tokens), it's normal to pull from more than one — they're meant to compose.
4. Most design domains bundle real reference data (CSVs of palettes/fonts/charts, preset theme definitions, component templates) one level under their own directory — read those on demand rather than trying to hold the full database in context; that's why they're structured as references rather than inlined here.
5. **`brand` vs `anthropic-brand-guidelines`**: these sound similar but solve different jobs. `brand` helps *define or apply a brand system you're building* (any company's). `anthropic-brand-guidelines` applies one specific, already-fixed brand (Anthropic's) — reach for it only when the artifact is explicitly meant to carry Anthropic's look-and-feel, not as a generic "make this branded" request.
6. **`design` vs `brand`/`design-system`/`banner-design`/`slides`**: these all come from the same source package and deliberately overlap — `design` is the all-in-one entry point that bundles its own Logo/CIP/Banner/Icon/Social-Photo/Slides generation inline (one trigger, everything), while `brand`, `design-system`, `banner-design`, and `slides` are the same package's standalone, narrower versions of those individual pieces. Neither is more "correct" — pick `design` for a request spanning multiple deliverables or when unsure, pick the standalone skill when the request is for exactly one of those things and a smaller context load is preferable. Do not merge or treat one as deprecated; the duplication is intentional on the source package's part.

## Note on scope

Marketing content-strategy skills (copywriting, ads, SEO audits, etc.) are deliberately **not** folded into this category even though some produce templated output — they're domain playbooks about *what to say*, not scaffolding for *how a deliverable is structured*, and remain as independent skills.
