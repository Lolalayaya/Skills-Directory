# Building a Feedback Loop

Before Phase 1's error-reading and evidence-gathering can do much good, you need a **tight, red-capable feedback loop**: one command you can run that goes red on this specific bug and green once it's fixed. If you have that, bisection, hypothesis-testing, and instrumentation all just consume it. If you don't have one, no amount of staring at code will save you — build this first, spend disproportionate effort here.

## Ways to construct one — try in roughly this order

1. **Failing test** at whatever seam reaches the bug — unit, integration, e2e.
2. **Curl / HTTP script** against a running dev server.
3. **CLI invocation** with a fixture input, diffing stdout against a known-good snapshot.
4. **Headless browser script** (Playwright / Puppeteer) — drives the UI, asserts on DOM/console/network.
5. **Replay a captured trace.** Save a real network request / payload / event log to disk; replay it through the code path in isolation.
6. **Throwaway harness.** Spin up a minimal subset of the system (one service, mocked deps) that exercises the bug code path with a single function call.
7. **Property / fuzz loop.** If the bug is "sometimes wrong output", run 1000 random inputs and look for the failure mode.
8. **Bisection harness.** If the bug appeared between two known states (commit, dataset, version), automate "boot at state X, check, repeat" so you can `git bisect run` it.
9. **Differential loop.** Run the same input through old-version vs new-version (or two configs) and diff outputs.
10. **HITL bash script.** Last resort. If a human must click, drive _them_ with [hitl-loop.template.sh](hitl-loop.template.sh) so the loop is still structured. Captured output feeds back to you.

## Tighten the loop

Treat the loop as a product. Once you have _a_ loop, tighten it:

- Can I make it faster? (Cache setup, skip unrelated init, narrow the test scope.)
- Can I make the signal sharper? (Assert on the specific symptom, not "didn't crash".)
- Can I make it more deterministic? (Pin time, seed RNG, isolate filesystem, freeze network.)

A 30-second flaky loop is barely better than no loop; a 2-second deterministic one is a debugging superpower.

## Non-deterministic bugs

The goal is not a clean repro but a **higher reproduction rate**. Loop the trigger 100×, parallelise, add stress, narrow timing windows, inject sleeps. A 50%-flake bug is debuggable; 1% is not — keep raising the rate until it's debuggable.

## When you genuinely cannot build a loop

Stop and say so explicitly. List what you tried. Ask your human partner for: (a) access to whatever environment reproduces it, (b) a captured artifact (HAR file, log dump, core dump, screen recording with timestamps), or (c) permission to add temporary production instrumentation. Do **not** proceed to hypothesise without a loop.

## Completion criterion

The loop is ready when you can name **one command** — a script path, a test invocation, a curl — that you have **already run at least once** (paste the invocation and its output), and that is:

- [ ] **Red-capable** — drives the actual bug code path and asserts the **user's exact symptom**, so it goes red on this bug and green once fixed. Not "runs without erroring."
- [ ] **Deterministic** — same verdict every run (flaky bugs: a pinned, high reproduction rate, per above).
- [ ] **Fast** — seconds, not minutes.
- [ ] **Agent-runnable** — you can run it unattended; a human in the loop only via [hitl-loop.template.sh](hitl-loop.template.sh).

If you catch yourself reading code to build a theory before this command exists — stop. Jumping straight to a hypothesis is the exact failure this step prevents.
