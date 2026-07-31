---
name: agentic-dev-workflow
description: "The full agentic software-development lifecycle in one place — explore intent before building (brainstorming), write an implementation plan, isolate a workspace for it (git worktree), execute the plan (solo, subagent-driven, or dispatched in parallel across independent tasks), and decide how to integrate the finished branch once tests pass. Use before any creative/feature work, before writing a multi-step implementation, when starting an isolated workspace for a feature, when facing 2+ independent tasks that don't share state, when starting any conversation that should establish how to find and use the right skill first, and when implementation is done and tests pass and you need to decide how to land it."
---

# Agentic Dev Workflow

Router skill for the end-to-end shape of doing software work with an agent — from "what are we actually building" through "how does this branch get integrated." Previously the isolation step and the integration step lived in two other categories (`business-automation`, `cicd-deployment`); they're consolidated here so the whole lifecycle doesn't require hopping between skills.

## Domains (in typical lifecycle order)

| Domain | When to use | Full guide |
|---|---|---|
| Brainstorming before building | MUST use before any creative work — new features, components, functionality, or behavior changes — to explore intent and requirements first | [references/brainstorming/SKILL.md](references/brainstorming/SKILL.md) |
| Writing implementation plans | Have a spec/requirements for a multi-step task — write the plan before touching code | [references/writing-plans/SKILL.md](references/writing-plans/SKILL.md) |
| Isolated git-worktree workspace | Stand up an isolated workspace (native tool or `git worktree` fallback) before starting feature work | [references/using-git-worktrees/SKILL.md](references/using-git-worktrees/SKILL.md) |
| Executing plans (separate session) | Have a written implementation plan to execute with review checkpoints, potentially in a separate session | [references/executing-plans/SKILL.md](references/executing-plans/SKILL.md) |
| Subagent-driven execution | Execute an implementation plan with independent tasks in the current session via subagents | [references/subagent-driven-development/SKILL.md](references/subagent-driven-development/SKILL.md) |
| Dispatching parallel agents | 2+ independent tasks with no shared state or sequential dependency | [references/dispatching-parallel-agents/SKILL.md](references/dispatching-parallel-agents/SKILL.md) |
| Finishing a development branch | Implementation complete and tests pass — decide how to integrate (merge, PR, rebase) | [references/finishing-a-development-branch/SKILL.md](references/finishing-a-development-branch/SKILL.md) |
| Finding/using skills at all | Establishes how to discover and invoke the right skill before responding to anything, at the start of a session | [references/using-superpowers/SKILL.md](references/using-superpowers/SKILL.md) |

## How to use this skill

The natural lifecycle order for a non-trivial task:

1. `brainstorming` — clarify what's actually being asked before designing a solution.
2. `writing-plans` — turn the clarified intent into a concrete, reviewable implementation plan.
3. `using-git-worktrees` — isolate a workspace for the work if it shouldn't collide with what's currently checked out.
4. `executing-plans` or `subagent-driven-development` — execute the plan; pick the former for a plan meant to run with checkpoints (possibly in a fresh session), the latter when independent tasks in the plan can be split across subagents within the current session.
5. `dispatching-parallel-agents` — the specific trigger for recognizing "these N tasks don't depend on each other, dispatch them concurrently" rather than running them serially out of habit.
6. `finishing-a-development-branch` — once tests pass, decide the integration path (merge/PR/rebase). This is a decision step, not just a `git merge` command.

After step 6, actually shipping is `cicd-deployment`'s job (deploying to Vercel, interactively or via CI token auth) — this skill stops at "how to integrate," that one picks up "how to deploy."

## Relationship to `browser-automation`

If the work itself involves driving a browser (testing, scraping, automation), that tooling lives in `browser-automation` — this skill is about the shape of the development process, not a specific tool.

## Relationship to `openspec-workflow`

`openspec-workflow` is a more formal, convention-driven alternative to steps 1–2 here (brainstorm/plan) for projects that already use the OpenSpec `openspec/changes/` structure. Use one or the other for a given change, not both.
