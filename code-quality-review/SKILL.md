---
name: code-quality-review
description: "Standardize how code gets reviewed and secured — senior-engineer-lens review for SOLID violations and security risks, static analysis via Semgrep (including writing custom detection rules), secure-coding guidelines, LLM/RAG-application security (OWASP Top 10 for LLM), and the protocol for requesting and receiving code review with technical rigor rather than performative agreement. Use whenever code is about to be reviewed, merged, or scanned for vulnerabilities; when writing or reviewing code that touches user input, authentication, file operations, database queries, network requests, cryptography, or infrastructure config (Terraform/Kubernetes/Docker/GitHub Actions) — even if the user doesn't explicitly mention security; and when the user asks 'review my code', 'is this safe', 'scan with semgrep', or wants a second opinion before or after a PR."
---

# Code Quality & Review

Router skill for standardizing code review and security scanning instead of relying on whichever engineer happens to be reviewing. Several domains here compose naturally: a real review pass should combine a senior-engineer read, a static-analysis scan, and the request/receive discipline.

## Domains

| Domain | When to use | Full guide |
|---|---|---|
| Senior-engineer code review | Review current git changes for SOLID violations, security risks, actionable fixes | [references/code-review-expert/SKILL.md](references/code-review-expert/SKILL.md) |
| Semgrep static analysis | Run Semgrep scans, write custom YAML detection rules, find specific bug patterns | [references/semgrep/SKILL.md](references/semgrep/SKILL.md) |
| Secure coding guidelines | General secure-coding checklist — SQL injection, auth, file ops, crypto, infra config (Terraform/K8s/Docker/GH Actions) | [references/code-security/SKILL.md](references/code-security/SKILL.md) |
| LLM/RAG application security | OWASP Top 10 for LLM 2025 — prompt injection, RAG vulnerabilities, LLM app security review | [references/llm-security/SKILL.md](references/llm-security/SKILL.md) |
| Requesting code review | Protocol for asking for review when completing tasks or before merging major features | [references/requesting-code-review/SKILL.md](references/requesting-code-review/SKILL.md) |
| Receiving code review | Protocol for evaluating review feedback with technical rigor before implementing it — especially when feedback seems unclear or questionable; not blind agreement | [references/receiving-code-review/SKILL.md](references/receiving-code-review/SKILL.md) |

## How to use this skill

1. **Writing code that touches a sensitive surface** (user input, auth, file ops, DB queries, network calls, crypto, infra config): consult `code-security` (and `llm-security` if it's an LLM/RAG app) proactively, even if the user didn't ask for a security review — this is a standing trigger, not an opt-in.
2. **Before merging / opening a PR**: run `code-review-expert` for a structural/SOLID pass and `semgrep` for a static-analysis pass. These are complementary, not redundant — one reads intent, the other pattern-matches known vulnerability shapes.
3. **Asking for review**: follow `requesting-code-review`'s protocol for when/how to surface work for review.
4. **Getting review feedback back**: follow `receiving-code-review` — verify unclear or technically questionable feedback rather than agreeing performatively; push back with evidence when the reviewer is wrong.

## Standing triggers worth keeping active

Per `code-security`: treat *any* code handling user input, authentication, file operations, database queries, network requests, cryptography, or infrastructure config as an implicit review trigger — don't wait for the user to say "check this for security."

Per `receiving-code-review`: reviewer feedback is not automatically correct. Verify it against the actual codebase/behavior before implementing; technical rigor beats agreeableness.
