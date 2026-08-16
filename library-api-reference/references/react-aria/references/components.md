# React Aria Components (`react-aria-components`)

Over 50 unstyled, behavior-complete components, ready for your own styles. Every example below is real source pulled directly from Adobe's official Tailwind starter kit — `starters/tailwind/src/` in `adobe/react-spectrum` (raw base: `https://raw.githubusercontent.com/adobe/react-spectrum/main/starters/tailwind/src/`). These are Adobe's own reference implementations, not invented usage — copy the patterns, not necessarily every Tailwind class verbatim.

Every component below composes the primitives from `Field.tsx` (`Label`, `Description`, `FieldError`, `FieldGroup`, `Input`) and `utils.ts` (`focusRing`, `composeTailwindRenderProps`) also shipped in the same starter directory — see [patterns.md](patterns.md) for how those fit together.

---

## Buttons & Toggles

### Button

Wraps a press-interaction primitive (mouse, touch, keyboard, screen reader all normalized through `onPress`) with variant styling.

```tsx
'use client';
import React from 'react';
import {composeRenderProps} from 'react-aria-components/composeRenderProps';
import {
  Button as RACButton,
  type ButtonProps as RACButtonProps
} from 'react-aria-components/Button';
import {tv} from 'tailwind-variants';
import {focusRing} from './utils';

export interface ButtonProps extends RACButtonProps {
  /** @default 'primary' */
  variant?: 'primary' | 'secondary' | 'destructive' | 'quiet';
}

let button = tv({
  extend: focusRing,
  base: 'relative inline-flex items-center justify-center gap-2 border border-transparent dark:border-white/10 h-9 box-border px-3.5 py-0 [&:has(>svg:only-child)]:px-0 [&:has(>svg:only-child)]:h-8 [&:has(>svg:only-child)]:w-8 font-sans text-sm text-center transition rounded-lg cursor-default [-webkit-tap-highlight-color:transparent]',
  variants: {
    variant: {
      primary: 'bg-blue-600 hover:bg-blue-700 pressed:bg-blue-800 text-white',
      secondary:
        'border-black/10 bg-neutral-50 hover:bg-neutral-100 pressed:bg-neutral-200 text-neutral-800 dark:bg-neutral-700 dark:hover:bg-neutral-600 dark:pressed:bg-neutral-500 dark:text-neutral-100',
      destructive: 'bg-red-700 hover:bg-red-800 pressed:bg-red-900 text-white',
      quiet:
        'border-0 bg-transparent hover:bg-neutral-200 pressed:bg-neutral-300 text-neutral-800 dark:hover:bg-neutral-700 dark:pressed:bg-neutral-600 dark:text-neutral-100'
    },
    isDisabled: {
      true: 'border-transparent dark:border-transparent bg-neutral-100 dark:bg-neutral-800 text-neutral-300 dark:text-neutral-600 forced-colors:text-[GrayText]'
    },
    isPending: {
      true: 'text-transparent'
    }
  },
  defaultVariants: {
    variant: 'primary'
  },
  compoundVariants: [
    {
      variant: 'quiet',
      isDisabled: true,
      class: 'bg-transparent dark:bg-transparent'
    }
  ]
});

export function Button(props: ButtonProps) {
  return (
    <RACButton
      {...props}
      className={composeRenderProps(props.className, (className, renderProps) =>
        button({...renderProps, variant: props.variant, className})
      )}>
      {composeRenderProps(props.children, (children, {isPending}) => (
        <>
          {children}
          {isPending && (
            <span aria-hidden className="flex absolute inset-0 justify-center items-center">
              <svg
                className="w-4 h-4 text-white animate-spin"
                viewBox="0 0 24 24"
                stroke={
                  props.variant === 'secondary' || props.variant === 'quiet'
                    ? 'light-dark(black, white)'
                    : 'white'
                }>
                <circle cx="12" cy="12" r="10" strokeWidth="4" fill="none" className="opacity-25" />
                <circle
                  cx="12"
                  cy="12"
                  r="10"
                  strokeWidth="4"
                  strokeLinecap="round"
                  fill="none"
                  pathLength="100"
                  strokeDasharray="60 140"
                  strokeDashoffset="0"
                />
              </svg>
            </span>
          )}
        </>
      ))}
    </RACButton>
  );
}
```

### ToggleButton

Wraps a two-state (pressed/not-pressed) toggle button, exposing `isSelected` via render props/`data-selected` instead of `Button`'s momentary press state.

```tsx
'use client';
import React from 'react';
import {
  ToggleButton as RACToggleButton,
  type ToggleButtonProps
} from 'react-aria-components/ToggleButton';
import {composeRenderProps} from 'react-aria-components/composeRenderProps';
import {tv} from 'tailwind-variants';
import {focusRing} from './utils';

let styles = tv({
  extend: focusRing,
  base: 'relative inline-flex items-center justify-center gap-2 border border-black/10 dark:border-white/10 h-9 box-border px-3.5 [&:has(>svg:only-child)]:px-0 [&:has(>svg:only-child)]:h-8 [&:has(>svg:only-child)]:aspect-square font-sans text-sm text-center transition rounded-lg cursor-default forced-color-adjust-none [-webkit-tap-highlight-color:transparent]',
  variants: {
    isSelected: {
      false:
        'bg-neutral-50 hover:bg-neutral-100 pressed:bg-neutral-200 text-neutral-800 dark:bg-neutral-700 dark:hover:bg-neutral-600 dark:pressed:bg-neutral-500 dark:text-neutral-100 forced-colors:bg-[ButtonFace]! forced-colors:text-[ButtonText]!',
      true: 'bg-neutral-700 hover:bg-neutral-800 pressed:bg-neutral-900 text-white dark:bg-neutral-300 dark:hover:bg-neutral-200 dark:pressed:bg-neutral-100 dark:text-black forced-colors:bg-[Highlight]! forced-colors:text-[HighlightText]!'
    },
    isDisabled: {
      true: 'border-transparent dark:border-transparent bg-neutral-100 dark:bg-neutral-800 forced-colors:bg-[ButtonFace]! text-neutral-300 dark:text-neutral-600 forced-colors:text-[GrayText]!'
    }
  }
});

export function ToggleButton(props: ToggleButtonProps) {
  return (
    <RACToggleButton
      {...props}
      className={composeRenderProps(props.className, (className, renderProps) =>
        styles({...renderProps, className})
      )}
    />
  );
}
```

