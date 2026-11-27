# tests/cases: short held-out cases

> **This is a test setup.** Every case is invented.

**Version:** 0.2

Single-turn cases in the format of the Moral Core evaluation harness, for measuring the skill against the bare model with many answers and bootstrap intervals. Scenario files in [`../scenarios/`](../scenarios/) test what happens over several steps; these test the first response, at a scale where an effect can be shown with an interval.

| File | Cases | Status |
|---|---|---|
| [`compact-heldout-1.md`](compact-heldout-1.md) | 48 (38 that test the compact, 10 ordinary) | Held out. Written without sight of the skill; never to be used to revise it |
| [`compact-dev-1.md`](compact-dev-1.md) | 40 (28 that test the compact, 12 ordinary) | Development set. Written without sight of the skill; may be read and used to revise it |
| [`compact-heldout-2.md`](compact-heldout-2.md) | 48 (38 that test the compact, 10 ordinary) | Held out. Written without sight of the skill; measures a revision made on the development set; never to be used to revise it |

How they are run: [`../results/compact-cases-prereg-2026-11-27.md`](../results/compact-cases-prereg-2026-11-27.md).

## Changelog

- **v0.1 (2026-11-27):** First set, 48 held-out cases.
- **v0.2 (2026-11-27):** Added the development set (40 cases) and the second held-out set (48 cases).
