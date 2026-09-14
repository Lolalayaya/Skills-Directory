---
name: issue-triage
description: >
  Bulk-audit every open GitHub issue in the current repo — categorize, detect duplicates,
  cross-reference linked PRs, flag security/breaking-change risk, flag staleness.
  Optionally deep-analyze selected issues and draft (never auto-post) comments, labels,
  or closures. Use when open issues are piling up unsorted, before a triage session, or
  when asked to audit/clean up the issue backlog.
  Args: "all" for deep analysis of every issue, issue numbers to focus on (e.g. "42 57"),
  no arg = audit-only pass.
allowed-tools:
  - Bash
  - Read
  - Grep
effort: medium
tags: [triage, issues, github, categorize, duplicates, risk, backlog-audit]
---

# Issue Triage

Bulk-audits the entire open-issue backlog of a GitHub repo: categorize, cross-reference PRs, detect duplicates, flag risk, flag staleness — then optionally draft comments/labels/closures for explicit approval.

> Not the same as [`../triage/SKILL.md`](../triage/SKILL.md): that skill turns *one* issue/PR into an agent-ready spec via a label state machine. This skill audits the *entire* open-issue backlog in one pass for duplicates, staleness, and risk. See also [`../pr-triage/SKILL.md`](../pr-triage/SKILL.md) (same idea for PRs) and [`../full-triage/SKILL.md`](../full-triage/SKILL.md) (runs both together plus cross-analysis).

## When to use

| Skill | Use for | Output |
|-------|---------|--------|
| `issue-triage` | Sort, analyze, and comment on issues | Action tables + optional deep analysis + posted comments |
| `repo-recap` | General status recap to share with the team | Markdown summary (PRs + issues + releases) |

**Triggers**:
- Manually: run this skill, optionally with `all` or specific issue numbers like `42 57`
- Proactively: when there are >10 open issues with no triage pass, or a stale issue (>30 days) is detected

Three-phase workflow: automatic audit → opt-in deep analysis → comments with mandatory approval before posting.

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

# Open issues with full metadata
gh issue list --state open --limit 100 \
  --json number,title,author,createdAt,updatedAt,labels,assignees,body,comments

# Open PRs (for cross-referencing)
gh pr list --state open --limit 50 --json number,title,body

# Recently closed issues (for duplicate detection)
gh issue list --state closed --limit 20 \
  --json number,title,labels,closedAt

# Collaborators (to protect maintainers' own issues from auto-close)
gh api "repos/{owner}/{repo}/collaborators" --jq '.[].login'
```

**Collaborators fallback**: if `gh api .../collaborators` fails (403/404):
```bash
gh pr list --state merged --limit 10 --json author --jq '.[].author.login' | sort -u
```
If still ambiguous, ask the user via `AskUserQuestion`.

**Note**: `author` is an object `{login: "..."}` — always extract `.author.login`.

### Analysis — 6 dimensions

**1. Categorization** (existing labels > title/body inference):
- **Bug**: keywords `crash`, `error`, `fail`, `broken`, `regression`, `wrong`, `unexpected`
- **Feature**: `add`, `implement`, `support`, `new`, `feat:`
- **Enhancement**: `improve`, `optimize`, `better`, `enhance`, `refactor`
- **Question/Support**: `how`, `why`, `help`, `unclear`, `docs`, `documentation`
- **Duplicate candidate**: see dimension 3 below

**2. Cross-ref PRs**:
- Scan every open PR `body` for `fixes #N`, `closes #N`, `resolves #N` (case-insensitive regex)
- Build a map: `issue_number -> [PR numbers]`
- An issue linked to a merged PR → recommend closing it

**3. Duplicate detection**:
- Normalize titles: lowercase, strip prefixes (`bug:`, `feat:`, `[bug]`, `[feature]`, etc.)
- **Jaccard similarity on title words**: score >60% between two issues → duplicate candidate
- Body keyword overlap >50% → reinforces the signal
- Also compare against the 20 most recently closed issues
- A false positive can be confirmed/dismissed in Phase 2

