# `hallmark audit`

Read the file(s) the user pointed at. For each finding, return:

- **Tell** — the named anti-pattern from [`anti-patterns.md`](../anti-patterns.md).
- **Where** — file path and line range.
- **Severity** — `critical` (ships as slop), `major` (looks AI-generated), `minor` (small taste issue).
- **Fix** — one-line concrete correction.

Group by severity. Do not edit. Do not redesign. End with a count: `N critical · M major · K minor`.

Audit *also* checks structural fingerprint: if the page uses the AI template (centered hero, 3 equal feature cards, CTA, footer, with no asymmetry or surprise), flag it as a critical structural finding even if the visual treatment is fine.

**Stamp-vs-page check.** If the audited file contains a `/* Hallmark · macrostructure: <name> · ... */` stamp, verify the page actually matches that name. If the stamp says **Bento Grid** but the page is a centered single-column hero with a CTA, flag it as a critical structural finding: `stamp lies` — the stamp must reflect what shipped or be removed. This catches drift where a previous Hallmark run stamped one thing and a later edit pulled the page back toward the AI template.

**Genre-aware audit.** If the audited file's stamp names a genre (e.g. `genre: atmospheric`), apply the genre-scoped overrides from [`slop-test.md`](../slop-test.md) when grading. A radial-gradient background is a critical tell for editorial — but allowed for atmospheric. A pure-white paper is a tell for editorial — but allowed for modern-minimal. The audit verb must respect the genre the page declared.

**`design.md` audit.** If the project root has a `design.md` (or `DESIGN.md`), read it before grading. Then check every audited page against the system:

- **Theme drift.** Page uses tokens / fonts / accent that don't match `design.md`'s declared system → flag as `critical: design-system drift`. Per-page theme picks are slop on a system-managed project even if each page is internally fine.
- **Macrostructure family violation.** `design.md` says marketing pages use Marquee Hero or Stat-Led — the audited page is a Letter format → flag as `major: outside design.md family`.
- **Stamp mismatch.** The page's CSS stamp says `designed-as-app` but reads `design-system: design.md` and the page actually drifts from `design.md` → flag as `critical: stamp lies`. The stamp claims compliance the code doesn't deliver.
- **No stamp at all on a system-managed project** → flag as `major: missing system reference`. Every page on a `design.md` project must stamp its allegiance to the system.

Inversely, on a project *without* `design.md`, the standard diversification rule applies — flag pages that share macrostructure / theme with a previous Hallmark output as `minor: variety drift`.

## Alternate mode: doc-grounded, phased audit

Trigger this mode only when the project actually has the named docs present (check for `DESIGN_SYSTEM.md`, `FRONTEND_GUIDELINES.md`, `APP_FLOW.md`, `PRD.md`, `TECH_STACK.md`, `LESSONS.md`, or their lowercase/`.txt` variants, at the project root or in a `docs/` folder). If none of these exist, stay on the default flat-severity-list flow above — this mode does not replace it.

**Before forming any opinion**, read whatever subset of these exists:

1. `DESIGN_SYSTEM` — tokens, colors, typography, spacing, shadows, radii.
2. `FRONTEND_GUIDELINES` — component engineering, state management, file structure.
3. `APP_FLOW` — every screen, route, user journey.
4. `PRD` — features and requirements.
5. `TECH_STACK` — what the stack actually supports.
6. `LESSONS` — past design mistakes and corrections already learned on this project.

Understand the current system completely before proposing a single change — an audit that contradicts the project's own documented design system isn't a review, it's noise.

**Then run the same dimension sweep as the default flow above**, but compile findings into three approval-gated phases instead of one flat list:

- **Phase 1 — Critical**: hierarchy, usability, responsiveness, consistency issues that actively hurt UX.
- **Phase 2 — Refinement**: spacing, typography, color, alignment, iconography that elevate the experience.
- **Phase 3 — Polish**: micro-interactions, transitions, empty/loading/error states, dark mode, subtle details.

**Present the plan. Do not implement anything.** The user may reorder, cut, or modify any recommendation. Execute only what's approved, surgically, one phase at a time — present results for review before moving to the next phase. If a result doesn't feel right after implementing, say so and propose refinement before proceeding to the next phase.

This is a **stricter, alternate mode of the same `audit` verb**, not a replacement for the default flat-severity-list behavior above — use it only when the project's own docs make a doc-grounded read possible; otherwise the default flow (read the file(s) the user pointed at, return grouped findings, stop) still applies.

*(Source: the doc-reading + phased/approval-gated workflow from bencium.io's `design-audit` skill — MIT, Bencium Limited, see `THIRD-PARTY-LICENSES.md`. Only this process pattern was folded in; that skill's own 14-dimension checklist was left uninstalled since it duplicates the dimension table already above in this same file.)*
