---
name: internal-writing-comms
description: "Structured workflows for co-authoring documentation (proposals, technical specs, decision docs), writing internal company communications (status updates, announcements) in the formats a company actually uses, drafting/editing articles from raw material, turning unanswerable questions into a questionnaire for someone else, improving academic research-paper writing quality (abstract/intro/method/experiments/conclusion structure, claim-evidence alignment), and removing AI-writing tells from a draft to make it read more naturally. Use when the user wants to write documentation, a proposal, a technical spec, a decision doc, any internal communication, an article from notes/transcript, a questionnaire to delegate questions, a research paper draft/revision, or wants text edited so it doesn't sound AI-generated — and cares about matching an existing structure/format rather than freeform prose."
---

# Internal Writing & Comms

Router skill for structured internal writing — distinct from `marketing`'s external-facing copy and from `scaffolding-templating`'s visual design; this is about document *structure and process*, for audiences inside the organization.

## Domains

| Domain | When to use | Full guide |
|---|---|---|
| Doc co-authoring workflow | Structured process for writing docs/proposals/specs/decision docs — efficient context transfer, iterative refinement, verifying the doc works for its readers | [references/doc-coauthoring/SKILL.md](references/doc-coauthoring/SKILL.md) |
| Internal communications formats | Write status updates, announcements, and other internal comms in the company's preferred formats | [references/internal-comms/SKILL.md](references/internal-comms/SKILL.md) |
| Fragment capture (explore) | Mine raw, unstructured writing fragments from conversation, no commitment to structure yet | [references/writing-fragments/SKILL.md](references/writing-fragments/SKILL.md) |
| Article shaping (exploit) | Shape raw material into an article paragraph/beat by paragraph/beat, or edit an existing draft section by section | [references/writing-shape/SKILL.md](references/writing-shape/SKILL.md) |
| Delegated questionnaire | Turn questions you can't answer into a Markdown questionnaire for someone else to fill in async or in a meeting | [references/to-questionnaire/SKILL.md](references/to-questionnaire/SKILL.md) |
| Research paper writing | Draft/revise Abstract, Introduction, Related Work, Method, Experiments, or Conclusion for ML/CV/NLP-style papers; paragraph-flow checks, claim-evidence alignment, reviewer-facing self-review | [references/research-paper-writing/SKILL.md](references/research-paper-writing/SKILL.md) |
| AI-writing-tell removal (Traditional Chinese) | Rewrite text to remove common LLM writing patterns (puffery, false ranges, "not only...but," em-dash overuse, hedge-stacking) and add genuine voice; based on Wikipedia's "Signs of AI writing" | [references/humanizer-zh-tw/SKILL.md](references/humanizer-zh-tw/SKILL.md) |

## How to use this skill

1. **Long-form structured documents** (proposal, spec, decision doc): `doc-coauthoring` — its value is the iterative process (transfer context → draft → refine → verify against readers), not just producing a first draft.
2. **Shorter recurring internal formats** (status update, announcement): `internal-comms` — check its bundled format examples before free-writing, since the point is matching an existing house style rather than inventing a new one.
3. **Writing an article from scratch**: `writing-fragments` to explore/mine material first (no structure), then `writing-shape` to commit to a structure and draft — or go straight to `writing-shape` in its editing mode if a draft already exists and just needs restructuring/tightening.
4. **A decision needs input only someone else has**: `to-questionnaire` turns the unanswerable questions into something they can fill in without a live conversation.
5. If the user's company/team has a documented style guide for prose quality (tone, voice) rather than structure, that's `scaffolding-templating`'s `writing-guidelines` domain instead — use both together when relevant (structure from here, style compliance from there).
6. **Writing or revising an academic paper**: `research-paper-writing` — section-specific guidance plus a claim-evidence self-review pass, distinct from `doc-coauthoring`'s general proposal/spec process. If the paper is an arXiv preprint you need fetched and converted to Markdown first, that's `library-api-reference`'s `arxiv-doc-builder`, not this skill.
7. **A draft reads like it was written by an LLM** (puffery, "not only...but," em-dash overuse, hedge-stacking, generic positive closers): `humanizer-zh-tw` rewrites it to remove those tells and add genuine voice. Its rules are written in Traditional Chinese and its examples are Chinese-language, but the underlying pattern catalog (from Wikipedia's "Signs of AI writing") is language-general — apply the same patterns when editing English text. This is a prose-craft tool, not a detection-evasion one: it improves writing quality, it makes no claim about defeating an AI-detection tool, and it doesn't touch provenance metadata or watermarks.
