---
name: background-research
description: Investigate a single question against high-trust primary sources and capture the findings as a cited Markdown file, via a background agent — a one-shot lookup, not a multi-item pipeline. Use when the user wants one topic/question researched, docs or API facts gathered, or reading legwork delegated to a background agent. For a structured outline→fields/items→multi-agent→report pipeline over several comparable items instead, see this same skill's `research` (outline stage) through `research-report`.
---

Spin up a **background agent** to do the research, so you keep working while it reads.

Its job:

1. Investigate the question against **primary sources** — official docs, source code, specs, first-party APIs — not a secondary write-up of them. Follow every claim back to the source that owns it.
2. Write the findings to a single Markdown file, citing each claim's source.
3. Save it where the repo already keeps such notes; match the existing convention, and if there is none, put it somewhere sensible and say where.