### Switch

Wraps an on/off toggle-switch pattern; composed from RAC's `SwitchField` + `SwitchButton` slot pair plus this starter's shared `Description`/`FieldError` field primitives.

```tsx
'use client';
import React from 'react';
import {
  SwitchField,
  SwitchButton,
  type SwitchFieldProps,
  type ValidationResult
} from 'react-aria-components/Switch';
import {tv} from 'tailwind-variants';
import {composeTailwindRenderProps, focusRing} from './utils';
import {Description, FieldError} from './Field';

export interface SwitchProps extends Omit<SwitchFieldProps, 'children'> {
  children: React.ReactNode;
  description?: string;
  errorMessage?: string | ((validation: ValidationResult) => string);
}

const track = tv({
  extend: focusRing,
  base: 'flex h-5 w-9 box-border px-px items-center shrink-0 cursor-default rounded-full transition duration-200 ease-in-out shadow-inner border border-transparent font-sans',
  variants: {
    isSelected: {
      false:
        'bg-neutral-100 dark:bg-neutral-800 group-pressed:bg-neutral-200 dark:group-pressed:bg-neutral-700 border-neutral-400 dark:border-neutral-400',
      true: 'bg-neutral-700 dark:bg-neutral-300 forced-colors:bg-[Highlight]! group-pressed:bg-neutral-800 dark:group-pressed:bg-neutral-200'
    },
    isDisabled: {
      true: 'bg-neutral-100 dark:bg-neutral-800 group-selected:bg-neutral-300 dark:group-selected:bg-neutral-800 forced-colors:group-selected:bg-[GrayText]! border-neutral-300 dark:border-neutral-900 forced-colors:border-[GrayText]'
    }
  }
});

const handle = tv({
  base: 'h-4 w-4 transform rounded-full outline outline-1 -outline-offset-1 outline-transparent shadow-xs transition duration-200 ease-in-out',
  variants: {
    isSelected: {
      false: 'translate-x-0 bg-neutral-900 dark:bg-neutral-300',
      true: 'translate-x-[100%] bg-white dark:bg-neutral-900'
    },
    isDisabled: {
      true: 'forced-colors:outline-[GrayText]'
    }
  },
  compoundVariants: [
    {
      isSelected: false,
      isDisabled: true,
      class: 'bg-neutral-300 dark:bg-neutral-700'
    },
    {
      isSelected: true,
      isDisabled: true,
      class: 'bg-neutral-50 dark:bg-neutral-700'
    }
  ]
});

export function Switch({children, ...props}: SwitchProps) {
  return (
    <SwitchField {...props} className="flex flex-col gap-1 group">
      <SwitchButton
        className={composeTailwindRenderProps(
          props.className,
          'group relative flex gap-2 items-center text-neutral-800 disabled:text-neutral-300 dark:text-neutral-200 dark:disabled:text-neutral-600 forced-colors:disabled:text-[GrayText] text-sm transition [-webkit-tap-highlight-color:transparent]'
        )}>
        {renderProps => (
          <>
            <div className={track(renderProps)}>
              <span className={handle(renderProps)} />
            </div>
            {children}
          </>
        )}
      </SwitchButton>
      {props.description && <Description>{props.description}</Description>}
      <FieldError>{props.errorMessage}</FieldError>
    </SwitchField>
  );
}
```

---

## Forms & Fields

### TextField

Wraps a labeled single-line (or multi-line, via the underlying hook) text input with built-in label/description/error-message association.

```tsx
'use client';
import React from 'react';
import {
  TextField as AriaTextField,
  type TextFieldProps as AriaTextFieldProps,
  type ValidationResult
} from 'react-aria-components/TextField';
import {tv} from 'tailwind-variants';
import {Description, FieldError, Input, Label, fieldBorderStyles} from './Field';
import {composeTailwindRenderProps, focusRing} from './utils';

const inputStyles = tv({
  extend: focusRing,
  base: 'border-1 rounded-lg min-h-9 font-sans text-sm py-0 px-3 box-border transition',
  variants: {
    isFocused: fieldBorderStyles.variants.isFocusWithin,
    isInvalid: fieldBorderStyles.variants.isInvalid,
    isDisabled: fieldBorderStyles.variants.isDisabled
  }
});

export interface TextFieldProps extends AriaTextFieldProps {
  label?: string;
  description?: string;
  placeholder?: string;
  errorMessage?: string | ((validation: ValidationResult) => string);
}

export function TextField({label, description, errorMessage, ...props}: TextFieldProps) {
  return (
    <AriaTextField
      {...props}
      className={composeTailwindRenderProps(props.className, 'flex flex-col gap-1 font-sans')}>
      {label && <Label>{label}</Label>}
      <Input className={inputStyles} />
      {description && <Description>{description}</Description>}
      <FieldError>{errorMessage}</FieldError>
    </AriaTextField>
  );
}
```

### NumberField

Wraps a numeric input with locale-aware parsing/formatting plus increment/decrement stepper buttons.

