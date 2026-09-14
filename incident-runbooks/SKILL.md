---
name: incident-runbooks
description: "Systematic methodology for diagnosing bugs, test failures, or unexpected behavior before proposing a fix — and capturing the resulting root cause, blast radius, and remedy as a reusable diagnostic record. Also covers turning incoming bug reports/requests into agent-ready issues (triage, conversational bug intake), and bulk-auditing/reviewing a repo's existing GitHub issue and PR backlog (staleness, duplicates, risk, overlap, batch review-and-merge, status recaps). Use whenever encountering any bug, crash, failing test, or surprising behavior, BEFORE writing or proposing a fix; the goal is root-cause evidence and a clear record future debugging can reuse, not a guessed patch; whenever bug reports or requests are piling up unsorted; and whenever open GitHub issues/PRs need auditing, reviewing, merging, or summarizing in bulk."
---

# Incident Runbooks

Router skill for "diagnose properly, then write down what was learned" — treating debugging as evidence-gathering rather than guess-and-check, and treating the write-up as a reusable asset for the next time something similar breaks.

## Domains

| Domain | When to use | Full guide |
|---|---|---|
| Systematic debugging | Any bug, test failure, or unexpected behavior — before proposing a fix | [references/systematic-debugging/SKILL.md](references/systematic-debugging/SKILL.md) |
| Issue triage (single-issue) | Move incoming bug reports/feature requests through a triage-role state machine, produce agent-ready issues | [references/triage/SKILL.md](references/triage/SKILL.md) |
| Conversational bug intake | User reports a bug by describing it out loud; explore the codebase in the background, file the resulting issue(s) | [references/qa/SKILL.md](references/qa/SKILL.md) |
| Issue backlog audit (bulk) | Audit every open GitHub issue for categorization, duplicates, risk, staleness; optionally deep-analyze and draft comments | [references/issue-triage/SKILL.md](references/issue-triage/SKILL.md) |
| PR backlog audit (bulk) | Audit every open GitHub PR for size, CI status, overlaps, clusters, staleness; optionally deep-review with a code-reviewer subagent | [references/pr-triage/SKILL.md](references/pr-triage/SKILL.md) |
| Repo status recap | Lightweight shareable Markdown summary of open PRs/issues/releases for the team | [references/repo-recap/SKILL.md](references/repo-recap/SKILL.md) |
| Interactive PR review & merge | Work a PR queue one at a time, smallest first, with explicit sign-off before every merge | [references/pr-review/SKILL.md](references/pr-review/SKILL.md) |
| Full backlog cross-triage | Run issue-triage + pr-triage together plus cross-analysis (double coverage, security gaps, orphaned P0/P1 bugs); saves a dated report | [references/full-triage/SKILL.md](references/full-triage/SKILL.md) |

## How to use this skill

0. **Bugs/requests arriving raw, before diagnosis starts**: `triage` (external reports piling up) or `qa` (user describing a bug conversationally) turn them into a well-formed, agent-ready issue first. Don't triage issues that already came in well-formed (e.g. from a planning skill's own ticket output) — triage is for *raw* incoming reports only. This is distinct from the bulk backlog-audit group below: `triage` processes *one* issue/PR into a spec, it doesn't sweep the whole backlog.
0b. **The whole backlog needs auditing, reviewing, or summarizing**: use `issue-triage` / `pr-triage` (bulk audit with duplicates/risk/staleness detection), `repo-recap` (lightweight status summary), `pr-review` (work the merge queue one PR at a time), or `full-triage` (both triage skills plus cross-analysis, for a deeper periodic sweep). These four/five skills cross-reference each other for exactly when to use which.
1. **Don't propose a fix before you've diagnosed the actual cause.** Follow `systematic-debugging`'s methodology to isolate root cause with evidence (reproduce, bisect, read the actual error, form and test a hypothesis) rather than pattern-matching to the first plausible-looking cause.
2. **Cross-system, multi-tool debugging**: this category is meant to span whatever tools the incident touches (browser trace from `product-verification`, deployment logs from `cicd-deployment`, static-analysis findings from `code-quality-review`) — pull in evidence from those categories rather than treating debugging as code-only.
3. **After resolving**, write the diagnostic record explicitly rather than letting the fix speak for itself. A useful record covers, at minimum:
   - **Symptom**: what was observed (exact error text, reproduction steps)
   - **Root cause**: what was actually wrong, not just what was changed
   - **Blast radius**: what else could have been affected by the same root cause
   - **Fix applied**: the concrete change, and why it addresses the root cause specifically
   - **How to recognize this again**: the signal that would let a future session recognize the same class of bug faster
4. This record is what makes debugging cumulative rather than starting from zero every time — treat it as a first-class deliverable of the debugging session, not an afterthought.

## Note on scope

This category is a natural home for future skills that specifically produce structured incident write-ups or issue intake (e.g. a postmortem-template skill, an on-call handoff skill) — add them under `references/` following the same pattern as the other consolidated skills in this workspace.
