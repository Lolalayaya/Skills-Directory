---
name: pr-triage
description: >
  Bulk-audit every open GitHub PR in the current repo — size, CI status, overlap/conflict
  detection, author clusters, staleness. Optionally deep-review selected PRs with a
  code-reviewer subagent and draft (never auto-post) review comments. Use when open PRs
  are piling up unreviewed, before a review session, or when asked to audit/clean up the
  PR backlog.
  Args: "all" to review every external PR, PR numbers to focus on (e.g. "42 57"), no arg
  = audit-only pass.
allowed-tools:
  - Bash
  - Read
  - Grep
effort: medium
tags: [triage, pr, github, review, code-review, backlog-audit]
---

# PR Triage

Bulk-audits the entire open-PR backlog of a GitHub repo: size, CI status, overlaps, author clusters, staleness — then optionally runs deep code review and drafts comments for explicit approval.

> See also [`../issue-triage/SKILL.md`](../issue-triage/SKILL.md) (same idea for issues), [`../full-triage/SKILL.md`](../full-triage/SKILL.md) (runs both together plus cross-analysis), and [`../pr-review/SKILL.md`](../pr-review/SKILL.md) (a different workflow: reviews and merges PRs one at a time with your sign-off on each, rather than bulk-auditing and drafting comments).

## When to use

| Skill | Use for | Output |
|-------|---------|--------|
| `pr-triage` | Sort, review, and comment on PRs | Action table + reviews + posted comments |
| `repo-recap` | General status recap to share with the team | Markdown summary (PRs + issues + releases) |

**Triggers**:
- Manually: run this skill, optionally with `all` or specific PR numbers like `42 57`
- Proactively: when there are >5 open PRs with no review, or a stale PR (>14 days) is detected

Three-phase workflow: automatic audit → opt-in deep review → comments with mandatory approval before posting.

## Preconditions

```bash
git rev-parse --is-inside-work-tree
gh auth status
```

If either fails, stop and explain what's missing.

---

## Phase 1 — Audit (always runs)

### Data gathering (run in parallel)

```bash
# Repo identity
gh repo view --json nameWithOwner -q .nameWithOwner

# Open PRs with full metadata (include body for issue cross-referencing)
gh pr list --state open --limit 50 \
  --json number,title,author,createdAt,updatedAt,additions,deletions,changedFiles,isDraft,mergeable,reviewDecision,statusCheckRollup,body

# Collaborators (to separate "our PRs" from external ones)
gh api "repos/{owner}/{repo}/collaborators" --jq '.[].login'
```

**Collaborators fallback**: if `gh api .../collaborators` fails (403/404):
```bash
# Extract authors from the last 10 merged PRs
gh pr list --state merged --limit 10 --json author --jq '.[].author.login' | sort -u
```
If still ambiguous, ask the user via `AskUserQuestion`.

For each PR, fetch existing reviews AND changed files:

```bash
gh api "repos/{owner}/{repo}/pulls/{num}/reviews" \
  --jq '[.[] | .user.login + ":" + .state] | join(", ")'

# Changed files (needed for overlap detection)
gh pr view {num} --json files --jq '[.files[].path] | join(",")'
```

**Rate-limiting note**: fetching files is one API call per PR. For repos with 20+ PRs, prioritize the PRs most likely to overlap (same functional area, same author).

**Note**: `author` is an object `{login: "..."}` — always extract `.author.login`.

### Analysis

**Size classification**:
| Label | Additions |
|-------|-----------|
| XS | < 50 |
| S | 50–200 |
| M | 200–500 |
| L | 500–1000 |
| XL | > 1000 |

Size format: `+{additions}/-{deletions}, {files} files ({label})`

**Detections**:
- **Overlaps**: compare file lists between PRs — if >50% of files are shared → cross-reference
- **Clusters**: an author with 3+ open PRs → suggest a review order (smallest first)
- **Staleness**: no activity for >14 days → flag "stale"
- **CI status**: via `statusCheckRollup` → `clean` / `unstable` / `dirty`
- **Reviews**: approved / changes_requested / none

**PR ↔ Issue links**:
- Scan each PR's `body` for `fixes #N`, `closes #N`, `resolves #N` (case-insensitive)
- If found, show it in the table: `Fixes #42` in the Action/Status column

**Categorization**:

_Our PRs_: author is in the collaborators list

_External — Ready_: additions ≤ 1000 AND files ≤ 10 AND `mergeable` ≠ `CONFLICTING` AND CI clean/unstable

_External — Problematic_: any of the following:
- additions > 1000 OR files > 10
- OR `mergeable` == `CONFLICTING`
- OR CI dirty (`statusCheckRollup` contains failures)
- OR overlaps another open PR (>50% shared files)

### Output — Triage table

```
## Open PRs ({count})

### Our PRs
| PR | Title | Size | CI | Status |
| -- | ----- | ---- | -- | ------ |

### External — Ready for review
| PR | Author | Title | Size | CI | Reviews | Action |
| -- | ------ | ----- | ---- | -- | ------- | ------ |

### External — Problematic
| PR | Author | Title | Size | Problem | Recommended action |
| -- | ------ | ----- | ---- | ------- | ------------------- |

### Summary
- Quick wins: {XS/S PRs ready to merge}
- Risks: {overlaps, XL sizes, CI dirty}
- Clusters: {authors with 3+ PRs}
- Stale: {PRs with no activity >14d}
- Overlaps: {PRs touching the same files}
```