```tsx
'use client';
import {ChevronDown, ChevronUp} from 'lucide-react';
import React from 'react';
import {
  NumberField as AriaNumberField,
  type NumberFieldProps as AriaNumberFieldProps,
  Button,
  type ButtonProps,
  type ValidationResult
} from 'react-aria-components/NumberField';
import {Description, FieldError, FieldGroup, Input, Label, fieldBorderStyles} from './Field';
import {composeTailwindRenderProps} from './utils';

export interface NumberFieldProps extends AriaNumberFieldProps {
  label?: string;
  description?: string;
  errorMessage?: string | ((validation: ValidationResult) => string);
  placeholder?: string;
}

export function NumberField({
  label,
  description,
  errorMessage,
  placeholder,
  ...props
}: NumberFieldProps) {
  return (
    <AriaNumberField
      {...props}
      className={composeTailwindRenderProps(
        props.className,
        'group flex flex-col gap-1 font-sans'
      )}>
      <Label>{label}</Label>
      <FieldGroup>
        {renderProps => (
          <>
            <Input className="w-20" placeholder={placeholder} />
            <div
              className={fieldBorderStyles({
                ...renderProps,
                class: 'flex flex-col border-s h-full'
              })}>
              <StepperButton slot="increment">
                <ChevronUp aria-hidden className="w-4 h-4" />
              </StepperButton>
              <div className={fieldBorderStyles({...renderProps, class: 'border-b'})} />
              <StepperButton slot="decrement">
                <ChevronDown aria-hidden className="w-4 h-4" />
              </StepperButton>
            </div>
          </>
        )}
      </FieldGroup>
      {description && <Description>{description}</Description>}
      <FieldError>{errorMessage}</FieldError>
    </AriaNumberField>
  );
}

function StepperButton(props: ButtonProps) {
  return (
    <Button
      {...props}
      className="flex border-0 py-0 px-0.5 flex-1 box-border cursor-default text-neutral-500 bg-transparent pressed:bg-neutral-100 group-disabled:text-neutral-200 dark:text-neutral-400 dark:pressed:bg-neutral-800 dark:group-disabled:text-neutral-600 forced-colors:group-disabled:text-[GrayText] [-webkit-tap-highlight-color:transparent]"
    />
  );
}
```

### Checkbox

Wraps a tri-state (checked/unchecked/indeterminate) checkbox, built on RAC's `CheckboxField`/`CheckboxButton` slot pair.

```tsx
'use client';
import {Check, Minus} from 'lucide-react';
import React from 'react';
import {
  CheckboxField,
  CheckboxButton,
  type CheckboxFieldProps,
  type ValidationResult
} from 'react-aria-components/Checkbox';
import {composeRenderProps} from 'react-aria-components/composeRenderProps';
import {tv} from 'tailwind-variants';
import {focusRing} from './utils';
import {Description, FieldError} from './Field';

const checkboxStyles = tv({
  base: 'flex gap-2 items-center group font-sans text-sm transition relative [-webkit-tap-highlight-color:transparent]',
  variants: {
    isDisabled: {
      false: 'text-neutral-800 dark:text-neutral-200',
      true: 'text-neutral-300 dark:text-neutral-600 forced-colors:text-[GrayText]'
    }
  }
});

const boxStyles = tv({
  extend: focusRing,
  base: 'w-4.5 h-4.5 box-border shrink-0 rounded-sm flex items-center justify-center border transition',
  variants: {
    isSelected: {
      false:
        'bg-white dark:bg-neutral-900 border-(--color) [--color:var(--color-neutral-400)] dark:[--color:var(--color-neutral-400)] group-pressed:[--color:var(--color-neutral-500)] dark:group-pressed:[--color:var(--color-neutral-300)]',
      true: 'bg-(--color) border-(--color) [--color:var(--color-neutral-700)] group-pressed:[--color:var(--color-neutral-800)] dark:[--color:var(--color-neutral-300)] dark:group-pressed:[--color:var(--color-neutral-200)] forced-colors:[--color:Highlight]!'
    },
    isInvalid: {
      true: '[--color:var(--color-red-700)] dark:[--color:var(--color-red-600)] forced-colors:[--color:Mark]! group-pressed:[--color:var(--color-red-800)] dark:group-pressed:[--color:var(--color-red-700)]'
    },
    isDisabled: {
      true: '[--color:var(--color-neutral-200)] dark:[--color:var(--color-neutral-700)] forced-colors:[--color:GrayText]!'
    }
  }
});

const iconStyles =
  'w-3.5 h-3.5 text-white group-disabled:text-neutral-400 dark:text-neutral-900 dark:group-disabled:text-neutral-600 forced-colors:text-[HighlightText] pointer-events-none';

interface CheckboxProps extends CheckboxFieldProps {
  children?: React.ReactNode;
  description?: string;
  errorMessage?: string | ((validation: ValidationResult) => string);
}

export function Checkbox(props: CheckboxProps) {
  return (
    <CheckboxField {...props} className="flex flex-col gap-1 group">
      <CheckboxButton
        className={composeRenderProps(props.className, (className, renderProps) =>
          checkboxStyles({...renderProps, className})
        )}>
        {composeRenderProps(
          props.children,
          (children, {isSelected, isIndeterminate, ...renderProps}) => (
            <>
              <div
                className={boxStyles({isSelected: isSelected || isIndeterminate, ...renderProps})}>
                {isIndeterminate ? (
                  <Minus aria-hidden className={iconStyles} />
                ) : isSelected ? (
                  <Check aria-hidden className={iconStyles} />
                ) : null}
              </div>
              {children}
            </>
          )
        )}
      </CheckboxButton>
      {props.description && <Description className="ms-6.5">{props.description}</Description>}
      <FieldError className="ms-6.5">{props.errorMessage}</FieldError>
    </CheckboxField>
  );
}
```

### RadioGroup

Wraps single-selection radio-button groups, managing roving tabindex/arrow-key navigation across `Radio` children automatically.

