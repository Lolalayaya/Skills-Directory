---
name: personal-learning
description: "Personal knowledge acquisition and retention tools — a systematic reading coach with spaced repetition and mastery testing, a wiki/knowledge-base ingestion pipeline for articles and notes, a Socratic 1-on-1 AI tutor for learning any topic, and a multi-session course-building workspace. Use when the user wants to study a book systematically, quiz themselves on material, compile notes/articles into a structured knowledge base, wants adaptive Socratic-style tutoring on a topic rather than a plain explanation, or wants to build a durable multi-session course/knowledge asset on a topic."
---

# Personal Learning

Router skill for individual knowledge-building — studying material, retaining it, and organizing it into a durable personal knowledge base.

## Domains

| Domain | When to use | Full guide |
|---|---|---|
| Book study coach | Systematic reading with knowledge compilation, mastery testing, spaced repetition, and querying — "read this book with me", "quiz me on the book" | [references/book-study/SKILL.md](references/book-study/SKILL.md) |
| Wiki ingestion | Compile articles, documents, or notes into a structured wiki knowledge base | [references/wiki-ingest/SKILL.md](references/wiki-ingest/SKILL.md) |
| Socratic AI tutor (Sigma) | Bloom's 2-Sigma mastery learning — Socratic questioning, adaptive pacing, rich visual output for any topic | [references/sigma/SKILL.md](references/sigma/SKILL.md) |
| Multi-session teaching workspace | Learn a concept over multiple sessions using the current directory as a stateful course workspace — builds a durable course asset, not a mastery-tracked session | [references/teach/SKILL.md](references/teach/SKILL.md) |

## How to use this skill

1. **Working through a specific book**: `book-study` — it has its own sub-commands (ingest/query/review/compare/status), don't reinvent that flow.
2. **Turning scattered notes/articles into something searchable later**: `wiki-ingest`.
3. **Learning an open-ended topic conversationally** (not a specific book, not just filing notes): `sigma`'s Socratic/adaptive approach for rigorous mastery tracking, or `teach` when the goal is building a durable multi-session course/knowledge-base asset rather than strict mastery testing — pick one, they overlap in trigger phrasing ("teach me", "I want to learn").
4. These can compose: use `book-study` to work through source material, `sigma` to test/deepen understanding of a specific concept from it, and `wiki-ingest` to file the resulting notes for later retrieval.
