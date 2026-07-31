---
name: personal-learning
description: "Personal knowledge acquisition and retention tools — a systematic reading coach with spaced repetition and mastery testing, a wiki/knowledge-base ingestion pipeline for articles and notes, and a Socratic 1-on-1 AI tutor for learning any topic. Use when the user wants to study a book systematically, quiz themselves on material, compile notes/articles into a structured knowledge base, or wants adaptive, Socratic-style tutoring on a topic rather than a plain explanation."
---

# Personal Learning

Router skill for individual knowledge-building — studying material, retaining it, and organizing it into a durable personal knowledge base.

## Domains

| Domain | When to use | Full guide |
|---|---|---|
| Book study coach | Systematic reading with knowledge compilation, mastery testing, spaced repetition, and querying — "read this book with me", "quiz me on the book" | [references/book-study/SKILL.md](references/book-study/SKILL.md) |
| Wiki ingestion | Compile articles, documents, or notes into a structured wiki knowledge base | [references/wiki-ingest/SKILL.md](references/wiki-ingest/SKILL.md) |
| Socratic AI tutor (Sigma) | Bloom's 2-Sigma mastery learning — Socratic questioning, adaptive pacing, rich visual output for any topic | [references/sigma/SKILL.md](references/sigma/SKILL.md) |

## How to use this skill

1. **Working through a specific book**: `book-study` — it has its own sub-commands (ingest/query/review/compare/status), don't reinvent that flow.
2. **Turning scattered notes/articles into something searchable later**: `wiki-ingest`.
3. **Learning an open-ended topic conversationally** (not a specific book, not just filing notes): `sigma`'s Socratic/adaptive approach.
4. These can compose: use `book-study` to work through source material, `sigma` to test/deepen understanding of a specific concept from it, and `wiki-ingest` to file the resulting notes for later retrieval.