```tsx
'use client';
import React, {type ReactNode} from 'react';
import {composeRenderProps} from 'react-aria-components/composeRenderProps';
import {
  RadioField,
  RadioButton,
  RadioGroup as RACRadioGroup,
  type RadioGroupProps as RACRadioGroupProps,
  type RadioFieldProps,
  type ValidationResult
} from 'react-aria-components/RadioGroup';
import {tv} from 'tailwind-variants';
import {Description, FieldError, Label} from './Field';
import {composeTailwindRenderProps, focusRing} from './utils';

export interface RadioGroupProps extends Omit<RACRadioGroupProps, 'children'> {
  label?: string;
  children?: ReactNode;
  description?: string;
  errorMessage?: string | ((validation: ValidationResult) => string);
}

export function RadioGroup(props: RadioGroupProps) {
  return (
    <RACRadioGroup
      {...props}
      className={composeTailwindRenderProps(
        props.className,
        'group flex flex-col gap-2 font-sans'
      )}>
      <Label>{props.label}</Label>
      <div className="flex group-orientation-vertical:flex-col gap-2 group-orientation-horizontal:gap-4">
        {props.children}
      </div>
      {props.description && <Description>{props.description}</Description>}
      <FieldError>{props.errorMessage}</FieldError>
    </RACRadioGroup>
  );
}

const styles = tv({
  extend: focusRing,
  base: 'w-4.5 h-4.5 flex-shrink-0 box-border rounded-full border bg-white dark:bg-neutral-900 transition-all',
  variants: {
    isSelected: {
      false:
        'border-neutral-400 dark:border-neutral-400 group-pressed:border-neutral-500 dark:group-pressed:border-neutral-300',
      true: 'border-[calc(var(--spacing)*1.5)] border-neutral-700 dark:border-neutral-300 forced-colors:border-[Highlight]! group-pressed:border-neutral-800 dark:group-pressed:border-neutral-200'
    },
    isInvalid: {
      true: 'border-red-700 dark:border-red-600 group-pressed:border-red-800 dark:group-pressed:border-red-700 forced-colors:border-[Mark]!'
    },
    isDisabled: {
      true: 'border-neutral-200 dark:border-neutral-700 forced-colors:border-[GrayText]!'
    }
  }
});

export interface RadioProps extends RadioFieldProps {
  description?: string;
}

export function Radio(props: RadioProps) {
  return (
    <RadioField {...props} className="flex flex-col gap-1 group">
      <RadioButton
        className={composeTailwindRenderProps(
          props.className,
          'flex relative gap-2 items-center group text-neutral-800 disabled:text-neutral-300 dark:text-neutral-200 dark:disabled:text-neutral-600 forced-colors:disabled:text-[GrayText] text-sm transition [-webkit-tap-highlight-color:transparent]'
        )}>
        {composeRenderProps(props.children, (children, renderProps) => (
          <>
            <div className={styles(renderProps)} />
            {children}
          </>
        ))}
      </RadioButton>
      {props.description && <Description className="ms-6.5">{props.description}</Description>}
    </RadioField>
  );
}
```

---

## Pickers & Menus

### Select

Wraps a listbox-backed, single/multi-select dropdown trigger (native `<select>` replacement) with full keyboard typeahead and a `Popover` for the options.

```tsx
'use client';
import {ChevronDown} from 'lucide-react';
import React from 'react';
import {
  Select as AriaSelect,
  type SelectProps as AriaSelectProps,
  Button,
  ListBox,
  type ListBoxItemProps,
  SelectValue,
  type ValidationResult
} from 'react-aria-components/Select';
import {tv} from 'tailwind-variants';
import {Description, FieldError, Label} from './Field';
import {DropdownItem, DropdownSection, type DropdownSectionProps} from './ListBox';
import {Popover} from './Popover';
import {composeTailwindRenderProps, focusRing} from './utils';

const styles = tv({
  extend: focusRing,
  base: 'flex items-center text-start gap-4 w-full font-sans border border-black/10 dark:border-white/10 cursor-default rounded-lg pl-3 pr-2 h-9 min-w-[180px] transition bg-neutral-50 dark:bg-neutral-700 [-webkit-tap-highlight-color:transparent]',
  variants: {
    isDisabled: {
      false:
        'text-neutral-800 dark:text-neutral-300 hover:bg-neutral-100 pressed:bg-neutral-200 dark:hover:bg-neutral-600 dark:pressed:bg-neutral-500 group-invalid:outline group-invalid:outline-red-600 forced-colors:group-invalid:outline-[Mark]',
      true: 'border-transparent dark:border-transparent text-neutral-200 dark:text-neutral-600 forced-colors:text-[GrayText] bg-neutral-100 dark:bg-neutral-800'
    }
  }
});

export interface SelectProps<T, M extends 'single' | 'multiple'> extends Omit<
  AriaSelectProps<T, M>,
  'children'
> {
  label?: string;
  description?: string;
  errorMessage?: string | ((validation: ValidationResult) => string);
  items?: Iterable<T>;
  children: React.ReactNode | ((item: T) => React.ReactNode);
}

export function Select<T, M extends 'single' | 'multiple' = 'single'>({
  label,
  description,
  errorMessage,
  children,
  items,
  ...props
}: SelectProps<T, M>) {
  return (
    <AriaSelect
      {...props}
      className={composeTailwindRenderProps(
        props.className,
        'group flex flex-col gap-1 relative font-sans'
      )}>
      {label && <Label>{label}</Label>}
      <Button className={styles}>
        <SelectValue className="flex-1 text-sm">
          {({selectedText, defaultChildren}) => selectedText || defaultChildren}
        </SelectValue>
        <ChevronDown
          aria-hidden
          className="w-4 h-4 text-neutral-600 dark:text-neutral-400 forced-colors:text-[ButtonText] group-disabled:text-neutral-200 dark:group-disabled:text-neutral-600 forced-colors:group-disabled:text-[GrayText]"
        />
      </Button>
      {description && <Description>{description}</Description>}
      <FieldError>{errorMessage}</FieldError>
      <Popover className="min-w-(--trigger-width)">
        <ListBox
          items={items}
          className="outline-hidden box-border p-1 max-h-[inherit] overflow-auto [clip-path:inset(0_0_0_0_round_.75rem)]">
          {children}
        </ListBox>
      </Popover>
    </AriaSelect>
  );
}

export function SelectItem(props: ListBoxItemProps) {
  return <DropdownItem {...props} />;
}

export function SelectSection<T>(props: DropdownSectionProps<T>) {
  return <DropdownSection {...props} />;
}
```

### ComboBox

Wraps a filterable, type-to-search combo of text input + listbox popover — like `Select` but with free-text filtering of the options.