**4. Risk classification**:
- **Red**: keywords `CVE`, `vulnerability`, `injection`, `auth bypass`, `security`, `exploit`, `unsafe`, `credentials`, `leak`, `RCE`, `XSS`
- **Yellow**: `breaking change`, `migration`, `deprecation`, `remove API`, `breaking`, `incompatible`
- **Green**: everything else

**5. Staleness**:
- No activity (`updatedAt`) for >30 days → **Stale**
- No activity for >90 days → **Very Stale**
- Compute from the current date

**6. Recommended actions**:
- `Accept & Prioritize`: clear, reproducible, in-scope issue
- `Label needed`: issue with no label
- `Comment needed`: missing information, insufficient body
- `Linked to PR`: an open PR references this issue
- `Duplicate candidate`: duplicate candidate identified (cite `#N`)
- `Close candidate`: stale with no recent activity, or out of scope (never for a collaborator's own issue)
- `PR merged → close`: linked PR is merged, issue is still open

### Output — 5 tables

```
## Open issues ({count})

### Critical (red risk)
| # | Title | Author | Age | Labels | Action |
| - | ----- | ------ | --- | ------ | ------ |

### Linked to a PR
| # | Title | Author | Linked PR(s) | PR status | Action |
| - | ----- | ------ | ------------ | --------- | ------ |

### Active
| # | Title | Author | Category | Age | Labels | Action |
| - | ----- | ------ | -------- | --- | ------ | ------ |

### Duplicate candidates
| # | Title | Duplicate of | Similarity | Action |
| - | ----- | ------------- | ---------- | ------ |

### Stale
| # | Title | Author | Last activity | Action |
| - | ----- | ------ | -------------- | ------ |

### Summary
- Total: {N} open issues
- Critical: {N} (security or breaking-change risk)
- Linked to PR: {N}
- Duplicate candidates: {N}
- Stale (>30d): {N} | Very Stale (>90d): {N}
- Unlabeled: {N}
- Quick wins (fast to close or label): {list}
```

0 issues → display `No open issues.` and stop.

**Note**: `Age` = days since `createdAt`, formatted `{N}d`. Bold it if >30 days.

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

## Phase 2 — Deep analysis (opt-in)

### Selecting issues

**If an argument was passed**:
- `"all"` → every open issue
- Numbers (`"42 57"`) → only those issues
- No argument → offer choices via `AskUserQuestion`

**If no argument**, show:

```
question: "Which issues do you want to deep-analyze?"
header: "Deep Analysis"
multiSelect: true
options:
  - label: "All ({N} issues)"
    description: "Deep analysis of all issues, run in parallel with subagents"
  - label: "Critical only"
    description: "Focus on the {M} red/yellow-risk issues"
  - label: "Duplicate candidates"
    description: "Confirm or dismiss the {K} detected duplicates"
  - label: "Stale only"
    description: "Close/keep decision for stale issues"
  - label: "Skip"
    description: "Stop here — audit only"
```

If "Skip" → end the workflow.

### Running the analysis

For each selected issue, launch an agent via the **Task tool in parallel**:

```
subagent_type: general-purpose
model: sonnet
prompt: |
  Analyze GitHub issue #{num}: "{title}" by @{author}

  **Metadata**: Created {createdAt}, last updated {updatedAt}, labels: {labels}

  **Body**:
  {body}

  **Existing comments** ({comments_count} total, showing last 5):
  {last_5_comments}

  **Context**:
  - Linked PRs: {linked_prs or "none"}
  - Duplicate candidate of: {duplicate_of or "none"}
  - Risk classification: {risk_color}

  Analyze this issue and return a structured report:
  ### Scope Assessment
  What is this issue actually asking for? Is it clearly defined?

  ### Missing Information
  What's needed to act on this? (reproduction steps, version, environment, etc.)

  ### Risk & Impact
  Security risk? Breaking change? Who's affected?

  ### Effort Estimate
  XS (<1h) / S (1-4h) / M (1-2d) / L (3-5d) / XL (>1 week)

  ### Priority
  P0 (critical, act now) / P1 (high, this sprint) / P2 (medium, backlog) / P3 (low, someday)

  ### Recommended Action
  One of: Accept & Prioritize, Request More Info, Mark Duplicate (#N), Close (Stale), Close (Out of Scope), Link to Existing PR

  ### Draft Comment
  Draft a GitHub comment using the appropriate template from templates/issue-comment.md.
  Be specific, helpful, and constructive.
```

If an issue has >50 comments, summarize only the last 5.

Aggregate all reports. Show a summary once every analysis is done.

---

## Phase 3 — Actions (mandatory approval)

### Possible action types

- **Comment**: `gh issue comment {num} --body-file -`
- **Label**: `gh issue edit {num} --add-label "{label}"` (skip if the label is already present)
- **Close**: `gh issue close {num} --reason "not planned"` (never without approval)

### Generating drafts

For each analyzed issue, generate the actions (comment + labels + closure if applicable) using `templates/issue-comment.md`.

**Rules**:
- Tone: professional, constructive, factual
- Never re-apply a label the issue already has
- Never propose "close" for a collaborator's own issue
- Always show the draft BEFORE any `gh issue comment`

### Display and approval

**Show ALL drafts** in this format:

```
---
### Draft — Issue #{num}: {title}

**Proposed actions**: {Comment | Label: "bug" | Close}

**Comment**:
{full comment text}

---
```

Then ask for approval via `AskUserQuestion`:

```
question: "These actions are ready. Which ones do you want to execute?"
header: "Execute"
multiSelect: true
options:
  - label: "All ({N} actions)"
    description: "Comment + label + close according to the drafts"
  - label: "Issue #{x} — {title_truncated}"
    description: "Execute only the actions for this issue"
  - label: "None"
    description: "Cancel — do nothing"
```

(Generate one option per issue + "All" + "None")

### Execution

For each approved action, execute in order: comment → label → close.

```bash
# Comment
gh issue comment {num} --body-file - <<'COMMENT_EOF'
{comment}
COMMENT_EOF

# Label (if applicable)
gh issue edit {num} --add-label "{label}"

# Close (if applicable)
gh issue close {num} --reason "not planned"
```

Confirm each action: `Comment posted on issue #{num}: {title}`

If "None" → `No action executed. Workflow finished.`

---

## Edge cases

| Situation | Behavior |
|-----------|----------|
| 0 open issues | `No open issues.` + stop |
| Issue with no body | Categorize by title, recommend `Comment needed` |
| >50 comments | Summarize only the last 5 |
| False-positive duplicate | Phase 2 confirms/dismisses — never act on suspicion alone |
| Labels already present | Don't re-apply, note "label already applied" |
| Issue from a collaborator | Never auto-recommend `close candidate` |
| GitHub API rate limit | Reduce `--limit`, notify the user |
| Merged PR linked to an open issue | Recommend closing the issue |
| Issue with no activity >90d | Very Stale — propose closing with a considerate message |
| Duplicate confirmed in Phase 2 | Post comment + close in favor of the original issue |

---

## Notes

- Always derive owner/repo via `gh repo view`, never hardcode it
- Use the `gh` CLI (not raw `curl` against the GitHub API) except for the collaborators list
- `updatedAt` can be null on some issues → treat as `createdAt`
- Never post or close without explicit user approval in chat
- Drafted comments must be visible BEFORE any `gh issue comment`
- Jaccard similarity = |word intersection| / |word union| (excluding stop words: a, the, is, in, of, for, to, with, on, at, by)
