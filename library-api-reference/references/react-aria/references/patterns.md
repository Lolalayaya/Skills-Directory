# Cross-Cutting Patterns

These are patterns that show up across multiple components in [components.md](components.md) rather than belonging to any single one. All source below is real, from the same Adobe Tailwind starter kit (`starters/tailwind/src/` in `adobe/react-spectrum`).

## Composing a Form From Shared Field Primitives

Every field-shaped component in `components.md` (`TextField`, `NumberField`, `Select`, `ComboBox`, `DatePicker`) is built from the same small set of shared primitives, all from `Field.tsx`:

```tsx
'use client';
import React from 'react';
import {type FieldErrorProps, FieldError as RACFieldError} from 'react-aria-components/FieldError';
import {Group, type GroupProps} from 'react-aria-components/Group';
import {type InputProps, Input as RACInput} from 'react-aria-components/Input';
import {type LabelProps, Label as RACLabel} from 'react-aria-components/Label';
import {Text, type TextProps} from 'react-aria-components/Text';
import {composeRenderProps} from 'react-aria-components/composeRenderProps';
import {twMerge} from 'tailwind-merge';
import {tv} from 'tailwind-variants';
import {composeTailwindRenderProps, focusRing} from './utils';

export function Label(props: LabelProps) {
  return (
    <RACLabel
      {...props}
      className={twMerge(
        'font-sans text-sm text-neutral-600 dark:text-neutral-300 font-medium cursor-default w-fit',
        props.className
      )}
    />
  );
}

export function Description(props: TextProps) {
  return (
    <Text
      {...props}
      slot="description"
      className={twMerge(
        'text-xs text-neutral-600 dark:text-neutral-400 group-disabled:text-neutral-200 dark:group-disabled:text-neutral-700 contain-inline-size',
        props.className
      )}
    />
  );
}

export function FieldError(props: FieldErrorProps) {
  return (
    <RACFieldError
      {...props}
      className={composeTailwindRenderProps(
        props.className,
        'text-xs text-red-600 contain-inline-size forced-colors:text-[Mark]'
      )}
    />
  );
}

export const fieldBorderStyles = tv({
  base: 'transition',
  variants: {
    isFocusWithin: {
      false: 'border-neutral-300 hover:border-neutral-400 dark:border-neutral-600 dark:hover:border-neutral-500 forced-colors:border-[ButtonBorder]',
      true: 'border-neutral-600 dark:border-neutral-300 forced-colors:border-[Highlight]'
    },
    isInvalid: {true: 'border-red-600 dark:border-red-600 forced-colors:border-[Mark]'},
    isDisabled: {true: 'border-neutral-200 dark:border-neutral-700 forced-colors:border-[GrayText]'}
  }
});

export const fieldGroupStyles = tv({
  extend: focusRing,
  base: 'group flex items-center h-9 box-border bg-white dark:bg-neutral-900 forced-colors:bg-[Field] border rounded-lg overflow-hidden transition',
  variants: fieldBorderStyles.variants
});

export function FieldGroup(props: GroupProps) {
  return (
    <Group
      {...props}
      className={composeRenderProps(props.className, (className, renderProps) =>
        fieldGroupStyles({...renderProps, className})
      )}
    />
  );
}

export function Input(props: InputProps) {
  return (
    <RACInput
      {...props}
      className={composeTailwindRenderProps(
        props.className,
        'px-3 py-0 min-h-9 flex-1 min-w-0 border-0 outline outline-0 bg-white dark:bg-neutral-900 font-sans text-sm text-neutral-800 dark:text-neutral-200 placeholder:text-neutral-600 dark:placeholder:text-neutral-400 disabled:text-neutral-200 dark:disabled:text-neutral-600 disabled:placeholder:text-neutral-200 dark:disabled:placeholder:text-neutral-600 [-webkit-tap-highlight-color:transparent]'
      )}
    />
  );
}
```

