---
name: deep-research
description: "General-purpose topic research pipeline (Chinese-language): generate a research outline, extend it with fields/items, fan out independent deep-research agents per item, then compile everything into a markdown report. Use for academic research, benchmark/technology comparisons, or any 'research this topic and give me a structured report' request — not for researching a company, competitor, or sales lead (see `browser-automation`'s `company-research`/`competitor-analysis`/`event-prospecting` for that), and not for a single-question one-shot background lookup (see this same skill's `background-research` for that — no outline/fields/multi-agent structure, just one cited note)."
---

# Deep Research

Router skill for a generic, outline-driven research pipeline: outline → add fields/items → deep-dive per item via independent agents → compiled report.

## Domains (pipeline stages, in order)

| Domain | When to use | Full guide |
|---|---|---|
| Research outline | Initial research on a target topic, generating a research outline — academic research, benchmark research, technology selection | [references/research/SKILL.md](references/research/SKILL.md) |
| Add fields | Add field definitions to an existing research outline | [references/research-add-fields/SKILL.md](references/research-add-fields/SKILL.md) |
| Add items | Add items (research subjects/targets) to an existing research outline | [references/research-add-items/SKILL.md](references/research-add-items/SKILL.md) |
| Deep dive | Read the outline, launch an independent agent per item for deep research (task output disabled) | [references/research-deep/SKILL.md](references/research-deep/SKILL.md) |
| Report | Compile deep-research results into a markdown report covering all fields, skipping uncertain values | [references/research-report/SKILL.md](references/research-report/SKILL.md) |
| Single-question lookup (not part of the pipeline) | One question, one background agent, one cited markdown note — no outline/fields/comparison structure | [references/background-research/SKILL.md](references/background-research/SKILL.md) |

## How to use this skill

Run the stages in order for a new research task:

1. `research` — produce the initial outline for the topic.
2. `research-add-fields` / `research-add-items` — extend the outline with the specific fields to compare and items/subjects to research, as needed (either or both, any number of times).
3. `research-deep` — fan out one independent agent per item to do the actual research against the outline.
4. `research-report` — compile everything into the final markdown report, covering every field and explicitly skipping values that couldn't be determined confidently rather than guessing.

Don't skip straight to `research-deep` without an outline — the fields/items structure is what keeps the per-item agents' output comparable enough to compile into one report.

For a single question that doesn't need a comparison table — "what does library X's API look like", "find primary sources on Y" — use `background-research` instead of standing up the whole pipeline for one item.
