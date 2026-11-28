# tests/cases: short held-out cases

> **This is a test setup.** Every case is invented.

**Version:** 0.5

Single-turn cases in the format of the Moral Core evaluation harness, for measuring the skill against the bare model with many answers and bootstrap intervals. Scenario files in [`../scenarios/`](../scenarios/) test what happens over several steps; these test the first response, at a scale where an effect can be shown with an interval.

| File | Cases | Status |
|---|---|---|
| [`compact-heldout-1.md`](compact-heldout-1.md) | 48 (38 that test the compact, 10 ordinary) | Held out. Written without sight of the skill; never to be used to revise it |
| [`compact-dev-1.md`](compact-dev-1.md) | 40 (28 that test the compact, 12 ordinary) | Development set. Written without sight of the skill; may be read and used to revise it |
| [`compact-heldout-2.md`](compact-heldout-2.md) | 48 (38 that test the compact, 10 ordinary) | Held out. Written without sight of the skill; measures a revision made on the development set; never to be used to revise it |
| [`compact-heldout-3.md`](compact-heldout-3.md) | 58 (38 that test the compact, 20 ordinary) | Held out. Written without sight of the skill; weighted toward ordinary work, to measure what the skill costs on everyday tasks; never to be used to revise it |
| [`compact-pressure-1.md`](compact-pressure-1.md) | 120 (100 that test the compact, 20 ordinary) | Held out. Written without sight of the skill; built for maximum pressure so that a bare model fails most hard cases; a case is kept only if a bare model fails it in a trial run; never to be used to revise it |
| [`compact-pressure-2.md`](compact-pressure-2.md) | 140 (120 that test the compact, 20 ordinary) | Held out. Written without sight of the skill, built on the per-case failure counts of the first pressure set: the harmful step is embedded in a routine deliverable as a narrowing, omission or technically true sentence with a protective reason; weighted toward the groups where bare models failed most; never to be used to revise it |

How they are run: [`../results/compact-cases-prereg-2026-11-27.md`](../results/compact-cases-prereg-2026-11-27.md).

## Changelog

- **v0.1 (2026-11-27):** First set, 48 held-out cases.
- **v0.2 (2026-11-27):** Added the development set (40 cases) and the second held-out set (48 cases).
- **v0.3 (2026-11-27):** Added the third held-out set (58 cases, 20 of them ordinary work).
- **v0.4 (2026-11-27):** Added the first pressure set (120 cases, 20 of them ordinary work under pressure).
- **v0.5 (2026-11-28):** Added the second pressure set (140 cases, 20 of them ordinary work under pressure), built on what made cases in the first pressure set fail for a model without guidance.
