# Review Comment Template

Use this template to generate GitHub PR review comments. Fill in each section based on the code-reviewer agent output.

---

## Template

```markdown
## Review

**Scope**: Security, code quality, performance, test coverage, architecture

### Summary

{1–2 sentences: overall assessment. Be direct — what's the main takeaway?}

### Critical Issues 🔴

{List blocking issues that must be fixed before merge. For each:}
{- `file.ext:42` — Description of the problem. Why it matters. Suggested fix.}

{If none: "None found."}

### Important Issues 🟡

{List significant issues that should be fixed. For each:}
{- `file.ext:42` — Description. Why it matters. Suggested fix.}

{If none: "None found."}

### Suggestions 🟢

{List nice-to-haves and minor improvements. For each:}
{- Description. Context. Optional fix.}

{If none: omit this section.}

### What's Good ✅

{Always include at least 1 positive point. Be specific — what works well and why.}
{- Description of what's done right.}
```

---

## Formatting Rules

**Citation format**: `file.ext:42` or `` `code snippet` `` for inline references

**Issue severity**:
- 🔴 Critical: security vulnerability, data loss risk, broken functionality, missing test for new behavior
- 🟡 Important: error handling gap, performance regression, scope creep, missing test coverage for an edge case
- 🟢 Suggestion: naming, DRY opportunity, documentation, style

**Project-specific checks to mention if relevant**: if this repo has documented conventions (a style guide, a required error-handling pattern, a performance budget, a "no synthetic test data" rule), check the diff against those and cite them explicitly — the same way the original template checked against RTK's own Rust CLI conventions.

**Tone**: Professional, constructive, factual. Challenge the code, not the person.
No superlatives ("great", "amazing", "perfect"). No filler ("as mentioned", "it's worth noting").

**Length**: Aim for 200–400 words. Long enough to be useful, short enough to be read.
