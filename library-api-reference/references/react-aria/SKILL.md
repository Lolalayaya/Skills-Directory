---
name: react-aria
description: Guide for building fully accessible, unstyled ("headless") React components with React Aria (`react-aria-components`, and the lower-level `@react-aria/*` hooks like `useButton`, `useTextField`, `useCheckbox`). Use this skill whenever the user wants to build a custom design system from scratch with full WAI-ARIA accessibility, needs a headless component library with deep internationalization (RTL, 30+ languages, international date/number/calendar formatting), or mentions React Aria, `react-aria-components`, `@react-aria/*`, or any specific hook like `useButton`/`useTextField`/`useListBox`. Also use when the user is deciding between headless UI libraries and React Aria is on the table.
license: Apache-2.0
metadata:
  author: adobe
  version: "1.0.0"
---

# React Aria

React Aria (from Adobe's `adobe/react-spectrum` monorepo) is a **headless, unstyled** library for building accessible, adaptive, and internationalized web components and design systems. It ships zero CSS and imposes no required DOM structure — you get behavior, accessibility, and interaction handling; you provide the visual design. Reach for it when a project needs a from-scratch design system with rigorous WAI-ARIA compliance and international-grade i18n (right-to-left layout, 30+ locales, and localized date/number/calendar formatting across 13 calendar systems and 5 numbering systems) — that depth of accessibility and i18n coverage is React Aria's specific edge over comparable headless libraries, at the cost of a larger API surface and a steeper learning curve.

This skill does not resolve *which* headless UI library (React Aria vs. base-ui vs. Radix, etc.) a project should standardize on globally — that decision belongs to `scaffolding-templating`'s `pick-ui-library` skill. Cross-reference that skill when the choice itself is in question; another process is responsible for wiring the actual cross-reference into that skill's content. This skill activates once React Aria has already been chosen, or when the user explicitly asks about it by name.

## The 4-Layer Architecture

The `react-spectrum` repo is layered — changes flow upward from the lowest level:

1. **`@internationalized/*` and `@react-stately/*`** — i18n utilities (date/number/calendar formatting, RTL) and framework-agnostic state management (lowest level, no DOM/accessibility concerns).
2. **`@react-aria/*`** — behavior and accessibility hooks built on top of the above (e.g. `useButton`, `useTextField`). Attaches ARIA attributes and interaction handling to elements you render yourself.
3. **`react-aria-components` (RAC)** — the component layer built on the hooks: pre-built unstyled components with render props and `data-*` state attributes, ready to style. This is what most people mean today when they say "React Aria." (React Spectrum v3 also sits at roughly this layer.)
4. **RSP S2 (`@react-spectrum/s2`)** — Adobe's own fully-styled design system, built on top of RAC. **Out of scope for this skill** — everything here concerns the unstyled layers below it.

## Installation

For building a styled design system from scratch, start with the component layer:

```
npm install react-aria-components
```

Only drop down to individual `@react-aria/*` hooks (e.g. `npm install @react-aria/button react-stately`) when you need fully custom or highly bespoke behavior that RAC's components don't expose — see [references/hooks.md](references/hooks.md) for when that trade-off is worth it.

## Styling Model

`react-aria-components` ships no CSS. Style components through:

- **`className`** — a plain string, or a callback that receives the component's render state and returns a string (useful with utilities like `tailwind-variants` or `clsx`).
- **`data-*` attributes** — RAC sets these on the rendered DOM element for every interaction/selection state: `data-hovered`, `data-pressed`, `data-selected`, `data-disabled`, `data-focused`, `data-focus-visible`, `data-invalid`, and more, depending on the component. Target them directly in CSS, or via Tailwind variants (`pressed:`, `selected:`, `disabled:`, ...) as the starter kit below does.
- **Slots** — some composite components (e.g. `Switch`) expose sub-parts as separate exported pieces you compose yourself, rather than a single monolithic component with configuration props.

Real example — the `className` render-prop pattern, from Adobe's own Tailwind starter kit's `Button.tsx` (`starters/tailwind/src/Button.tsx` in `adobe/react-spectrum`):

```tsx
import {composeRenderProps} from 'react-aria-components/composeRenderProps';
import {Button as RACButton, type ButtonProps as RACButtonProps} from 'react-aria-components/Button';
import {tv} from 'tailwind-variants';

let button = tv({
  base: 'relative inline-flex items-center justify-center gap-2 ... rounded-lg cursor-default',
  variants: {
    variant: {
      primary: 'bg-blue-600 hover:bg-blue-700 pressed:bg-blue-800 text-white',
      secondary: 'border-black/10 bg-neutral-50 hover:bg-neutral-100 pressed:bg-neutral-200 ...'
    },
    isDisabled: {
      true: 'border-transparent bg-neutral-100 text-neutral-300 ...'
    }
  },
  defaultVariants: {variant: 'primary'}
});

export function Button(props: ButtonProps) {
  return (
    <RACButton
      {...props}
      className={composeRenderProps(props.className, (className, renderProps) =>
        button({...renderProps, variant: props.variant, className})
      )}
    />
  );
}
```

`composeRenderProps` merges any `className` the consumer passed in with the component's own render-state-driven styles, and `renderProps` carries the live interaction state (`isPressed`, `isHovered`, `isFocusVisible`, `isDisabled`, ...) straight into the `tailwind-variants` config — the same state that also lands on the DOM node as `data-pressed`, `data-hovered`, etc.

## Reference Files

- **[references/hooks.md](references/hooks.md)** — The low-level `@react-aria/*` hook layer: `useButton`, `useTextField`, `useCheckbox`, and when to drop down to hooks instead of RAC components.
- **[references/components.md](references/components.md)** — The `react-aria-components` layer: real embedded source for ~17 components across Buttons/Toggles, Forms/Fields, Pickers/Menus, Overlays, Collections, and Date/Time.
- **[references/patterns.md](references/patterns.md)** — Cross-cutting patterns: composing forms with validation, the shared `items`/render-function API across collection components, overlay stacking/dismissal, and hook-vs-component decision points.
