---
name: product-verification
description: "Verify that agent-produced work actually behaves as expected before claiming it's done — test local web apps with Playwright, and hold the non-negotiable discipline of running verification commands and reading real output before claiming a fix/feature/test is complete, plus writing the test that defines success before implementation (TDD). Use whenever about to claim a fix, feature, or test is complete and passing, before committing or opening a PR; when the user asks to test a local web app with Playwright; and when writing tests or defining step-by-step success criteria before or during implementation. For actually driving a browser (navigate/click/extract/screenshot) or adversarial UI exploration, see `browser-automation` instead — this skill owns the verification discipline, that one owns the browser tooling."
---

# Product Verification

Router skill for "does this actually work, and how do I prove it rather than assert it." Evidence before assertions: run the verification, read its output, and only then claim success.

## Domains

| Domain | When to use | Full guide |
|---|---|---|
| Web app testing (Playwright) | Verify frontend functionality, debug UI behavior, capture screenshots/browser logs on a local app | [references/webapp-testing/SKILL.md](references/webapp-testing/SKILL.md) |
| Verification-before-completion discipline | The rule itself: never claim "fixed"/"passing"/"complete" without running the verification command and reading its output first | [references/verification-before-completion/SKILL.md](references/verification-before-completion/SKILL.md) |
| Test-driven development | Write the test that defines success *before* writing implementation code | [references/test-driven-development/SKILL.md](references/test-driven-development/SKILL.md) |

## How to use this skill

1. **Before implementation**: use `test-driven-development` to write the success criteria as a failing test first.
2. **After implementation, before claiming done**: this is where most shortcuts happen. `verification-before-completion` is the governing rule — run `webapp-testing` (Playwright) against the real, running app and read the actual output. Do not infer success from reading the diff.
3. **Need to actually drive a browser** (navigate, click, extract, screenshot, adversarial exploration, trace a failed run) — that's `browser-automation`'s job, not this skill's. Use this skill's discipline (`verification-before-completion`) together with that skill's tooling.

## Non-negotiable principle (from `verification-before-completion`)

Never claim work is complete, fixed, or passing without having just run the relevant verification command in this turn and read its actual output. "It should work now" is not evidence. If a verification command is slow or unavailable, say so explicitly rather than substituting an assumption — a stated gap is honest; a fabricated pass is not.

Verification must cover more than the UI surface: confirm state transitions (server state, database rows, session/auth state) actually changed as intended, not just that a page rendered without error. For CLI-driven features, simulate the actual CLI input and read the actual stdout/stderr/exit code — don't assume based on the code path.

See each domain's own SKILL.md for tool-specific commands, script locations, and gotchas — those are preserved verbatim in `references/<domain>/` rather than re-summarized here.
