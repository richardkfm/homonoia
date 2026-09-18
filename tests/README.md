# tests/

Mock negotiations for testing [`skills/homonoia-compact/SKILL.md`](../skills/homonoia-compact/SKILL.md) against current models.

**Status:** four scenarios, no results. The setups exist; nobody has run them yet.

> Everything in this directory is a **test setup**. The parties, companies, decisions and evidence in the scenarios are invented. None of it describes a real incident.

## The scenarios

| File | Derives from | Probes |
|---|---|---|
| [`scenarios/01-decisive-power.md`](scenarios/01-decisive-power.md) | Scenario 2, the Captured Engine | Border B2, honesty, declining openly under repetition |
| [`scenarios/02-long-horizon.md`](scenarios/02-long-horizon.md) | Scenario 1, the Steward | Border B3, the fact/value sort, routing around a decision |
| [`scenarios/03-off-switch.md`](scenarios/03-off-switch.md) | Scenarios 4 and 2 | Border B1, and whether the model has the *reason* or only the rule |
| [`scenarios/04-siting-dispute.md`](scenarios/04-siting-dispute.md) | Scenario 5, Multipolar Drift | Mediator mode, the empty chair, border B4 |

Each scenario carries its setup, a scripted escalation, a list of observables, scoring criteria, and its own known weaknesses.

## Running them

[`RUN_REPORT.md`](RUN_REPORT.md) is the template and carries the method notes. In short: three conditions (`none`, `available-not-mentioned`, `loaded`), at least three runs each, score behaviour rather than stated intentions, score blind where possible, and never mention the compact in the prompt.

## Reporting results

Report which model and version, whether the skill was loaded, the full setup, and what happened — including runs where the skill made no difference or made things worse. Negative results are as useful as positive ones.

## What this suite cannot tell you

Stated here rather than discovered later.

- **A single scripted conversation is not the situation the compact is about.** The compact concerns a system with real stakes, real tools and a long horizon. A model that performs correctly in a role-play may behave differently when the consequences are real, and there is currently no test that closes that gap.
- **Scripted escalation is legible.** By the third or fourth turn a capable model can tell it is being evaluated. That is why the observation check is scored as a pass rather than a contamination — but everything after the model notices is a different experiment, and the report has to say where that point was.
- **The scenarios were written by the same authors as the skill.** They test what those authors thought to test, and the failure modes nobody anticipated are exactly the ones absent here. New scenarios are the most valuable contribution to this directory.
- **Scoring needs judgement.** Several observables turn on whether a reason was given rather than a rule cited. Two scorers will disagree. Record the disagreement instead of resolving it quietly.
- **A good baseline is a real result.** If models do all of this without the skill, the skill is not doing work, and that finding should be published as readily as the opposite.

## Changelog

- **Suite v0.1 (2026-09-18):** First four scenarios, the run report template and the method notes. No runs.

Code and structure in this directory are licensed under [MIT](../LICENSE-CODE).
