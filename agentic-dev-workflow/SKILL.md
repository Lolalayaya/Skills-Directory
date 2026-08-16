---
name: agentic-dev-workflow
description: "The full agentic software-development lifecycle in one place — explore intent before building (brainstorming or interview-driven grilling), write an implementation plan or formal spec/tickets, isolate a workspace for it (git worktree), execute the plan (solo, subagent-driven, or dispatched in parallel across independent tasks), resolve merge conflicts, hand off between sessions, and decide how to integrate the finished branch once tests pass. Use before any creative/feature work, before writing a multi-step implementation, when starting an isolated workspace for a feature, when facing 2+ independent tasks that don't share state, when starting any conversation that should establish how to find and use the right skill first, when resolving an in-progress merge conflict, when handing a conversation off to another session, and when implementation is done and tests pass and you need to decide how to land it."
---

# Agentic Dev Workflow

Router skill for the end-to-end shape of doing software work with an agent — from "what are we actually building" through "how does this branch get integrated." Previously the isolation step and the integration step lived in two other categories (`business-automation`, `cicd-deployment`); they're consolidated here so the whole lifecycle doesn't require hopping between skills. On 2026-07-31, a curated set of sub-skills from Matt Pocock's third-party `mattpocock-skills` pack (MIT license — see [`THIRD-PARTY-LICENSES.md`](../THIRD-PARTY-LICENSES.md)) was folded in here too, since they cover the same lifecycle with different tools (interview-driven planning, formal spec/ticket flows, git mechanics). On 2026-08-01, `karpathy-guidelines` (MIT, forrestchang's `andrej-karpathy-skills` — see [`THIRD-PARTY-LICENSES.md`](../THIRD-PARTY-LICENSES.md)) was folded in as a lightweight, always-relevant behavioral reference rather than a lifecycle step. On 2026-08-16, `loyalty-mindset` (MIT, extracted fragment from bencium.io's `human-architect-mindset` — see [`THIRD-PARTY-LICENSES.md`](../THIRD-PARTY-LICENSES.md)) was folded in the same way — a standing philosophical reference for architectural-change decisions, not a lifecycle step.

## Domains (core lifecycle, in typical order)

| Domain | When to use | Full guide |
|---|---|---|
| Finding/using skills at all | Establishes how to discover and invoke the right skill before responding to anything, at the start of a session | [references/using-superpowers/SKILL.md](references/using-superpowers/SKILL.md) |
| Coding-discipline reference | Quick 4-principle checklist (think before coding, simplicity first, surgical changes, goal-driven execution) — a condensed standing reference, not a step in the lifecycle; overlaps in spirit with `brainstorming` (surface assumptions), `product-verification`'s TDD/verification (goal-driven execution), and `code-quality-review` (simplicity/surgical changes) without duplicating any of their detailed processes | [references/karpathy-guidelines/SKILL.md](references/karpathy-guidelines/SKILL.md) |
| Architectural loyalty framing | Standing philosophical reference, not a lifecycle step — why committing to an existing architecture over chasing the next trend/framework/rewrite is a distinct human capability, a Loyalty Decision Matrix, and 5 named anti-patterns (Endless Pivot, Greenfield Fallacy, Trend Chase, Premature Abstraction, Shiny Object Syndrome). Use when deciding whether to migrate/rewrite/abandon an existing architectural commitment | [references/loyalty-mindset/SKILL.md](references/loyalty-mindset/SKILL.md) |
| Brainstorming before building | MUST use before any creative work — new features, components, functionality, or behavior changes — to explore intent and requirements first | [references/brainstorming/SKILL.md](references/brainstorming/SKILL.md) |
| Writing implementation plans | Have a spec/requirements for a multi-step task — write the plan before touching code | [references/writing-plans/SKILL.md](references/writing-plans/SKILL.md) |
| Isolated git-worktree workspace | Stand up an isolated workspace (native tool or `git worktree` fallback) before starting feature work | [references/using-git-worktrees/SKILL.md](references/using-git-worktrees/SKILL.md) |
| Executing plans (separate session) | Have a written implementation plan to execute with review checkpoints, potentially in a separate session | [references/executing-plans/SKILL.md](references/executing-plans/SKILL.md) |
| Subagent-driven execution | Execute an implementation plan with independent tasks in the current session via subagents | [references/subagent-driven-development/SKILL.md](references/subagent-driven-development/SKILL.md) |
| Dispatching parallel agents | 2+ independent tasks with no shared state or sequential dependency — a separate scenario from a plan's own implementer tasks, which stay sequential (see note under "How to use" below) | [references/dispatching-parallel-agents/SKILL.md](references/dispatching-parallel-agents/SKILL.md) |
| Finishing a development branch | Implementation complete and tests pass — decide how to integrate (merge, PR, rebase) | [references/finishing-a-development-branch/SKILL.md](references/finishing-a-development-branch/SKILL.md) |

## Domains (interview-driven planning — alternative/complementary tools)

| Domain | When to use | Full guide |
|---|---|---|
| Flow router (this pack) | Unsure which of the tools below fits — ask this first | [references/ask-matt/SKILL.md](references/ask-matt/SKILL.md) |
| Relentless interview | Stress-test a plan/decision one question at a time (or `--batch` a whole round at once); general-purpose, not code-specific | [references/grilling/SKILL.md](references/grilling/SKILL.md) / [references/grill-me/SKILL.md](references/grill-me/SKILL.md) |
| Interview + domain docs | Same interview, but persists to a codebase's `CONTEXT.md`/ADRs inline — use when you have a codebase | [references/grill-with-docs/SKILL.md](references/grill-with-docs/SKILL.md) |
| Domain vocabulary | Challenge a fuzzy term, resolve a word doing two jobs, record a hard-to-reverse decision as an ADR | [references/domain-modeling/SKILL.md](references/domain-modeling/SKILL.md) |
| Conversation → formal spec | Turn the current conversation into a spec, publish to an issue tracker | [references/to-spec/SKILL.md](references/to-spec/SKILL.md) |
| Spec → tracer-bullet tickets | Break a plan/spec into tickets that declare their blocking edges | [references/to-tickets/SKILL.md](references/to-tickets/SKILL.md) |
| Fog-of-war planning | A greenfield/huge effort too big for one session — chart a decision-ticket map, resolve one at a time | [references/wayfinder/SKILL.md](references/wayfinder/SKILL.md) |
| Refactor request → plan | Interview a refactor request into small, ordered, committable steps, filed as an issue | [references/request-refactor-plan/SKILL.md](references/request-refactor-plan/SKILL.md) |
| Throwaway prototype | Answer one hard design question (state/logic or UI) with disposable code, then delete it | [references/prototype/SKILL.md](references/prototype/SKILL.md) |
| ↳ vs `prototype-variants` | For "build N genuinely different versions of this UI piece and let me flip through them," use `scaffolding-templating`'s `prototype-variants` instead — a multi-variant visual-picker workflow, not a single disposable artifact | (see `scaffolding-templating/SKILL.md`) |
| One-time repo setup | Configure issue tracker, triage labels, doc layout for the tools above — run once per repo | [references/setup-matt-pocock-skills/SKILL.md](references/setup-matt-pocock-skills/SKILL.md) |

## Domains (session & git mechanics)

| Domain | When to use | Full guide |
|---|---|---|
| Session handoff | Compact the conversation into a handoff — launches a background agent if the CLI supports it, else saves a file for the next session to read | [references/handoff/SKILL.md](references/handoff/SKILL.md) |
| Merge-conflict resolution | Work an in-progress git merge/rebase conflict hunk by hunk, by intent, never `--abort` | [references/resolving-merge-conflicts/SKILL.md](references/resolving-merge-conflicts/SKILL.md) |
| Git safety hooks | Install a hook blocking dangerous git commands (`push --force`, `reset --hard`, etc.) before they run | [references/git-guardrails-claude-code/SKILL.md](references/git-guardrails-claude-code/SKILL.md) |

## How to use this skill

The natural lifecycle order for a non-trivial task:

1. `brainstorming` (or `grilling`/`grill-with-docs` for a more relentless, decision-by-decision interview — pick whichever style fits; they're complementary, not sequential) — clarify what's actually being asked before designing a solution.
2. `writing-plans` (or the formal `to-spec` → `to-tickets` route, or `wayfinder` if the effort is too big/foggy for one session) — turn the clarified intent into a concrete, reviewable implementation plan.
3. `using-git-worktrees` — isolate a workspace for the work if it shouldn't collide with what's currently checked out.
4. `executing-plans` or `subagent-driven-development` — execute the plan; pick the former for a plan meant to run with checkpoints (possibly in a fresh session), the latter when independent tasks in the plan can be split across subagents within the current session.
5. `dispatching-parallel-agents` — a separate tool for a different kind of work: 2+ *independent* tasks that don't share a workspace (e.g. unrelated bug investigations, standalone research tasks), dispatched concurrently rather than serially out of habit. **This is not the next step after step 4 for a single plan's own tasks** — `subagent-driven-development` explicitly forbids dispatching multiple implementer subagents in parallel, because they'd write to the same worktree/branch and conflict. Use this skill only when the tasks at hand are outside the plan being executed, or don't share state at all.
6. `finishing-a-development-branch` — once tests pass, decide the integration path (merge/PR/rebase). This is a decision step, not just a `git merge` command.

Cutting across all of the above: `resolving-merge-conflicts` whenever a merge/rebase is mid-conflict, `handoff` whenever the conversation needs to move to a fresh session, and `git-guardrails-claude-code` as a standing safety net, not a lifecycle step.

After step 6, actually shipping is `cicd-deployment`'s job (deploying to Vercel, interactively or via CI token auth) — this skill stops at "how to integrate," that one picks up "how to deploy."

## Relationship to `browser-automation`

If the work itself involves driving a browser (testing, scraping, automation), that tooling lives in `browser-automation` — this skill is about the shape of the development process, not a specific tool.

## Relationship to `openspec-workflow`

`openspec-workflow` is a more formal, convention-driven alternative to steps 1–2 here (brainstorm/plan) for projects that already use the OpenSpec `openspec/changes/` structure. Use one or the other for a given change, not both. `to-spec`/`to-tickets` above are a lighter-weight formal alternative that doesn't require the OpenSpec directory convention.
