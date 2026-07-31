---
name: grilling
description: Grill the user relentlessly about a plan, decision, or idea. Use when the user wants to stress-test their thinking, or uses any 'grill' trigger phrases.
argument-hint: "[--batch] optional: what to grill me about"
---

Interview me relentlessly about every aspect of this until we reach a shared understanding. Map this as a **design tree**: every decision branches into the decisions that hang off it. For each question, provide your recommended answer.

Finding *facts* is your job, never mine. When a question needs a fact from the environment (filesystem, tools, etc.), look it up yourself — dispatch a sub-agent for it if useful — rather than asking me. The *decisions* are mine — put each one to me and wait for my answer. Do not act on it until I confirm we have reached a shared understanding.

## Default mode: one at a time

Walk down each branch of the decision tree, resolving dependencies between decisions one-by-one. Ask the questions **one at a time**, waiting for feedback on each before continuing. Asking multiple questions at once is bewildering — this is the default for a reason.

## Batch mode: whole frontier per round

If the user passes `--batch`, or the tree has many independent decisions where speed matters more than avoiding overwhelm, work the tree in **rounds** instead:

The **frontier** is every decision whose prerequisites are already settled — the questions you can ask *now* without guessing at answers you haven't heard yet. Ask the whole frontier in one round: number each question and give your recommended answer. Then wait for the user's answers before the next round.

Each round the user answers reshapes the tree — settled decisions push the frontier outward and unblock questions that depended on them. Recompute the frontier and ask the next round. A question whose answer depends on another question still open in this round belongs to a *later* round, not this one.

When exploring the environment for facts in batch mode, don't block the whole round on one lookup: a running exploration is an unsettled prerequisite, so only the questions downstream of it wait — ask the rest of the frontier now.

## Done

The session is done when every branch of the design tree has been visited and nothing is left silently assumed (one-at-a-time mode), or the frontier is empty (batch mode). Do not act on it until the user confirms a shared understanding has been reached.
