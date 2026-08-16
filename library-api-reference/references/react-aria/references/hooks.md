# React Aria Hooks (`@react-aria/*`)

The lowest application-facing layer of React Aria. Each hook attaches accessible behavior (ARIA attributes, keyboard handling, pointer/touch interactions, focus management) to DOM elements *you* render — the hook returns prop objects you spread onto your own markup, rather than rendering anything itself. State is usually managed separately by a matching `@react-stately/*` hook (e.g. `useToggleState` alongside `useCheckbox`).

## When to Reach for a Hook Instead of a RAC Component

Drop down from `react-aria-components` to individual hooks only when:

1. **Building a truly custom low-level primitive** that isn't one of RAC's ~50 pre-built components, or needs a fundamentally different composition than RAC offers.
2. **Integrating ARIA behavior into an already-existing, non-RAC DOM structure** — e.g. retrofitting accessibility onto markup from a design system, CMS-driven layout, or third-party component you don't control the render tree of.
3. **Needing something RAC doesn't expose** — a niche interaction, a non-standard DOM nesting requirement, or fine-grained control over exactly which ARIA attributes land where.

For everything else, prefer `react-aria-components` (see [components.md](components.md)) — it's built on these same hooks internally, so you aren't giving up behavior or accessibility by using the higher-level component; you're only giving up low-level control you likely don't need.

## Real Example 1: `useButton`

From `packages/react-aria/README.md`:

```jsx
import {useButton} from '@react-aria/button';

function Button(props) {
  let ref = React.useRef();
  let {buttonProps} = useButton(props, ref);

  return (
    <button {...buttonProps} ref={ref}>
      {props.children}
    </button>
  );
}

<Button onPress={() => alert('Button pressed!')}>Press me</Button>
```

`useButton` normalizes press handling (`onPress` instead of `onClick`, so mouse/touch/keyboard/screen-reader activation all behave consistently) and returns the ARIA/event props to spread onto whatever element you're turning into a button.

## Real Example 2: `useCheckbox`

From `packages/react-aria/stories/checkbox/useCheckbox.stories.tsx` in `adobe/react-spectrum`:

```tsx
import {AriaCheckboxProps, useCheckbox} from '../../src/checkbox/useCheckbox';
import {useToggleState} from 'react-stately/useToggleState';

function Checkbox(props: AriaCheckboxProps) {
  let {children} = props;
  let state = useToggleState(props);
  let ref = React.useRef(null);
  let {inputProps, labelProps} = useCheckbox(props, state, ref);

  return (
    <>
      <label {...labelProps} style={{display: 'block'}}>
        {children}
      </label>
      <input {...inputProps} ref={ref} />
    </>
  );
}
```

Note the pairing: `useToggleState` (from `@react-stately`, layer 1) owns the selected/checked state; `useCheckbox` (from `@react-aria`, layer 2) consumes that state plus a ref and returns the accessible `inputProps`/`labelProps` to spread onto plain `<input>`/`<label>` elements. This state-hook + behavior-hook pairing is the general shape of the `@react-aria/*` layer.

## Real Example 3: `useTextField`

From `packages/react-aria/stories/textfield/useTextField.stories.tsx` in `adobe/react-spectrum`:

```tsx
import {useTextField} from '../../src/textfield/useTextField';

const TextInputField = (props: TextFieldProps): JSX.Element => {
  const {label} = props;
  const ref = useRef<HTMLInputElement>(null);
  const {labelProps, inputProps} = useTextField(props, ref);

  return (
    <div>
      <label {...labelProps}>{label}</label>
      <input {...inputProps} ref={ref} />
    </div>
  );
};

const TextAreaField = (props: TextFieldProps): JSX.Element => {
  const {label} = props;
  const ref = useRef<HTMLTextAreaElement>(null);
  const {labelProps, inputProps} = useTextField({...props, inputElementType: 'textarea'}, ref);

  return (
    <div>
      <label {...labelProps}>{label}</label>
      <textarea {...inputProps} ref={ref} />
    </div>
  );
};
```

Note `useTextField` adapts to either a `<textarea>` or an `<input>` via the `inputElementType` option, while returning the same shape of props (`labelProps`, `inputProps`) either way — the hook does not care what element you ultimately render it onto, only that it's a compatible one.

## Summary

All three real examples share the same shape: a state hook (where applicable) plus a behavior hook, both returning plain prop objects, spread onto elements *you* choose and render. There is no imposed DOM structure at this layer — that flexibility is also the reason it takes more code than the equivalent RAC component.