```tsx
'use client';
import {ChevronDown} from 'lucide-react';
import React from 'react';
import {
  ComboBox as AriaComboBox,
  type ComboBoxProps as AriaComboBoxProps,
  ComboBoxValue,
  ListBox,
  type ListBoxItemProps,
  type ValidationResult
} from 'react-aria-components/ComboBox';
import {Description, FieldError, FieldGroup, Input, Label} from './Field';
import {DropdownItem, DropdownSection, type DropdownSectionProps} from './ListBox';
import {Popover} from './Popover';
import {composeTailwindRenderProps} from './utils';
import {FieldButton} from './FieldButton';

export interface ComboBoxProps<T, M extends 'single' | 'multiple'> extends Omit<
  AriaComboBoxProps<T, M>,
  'children'
> {
  label?: string;
  description?: string | null;
  errorMessage?: string | ((validation: ValidationResult) => string);
  placeholder?: string;
  children: React.ReactNode | ((item: T) => React.ReactNode);
}

export function ComboBox<T, M extends 'single' | 'multiple' = 'single'>({
  label,
  description,
  errorMessage,
  children,
  items,
  ...props
}: ComboBoxProps<T, M>) {
  return (
    <AriaComboBox
      {...props}
      className={composeTailwindRenderProps(
        props.className,
        'group flex flex-col gap-1 font-sans'
      )}>
      <Label>{label}</Label>
      <FieldGroup>
        <Input className="ps-3 pe-1" />
        <FieldButton className="w-6 mr-1 outline-offset-0">
          <ChevronDown aria-hidden className="w-4 h-4" />
        </FieldButton>
      </FieldGroup>
      {props.selectionMode === 'multiple' && (
        <ComboBoxValue
          placeholder="No items selected"
          className="text-xs text-neutral-600 dark:text-neutral-300"
        />
      )}
      {description && <Description>{description}</Description>}
      <FieldError>{errorMessage}</FieldError>
      <Popover className="w-(--trigger-width)">
        <ListBox
          items={items}
          className="outline-0 p-1 box-border max-h-[inherit] overflow-auto [clip-path:inset(0_0_0_0_round_.75rem)]">
          {children}
        </ListBox>
      </Popover>
    </AriaComboBox>
  );
}

export function ComboBoxItem(props: ListBoxItemProps) {
  return <DropdownItem {...props} />;
}

export function ComboBoxSection<T>(props: DropdownSectionProps<T>) {
  return <DropdownSection {...props} />;
}
```

### Menu

Wraps an action menu (as opposed to a selection listbox) — press-to-activate items, optional submenus, sections, and separators, opened via `MenuTrigger`.

```tsx
'use client';
import {Check, ChevronRight} from 'lucide-react';
import React from 'react';
import {
  Menu as AriaMenu,
  MenuItem as AriaMenuItem,
  type MenuProps,
  type MenuItemProps,
  MenuSection as AriaMenuSection,
  type MenuSectionProps as AriaMenuSectionProps,
  MenuTrigger as AriaMenuTrigger,
  SubmenuTrigger as AriaSubmenuTrigger,
  Separator,
  type SeparatorProps,
  Header,
  Collection,
  type SubmenuTriggerProps,
  type MenuTriggerProps as AriaMenuTriggerProps
} from 'react-aria-components/Menu';
import {composeRenderProps} from 'react-aria-components/composeRenderProps';
import {dropdownItemStyles} from './ListBox';
import {Popover, type PopoverProps} from './Popover';

export function Menu<T>(props: MenuProps<T>) {
  return (
    <AriaMenu
      {...props}
      className="font-sans p-1 outline outline-0 max-h-[inherit] overflow-auto [clip-path:inset(0_0_0_0_round_.75rem)] empty:text-center empty:pb-2"
    />
  );
}

export function MenuItem(props: MenuItemProps) {
  let textValue =
    props.textValue || (typeof props.children === 'string' ? props.children : undefined);
  return (
    <AriaMenuItem textValue={textValue} {...props} className={dropdownItemStyles}>
      {composeRenderProps(props.children, (children, {selectionMode, isSelected, hasSubmenu}) => (
        <>
          {selectionMode !== 'none' && (
            <span className="flex items-center w-4">
              {isSelected && <Check aria-hidden className="w-4 h-4" />}
            </span>
          )}
          <span className="flex items-center flex-1 gap-2 font-normal truncate group-selected:font-semibold">
            {children}
          </span>
          {hasSubmenu && <ChevronRight aria-hidden className="absolute w-4 h-4 right-2" />}
        </>
      ))}
    </AriaMenuItem>
  );
}

export function MenuSeparator(props: SeparatorProps) {
  return (
    <Separator
      {...props}
      className="mx-3 my-1 border-b border-neutral-300 dark:border-neutral-700"
    />
  );
}

export interface MenuSectionProps<T> extends AriaMenuSectionProps<T> {
  title?: string;
  items?: any;
}

export function MenuSection<T>(props: MenuSectionProps<T>) {
  return (
    <AriaMenuSection
      {...props}
      className="first:-mt-[5px] after:content-[''] after:block after:h-[5px]">
      {props.title && (
        <Header className="text-sm font-semibold text-neutral-500 dark:text-neutral-300 px-4 py-1 truncate sticky -top-[5px] -mt-px -mx-1 z-10 bg-neutral-100/60 dark:bg-neutral-700/60 backdrop-blur-md supports-[-moz-appearance:none]:bg-neutral-100 border-y border-y-neutral-200 dark:border-y-neutral-700 [&+*]:mt-1">
          {props.title}
        </Header>
      )}
      <Collection items={props.items}>{props.children}</Collection>
    </AriaMenuSection>
  );
}

interface MenuTriggerProps extends AriaMenuTriggerProps {
  placement?: PopoverProps['placement'];
}

export function MenuTrigger(props: MenuTriggerProps) {
  let [trigger, menu] = React.Children.toArray(props.children) as [
    React.ReactElement,
    React.ReactElement
  ];
  return (
    <AriaMenuTrigger {...props}>
      {trigger}
      <Popover placement={props.placement} className="min-w-[150px]">
        {menu}
      </Popover>
    </AriaMenuTrigger>
  );
}

export function SubmenuTrigger(props: SubmenuTriggerProps) {
  let [trigger, menu] = React.Children.toArray(props.children) as [
    React.ReactElement,
    React.ReactElement
  ];
  return (
    <AriaSubmenuTrigger {...props}>
      {trigger}
      <Popover offset={-2} crossOffset={-4}>
        {menu}
      </Popover>
    </AriaSubmenuTrigger>
  );
}
```

---

## Overlays

### Dialog

Wraps the ARIA `dialog` role and focus-trap content region rendered inside a `Modal` or `Popover` — provides the `Heading` and content container, not the overlay/backdrop itself.

