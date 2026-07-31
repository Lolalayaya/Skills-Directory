---
name: cicd-deployment
description: "Deploy to Vercel both interactively and via CI-friendly token-based authentication, including reading back deployment errors/logs. Use whenever the user wants to deploy, 'push this live', create a preview deployment, or set up token-based Vercel CI auth (no interactive login). For deciding how to integrate a finished development branch (merge/PR/rebase) before deploying, see `agentic-dev-workflow` instead — this skill starts once that decision is already made."
---

# CI/CD & Deployment

Router skill for the actual deploy mechanics, once work is already reviewed, tested, and ready to ship.

## Domains

| Domain | When to use | Full guide |
|---|---|---|
| Deploy to Vercel (interactive) | "Deploy my app", "push this live", "create a preview deployment" | [references/deploy-to-vercel/SKILL.md](references/deploy-to-vercel/SKILL.md) |
| Vercel CLI with tokens (CI-friendly) | Deploy/manage Vercel projects using access-token auth instead of interactive login — CI pipelines, non-interactive environments, env-var setup | [references/vercel-cli-with-tokens/SKILL.md](references/vercel-cli-with-tokens/SKILL.md) |

## How to use this skill

1. Confirm the prerequisites are actually satisfied first: tests passing and evidence read (see `product-verification`), and the integration decision made (see `agentic-dev-workflow`'s `finishing-a-development-branch` domain) — this skill picks up right after those.
2. Use `deploy-to-vercel` when working interactively with the user present, or `vercel-cli-with-tokens` when running non-interactively (CI, background agents, scripted pipelines) — the token-based flow exists specifically to avoid needing an interactive login prompt.
3. If a deployment fails, read the actual returned error/log output before retrying — don't guess at the cause from the command name alone.

## Gotcha

Never put deployment auth tokens directly in shell commands where they might be echoed into chat or logs (`VERCEL_TOKEN=...` inline, `--token ...` in a visible command). Use environment variables set outside the visible command, or the mechanism `vercel-cli-with-tokens` documents.
