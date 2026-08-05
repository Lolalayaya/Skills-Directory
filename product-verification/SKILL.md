---
name: product-verification
description: "Verify that agent-produced work actually behaves as expected before claiming it's done — test local web apps with Playwright, hold the non-negotiable discipline of running verification commands and reading real output before claiming a fix/feature/test is complete, write the test that defines success before implementation (TDD), and enforce complete, untruncated output on any exhaustive-generation task. Use whenever about to claim a fix, feature, or test is complete and passing, before committing or opening a PR; when the user asks to test a local web app with Playwright; when writing tests or defining step-by-step success criteria before or during implementation; and when a task demands full, unabridged output (many files/components, no placeholder patterns). For actually driving a browser (navigate/click/extract/screenshot) or adversarial UI exploration, see `browser-automation` instead — this skill owns the verification discipline, that one owns the browser tooling."
---

# Product Verification

Router skill for "does this actually work, and how do I prove it rather than assert it." Evidence before assertions: run the verification, read its output, and only then claim success.

## Domains

| Domain | When to use | Full guide |
|---|---|---|
| Web app testing (Playwright) | Verify frontend functionality, debug UI behavior, capture screenshots/browser logs on a local app | [references/webapp-testing/SKILL.md](references/webapp-testing/SKILL.md) |
| Verification-before-completion discipline | The rule itself: never claim "fixed"/"passing"/"complete" without running the verification command and reading its output first | [references/verification-before-completion/SKILL.md](references/verification-before-completion/SKILL.md) |
| Test-driven development | Write the test that defines success *before* writing implementation code | [references/test-driven-development/SKILL.md](references/test-driven-development/SKILL.md) |
| Full-output enforcement | Ban truncation/placeholder patterns (`// rest of code`, "for brevity", skeleton-only output); scope the deliverable count up front and cross-check it before responding; clean pause/resume format when a response would hit the token limit | [references/output-skill/SKILL.md](references/output-skill/SKILL.md) |

## How to use this skill

1. **Before implementation**: use `test-driven-development` to write the success criteria as a failing test first.
2. **After implementation, before claiming done**: this is where most shortcuts happen. `verification-before-completion` is the governing rule — run `webapp-testing` (Playwright) against the real, running app and read the actual output. Do not infer success from reading the diff.
3. **Need to actually drive a browser** (navigate, click, extract, screenshot, adversarial exploration, trace a failed run) — that's `browser-automation`'s job, not this skill's. Use this skill's discipline (`verification-before-completion`) together with that skill's tooling.
4. **`verification-before-completion` vs `output-skill`**: adjacent but distinct axes. `verification-before-completion` governs *claiming* something works (run it, read the output, don't assert). `output-skill` governs *delivering* the full thing in the first place (don't truncate, don't placeholder, don't skip items) — a response can be honestly "not yet verified" but still fully written, or fully verified but silently missing half the requested files. Apply both on any non-trivial multi-file generation task.

## Non-negotiable principle (from `verification-before-completion`)

Never claim work is complete, fixed, or passing without having just run the relevant verification command in this turn and read its actual output. "It should work now" is not evidence. If a verification command is slow or unavailable, say so explicitly rather than substituting an assumption — a stated gap is honest; a fabricated pass is not.

Verification must cover more than the UI surface: confirm state transitions (server state, database rows, session/auth state) actually changed as intended, not just that a page rendered without error. For CLI-driven features, simulate the actual CLI input and read the actual stdout/stderr/exit code — don't assume based on the code path.

See each domain's own SKILL.md for tool-specific commands, script locations, and gotchas — those are preserved verbatim in `references/<domain>/` rather than re-summarized here.