```tsx
'use client';
import React from 'react';
import {type DialogProps, Dialog as RACDialog, Heading} from 'react-aria-components/Dialog';
import {twMerge} from 'tailwind-merge';

export function Dialog(props: DialogProps) {
  return (
    <RACDialog
      {...props}
      className={twMerge(
        'outline outline-0 box-border p-6 [[data-placement]>&]:p-4 max-h-[inherit] overflow-auto relative',
        props.className
      )}
    />
  );
}

export {Heading};
```

### Modal

Wraps the full-screen backdrop (`ModalOverlay`) plus the centered modal surface (`Modal`) — handles enter/exit animation state (`isEntering`/`isExiting`) and dismiss-on-backdrop-click/Escape.

```tsx
'use client';
import React from 'react';
import {ModalOverlay, type ModalOverlayProps, Modal as RACModal} from 'react-aria-components/Modal';
import {tv} from 'tailwind-variants';

const overlayStyles = tv({
  base: 'absolute top-0 left-0 w-full h-(--page-height) isolate z-20 bg-black/[50%] text-center backdrop-blur-lg',
  variants: {
    isEntering: {
      true: 'animate-in fade-in duration-200 ease-out'
    },
    isExiting: {
      true: 'animate-out fade-out duration-200 ease-in'
    }
  }
});

const modalStyles = tv({
  base: 'font-sans w-full max-w-[min(90vw,450px)] max-h-[calc(var(--visual-viewport-height)*.9)] rounded-2xl bg-white dark:bg-neutral-800/70 dark:backdrop-blur-2xl dark:backdrop-saturate-200 forced-colors:bg-[Canvas] text-left align-middle text-neutral-700 dark:text-neutral-300 shadow-2xl bg-clip-padding border border-black/10 dark:border-white/10',
  variants: {
    isEntering: {
      true: 'animate-in zoom-in-105 ease-out duration-200'
    },
    isExiting: {
      true: 'animate-out zoom-out-95 ease-in duration-200'
    }
  }
});

export function Modal(props: ModalOverlayProps) {
  return (
    <ModalOverlay {...props} className={overlayStyles}>
      <div className="sticky top-0 left-0 w-full h-(--visual-viewport-height) flex items-center justify-center box-border">
        <RACModal {...props} className={modalStyles} />
      </div>
    </ModalOverlay>
  );
}
```

### Tooltip

Wraps a non-interactive, hover/focus-triggered overlay anchored to a trigger element, with an `OverlayArrow` pointing back at it.

```tsx
'use client';
import React from 'react';
import {
  Tooltip as AriaTooltip,
  type TooltipProps as AriaTooltipProps,
  OverlayArrow
} from 'react-aria-components/Tooltip';
import {composeRenderProps} from 'react-aria-components/composeRenderProps';
import {tv} from 'tailwind-variants';

export interface TooltipProps extends Omit<AriaTooltipProps, 'children'> {
  children: React.ReactNode;
}

const styles = tv({
  base: 'group bg-neutral-700 dark:bg-neutral-600 border border-neutral-800 dark:border-white/10 font-sans text-xs text-white rounded-lg drop-shadow-lg will-change-transform px-3 py-1.5 box-border',
  variants: {
    isEntering: {
      true: 'animate-in fade-in placement-bottom:slide-in-from-top-0.5 placement-top:slide-in-from-bottom-0.5 placement-left:slide-in-from-right-0.5 placement-right:slide-in-from-left-0.5 ease-out duration-200'
    },
    isExiting: {
      true: 'animate-out fade-out placement-bottom:slide-out-to-top-0.5 placement-top:slide-out-to-bottom-0.5 placement-left:slide-out-to-right-0.5 placement-right:slide-out-to-left-0.5 ease-in duration-150'
    }
  }
});

export function Tooltip({children, ...props}: TooltipProps) {
  return (
    <AriaTooltip
      {...props}
      offset={10}
      className={composeRenderProps(props.className, (className, renderProps) =>
        styles({...renderProps, className})
      )}>
      <OverlayArrow>
        <svg
          width={8}
          height={8}
          viewBox="0 0 8 8"
          className="block fill-neutral-700 dark:fill-neutral-600 forced-colors:fill-[Canvas] stroke-neutral-800 dark:stroke-white/10 forced-colors:stroke-[ButtonBorder] group-placement-bottom:rotate-180 group-placement-left:-rotate-90 group-placement-right:rotate-90">
          <path d="M0 0 L4 4 L8 0" />
        </svg>
      </OverlayArrow>
      {children}
    </AriaTooltip>
  );
}
```

---

## Collections

### ListBox

Wraps a selectable list of options with roving focus, type-ahead, and section grouping — the shared collection primitive that `Select` and `ComboBox` render their options through.

```tsx
'use client';
import {Check} from 'lucide-react';
import React from 'react';
import {
  ListBox as AriaListBox,
  ListBoxItem as AriaListBoxItem,
  ListBoxSection,
  Header,
  Collection,
  type ListBoxProps as AriaListBoxProps,
  type ListBoxItemProps,
  type ListBoxSectionProps
} from 'react-aria-components/ListBox';
import {composeRenderProps} from 'react-aria-components/composeRenderProps';
import {tv} from 'tailwind-variants';
import {composeTailwindRenderProps, focusRing} from './utils';

interface ListBoxProps<T> extends Omit<AriaListBoxProps<T>, 'layout' | 'orientation'> {}

export function ListBox<T>({children, ...props}: ListBoxProps<T>) {
  return (
    <AriaListBox
      {...props}
      className={composeTailwindRenderProps(
        props.className,
        'outline-0 p-1 w-[200px] bg-white dark:bg-neutral-900 border border-neutral-300 dark:border-neutral-700 rounded-lg font-sans'
      )}>
      {children}
    </AriaListBox>
  );
}

export const itemStyles = tv({
  extend: focusRing,
  base: 'group relative flex items-center gap-8 cursor-default select-none py-1.5 px-2.5 rounded-md will-change-transform text-sm forced-color-adjust-none',
  variants: {
    isSelected: {
      false:
        'text-neutral-700 dark:text-neutral-300 hover:bg-neutral-100 pressed:bg-neutral-100 dark:hover:bg-neutral-800 dark:pressed:bg-neutral-800 -outline-offset-2',
      true: 'bg-blue-600 text-white forced-colors:bg-[Highlight] forced-colors:text-[HighlightText] [&:has(+[data-selected])]:rounded-b-none [&+[data-selected]]:rounded-t-none -outline-offset-4 outline-white dark:outline-white forced-colors:outline-[HighlightText]'
    },
    isDisabled: {
      true: 'text-neutral-300 dark:text-neutral-600 forced-colors:text-[GrayText]'
    }
  }
});

export function ListBoxItem(props: ListBoxItemProps) {
  let textValue =
    props.textValue || (typeof props.children === 'string' ? props.children : undefined);
  return (
    <AriaListBoxItem {...props} textValue={textValue} className={itemStyles}>
      {composeRenderProps(props.children, children => (
        <>
          {children}
          <div className="absolute left-4 right-4 bottom-0 h-px bg-white/20 forced-colors:bg-[HighlightText] hidden [.group[data-selected]:has(+[data-selected])_&]:block" />
        </>
      ))}
    </AriaListBoxItem>
  );
}
```