The pattern every field component in `components.md` follows: `Label` (associated via RAC's own id-wiring, not manual `htmlFor`), an optional `Description`, the actual input surface (`Input` directly, or `FieldGroup` wrapping `Input` + a trigger/stepper button for `NumberField`/`ComboBox`/`DatePicker`), then `FieldError` last. `fieldBorderStyles`/`fieldGroupStyles` centralize the focus/invalid/disabled border treatment so every field looks consistent without each component re-deriving it — `TextField`'s own `inputStyles` in `components.md` extends `fieldBorderStyles.variants` directly rather than redefining those states.

Validation wiring: `FieldError` renders nothing until the field's own validation state says otherwise (RAC handles this internally) — pass `errorMessage` as a plain string for a static message, or a function `(validation: ValidationResult) => string` to render different text per failing constraint.

## Collections Share One `items` / Render-Function API

`ListBox`, `Table`'s rows, `Select`'s options, `ComboBox`'s options, and `Menu`'s items all accept the same shape: either static JSX children, or an `items` prop (an iterable of data) paired with `children` as a `(item: T) => ReactNode` render function. This is why `Select` and `ComboBox` in `components.md` both render their options through the same `ListBox`/`DropdownItem` — they're not reimplementing selection behavior, they're composing the shared collection primitive.

Practical implication: build one item-rendering function per data shape once, and reuse it across whichever collection component (`ListBox`, `Select`, `ComboBox`, `Menu`) needs to display that data — don't hand-roll a separate `.map()` per component.

## Overlay Stacking & Dismissal (Modal / Popover / Dialog)

`Modal`, `Popover`, and `Dialog` in `components.md` are deliberately three separate, composable layers rather than one monolithic "modal component":

- **`Dialog`** — just the ARIA `dialog` role, a focus-trap boundary, and content padding. It does not render any backdrop or positioning itself.
- **`Modal`** (built from RAC's `ModalOverlay` + `Modal`) — the full-screen backdrop and centered surface, with `isEntering`/`isExiting` render-state hooked to enter/exit animation classes. Dismiss-on-backdrop-click and Escape are handled by `ModalOverlay` automatically.
- **`Popover`** (real source, from `Popover.tsx`) — the trigger-anchored, positioned surface (used by `Select`, `ComboBox`, `MenuTrigger`, `DatePicker`'s calendar) instead of a centered modal:

```tsx
'use client';
import {
  OverlayArrow,
  Popover as AriaPopover,
  type PopoverProps as AriaPopoverProps
} from 'react-aria-components/Popover';
import {composeRenderProps} from 'react-aria-components/composeRenderProps';
import React from 'react';
import {tv} from 'tailwind-variants';

export interface PopoverProps extends Omit<AriaPopoverProps, 'children'> {
  showArrow?: boolean;
  children: React.ReactNode;
}

const styles = tv({
  base: 'font-sans bg-white dark:bg-neutral-900/70 dark:backdrop-blur-2xl dark:backdrop-saturate-200 forced-colors:bg-[Canvas] shadow-2xl rounded-xl bg-clip-padding border border-black/10 dark:border-white/10 text-neutral-700 dark:text-neutral-300 outline-0 overflow-auto',
  variants: {
    isEntering: {
      true: 'animate-in fade-in placement-bottom:slide-in-from-top-1 placement-top:slide-in-from-bottom-1 placement-left:slide-in-from-right-1 placement-right:slide-in-from-left-1 ease-out duration-200'
    },
    isExiting: {
      true: 'animate-out fade-out placement-bottom:slide-out-to-top-1 placement-top:slide-out-to-bottom-1 placement-left:slide-out-to-right-1 placement-right:slide-out-to-left-1 ease-in duration-150'
    }
  }
});

export function Popover({children, showArrow, className, ...props}: PopoverProps) {
  let offset = showArrow ? 12 : 8;
  return (
    <AriaPopover
      offset={offset}
      {...props}
      className={composeRenderProps(className, (className, renderProps) =>
        styles({...renderProps, className})
      )}>
      {showArrow && (
        <OverlayArrow className="group">
          <svg width={12} height={12} viewBox="0 0 12 12" className="block fill-white dark:fill-[#1f1f21] forced-colors:fill-[Canvas] stroke-1 stroke-black/10 dark:stroke-neutral-700 forced-colors:stroke-[ButtonBorder] group-placement-bottom:rotate-180 group-placement-left:-rotate-90 group-placement-right:rotate-90">
            <path d="M0 0 L6 6 L12 0" />
          </svg>
        </OverlayArrow>
      )}
      {children}
    </AriaPopover>
  );
}
```

Rule of thumb: reach for `Dialog` inside `Modal` for anything that should feel like it owns the whole screen and blocks interaction with everything else (confirmation dialogs, forms that need full attention); reach for `Popover` (optionally wrapping a `Dialog` too, for a "popover with a focus-trapped form inside" pattern) for anything anchored to a specific trigger element that the user can dismiss by clicking elsewhere — that's what `Select`, `ComboBox`, and `MenuTrigger` all do in `components.md`. `Tooltip` is a third, lighter category: non-interactive and hover/focus-triggered rather than click-triggered, never focus-trapped.

Both `Modal` and `Popover` expose `isEntering`/`isExiting` as render props specifically so exit animations can play before the element actually unmounts — don't conditionally render based on your own boolean state and skip this, or exit transitions silently never play.

## When to Drop to a Hook Instead of a Full Component

Cross-reference [hooks.md](hooks.md) for the full explanation. In the context of the components above specifically: if `components.md`'s `Table`, `ListBox`, or `Menu` don't support a layout/interaction you need (a non-standard grid shape, a custom drag source, etc.), that's the signal to drop to the underlying `@react-aria/*` hook layer for just that one piece — not to abandon RAC for the rest of the app. Mixing layers per-component is normal; you don't have to pick one layer for an entire project.
