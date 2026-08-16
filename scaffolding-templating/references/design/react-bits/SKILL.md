---
name: react-bits
description: Catalog and install guide for react-bits (reactbits.dev) — a framework-agnostic-flavored library of 160+ free animated React components (text effects, general motion, interactive UI, animated backgrounds) with official Vue/Svelte ports, installed fresh per-project via shadcn CLI or jsrepo. Use when the user wants a ready-made animated background, text effect, or flashy UI component that isn't tied to the shadcn/Tailwind/Framer-Motion stack, when they name react-bits explicitly, or when comparing it against magicui/animate/animation-vocabulary/pick-ui-library.
---

# React Bits

A catalog and installation guide for [react-bits](https://reactbits.dev) (source: [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits), ~45k GitHub stars) — "the largest & most creative library of animated React components," per its own README. This skill is a lookup + decision guide. It does not build custom animations from scratch (that's `animate`) and it does not embed react-bits' component code (see below).

## License note — read this before doing anything else

react-bits ships under **"MIT + Commons Clause License Condition v1.0."** The Commons Clause carve-out says you may use the software for any purpose, including commercial, **so long as you do not sell, sublicense, or redistribute the components themselves — alone, in a bundle, or as a ported version.**

This Skills-Directory repo *is* a bundle that gets copied wholesale onto a live `~/.claude/skills/` folder and shared onward. Statically storing a copy of react-bits' `.tsx`/`.jsx`/`.css` component source inside this file would be exactly the "redistribute...in a bundle" the clause forbids — even a short snippet. So, by design:

**This skill contains zero embedded react-bits component source code.** No `.tsx`, `.jsx`, or `.css` copied from the site or repo appears anywhere below. What it does instead:
- Names real components and categories (verified against the live GitHub repo, see below) and describes what each category of effect looks like in prose.
- Links to the official site and install commands.
- Tells you the CLI command to pull the component fresh, at time of use, directly into *your own project* — that's the license-permitted path ("use it as part of your application"), distinct from us keeping a static copy in this repo.

Practical upshot: you can use react-bits freely in whatever you're building. This skill just can't be your offline archive of its source — see "When NOT to use react-bits" below for where to go for that instead.

## What it is

- **160+ animated components** (README advertises "165+, growing weekly"; a live listing of `src/content/` in the GitHub repo on 2026-08-16 showed 31 Text Animation, 36 Animations, 43 Components, and 51 Backgrounds entries — 161 total, consistent with "165+" and ongoing weekly growth) across **4 official categories**:
  - **Text Animations** — effects applied to text itself (e.g. `BlurText`, `DecryptedText`, `GlitchText`, `ScrambledText`, `SplitText`, `ShinyText`, `TextType`, `CountUp`).
  - **Animations** — general-purpose UI motion and cursor/pointer effects, not tied to a specific component shape (e.g. `ClickSpark`, `Magnet`, `ImageTrail`, `GlareHover`, `MetallicPaint`, `SplashCursor`, `Noise`).
  - **Components** — interactive UI widgets with animation baked in (e.g. `Dock`, `Carousel`, `CardSwap`, `GooeyNav`, `TiltedCard`, `InfiniteMenu`, `Stepper`, `Masonry`).
  - **Backgrounds** — full animated background/canvas effects (e.g. `Aurora`, `Silk`, `Threads`, `LiquidChrome`, `Particles`, `Hyperspeed`, `DotGrid`, `Waves`).
- **4 code variants per component**: JS-CSS, JS-Tailwind, TS-CSS, TS-Tailwind — you pick the language/styling combo per component at install time.
- **Framework reach beyond React**: official ports exist for Vue (vue-bits.dev) and Svelte (sveltebits.xyz). It is not a React-only or shadcn-only project.
- **Not tied to shadcn's design system or Framer Motion.** Some components use Framer Motion internally, others use raw CSS/WebGL/canvas — there's no single underlying motion engine the way Magic UI standardizes on Framer Motion, and no shared design-token system the way shadcn-based libraries do.
- Confirmed via the repo's own count and honesty caveat: the exhaustive 161-name list above is real (pulled directly from the GitHub API's directory listing of `src/content/{TextAnimations,Animations,Components,Backgrounds}` on 2026-08-16), but it will drift as the project adds components weekly — treat the named examples as illustrative, not a frozen catalog, and re-check the live repo or reactbits.dev for the current full list.