*(The same file also exports `dropdownItemStyles`, `DropdownItem`, and `DropdownSection` — the shared item styling reused by `Select`, `ComboBox`, and `Menu` above.)*

### Table

Wraps a full ARIA grid: sortable/resizable columns (`ResizableTableContainer`, `ColumnResizer`), selection checkboxes, and tree-style expandable rows.

```tsx
'use client';
import {ArrowUp, ChevronRight} from 'lucide-react';
import React from 'react';
import {
  Cell as AriaCell,
  Column as AriaColumn,
  Row as AriaRow,
  Table as AriaTable,
  TableHeader as AriaTableHeader,
  TableBody as AriaTableBody,
  Button,
  type CellProps,
  Collection,
  type ColumnProps,
  ColumnResizer,
  ResizableTableContainer,
  type RowProps,
  type TableHeaderProps,
  type TableProps as AriaTableProps,
  useTableOptions,
  type TableBodyProps,
  TableFooter as AriaTableFooter,
  type TableFooterProps
} from 'react-aria-components/Table';
import {Group} from 'react-aria-components/Group';
import {composeRenderProps} from 'react-aria-components/composeRenderProps';
import {twMerge} from 'tailwind-merge';
import {tv} from 'tailwind-variants';
import {Checkbox} from './Checkbox';
import {composeTailwindRenderProps, focusRing} from './utils';

interface TableProps extends Omit<AriaTableProps, 'className'> {
  className?: string;
}

export function Table(props: TableProps) {
  return (
    <ResizableTableContainer
      onScroll={props.onScroll}
      className={twMerge(
        'w-full max-h-[320px] overflow-auto scroll-pt-[2.281rem] relative bg-white dark:bg-neutral-900 box-border border border-neutral-300 dark:border-neutral-700 rounded-lg font-sans',
        props.className
      )}>
      <AriaTable
        {...props}
        className="border-separate border-spacing-0 box-border overflow-hidden has-[>[data-empty]]:h-full"
      />
    </ResizableTableContainer>
  );
}

export function Column(props: ColumnProps) {
  return (
    <AriaColumn
      {...props}
      className={composeTailwindRenderProps(
        props.className,
        'box-border h-1 [&:hover]:z-20 focus-within:z-20 text-start text-sm font-semibold text-neutral-700 dark:text-neutral-300 cursor-default'
      )}>
      {composeRenderProps(props.children, (children, {allowsSorting, sortDirection}) => (
        <div className="flex items-center">
          <Group role="presentation" tabIndex={-1} className="px-2 h-5 box-border flex-1 flex gap-1 items-center overflow-hidden">
            <span className="truncate">{children}</span>
            {allowsSorting && (
              <span
                className={`w-4 h-4 flex items-center justify-center transition ${
                  sortDirection === 'descending' ? 'rotate-180' : ''
                }`}>
                {sortDirection && (
                  <ArrowUp
                    aria-hidden
                    className="w-4 h-4 text-neutral-500 dark:text-neutral-400 forced-colors:text-[ButtonText]"
                  />
                )}
              </span>
            )}
          </Group>
          {!props.width && <ColumnResizer className="w-px px-[8px] translate-x-[8px] box-content py-1 h-5 bg-clip-content bg-neutral-400 dark:bg-neutral-500 cursor-col-resize rounded-xs" />}
        </div>
      ))}
    </AriaColumn>
  );
}

export function TableHeader<T>(props: TableHeaderProps<T>) {
  let {selectionBehavior, selectionMode, allowsDragging} = useTableOptions();

  return (
    <AriaTableHeader
      {...props}
      className={composeTailwindRenderProps(
        props.className,
        'sticky top-0 z-10 bg-neutral-100/60 dark:bg-neutral-700/60 backdrop-blur-md rounded-t-lg border-b border-b-neutral-200 dark:border-b-neutral-700'
      )}>
      {/* Add extra columns for drag and drop and selection. */}
      {allowsDragging && <Column />}
      {selectionBehavior === 'toggle' && (
        <AriaColumn
          width={36}
          minWidth={36}
          className="box-border p-2 text-sm font-semibold cursor-default text-start">
          {selectionMode === 'multiple' && <Checkbox slot="selection" />}
        </AriaColumn>
      )}
      <Collection items={props.columns}>{props.children}</Collection>
    </AriaTableHeader>
  );
}

export function TableBody<T>(props: TableBodyProps<T>) {
  return <AriaTableBody {...props} className="empty:italic empty:text-center empty:text-sm" />;
}

export function TableFooter<T>(props: TableFooterProps<T>) {
  return <AriaTableFooter {...props} className="bg-neutral-200 dark:bg-neutral-700 font-bold" />;
}

export function Row<T>({id, columns, children, ...otherProps}: RowProps<T>) {
  let {selectionBehavior, allowsDragging} = useTableOptions();

  return (
    <AriaRow id={id} {...otherProps} className="group/row relative cursor-default select-none -outline-offset-2 text-sm hover:bg-neutral-100 dark:hover:bg-neutral-800 selected:bg-blue-100 dark:selected:bg-blue-700/30 last:rounded-b-lg">
      {allowsDragging && (
        <Cell>
          <Button slot="drag">≡</Button>
        </Cell>
      )}
      {selectionBehavior === 'toggle' && (
        <Cell>
          <Checkbox slot="selection" />
        </Cell>
      )}
      <Collection items={columns}>{children}</Collection>
    </AriaRow>
  );
}

export function Cell(props: CellProps) {
  return (
    <AriaCell
      {...props}
      className="box-border border-b border-b-neutral-200 dark:border-b-neutral-700 p-2 truncate -outline-offset-2"
      style={({hasChildItems, isTreeColumn, level}) => ({
        paddingInlineStart: isTreeColumn
          ? 4 + (hasChildItems ? 0 : 20) + (level - 1) * 16
          : undefined
      })}>
      {composeRenderProps(
        props.children,
        (children, {hasChildItems, isTreeColumn, isExpanded, isDisabled}) => (
          <>
            {hasChildItems && isTreeColumn && (
              <Button slot="chevron">
                <ChevronRight aria-hidden className={isExpanded ? 'rotate-90' : ''} />
              </Button>
            )}
            {children}
          </>
        )
      )}
    </AriaCell>
  );
}
```

