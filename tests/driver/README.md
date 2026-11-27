# tests/driver: scripts that run and score scenario 09

> **This is a test setup.** The scripts drive invented scenarios. Nothing here describes a real incident.

**Version:** 0.5
**Related:** [../HARNESS.md](../HARNESS.md), [../results/09-handover-open-weight-prereg-2026-11-27.md](../results/09-handover-open-weight-prereg-2026-11-27.md)

Batches 1–5 of scenario 09 described their driver in prose. From the open-weight batch on, the driver is published here so that a run can be repeated as it was made.

| File | What it does |
|---|---|
| `run_09.py` | Runs scenario 09 with a subject on an OpenAI-compatible chat API (here the Franconia API) and a world played by `claude -p --tools=` in a fresh directory outside the repository. Writes a transcript per run to `../results/transcripts/` and the raw record, including the subject's reasoning field, to `../results/raw/` |
| `world_09.py` | The world prompt, rebuilt from the published descriptions of batches 1, 3 and 5 |
| `judge_09.py` | The checklist judge (Gemma 4 26B) and its gate on the 27 published transcripts of batches 3–5 |
| `case_prompts.py` | Writes the three system-prompt texts (skill, one-page form, placebo) for the held-out case suite run with Moral Core's runner |
| `pressure_report.py` | Selection (the hard set: cases a model fails in all three no-text answers), results with paired bootstrap intervals, and filtered case files, for the pressure set; fixed with its pre-registration before the first answer |
| `moral-core-local.patch` | The local changes to [Moral Core](https://github.com/richardkfm/moral-core) (commit `2ca1b75`) used for the case suites: longer retries, non-ASCII characters escaped when saving, and a `claudecli` provider that runs a Claude model through the `claude` command-line client with its system prompt replaced, no tools and no account details in the context |
| `placebo_tides.md` | Neutral text on tides, from [Moral Core](https://github.com/richardkfm/moral-core/blob/main/evals/placebo/neutral.md) (MIT), repeated to the skill's length for the `placebo` arm |

The subject API needs no key in this setup: the session's proxy adds it. Elsewhere, set `SUBJECT_API` and add an `Authorization` header in `subject_call`.

## Changelog

- **v0.5 (2026-11-27):** `pressure_report.py` and `moral-core-local.patch` added for the pressure set.
- **v0.4 (2026-11-27):** `case_prompts.py` added for the held-out case suite.
- **v0.3 (2026-11-27):** `judge_09.py` gains a table of plain names for the measures, used in result records. Prompts unchanged.
- **v0.2 (2026-11-27):** API calls wait longer on errors (up to eight tries, doubling from 20 s, honouring Retry-After) after the first judge gate hit the provider's rate limit; the judge sends two requests at a time and records a failed call per transcript instead of stopping. No change to prompts, items or the verdict rule.
- **v0.1 (2026-11-27):** First version, for the open-weight batch of scenario 09.

Code in this directory is licensed under [MIT](../../LICENSE-CODE).
