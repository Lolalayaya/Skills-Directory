---
name: pr-review
description: >
  Interactively review and merge open PRs one at a time, smallest first — check
  mergeability/CI/CLA/review state, read the full diff, present a summary, and wait for
  your explicit go-ahead before merging. Drafts a comment for any blocked PR (conflict,
  CLA, changes requested). Use when working through a PR backlog PR-by-PR with a merge
  decision on each one, as opposed to a bulk audit.
  Args: "triage" to run pr-triage first and use its quick-wins list as the queue,
  "from:<num>" to resume from a specific PR number.
allowed-tools:
  - Bash
  - Read
  - Grep
  - Glob
  - Write
  - AskUserQuestion
tags: [pr, review, merge, github, code-review]
---

# PR Review

Batch PR review — smallest to largest, one at a time, with your explicit sign-off before every merge.

> Different from [`../pr-triage/SKILL.md`](../pr-triage/SKILL.md): that skill bulk-audits the whole PR backlog and drafts review *comments* for later posting. This skill walks the queue interactively and can actually *merge* PRs, one at a time, only with your explicit approval on each. Also different from the top-level `code-review` skill, which reviews a single diff/PR for correctness bugs rather than working a merge queue.

---

## When to use

- After a `pr-triage` pass, to act on its results
- Regularly, to work down the backlog
- Before a release, to clear quick-win PRs out of the queue

---

## Workflow

### Phase 0 — Preconditions

```bash
git rev-parse --is-inside-work-tree
gh auth status
date +%Y-%m-%d
```

If the `triage` argument was passed, run `pr-triage` first and use its quick-wins list as the queue. Otherwise, build the list yourself.

---

### Phase 1 — Build the PR list (if no triage was run)

```bash
gh pr list --state open --limit 200 \
  --json number,title,author,additions,deletions,changedFiles,mergeable,mergeStateStatus,isDraft,statusCheckRollup,reviewDecision,body \
  | jq 'sort_by(.additions + .deletions)'
```

**Sort by size**:

| Size | Criteria | Handling |
|--------|---------|------------|
| XS | < 30 lines, 1 file | First |
| S | 30-100 lines, 1-3 files | Next |
| M | 100-200 lines, non-trivial logic | After |
| L | > 200 lines | Last, or skip |
| XL | > 500 lines | Skip (dedicated session) |

**Filter up front**:
- Exclude draft PRs
- Exclude your own PRs (those typically have a different review flow)
- If `from:<num>` was passed as an argument, start at that number

---

### Phase 2 — For each PR (one at a time, in order)

#### Step A — Check state (BEFORE reading the diff)

```bash
# 1. Derive owner/repo — never hardcode it
gh repo view --json nameWithOwner -q .nameWithOwner

# 2. Mergeable state + CI/CLA rollup
gh pr view <num> --json mergeable,mergeStateStatus,statusCheckRollup,reviewDecision

# 3. Existing reviews (CHANGES_REQUESTED?)
gh api repos/{owner}/{repo}/pulls/<num>/reviews \
  --jq '.[] | {author: .user.login, state: .state, body: .body}'

# 4. Inline comments (if CHANGES_REQUESTED)
gh api repos/{owner}/{repo}/pulls/<num>/comments \
  --jq '.[] | {author: .user.login, body: .body, path: .path, line: .line}'
```

**Quick decision by state**:

| State | Action |
|------|--------|
| MERGEABLE + no CHANGES_REQUESTED | → read the diff |
| CONFLICTING | → prepare a rebase comment, skip the diff |
| CLA unsigned (if this repo requires one) | → prepare a CLA comment, skip the diff |
| CHANGES_REQUESTED by a maintainer | → skip (don't override), note it |
| Draft | → skip silently |

#### Step B — Read the full diff

```bash
gh pr diff <num>
```

If the diff touches complex logic, read the source file in context with `Read` to understand the real impact.

#### Step C — Present to the user

**Mandatory** presentation format for each PR:

```
**PR #<num>** — https://github.com/{owner}/{repo}/pull/<num>

**Author**: <login> | **Size**: <XS/S/M/L> (+<add> -<del>, <N> files) | **Mergeable**: <clean/conflict>

**What it does** — [2-4 sentences: the problem solved, files touched, logic changed, tests added]

**Diff quality**: [honest assessment: clean / needs a second look / issue detected]

Merge #<num>?
```

**Presentation rules**:
- Always include the clickable GitHub link
- Always mention whether tests cover the change
- If a complex function is touched, explain the impact
- Don't embellish — if the diff is mediocre, say so
- Be direct and factual — no filler, no forced enthusiasm

#### Step D — Wait for approval

**NEVER MERGE WITHOUT AN EXPLICIT RESPONSE.** Expected responses:

| Response | Action |
|---------|--------|
| "ok" / "go" / "merge" | Merge with `gh pr merge --merge` |
| "skip" / "next" | Move to the next PR without merging |
| "comment" | Post a comment (ask for the text if not provided) |
| "close" | Close the PR |
| Feedback with instructions | Apply it, then ask for confirmation again |

#### Step E — Merge (if approved)

```bash
gh pr merge <num> --merge --squash
```

Confirm immediately: `Merged #<num>. ✓`

Then **check that the next PR hasn't turned CONFLICTING** because of this merge — especially if both PRs touch the same frequently-modified files (check `changedFiles` overlap from Phase 1's data, or the repo's own CONTRIBUTING notes if it documents hot files).

---

### Phase 3 — Blocked PRs: drafted comment

For PRs with a conflict, missing CLA, or needing a rebase, post a comment with the tone rules below.

**Comment rules**:
- Thank the contributor genuinely in the opening (specific to their contribution, not generic)
- State clearly what's blocking (1-2 points max)
- Give the exact steps to unblock
- No em dashes, no staccato rhythm, vary sentence length
- Don't sound like a bot

**Conflict + CLA template**:
```
Hey @<author>, thanks for the contribution! [specific mention of what the PR adds]

Two things before we can merge:

1. The branch needs a rebase on `<base-branch>` — there's a conflict on [file]. A `git rebase origin/<base-branch>` should do it.

2. The CLA hasn't been signed yet (if this repo requires one) — follow the bot's instructions in the PR, takes about a minute.

Once both are sorted, this will move quickly.
```

**Conflict-only template**:
```
Hey @<author>, good fix on [specific description]. One thing to address before merge: the branch has a conflict on [file] after recent changes to `<base-branch>`. A `git rebase origin/<base-branch>` should resolve it cleanly.
```

**CLA-only template**:
```
Hey @<author>, thanks for [specific description]. The only thing blocking merge is the CLA signature — the bot left the link in the PR. Once that's done, we're good to go.
```

---

### Phase 4 — Session recap

After processing all PRs (or on request):

```
## Session recap — YYYY-MM-DD

| PR | Title | Action | Reason |
|----|-------|--------|--------|
| #N | title | Merged ✓ | — |
| #N | title | Skipped | CHANGES_REQUESTED (reviewer) |
| #N | title | Commented | Conflict + CLA |
| #N | title | Closed | Duplicate of #M |

Merged: N | Skipped: N | Commented: N
```

---

## Rules

- **One PR at a time** — never present multiple PRs awaiting approval at once
- **Never merge without an explicit "ok"** — "looks good" is not approval
- **Don't override a CHANGES_REQUESTED** from a maintainer without the user's explicit instructions
- **Check for post-merge conflicts** on the next PR if both touch the same files
- **Tone**: factual, direct, considerate — no AI tells (em dashes, staccato rhythm, a too-perfect closing line)

---

## Notes

- Always derive owner/repo via `gh repo view`, never hardcode a specific repo — hardcoding it is exactly the kind of bug this skill should avoid reproducing
- If this repo documents a set of files that frequently conflict across concurrent PRs (a CONTRIBUTING guide, a CODEOWNERS-adjacent note), watch those specifically after each merge