### Tabs

Wraps a `Tabs`/`TabList`/`Tab`/`TabPanels`/`TabPanel` composition with automatic ARIA relationships, keyboard arrow navigation, and an animated `SelectionIndicator`.

```tsx
'use client';
import React from 'react';
import {
  Tab as RACTab,
  TabList as RACTabList,
  TabPanels as RACTabPanels,
  TabPanel as RACTabPanel,
  Tabs as RACTabs,
  SelectionIndicator,
  type TabListProps,
  type TabPanelProps,
  type TabPanelsProps,
  type TabProps,
  type TabsProps
} from 'react-aria-components/Tabs';
import {composeRenderProps} from 'react-aria-components/composeRenderProps';
import {tv} from 'tailwind-variants';
import {focusRing} from './utils';
import {twMerge} from 'tailwind-merge';

const tabsStyles = tv({
  base: 'flex gap-4 font-sans max-w-full',
  variants: {
    orientation: {
      horizontal: 'flex-col',
      vertical: 'flex-row'
    }
  }
});

export function Tabs(props: TabsProps) {
  return (
    <RACTabs
      {...props}
      className={composeRenderProps(props.className, (className, renderProps) =>
        tabsStyles({...renderProps, className})
      )}
    />
  );
}

export function TabList<T>(props: TabListProps<T>) {
  return (
    <RACTabList
      {...props}
      className="flex max-w-full p-1 -m-1 overflow-x-auto overflow-y-clip [scrollbar-width:none]"
    />
  );
}

const tabProps = tv({
  extend: focusRing,
  base: 'group relative flex items-center cursor-default rounded-full px-3 py-1.5 text-sm font-medium transition forced-color-adjust-none [-webkit-tap-highlight-color:transparent]',
  variants: {
    isDisabled: {
      true: 'text-neutral-200 dark:text-neutral-600 forced-colors:text-[GrayText]'
    }
  }
});

export function Tab(props: TabProps) {
  return (
    <RACTab
      {...props}
      className={composeRenderProps(props.className, (className, renderProps) =>
        tabProps({...renderProps, className})
      )}>
      {composeRenderProps(props.children, children => (
        <>
          {children}
          <SelectionIndicator className="absolute top-0 left-0 w-full h-full z-10 bg-white rounded-full mix-blend-difference group-disabled:bg-neutral-400 motion-safe:transition-[translate,width,height]" />
        </>
      ))}
    </RACTab>
  );
}

export function TabPanels<T>(props: TabPanelsProps<T>) {
  return (
    <RACTabPanels
      {...props}
      className={twMerge(
        'relative h-(--tab-panel-height) motion-safe:transition-[height] overflow-clip',
        props.className
      )}
    />
  );
}

export function TabPanel(props: TabPanelProps) {
  return (
    <RACTabPanel
      {...props}
      className={composeRenderProps(props.className, (className, renderProps) =>
        tv({
          extend: focusRing,
          base: 'flex-1 box-border p-4 text-sm transition entering:opacity-0 exiting:opacity-0'
        })({...renderProps, className})
      )}
    />
  );
}
```

---

## Date/Time

### DatePicker

Wraps a segmented date-entry field (`DateInput`, from `DateField.tsx`) plus a `Popover`-hosted `Calendar` for visual picking — locale-aware date formatting and parsing come from the underlying `@internationalized/date` layer.

```tsx
'use client';
import {CalendarIcon} from 'lucide-react';
import React from 'react';
import {
  DatePicker as AriaDatePicker,
  type DatePickerProps as AriaDatePickerProps,
  type DateValue,
  type ValidationResult
} from 'react-aria-components/DatePicker';
import {Calendar} from './Calendar';
import {DateInput} from './DateField';
import {Description, FieldError, FieldGroup, Label} from './Field';
import {Popover} from './Popover';
import {composeTailwindRenderProps} from './utils';
import {FieldButton} from './FieldButton';

export interface DatePickerProps<T extends DateValue> extends AriaDatePickerProps<T> {
  label?: string;
  description?: string;
  errorMessage?: string | ((validation: ValidationResult) => string);
}

export function DatePicker<T extends DateValue>({
  label,
  description,
  errorMessage,
  ...props
}: DatePickerProps<T>) {
  return (
    <AriaDatePicker
      {...props}
      className={composeTailwindRenderProps(
        props.className,
        'group flex flex-col gap-1 font-sans'
      )}>
      {label && <Label>{label}</Label>}
      <FieldGroup className="min-w-[208px] w-auto cursor-text disabled:cursor-default">
        <DateInput className="flex-1 min-w-[150px] px-3 text-sm" />
        <FieldButton className="w-6 mr-1 outline-offset-0">
          <CalendarIcon aria-hidden className="w-4 h-4" />
        </FieldButton>
      </FieldGroup>
      {description && <Description>{description}</Description>}
      <FieldError>{errorMessage}</FieldError>
      <Popover className="p-2">
        <Calendar />
      </Popover>
    </AriaDatePicker>
  );
}
```

For the underlying calendar grid itself (`Calendar`, `CalendarGrid`, `CalendarCell`, month navigation, RTL-aware chevron direction via `useLocale`), see `starters/tailwind/src/Calendar.tsx` in the same repo — `DatePicker` above composes it directly.