0 PRs → display `No open PRs.` and stop.

### Auto-copy

After displaying the triage table, copy it to the clipboard:
```bash
# Cross-platform clipboard
clip() {
  if command -v pbcopy &>/dev/null; then pbcopy
  elif command -v xclip &>/dev/null; then xclip -selection clipboard
  elif command -v wl-copy &>/dev/null; then wl-copy
  else cat
  fi
}

clip <<'EOF'
{full triage table}
EOF
```
Confirm: `Table copied to clipboard.`

---

## Phase 2 — Deep review (opt-in)

### Selecting PRs

**If an argument was passed**:
- `"all"` → every external PR
- Numbers (`"42 57"`) → only those PRs
- No argument → offer choices via `AskUserQuestion`

**If no argument**, show:

```
question: "Which PRs do you want to deep-review?"
header: "Deep Review"
multiSelect: true
options:
  - label: "All external"
    description: "Review {N} external PRs with code-reviewer subagents in parallel"
  - label: "Problematic only"
    description: "Focus on the {M} at-risk PRs (CI dirty, oversized, overlaps)"
  - label: "Ready only"
    description: "Review {K} PRs that are ready to merge"
  - label: "Skip"
    description: "Stop here — audit only"
```

**Note on drafts**:
- Draft PRs are EXCLUDED from "All external" and "Ready only"
- Draft PRs are INCLUDED in "Problematic only" (they need attention)
- To review a draft, name its number explicitly (e.g. `42`)

If "Skip" → end the workflow.

### Running the reviews

For each selected PR, launch a `code-reviewer` agent via the **Task tool in parallel**:

```
subagent_type: code-reviewer
model: sonnet
prompt: |
  Review PR #{num}: "{title}" by @{author}

  **Metadata**: +{additions}/-{deletions}, {changedFiles} files ({size_label})
  **CI**: {ci_status} | **Reviews**: {existing_reviews} | **Draft**: {isDraft}

  **PR Body**:
  {body}

  **Diff**:
  {gh pr diff {num} output}

  Apply your standard security and architecture review lenses.
  If this repo has its own documented conventions (contribution guide, coding
  standards doc, style checklist), apply those too.

  Return structured review:
  ### Critical Issues 🔴
  ### Important Issues 🟡
  ### Suggestions 🟢
  ### What's Good ✅

  Be specific: quote the file:line, explain why it's an issue, suggest the fix.
```

Fetch the diff via:
```bash
gh pr diff {num}
gh pr view {num} --json body,title,author -q '{body: .body, title: .title, author: .author.login}'
```

Aggregate all reports. Show a summary once every review is done.

---

## Phase 3 — Comments (mandatory approval)

### Generating drafts

For each reviewed PR, generate a GitHub comment using the `templates/review-comment.md` template.

**Rules**:
- Tone: professional, constructive, factual
- Always include at least 1 positive point
- Cite code lines when relevant (format `file.rs:42`)

### Display and approval

**Show ALL drafted comments** in this format:

```
---
### Draft — PR #{num}: {title}

{full comment text}

---
```

Then ask for approval via `AskUserQuestion`:

```
question: "These comments are ready. Which ones do you want to post?"
header: "Post"
multiSelect: true
options:
  - label: "All ({N} comments)"
    description: "Post on every reviewed PR"
  - label: "PR #{x} — {title_truncated}"
    description: "Post only on this PR"
  - label: "None"
    description: "Cancel — post nothing"
```

(Generate one option per PR + "All" + "None")

### Posting

For each approved comment:

```bash
gh pr comment {num} --body-file - <<'REVIEW_EOF'
{comment}
REVIEW_EOF
```

Confirm each post: `✅ Comment posted on PR #{num}: {title}`

If "None" → `No comment posted. Workflow finished.`

---

## Edge cases

| Situation | Behavior |
|-----------|----------|
| 0 open PRs | `No open PRs.` + stop |
| Draft PR | Show in the table, skip for review unless explicitly selected |
| Unknown CI | Show `?` in the CI column |
| Review agent timeout | Show a partial error, continue with the others |
| `gh pr diff` empty | Skip this PR, notify the user |
| Very large PR (>5000 additions) | Warn: "Partial review, diff truncated" |
| Collaborators API 403/404 | Fall back to authors of the last 10 merged PRs |

---

## Notes

- Always derive owner/repo via `gh repo view`, never hardcode it
- Use the `gh` CLI (not raw `curl` against the GitHub API) except for the collaborators list
- `statusCheckRollup` can be null → treat as `?`
- `mergeable` can be `MERGEABLE`, `CONFLICTING`, or `UNKNOWN` → treat `UNKNOWN` as `?`
- Never post without explicit user approval in chat
- Drafted comments must be visible BEFORE any `gh pr comment`
