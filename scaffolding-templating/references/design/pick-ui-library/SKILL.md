---
name: pick-ui-library
description: Pick the right library for a given frontend task from a curated, opinionated list — numbers, OTP inputs, charts, command menus, virtualization, drag and drop, toasts, state, styling, and more. Only runs when explicitly invoked; it does not trigger on its own.
disable-model-invocation: true
---

# Picking The Right Library

A lookup skill. When invoked with a task ("I need toasts", "what should I use for drag and drop?"), match the task to the curated list below and recommend the library. These are deliberate, taste-driven picks — don't substitute alternatives outside this list unless the user asks for one or the task genuinely isn't covered.

## How to use this

1. **Identify the task**, not the library the user named. "I need to show a dropdown" is a UI-primitives task (base-ui), even if they asked about something else.
2. **Check what's already installed.** Look at `package.json` first. If the project already uses a listed library, use it. If it uses a competitor (e.g. react-window instead of Virtuoso), flag the recommendation but don't churn the dependency without being asked.
3. **Recommend one library**, state what it's for in one sentence, and install/wire it up if that's part of the request. Don't present a menu of options when the list has a clear answer.
4. If the task isn't covered by the list, say so explicitly and recommend from your own knowledge — but be clear you've left the curated list.

## The list

### UI components & primitives

| Task | Library |
| --- | --- |
| Unstyled, accessible UI components (dialogs, popovers, menus, selects…) | [base-ui](https://base-ui.com) — default pick, lighter API surface, pairs naturally with shadcn/ui |
| Same, but the project needs deeper WAI-ARIA coverage or heavy internationalization (RTL, 30+ locales, international date/number/calendar formatting) | React Aria (`react-aria-components`) — see `library-api-reference`'s `react-aria` sub-skill. Bigger API surface and steeper learning curve than base-ui; reach for it specifically for that accessibility/i18n depth, not as a default swap |
| Command menus (⌘K palettes) | [cmdk](https://cmdk.paco.me) |
| Toasts / notifications | [Sonner](https://sonner.emilkowal.ski) |
| One-time password / verification code inputs | [input-otp](https://input-otp.rodz.dev) |
| Customizable GUIs / control panels | [Leva](https://github.com/pmndrs/leva) — [dialkit](https://joshpuckett.me/dialkit) is an alternative |

An existing project already on shadcn/ui + Radix that wants to move to base-ui specifically (not a fresh choice, a migration) has its own dedicated skill: `migrate-radix-to-base` (in this same `scaffolding-templating/references/design/` tree) — vendored verbatim from shadcn/ui's own official migration tooling. Use that instead of hand-rolling the swap.

### Animated component galleries

| Task | Library |
| --- | --- |
| Ready-made animated component, native to the shadcn/ui + Tailwind + Framer Motion stack | `magicui` (in this same tree) — real embedded source for 20 representative components |
| Ready-made animated component/effect, not tied to shadcn (framework-agnostic, also has Vue/Svelte ports) | `react-bits` (in this same tree) — catalog only, no embedded source (license restriction), install via CLI at time of use |

These are component *galleries* — pick one ready-made effect and install it. For building bespoke motion from first principles (should it animate, which curve/duration/spring), that's `animate`, not this row. For naming an effect you can't name yet, that's `animation-vocabulary`. The `react-bits` skill's own SKILL.md has the full comparison table between it and `magicui` if the choice isn't obvious from the one-liners above.

### Motion & visuals

| Task | Library |
| --- | --- |
| General-purpose animation (springs, layout animations, enter/exit) | [motion](https://motion.dev) (Framer Motion) |
| Animating numbers (counters, prices, stats) | [NumberFlow](https://number-flow.barvian.me) |
| Animated text components | [torph](https://torph.lochie.me/) |
| 3D globes | [Cobe](https://cobe.vercel.app) |
| Dynamic OG images (HTML/CSS → SVG/PNG) | [Satori](https://github.com/vercel/satori) |
| Syntax highlighting | [shiki](https://shiki.style) |

Reach for motion when you need springs, layout animations, exit animations, or gesture-driven values. A simple hover or fade doesn't need it — plain CSS transitions are the right tool there.

### Charts

| Task | Library |
| --- | --- |
| Real-time / streaming charts | [Liveline](https://github.com/benjitaylor/liveline) |
| General charts (static or interactive dashboards) | [recharts](https://recharts.org) |

The split: if data points arrive live and the chart scrolls with time, use Liveline. Everything else is recharts.

### Interaction & performance

| Task | Library |
| --- | --- |
| Drag and drop | [dnd kit](https://dndkit.com) |
| Virtualization (long lists, large tables) | [Virtuoso](https://virtuoso.dev) |

### State & styling

| Task | Library |
| --- | --- |
| State management | [zustand](https://zustand.docs.pmnd.rs) |
| Constructing `className` strings conditionally | [clsx](https://github.com/lukeed/clsx) |
| Type-safe, variant-driven styling for Tailwind | [cva](https://cva.style) |
| Theme switching / dark mode (no flash on load) | [next-themes](https://github.com/pacocoursey/next-themes) |

The styling split: clsx for ad-hoc conditional classes; cva when a component has real variants (size, intent, state) that deserve a typed API. They compose — cva uses clsx-style inputs internally.

## Common mismatches to catch

- **Toasts built by hand or with a modal library** → Sonner exists for exactly this.
- **A `<div>`-based dropdown/dialog with manual focus handling** → base-ui, which handles accessibility, focus trapping, and dismissal.
- **Animating a number by re-rendering text** → NumberFlow handles digit transitions properly.
- **Rendering a 1,000+ row list directly** → Virtuoso before reaching for pagination hacks.
- **A `useState`-per-component web of props for shared state** → zustand.
- **Template-literal className ternaries three conditions deep** → clsx (or cva if it's variant-shaped).