## Install workflow

Two official install paths, both pulling code live into the user's own project (never from this skill's files):

```bash
# via shadcn CLI (registry-style; example from the project's own README)
npx shadcn@latest add @react-bits/BlurText-TS-TW

# via jsrepo (the project's own CLI, jsrepo.config.ts ships in the repo root)
npx jsrepo add <component>
```

Each component's page on reactbits.dev exposes copy-ready CLI commands for all 4 variants, plus a manual copy-paste option if you'd rather not use a CLI. When recommending a component, ask (or infer from the project) which combination applies:

| Choice | Options |
| --- | --- |
| Language | JS or TS |
| Styling | plain CSS or Tailwind |

e.g. `BlurText-JS-CSS`, `BlurText-JS-TW`, `BlurText-TS-CSS`, `BlurText-TS-TW` — same component, four ready-made variants matching the target project's stack.

## The comparison — when to reach for react-bits vs. something else

This is the main point of this skill: react-bits overlaps in *intent* (animated, ready-made UI) with several other skills in this collection but sits on a different axis from each of them.

| Compare against | What it actually is | Reach for react-bits instead when… | Reach for the other one when… |
| --- | --- | --- | --- |
| **magicui** (`scaffolding-templating/references/design/magicui/`) | ~80 components native to the shadcn + Tailwind + Framer Motion stack, MIT-licensed (no redistribution restriction), so that skill embeds real source snippets directly | The project isn't shadcn-based (or doesn't care about matching shadcn's visual language) and you want one specific flashy effect — a particular background, text animation, or interaction — from a much larger and more varied catalog; you also need a Vue or Svelte port | The project already runs on shadcn + Tailwind + Framer Motion and you want something that visually matches that ecosystem's polished-SaaS-marketing aesthetic; you also want the actual source statically available in this repo for offline reference (magicui's MIT license permits that, react-bits' does not) |
| **`animate`** (`scaffolding-templating/references/design/animate/SKILL.md`) | A build/decision skill for hand-rolling motion from first principles — should this animate at all, which tool (CSS transition vs WAAPI vs Motion), which easing curve, which duration or spring config | You just want a ready-made, named effect installed (an aurora background, a glitch-text heading) — no bespoke decision process needed | You're building or adjusting a bespoke interaction (a dropdown open, a toast enter/exit, a hover state) where the right motion has to be *decided*, not picked off a shelf. They aren't competitors: "give me an aurora background effect" → react-bits; "should this dropdown animate, and how" → `animate` |
| **`animation-vocabulary`** (`scaffolding-templating/references/design/animation-vocabulary/SKILL.md`) | A pure reverse-lookup glossary — turns a vague description ("the bouncy thing when it opens") into the correct term ("Pop in"). Names effects; installs nothing | You already know (or now know) the name/shape of the effect you want and are ready to find and install a component for it | You can't name the effect you're picturing. Use `animation-vocabulary` first to get the term, then come to react-bits (or `animate`, or magicui) to actually build or install it |
| **`pick-ui-library`** (`scaffolding-templating/references/design/pick-ui-library/SKILL.md`) | The umbrella "which library for this task" picker across all frontend concerns — toasts, dropdowns, charts, drag-and-drop, state management, styling, and more | You've already narrowed the task to "I want an animated text/background/UI effect component" and need the deep-dive on that specific corner | You're not sure which *category* of library problem you even have (e.g. "how do I do toasts" or "what should I use for virtualization") — `pick-ui-library` is the router; this skill is one specific entry it can point into |

## When NOT to use react-bits

If the task requires the component's actual `.tsx`/`.jsx`/`.css` source to be **stored and version-controlled statically inside this skill repo** for offline reference — that is not possible here by license (see the note at the top). Use **magicui** or **shadcn-official** instead for anything that needs a locally-archived, license-clear source copy. react-bits remains a fine choice for *live, per-project* installs; it just can't be this repo's offline archive.
