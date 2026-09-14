---
name: full-triage
description: >
  Orchestrates issue-triage + pr-triage together and cross-analyzes the results —
  double coverage (2 PRs for 1 issue), security findings with no PR, P0/P1 bugs with no
  PR, our own dirty/conflicting PRs. Saves a dated report to disk. Use for a
  weekly/pre-sprint deep backlog sweep, or when the PR/issue backlog is growing fast and
  duplicated effort is suspected.
  Args: "save" to force saving the report even if it would otherwise be skipped.
allowed-tools:
  - Bash
  - Write
  - Read
  - AskUserQuestion
effort: high
tags: [triage, orchestration, issues, pr, security, cross-analysis, backlog-audit]
---

# Full Triage

Orchestrates [`../issue-triage/SKILL.md`](../issue-triage/SKILL.md) and [`../pr-triage/SKILL.md`](../pr-triage/SKILL.md), then adds a cross-analysis pass that neither one does alone: duplicate coverage, security gaps, and stuck work that spans both issues and PRs.

---

## When to use

- Weekly, or before each sprint
- When the PR/issue backlog is growing fast
- To spot duplicated effort before review starts

---

## Four-phase workflow

### Phase 0 — Preconditions

```bash
git rev-parse --is-inside-work-tree
gh auth status
```

Confirm the current date is known (`date +%Y-%m-%d`).

---

### Phase 1 — Data gathering (parallel)

Run both collections simultaneously:

**Issues**:
```bash
gh repo view --json nameWithOwner -q .nameWithOwner

gh issue list --state open --limit 150 \
  --json number,title,author,createdAt,updatedAt,labels,assignees,body

gh issue list --state closed --limit 20 \
  --json number,title,labels,closedAt

gh api "repos/{owner}/{repo}/collaborators" --jq '.[].login'
```

**PRs**:
```bash
# Fetch every open PR — paginate if needed (gh caps at 200 per call)
gh pr list --state open --limit 200 \
  --json number,title,author,createdAt,updatedAt,additions,deletions,changedFiles,isDraft,mergeable,reviewDecision,statusCheckRollup,body

# If the repo has >200 open PRs, re-run with --search to paginate:
# gh pr list --state open --limit 200 --search "is:pr is:open sort:updated-desc" ...

# For each PR, fetch changed files (needed for overlap detection)
# Prioritize candidate PRs (same domain, same author)
gh pr view {num} --json files --jq '[.files[].path] | join(",")'
```

---

### Phase 2 — Individual triage

Run the same analysis as `issue-triage` and `pr-triage` independently to produce:

**Issues**:
- Categorization (Bug/Feature/Enhancement/Question/Duplicate)
- Risk (Red/Yellow/Green)
- Staleness (>30d)
- Map `issue_number → [PR numbers]` via scanning `fixes #N`, `closes #N`, `resolves #N`

**PRs**:
- Size (XS/S/M/L/XL)
- CI status (clean/dirty)
- Ours vs. external
- Overlaps (>50% shared files between 2 PRs)
- Clusters (author with 3+ PRs)

Show the standard tables from each skill (see `issue-triage`'s and `pr-triage`'s SKILL.md for the exact format).

---

### Phase 3 — Cross-analysis (the point of this skill)

This is where this skill adds value beyond the two individual skills.

#### 3.1 Double coverage — 2 PRs for 1 issue

For each issue linked to ≥2 PRs (via body scan + file overlap):

| Issue | PR1 (info) | PR2 (info) | Recommended verdict |
|-------|-------------|-------------|-------------------|
| #N (title) | PR#X — author, size, CI | PR#Y — author, size, CI | Keep the more targeted one. Close/coordinate the other |

Verdict rule:
- Prefer the smaller one (XS < S < M) if same scope
- Prefer clean CI over dirty CI
- Prefer "our PRs" if one is internal
- If file overlap >80% → near-certain conflict, flag it

#### 3.2 Security coverage gaps

For each red-risk issue (e.g. a security-review issue with sub-findings):
- List the sub-findings mentioned in the body
- Cross-reference against existing PRs (keywords in title/body)
- Identify findings with no PR

Format:
```
## Issue #N — security review (finding by finding)
| Finding | Associated PR | Status |
|---------|-------------|--------|
| Description of finding 1 | PR#X | In review |
| **Description of critical finding** | **NONE** | ⚠️ Gap |
```

#### 3.3 P0/P1 bugs with no PR

Issues labeled P0 or P1 (or keywords: "crash", "truncat", "cap", "hardcoded") with no linked PR.

Format:
```
## Critical bugs with no PR
| Issue | Title | Common pattern | Estimated effort |
|-------|-------|----------------|---------------|
```

Look for a common pattern (e.g. "hardcoded cap", "lost exit code") — if 3+ bugs share a pattern, suggest a grouped sprint.

#### 3.4 Our dirty PRs — likely causes

For each internal PR with dirty CI or CONFLICTING state:
- Check whether another PR touches the same files
- Check whether a recent merge to the base branch could explain the conflict
- Recommend: rebase, close, or wait

Format:
```
## Our dirty PRs
| PR | Issue(s) | Likely cause | Action |
|----|----------|----------------|--------|
```

#### 3.5 PRs with no tracked issue

Internal PRs with no `fixes #N` in the body — flag for traceability.

---

### Phase 4 — Final output

#### Show the full cross-analysis (sections 3.1 → 3.5)

Then show the numeric summary:

```
## Numeric summary — YYYY-MM-DD

| Category | Count |
|-----------|-------|
| Our PRs ready to merge | N |
| External quick wins | N |
| Double coverage (conflicts) | N pairs |
| P0/P1 bugs with no PR | N |
| Security findings with no PR | N |
| Our dirty PRs needing rebase | N |
| PRs recommended for closure | N |
```

#### Save to disk

```bash
gh repo view --json name -q .name  # for the filename
date +%Y-%m-%d
```

Save to `./triage-reports/{repo-name}-YYYY-MM-DD.md` with:
- The issue + PR triage tables (Phase 2)
- The full cross-analysis (Phase 3)
- The numeric summary

Confirm: `Saved to triage-reports/{repo-name}-YYYY-MM-DD.md`

---

## Saved file format

```markdown
# {Repo Name} Triage — YYYY-MM-DD

Cross-referencing issues × PRs. {N} open PRs, {N} open issues.

---

## 1. Double coverage
...

## 2. Security gaps
...

## 3. P0/P1 with no PR
...

## 4. Our dirty PRs
...

## 5. Our PRs ready to merge
...

## 6. External quick wins
...

## 7. Priority actions
(ordered by impact/urgency)

---

## Numeric summary
...
```

---

## Rules

- Never post GitHub comments without user approval (`AskUserQuestion`).
- If >200 issues or >200 PRs: warn the user and paginate (re-run with `--search` or paginated `gh api`).
- The cross-analysis (Phase 3) always runs — it's this skill's whole value-add over running the two individual skills separately.
- The report file is saved automatically unless the user says "no save".
